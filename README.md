# fbs-sample
Sample project for creating cross-platform desktop appications with
[fbs](https://github.com/mherrmann/fbs)

## Getting Started
This example should work on Windows, Mac and Ubuntu. You need Python 3.5.
(Higher versions may work as well, but are not officially supported.)

Clone this repository and `cd` into it:

    git clone https://github.com/mherrmann/fbs-sample
    cd fbs-sample

Create a virtual environment:

    python3 -m venv venv

Activate the virtual environment:

    # On Mac/Linux:
    source venv/bin/activate
    # On Windows:
    call venv\scripts\activate.bat

Install the required libraries (most notably, `fbs` and `PyQt5`):

    pip install -r requirements.txt

Run the sample app:

    python -m fbs run

This shows a (admittedly not very exciting) window:

![Screenshot of sample app](screenshot.png)

To compile the app to a standalone executable:

    python -m fbs freeze

This produces the folder `target/app`. You can copy this folder to any other
computer (with the same OS as yours) and run your app there. Isn't that awesome?

## The source code
The source code for the above app is in [`src/main/python`](src/main/python).
It contains a [`main.py` script](src/main/python/sample/main.py), which serves
as the entry point for the application. This script instantiates and then runs
an _application context_. This is defined in
[`application_context.py`](src/main/python/sample/application_context.py).

Your apps should follow the same structure:

 * Create a subclass of `fbs_runtime.application_context.ApplicationContext`.
 * Define a `run()` method that ends with `return self.app.exec_()`.
 * Use `cached_property` to define the objects of your app.
 * In your `main` script, instantiate your application context, invoke its
   `run()` method and pass the return value to `sys.exit(...)`.

Subclassing `ApplicationContext` may seem complicated at first. But it has
several advantages: First, it lets `fbs` define useful default behaviour (such
as setting the [app icon](src/main/icons) or letting you access resources files
bundled with your app). Also, as your application becomes more complex, you will
find that an application context is extremely useful for "wiring together" the
various Python objects that make up your app. The next section demonstrates both
of these advantages.

## A more complicated example
Take a look at
[`application_context_2.py`](src/main/python/sample/application_context_2.py).
It defines a new `@cached_property`:

```python
class AppContext(ApplicationContext):
    ...
    @cached_property
    def image(self):
        return QPixmap(self.get_resource('success.jpg'))```

A `@cached_property` is simply a Python `@property` whose value is cached.
Here's how it is used:

```python
class AppContext(ApplicationContext):
    ...
    @cached_property
    def main_window(self):
        ...
        image_container.setPixmap(self.image)```

The first time `self.image` is accessed, the `return QPixmap(...)` code is
executed. After that, the value is cached and returned without executing the
code again.

This behaviour makes `@cached_property` very useful for instantiating and
connecting the Python objects that make up your application. For each component,
define a `@cached_property`. If it requires other objects, simply access them as
properties, similarly to `self.image` above. The fact that all parts of your
application live in one place (the application context) makes it extremely easy
to manage them and see what is needed where.

To see the above example in action, change the line

```python
from sample.application_context import AppContext```

in your copy of [`main.py`](src/main/python/sample/main.py) to

```python
from sample.application_context_2 import AppContext```

Then, run `python -m fbs run`. You will be rewarded ;-)

### Resources
Another feature of our new example was the call `self.get_resource(...)`.
It loads an image that lives in the folder
[`src/main/resources`](src/main/resources).
But what if your user is running the compiled form of your app? In that case,
the directory structure is completely different.

The short answer is that `get_resource(...)` is clever enough to determine if it
is running from source, or from the compiled form of your app. To ensure that
the image is in fact distributed alongside your application, `fbs` copies all
files from `src/main/resources` into the `target/app` folder. So, if you have
data files that you want to include, such as images, `.qss` style sheets (Qt's
equivalent of `.css` files) and many others, place them in `src/main/resources`.

### Different OSs
Often, you will want to use different versions of a resource file depending on
the operating system your app is currently running on. A typical example of this
are `.qss` files where you modify your app's style to match the current OS.
(In fact, multiple `.qss` files are often also necessary for maintaining the
_same_ appearance, because of small differences in Qt's rendering engine.)

The solution for this is that `get_resource('file.txt')` first looks for a
platform-specific version of `file.txt`. Depending on your current OS, it
searches the following locations:

 * `src/main/resources/windows`
 * `src/main/resources/mac`
 * `src/main/resources/linux`

If it can't find `file.txt` in any of these folders, it falls back to
`src/main/resources/base`.