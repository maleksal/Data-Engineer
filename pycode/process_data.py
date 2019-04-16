# imports
import os
import re
import sys
import fnmatch


class ProcessData:

    def __init__(self, repo_root):
        """
        :param repo_root: repository path
        Ex: ../Desktop/repos/myrepository
        """
        self.repo_root = repo_root

    def count_lines(self):
        """
        count lines of code function
        return:{
            'repository_url': repository url',
             number of lines': Ex: 5000'
             }
        """
        def walk(root, pattern='*'):
            
            """ Generator for walking a directory tree."""
            
            for root_, dirs, files in os.walk(root):
                for file in files:
                    if fnmatch.fnmatch(file, pattern):
                        # if file extension match pattern '.py'
                        yield os.path.join(root_, file)

        # get number lines of code
        number_of_lines = 0
        for pyfile in walk(self.repo_root, pattern="*.py"):
            with open(pyfile, encoding="utf8", errors='ignore') as f:
                num = len(f.readlines())
                number_of_lines += num

        # get repository url for .git/config file
        with open(f'{self.repo_root}/.git/config') as r:
            url = r.read()
            repository_url = re.findall(
                'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
        return {'repository_url': f'{repository_url}', 'number of lines': f'{number_of_lines}'}


# get repository path from command line
path = sys.argv[1]

process_data = ProcessData(path)
process_data.count_lines()
