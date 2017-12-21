""""
==========
 Examples 
==========
  searchsploit afd windows local
  searchsploit -t oracle windows
  searchsploit -p 39446
  searchsploit linux kernel 3.2 --exclude="(PoC)|/dos/"

  For more examples, see the manual: https://www.exploit-db.com/searchsploit/

=========
 Options 
=========
   -c, --case     [Term]      Perform a case-sensitive search (Default is inSEnsITiVe).
   -e, --exact    [Term]      Perform an EXACT match on exploit title (Default is AND) [Implies "-t"].
   -h, --help                 Show this help screen.
   -j, --json     [Term]      Show result in JSON format.
   -m, --mirror   [EDB-ID]    Mirror (aka copies) an exploit to the current working directory.
   -o, --overflow [Term]      Exploit titles are allowed to overflow their columns.
   -p, --path     [EDB-ID]    Show the full path to an exploit (and also copies the path to the clipboard if possible).
   -t, --title    [Term]      Search JUST the exploit title (Default is title AND the file's path).
   -u, --update               Check for and install any exploitdb package updates (deb or git).
   -w, --www      [Term]      Show URLs to Exploit-DB.com rather than the local path.
   -x, --examine  [EDB-ID]    Examine (aka opens) the exploit using $PAGER.
       --colour               Disable colour highlighting in search results.
       --id                   Display the EDB-ID value rather than local path.
       --nmap     [file.xml]  Checks all results in Nmap's XML output with service version (e.g.: nmap -sV -oX file.xml).
                                Use "-v" (verbose) to try even more combinations
       --exclude="term"       Remove values from results. By using "|" to separated you can chain multiple values.
                                e.g. --exclude="term1|term2|term3".

=======
 Notes 
=======
 * You can use any number of search terms.
 * Search terms are not case-sensitive (by default), and ordering is irrelevant.
   * Use '-c' if you wish to reduce results by case-sensitive searching.
   * And/Or '-e' if you wish to filter results by using an exact match.
 * Use '-t' to exclude the file's path to filter the search results.
   * Remove false positives (especially when searching using numbers - i.e. versions).
 * When updating or displaying help, search terms will be ignored.

"""

from subprocess import check_output
import json
PATH = "/opt/exploit-database/searchsploit"


def search(*keywords) -> dict: 
    # get result as json format
    searchword_list = [PATH, "-j"] + list(keywords)
    result_json = check_output(searchword_list)

    return json.loads(result_json.decode('utf-8'), strict=False)
