# test_hello.py

def test_print_output(capsys):
    # Run the code
    exec(open('hello_code.p').read())

    # Capture stdout
    captured = capsys.readouterr()

    # Check if the output matches the expected value
    assert captured.out == "Hello world! Hello sun!! Hello sky!!!\n"


