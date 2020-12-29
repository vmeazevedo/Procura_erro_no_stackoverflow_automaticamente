# Simple automatic error search algorithm on the Stackoverflow website
Simple algorithm using the webbrowser and logging libraries to search for any errors on the stackoverflow website automatically.

# Requirements
You will need to install the library below:

- webbrowser

# Basic operation

I used try / except normally to simulate an error and threw the error string into any variable using the logging library.
Then, inside the exception, I used the web browser library to perform the error search directly on the stackoverflow website.
