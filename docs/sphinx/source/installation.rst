Installation
============

You can install this program by grabbing the source code and running `pip install .` inside the project root.

Download and Install
--------------------

.. code-block:: bash

    # Download
    git clone https://github.com/JamesClarke7283/AltEgo.git
    cd AltEgo
    # Make a virtual environment
    python3 -m venv .venv
    # Enter environment
    source .venv/bin/activate
    # Install Dependencies
    pip3 install briefcase
    # Run
    briefcase dev

    # Or to install
    briefcase package
    # Then look in the ./dist directory, the package/executable for your platform will be in that folder.