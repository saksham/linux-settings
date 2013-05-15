#!/usr/bin/python
import os;

vim_bundles_dir = os.getcwd();
files = os.listdir(vim_bundles_dir)
for bundle in files:
	os.chdir(vim_bundles_dir)
	if os.path.isdir(bundle) and os.listdir(bundle).index('.git') != -1:
		print "Updating bundle %s..." % bundle
		os.chdir(bundle)
		os.system("git pull");

