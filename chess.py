from typing import List, Tuple


def main():

    class PLAYER():

        def __init__(self, color: int, king_pos) -> None:
            
            self.pieces_left = []
            self.king_pos = king_pos
            self.color = color

        def update_king_pos(self, king_pos: List[int]) -> None:
            self.king_pos = [king_pos[0], king_pos[1]]

    class CHESS_RULES():

        def isin_check(self, col_mov: int, board: List[List[int]], king_pos) -> bool:
            pass

            return False

        def check_rules(self):
            
            self.isin_check()

    
    class CHESS_BOARD():

        #--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==#

        def __init__(self) -> None:

            self.MOVE_Y_REFFERENCE = {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8
            }

            self.MOVEMENT_TYPE_REFFERENCE = {

                'K': {
                    'VALUE': 0,
                    'MOVES': 1,
                    'AXIS_X': [1, 0],
                    'AXIS_Y': [0, 1],
                },
                'Q':{
                    'VALUE': 1,
                    'MOVES': 8,
                    'AXIS_X': [8, 0],
                    'AXIS_Y': [0, 8],
                    'AXIS_Z': 0
                },
                'F':{ # KNIGHT
                    'VALUE': 4,
                    'MOVES': 2,
                    'AXIS': -1
                }
            }

            self.BOARD_PIECES_REFFERENCE: List[dict[dict]] = {
                0: {
                    'name': 'KING',
                    'value': 0,
                    'movement_type': self.MOVEMENT_TYPE_REFFERENCE['K'],
                },
                1: {
                    'name': 'QUEEN',
                    'value': 1,
                    'movement_type': [
                        self.MOVEMENT_TYPE_REFFERENCE['Q']['AXIS_X'],
                        self.MOVEMENT_TYPE_REFFERENCE['Q']['AXIS_Y'],
                    ]
                },
                2: {
                    'name': 'rook',
                    'value': 2,
                    'movement_type': [
                        self.MOVEMENT_TYPE_REFFERENCE['Q']['AXIS_X'],
                        self.MOVEMENT_TYPE_REFFERENCE['Q']['AXIS_Y'],
                    ]
                },
                3: {
                    'name': 'bishop',
                    'value': 3,
                    'movement_type': self.MOVEMENT_TYPE_REFFERENCE['Q']['AXIS_Z'],
                },
                4: {
                    'name': 'KNIGHT',
                    'value': 4,
                    'movement_type': self.MOVEMENT_TYPE_REFFERENCE['F'],
                },
                5: {
                    'name': 'pawn',
                    'value': 5,
                    'movement_type': self.MOVEMENT_TYPE_REFFERENCE['K'],
                }
            }

            self.BOARD: List[List[int]] = [
                [2 , 3 , 4 , 0 , 1 , 4 , 3 , 2 ],
                [5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 ],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [11, 11, 11, 11, 11, 11, 11, 11],
                [8 , 9 , 10 , 6 , 7 , 10 , 9 , 8]
            ]

            self.test_board = [
                
                [-1, -1, -1, -1, 0, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [1, -1, -1, -1, -1, -1, -1, -1],

            ]

        #--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==#

        def __str__(self) -> str:
            return str(self.BOARD_PIECES_REFERENCE[0]['movement_type']['MOVES'])

        #--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==#

        def move(self, _move, color):

            """Function to move a piece on the board with the correct rules, if the move is invalid except -1, valid input is required to continue the game"""

            position_obj = self.det_pos(cur_pos=_move[0], fut_pos=_move[1], board=self.test_board, color=color)

            self.det_move(position_obj)

        #--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==#

        def det_pos(self, cur_pos: str, fut_pos: str, board: List[List[int]], color) -> None:

            """ ALL POSSIBLE PIECES TO MOVE: Qxx Kxx Fxx, Q standing for queen type movement, F for knight, K for king """

            if cur_pos[0] != fut_pos[0]:
                return -1

            ACT_PIECE = None

            if len(fut_pos) == 2 :

                ACT_PIECE = '5'
                PIECE: str = 'K'
                FUT_POS: str = fut_pos[0:]
                CUR_POS: str = cur_pos[0:]

            else:

                PIECE: str = fut_pos[0]

                if PIECE == 'Q':
                    ACT_PIECE = '1'
                elif PIECE == 'F':
                    ACT_PIECE = '4'
                elif PIECE == 'B':
                    ACT_PIECE = '3'
                elif PIECE == 'R':
                    ACT_PIECE = '2'
                elif PIECE == 'K':
                    ACT_PIECE = '0'

                FUT_POS: str = fut_pos[1:]
                CUR_POS: str = cur_pos[1:]


            TRANSLATE_Y_X_CUR: List[int] = [int(CUR_POS[1])-1, self.MOVE_Y_REFFERENCE[CUR_POS[0]]-1]
            TRANSLATE_Y_X: List[int] = [int(FUT_POS[1])-1, self.MOVE_Y_REFFERENCE[FUT_POS[0]]-1]

            if PIECE != 'N' or PIECE != 'K' or PIECE != 'Q':

                if PIECE == 'R':
                    PIECE = 'Q'

                if PIECE == 'B':
                    PIECE = 'Q'

            return [PIECE ,TRANSLATE_Y_X_CUR, TRANSLATE_Y_X, ACT_PIECE, board, color]

        #--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==#

        def det_move(self, pos_info: Tuple[str, List[int], List[int]]) -> None:

            """ DETERMINE IF A PIECE CAN MOVE AND IF SO, WHERE"""

            player_color = pos_info[-1]
            act_piece = pos_info[-3]
            board = pos_info[-2]
            PIECE = pos_info[0]
            TRANSLATE_Y_X_CUR = pos_info[1]
            TRANSLATE_Y_X = pos_info[2]
            print('-----------------')

            if board[TRANSLATE_Y_X[0]][TRANSLATE_Y_X[1]] == -1:

                print(f'{PIECE} can move to {TRANSLATE_Y_X[0]}, {TRANSLATE_Y_X[1]}')
                
                if PIECE == 'K':
                    
                    if player_color == 0:
                        
                        print(PLAYER_WHITE.king_pos)
                        PLAYER_WHITE.update_king_pos(TRANSLATE_Y_X)
                        print(PLAYER_WHITE.king_pos)
                    
                board[TRANSLATE_Y_X[0]][TRANSLATE_Y_X[1]] = int(act_piece)
                board[TRANSLATE_Y_X_CUR[0]][TRANSLATE_Y_X_CUR[1]] = -1
            
            else:
                CHESS_RULES.check_rules()

            for y in board:
                print(y)
            return board

        #--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==#

    PLAYER_WHITE = PLAYER(color=0, king_pos=[0, 4])
    PLAYER_BLACK = PLAYER(color=1, king_pos=[4, 7])
    CHESS_BOARD = CHESS_BOARD()
    CHESS_BOARD.move(['Ke1', 'Ke2'], PLAYER_WHITE.color)
    CHESS_BOARD.move(['Ke2', 'Ke3'], PLAYER_WHITE.color)
    CHESS_BOARD.move(['Ke3', 'Ke4'], PLAYER_WHITE.color)
    CHESS_BOARD.move(['Ke4', 'Kf5'], PLAYER_WHITE.color)
    CHESS_BOARD.move(['Kf5', 'Kf4'], PLAYER_WHITE.color)

if __name__ == '__main__':
    main()