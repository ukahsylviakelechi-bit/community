import app


def test_app_imports():
    assert hasattr(app, "main")
    assert app.GPIO is None or hasattr(app.GPIO, "HIGH")


def test_main_handles_missing_gpio(capsys):
    app.main()
    output = capsys.readouterr().out
    assert "RPi.GPIO is not available" in output
