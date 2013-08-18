tags: Networks
      TikZ

Torus Construction
==================

* [Download `torus-flat.tex`](file://src/torus-flat.tex)
* [Download `torus-pipe.tex`](file://src/torus-pipe.tex)
* [Download `torus-3D.tex`](file://src/torus-3D.tex)

Shows how the torus network gets its name by transforming a torus in the
conventional 2D form (with wrap-around links) and turning it into a torus.

Usage
-----

\begin{latex}[<preamble>]
	\usepackage{tikz3d}
\end{latex}

	::latex
	\input{torus-flat}

\begin{latex}[--pdf Torus Flat]
	\input{src/torus-flat}
\end{latex}

	::latex
	\input{torus-pipe}

\begin{latex}[--pdf Torus Rolled into Tube]
	\input{src/torus-pipe}
\end{latex}

	::latex
	\input{torus-3D}

\begin{latex}[--pdf Torus 3D]
	\input{src/torus-3D}
\end{latex}

Some configuration is available at the top of each file. Requires Tikz3D (Part
of [Tex-SX](http://bazaar.launchpad.net/~tex-sx/tex-sx/development/files)) to
compile.
