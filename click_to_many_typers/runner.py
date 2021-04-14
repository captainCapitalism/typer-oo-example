import typer

from click_to_many_typers.base_module import BaseModule, PapaTyper


class AngryModule(BaseModule):
    @staticmethod
    def hello(name: str):
        typer.echo(f"Hello very much, {name}")

    @staticmethod
    def goodbye(name: str):
        typer.echo(f"Goodbye very much, {name}")


class YourModule(BaseModule):
    @staticmethod
    def hello(name: str):
        typer.echo(f"Greetings chap! If I recall correctly you are named {name}")

    @staticmethod
    def goodbye(name: str):
        typer.echo(f'See you later, {name}')


my_typers = [
    ("angry", AngryModule()),
    ("classic", YourModule()),
]

PapaTyper(my_typers).run()
