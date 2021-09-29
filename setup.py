import cx_Freeze
executables=[cx_Freeze.Executable("gametask.py")]
cx_Freeze.setup(name="Game Task Kushal Sharma(KD)",
options={"build_exe":{"packages":["pygame"],
"include_files":["star.png"]}},
executables=executables
)