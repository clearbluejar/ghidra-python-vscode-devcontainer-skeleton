import os
import subprocess

# Env vars from launch.json
GHIDRA_HEADLESS = '/ghidra/support/analyzeHeadless'
PROJECT_NAME = 'sample_pyhidra'
PROJECT_LOCATION = '.ghidra_projects'
PROJECT_PATH = os.path.join(PROJECT_LOCATION, PROJECT_NAME)

# Project Path Needs to exist
if not os.path.exists(PROJECT_PATH):
    os.mkdir(PROJECT_PATH)

BINARY_PATH = "/bin/ls"

# Arguments for Ghidra's Headless Analyzer
args = [GHIDRA_HEADLESS, PROJECT_PATH, PROJECT_NAME, "-import", BINARY_PATH, "-overwrite"]

print(args)

subprocess.run(args)
