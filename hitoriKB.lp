% Hitori puzzle
% Ángela María Martín García	login: angela.martin

#show result/3.
value(0..9;a;b;c).

% Every square is either black or not:
1 { black(X,Y); not black(X,Y) } 1 :- cell(X,Y,_).

% The same number cannot appear twice or more in a row/column:
:- cell(X,Y,N), cell(X,Y',N), not black(X,Y), not black(X,Y'), Y!=Y'.
:- cell(X,Y,N), cell(X',Y,N), not black(X,Y), not black(X',Y), X!=X'.

% black squares cannot be 4-connected:
:- black(X,Y), black(X',Y), X'==X+1.
:- black(X,Y), black(X,Y'), Y'==Y+1.

% non black squares have to be 4-connected:
neighbours(X,Y,X',Y) :- cell(X,Y,_), cell(X',Y,_), not black(X,Y), not black(X',Y), X'==X+1.
neighbours(X,Y,X,Y') :- cell(X,Y,_), cell(X,Y',_), not black(X,Y), not black(X,Y'), Y'==Y+1.
neighbours(X,Y,X',Y') :- neighbours(X',Y',X,Y).

connected(X,Y,X',Y') :- neighbours(X,Y,X',Y'), not black(X,Y), not black(X',Y').
connected(X1,Y1,X3,Y3) :- connected(X1,Y1,X2,Y2), connected(X2,Y2,X3,Y3).
:- not black(X1,Y1), cell(X1,Y1,_), not black(X2,Y2), cell(X2,Y2,_), not connected(X1,Y1,X2,Y2), (X1,Y1) != (X2,Y2).

% use 0 for black cells and copy the original value for the rest
result(X,Y,0) :- cell(X,Y,N), black(X,Y).
result(X,Y,N) :- cell(X,Y,N), not black(X,Y).
