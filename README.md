# Team 1-2
---

## Summary
- [Requirements](#requirements)
- [Initial Setup](#setup)
	+ [UV](#uv-install)
	+ [Virtual Enviroment](#venv-setup)
	+ [Libraries](#libs-install)
- [Database manipulations through polars](#polars-database)

---
## Requirements <a name="requirements"></a>

- Python 	=> 3.12.3
- Docker 	=> 28.1.1
- uv 		=> 0.6.14
- Git		=> 2.43.0

|**Python Library**|**Version**|
|:---:|---:|
|Jupyterlab|4.4.0|
|SQLAlchemy|2.0|
|Polars|1.22.0|
|Psycopg|3.2.0|
|Pandas|2.2.3|
|Pyarrow|10.0.0|


## Initial Setup <a name="setup"></a>
### 1. UV
There are three official ways to install the UV (the package manager) and they can be found on its [documentation](https://docs.astral.sh/uv/getting-started/installation/#pypi). But for linux standalone installer can be done with:
`$ curl -LsSf https://astral.sh/uv/0.6.14/install.sh | sh`.
### 2. Virtual Enviroment <a name="virtual-enviroment"></a>
To setup the virtual enviroment that is going to be used on the project it is necessary to build a virtual enviroment with:
```bash
$ uv venv --python 3.12.3
```
Furthermore, to initialize the venv enviroment it's going to be used the command:
```bash
$ source .venv/bin/activate
```
After that, each input line on the terminal during the session is going to begin with ```(enviroment name)```. Also, to disable the vitual enviroment on the session it's enough to send:
```bash
(enviroment name) $ deactivate
```

### 3. Libraries
Each library can be downloaded with the corrected versions inside the correct virtual enviroment with the following command example:
```bash
(enviroment name) $ uv pip install <library_name>==<library_version>
```


---
## Database manipulations through polars <a name="polars-database"></a>

###