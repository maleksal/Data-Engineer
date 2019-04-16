# Data Engineering Challange

## Run Instructions
* Clone the source repository from Github.
```git
git clone https://github.com/maleksal/Data-Engineer
```
* install requirments.txt
```
run: pip install -r requirements.txt
```

* Run git_clone.py to clone a list of repositories
```sys
python git_clone.py <repositories list>
Ex: python git_clone.py "mylist.txt"
```
* Run process_data.py to start processing data
```sys
python process_data.py <repository path>
Ex: process_data.py "../Desktop/myrepo"
```

## Obtaining the data
> A list of 100,000 repositories is provided [here](https://raw.githubusercontent.com/monikturing/turing-data-challenge/master/url_list.csv) . These repositories are around 2Mb and the primary language is python.

## Processing

For each repository, our goal is to compute certa
in statistics only for the Python code present. Here is the list of items that you need to compute for each repository:
* Number of lines of code [this excludes comments, whitespaces, blank lines].
  List of external libraries/packages used.
* The Nesting factor for the repository: the Nesting factor is the average depth of a nested for loop throughout the code.

```python
#Loop 1
for i in range(100):
	for elem in elements:
		...do something..
		for k in elem:
			..do something..

#Loop 2
for i in range(100):
	for elem in elements:
		..do something..
	for k in range(100):
		..do something..
```
>Loop 1 has nesting depth of 3
>Loop 2 has nesting depth of 2
>The average nesting depth for the code is (3+2)/2 = 2.5

* Code duplication: What percentage of the code is duplicated per file. 
`Note: If the same 4 consecutive lines of code (disregarding blank lines, comments, etc. other non code items) appear in multiple places in a file, all the occurrences except the first occurence are considered to be duplicates.`

* Average number of parameters per function definition in the repository.
* Average Number of variables defined per line of code in the repository.

## Result
An output file ‘results.json’ with the results of the computation in the following JSON format. Each item in the Array list represents the result for a single repository.

```json
[
{	'repository_url': 'https://github.com/tensorflow/tensorflow', 
	'number of lines': 59234, 
	'libraries': ['tensorflow','numpy',..],
	'nesting factor': 1.457845,
	'code duplication': 23.78955,
	'average parameters': 3.456367,
	'average variables': 0.03674
}, ......
]
```

