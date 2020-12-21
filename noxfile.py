import nox
import os.path


test_reqs = [
    'pytest',
    'pytest-cov'
]

pytest_cov_args = [
    '--cov=find_libpython',
    '--cov-branch'
]


@nox.session
def tests(session):

    # install current module and runtime dependencies
    session.install('.')

    # install testing dependencies
    session.install(*test_reqs)

    # run pytest
    install_loc = session.run('python', '-c', 'import find_libpython; print(find_libpython.__file__)', silent=True)
    install_loc = os.path.dirname(install_loc.strip())
    session.run('pytest', *pytest_cov_args, 'tests/')
    session.run('pytest', *pytest_cov_args, '--cov-append', '--doctest-modules', install_loc)
