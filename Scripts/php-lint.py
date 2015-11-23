#!/usr/bin/env python

# TODO: this fails because STDIN appears to always be blank; WTF? Bug in ShellActions.sugar?

import sys, os, subprocess, urllib, tempfile, re

# Grab our file contents
fileContents = sys.stdin.read()
# Create a temporary file (this is necessary in case there are unsaved changes)
tempFile = tempfile.NamedTemporaryFile(mode='w+')
tempFile.write(fileContents)
tempFile.flush()
os.fsync(tempFile.fileno())

# Grab our path information
filePath = os.environ['EDITOR_PATH']
fileName = os.path.basename(filePath)
rootPath = os.environ['EDITOR_PROJECT_PATH']
if rootPath == '':
	rootPath = os.path.dirname(filePath)

# Compose and execute our lint command
command = ['/usr/bin/php', '-l', tempFile.name]
result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.path.dirname(filePath))
output, error = result.communicate()

# Save our tempFile's base name (need to replace it with the actual file name in the output)
tempName = tempFile.name

# Close our file (causes it to be automatically removed)
tempFile.close()

htmlOutput = '''<!DOCTYPE HTML>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<title>PHP Lint Output</title>
	<link rel="stylesheet" href="Support/styles.css" />
</head>
<body><div id="page">
	<h1>Syntax check results for "'''

htmlOutput += fileName + '"</h1>\n'

# Replace all instances of the temp file name with the actual file name
output = output.replace(tempName, fileName)

# Replace any line numbers with links
output = re.sub(r'line (\d+)', r'<a href="x-espresso://open?filepath=' + urllib.quote(filePath) + r'&lines=\1">line \1</a>', output)

# Build out our HTML
errParseIndex = output.find('Errors parsing')
if errParseIndex > -1:
	htmlOutput += '<h2 class="errors">' + output[errParseIndex:] + '</h2>\n'
	htmlOutput += '<p>' + output[0:errParseIndex] + '</p>\n'
elif output.find('No syntax errors detected') > -1:
	htmlOutput += '<h2 class="success">' + output + '</h2>\n'
else:
	htmlOutput += '<p>' + output.replace('\n', '<br/>')

htmlOutput += '</div></body></html>'

# Output our HTML
sys.stdout.write(htmlOutput)
