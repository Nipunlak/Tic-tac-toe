# Tic Tac Toe
## [Video Demo](https://youtu.be/GxSl1NGBqLc)
### Description:
This program simulate simple Tic Tac Toe game on console. 

#### How the Program Works?
First, this program populates a 2D array with values from 1 to 9 and prints this array as a grid using Tabulate, with values inside the columns from 1 to 9. Then, it checks if one of the players (either 'X' or 'O') has won. If yes, the program prints the winner. If not, the program checks for a draw and prints 'Game Draw' if no winner is found. If there’s no winner or draw, the program prompts the users to input a value between 1 and 9 to mark their move. Before marking, the program checks if the user’s input value is valid. If it’s invalid, the program re-prompts the user until a valid value is provided. Once a valid move is made, the program marks the chosen cell with the user’s symbol ('X' or 'O'). The game stops if either a user wins or if the game results in a draw.


### Project Structure
- project.py
- test_project.py
- requirements.py
- README.md

### TODO:

#### Installation
```
Clone the project From the Github

```
```
$ pip install -r requirements.txt
```
#### Usage
Run the program python script `project.py` with [python](https://www.python.org/).
```
python project.py
```
Test the program python script `test_project.py` with [pytest](https://docs.pytest.org/en/stable/).
```
pytest test_project.py
```
After successfully running the program, it will prompt for a value from 1 - 9.

Then it will check for valid value if yes it will mark it.

this will continue unitl game draw or user wins.

## References
[^1]: [tabulate library](https://github.com/astanin/python-tabulate)