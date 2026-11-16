# EECE 435L Lab 10 Jenkins CI and CD

Andrew Khoury

The project automates dependency installation, Python style checks, unit tests,
test coverage, security scanning, and a persistent local deployment with Jenkins.

## Project files

- `app.py`: personalized greeting application.
- `tests/`: nine unit and command-line tests for the application and deployment.
- `deploy.py`: copies the application into a persistent local directory.
- `requirements.txt`: pinned versions of the four tools required by the pipeline.
- `Jenkinsfile_Andrew_Khoury`: declarative pipeline for Parts 3 and 4.

## Run the checks locally

Use Python 3.10 or newer on macOS or Linux. From the repository directory:

```sh
python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
mkdir -p reports
venv/bin/python -m flake8 app.py deploy.py tests
venv/bin/python -m pytest -v --junitxml=reports/tests.xml
venv/bin/python -m coverage run -m pytest -q
venv/bin/python -m coverage report
venv/bin/python -m coverage xml
venv/bin/python -m coverage html
venv/bin/python -m bandit app.py deploy.py -f json -o reports/bandit.json
venv/bin/python deploy.py --target ../deployments/jenkins_project
venv/bin/python ../deployments/jenkins_project/app.py
```

Expected deployed application output: `Hello, World from Andrew Khoury!`
The coverage gate requires 100 percent for the application and deployment code.

## Configure Jenkins

1. Install Jenkins LTS with a supported Java runtime (Java 21 or Java 25).
2. Start Jenkins and complete its normal setup wizard with authentication enabled.
3. Install Git, Pipeline, SSH Agent, Workspace Cleanup, and JUnit plugins.
   Pipeline Stage View is useful for the build screenshot.
4. Make sure `git` and `python3` are on the Jenkins process's PATH.
5. Create a Pipeline job named `Python-CI-CD`.
6. Set Definition to **Pipeline script from SCM**, and SCM to **Git**.
7. Use the GitHub repository URL, and set the branch specifier to `*/main`.
8. Set Script Path to **Jenkinsfile_Andrew_Khoury**.
9. Save and click **Build Now**. A manual build is sufficient for the lab.

The six stages must all pass: Setup, Lint, Test, Coverage, Security Scan, Deploy.
Test results and reports are archived before the workspace is cleaned. Deployment
is stored in `$JENKINS_HOME/deployments/jenkins_project`, outside the workspace.
The local deployment needs no remote server or SSH credentials. SSH Agent is
installed because the lab lists it as a prerequisite plugin.

## Corrections to the handout example

The application returns the personalized string expected by the unit test.
The dependency list includes pytest, coverage, and Bandit as well as Flake8.
The pipeline invokes the virtual environment's interpreter directly so that it
does not depend on the non-POSIX `source` command or an activation persisting
between Jenkins shell steps. The custom Jenkinsfile path is configured explicitly.
The Deploy stage copies and executes the application instead of only printing
a placeholder message.

## Submission

Submit a text file containing the GitHub link, the modified Jenkinsfile, and a
brief report describing the modifications and the actual Jenkins build output.
Include the successful build number, console output, test results, coverage,
Bandit results, and deployment output in the final report or its evidence.
