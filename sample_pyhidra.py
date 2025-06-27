import pyghidra

# Section to make autocomplete work
try:
    import ghidra
    from ghidra_builtins import *
except:
    pass
####

PROJECT_NAME = 'sample_pyghidra'
PROJECT_LOCATION = '.ghidra_projects'

pyghidra.start(True)  # setting Verbose output

from ghidra.program.model.listing import Program  # noqa

with pyghidra.open_program("/bin/ls", project_name=PROJECT_NAME, project_location=PROJECT_LOCATION) as flat_api:

    # from ghidra.program.model.listing import Program

    # set correct typing to leverage autocomplete  my_var: "ghidra-type"
    prog: "Program" = flat_api.getCurrentProgram()

    print("Program Info:")
    program_name = prog.getName()
    creation_date = prog.getCreationDate()
    language_id = prog.getLanguageID()
    compiler_spec_id = prog.getCompilerSpec().getCompilerSpecID()
    print("Program: {}: {}_{} ({})\n".format(program_name,
          language_id, compiler_spec_id, creation_date))

    # Python 3 formatted string literals (f-strings)!!!
    print(
        f"Program: {program_name}: {language_id}_{compiler_spec_id} ({creation_date})")

    # Get info about the current program's memory layout
    print("Memory layout:")
    print("Imagebase: " + hex(prog.getImageBase().getOffset()))
    for block in prog.getMemory().getBlocks():
        start = block.getStart().getOffset()
        end = block.getEnd().getOffset()
        print("{} [start: 0x{}, end: 0x{}]".format(
            block.getName(), start, end))
