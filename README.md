# greenhat <img src="https://github.com/4148/greenhat/blob/master/greenhat.png" alt="greenhat image" width="10%" height="10%"/>
greenhat is a quick hack for decorating your GitHub contribution calendar with commits for the past `n` days. It uses the `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environmental variables to make commits appear in the past. Be warned that greenhat will clobber your repository's commit history.

## How to Use
Place `greenhat.py` in your Git repository. Make sure your [remote repository URL is set](https://help.github.com/articles/adding-a-remote/), and that you have a [public SSH key set up](https://help.github.com/articles/generating-ssh-keys/). Then run the script with the python interpreter, with an integer specifying `n` number of days before today to generate commits for. E.g.,

	python greenhat.py <n>

It might take a while to generate all the commits. If greenhat stops before it finishes, you can resume where you last left off by specifying a date before today when you want it to resume, like so:

	python greenhat.py <n> <date>

`n` is the remaining days you want to generate commits for, and `date` is a date string in the form `yyyy-mm-dd`  (e.g., 2013-04-05).

### Arguments

`greenhat.py` accepts a few arguments to make things more fun or faster.

- `--push` will perform a `git push` after each `git commit`, makes the script much slower.
- `--no-sleep` will skip the `0.5s` sleep between commits, making the script much faster but uses a lot more resources.
- `--whatthecommit` will use [whatthecommit.com](http://whatthecommit.com/) to generate commit messages.
- `--commits=10` set the maximum number of commits that can happen per day (default is `10`).
- `--jump=5` randomly jump ahead in time by a random number of days, between 1 and the given value so your calendar contribution calendar isn't quite as decorated (by default days are not skipped)
- `--verbose` will output additional data to let you see overall process.

These arguments should go before `<n>` and the optional `<date>` arguments.

### An Example

The following calendar is the result of running `python greenhat.py 365`:

<img src="https://github.com/4148/greenhat/blob/master/example.png" alt="example image"/>

Beautiful, isn't it?

Enjoy your decorated calendar!

## License
greenhat is distributed under the GNU General Public License v3.0 (GPLv3).
