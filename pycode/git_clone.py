# imports
import os
import sys
import git
from tqdm import tqdm


def clone_repository(path="../Desktop", repositories_list="file.txt"):
    """
    clone repositories from github.com
    with a given repositories list

    :param path: where to clone repositories
    :param repositories_list: txt file contains repo urls
    """
    repos_list = open(
        f"{repositories_list}", "r").read().split()

    # Process Download
    for repo in tqdm(repos_list):
        try:
            git.Git(path).clone(repo, branch='master')
        except Exception as exception:
            open(
                f'{os.getcwd()}/Log.txt', 'a').write(str(exception))
    return


clone_dir = sys.argv[1]
list_repos = sys.argv[2]

clone_repository(clone_dir, list_repos)
