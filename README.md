# ghidra-python-skeleton

A simple template to provide a vscode Ghidra python scripting environment.

## Features

- Prescribes workflow to get you started (easily modified)
- Auto complete for Ghidra Python script
    - via pyi typings from [VDOO-Connected-Trust/ghidra-pyi-generator](https://github.com/VDOO-Connected-Trust/ghidra-pyi-generator)

## Workflow

Ghidra is a binary analysis tool (and much more). In order to do something useful, you need to create a project and add binaries. Once a project exists with at least one binary added, headless analysis can begin. 

1. [Create Ghidra Project](.vscode/tasks.json#L25-L35)
2. [Import binary to project](.vscode/tasks.json#L37-L49)
3. [Run script on binary](run_headless.py)
   - Sample Script - [sample.py](sample.py)

## Setup

### Clone Repo

```bash
git clone git@github.com:clearbluejar/ghidra-python-vscode-skeleton.git
cd ghidra-python-vscode-skeleton
```

### Setup venv
```bash
python3 -m venv .env
source .env/bin/activate
```

### Download  Ghidra

https://ghidra-sre.org/ 
   - Need to download the [latest Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases/latest) and it's [dependencies](https://ghidra-sre.org/InstallationGuide.html#Requirements)
   - Once downloaded, update [settings.json](.vscode/settings.json) with path to Ghidra install path (the directory path to the unzipped release)
:

Update setttings with install path:
https://github.com/clearbluejar/ghidra-python-vscode-skeleton/blob/0a081798d16e4a498c3f8a25a9b60863f421581e/.vscode/settings.json#L12-L18

### Install Ghidra Python stubs (auto-complete powers)

https://github.com/clearbluejar/ghidra-pyi-generator
- Fork that produces `ghidra-stubs` [builds](https://github.com/clearbluejar/ghidra-pyi-generator/releases/latest) against the latest Ghidra
- Relies on [settings.json](.vscode/settings.json) being configured correctly (already configured in template)

```
pip install https://github.com/clearbluejar/ghidra-pyi-generator/releases/download/v1.0.3-10.1.4/ghidra_stubs-10.1.4.refs_heads_master-py2.py3-none-any.whl
```

After installation, ensure the following settings are correct in [settings.json](.vscode/settings.json):
```json
    "python.analysis.stubPath": "${workspaceFolder}\\.env\\Lib\\site-packages\\ghidra-stubs",
    "python.autoComplete.extraPaths": [
        
        "${workspaceFolder}\\.env\\Lib\\site-packages\\ghidra-stubs"
    ],
    "python.analysis.extraPaths": [
        "${workspaceFolder}\\.env\\Lib\\site-packages\\ghidra-stubs"
    ],
```

### Run Setup Task

In VScode click `Terminal --> Run Task --> Setup`

Setup Task will run both "Import Binary" and "Create Project Directory" tasks found in [tasks.json](.vscode/tasks.json).

<details><summary>Create Project Directory</summary>

```powershell
> Executing task: mkdir -p C:\Users\user\source\ghidra-python-skeleton\.ghidra_project_files <



    Directory: C:\Users\user\source\ghidra-python-skeleton


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2022-05-08  12:55 AM                .ghidra_project_files



Terminal will be reused by tasks, press any key to close it.
```
</details>

<details><summary>Import Binary</summary>

```console
> Executing task: C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\support\analyzeHeadless.bat C:\Users\user\source\ghidra-python-skeleton\.ghidra_project_files sample_project -import C:\Users\user\source\ghidra-python-skeleton\.env\Scripts\python.exe -overwrite <

INFO  Using log config file: jar:file:/C:/Users/user/Downloads/ghidra_10.1.4_PUBLIC_20220519/ghidra_10.1.4_PUBLIC/Ghidra/Framework/Generic/lib/Generic.jar!/generic.log4j.xml (LoggingInitialization)  
INFO  Using log file: C:\Users\user\.ghidra\.ghidra_10.1.4_PUBLIC\application.log (LoggingInitialization)  
INFO  Loading user preferences: C:\Users\user\.ghidra\.ghidra_10.1.4_PUBLIC\preferences (Preferences)
INFO  Loading previous preferences: C:\Users\user\.ghidra\.ghidra_10.1.3_PUBLIC\preferences (Preferences)
INFO  Class search complete (973 ms) (ClassSearcher)  
INFO  Initializing SSL Context (SSLContextInitializer)  
INFO  Initializing Random Number Generator... (SecureRandomFactory)  
INFO  Random Number Generator initialization complete: SHA1PRNG (SecureRandomFactory)  
INFO  Trust manager disabled, cacerts have not been set (ApplicationTrustManagerFactory)
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.felix.framework.URLHandlers (file:/C:/Users/user/Downloads/ghidra_10.1.4_PUBLIC_20220519/ghidra_10.1.4_PUBLIC/Ghidra/Features/Base/lib/org.apache.felix.framework-6.0.3.jar) to constructor sun.net.www.protocol.file.Handler()
WARNING: Please consider reporting this to the maintainers of org.apache.felix.framework.URLHandlers
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
INFO  HEADLESS Script Paths:
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\Python\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\VersionTracking\ghidra_scripts
    C:\Users\user\.ghidra\.ghidra_10.1.4_PUBLIC\Extensions\PatchDiffCorrelator\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Debug\Debugger\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\Decompiler\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Processors\DATA\ghidra_scripts
    C:\Users\user\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Debug\Debugger-agent-dbgmodel-traceloader\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\FileFormats\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Processors\PIC\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\BytePatterns\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\MicrosoftCodeAnalyzer\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Processors\8051\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\Base\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\FunctionID\ghidra_scripts
    C:\Users\user\Downloads\ghidra_10.1.4_PUBLIC_20220519\ghidra_10.1.4_PUBLIC\Ghidra\Features\GnuDemangler\ghidra_scripts (HeadlessAnalyzer)
INFO  HEADLESS: execution starts (HeadlessAnalyzer)
INFO  Opening existing project: C:\Users\user\source\ghidra-python-skeleton\.ghidra_project_files\sample_project (HeadlessAnalyzer)
INFO  Opening project: C:\Users\user\source\ghidra-python-skeleton\.ghidra_project_files\sample_project (HeadlessProject)  
INFO  REPORT: Processing input files:  (HeadlessAnalyzer)  
INFO       project: C:\Users\user\source\ghidra-python-skeleton\.ghidra_project_files\sample_project (HeadlessAnalyzer)
INFO  IMPORTING: C:\Users\user\source\ghidra-python-skeleton\.env\Scripts\python.exe (HeadlessAnalyzer)  
INFO  /python.exe: file deleted (user) (LocalFileSystem)
INFO  Deleted local file python.exe (GhidraFileData)
WARN  REPORT: Removed conflicting program file from project: /python.exe (HeadlessAnalyzer)  
INFO  REPORT: Import succeeded with language "x86:LE:64:default" and cspec "windows" for file: C:\Users\user\source\ghidra-python-skeleton\.env\Scripts\python.exe (HeadlessAnalyzer)  
INFO  ANALYZING all memory and code: C:\Users\user\source\ghidra-python-skeleton\.env\Scripts\python.exe (HeadlessAnalyzer)  
WARN  Symbol directory missing control files, guessing storage scheme as level 1: C:\symbols (LocalSymbolStore)  
INFO  Skipping PDB processing: failed to locate PDB file in configured locations (PdbUniversalAnalyzer)  
INFO  Use a script to set the PDB file location. I.e.,
    PdbAnalyzer.setPdbFileOption(currentProgram, new File("/path/to/pdb/file.pdb")); or
    PdbUniversalAnalyzer.setPdbFileOption(currentProgram, new File("/path/to/pdb/file.pdb"));
Or set the symbol server search configuration using:    PdbPlugin.saveSymbolServerServiceConfig(...);
 This must be done using a pre-script (prior to analysis). (PdbUniversalAnalyzer)
INFO  Packed database cache: C:\Users\user\AppData\Local\Ghidra\packed-db-cache (PackedDatabaseCache)  
INFO  -----------------------------------------------------
    ASCII Strings                              0.377 secs
    Apply Data Archives                        0.117 secs
    Call Convention ID                         0.827 secs
    Call-Fixup Installer                       0.010 secs
    Create Address Tables                      0.027 secs
    Create Address Tables - One Time           0.041 secs
    Create Function                            0.209 secs
    Data Reference                             0.083 secs
    Decompiler Parameter ID                    4.542 secs
    Decompiler Switch Analysis                 1.306 secs
    Demangler Microsoft                        0.033 secs
    Disassemble                                0.125 secs
    Disassemble Entry Points                   0.804 secs
    Embedded Media                             0.013 secs
    External Entry References                  0.000 secs
    Function ID                                0.522 secs
    Function Start Search                      0.013 secs
    Non-Returning Functions - Discovered       0.063 secs
    Non-Returning Functions - Known            0.003 secs
    PDB Universal                              0.129 secs
    Reference                                  0.076 secs
    Scalar Operand References                  0.205 secs
    Shared Return Calls                        0.037 secs
    Stack                                      1.575 secs
    Subroutine References                      0.076 secs
    Subroutine References - One Time           0.006 secs
    Windows x86 PE Exception Handling          0.861 secs
    Windows x86 PE RTTI Analyzer               0.081 secs
    WindowsResourceReference                   0.762 secs
    x86 Constant Reference Analyzer            1.535 secs
-----------------------------------------------------
     Total Time   14 secs
-----------------------------------------------------
 (AutoAnalysisManager)
INFO  REPORT: Analysis succeeded for file: C:\Users\user\source\ghidra-python-skeleton\.env\Scripts\python.exe (HeadlessAnalyzer)  
INFO  REPORT: Save succeeded for file: /python.exe (HeadlessAnalyzer)  

Terminal will be reused by tasks, press any key to close it.
```
</details>

## Ways to run headless script

1. The most straightforward means to run the script it to hit run via launch on [run_headless.py](run_headless.py). It simply uses subprocess module with the correct arguments to run the sample script. 
2. Another way is to run the script directly by using the `Run Current Python Script in Ghidra Jython` task within [tasks.json](.vscode/tasks.json).  To use this task make sure you have open and focused the [sample.py](sample.py).
3. The third way would be to simply copy sample.py to your `ghidra_scripts` directory and run it in the GUI using Script Manager


## Ghidra Headless Scripting Hangups 

1. Ghidra runs Jython, not actually python. Limited to python 2.7 features. 
2. In order to supply arguments to calls like [askProgram](https://ghidra.re/ghidra_docs/api/ghidra/app/script/GhidraScript.html#askProgram(java.lang.String)) (which sets the current program being analyzed), a properties file needs to be provided with the same name and location as the script being run. In this case [sample.properties](sample.properties) and [sample.py](sample.py).

