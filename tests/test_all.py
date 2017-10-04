from denv import main


def test_all():
    command_line = ['python', '-c', """'import os;assert os.environ["foo"]=="bar"'"""]
    env_file_lines = ["foo=bar"]
    try:
        main(command_line, env_file_lines)
    except SystemExit as e:
        # check that python has asserted on the env_var foo equalling bar
        assert e.code == 0