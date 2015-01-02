# Subversion & Diff ------------------------------------------------
export SV_USER='hanbingfeng'  # Change this to your username that you normally use on subversion (only if it is different from your logged in name)
export SVN_EDITOR='${EDITOR}'

alias sv='svn --username ${SV_USER}'
alias svimport='sv import'
alias svcheckout='sv checkout'
alias svstatus='sv status'
alias svupdate='sv update'
alias svstatusonserver='sv status --show-updates' # Show status here and on the server
alias svcommit='sv commit'
alias svadd='svn add'
alias svaddall='svn status | grep "^\?" | awk "{print \$2}" | xargs svn add'
alias svdelete='sv delete'
alias svhelp='svn help' 
alias svblame='sv blame'

# svn external merge tool set
export SVN_MERGE='~/Applications/svn_ext_merge_araxis_compare_3.py'

svgetinfo (){
    sv info $@
    sv log $@
}

# returns path info get from 'svn status', by matching with path segment passed in
svmatchpath (){
    string=`svn status | grep $@ | awk '{print $2}'`

    echo $string
}

# You need to create fmdiff and fmresolve, which can be found at: http://ssel.vub.ac.be/ssel/internal:fmdiff
alias svdiff='sv diff --diff-cmd ~/Applications/svn_ext_diff_araxis_compare.py' # OS-X SPECIFIC
# Use diff for command line diff, use fmdiff for gui diff, and svdiff for subversion diff

# NodeJS global env
# global NodeJS modules at /usr/local/lib/node_modules, no need to set
