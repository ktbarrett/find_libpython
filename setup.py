from setuptools import setup

setup(
    use_scm_version=dict(
        write_to="src/find_libpython/_version.py"
    )
)
