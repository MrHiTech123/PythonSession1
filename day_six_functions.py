
def f(x):
    print("F is running")
    return (x + 5)

def swap_xes_and_os(board: str):
    return board.replace('X', 'o').replace('O', 'X').replace('o', 'O')

x = 'XOXOXOXOX'
while True:
    x = swap_xes_and_os(x)
    print(x)









