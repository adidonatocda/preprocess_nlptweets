import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_nlptweets', #this should be unique
	version = '0.0.3',
	author = 'Critical Design Associates Inc.',
	author_email = 'adidonato@criticaldesign.net',
	description = 'This is preprocessing package for NLP',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)