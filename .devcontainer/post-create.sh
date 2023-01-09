# Create local venv
python3 -m venv .env
source .env/bin/activate

# Download latest pyi typings
pip install ghidra-stubs

# Install ghidra-bridge
pip install ghidra_bridge

# Install bridge scripts to local dir
python -m ghidra_bridge.install_server .ghidra_bridge

# Install pyhdira
pip install pyhidra

# If arm64 os, need to build native binaries for Ghidra
if uname -a | grep -q 'aarch64'; then
    $GHIDRA_INSTALL_DIR/support/buildNatives
fi