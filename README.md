# PHPLint.sugar

PHP syntax checking for Espresso 2, using `php -l`.

## Installation

**Requires Espresso 2.2** and the **ShellActions.sugar**

1. Follow the instructions to install the [ShellActions.sugar](https://github.com/onecrayon/ShellActions-sugar) (if you have not already previously done so)
2. [Download PHPLint.sugar](http://onecrayon.com/downloads/PHPLint.sugar.zip)
3. Decompress the zip file (your browser might do this for you)
4. Double click the Sugar to install it

Optionally, you can clone it from GitHub for easier updating:

    cd ~/Library/Application\ Support/Espresso/Plug-Ins
    git clone git://github.com/onecrayon/PHPLint.sugar.git

Relaunch Espresso, and a new PHPLint submenu will be available in your Actions menu. You can then update the Sugar when necessary by running the following command:

    cd ~/Library/Application\ Support/Espresso/Plug-Ins/PHPLint.sugar
    git pull

## Available actions

PHPLint.sugar includes the following action:

* **Check Syntax**: Checks the frontmost document for syntax errors using PHP's built-in "lint" option. Note that this does not execute the file, so runtime errors will remain undetected.

## Development

PHPLint.sugar is written entirely in XML and Python using ShellAction.sugar's built-in HTML outputting! For linking to errors, it uses a special `x-espresso://` URL scheme that is new in Espresso 2.2.

To discover how I'm doing things or tweak its behavior to fit your own needs, right click the Sugar in the Finder and choose Show Package Contents or fork this project and go to town.

You can also [email me](http://onecrayon.com/about/contact/) if you have any feedback, requests, or run across any problems.

## Changelog

**1.0**:

* Initial release

## Licensing

Copyright (c) 2015 Ian Beck, and published under the MIT license

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
