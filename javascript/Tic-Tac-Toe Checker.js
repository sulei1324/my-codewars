function getZeroNum(board){
    var n = 0;
    for(var i = 0; i < board.length; i++){
        board[i].forEach(function(v){
//           console.log(v);
           if(v == 0){
               n++;
           }
        });
    }
    return n;
}


function isSolved(board){
    var x, y;
    var zeros_num = getZeroNum(board);
    for(var player = 1; player <= 2; player++){
        for(var p = 0; p < check_positon.length; p++){
            x = check_positon[p][0];
            y = check_positon[p][1];
//            console.log([x, y, player]);
            if(board[x][y] == player){
                for(var i = 0; i < winningModel[x][y].length; i++){
                    var flag = 1;
                    for(var j = 0; j < winningModel[x][y][i].length; j++){
                        var x1 = winningModel[x][y][i][j][0];
                        var y1 = winningModel[x][y][i][j][1];
//                        console.log([x1, y1]);
                        if(board[x1][y1] != player){
                            flag = 0;
                            break;
                        }

                    }
                    console.log(flag);
                    if(flag == 1){
                        return player;
                    }
                }

            }
        }
    }
    if(zeros_num == 0){
        return 0;
    }else{
        return -1;
    }

}

winningModel = [[],[],[]];
winningModel[0][0] = [
    [[0,1],[0,2]],
    [[1,0],[2,0]],
    [[1,1],[2,2]]
];
winningModel[0][1] = [
    [[1,1],[2,1]]
];
winningModel[0][2] = [
    [[1,1],[2,0]],
    [[1,2],[2,1]]
];
winningModel[1][0] = [
    [[1,1],[1,2]]
];
winningModel[2][0] = [
    [[2,1],[2,2]]
];
check_positon = [[0,0],[0,1],[0,2],[1,0],[2,0]];

b = [[2, 2, 2],
     [0, 1, 1],
     [0, 0, 0]
    ];

console.log(isSolved(b));

//console.log(getZeroNum(b));