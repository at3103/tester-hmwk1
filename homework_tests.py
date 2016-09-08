import os

import tester


GENERAL_ERROR = "[eE]rror:.*"


t = tester.HomeworkTester()

"""Modify this file with your tests.

The test is already filled out with some basic tests.

Basically, your main usage is:

	t.add_test("command to execute 1", "expected output as a regex string")
	t.add_test("command to execute 2", "expected output as a regex string")
	...
	t.add_test("command to execute 3", "expected output as a regex string")
	t.run()
	t.print_results()
	t.reset()
"""


##################### Basic Executables #########################
# ls should not be found
t.add_test("ls", GENERAL_ERROR)

# But /bin/echo should work
t.add_test("/bin/echo hello world", "hello world")
t.run()
t.print_results()
t.reset()

############################# Builtins ##########################
# Test that cd works
t.add_test("cd /tmp", "")
t.add_test("/bin/pwd", "/tmp")
t.add_test("cd /var", "")
t.add_test("/bin/pwd", "/var")
t.run()
t.print_results()
t.reset()

# Test that history works as expected
t.add_test("history", "0 history")
t.add_test("history -c", "")
t.add_test("abc abc", GENERAL_ERROR)
t.add_test("def", GENERAL_ERROR)
expected_output = [
    "0 abc abc",
    "1 def",
    "2 history"
]
t.add_test("history", "\n".join(expected_output))
t.add_test("history -c", "")
t.add_test("history", "0 history")
t.add_test("/bin/echo hello", "hello")
t.add_test("history 1", "hello")
t.run()
t.print_results()
t.reset()

############################# Pipes #############################
t.add_test("/bin/echo hello world | /bin/grep hello", "hello world")
t.add_test("/bin/echo blah          |/usr/bin/cut -b 3,4", "ah")
t.run()
t.print_results()
t.reset()

t.add_test("blah", GENERAL_ERROR)
t.add_test("history | /bin/grep blah", "0 blah\n1 history | /bin/grep blah")
t.run()
t.print_results()
t.reset()
