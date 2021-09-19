![](https://imgur.com/84luBvC.png)

# Mailbucket

Mailbucket is a Kubernetes-ready Postfix email server that will take received emails and upload them to an AWS S3 bucket for later processing or archive purposes.

Please consider opening an issue if you have an additional use-case or feature request for mailbucket!


# Configuration

The application utilizes the following environment variables:

|Environment|Default|
|-|-|
|AWS_SECRET_ACCESS_KEY|*None*|
|AWS_ACCESS_KEY_ID|*None*|
|AWS_REGION|`us-east-1`|
|S3_BUCKET|*None*|

# Installation

Mailbucket can be easily installed in Kubernetes via its Helm chart. From the project root:

```sh
helm install mailbucket helm/ \
    --set env.AWS_ACCESS_KEY_ID=AAAAAAAAAAAAAAAAAAAA \
    --set env.AWS_SECRET_ACCESS_KEY=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
    --set env.AWS_REGION=us-west-1 \
    --set env.S3_BUCKET=my-mailbucket
```

`AWS_REGION` will default to `us-east-1` if no value is provided. All other configuration values are ***required***.

Installing in this manner will configure a LoadBalancer service listening on port 8025. Port 8025 is used because AWS disables outbound SMTP traffic from EC2 instances by default (thank the email spammers for this policy). However, the listening port can be overridden with `--set service.port=25` during installation if your account has exemption.

Mailbucket's Helm chart also supports Helm-native testing. Executing `helm test mailbucket` after installation will run a test pod to ensure mailbucket is actively available for SMTP sessions.

---
# Development Setup

Ensure you have the following prerequisites satisfied:
 - Docker for Desktop
 - VS Code Extensions: Remote Containers
   - Download and install Microsoft's VS Code extension for developing in [Remote Containers](vscode:extension/ms-vscode-remote.remote-containers)

>Note: This is a VS Code Remote Containers development project: all development is done within a container to reduce initial time-to-develop. Getting this project up and running on your machine can be as simple as pulling down the repository, running the Docker daemon the host machine, opening the project in VS Code, and clicking twice.


## Directions

- Clone the repository

```sh
git clone git@github.com:jrcasso/mailbucket
```

- Open the repository in VS Code
```sh
code mailbucket
```
- Ensure you have the necessary environment variables to run this application set in your local environment; they will be used transferred to the remote container environment. You can see which are required in the `.devcontainer/devcontainer.json` file under the `remoteEnv` key.
- In the bottom-left corner of the VS Code window, click the highlighted "><" button (or navigate to the Remote Containers extension).
- From the dropdown, select "Remote Containers: Reopen in Container"

_**That's it!**_

>Note: When you enter the remote VS Code environment for the first time, a pop-up will appear in the corner indicating that you should install some of the go binaries required for tooling (e.g. gopls, dlv-dap - a Go debugging server). Click "Install", and these binaries will be persisted for all future spin-ups via a docker-compose volume for the environment.

## Development Details

VS Code will begin to build an image that is specified in `.devcontainer/`; it will be the container image that you develop in. When it's done, it'll automatically throw your entire VS Code interface/environment inside that container where you may begin deveopment. The current configuration will also mount your Docker engine socket into this container, so that Docker commands may be issued from within to manage containers on the host. Utilitarian tools like git and all the things needed to run a Go program are in that environment. It's still a container, so all of the idempotency and innate destructivity of containers are in fact *features* of this development strategy. If everyone develops in the same way, the time-to-develop becomes incredibly small.

Additional tooling that might be needed can be done so during container runtime; however, if it is something that should stick around for every other developer too (i.e. they might also run into this same issue), please modify the `.devcontainer/Dockerfile` and open a pull request.
