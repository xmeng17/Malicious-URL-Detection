import requests
import threading
import WhoisParser


# Multithreads programming.
# This class is a worker thread that will be started by main thread.
class WhoisWorker(threading.Thread):
    def __init__(self, thread_ID, queue, proxy_arr, console_logger, result_logger, conn_timeout=3, read_timeout=5, max_attempt=2):
        threading.Thread.__init__(self)
        self.thread_id = thread_ID
        self.queue = queue
        self.parser=WhoisParser.WhoisParser()
        self.console_logger = console_logger
        self.result_logger = result_logger
        self.proxy_arr = proxy_arr
        self.conn_timeout = conn_timeout  # connection timeout
        self.read_timeout = read_timeout  # response read timeout
        self.max_attempt = max_attempt
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0'}


    def step(self, i, url, proxy_index):
        try:
            # read http://docs.python-requests.org/en/master/
            # read http://docs.python-requests.org/zh_CN/latest/user/advanced.html
            response = requests.get(url, verify=False, headers=self.headers,
                                    timeout=(self.conn_timeout, self.read_timeout),
                                    proxies=self.proxy_arr[proxy_index])
            if response.status_code >= 400:
                self.console_logger.error('      Get bad request %d' % i)
                return False
            else:
                texts = response.text  # load contents in blocking mode
                self.console_logger.debug('Success loading %d, thread %d proxy index %d' % (i, self.thread_id, proxy_index))
                num_ip, reg_time, country, registrar = self.parser.parse(texts)
                self.result_logger.debug(u'%s:%d,%s,%s,%s'%(url, num_ip, reg_time, country, registrar))
                return True
        except Exception as e:
            self.console_logger.error('      Error loading %d, thread %d, proxy index %d' % (i, self.thread_id, proxy_index))
            self.console_logger.error('         %s'%str(e))
            return False

    def run(self):
        proxy_index = 0
        while True:
            i,url = self.queue.get()
            #self.logger.debug("start " + url)
            attempt=0
            while not self.step(i, url, proxy_index):
                attempt += 1
                if attempt>self.max_attempt:
                    proxy_index+=1
                    if proxy_index >= len(self.proxy_arr):
                        proxy_index = 0
                elif attempt>10:
                    self.console_logger.error('      Attempted %d times for url:%s'%(attempt,url))
            # Send signal to the queue that the worker thread
            #  has finished one task.
            self.queue.task_done()


