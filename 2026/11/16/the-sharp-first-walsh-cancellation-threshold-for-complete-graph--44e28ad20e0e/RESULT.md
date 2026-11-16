# The sharp first Walsh cancellation threshold for complete-graph spanning trees

## Finding

Let \(n\ge3\) be an integer, let \(E_n=E(K_n)\) be the edge set of the labelled complete graph, and write \(\mathcal T_n\subseteq\mathbb F_2^{E_n}\) for the edge-incidence vectors of all spanning trees. For a frequency support \(S\subseteq E_n\), define the **unnormalized** Walsh multiplier
\[
W_n(S)=\sum_{T\in\mathcal T_n}(-1)^{|S\cap E(T)|}.
\]

**Theorem (first cancellation, including all equality cases).**

* If \(n\) is odd, \(W_n(S)\) is odd and hence nonzero for every \(S\subseteq E_n\).
* If \(n=2p\) with \(p\ge2\), then \(W_n(S)>0\) for every \(S\) with \(|S|<p-1\). For \(|S|=p-1\), one has \(W_n(S)\ge0\), and equality holds **if and only if** the negative-edge graph \(([n],S)\) is a star \(K_{1,p-1}\) on \(p\) vertices together with exactly \(p\) isolated vertices.

Therefore the least cardinality of any vanishing Walsh frequency for even \(n=2p\ge4\) is exactly \(p-1\), and the number of least-cardinality vanishing supports is
\[
N_{2p}=\begin{cases}
6,&p=2,\\
(2p)\binom{2p-1}{p-1},&p\ge3.
\end{cases}
\]
For \(p=2\), a single edge has two interchangeable choices of star center; the second formula would double-count it.

For a uniformly sampled spanning tree, \(W_n(S)/n^{n-2}\) is the expected parity character on \(S\). The theorem therefore identifies the smallest number of prescribed edge coordinates for which this character can be exactly unbiased, and proves strict positive bias for every smaller selection. The earlier known parity and nonzero-gap statements alone do not determine the first zero support or its graph-isomorphism class.

## Assumptions and scope

All graphs are simple and labelled; the character at \(S\) is the product of the signs \(-1\) on edges in \(S\) and \(+1\) elsewhere. Multipliers count trees without normalization; no probabilistic normalization or asymptotic interpretation is used. The claim concerns the **minimum cardinality of a vanishing character support**, not the smallest absolute value among nonzero multipliers, and does not classify all frequencies with larger support.

## Proof

Let \(H=([n],S)\) be the negative-edge graph, \(L_H\) its ordinary combinatorial Laplacian, and \(J\) the all-ones matrix. Assign edge weight \(-1\) on \(S\) and \(+1\) off \(S\). The weighted matrix-tree theorem, valid as a polynomial identity even for negative weights, gives \(W_n(S)\) as any cofactor of the signed weighted Laplacian
\[
L_{\mathrm{sgn}}=nI-J-2L_H.
\]
The all-ones vector lies in the kernel. On its orthogonal complement, the operator equals \(nI-2L_H\). If the eigenvalues of \(L_H\), with multiplicity, are \(0=\lambda_1,\lambda_2,\ldots,\lambda_n\), then
\[
W_n(S)=\frac1n\prod_{i=2}^{n}(n-2\lambda_i). \tag{1}
\]
The identity holds also when the signed weighted Laplacian has additional zero eigenvalues, because the cofactor-product identity is polynomial/continuous in the matrix entries.

We need the following elementary sharp bound. If a graph \(H\) has \(k\) edges, every Laplacian eigenvalue is at most \(k+1\). Indeed, every nontrivial connected component \(C\) has at most \(k+1\) vertices, since a connected graph with \(v\) vertices has at least \(v-1\) edges. On the vectors orthogonal to the all-ones vector of \(C\),
\[
L_C+L_{\overline C}=vI,
\]
and the complement Laplacian is positive semidefinite. Thus all eigenvalues of \(L_C\) are at most \(v\le k+1\). Isolated vertices contribute only zeros.

We also characterize equality when \(k\ge1\): if \(k+1\) is an eigenvalue of \(L_H\), then \(H\) has a connected component on exactly \(k+1\) vertices, using all \(k\) edges. Hence it is a tree, with the other vertices isolated. Equality of its top Laplacian eigenvalue with its number of vertices holds exactly when its complement is disconnected. To see the latter statement, use \(L_C+L_{\overline C}=vI-J\) on the all-ones orthogonal complement. If the complement is disconnected, take a nonconstant componentwise-constant vector orthogonal to the all-ones vector. Conversely, a vector with top eigenvalue \(v\) must lie in the complement Laplacian kernel beyond the constants, so the complement is disconnected.

Finally, a tree on \(v\ge2\) vertices has disconnected complement exactly when it is a star. For if the complement has a disconnected partition into nonempty parts of sizes \(a,b\) with \(a+b=v\), every one of their \(ab\) crossing edges belongs to the tree. Since \(ab\ge v-1\) and the tree has \(v-1\) edges, equality is necessary; it forces \(a=1\) or \(b=1\), and the tree is a star. Every star has disconnected complement.

Now assume \(n=2p\ge4\). If \(k=|S|<p-1\), then each \(\lambda_i\le k+1<p\), so all factors in (1) are strictly positive. At \(k=p-1\), every factor is nonnegative, and the product vanishes precisely when \(L_H\) has eigenvalue \(p=k+1\). By the equality characterization this occurs precisely for a star \(K_{1,p-1}\) with the other \(p\) vertices isolated. Counting possible centers and leaf subsets gives the claimed formula, correcting for the symmetry of a one-edge star when \(p=2\).

For odd \(n\), Cayley's formula gives \(|\mathcal T_n|=n^{n-2}\), which is odd. Every summand in \(W_n(S)\) is \(+1\) or \(-1\), so \(W_n(S)\equiv|\mathcal T_n|\equiv1\pmod2\); it cannot vanish. This completes the proof.

## Verification

Two included independent integer checkers reproduce the boundary in small orders. The signed-cofactor implementation enumerates **all** supports of size at most the threshold in orders \(n=4,6,8,10\), obtaining respectively \(6,60,280,1260\) zeros, all at the predicted degree, with no negatives through that degree. Separately, a Prüfer-code construction plus an integer Walsh-Hadamard transform checks all Fourier coefficients for \(n=3,4,5,6\), and reproduces the first-zero counts. The C++ checker uses fraction-free Bareiss elimination with exact divisibility assertions. These finite checks corroborate the proof, but do not substitute for its infinite argument.

Reproduce with `g++ -std=c++17 -O2 complete_tree_threshold_check.cpp -o check && ./check` and `python3 complete_tree_prufer_check.py`.

## Relationship to prior work

Martin--Reiner (arXiv:math/0302213, public v1 on 2003-02-18) establishes weighted spanning-tree enumerator methods for complete-graph products and threshold graphs; the all-edge-sign cancellation degree is not among its stated results. Duval--Klivans--Martin (arXiv:0802.2576, public v1 on 2008-02-19) gives general weighted matrix-tree results, including the classical formula used in the proof here. Burton--Pemantle gives determinantal local-edge marginals for random spanning trees. These general methods are recognized as prior knowledge, and are not claimed here as inventions. The asserted finding is specifically the sharp all-order *first vanishing character support* and its star-only equality classification.

## Limitations

The theorem does not identify the complete Fourier zero set for even orders, nor the nonzero multiplier magnitudes or sharp convolution inverse norms. Any claim of historical novelty is bounded by the stated source and semantic comparison checks; unindexed sources may exist. The calculation is a self-review mathematical argument, not an independent audit.

## References

1. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, arXiv:math/0302213v1 (2003-02-18); https://arxiv.org/abs/math/0302213 .
2. A. M. Duval, C. J. Klivans and J. L. Martin, *Simplicial Matrix-Tree Theorems*, arXiv:0802.2576v1 (2008-02-19); https://arxiv.org/abs/0802.2576 .
3. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Ann. Probab. 21 (1993), 1329–1371; https://arxiv.org/abs/math/0404048 .
4. A. Dall and J. Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, arXiv:1404.3876v1 (2014-04-15); https://arxiv.org/abs/1404.3876 .
