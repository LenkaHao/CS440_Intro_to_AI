## Problem Definition
In this assignment, we are trying to:
- Implement a strategy to play the Atropos game intelligently.
- Design a static evaluator.
- Implement Minimax search algorithm and apply it to the Atropos Game.


## Method and Implementation
In order to correctly use the Minimax (with alpha-beta pruning) search algorithm, the most important thing we need to do is to assign scores to the nodes which are two steps ahead. So, we create a static evaluator, and assign high scores to nodes when they are in good situations for us, and low scores when they are in bad situations. After we finish building the static evaluator, we implement the Minimax method. This method will get highest score and lowest score alternately for each level, and finally help us to find the best move.
Functionss we use in our program:
- empty_neighbors: This function finds all empty spots around a move.
- will_lose: This function checks if this move will cause the script to lose the game.
- different_color_pair: This function counts the number of different colored neighboring pairs.
- same_color_neighbor: This function counts how many neighbors has the same color as the opponent's move.
- static_eval: This function assigns scores to this move according to its surroundings.
- minimax: This function implements the Minimax algorithm with alpha-beta pruning, will return the best move.


## Experiments
Our experiments include:
- Let the script play against a random player on the board of size 7.
- Play against a random player on the board of size 9.
Evaluation metrics:
- Win Rate in 10 games
- Overall Win Rate


## Results
- Experiment 1: Play against a random player on the board of size 7
Win Rate in 10 games: 80%

Win Rate in 10 games: 40%

Win Rate in 10 games: 60%

Win Rate in 10 games: 50%

Win Rate in 10 games: 60%

Overall Win Rate: 58% 

- Experiment 2: Play against a random player on the board of size 9
Win Rate in 10 games: 70%

Win Rate in 10 games: 80%

Win Rate in 10 games: 40%

Win Rate in 10 games: 60%

Win Rate in 10 games: 60%

Overall Win Rate: 62% 

- Experiment 3: Play against itself with board size of 7 and 8

Overall Win Rate in 50 games: 50% 


## Discussion and conclusion
The strengths and weaknesses of our method:
- Strength: Our minimax method and static evaluator help the script win for more than half times, and the win rate becomes higher when the board gets larger.
- Weakness: The win rate of our script is not very high, especially when the board size is small.
- Potential future works:
  - Add more evaluators to increase the win rate.
  - Use the minimax mathod to look more than 2 steps ahead.
  - Try some other search algorithms and see which one works better, or if necessary to combine them.


## Credits and Bibliography
Boston University Department of Computer Science, CS440, Professor Betke
This project is contributed by Jiatong Hao and Xianhui Li

