# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 

```bash
rm # general case file removal
rm -rf filename # recursive force deletion, don't ever do this on anything important or high level
# or you may erase your computer, still useful for removing things like directories with their own
# subdirectories (rails project?). also a classic mean programmer joke.
cd .. # up one level
cd # return to user level
ls # show files in directory
ls -a # show all files, including hidden files, in a directory
mkdir # make a folder
touch # create a file
ditto # copies a folder, useful for making backups
pwd # print working directory, lets you know where you are in the folder structure
cp # copy files
mv # move files, note that the syntax for this often functions to rename files rather 
# than move them the way you might think with a GUI. 

### late addition

grep # allows you to use regexes to find strings within files -from the command line-
# I'm not very good regexes but this looks pretty great
# http://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples




```

---

###Q2.  List Files in Unix   

What do the following commands do:  

> > Answers w/Commands:

`ls`  # lists the normal files in the current directory

`ls -a` # includes hidden files in the listing  

`ls -l`# includes size of files, owner, folder, and permissions, modified date/time

`ls -lh` # similar to ls -l above, the addition of the "h" flag toggles human-readable form

`ls -lah` # all hidden+normal files, with additional data per "l" flag above, in human-readable form per h flag

`ls -t` # files sorted by time modified

`ls -Glp` #G flag highlights (using colors) folders and directories differently, "l" flag provides additional information as above, "p" flag appends "/" to directories to highlight their folder structure vs regular files

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 5 more favorites:

Full confession, I'm not as in love with the ls command as others may be. Or at least, I'm not seeing all the utility of multiple display options just yet. 

`ls - R` # the R flag recursively displays lower-level files

`ls -ltr` # lower-case r flag combined with lt allows for reverse-order sorting


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> Per the linux man-pages: "The xargs utility reads space, tab, newline and end-of-file delimited strings from the standard input and executes utility with the strings as arguments."

>> What this means, in plainer english, is that xargs is a method for chaining command line actions together, especially since many command line actions normally call for a newline to execute.

>> Here's a core example of xargs, plundered from [Here](http://www.thegeekstuff.com/2013/12/xargs-examples/). In this case, the .find command is used with xargs to remove all files of a certain type, in this case files with the ".c" extension. For example, running the same command with .c replaced with .md the dsp directory would delete all of the markdown files, including the readme and this file! (So don't do it in this directory. Actually, be wary of rm -rf generally.)


```bash
$ ls
one.c  one.h  two.c  two.h

$ find . -name "*.c" | xargs rm -rf

$ ls
one.h  two.h
```

>> We could do a similar thing with renaming files, using xargs to change the format of all text files in a certain folder to markdown, etc. The utility you'll get out of xargs is probably directly relational to the large-scale operations you want to run from the command line.

<!-- >> One thing you can do with xargs is to use the -n flag to limit the per-line output.

```bash
# -n limits output per-line, examples 
echo a b c d e f g h i | xargs -n 2
echo a b c d e f g h i | xargs -n 3
echo a b c d e f g h i | xargs -n 5
``` -->

<!-- > > Many command line options have multiple flags that allow them to be used in different ways. For example, when I input

'ls --help' into the command line, I get the following response

```bash
ls: illegal option -- -
usage: ls [-ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1] [file ...]
```

This gives me a list of all the arguments I could apply to the ls command, in various ways. For some commands, however, certain combinations of flags written in a certain order might produce an error.
 -->
 

