# autofileaway
Short python script that moves away your files using regular expression matching

### Usage
The structure of the config file **autofileaway.rules.csv** can be as follow:
```
"/source/file/path","source_regex_[0-9]{2}\.mp4","/destination/folder/"
```
This line does not rename the file and simply moves it to another place. The **[0-9]{2}** part is for handling episode count.
Note that dots have to be escaped with \ character.

```
"/source/file/path","source_regex_([0-9]{2})\.mp4","/destination/folder/","destination_name_(\1).mp4"
```
Here the file is renamed using regular expressions. Note the **()** in the source regex that permits you to handle variables.

> NOTE: By specifing the same source and destination directories you can juste reame files in place.

### Usefull regex example
```
.*(?i)Name[_ -]Of[_ -]a[_ -]Show.*[_ -]([0-9]{2}).*\.([A-z0-9]{3})$
```
This is an good regex I often use. Here is some explanations
- .* permit the file name to start with what it wants
- (i?) ignore case
- [_ -] words can be separated by - or _ or space
- .*[_ -]([0-9]{2}).* be flexible around the episode count to also match files with ep10v2 in it
- \.([A-z0-9]{3})$ escape the dot, permit all 3 character long extention and specify clearly that this should be the end of the file name using $

> The output format string should look something like this : "Name Of a Show \1.\2"
