from rx import create
from rx.core.observer import Observer


def push_hello_world(observer, scheduler):
    observer.on_next("hello")
    observer.on_next("world")
    # observer.on_error("error")
    observer.on_completed()


class PrintObserver(Observer):
    def on_next(self, value):
        print("Received {}".format(value))

    def on_complete(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {}".format(error))


def main():
    source = create(push_hello_world)
    source.subscribe(PrintObserver())
