import os.path

import nox

test_reqs = ["pytest", "pytest-cov", "coverage"]
pytest_cov_args = ["--cov=find_libpython", "--cov-branch"]
coverage_file = "coverage.xml"


@nox.session
def tests(session):
    # install current module and runtime dependencies
    session.install(".")

    # print info
    session.run("python", "-m", "find_libpython", "--candidate-names")
    session.run("python", "-m", "find_libpython", "--candidate-paths")
    session.run("python", "-m", "find_libpython", "-v")

    # install testing dependencies
    session.install(*test_reqs)

    # run pytest
    install_loc = session.run(
        "python",
        "-c",
        "import find_libpython; print(find_libpython.__file__)",
        silent=True,
    )
    install_loc = os.path.dirname(install_loc.strip())
    session.run("pytest", *pytest_cov_args, "tests/")
    session.run(
        "pytest", *pytest_cov_args, "--cov-append", "--doctest-modules", install_loc
    )
    session.run("coverage", "xml", "-o", coverage_file)
