# Typer-oo-example

This is answer to question from [typer issue 261](
https://github.com/tiangolo/typer/issues/261
).

# Getting started.

### Poetry

```shell
poetry install
```

### pip

```shell
pip install -r requirements.txt
```

# Run.

### Modules including `click` in the name:

Given name of the module `something_click_else`:

```shell
python -m something_click_else
```

### Module `typer_example`:

```shell
python -m typer_example
```

# Content:

## click_example
Example from [this post](
https://github.com/tiangolo/typer/issues/261#issuecomment-819174185
) with additions to make the script able to execute.
#### Command

```shell
python -m click_example
```

## click_to_typer

* AbstractBaseClass that uses static methods to declare commands.
* Wrapper around `app.commmand()(lambda x: "my function")`

#### Command

```shell
python -m click_to_typer
```

## config_click_to_typer

* Usage of `self` attribute to expose some data.

#### Command

```shell
python -m config_click_to_typer
```

## click_to_many_typers

* registering two typers.

#### Command

```shell
python -m click_to_many_typers
```

## many_typers_extended

* registering two typers.
* extract PapaTyper to avoid import conflicts.
* extending `classic` with custom static methods.
* extending `angry` command with usage of `self` and typer `context`.
* Add subcommand group `sub` for `angry` command.
* Helper for registering commands.

#### Command

```shell
python -m many_typers_extended
```

## instance_app

* This extends `click_to_many_typers`.
* Have in mind this example has a bug and does not work correctly.
* This uses `typer.app` as class variable. It is created when class is declared.
  Creating `self. app` in `__init__` creates `app` for each instance of the class in the opposition
  to this example, where `app` is created once for all class instances.

```python
import typer 
import abc

class BaseModule(abc.ABC):
    app = typer.Typer()

```

The behaviour is incorrect: `angry` commands are overwritten by `classic` command. To check run:

```shell
python -m instance_app classic hello Mike
```

```shell
python -m instance_app angry hello Mike
```

You can see the message is the same. `YourModule` overwritten behaviour described in `AngryModule`

#### Command

```shell
python -m instance_app
```

## typer_example

#### Command

* Modified code from original question to the state the user goes through designed path.

```shell
python -m typer_example
```
