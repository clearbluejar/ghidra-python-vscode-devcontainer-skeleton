import os
import subprocess

GHIDRA_HEADLESS = '/ghidra/support/analyzeHeadless'
PROJECT_NAME = 'sample_pyhidra'
PROJECT_LOCATION = '.ghidra_projects'
PROJECT_PATH = os.path.join(PROJECT_LOCATION, PROJECT_NAME)

SCRIPT = 'sample.py'
BINARY = "ls"

# Create Properties File to pass arguments to script
PROPERTIES_PATH = os.path.basename(SCRIPT).strip('.py') + '.properties'
PROPERTIES_TEMPLATE = '''program={BINARY}'''

with open(PROPERTIES_PATH, 'w') as f:
    f.write(PROPERTIES_TEMPLATE.format(BINARY=BINARY))

# Arguments for Ghidra's Headless Analyzer
args = [GHIDRA_HEADLESS, PROJECT_PATH, PROJECT_NAME, "-postscript", SCRIPT]

print(args)
print(PROPERTIES_TEMPLATE.format(BINARY=BINARY))

subprocess.run(args)
