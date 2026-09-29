import click


def test_choice_get_invalid_choice_message():
    choice = click.Choice(["a", "b", "c"])
    message = choice.get_invalid_choice_message("d", ctx=None)
    assert message == "'d' is not one of 'a', 'b', 'c'."


def test_choice_did_you_mean_single_suggestion():
    choice = click.Choice(["apple", "banana", "cherry"])
    message = choice.get_invalid_choice_message("aple", ctx=None)
    assert message == (
        "'aple' is not one of 'apple', 'banana', 'cherry'. Did you mean 'apple'?"
    )


def test_choice_did_you_mean_several_suggestions():
    choice = click.Choice(["read", "ready", "reap"])
    message = choice.get_invalid_choice_message("rea", ctx=None)
    assert message == (
        "'rea' is not one of 'read', 'ready', 'reap'."
        " (Did you mean one of: 'read', 'ready', 'reap'?)"
    )


def test_choice_did_you_mean_case_insensitive():
    choice = click.Choice(["Apple", "Banana"], case_sensitive=False)
    message = choice.get_invalid_choice_message("APLE", ctx=None)
    assert message == "'APLE' is not one of 'apple', 'banana'. Did you mean 'apple'?"


def test_choice_did_you_mean_no_suggestion():
    choice = click.Choice(["foo", "bar", "baz"])
    message = choice.get_invalid_choice_message("meh", ctx=None)
    assert message == "'meh' is not one of 'foo', 'bar', 'baz'."
