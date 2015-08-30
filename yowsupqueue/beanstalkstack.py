from pystalkd.Beanstalkd import Connection
import json
import threading
import sys
import traceback


class BeanstalkStack(threading.Thread):
    def setConnectParams(self, host, port):
        self.host = host
        self.port = port

    def setStack(self, stack):
        self.stack = stack
    def run(self):
        self.beanstalk = Connection(host=self.host, port=int(self.port))
        self.beanstalk.watch('whatsapp-send')
        while 1:
            job = self.beanstalk.reserve()
            try:
                messageBody = str(job.body)
                message = json.loads(messageBody)
                if message["type"] == "simple":
                    print(messageBody)
                    self.stack.sendMessage(message["address"], message["body"])
                else:
                    raise Exception("Unrecognized Message: %s" % message)
                print("Sucessfully sended Message")
                job.delete()

            except Exception as e:
                job.bury()
                traceback.print_exc()

    def sendMessage(self, message):
        #self.beanstalk.use("whatsapp-receive")
        #if type(message) is not str:
        #    message = json.dumps(message)
        #self.beanstalk.put(message)
        pass
