from torch import __version__ as torch_version
torch_version = torch_version.__str__().split('+')[0]

setup_file_path = "src/PytorchNvCodec/setup.py"
setup_script = []
with open(setup_file_path, "r") as fopen:
    for line in fopen:
        if 'install_requires=["torch"]' in line:
            line = line.replace('"torch"', f'"torch<={torch_version}"')
        setup_script.append(line)
with open(setup_file_path, "w") as fopen:
    setup_script = "".join(setup_script)
    fopen.write(setup_script)


pyproject_file_path = "src/PytorchNvCodec/pyproject.toml"
pyproject_text = []
with open(pyproject_file_path, "r") as fopen:
    for line in fopen:
        if '"torch"' in line:
            line = line.replace('"torch"', f'"torch<={torch_version}"')
        pyproject_text.append(line)
with open(pyproject_file_path, "w") as fopen:
    pyproject_text = "".join(pyproject_text)
    fopen.write(pyproject_text)