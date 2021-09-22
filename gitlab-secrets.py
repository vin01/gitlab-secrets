#!/usr/bin/env python3

import requests
import fire

ROOT_URL = ""
PRETTY = False
NOMASK = False

SESSION = requests.session()

def vars(url, token, pretty=False, nomask=False):
    """List all ci/cd variables from all gitlab projects
    which the given token has access to.

    url : str
        URL to the gitlab instance
    token: str
        access token for authentication
    pretty: bool
        pretty print
    nomask: bool
        Do not mask values for variables. Default behavior is to mask the values after 10 characters
    """
    global ROOT_URL
    global PRETTY
    global NOMASK
    global SESSION

    if not "&page=" in url:
        ROOT_URL = url
        PRETTY = pretty
        NOMASK = nomask
        SESSION.headers.update({"Authorization": "Bearer %s" % (token)})
        resp = SESSION.get("%s/api/v4/projects?per_page=30&page=1" % (url))
    else:
        resp = SESSION.get(url)
    if resp.ok:
        for project in resp.json():
            var_resp = SESSION.get("%s/api/v4/projects/%s/variables" % (ROOT_URL, project["id"]))
            if var_resp.ok:
                variables = var_resp.json()
                if variables:
                    print("----")
                    print("Variables for project %s:" %
                          (project["path_with_namespace"]))
                    for variable in variables:
                        variable.pop("variable_type")
                        if len(variable["value"]) > 10 and not NOMASK:
                            variable["value"] = "%s***" % (
                                variable["value"][0:10])
                        if PRETTY:
                            variable.pop("protected")
                            print('{"key": %-22s| "value": %-14s| "masked": %-6s| "environment_scope": %s}' % (
                                variable["key"], variable["value"], variable["masked"], variable["environment_scope"]
                            ))
                        else:
                            print(variable)
                        variable.pop
                    print("----\n")
        if resp.links.get("next"):
            vars(resp.links["next"]["url"], token)
    else:
        print(resp.status_code, url)


if __name__ == '__main__':
    fire.Fire(vars)
