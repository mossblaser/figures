subtitle: For Illustration Purposes Only
img:file://neural_network.png
tags: Neuroscience
      Python

Neural Network
==============

[Download `ann-example.py`](file://src/ann-example.py)

An illustrative example of a neural network. Mostly illustrates that it is a
graph and can highlight a single neuron and its links which is handy while
talking about fan-out.

Usage
-----

	::latex
	\input{|"python ann-example.py 0 "}

\begin{latex}[--pdf Neural Network]
	\input{|"python src/ann-example.py 0"}
\end{latex}

	::latex
	\input{|"python ann-example.py 1 "}

\begin{latex}[--pdf Neural Network With Neuron Highlighted]
	\input{|"python src/ann-example.py 1"}
\end{latex}

Some parameters can be found at the top of the file which tweak the probability
of connectivity and the size of the world. Uses a fixed seed for deterministic
output. Search for the line which outputs the "tikzpicture" to change scaling
options.
