# fdm_hackathon_boggle
Hacks for the FDM Maximisation Hackathon 2018

## Config & Run
### Inputting the Board Manually
1. Edit `main.py`, change the `BOARD` variable according to the board, row by row.
2. Issue the command `python3 main.py`.
3. Check `output.txt`.

### Reading the Board Automatically (Practice Only)
1. Edit `onlinesolver.py`, change the `USERNAME`, `PASSWORD`, `FDMURL` and `QUESTION_NO` variables.
2. Issue the command `python3 online_solver.py`.
3. Check `output.json`.

## Idea
- Brute force based algorithm (DFS)
- Prunned when the traversed sequence is not a prefix of any word in the dictionary 
- Dicitonary stored as a sorted list. When queried, do a binary search, check whether it is an exact match. If not, check whether the word at the insertion point contains the query as a prefix. If it does, continue the search.
