"Blocked Galton Board" simulates a galton board with a block in the middle, displayed onto a bar chart. It is also plotted with the expected Gaussian curve.
The center of the block is positioned in the middle of th galton board, thus splitting the balls into two sets, and the value of BLOCK indicates the line you are placing it on.
TOTAL_LINES represents the number of rows of pins on a galton board. Thus the number of bins will be TOTAL_LINES + 1.

          o     TOTAL_LINES=5,
         ---    BLOCK=2
        o o o
       o o o o
      o o o o o
    | | | | | | |
 Bin 1 2 3 4 5 6 

You can also change the percentage in which the ball goes right, by changing the value of p.
The total number of tested balls is changed through TOTAL_BALLS.
Gaussian curves are drawn onto the same graph.

A shortened version without the block is available with the file "Galton Board".

You may notice that the position of the gaussian curve seems to be off when p is large or small. This is a problem that I have not solved yet. You are free to change the code of the value of u － the mean, and try out better versions.
