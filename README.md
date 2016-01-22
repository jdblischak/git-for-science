# A quick introduction to version control with Git and GitHub

This paper has been published ([link to final version][final]) as part of the PLOS Computational Biology [Education Collection][education].

[final]: http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668
[education]: http://collections.plos.org/compbiol-education

## Synopsis and Motivation

This is the repository for the paper "A quick introduction to version control with Git and GitHub".
The goal of this paper was to introduce scientists to the concepts behind version control (using Git) so that they can incorporate these practices into their workflows.
The [manuscript](https://www.authorea.com/users/5990/articles/17489/_show_article) was written using the [Authorea](http://www.Authorea.com) platform.

In the manuscript, we encourage readers to practice using GitHub by contributing to this repository.
The full details are explained in the section [Contribute to other projects][contribute], but briefly the steps are:

*  Fork the repository
*  `git clone` the fork locally
*  Add a file called {GitHub_username}.txt to the `readers` folder
*  `git add` + `git commit`
*  `git push` the commit to GitHub
*  Issue a Pull Request (PR) to incorporate the change into this repository

Take a look in the [readers](readers) folder to see all of the contributions from anyone who has had a Pull Request accepted.
If you haven't contributed already, we'd love to see your PR!

[contribute]: https://www.authorea.com/users/5990/articles/17489/_show_article#article-paragraph-contribute__minus__to__minus__other__minus__projects__dot__tex-landing-welcome

## Example code

The example code, which were provided as supplementary files, can be found in the sudirectory `code`.
If you're interested in running the scripts, please see the [README](code/README.md) in that directory for instructions.

## Build the document

The full tex file and compiled PDF can be obtained from the "Export document" on the [Authorea page][authorea-page] for this article.
Choose the PLOS 2015 template for the best results.

However, to both maintain a presentable version for display on Authorea (e.g. contain the figures) and a version that complies with the [PLOS submission guidelines][plos-submit] (e.g. only contain figure captions but not images), we created a [custom Python script](build-full-article.py) to build the final [TEX](blischak-et-al.tex) and [PDF](blischak-et-al.pdf) files for submission.
Run it as follows:

```python
python build-full-article.py > blischak-et-al.py
```

You should be able to run it with either major version of Python.
We were able to run it with either Python 2.7.10 or Python 3.4.3.

[authorea-page]: https://www.authorea.com/users/5990/articles/17489
[plos-submit]: http://journals.plos.org/plosone/s/latex

## Contributors

Thank you to all of our [contributors](https://github.com/jdblischak/git-for-science/graphs/contributors)!

## License

Please see our [license](LICENSE)
