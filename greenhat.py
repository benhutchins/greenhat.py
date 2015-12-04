# Copyright (c) 2015 Angus H. (4148)
# Distributed under the GNU General Public License v3.0 (GPLv3).
# Contributions by:
#  Benjamin Hutchins <ben@hutchins.co>

from datetime import date, timedelta
from random import randint
from time import sleep
import sys
import subprocess
import os
import urllib2

# returns a date string for the date that is N days before STARTDATE
def get_date_string(n, startdate):
	d = startdate - timedelta(days=n)
	rtn = d.strftime("%a %b %d %X %Y %z -0400")
	return rtn

def whatthecommit():
	return urllib2.urlopen("http://whatthecommit.com/index.txt").read()

# main app
def main(argv):
	should_push = False
	should_sleep = True
	use_whatthecommit = False
	verbose = False

	# Process argument flags (--)
	while len(argv) > 0 and argv[0][0:2] == "--":
		arg = argv.pop(0)
		print arg
		if arg is "--push":
			should_push = True
		elif arg == "--no-sleep":
			should_sleep = False
		elif arg in ("--wtc", "--whatthecommit"):
			use_whatthecommit = True
		elif arg in ("-v", "--verbose"):
			verbose = True
		else:
			print "Error: Bad arguments.", arg, "is not supported."
			sys.exit(1)

	if len(argv) < 1 or len(argv) > 2:
		print "Error: Bad input."
		sys.exit(1)
	n = int(argv[0])
	if len(argv) == 1:
		startdate = date.today()
	if len(argv) == 2:
		startdate = date(int(argv[1][0:4]), int(argv[1][5:7]), int(argv[1][8:10]))

	# Open the file we'll be updating (realwork.txt)
	file = open("realwork.txt", 'w')

	i = 0
	while i <= n:
		curdate = get_date_string(i, startdate)
		num_commits = randint(1, 10)

		if verbose:
			print "Processing", curdate, "(", i, "/", n, ") with", num_commits, "commits"

		for commit in range(0, num_commits):
			# Empty file
			file.seek(0)
			file.truncate()

			new_date = curdate + str(randint(0, 1000000))

			# Update a file (realwork.txt)
			file.write(new_date)
			file.flush()

			# Generate a commit message
			commit_message = whatthecommit() if use_whatthecommit else "update"

			# Perform git commit
			subprocess.call("git add realwork.txt", shell=True)
			os.environ["GIT_AUTHOR_DATE"] = curdate
			os.environ["GIT_COMMITTER_DATE"] = curdate
			subprocess.Popen(["git", "commit", "-m", commit_message])

			# Optionally push, since this is slow
			if should_push:
				subprocess.call("git push", shell=True)

			# Optionally sleep, since this makes the script slower
			if should_sleep:
				sleep(0.5)
		i += 1

	subprocess.call("git rm realwork.txt; git commit -m 'delete';", shell=True)

	if should_push:
		subprocess.call("git push", shell=True)

if __name__ == "__main__":
	main(sys.argv[1:])
