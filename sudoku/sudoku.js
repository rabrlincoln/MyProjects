function submit() {
  document.getElementById("win").innerHTML = "";
  var board = [["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"],["x","X","X","x","x","x","X","x","x"]];
  var allPossibleValues = [[],[],[],[],[],[],[],[],[]];
  for (var i = 0; i < 9; i++) {
    for (var j = 0; j < 9; j++) {
      //set all everybox to all values
      allPossibleValues[i][j] = [1,2,3,4,5,6,7,8,9];
    }
  }

      for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
      var id = `${i+1}${j+1}`;
      if(document.getElementById(id).value) {
        info = [i, j, parseInt(document.getElementById(id).value)];
        boards = enterNumber(allPossibleValues, board, info);
        //make table
        allPossibleValues = boards[0];
        board = boards[1];
      }
    }
  }
change = true;
while (change) {
  if (hiddenSingle(allPossibleValues)) {
    info = hiddenSingle(allPossibleValues);
    boards = enterNumber(allPossibleValues, board, info);
    allPossibleValues = boards[0];
    board = boards[1];
  }
  else if (onceInRow(allPossibleValues)) {
    info = onceInRow(allPossibleValues);
    boards = enterNumber(allPossibleValues, board, info);
    allPossibleValues = boards[0];
    board = boards[1];
  }
  else if (onceInColumn(allPossibleValues)) {
    info = onceInColumn(allPossibleValues);
    boards = enterNumber(allPossibleValues, board, info);
    allPossibleValues = boards[0];
    board = boards[1];
  }
  else if (onceInBox(allPossibleValues)) {
    info = onceInBox(allPossibleValues);
    boards = enterNumber(allPossibleValues, board, info);
    allPossibleValues = boards[0];
    board = boards[1];
  }
  else {
    change = false;
  }
}

  //print real values into grid
  for (var i = 0; i < 9; i++) {
    for (var j = 0; j < 9; j++) {
      if (board[i][j] <=9 && board[i][j] != 0) {
        var id = `${i+1}${j+1}`;
        document.getElementById(id).value = `${board[i][j]}`;
      }
      else {
        document.getElementById("win").innerHTML = "Sorry, could not beat the sudoku";
      }
    }
  }
}

function removeNum (array, num) {
  const index = array.indexOf(num);
  if (index > -1) {
    array.splice(index, 1);
  }
  return array;
}

function findNum (array, num) {
  const index = array.indexOf(num);
    return index;
}

function hiddenSingle(allPossibleValues) {
  for (var i = 0; i < 9; i++) {
    for (var j = 0; j < 9; j++) {
      if (allPossibleValues[i][j].length == 1) {
        row = i;
        column = j;
        value = allPossibleValues[i][j][0];
        return [row,column,value];
      }
    }
  }
  return false;
}

function onceInRow(allPossibleValues) {
  count = [0,0,0,0,0,0,0,0,0];
  for (var i = 0; i < 9; i++) {
   for (var j = 0; j < 9; j++) {
     for (var k = 0; k < allPossibleValues[i][j].length; k++) {
       count[allPossibleValues[i][j][k]-1]++;
     }
   }
   for (var l = 0; l < 9; l++) {
     if (count[l] == 1) {
       for (var m = 0; m < 9; m++) {
         if (findNum(allPossibleValues[i][m], l+1) > -1) {
           column = m;
           row = i;
           value = l+1;
           return [row, column, value];
         }
       }
     }
   }
   count = [0,0,0,0,0,0,0,0,0];
  }
  return false;
}

function onceInColumn(allPossibleValues) {
  count = [0,0,0,0,0,0,0,0,0];
  for (var i = 0; i < 9; i++) {
   for (var j = 0; j < 9; j++) {
     for (var k = 0; k < allPossibleValues[j][i].length; k++) {
       count[allPossibleValues[j][i][k]-1]++;
     }
   }
   for (var l = 0; l < 9; l++) {
     if (count[l] == 1) {
       for (var m = 0; m < 9; m++) {
         if (findNum(allPossibleValues[m][i], l+1) > -1) {
           row = m;
           column = i;
           value = l+1;
           return [row, column, value];
         }
       }
     }
   }
   count = [0,0,0,0,0,0,0,0,0];
  }
  return false;
}

function onceInBox(allPossibleValues) {
  count = [0,0,0,0,0,0,0,0,0];
  for (var y = 0; y < 9; y+=3) {
    for (var i = 0; i < 3; i++) {
      for (var j = 0; j < 3; j++) {
        for (var k = 0; k < allPossibleValues[i+y][j+y].length; k++) {
          count[allPossibleValues[i+y][j+y][k]-1]++;
        }
      }
    }
    for (var l = 0; l < 9; l++) {
      if (count[l] == 1) {
        for (var m = 0; m < 3; m++) {
          for (var n = 0; n < 3; n++) {
            if (findNum(allPossibleValues[m+y][n+y], l+1) > -1) {
              row = m+y;
              column = n+y;
              value = l+1;
              return [row, column, value];
            }
          }
        }
      }
    }
    count = [0,0,0,0,0,0,0,0,0];
  }
}

function enterNumber(allPossibleValues, board, info) {
  row = info[0];
  column = info[1];
  value = info[2];
  board[row][column] = value;
  allPossibleValues[row][column] = [];
  for (var i = 0; i < 9; i++) {
    removeNum(allPossibleValues[row][i], value);
    removeNum(allPossibleValues[i][column], value);
  }
  for (var l = 0; l < 3; l++) {
    for (var m = 0; m < 3; m++) {
      if (row<3 && column < 3) {
        removeNum(allPossibleValues[l][m],value);
      }
      else if (row < 3 && column<6) {
        removeNum(allPossibleValues[l][m+3],value);
      }
      else if (row< 3 && column<9) {
        removeNum(allPossibleValues[l][m+6],value);
      }
      else if (row< 6 && column<3) {
        removeNum(allPossibleValues[l+3][m],value);
      }
      else if (row< 6 && column<6) {
        removeNum(allPossibleValues[l+3][m+3],value);
      }
      else if (row< 6 && column<9) {
        removeNum(allPossibleValues[l+3][m+6],value);
      }
      else if (row< 9 && column<3) {
        removeNum(allPossibleValues[l+6][m],value);
      }
      else if (row< 9 && column<6) {
        removeNum(allPossibleValues[l+6][m+3],value);
      }
      else if (row< 9 && column<9) {
        removeNum(allPossibleValues[l+6][m+6],value);
      }
    }
  }
  return [allPossibleValues, board];
}
