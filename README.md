**Work in Progress**

https://thumpcc.github.io/

**Build locally**

Create/activate `venv` or `conda env`

Clone the repo

```shell
git clone https://github.com/thumpcc/thumpcc.github.io.git
cd thumpcc.github.io/
```

Install Peru and sync
```shell
pip install peru
peru sync
```

Install sphinx and other packages
```shell
pip install -r requirements.txt
```

Sphinx build and launch browser

```shell
make html
make browse
```