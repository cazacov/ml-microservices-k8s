# Machine Learning Microservices on Kubernetes

CircleCI continuous integration status: 

[![CircleCI](https://circleci.com/gh/cazacov/ml-microservices-k8s.svg?style=svg)](https://circleci.com/gh/cazacov/ml-microservices-k8s)


## Project Overview

In this project, you will apply the skills you have acquired in this course to operationalize a Machine Learning Microservice API. 

You are given a pre-trained, `sklearn` model that has been trained to predict housing prices in Boston according to several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and so on. You can read more about the data, which was initially taken from Kaggle, on [the data source site](https://www.kaggle.com/c/boston-housing). This project tests your ability to operationalize a Python flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This project could be extended to any pre-trained machine learning model, such as those for image recognition and data labeling.

### Project Tasks

Your project goal is to operationalize this working, machine learning microservice using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project you will:
* Test your project code using linting
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker and make a prediction
* Improve the log statements in the source code for this application
* Configure Kubernetes and create a Kubernetes cluster
* Deploy a container using Kubernetes and make a prediction
* Upload a complete Github repo with CircleCI to indicate that your code has been tested

You can find a detailed [project rubric, here](https://review.udacity.com/#!/rubrics/2576/view).

**The final implementation of the project will showcase your abilities to operationalize production microservices.**

---

## Prerequisites

### Install Python toolchain

```bash
sudo apt update
sudo apt install git
sudo apt install python3-venv python3-dev pylint python3-wheel pylin

pip install --upgrade pip
pip install wheel

sudo apt install libblas-dev liblapack-dev libatlas-base-dev gfortran
sudo apt-get install python3-sklearn python3-sklearn-lib
```

### Install Docker

See [instructions](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04).

### Install Kubernetes

For local installation of Kubernetes on Ubuntu see instructions at https://microk8s.io/

### Install hadolint

```bash
wget -O /usr/local/bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.18.0/hadolint-Linux-x86_64
sudo chmod go+rx /usr/local/bin/hadolint
```

### Install Amazon CLI

```bash
sudo apt  install awscli
```

### Install CircleCI
```bash
wget https://raw.githubusercontent.com/CircleCI-Public/circleci-cli/master/install.sh
less install.sh 
sudo bash install.sh
rm install.sh
```

## Setup the Environment

* Create a virtualenv with `make setup` and activate it with `source ~/.ml-microservices-k8s/bin/activate` 
* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`
4. Run in microk8s (local Kubernetes for Ubuntu):  `./run_microk8s.sh`

### Continuous Integration

1. Check CircleCI config: `make validate-circleci`
2. Run local build: `make run-circleci-local`

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Run via kubectl (or microk8s kubectl)