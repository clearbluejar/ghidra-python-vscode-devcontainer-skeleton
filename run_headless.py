import os
import subprocess

# env vars from launch.json 
ghidraHeadless = os.getenv('GHIDRA_HEADLESS')
projectPath = os.getenv('PROJECT_PATH')
projectName = os.getenv('PROJECT_NAME')
script =  os.getenv('HEADLESS_SCRIPT')
properties = os.path.basename(script).strip('.py') + '.properties'
properties_template = '''program={program}'''
binary= "ls"

# Arguments for Ghidra's Headless Analyzer
args = [ghidraHeadless, projectPath, projectName, "-postscript", script]

print(args)

with open(properties, 'w') as f:
    f.write(properties_template.format(program=binary))

with open(properties, 'r') as f:
    print(f.read())

subprocess.run(args)
