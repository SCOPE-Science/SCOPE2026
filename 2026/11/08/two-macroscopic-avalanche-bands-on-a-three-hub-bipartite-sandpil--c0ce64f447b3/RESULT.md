# Two macroscopic avalanche bands on a three-hub bipartite sandpile

## Finding

Let \(n\ge 2\). In the standard finite undirected Abelian sandpile on \(K_{3,n}\), fix a sink \(s\) in the three-vertex part and a distinct source \(a\) in that same part. Draw the initial stable configuration uniformly from the recurrent configurations, add one grain at \(a\), and let \(T_n\) be the **total number of topplings, counting repeated topplings**. The source-resolved avalanche polynomial, whose coefficient at \(x^k\) is the number of recurrent initial configurations giving \(T_n=k\), is exactly

\[
\begin{aligned}
H_n(x)={}&n\bigl[(n-2)3^{n-1}+2^{n-1}\bigr]\\
&+nx\bigl[(2+x)^{n-1}-2^{n-1}\bigr]\\
&+nx^3(1+2x)^{n-1}\\
&+n2^{n-1}x^{n+2}(x-1).
\end{aligned}
\]

Consequently,

\[
\mathbb P(T_n>0)=\frac{2-(2/3)^{n-1}}{n},\qquad
\mathcal L(T_n/n\mid T_n>0)\Longrightarrow
\tfrac12\delta_{1/3}+\tfrac12\delta_{2/3},
\]

and the unique possible extra-wave maximum is \(T_n=n+3\), with

\[
\mathbb P(T_n=n+3)=\frac1n\left(\frac23\right)^{n-1}.
\]

Thus a rare source-triggered avalanche has **two distinct macroscopic size bands**, near one-third and two-thirds of the growing part, and a still rarer event topples the source twice.

## Assumptions and scope

The graph is the simple unweighted complete bipartite graph \(K_{3,n}\). Write its three-vertex part as \(\{s,a,b\}\) and its other part as \(\{v_1,\ldots,v_n\}\). The sink \(s\) absorbs all incoming grains and never topples. Each non-sink hub has threshold \(n\); each of the \(n\) other vertices has threshold \(3\). A vertex with at least its degree in grains topples, sending one grain along each incident edge. Only one grain is initially added, at \(a\). The initial law is uniform over recurrent **stable** sandpiles, not arbitrary stable configurations. Avalanche size is the sum of the odometer over all non-sink vertices; it is not the number of distinct toppled vertices or the number of grains lost to the sink.

For each stable state, denote hub heights by \(A,B\in\{0,\ldots,n-1\}\), and write \(z_j\) for the number of non-sink leaf vertices of height \(j\), for \(j=0,1,2\). Thus \(z_0+z_1+z_2=n\).

## Proof

**1. Classification of recurrent configurations.** Dhar's burning criterion says to send one grain from the sink to every leaf, then test whether every non-sink vertex topples once. The \(z_2\) leaves initially at height two topple first. At least one of \(a,b\) must then topple, which is equivalent to \(\max(A,B)\ge n-z_2=z_0+z_1\). The first hub toppling activates all \(z_1\) leaves initially at height one. The second hub can then topple if and only if \(\min(A,B)\ge n-z_2-z_1=z_0\); after it topples, the \(z_0\) leaves topple. The two conditions are also necessary because no other event can initiate or continue the burning waves. Hence

\[
\boxed{\text{recurrent}\quad\Longleftrightarrow\quad
\max(A,B)\ge z_0+z_1\ \text{ and }\ \min(A,B)\ge z_0.}
\]

For fixed ordered leaves with these three populations, the number of allowed ordered hub-height pairs is \((n-z_0)^2-z_1^2=z_2^2+2z_1z_2\). Summing over the \(3^n\) leaf-height assignments gives \(n^2 3^{n-1}\) recurrent states: under three equiprobable leaf heights, the expectation of \(z_2^2+2z_1z_2\) is \(n^2/3\). This independently matches the matrix-tree count for \(K_{3,n}\).

**2. Source-triggered cases.** If \(A<n-1\), adding at \(a\) produces no toppling. Otherwise \(A=n-1\), and the recurrence condition forces \(z_2\ge1\). First \(a\) topples and then precisely the \(z_2\) leaves at height two topple. There are three exhaustive cases:

- If \(B<n-z_2\), hub \(b\) does not topple, and \(T_n=1+z_2\). For a given leaf configuration, the admissible \(B\) values form an interval of length \(z_1\).
- If \(B\ge n-z_2\) and \(z_0>0\), hub \(b\) topples and activates precisely the \(z_1\) leaves at height one. Neither hub can topple again, giving \(T_n=z_1+z_2+2=n-z_0+2\). The admissible \(B\) interval has length \(z_2\).
- If \(B\ge n-z_2\) and \(z_0=0\), all \(n\) leaves topple once. They return exactly \(n\) grains to \(a\), which topples for a second time. All sites are then stable, giving \(T_n=n+3\). Again there are \(z_2\) choices for \(B\).

No additional topplings occur: after the described topplings, leaf heights are below three, the other hub has received fewer than \(n\) grains following its toppling, and the source is stable after at most its second toppling.

**3. Exact coefficient counts.** In the first case, set \(r=z_2\), with \(1\le r\le n-1\). Summing the number \(z_1\) of possible \(B\) heights over the other leaf heights gives

\[
\#\{T_n=r+1,\ \text{first case}\}
=(n-r)\binom nr2^{n-r-1}
=n\binom{n-1}{r}2^{n-1-r}.
\]

In the second case, put \(k=z_1+z_2=n-z_0\), with \(1\le k\le n-1\). Summing the \(z_2\) possible \(B\) heights over assignments of the \(k\) nonzero leaves yields

\[
\#\{T_n=k+2,\ \text{second case}\}
=\binom nk\sum_{r=1}^k r\binom kr
=k\binom nk2^{k-1}
=n\binom{n-1}{k-1}2^{k-1}.
\]

For the third case, the number is \(\sum_{r=1}^n r\binom nr=n2^{n-1}\). Subtracting all positive avalanche counts from the number of recurrent states gives exactly \(n[(n-2)3^{n-1}+2^{n-1}]\) zero-avalanche states. Summing the resulting three binomial generating functions proves the displayed polynomial, including the single exceptional toppling at exponent \(n+3\).

**4. Limiting distribution.** The first positive branch has total count \(n[3^{n-1}-2^{n-1}]\), with size \(1+R\), where \(R\) is \(\operatorname{Bin}(n-1,1/3)\) conditioned on \(R\ge1\). The union of the other two positive branches has total count \(n3^{n-1}\); its size has the law of \(3+S+\mathbf1_{\{S=n-1\}}\), where \(S\sim\operatorname{Bin}(n-1,2/3)\). The first branch's conditioning probability tends to one, the exceptional indicator tends to zero in probability, and the two branch weights tend to \(1/2\). Binomial weak laws give the two-atom conditional limit. Dividing the exact positive and maximum counts by \(n^2 3^{n-1}\) gives the displayed probabilities.

## Verification

The standalone standard-library script `verify.py` reconstructs burning and source additions directly from toppling rules, exhaustively tests all stable states for \(2\le n\le7\), compares the independent burning test against the stated recurrent criterion, and verifies every coefficient of \(H_n\). It separately checks exact coefficient normalization and maximum-event counts for \(2\le n\le80\). Run `python3 verify.py` from the directory containing this document and script. These computations are finite corroboration; the proof covers every integer \(n\ge2\).

## Relationship to prior work

Dukes and Le Borgne (arXiv:1208.0024, first public 2012-07-31) classify the recurrent configurations of complete bipartite sandpiles using decorated polyominoes. Aval, D'Adderio, Dukes and Le Borgne (arXiv:1307.7740, first public 2013-07-29) analyze recurrent/parking operators and a cyclic lemma for complete bipartite sandpiles. Austin and collaborators (arXiv:1605.02713, first public 2016-05-09) introduce a multivariate avalanche-polynomial treatment for trees, cycles, wheels and complete graphs. These works provide the relevant framework but do not state the fixed-source \(K_{3,n}\) polynomial or its two-band limit in the examined material. Selig and Zhu (arXiv:2409.11811, first public 2024-09-18) later study recurrent states of bipartite Abelian and stochastic sandpiles; this model is the deterministic version and the stated size distribution is not identified in their examined manuscript. The present theorem is a model-specific calculation, not a claim that binomial wave decompositions are universally new.

## Limitations

The exact law is for a fixed hub source distinct from the sink in \(K_{3,n}\), with a uniformly recurrent initial law. It does not characterize the avalanche polynomial summed over all sources, a stochastic-toppling sandpile, a different sink location, or universal large-graph critical exponents. Broader independent historical-priority verification may reveal an equivalent exact formula under a different parametrization. The positive-event conditional limit does not imply power-law scaling.

## References

1. Mark Dukes and Yvan Le Borgne, *Parallelogram polyominoes, the sandpile model on a complete bipartite graph, and a q,t-Narayana polynomial*, arXiv:1208.0024, https://arxiv.org/abs/1208.0024 (first public 2012-07-31).
2. Jean-Christophe Aval, Michele D'Adderio, Mark Dukes and Yvan Le Borgne, *Two operators on sandpile configurations, the sandpile model on the complete bipartite graph, and a Cyclic Lemma*, arXiv:1307.7740, https://arxiv.org/abs/1307.7740 (first public 2013-07-29).
3. Demara Austin, Megan Chambers, Rebecca Funke, Luis David García Puente and Lauren Keough, *The Avalanche Polynomial of a Graph*, arXiv:1605.02713, https://arxiv.org/abs/1605.02713 (first public 2016-05-09).
4. Thomas Selig and Haoyue Zhu, *Abelian and stochastic sandpile models on complete bipartite graphs*, arXiv:2409.11811, https://arxiv.org/abs/2409.11811 (first public 2024-09-18).
