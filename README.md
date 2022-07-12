# ghidra-python-vscode-devcontainer-skeleton

A simple template repo to provide a VScode Ghidra python scripting environment.

## About

This version is an upgrade for the old one. Upgrade because with `vscode` devcontainers, everything can just work. Don't beleieve me? Try it.



## Features

- Container setup and ready in .devcontainer 
    - Leverages standard [python3](https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3) devcontainer image with Java [feature](.devcontainer/devcontainer.json) available.  
    - Downloads latest of specified Ghidra based on GHIDRA_VERSION in devcontainer.json
- Prescribes workflow to get you started (easily modified)
- Auto complete for Ghidra Python script
    - via pyi typings from [VDOO-Connected-Trust/ghidra-pyi-generator](https://github.com/VDOO-Connected-Trust/ghidra-pyi-generator)

## Workflow

Ghidra is a binary analysis tool (and much more). In order to do something useful, you need to create a project and add binaries. Once a project exists with at least one binary added, headless analysis can begin. 

1. [Create Ghidra Project](.vscode/tasks.json)
2. [Import binary to project](.vscode/tasks.json)
3. [Run script on binary](run_headless.py)
   - Sample Script - [sample.py](sample.py)

## Dev Container Setup (Best Option)

If you haven't tried [developing inside a container](https://code.visualstudio.com/docs/remote/containers#_getting-started) with vscode, you should.

> "One of the useful things about developing in a container is that you can use specific versions of dependencies that your application needs without impacting your local development environment. " [Get started with development Containers in Visual Studio Code](https://code.visualstudio.com/docs/remote/containers-tutorial)

- [Developing inside a Container using Visual Studio Code Remote Development](https://code.visualstudio.com/docs/remote/containers)




On first run, it will build a fast [debian image] with the python and java dependenices needed for Ghidra scripting. Then it will download Ghidra based on your settings in [devcontainer.json](.devcontainer/devcontainer.json) using [post-create.sh](.devcontainer/post-create.sh)

If you aren't using the dev container, you will need to use the [manual setup](#manual-setup-alternative-painful-option)


</details>

## Ways to run headless script

1. The most straightforward means to run the script it to hit run via launch on [run_headless.py](run_headless.py). It simply uses subprocess module with the correct arguments to run the sample script. 
2. Another way is to run the script directly by using the `Run Current Python Script in Ghidra Jython` task within[tasks.json](.vscode/tasks.json).  To use this task make sure you have open and focused the [sample.py](sample.py).


## Ghidra Headless Scripting Hangups 

1. Ghidra runs Jython, not actually python. Limited to python 2.7 features. 
2. In order to supply arguments to calls like [askProgram](https://ghidra.re/ghidra_docs/api/ghidra/app/script/GhidraScript.html#askProgram(java.lang.String)) (which sets the current program being analyzed), a properties file needs to be provided with the same name and location as the script being run. In this case [sample.properties](sample.properties) and [sample.py](sample.py).
