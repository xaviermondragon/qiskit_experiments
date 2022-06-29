## Description:
The script in main.py puts takes two qubits into the Bell state  and measures this state 100 times.
We expect to observe the states |00> and |11> approximately half of the time.

## Preparation
- sudo apt-get install python3-tk
- pip3 install virtualenv

## Install dependencies in the virtual environment
```
virtualenv venv
source env/bin/activate
pip install -r requirements.txt

deactivate
```