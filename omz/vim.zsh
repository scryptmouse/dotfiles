
bundles=${VIMBUNDLE:-~/.vim/bundle}

vimbundles() {
	for bundle in $(ls "$bundles"); do
		if [ -d "$bundles/$bundle/.git" ]; then
			# echo git bundles on stdout
			echo ${bundle%/}
		else
			# Echo non-git bundles on stderr
			echo ${bundle%/} >&2
		fi
	done
}

# Show normal vim bundles
alias vimbundles-git='vimbundles 2>/dev/null'

# Show bundles that are not currently tracked with git
alias vimbundles-nogit='vimbundles 2>&1 1>/dev/null'

vimbundles-urls() {
	for bundle in $(vimbundles-git); do
		(cd "$bundles/$bundle" && git remote -v | head -1 | awk '{print $2}')
	done
}
