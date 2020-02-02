# vector-fun
Playing around with the Anki Vector robot

Built with the [Official Vector SDK](https://github.com/anki/vector-python-sdk)


# Installation
1. Set up your Vector
  
    Go download the Vector app, once you're done setting it up, come back here.
1. Create a Python3 Virtual Environment

    `python3 -m venv venv`
    
1. Activate the Virtual Environment
    
    `source venv/bin/activate`
    
1. Install the requirements
    
    `pip install -r requirements.txt`
    
1. Install 3D Viewer requirements

    `pip3 install "anki_vector[3dviewer]"`
    
1. Run the Anki Vector setup tool
    
    `python -m anki_vector.configure`
    
    Then follow through this setup. It will ask for your Vector's IP, Serial, and Name.
