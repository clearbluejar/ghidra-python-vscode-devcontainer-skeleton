import os
import subprocess

# env vars from launch.json 
ghidraHeadless = os.getenv('GHIDRA_HEADLESS')
projectPath = os.getenv('PROJECT_PATH')
projectName = os.getenv('PROJECT_NAME')
script =  os.getenv('HEADLESS_SCRIPT')
properties = os.path.basename(script).strip('.py') + '.properties'
binary= "/bin/ls"

# Arguments for Ghidra's Headless Analyzer
args = [ghidraHeadless, projectPath, projectName, "-import", binary, "-overwrite"]

print(args)

subprocess.run(args)