# A two-state distance law and Gaussian fluctuations for complete-DAG unit-flow polytopes

## Finding

Let \(P_m\) be the unit-source/unit-sink flow polytope of the complete transitively oriented digraph on \(\{0,1,\ldots,m+1\}\), in the **standard orthonormal edge-coordinate Euclidean metric**. For every integer \(m\ge0\), choose vertices \(X_m,Y_m\) independently and uniformly among the \(2^m\) unit-path flows, and put \(D_m=\|X_m-Y_m\|_2^2\). The complete finite-dimensional squared-distance distribution has probability generating polynomial

\[
\mathbb E[z^{D_m}]
=(0,1)
\begin{pmatrix}
(1+2z)/4&z^2/4\\
z/2&1/2
\end{pmatrix}^{m}
\begin{pmatrix}z^2\\1\end{pmatrix}.
\]

In particular, for all \(m\ge0\),
\[
\mathbb E D_m=\frac{5m}{6}+\frac89(1-4^{-m}),
\qquad
\operatorname{Var}(D_m)=\frac{43m}{108}+O(1)\quad(m\to\infty).
\]

The exact two-state law has a sharp nondegenerate metric limit:
\[
\frac{D_m-5m/6}{\sqrt m}\ \Longrightarrow\
N\!\left(0,\frac{43}{108}\right),
\quad
\|X_m-Y_m\|_2-\sqrt{5m/6}\ \Longrightarrow\
N\!\left(0,\frac{43}{360}\right).
\]
The limits apply as \(m\to\infty\). The \(m=0\) flow polytope is a singleton, and its distance law is identically zero.

## Assumptions and scope

The graph has every arc \(i\to j\) for \(0\le i<j\le m+1\). Its nonnegative flows satisfy netflow \(+1\) at \(0\), \(-1\) at \(m+1\), and zero at each intermediate vertex. Coordinates are arc flows, and the norm is the ordinary \(\ell_2\) norm in \(\mathbb R^{\binom{m+2}{2}}\), restricted to the affine flow space. This metric must not be confused with the generally nonisometric standard Frobenius metric in the Birkhoff-face realization of the same combinatorial polytope.

The vertices are precisely indicators of increasing directed \(0\)-to-\(m+1\) paths. A path is determined by the subset of its \(m\) internal vertices, proving there are \(2^m\) vertices. Uniformly sampling a vertex is therefore equivalent to independent fair inclusion of each internal vertex. Sampling is with replacement, so the diagonal pairs are included; indeed \(\Pr(D_m=0)=2^{-m}\).

## Proof

**Exact distance encoding.** For two paths \(P,Q\), each edge-flow vector is Boolean, so \(\|\mathbf{1}_P-\mathbf{1}_Q\|_2^2=|E(P)\triangle E(Q)|\). At each internal vertex encode membership in \(P,Q\) by one of four equally probable symbols: \(00\), \(10\), \(01\), \(11\). Ignore \(00\)'s when testing for a shared arc. Put a \(11\) symbol at both the source and the sink. An arc is shared by the two paths if and only if its endpoints are *consecutive* \(11\) symbols in the sequence after deletion of all \(00\) symbols and without any intervening \(10\) or \(01\) symbol. Hence

\[
D_m=2+N_{10}+N_{01}+2N_{11}-2N_{\mathrm{consecutive}\ 11},
\]
where the last count includes the two boundary \(11\)'s. Here \(N_{10},N_{01},N_{11}\) count internal symbols.

Let state \(1\) mean that the most recent nonzero symbol in the prefix was \(11\), and state \(0\) that it was one of \(10,01\). The initial state, at the source, is \(1\). The transition table, with entries (new state, number of equally likely symbols, increase in squared distance before the sink), is:

- state \(0\): \((0,1,0)\) for \(00\), \((0,2,1)\) for \(10,01\), and \((1,1,2)\) for \(11\);
- state \(1\): \((1,1,0)\) for \(00\), \((0,2,1)\) for \(10,01\), and \((1,1,0)\) for \(11\).

At the sink add \(2\) if the final state is \(0\), and add \(0\) if it is \(1\). Weighting each transition by \(z^{\text{increase}}/4\) gives the displayed \(2\times2\) matrix, initial row \((0,1)\), and final column \((z^2,1)^\mathsf T\). This proves every coefficient of the exact probability generating polynomial. In particular, substituting \(z=0\) yields \(\Pr(D_m=0)=2^{-m}\).

**Exact first moment.** For an arc \((i,j)\), the probability that it belongs to a uniformly sampled path is
\[
p_{ij}=2^{-(j-i-1)-\mathbf1_{i>0}-\mathbf1_{j<m+1}}.
\]
The expected number of arcs in one path is \(1+m/2\); the expected number of arcs shared by two independent paths is \(\sum_{i<j}p_{ij}^2\). Summing by arc gaps gives the exact identity
\[
\sum_{i<j}p_{ij}^2=\frac m{12}+\frac59+\frac4{9\,4^m}.
\]
Since \(D_m=|E(P)|+|E(Q)|-2|E(P)\cap E(Q)|\), this yields the displayed formula \(5m/6+(8/9)(1-4^{-m})\), including the boundary case \(m=0\).

**Fluctuations.** Let \(M(z)\) denote the transfer matrix. Its Perron eigenvalue for positive \(z\) near \(1\) is
\[
\lambda(z)=\frac{3+2z+\sqrt{8z^3+4z^2-4z+1}}8.
\]
At \(z=1\), the two eigenvalues are \(1\) and \(1/4\). In a fixed complex neighborhood of \(z=1\), analytic spectral decomposition therefore gives
\[
\mathbb E e^{tD_m}=c(t)\lambda(e^t)^m+O(\rho^m),
\]
with an analytic \(c(t)\) satisfying \(c(0)=1\), uniformly for sufficiently small complex \(t\), for some \(\rho<1\). Direct differentiation of the explicit eigenvalue gives
\[
\log\lambda(e^t)=\frac56t+\frac{43}{216}t^2+O(t^3).
\]
Insert \(t=iu/\sqrt m\) for fixed real \(u\), subtract \(5m/6\), and let \(m\to\infty\). The characteristic functions converge to \(\exp(-43u^2/216)\), proving the normal limit with variance \(43/108\). Differentiating the analytic log moment-generating function twice at zero also gives \(\operatorname{Var}(D_m)=43m/108+O(1)\). The law of large numbers \(D_m/m\to5/6\) in probability follows from the variance bound. Finally, apply
\[
\sqrt{D_m}-\sqrt{5m/6}
=\frac{D_m-5m/6}{\sqrt{D_m}+\sqrt{5m/6}}
\]
and Slutsky's theorem to obtain the unscaled Euclidean-distance fluctuation variance \((43/108)/(4(5/6))=43/360\).

## Verification

Run the standalone script \(`python3 verify.py`\) with Python 3 standard library. It constructs each path's actual arc set, exhaustively evaluates all \(4^m\) ordered pairs for \(0\le m\le7\), and independently reproduces the distance polynomial by integer-weighted two-state transitions. It checks all coefficients and the rational mean identity exactly. For \(m=8,9,10,12,20,40\), it checks the polynomial normalization and exact mean using only the transfer recurrence, and prints the approach of variance per site to \(43/108\). The infinite central limit theorem is proved by spectral analysis above; the finite script does not certify that limit by enumeration.

## Relationship to prior work

Dugan, *On the \(f\)-vectors of flow polytopes for the complete graph*, originally public on 2024-09-23 (arXiv:2409.15519, primary MSC2020 \(52\mathrm B05\)), explicitly establishes the complete-DAG flow realization and the \(2^m\)-vertex increasing-path encoding. Its main theorems evaluate face numbers rather than vertex-pair Euclidean distances. The present result uses that established realization but evaluates a different, coordinate-dependent geometric invariant: the complete squared-distance distribution and its Gaussian metric fluctuation, including the constants \(5/6\), \(43/108\) and \(43/360\). The Birkhoff-face permutation-matrix metric is not asserted to be isometric to the edge-flow metric.

A related published result on Euclidean inballs of complete directed flow polytopes concerns optimal interior balls and center loci, not distances of independently sampled vertices. The general theory of analytic transfer matrices is standard; the evaluated two-state encoding and resulting metric coefficients are the specific contribution assessed here.

## Limitations

The assertion is specific to the unit source/sink flow polytope of the **complete transitively oriented graph**, uniformly sampled vertices, and the **orthonormal arc-coordinate metric**. It does not assert the same formula for other netflows, other digraphs, interior-volume sampling or the Birkhoff Frobenius embedding. The literature comparison is best knowledge, not a proof of historical uniqueness; an unindexed equivalent in random increasing-path overlap statistics remains possible. The normal limits do not provide an all-\(m\) error rate.

## References

1. W. T. Dugan, *On the \(f\)-vectors of flow polytopes for the complete graph*, arXiv:2409.15519 (first public version 2024-09-23); *Canadian Journal of Mathematics* (2025). https://arxiv.org/abs/2409.15519 ; https://doi.org/10.4153/S0008414X2510151X .
2. S. Corteel, J. S. Kim and K. Mészáros, *Flow polytopes with Catalan volumes*, arXiv:1612.00102 (2016); *Comptes Rendus Mathématique* 355 (2017), 248–259. https://arxiv.org/abs/1612.00102 .
3. *Pattern-avoiding polytopes*, *European Journal of Combinatorics* (2018), https://doi.org/10.1016/j.ejc.2018.07.006 (additional background on the permutation-matrix realization; full text was not accessible for a decisive novelty comparison).
