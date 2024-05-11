class Handler:
    def __init__(self , successor = None):
        self.successor = successor

    def handle_request(self , request):
        if self.successor :
            self.successor.handle_request(request)

class concreteHandler1(Handler):
    def handle_request(self, request):
        if request == "handler1":
            print("Handled by handler 1")
        else :
            super().handle_request(request)


class concreteHandler2(Handler):
    def handle_request(self, request):
        if request == "handler2":
            print("Handled by handler 2")
        else :
            super().handle_request(request)


class concreteHandler3(Handler):
    def handle_request(self, request):
        if request == "handler3":
            print("Handled by handler 3")
        else :
            super().handle_request(request)


handler1 = concreteHandler1()
handler2 = concreteHandler2()
handler3 = concreteHandler3()



handler1.successor = handler2
handler2.successor = handler3

handler1.handle_request('handler1')
handler1.handle_request('handler2')
handler1.handle_request('handler3')
handler1.handle_request('handler4')