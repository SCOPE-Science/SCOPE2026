# Exact one-spin metastability on crown graphs and a high-field entropy spike

## Finding
Let \(n\ge3\), let \(G_n=K_{n,n}\setminus\{a_i b_i:1\le i\le n\}\) be the crown graph, and put classical spins \(a_i,b_i\in\{-1,+1\}\) on its vertices. For antiferromagnetic coupling \(J>0\), uniform positive field \(h>0\), and Hamiltonian
\[
\mathcal H=J\sum_{i\ne j}a_i b_j-h\sum_{i=1}^n(a_i+b_i),
\qquad \alpha=h/J,
\]
write \(N_n(\alpha)\) for the number of labeled configurations in which flipping any **single** spin cannot *lower* the energy (zero-energy flips are allowed).

For \(0<\alpha<n-1\), define
\[
S_n(\alpha)=\sum_{\substack{M=-n,-n+2,\ldots,n\\ |\alpha-M|\le1}}
\binom{n}{(n+M)/2}.
\]
Then the exact all-size, all-field classification is
\[
\boxed{N_n(\alpha)=\begin{cases}
2+S_n(\alpha)+2n\binom{n-1}{(n-1+\alpha)/2},
&0<\alpha\le n-3,\ \alpha\in\mathbb Z,\ \alpha\not\equiv n\pmod2,\\
2+S_n(\alpha),&0<\alpha<n-1\text{ otherwise},\\
2^{n+1}+n-1,&\alpha=n-1,\\
1,&\alpha>n-1.
\end{cases}}
\]
The binomial term in the first line is used **only** where its lower entry is an integer, as specified by the same line's conditions. The two constant configurations with opposite uniform bipartition spins account for the term \(2\) below saturation.

For any fixed *noninteger* \(\alpha>0\), as \(n\to\infty\),
\[
N_n(\alpha)\sim2^n\sqrt{\frac{2}{\pi n}},\qquad
\frac{\log N_n(\alpha)}{2n}\to\frac{\log2}{2}.
\]
At positive integer \(\alpha\), the same limiting entropy holds, but the subsequence with \(\alpha\not\equiv n\pmod2\) has an additional order-\(n\) multiplicative enhancement from one mismatched pair. A sharper, isolated high-field effect occurs for each fixed \(0<\varepsilon<1\): for all sufficiently large \(n\),
\[
\boxed{N_n(n-1-\varepsilon)=n+2,\quad
N_n(n-1)=2^{n+1}+n-1,\quad
N_n(n-1+\varepsilon)=1.}
\]
Thus the metastable-state entropy per spin in these three regimes tends respectively to \(0\), \((\log 2)/2\), and \(0\). By contrast, on the full complete bipartite graph \(K_{n,n}\), for noninteger \(0<\alpha<n-1\), the only one-spin-stable configurations are the two uniform opposite-partition states. Deleting one perfect matching therefore changes a generic fixed-field count from \(2\) to exponentially many, without introducing disorder or odd-cycle frustration.

## Assumptions and scope
Vertices and matched pairs are labeled; \(n\ge3\); all surviving edges have the same antiferromagnetic coupling \(J>0\), while missing matched edges have zero coupling. Field \(h\) is applied equally to both parts, with \(\alpha=h/J>0\). No normalization by graph size is used. Stability means \(\mathcal H(\sigma^{(v)})-\mathcal H(\sigma)\ge0\) at every vertex \(v\). Hence fields exactly at integers may admit marginal, neutrally flippable configurations. At negative fields, global spin reversal gives \(N_n(-\alpha)=N_n(\alpha)\); the theorem as stated concerns positive fields. This is not a statement about dynamical absorption, global ground states, or finite-temperature metastability.

## Proof
Put \(A=\sum_i a_i\), \(B=\sum_i b_i\). Directly flipping the individual spin at position \(i\) gives the **exact** nonnegative-energy conditions
\[
a_i(\alpha-B+b_i)\ge0,\qquad b_i(\alpha-A+a_i)\ge0.
\tag{1}
\]
Classify each deleted-matching pair into \((+,+)\), \((-,-)\), \((+,-)\), or \((-,+)\), with respective counts \(p,q,r,t\), \(p+q+r+t=n\). Put \(M=p-q\). Then
\[
A=M+r-t,\qquad B=M-r+t.
\tag{2}
\]
The four pair types translate (1) into these complete local constraints whenever their count is nonzero:
\[
\begin{array}{c|c}
(+,+)&\alpha\ge\max(A,B)-1\\
(-,-)&\alpha\le\min(A,B)+1\\
(+,-)&B+1\le\alpha\le A-1\\
(-,+)&A+1\le\alpha\le B-1.
\end{array}
\tag{3}
\]
Having both \(r>0\) and \(t>0\) is impossible, because it would require both \(A-B\ge2\) and \(B-A\ge2\).

**No mismatched pair.** If \(r=t=0\), then \(A=B=M=p-q\). When \(p,q>0\), (3) gives exactly \(|\alpha-M|\le1\). The all-positive state (\(p=n\)) is stable exactly when \(\alpha\ge n-1\); the all-negative state (\(q=n\)) is not stable for positive \(\alpha\). This gives \(S_n(\alpha)\) in the subcritical range, plus an all-positive state at and above saturation.

**Mismatched pairs.** By exchanging the bipartition labels it suffices to take \(r>0\), \(t=0\), so \(A=M+r\) and \(B=M-r\). If \(p,q>0\), the \((+,-)\) constraints in (3), together with the constraints for both aligned types, force
\[
\alpha=M+r-1=M-r+1,
\]
hence \(r=1\) and \(\alpha=M=p-q\). Such states exist precisely at integer \(0<\alpha\le n-3\) with parity opposite to \(n\). For each mismatched orientation, select its position in \(n\) ways and select which \((n-1+\alpha)/2\) of the remaining \(n-1\) pairs are \((+,+)\). Including the exchanged orientation gives the term \(2n\binom{n-1}{(n-1+\alpha)/2}\).

If \(p>0,q=0,r>0\), the same inequalities force \(\alpha=A-1=n-1\); if \(p=0,q>0,r>0\), they force \(\alpha=B+1=1-n\), excluded by positive field. When \(p=q=0\) and \(r=n\), the uniform opposite-partition state is stable exactly when \(\alpha\le n-1\). The exchanged orientation gives the second such state. Thus these are the **only** subcritical mismatched configurations besides the one-pair boundary class. At the special field \(\alpha=n-1\), every state with all \(a_i=+1\) or all \(b_i=+1\) is stable: these sets have \(2^n+2^n-1\) elements in their union. Additionally, exactly \(n\) aligned states with one \((-,-)\) pair are stable, giving \(2^{n+1}+n-1\). Above this field, (3) leaves only the all-positive state. The classification is complete.

For fixed positive noninteger \(\alpha\) and all sufficiently large \(n\), a unique admissible \(M\) of the parity of \(n\) satisfies \(|\alpha-M|<1\), with \(M=O(1)\). The central binomial estimate gives \(S_n(\alpha)\sim2^n\sqrt{2/(\pi n)}\). For fixed positive integer \(\alpha\) the one-pair term adds at most a polynomial factor \(n\), so the entropy per spin is unchanged. Finally \(\alpha=n-1-\varepsilon\) selects only \(M=n-2\) and the two opposite-partition states; the other two high-field counts are already proved. In \(K_{n,n}\), the missing-pair corrections in (1) vanish, so a mixed part would force an integer equality \(\alpha=A\) or \(\alpha=B\), impossible at noninteger field. The two uniform opposite-partition states are then the only possibilities in the stated range.

## Verification
The standalone file `verify_crown.py` uses only Python's standard library. It independently enumerates all \(2^{2n}\) spin configurations for \(3\le n\le6\), evaluating the **full edge-sum Hamiltonian** before and after each possible flip, and compares the count with the closed formula at rational fields including all important integer boundaries. It separately enumerates every multinomial orbit of four pair-types for \(3\le n\le18\), using exact fractions. It reports `PASS 240 comparisons`. This finite verification checks implementations and boundary arithmetic; it is not the proof for arbitrary \(n\), which is the exhaustive symbolic classification above.

Run: `python3 verify_crown.py`.

## Relationship to prior work
Berg and Sellitto (2001) study one-flip-stable Ising configurations on random graphs, emphasizing annealed and quenched disorder averages and finite connectivity, not an exact count for a deterministic dense crown graph in a uniform field. Waclaw and Burda (2008) develop a field-theoretical approach for Gaussian spin glasses on arbitrary graph topologies and give large-graph complexity estimates, not this all-size deterministic homogeneous antiferromagnetic classification. Rosinberg, Tarjus, and Pérez-Reche (2008) investigate Gaussian random-field ferromagnets on Bethe lattices and hysteresis, not the crown graph. Earlier exact ground-state work on matching-deleted bipartite systems concerns global energy minima, whereas the configurations counted here are all one-spin-local minima, including nonground states.

The deleted-matching graph admits a simple local-field reduction, but neither a generic graph-counting framework nor the known random-coupling models imply the exact marginal-field spike \(2^{n+1}+n-1\) or its sharp one-sided contrast without the separate counting argument. No directly covering infinite-family formula was located in the examined mathematical literature and searchable records; historical originality remains subject to unindexed literature.

## Limitations
The result addresses only zero-temperature weak one-spin stability, not strict dynamics that may accept zero-energy flips. The coupling is homogeneous and unscaled, and only the crown graph family is considered. It does not determine mixing times or transition barriers. The claims of historical priority are bounded by the inspected literature and accessible records. Computational checks cover a finite range only; the all-size conclusion rests on the complete symbolic pair-classification proof.

## References
1. J. Berg and M. Sellitto, *Metastable configurations of spin models on random graphs*, arXiv:cond-mat/0108247, first publicly submitted 2001-08-15, https://arxiv.org/html/cond-mat/0108247v2 .
2. B. Waclaw and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224, first publicly submitted 2008-01-08, https://arxiv.org/abs/0801.1224 .
3. M. L. Rosinberg, G. Tarjus, and F. J. Pérez-Reche, *The T=0 random-field Ising model on a Bethe lattice with large coordination number: hysteresis and metastable states*, arXiv:0809.3774, first publicly submitted 2008-09-22, https://arxiv.org/abs/0809.3774 .
4. E. W. Weisstein, *Crown Graph*, MathWorld, https://mathworld.wolfram.com/CrownGraph.html (definition of the graph family).
