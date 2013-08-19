img:file://parallel_signalling_skewed.png
tags: Signalling
      Python

Skew in Parallel Signals
========================

A (horrific) script which generates examples of parallel signals with varying
amounts of skew.

[Download `parallel_comms.py`](file://src/parallel_comms.py)

Usage
-----

	python parallel_comms.py [ASCII Message] [vertical spacing] [horizontal scaling] [maximum skew]

	::latex
	\input{|"python parallel_comms.py 'Hello, World!' 1.0 1.3 0"}

\begin{latex}[--pdf Parallel Signalling]
	\input{|"python src/parallel_comms.py 'Hello, World!' 1.0 1.3 0"}
\end{latex}

	::latex
	\input{|"python parallel_comms.py 'Hello, World!' 1.0 1.3 0.7"}

\begin{latex}[--pdf Parallel Signalling Skewed]
	\input{|"python src/parallel_comms.py 'Hello, World!' 1.0 1.3 0.7"}
\end{latex}
