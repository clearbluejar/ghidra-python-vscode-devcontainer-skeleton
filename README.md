# ghidra-python-vscode-devcontainer-skeleton

A simple template repo to provide a VScode Ghidra python scripting environment.

## About

If you haven't tried [developing inside a container](https://code.visualstudio.com/docs/remote/containers#_getting-started) with vscode, you should. 

> "One of the useful things about developing in a container is that you can use specific versions of dependencies that your application needs without impacting your local development environment. " [Get started with development Containers in Visual Studio Code](https://code.visualstudio.com/docs/remote/containers-tutorial)

- [Developing inside a Container using Visual Studio Code Remote Development](https://code.visualstudio.com/docs/remote/containers)

This version is an upgrade from the old [ghidra-python-vscode-skeleton](https://github.com/clearbluejar/ghidra-python-vscode-skeleton). Upgraded via the power of  `vscode` devcontainers. Everything just works. Don't beleieve me? Try it.

> insert cool animated gif here

This can still work without devcontainers, but will need to follow the [manual setup](#manual-setup-less-good-option).

## Features

- Container dependencies captured in [.devcontainer](.devcontainer/)
    - Leverages [vscode python3 devcontainer image](https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3)  with Java [feature](.devcontainer/devcontainer.json#L65) added for running Ghidra  
    - Provisions specified versions Ghidra based on `GHIDRA_VERSION` in [devcontainer.json](..devcontainer/devcontainer.json#L16)
- Prescribes workflow to get you started (modify as needed)
- Auto complete for Ghidra Python script
    - via pyi typings from [VDOO-Connected-Trust/ghidra-pyi-generator](https://github.com/VDOO-Connected-Trust/ghidra-pyi-generator)
- ~~IDE debugging via [ghidra_bridge](https://github.com/justfoxing/ghidra_bridge)~~
  - May add this later. It works, just slow for most of my applications. Create an issue if you really want to see this. 

## Workflow

[Ghidra](https://github.com/NationalSecurityAgency/ghidra) is a binary analysis tool (and much more). In order to do something useful, you need to create a project and add binaries. Once a project exists with at least one binary added, headless analysis (scripting Ghidra) can begin. 

### Usage 

The basic usage for the headless analyzer in Ghidra is:
``` 
analyzeHeadless <project_location> <project_name> [[-import [<directory>|<file>]+] | [-process [<project_file>]]] [-postScript <ScriptName>]
```
Full usage:
<details>
<summary>analyzeHeadless full usage</summary>

```bash
analyzeHeadless <project_location> <project_name>[/<folder_path>]
        | ghidra://<server>[:<port>]/<repository_name>[/<folder_path>]
    [[-import [<directory>|<file>]+] | [-process [<project_file>]]]
    [-preScript <ScriptName>]
    [-postScript <ScriptName>]
    [-scriptPath "<path1>[;<path2>...]"]
    [-propertiesPath "<path1>[;<path2>...]"]
    [-scriptlog <path to script log file>]
    [-log <path to log file>]
    [-overwrite]
    [-recursive]
    [-readOnly]
    [-deleteProject]
    [-noanalysis]
    [-processor <languageID>]
    [-cspec <compilerSpecID>]
    [-analysisTimeoutPerFile <timeout in seconds>]
    [-keystore <KeystorePath>]
    [-connect <userID>]
    [-p]
    [-commit ["<comment>"]]
    [-okToDelete]
    [-max-cpu <max cpu cores to use>]
    [-loader <desired loader name>]
```
</details>

This skeleton project prescibes a workflow to teach a workflow that can easily be modified to suit your needs. 

### Steps
1. [Create Ghidra Project](import_bins.py) 
2. [Import binary to project](import_bins.py)
3. [Analyze Binary](import_bins.py)
4. [Run script on binary](run_headless.py)
   - Sample Script - [sample.py](sample.py)

Steps 1,2, and 3 are combined in a single call to `analyzeHeadless`. This single call will create a project, import a binary (or binaries with multiple `-import`s), and analyze the binary.

`analyzeHeadless .ghidra_projects/sample_project sample_project -import /bin/ls` 

Step 4 runs the script on the imported binary after (*-postscript*) analysis on a subequent call to `analyzeHeadless` with your [sample.py](sample.py). 

`analyzeHeadless .ghidra_projects/sample_project sample_project -postscript sample.py`

## Dev Container Setup (Best Option)

On first run, it will build a fast [debian image] with the python and java dependenices needed for Ghidra scripting. Then it will download Ghidra based on your settings in [devcontainer.json](.devcontainer/devcontainer.json) using [post-create.sh](.devcontainer/post-create.sh)

If you aren't using the devcontainer, you will need to use the manual setup:

## Manual Setup (Less Good Option)

1. [Install Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases) yourself.
2. Update `GHIDRA_INSTALL_DIR` in [settings.json] with your path. 
3. Set environment veriable with `GHIDRA_VERSION`
   - `export GHIDRA_VERSION=10.1.4`
4. Install `ghidra-stubs` that match your `GHIDRA_VERSION`
   - something like 
     - `pip install https://github.com/clearbluejar/ghidra-pyi-generator/releases/download/v1.0.3-10.1.4/ghidra_stubs-10.1.4.refs_heads_master-py2.py3-none-any.whl`
     - or `pip install ghidra-stubs` from pypi, but this is an old version

## Different Ways to run a Ghidra Headless script

1. The most straightforward means to run the script it to hit run via launch on [run_headless.py](run_headless.py). It simply uses subprocess module with the correct arguments to run the sample script. 
2. Another way is to run the script directly by using the `Run Current Python Script in Ghidra Jython` task within [tasks.json](.vscode/tasks.json).  To use this task make sure you have open and focused the [sample.py](sample.py).
3. The 3rd way is to run [sample.py](sample.py) directly in Ghidra after copying it to the `ghidra_scripts` directory. If you are doing that, you likely don't need this repo. 

### Sample Outputs

<details><summary>1. run_headless.py sample.py Output</summary>

```bash
(.env) vscode ➜ /workspaces/ghidra-python-vscode-devcontainer-skeleton (main ✗) $  ghidra-python-vscode-devcontainer-skeleton/run_headless.py 

['/ghidra/support/analyzeHeadless', '/workspaces/ghidra-python-vscode-devcontainer-skeleton/.ghidra_projects/sample_project', 'sample_project', '-postscript', 'sample.py']

program=ls

openjdk version "11.0.15" 2022-04-19 LTS
OpenJDK Runtime Environment Microsoft-32930 (build 11.0.15+10-LTS)
OpenJDK 64-Bit Server VM Microsoft-32930 (build 11.0.15+10-LTS, mixed mode)
INFO  Using log config file: jar:file:/ghidra/Ghidra/Framework/Generic/lib/Generic.jar!/generic.log4j.xml (LoggingInitialization)  
INFO  Using log file: /home/vscode/.ghidra/.ghidra_10.1.4_PUBLIC/application.log (LoggingInitialization)  
INFO  Loading user preferences: /home/vscode/.ghidra/.ghidra_10.1.4_PUBLIC/preferences (Preferences)  
INFO  Class search complete (1006 ms) (ClassSearcher)  
INFO  Initializing SSL Context (SSLContextInitializer)  
INFO  Initializing Random Number Generator... (SecureRandomFactory)  
INFO  Random Number Generator initialization complete: NativePRNGNonBlocking (SecureRandomFactory)  
INFO  Trust manager disabled, cacerts have not been set (ApplicationTrustManagerFactory)  
WARN  Neither the -import parameter nor the -process parameter was specified; therefore, the specified prescripts and/or postscripts will be executed without any type of program context. (HeadlessAnalyzer)  
INFO  HEADLESS Script Paths:
    /ghidra/Ghidra/Features/Decompiler/ghidra_scripts
    /ghidra/Ghidra/Features/Base/ghidra_scripts
    /ghidra/Ghidra/Features/BytePatterns/ghidra_scripts
    /ghidra/Ghidra/Processors/8051/ghidra_scripts
    /ghidra/Ghidra/Features/Python/ghidra_scripts
    /ghidra/Ghidra/Debug/Debugger/ghidra_scripts
    /ghidra/Ghidra/Features/FileFormats/ghidra_scripts
    /ghidra/Ghidra/Processors/PIC/ghidra_scripts
    /ghidra/Ghidra/Processors/DATA/ghidra_scripts
    /ghidra/Ghidra/Debug/Debugger-agent-dbgmodel-traceloader/ghidra_scripts
    /ghidra/Ghidra/Features/VersionTracking/ghidra_scripts
    /ghidra/Ghidra/Features/FunctionID/ghidra_scripts
    /ghidra/Ghidra/Features/GnuDemangler/ghidra_scripts
    /ghidra/Ghidra/Features/MicrosoftCodeAnalyzer/ghidra_scripts (HeadlessAnalyzer)  
INFO  HEADLESS: execution starts (HeadlessAnalyzer)  
INFO  Opening existing project: /workspaces/ghidra-python-vscode-devcontainer-skeleton/.ghidra_projects/sample_project/sample_project (HeadlessAnalyzer)  
INFO  Opening project: /workspaces/ghidra-python-vscode-devcontainer-skeleton/.ghidra_projects/sample_project/sample_project (HeadlessProject)  
INFO  SCRIPT: /workspaces/ghidra-python-vscode-devcontainer-skeleton/sample.py (HeadlessAnalyzer)  
INFO  Reading script properties file: /workspaces/ghidra-python-vscode-devcontainer-skeleton/sample.properties (GhidraScriptProperties)  
sample_project
ghidra.framework.data.ProjectFileManager@60a907d9
sample_project:/
Program Info:
Program: ls: AARCH64:LE:64:v8A_default (Wed Jul 13 12:59:48 UTC 2022)

Memory layout:
Imagebase: 0x100000L
segment_2.1 [start: 0x1048576, end: 0x1049143]
.interp [start: 0x1049144, end: 0x1049170]
.note.gnu.build-id [start: 0x1049172, end: 0x1049207]
.note.ABI-tag [start: 0x1049208, end: 0x1049239]
.gnu.hash [start: 0x1049240, end: 0x1049303]
.dynsym [start: 0x1049304, end: 0x1052423]
.dynstr [start: 0x1052424, end: 0x1053877]
.gnu.version [start: 0x1053878, end: 0x1054137]
.gnu.version_r [start: 0x1054144, end: 0x1054255]
.rela.dyn [start: 0x1054256, end: 0x1060087]
.rela.plt [start: 0x1060088, end: 0x1062703]
.init [start: 0x1062704, end: 0x1062723]
.plt [start: 0x1062736, end: 0x1064511]
.text [start: 0x1064512, end: 0x1149231]
.fini [start: 0x1149232, end: 0x1149247]
.rodata [start: 0x1149248, end: 0x1168549]
.eh_frame_hdr [start: 0x1168552, end: 0x1170795]
.eh_frame [start: 0x1170800, end: 0x1182903]
.init_array [start: 0x1250024, end: 0x1250031]
.fini_array [start: 0x1250032, end: 0x1250039]
.data.rel.ro [start: 0x1250040, end: 0x1252607]
.dynamic [start: 0x1252608, end: 0x1253119]
.got [start: 0x1253120, end: 0x1253351]
.got.plt [start: 0x1253352, end: 0x1254247]
.data [start: 0x1254248, end: 0x1254935]
.bss [start: 0x1254936, end: 0x1259735]
EXTERNAL [start: 0x1261568, end: 0x1262527]
.gnu_debugaltlink [start: 0x0, end: 0x73]
.gnu_debuglink [start: 0x0, end: 0x51]
.shstrtab [start: 0x0, end: 0x279]
_elfSectionHeaders [start: 0x0, end: 0x1855]
```
</details>

<details><summary>2. Run Current Python Script in Ghidra Jython Task Output</summary>

```terminal
 *  Executing task: /ghidra/support/analyzeHeadless /workspaces/ghidra-python-vscode-devcontainer-skeleton/.ghidra_projects/sample_project sample_project -postscript /workspaces/ghidra-python-vscode-devcontainer-skeleton/sample.py 

source /workspaces/ghidra-python-vscode-devcontainer-skeleton/.env/bin/activate
openjdk version "11.0.15" 2022-04-19 LTS
OpenJDK Runtime Environment Microsoft-32930 (build 11.0.15+10-LTS)
OpenJDK 64-Bit Server VM Microsoft-32930 (build 11.0.15+10-LTS, mixed mode)
INFO  Using log config file: jar:file:/ghidra/Ghidra/Framework/Generic/lib/Generic.jar!/generic.log4j.xml (LoggingInitialization)  
INFO  Using log file: /home/vscode/.ghidra/.ghidra_10.1.4_PUBLIC/application.log (LoggingInitialization)  
INFO  Loading user preferences: /home/vscode/.ghidra/.ghidra_10.1.4_PUBLIC/preferences (Preferences)  
INFO  Class search complete (776 ms) (ClassSearcher)  
INFO  Initializing SSL Context (SSLContextInitializer)  
INFO  Initializing Random Number Generator... (SecureRandomFactory)  
INFO  Random Number Generator initialization complete: NativePRNGNonBlocking (SecureRandomFactory)  
INFO  Trust manager disabled, cacerts have not been set (ApplicationTrustManagerFactory)  
WARN  Neither the -import parameter nor the -process parameter was specified; therefore, the specified prescripts and/or postscripts will be executed without any type of program context. (HeadlessAnalyzer)  
INFO  HEADLESS Script Paths:
    /ghidra/Ghidra/Features/Decompiler/ghidra_scripts
    /ghidra/Ghidra/Features/Base/ghidra_scripts
    /ghidra/Ghidra/Features/BytePatterns/ghidra_scripts
    /ghidra/Ghidra/Processors/8051/ghidra_scripts
    /ghidra/Ghidra/Features/Python/ghidra_scripts
    /ghidra/Ghidra/Debug/Debugger/ghidra_scripts
    /ghidra/Ghidra/Features/FileFormats/ghidra_scripts
    /ghidra/Ghidra/Processors/PIC/ghidra_scripts
    /ghidra/Ghidra/Processors/DATA/ghidra_scripts
    /ghidra/Ghidra/Debug/Debugger-agent-dbgmodel-traceloader/ghidra_scripts
    /ghidra/Ghidra/Features/VersionTracking/ghidra_scripts
    /ghidra/Ghidra/Features/FunctionID/ghidra_scripts
    /ghidra/Ghidra/Features/GnuDemangler/ghidra_scripts
    /ghidra/Ghidra/Features/MicrosoftCodeAnalyzer/ghidra_scripts (HeadlessAnalyzer)  
INFO  HEADLESS: execution starts (HeadlessAnalyzer)  
INFO  Opening existing project: /workspaces/ghidra-python-vscode-devcontainer-skeleton/.ghidra_projects/sample_project/sample_project (HeadlessAnalyzer)  
INFO  Opening project: /workspaces/ghidra-python-vscode-devcontainer-skeleton/.ghidra_projects/sample_project/sample_project (HeadlessProject)  
INFO  SCRIPT: /workspaces/ghidra-python-vscode-devcontainer-skeleton/sample.py (HeadlessAnalyzer)  
INFO  Reading script properties file: /workspaces/ghidra-python-vscode-devcontainer-skeleton/sample.properties (GhidraScriptProperties)  
sample_project
ghidra.framework.data.ProjectFileManager@7a9f836e
sample_project:/
Program Info:
Program: ls: AARCH64:LE:64:v8A_default (Wed Jul 13 13:49:27 UTC 2022)

Memory layout:
Imagebase: 0x100000L
segment_2.1 [start: 0x1048576, end: 0x1049143]
.interp [start: 0x1049144, end: 0x1049170]
.note.gnu.build-id [start: 0x1049172, end: 0x1049207]
.note.ABI-tag [start: 0x1049208, end: 0x1049239]
.gnu.hash [start: 0x1049240, end: 0x1049303]
.dynsym [start: 0x1049304, end: 0x1052423]
.dynstr [start: 0x1052424, end: 0x1053877]
.gnu.version [start: 0x1053878, end: 0x1054137]
.gnu.version_r [start: 0x1054144, end: 0x1054255]
.rela.dyn [start: 0x1054256, end: 0x1060087]
.rela.plt [start: 0x1060088, end: 0x1062703]
.init [start: 0x1062704, end: 0x1062723]
.plt [start: 0x1062736, end: 0x1064511]
.text [start: 0x1064512, end: 0x1149231]
.fini [start: 0x1149232, end: 0x1149247]
.rodata [start: 0x1149248, end: 0x1168549]
.eh_frame_hdr [start: 0x1168552, end: 0x1170795]
.eh_frame [start: 0x1170800, end: 0x1182903]
.init_array [start: 0x1250024, end: 0x1250031]
.fini_array [start: 0x1250032, end: 0x1250039]
.data.rel.ro [start: 0x1250040, end: 0x1252607]
.dynamic [start: 0x1252608, end: 0x1253119]
.got [start: 0x1253120, end: 0x1253351]
.got.plt [start: 0x1253352, end: 0x1254247]
.data [start: 0x1254248, end: 0x1254935]
.bss [start: 0x1254936, end: 0x1259735]
EXTERNAL [start: 0x1261568, end: 0x1262527]
.gnu_debugaltlink [start: 0x0, end: 0x73]
.gnu_debuglink [start: 0x0, end: 0x51]
.shstrtab [start: 0x0, end: 0x279]
_elfSectionHeaders [start: 0x0, end: 0x1855]
 *  Terminal will be reused by tasks, press any key to close it. 
```
</details>

## Ghidra Headless Scripting Hangups 

1. Ghidra runs Jython, not actually python. Limited to python 2.7 features. 
2. In order to supply arguments to calls like [askProgram](https://ghidra.re/ghidra_docs/api/ghidra/app/script/GhidraScript.html#askProgram(java.lang.String)) (which sets the current program being analyzed), a properties file needs to be provided with the same name and location as the script being run. In this case a [sample.properties](sample.properties) sets the arguments for [sample.py](sample.py).