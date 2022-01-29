from visualizer import Board

def main():
    board = Board(cells=20)

    board.run_loop()
    
if __name__ == '__main__':
    main()