img:file://step_three_in_folding_the_boards.png
tags: Networks
      SpiNNer
      Python

SpiNNaker Network Folding
=========================

Shows the steps to fold a network of $4\times4$ threeboards in
[SpiNNaker](http://apt.cs.man.ac.uk/projects/SpiNNaker/). Red, Green and Blue
correspond to North, North-East, East respectively. Touching edges are
implicitly connected.

Uses the [SpiNNer](https://github.com/mossblaser/SpiNNer) library which must be
present in `/home/jonathan/Programing/Python/SpiNNer`. (Sorry...)

* [Download `boardsFoldedShift.py`](file://src/boardsFoldedShift.py)
* [Download `boardsFoldedSpaced.py`](file://src/boardsFoldedSpaced.py)
* [Download `boardsFoldedInterleaved.py`](file://src/boardsFoldedInterleaved.py)

Usage
-----

### Shift Boards Into Rectangle

	::latex
	\input{|"python boardsFoldedShift.py"}

\begin{latex}[--pdf Step one in folding the boards]
	\input{|"python src/boardsFoldedShift.py"}
\end{latex}

### Fold Boards Into $4\times2$

	::latex
	\input{|"python boardsFoldedSpaced.py"}

\begin{latex}[--pdf Step two in folding the boards]
	\input{|"python src/boardsFoldedSpaced.py"}
\end{latex}

### After Folding & Interleaving

	::latex
	\input{|"python boardsFoldedInterleaved.py"}

\begin{latex}[--pdf Step three in folding the boards]
	\input{|"python src/boardsFoldedInterleaved.py"}
\end{latex}

The size of the system can be changed in the python files with relative ease.
