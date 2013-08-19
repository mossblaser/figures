img:file://differential_signalling.png
tags: Signalling
      Python

High Speed Serial Signals
=========================

A (horrific) script which generates examples of serial signals with options to
distort and encode the messages. Relies on `eightbtenb.py`, an equally horrific
and known incorrect 8b10b encoder/decoder implementation (good enough for
figures...).

* [Download `serial_comms.py`](file://src/serial_comms.py)
* [Download `eightbtenb.py`](file://src/eightbtenb.py)

Usage
-----

### Arguments

	python serial_comms.py [Label] [ASCII Message] [show decoding] [noise sigma] [just show noise] [negate signal] [8b10b encode] [horizontal scaling] [brace size]

### Simple Serial Signal

	::latex
	\begin{tikzpicture}
		\input{|"python serial_comms.py 'Basic' 'Hello, World!' 1 0 0 0 0 0.4 0.2"}
	\end{tikzpicture}

\begin{latex}[--pdf Basic Signalling]
	\begin{tikzpicture}
		\input{|"python src/serial_comms.py 'Basic' 'Hello, World!' 1 0 0 0 0 0.4 0.2"}
	\end{tikzpicture}
\end{latex}

### Signal + Noise = Corrupt Signal

	::latex
	\begin{tikzpicture}
		\begin{scope}[yshift=-0cm]
			\input{|"python src/serial_comms.py      'Signal' 'Hello, World!' 0 0.0 0 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-1cm]
			\input{|"python src/serial_comms.py     '+ Noise' 'Hello, World!' 0 0.2 1 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-2cm]
			\input{|"python src/serial_comms.py '= Corrupted' 'Hello, World!' 1 0.2 0 0 0 0.4 0.2"}
		\end{scope}
	\end{tikzpicture}

\begin{latex}[--pdf Corrupt Signalling]
	\begin{tikzpicture}
		\begin{scope}[yshift=-0cm]
			\input{|"python src/serial_comms.py      'Signal' 'Hello, World!' 0 0.0 0 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-1cm]
			\input{|"python src/serial_comms.py     '+ Noise' 'Hello, World!' 0 0.2 1 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-2cm]
			\input{|"python src/serial_comms.py '= Corrupted' 'Hello, World!' 1 0.2 0 0 0 0.4 0.2"}
		\end{scope}
	\end{tikzpicture}
\end{latex}

### Differential Signalling

	::latex
	\begin{tikzpicture}
		\begin{scope}[yshift=-0cm]
			\input{|"python serial_comms.py         'Noise' 'Hello, World!' 0 0.2 1 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-1cm]
			\input{|"python serial_comms.py      '+ Signal' 'Hello, World!' 0 0.2 0 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-2cm]
			\input{|"python serial_comms.py      '- Signal' 'Hello, World!' 0 0.2 0 1 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-3cm]
			\input{|"python serial_comms.py    'Difference' 'Hello, World!' 1 0.0 0 0 0 0.4 0.2"}
		\end{scope}
	\end{tikzpicture}

\begin{latex}[--pdf Differential Signalling]
	\begin{tikzpicture}
		\begin{scope}[yshift=-0cm]
			\input{|"python src/serial_comms.py         'Noise' 'Hello, World!' 0 0.2 1 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-1cm]
			\input{|"python src/serial_comms.py      '+ Signal' 'Hello, World!' 0 0.2 0 0 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-2cm]
			\input{|"python src/serial_comms.py      '- Signal' 'Hello, World!' 0 0.2 0 1 0 0.4 0.2"}
		\end{scope}
		\begin{scope}[yshift=-3cm]
			\input{|"python src/serial_comms.py    'Difference' 'Hello, World!' 1 0.0 0 0 0 0.4 0.2"}
		\end{scope}
	\end{tikzpicture}
\end{latex}

### 8b/10b Encoding

	::latex
	\begin{tikzpicture}
		\begin{scope}[yshift=-0cm]
			\input{|"python serial_comms.py    'Raw' '@@@@' 1 0.0 0 0 0 0.8 0.2"}
		\end{scope}
		\begin{scope}[yshift=-2cm]
			\input{|"python serial_comms.py '8b/10b' '@@@@' 1 0.0 0 0 1 0.8 0.2"}
		\end{scope}
	\end{tikzpicture}

\begin{latex}[--pdf 8b10b Encoding]
	\begin{tikzpicture}
		\begin{scope}[yshift=-0cm]
			\input{|"python src/serial_comms.py    'Raw' '@@@@' 1 0.0 0 0 0 0.8 0.2"}
		\end{scope}
		\begin{scope}[yshift=-2cm]
			\input{|"python src/serial_comms.py '8b/10b' '@@@@' 1 0.0 0 0 1 0.8 0.2"}
		\end{scope}
	\end{tikzpicture}
\end{latex}
