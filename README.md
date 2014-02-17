BatchRename
===========

A regex centric batch file rename script.

usage: renameBatch \"path\" \"search_exp\" \"replacement_string\"


This script currently depends on the UNIX FS schema for path traversing. It also depends on the following tools: 'ls', 'grep', 'mv', and uses UNIX pipe. It also assumes that strings adhere to '\n' newlines, not '\r' carriage return format. Prompts user with altered list-prototype that the user can either modify or accept. Can be edited if no prompts are desired.
