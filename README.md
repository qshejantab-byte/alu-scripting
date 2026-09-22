# alu-scripting

Ruby scripts using regular expressions, written for the `regular_expressions` project.

## Requirements

- Ruby, interpreted, run on Ubuntu
- Each script is executable and takes a single command-line argument
- All scripts use Ruby's regex methods (`match`, `scan`) to process the argument

## Directory: regular_expressions

| File | Description |
| --- | --- |
| `0-simply_match_school.rb` | Matches and prints every occurrence of "School" in the argument |
| `1-repetition_token_0.rb` | Matches `hbt` followed by 2 to 5 `t`s, then `n` |
| `2-repetition_token_1.rb` | Matches `hbtn` with an optional `b` |
| `3-repetition_token_2.rb` | Matches `hbt` followed by 1 to 5 `t`s, then `n` |
| `4-repetition_token_3.rb` | Matches `hbt` followed by zero or more `t`s, then `n` |
| `5-beginning_and_end.rb` | Matches a string that starts with `h`, ends with `n`, with exactly one character in between |
| `6-phone_number.rb` | Matches a string that is exactly 10 digits, nothing else |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Extracts and prints only the capital letters in the argument |
| `8-textme.rb` | Parses a TextMe log line and prints `[SENDER],[RECEIVER],[FLAGS]` |
| `9-passed_linkedin_regex_challenge.jpg` | Screenshot of completing the LinkedIn regex puzzle |

## Usage

```
./<script>.rb "<argument>"
```

Example:

```
$ ./0-simply_match_school.rb "Best School"
School
```

## Author

Quentin
