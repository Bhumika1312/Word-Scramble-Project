# Simple Word Scramble Game Python Project

## Video Demo: [URL HERE]

## Table of Contents
- [Description](#description)
- [Project Structure](#project-structure)
- [Libraries](#libraries)
- [Run Locally](#run-locally)
- [Running Tests](#running-tests)
- [Design Choices](#design-choices)
- [Conclusion](#conclusion)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Description
The **Word Scramble Game** is an engaging and educational game designed to challenge and improve players' word-solving skills. In this game, players are presented with a scrambled version of a word and must guess the original word. It provides a fun way to test vocabulary and quick thinking. The game offers immediate feedback on guesses and keeps track of the player’s score, enhancing the competitive aspect of the game.

## Project Structure
This project is implemented in Python and consists of several key files:

1. **`project.py`**: This is the main script that contains the core functionality of the game.
   - **`main()`**: The entry point of the program. It initializes the game, displays the rules, and manages the game loop. Players are prompted with scrambled words, make guesses, and receive feedback. The final score is displayed when the player decides to exit.
   - **`display_rules()`**: This function prints the game rules to the console in a clear, formatted box. It provides players with instructions on how to play the game.
   - **`get_random_word()`**: This function selects a random word from a predefined list of words. It ensures that each game round features a different word to keep the game interesting.
   - **`scramble_word()`**: This function takes a word, scrambles its letters randomly, and returns the scrambled version. It uses the `random.shuffle()` method to achieve this.
   - **`check_guess()`**: This function compares the player’s guess with the correct word and returns a boolean indicating whether the guess is correct.

2. **`test_project.py`**: This file contains tests for the functions in `project.py`. It uses `pytest` to ensure that the core functionalities of the game work as expected.
   - **`test_scramble_word()`**: Tests the `scramble_word()` function to ensure it produces a scrambled word and checks that the scrambled word is not the same as the original.
   - **`test_check_guess()`**: Tests the `check_guess()` function to verify it correctly identifies correct and incorrect guesses.
   - **`test_get_random_word()`**: Tests the `get_random_word()` function to ensure it returns a word from the predefined list of words.

3. **`requirements.txt`**: This file lists the dependencies required for the project. Currently, it includes:
   - `pytest` for running tests. This ensures that the codebase remains reliable and that changes do not introduce new bugs.

## __Libraries__

__RANDOM__ : This module implements pseudo-random number generators for various distributions.. [(Readmore)](https://docs.python.org/3/library/random.html)

## Run Locally

Install dependencies
```python
pip install -r requirements.txt
```
```python
pip install -U pytest
```

## Running Tests

Use [python](https://www.python.org/) to run the application
```
python project.py
```

Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
pytest test_project.py
```

## Design Choices
In designing this project, several choices were made to balance simplicity and functionality:

- **Simplified Rules Display**: The `display_rules()` function uses a multi-line string for simplicity. This approach avoids complex formatting but still provides clear instructions to the user.
- **Scoring Mechanism**: A basic scoring system was implemented to keep track of correct guesses. This helps motivate players and provides a tangible measure of success.
- **Interactive Game Flow**: The game runs in a loop, allowing continuous play until the user chooses to exit. This design choice ensures an engaging experience and encourages multiple rounds of play.
- **Testing**: Basic unit tests were created to validate the core functions. While more extensive testing could be added, these tests cover critical functionalities and ensure that the core logic works correctly.

## Conclusion
The Word Scramble Game is a simple yet effective project that demonstrates fundamental programming concepts such as user input, conditional logic, and basic game design. It is an excellent example of how to create an interactive and enjoyable Python application. Feel free to explore the code, try out the game, and review the provided tests to understand how each component contributes to the overall functionality.

Thank you for checking out the Word Scramble Game!

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Author
**Bhumika Bhatt** You can find more of my projects on [GitHub](https://github.com/Bhumika1312).

## License
This project is licensed under the MIT License - see the [License](https://opensource.org/licenses/MIT) file for details.
