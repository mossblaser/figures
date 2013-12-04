img:file://spinnaker_torus.png
tags: Networks
      TikZ

SpiNNaker Torus Network (Without Wrap-around Links)
===================================================

An illustration of a hexagonal torus network as used in
[SpiNNaker](http://apt.cs.man.ac.uk/projects/SpiNNaker/) with the wrap-around
links stubbed. This version is drawn with all edges of equal distance rather
than the misleading projection often used with a normal 2D mesh augmented with
diagonal links.

[Download `spinnaker-torus.tex`](file://src/spinnaker-torus.tex)

Usage
-----

	::latex
	\input{spinnaker-torus}

\begin{latex}[--pdf SpiNNaker torus]
	\input{src/spinnaker-torus}
\end{latex}

Can be varied in size by adjusting the clip and for loop dimensions. Sorry this
isn't done with a nice variable...
