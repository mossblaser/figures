img:file://spiking_neuron.png
subtitle: For Illustration Purposes Only
tags: Neuroscience
      Python

Spiking Neuron
==============

An illustrative example of a spiking neuron model. Highly biologically
unrealistic and so not the sort of thing *really* used in simulations but gets
the jist across.

Internally it simulates a very simple model and generates the TikZ.

[Download `snn-example.py`](file://src/snn-example.py)

Usage
-----

\begin{latex}[--pdf Spiking Neuron]
	\input{|"python src/snn-example.py"}
\end{latex}

LaTeX Source:

	::latex
	\input{|"python snn-example.py"}

Some parameters can be found at the top of the file which tweak the probability
and effect of spikes. Uses a fixed seed for deterministic output.
