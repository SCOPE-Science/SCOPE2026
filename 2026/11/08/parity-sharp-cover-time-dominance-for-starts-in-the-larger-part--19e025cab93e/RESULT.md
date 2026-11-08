# Parity-sharp cover-time dominance for starts in the larger part of a complete bipartite graph

## Finding
Let \(1\le b\le a\) be integers and let \(C_A\), respectively \(C_B\), be the cover time in *edge traversals* of a simple random walk on the complete bipartite graph \(K_{a,b}\), started at a fixed vertex in its \(a\)-vertex part \(A\), respectively its \(b\)-vertex part \(B\). Initial time \(0\) counts the starting vertex as visited. Define, for integers \(n\ge1\) and \(k\ge0\),
\[
U_n(k)=\Pr\{\text{all }n\text{ labels occur among }k\text{ independent uniform draws}\}=
\frac{n!\,S(k,n)}{n^k},
\]
where \(S(k,n)\) is a Stirling number of the second kind and \(U_n(k)=0\) when \(k<n\).

For every integer \(k\ge0\), the cover-time cumulative distribution functions are
\[
\begin{aligned}
\Pr(C_A\le 2k)&=U_a(k+1)U_b(k),\\
\Pr(C_B\le 2k)&=U_a(k)U_b(k+1),\\
\Pr(C_A\le 2k+1)&=\Pr(C_B\le 2k+1)=U_a(k+1)U_b(k+1).
\end{aligned}
\]
If \(a>b\), then \(C_A\) is strictly smaller than \(C_B\) in first-order stochastic order: the two cumulative distribution functions agree at every odd integer and at even times \(2k\) with \(k<a-1\), but
\[
\Pr(C_A\le 2k)>\Pr(C_B\le 2k)\qquad (k\ge a-1).
\]
If \(a=b\), their laws agree. In particular the larger-part start uniquely minimizes every strictly increasing function of cover time having finite expectations, among starting vertices, when \(a>b\).

Let \(X_a\) and \(X_b\) be independent standard coupon-collector completion counts for \(a\) and \(b\) labels. The exact positive expected-time advantage is
\[
\mathbb E C_B-\mathbb E C_A
=\Pr(X_a>X_b)-\Pr(X_b>X_a)>0\qquad(a>b).
\]
It equals \(1\) if \(b=1<a\), and lies strictly between \(0\) and \(1\) for \(a>b\ge2\). Thus even for arbitrarily large graphs the starting-side effect never exceeds one expected traversal. For \(K_{3,2}\), the first positive even-time cumulative probability gap (at time \(4\)) is \(1/9\), whereas the expected gap is \(7/10\).

## Assumptions and scope
Graphs are finite, simple, unweighted, and complete bipartite; the simple random walk chooses a neighbor uniformly at every transition, with no holding. All vertices must be visited at least once, counting the starting vertex at time zero. Every pair of part sizes \(a,b\ge1\) is included, including stars and the two-vertex graph. The stochastic-order comparison is from the side with *more* vertices (and therefore the smaller degree); there is no claim for arbitrary bipartite or weighted graphs.

## Proof
**Alternating coupon streams.** Starting in \(A\), the walk alternates between the two parts. At successive visits to \(A\) after time zero, each sampled vertex is uniform on \(A\), independently of every other choice. Likewise the vertices visited in \(B\) form an independent, uniformly sampled sequence in \(B\). Include the initial \(A\)-vertex as the first \(A\)-sample. With independent standard completion counts \(X_a,X_b\), all \(A\)-vertices have been seen by traversal time \(2X_a-2\) and all \(B\)-vertices by \(2X_b-1\). Hence
\[
C_A\overset{d}=\max\{2X_a-2,\ 2X_b-1\},\quad
C_B\overset{d}=\max\{2X_a-1,\ 2X_b-2\}.
\]
Taking the respective events that both streams have completed gives the four displayed cumulative formulas, with the two odd-time formulas identical.

**Strict coupon ratio lemma.** For every integer \(k\ge1\), set \(A_n(k)=n!S(k,n)\) and \(G_k(z)=\sum_{n=1}^k A_n(k)z^n=zQ_k(z)\). Stirling recurrence gives
\[
G_{k+1}(z)=z\big((1+z)G_k(z)\big)',\qquad
Q_{k+1}(z)=\big(z(1+z)Q_k(z)\big)',\quad Q_1(z)=1.
\]
Inductively, \(Q_k\) has exactly \(k-1\) simple roots strictly between \(-1\) and \(0\): this is clear for \(k=1\); if it holds for \(k\), the polynomial \(z(1+z)Q_k(z)\) has \(k+1\) distinct roots in \([-1,0]\), and Rolle's theorem places exactly \(k\) derivative roots strictly between them. Thus \(G_k\) has only real nonpositive roots. Newton's inequalities give strict log-concavity of its positive coefficient sequence \((A_1(k),\ldots,A_k(k))\), since it is not supported on only one index when \(k\ge2\). In particular \(A_{n-1}(k)/A_n(k)\) increases strictly with \(n\) for \(1\le n\le k\), using \(A_0(k)=0\). The same Stirling recurrence yields
\[
\frac{U_n(k+1)}{U_n(k)}=\frac{A_n(k)+A_{n-1}(k)}{A_n(k)}
=1+\frac{A_{n-1}(k)}{A_n(k)}.
\]
This ratio is strictly increasing in the number of coupons \(n\), for \(1\le n\le k\).

**Sharp sign and all boundaries.** If \(a>b\) and \(k<a-1\), neither \(a\)-coupon process can complete by time \(k+1\), and both even-time cumulative distributions vanish. For \(k=a-1\), \(U_a(k)=0\) but \(U_a(k+1)>0\) and \(U_b(k)>0\); the even-time gap is strictly positive. For \(k\ge a\), the strict coupon ratio lemma at \(n=a>b\) gives
\[
\frac{U_a(k+1)}{U_a(k)}>\frac{U_b(k+1)}{U_b(k)},
\]
so cross multiplication gives the strict gap. When \(a=b\), the explicit cumulative formulas coincide. The stochastic ordering follows for all integer times and hence all real times. For a strictly increasing test function with finite expectations, strict stochastic dominance yields a strict expectation comparison by summation by parts or monotone coupling.

Finally couple \(C_A\) and \(C_B\) with the *same* independent pair of coupon collectors. If \(X_a>X_b\), then \(C_B-C_A=1\); if \(X_b>X_a\), it equals \(-1\); if the counts tie, it equals \(0\). Consequently their mean difference is the displayed difference of two event probabilities and also the sum of the nonnegative even-time cumulative gaps. For \(a>b\), positivity is strict by the sharp sign argument. If \(b=1<a\), then \(X_b=1\) and \(X_a\ge a>1\) surely, so the difference is \(1\). If \(a>b\ge2\), both orderings \(X_a>X_b\) and \(X_b>X_a\) have strictly positive probability, so the strictly positive difference is below \(1\). This proves every assertion. \(\square\)

## Verification
An independent exact-rational finite-state calculation, provided in `check_cover.py`, tracks the current vertex and the set of visited vertices for every \(1\le a,b\le5\) and each time \(0\le t\le16\), directly checks all \(850\) cumulative probabilities against the coupon-factor formulas, and verifies the sharp stochastic inequalities, including \(60\) cases of strict even-time gap. It also evaluates strict coefficient log-concavity of \(n!S(k,n)\) through \(k=29\), checks the first \(K_{3,2}\) gap, and verifies the rational \(7/10\) expected-time gap via a separate inclusion-exclusion formula. These checks independently corroborate the algebra; the all-size conclusion follows from the proof, not finite enumeration. The displayed \(7/10\) example is obtainable from exact coupon-collector inclusion-exclusion (or direct rational absorbing-chain expectations).

## Relationship to prior work
Dong et al., *Universal cover-time distribution of heterogeneous random walks* (first public October 11, 2022), study rescaling and universality for heterogeneous random walks, rather than exact alternating bipartite start-side stochastic comparisons. Tishby, Biham and Katzav analyze cover-time distributions on random regular graphs, not the fixed complete bipartite graph with two distinct vertex orbits. Zlatanov and Kocarev give general transfer-matrix formulas for exact cover-time distributions on arbitrary graphs; applying such a general formula can calculate individual examples but does not itself establish the sign-uniform ratio inequality and sharp odd/even ordering. Falgas-Ravry, Larsson and Markström study concentration for independent structured coupons rather than the periodically alternating bipartite covering process. The coefficient real-rootedness method is classical and is used here solely as a proof device, not claimed as a new polynomial theorem.

## Limitations
The result covers only the uniform non-lazy walk on complete bipartite graphs. It does not determine an optimal starting vertex on a general irregular graph or compare other stochastic protocols. The originality comparison is based on examined open literature and targeted database searches, not an exhaustive historical-priority certification. The finite-state checker is confirmatory, not a proof for unbounded part sizes.

## References
- Jia-Qi Dong, Wen-Hui Han, Yisen Wang, Xiao-Song Chen and Liang Huang, *Universal cover-time distribution of heterogeneous random walks*, arXiv:2210.05122v1, October 11, 2022. https://arxiv.org/abs/2210.05122
- Ido Tishby, Ofer Biham and Eytan Katzav, *Analytical results for the distribution of cover times of random walks on random regular graphs*, arXiv:2110.13592v1, October 26, 2021. https://arxiv.org/abs/2110.13592
- Nikola Zlatanov and Ljupco Kocarev, *Random walks on networks: cumulative distribution of cover time*, arXiv:0910.3545, October 19, 2009. https://arxiv.org/abs/0910.3545
- Victor Falgas-Ravry, Joel Larsson and Klas Markström, *Speed and concentration of the covering time for structured coupon collectors*, arXiv:1601.04455v1, January 18, 2016. https://arxiv.org/abs/1601.04455
