from socketserver import TCPServer, BaseRequestHandler

from guess_game import GuessGame, Result


class TCPHandler(BaseRequestHandler):
    def __sendall(self, msg: str):
        self.request.sendall(msg.encode("utf-8"))

    def setup(self):
        print("Starting a new connection...")

    def finish(self):
        print("Dropping connection...")

    def handle(self):
        game = GuessGame()
        while True:
            data = str(self.request.recv(1024), "utf-8")
            try:
                command, arg, *_ = data.split(" ")
            except ValueError:
                self.__sendall("Принимается только команда guess <number>")
                continue

            if command != "guess":
                self.__sendall("Принимается только команда guess <number>")
                continue

            try:
                number = int(arg)
            except ValueError:
                self.__sendall("Нужно ввести число! Как тут: guess <number>")
                continue

            res = game.guess(number)
            self.__sendall(res.value)
            if res == Result.CORRECT:
                game.restart()


HOST, PORT = "localhost", 8000
with TCPServer((HOST, PORT), TCPHandler) as server:
    server.serve_forever()
