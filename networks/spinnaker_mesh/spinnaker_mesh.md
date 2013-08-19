tags: Networks
      TikZ

SpiNNaker Mesh Network Subsection
=================================

[Download `spinnaker-mesh.tex`](file://src/spinnaker-mesh.tex)
[Download `tikzlibraryhexagon.code.tex`](file://tikzlibraryhexagon.code.tex)

An illustration of a subsection of the hexagonal torus network used in
[SpiNNaker](http://apt.cs.man.ac.uk/projects/SpiNNaker/). This version is drawn
with all edges of equal distance rather than the misleading projection often
used with a normal 2D mesh augmented with diagonal links.

Usage
-----

	::latex
	% Requires tikzlibraryhexagon.code.tex in the current directory.
	\usetikzlibrary{hexagon}
	...
	\begin{document}
		\input{spinnaker-mesh}
	\end{document}

\begin{latex}[<preamble>]
	\usetikzlibrary{hexagon}
\end{latex}

\begin{latex}[--pdf SpiNNaker Mesh]
	\input{src/spinnaker-mesh}
\end{latex}

Can be varied in size by adjusting the clip and for loop dimensions. Sorry this
isn't done with a nice variable...
