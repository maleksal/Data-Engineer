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
        return:{ 'repository_url': Ex: 'github.com/my_repo.git',
                'number of lines': Ex: 5000'}
        """
        def walk(dir_path, pattern='*'):
            """
            Generator for walking a directory tree.
            :param:dir_path -> ../repository
            :param:pattern -> [*.py, *.txt, ...]
            """
            for root_, dirs, files in os.walk(dir_path):
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
        return {'repository_url': f'{repository_url[0]}', 'number of lines': f'{number_of_lines}'}

    def extract_libraries(self):
        """
        Function that generate requirements.txt for repo
        Using < pipreqs >
        then return a list of all external libraries
        :return: { 'libraries': [lib1, lib2, ...]}
        """
        def extract_from_file(file_path='../file.txt'):
            """ extract libraries from a requirements.txt file """

            # check if file not empty
            not_empty = os.path.getsize(file_path) > 1
            if not_empty:
                with open(file_path) as r:
                    lib_list = r.read().split('\n')
                    return lib_list
            return 'no external libraries'

        # check for a requirements.txt file
        req_path = f'{self.repo_root}/requirements.txt'
        check_file_exists = os.path.exists(req_path)
        if check_file_exists:
            return {'libraries': extract_from_file(file_path=req_path)}
        else:
            # Generate requirements.txt
            os.system(f"pipreqs {self.repo_root}")
            return {'libraries': extract_from_file(file_path=req_path)}


# get repository path from command line
path = sys.argv[1]

process_data = ProcessData(path)
print(process_data.count_lines())
print(process_data.extract_libraries())
