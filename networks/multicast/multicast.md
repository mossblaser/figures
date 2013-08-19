img:file://multicast_a.png
tags: Networks
      TikZ

Multicast Routing Examples
==========================

Shows various multicast routes from one source to two destinations and their
various properties as shown in the following table:


Route | Router Entries | Total Hops | Hops to $T_1$ | Hops to $T_2$
----- | -------------- | ---------- | ------------- | -------------
(a)   | 4              | 5          | 3             | 2
(b)   | 5              | 4          | 4             | 2
(c)   | 4              | 4          | 3             | 3
(d)   | 4              | 4          | 3             | 2

* [Download `multicast-routing.tex`](file://src/multicast-routing.tex)
* [Download `multicast-routing-a.tex`](file://src/multicast-routing-a.tex)
* [Download `multicast-routing-b.tex`](file://src/multicast-routing-b.tex)
* [Download `multicast-routing-c.tex`](file://src/multicast-routing-c.tex)
* [Download `multicast-routing-d.tex`](file://src/multicast-routing-d.tex)

The file `multicast-routing.tex` is a dependency of all of the above examples
and the `\input` at the start of each example must be adjusted accordingly.

Usage
-----

### Routing A

	::latex
	\input{multicast-routing-a}

\begin{latex}[--pdf Multicast A]
	\input{src/multicast-routing-a}
\end{latex}

### Routing B

	::latex
	\input{multicast-routing-b}

\begin{latex}[--pdf Multicast B]
	\input{src/multicast-routing-b}
\end{latex}

### Routing C

	::latex
	\input{multicast-routing-c}

\begin{latex}[--pdf Multicast C]
	\input{src/multicast-routing-c}
\end{latex}

### Routing D

	::latex
	\input{multicast-routing-d}

\begin{latex}[--pdf Multicast D]
	\input{src/multicast-routing-d}
\end{latex}

