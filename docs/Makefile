SPHINXOPTS    ?= --builder html --fail-on-warning --fresh-env --write-all --quiet
SPHINXBUILD   ?= sphinx-build
SPHINXLINT   ?= sphinx-lint
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: html
html:
	@$(SPHINXLINT) "$(SOURCEDIR)" -i source/_tags/ -d role-with-double-backticks,role-without-backticks
	@$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: clean
clean:
	rm -rf "$(BUILDDIR)"
