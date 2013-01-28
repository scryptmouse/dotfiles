alias cdc="cd ${ZSH_CUSTOM}"
alias rm='rm -iv'
alias mv='mv -iv'
alias cp='cp -iv'

alias wherearemy='which'
alias jake="noglob jake"
alias rake="noglob rake"

alias cx='chmod +x'
alias c0='chmod 0000'

macvim="/Applications/MacVim.app/Contents/MacOS/Vim"

if [ -x "$macvim" ]; then
	alias vim=$macvim
	EDITOR=$macvim
	export EDITOR
fi

memory_used() {
	# Must use awk instead of cut in case of double-digit memory usage
	ps -eo pmem,comm | fgrep "$1" | awk '{print $1}' | paste -sd+ | bc
}

rezsh() {
	source ~/.zshenv
	source ~/.zshrc
}

# Load stuff for mielikki
if [[ $(hostname -s) == "mielikki" ]]; then
	alias ics_clients="nmap -nsP 192.168.2.0/24"
	alias pear="php /usr/lib/php/pear/pearcmd.php"
	alias pecl="php /usr/lib/php/pear/peclcmd.php"
	alias lastmysql="tail -30 /usr/local/var/mysql/mielikki.log"
fi

if [[ $(uname) == "Darwin" ]]; then
	# Unset say function from perl plugin on Darwin platforms
	unset -f say 2>/dev/null
fi

IS_GNU_LS="no"

# Test if we are running GNU LS
if ls -d --version >/dev/null 2>&1; then
	IS_GNU_LS="yes"
	LS_OPTIONS="--group-directories-first --color=auto -Fh"

	alias ls="ls $LS_OPTIONS"
	alias l="ls -lA"
	alias ll="ls -o"

	if [ -r "~/.dircolors" ]; then
		eval `dircolors ~/.dircolors`
	fi
fi

export IS_GNU_LS
