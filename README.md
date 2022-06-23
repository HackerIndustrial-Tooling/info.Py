# info.Py
Info.Py is a situationally aware python library for gathering system information. Can be leveraged by additional libraries or used in a standalone manner. 


### How to use 

clone the repo:
```
git clone https://github.com/HackerIndustrial-Tooling/info.Py
```

cd into the folder:
```
cd info.py
```

start an interactive python shell:
```python3
```

then import the following:
```
from src.info import Info
info = Info()
print(info.platform)
#get all the running proccesses (linux olnly atm)
info.processList
```

