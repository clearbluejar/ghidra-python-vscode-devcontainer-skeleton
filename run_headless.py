import os
import subprocess

# env vars from launch.json 
ghidraHeadless = os.getenv('GHIDRA_HEADLESS')
projectPath = os.getenv('PROJECT_PATH')
projectName = os.getenv('PROJECT_NAME')
binary = os.path.basename(os.getenv('BINARY'))
script =  os.getenv('HEADLESS_SCRIPT')
properties = script.split('.')[0] + '.properties'
properties_template = '''program={program}'''


# Arguments to pass to Ghidra

# PdbSymbolServerExamplePrescript.java - configures symbol server
args = [ghidraHeadless, projectPath, projectName, "-postscript", script]

print(args)

with open(properties, 'w') as f:
    f.write(properties_template.format(program=binary))

with open(properties, 'r') as f:
    print(f.read())

subprocess.run(args)



