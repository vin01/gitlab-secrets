# gitlab-secrets

Retrieve Ci/CD variables from all projects on a Gitlab instance.

This can be helpful for audits and penetration testing. Ci/CD systems have access to various secrets like package registries, API tokens, internal services and even production environments.

Even CI tests like `terraform plan` for [infrastructure as code](https://docs.gitlab.com/ee/user/infrastructure/iac/) mean providing credentials for cloud services and APIs and can be [very risky](https://alex.kaskaso.li/post/terraform-plan-rce).

# usage

```
NAME
    gitlab-secrets.py - List ci/cd variables from all gitlab projects
                        which the given token has access to.

SYNOPSIS
    gitlab-secrets.py URL TOKEN <flags>

DESCRIPTION
    url : str
        URL to the gitlab instance
    token: str
        access token for authentication
    pretty: bool
        pretty print
    nomask: bool
        Do not mask values for variables.
        Default behavior is to mask the values after 10 characters

POSITIONAL ARGUMENTS
    URL
    TOKEN

FLAGS
    --pretty=PRETTY
        Default: False
    --nomask=NOMASK
        Default: False
```

# You might also like

- [Anatomy of a Cloud Infrastructure Attack via a Pull Request](https://goteleport.com/blog/hack-via-pull-request/)
- [Authenticating and reading secrets with HashiCorp Vault](https://docs.gitlab.com/ee/ci/examples/authenticating-with-hashicorp-vault/)
