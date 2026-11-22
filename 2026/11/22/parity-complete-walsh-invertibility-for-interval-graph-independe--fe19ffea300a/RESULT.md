# Parity-complete Walsh invertibility for interval-graph independent sets

## Finding
Let \(G\) be any finite interval graph on \(n\geq0\) labelled vertices. Write \(\mathcal I(G)\) for all independent vertex subsets, including the empty set, and set \(N(G)=|\mathcal I(G)|\). On \(H=\mathbb F_2^n\), let \(f_G\) indicate the incidence vectors of \(\mathcal I(G)\), and let \(T_Gu=f_G*u\) be **unnormalized** XOR convolution. Then

\[
T_G\text{ is invertible}\quad\Longleftrightarrow\quad N(G)\text{ is odd}.
\]

More precisely, among the signed Walsh multipliers \(\lambda_G(s)=\sum_{S\in\mathcal I(G)}\prod_{i\in S}s_i\), for \(s\in\{-1,+1\}^n\), the minimum absolute magnitude is exactly \(0\) for even \(N(G)\), and exactly \(1\) for odd \(N(G)\). A signing attaining this parity-minimal magnitude can be constructed in \(O(n)\) time once the sorted interval representation and predecessor indices are known, or in \(O(n\log n)\) time from an unsorted interval representation. In the invertible case, with counting measure on \(H\),

\[
\|T_G^{-1}\|_{\ell^2(H)\to\ell^2(H)}=1,
\qquad
\kappa_2(T_G)=N(G).
\]

The interval-graph hypothesis is substantive. For the octahedral graph \(K_{2,2,2}\), the independent-set count is \(10\), but every signed Walsh multiplier is one of \(-2,2,6,10\), with respective multiplicities \(27,27,9,1\). Thus its independent-set convolution is invertible despite having an even number of independent sets.

## Assumptions and scope
An interval representation consists of finitely many nonempty closed real intervals \(I_i=[\ell_i,r_i]\); distinct vertices are adjacent exactly when their intervals meet. Endpoints may coincide and interval lengths may vary. Label the intervals by nondecreasing right endpoint, breaking ties arbitrarily. Define \(G_i\) as the subgraph on the first \(i\) vertices, and

\[
k_i=\#\{j<i:r_j<\ell_i\},\qquad 0\leq k_i<i.
\]

The earlier vertices nonadjacent to vertex \(i\) are exactly those with indices \(1,\dots,k_i\). Let \(Z_0=1\). For a choice of signs \(s_1,\ldots,s_i\), let \(Z_i\) be the signed independent-set sum of \(G_i\). All assertions are exact and include isolated vertices, disconnected interval graphs, empty graphs, and repeated endpoints. Fourier transforms are unnormalized sums, not expectations; the \(\ell^2\) norm is taken on the entire space of complex-valued functions on \(H\).

## Proof
**Signed recurrence.** Partition independent subsets of \(G_i\) according to whether they contain vertex \(i\). If not, their sum is \(Z_{i-1}\). If yes, their remaining vertices belong to \(G_{k_i}\), and their sum is \(s_iZ_{k_i}\). Consequently,

\[
Z_i=Z_{i-1}+s_iZ_{k_i},\qquad Z_0=1.
\]

**Greedy cancellation lemma.** Suppose signs through stage \(i-1\) have been fixed with \(Z_j\in\{-1,0,1\}\) for every \(j<i\). Both \(a=Z_{i-1}\) and \(b=Z_{k_i}\) belong to this set. If \(ab>0\), choose \(s_i=-1\); otherwise choose \(s_i=+1\). In either case \(|a+s_ib|\le1\): two nonzero terms of equal sign cancel; of opposite sign they already cancel with \(s_i=+1\); and if a term vanishes the other has magnitude at most one. Induction constructs a signing with \(Z_i\in\{-1,0,1\}\) for all \(0\le i\le n\). This is a finite, deterministic construction requiring one addition and comparison per vertex once the predecessor indices are known. Each predecessor is found by binary search in the sorted right endpoints, and sorting the input intervals takes \(O(n\log n)\) time.

**Parity and invertibility.** Every \(s_i\) is congruent to \(1\) modulo \(2\), so \(\lambda_G(s)\equiv N(G)\pmod 2\) for every signing. The greedy final value \(Z_n\) has the same parity as \(N(G)\) and magnitude at most one. It is therefore \(0\) when \(N(G)\) is even and \(\pm1\) when \(N(G)\) is odd. Conversely, odd parity excludes zero at every signing. Walsh characters form an orthogonal basis of complex functions on \(H\), and each is an eigenvector of \(T_G\) with multiplier \(\lambda_G(s)\). This establishes both the invertibility equivalence and the sharp minimum multiplier magnitude.

**Hilbert norm.** In the odd case, the sharp lower multiplier magnitude is one, so the norm of the inverse is one. The trivial character has multiplier \(N(G)\), and the triangle inequality gives \(|\lambda_G(s)|\le N(G)\) for every character. The ratio of largest and smallest singular values is thus exactly \(N(G)\).

**Sharp boundary.** In \(K_{2,2,2}\), any nonempty independent set lies wholly in one of the three size-two color classes. For signs \(s_{j,1},s_{j,2}\) within class \(j\),

\[
\lambda(s)=1+\sum_{j=1}^3\left((1+s_{j,1})(1+s_{j,2})-1\right)
=4t-2,
\]

where \(t\) is the number of classes whose two signs are both positive. The multiplicity at fixed \(t\) is \(\binom3t3^{3-t}\). This proves the four-level nonvanishing spectrum and \(N(G)=\lambda(+1)=10\). The graph contains an induced four-cycle and hence is not an interval graph.

**All powers of paths.** As a corollary, for every integer \(h\ge0\), all independent-set XOR convolution operators of \(P_n^h\) are invertible exactly when the ordinary count \(q_n\) is odd. Here \(q_0=1\) and \(q_i=q_{i-1}+q_{\max(0,i-h-1)}\) for \(i\ge1\); this computes the answer modulo two in linear time, for arbitrary \(n\) and \(h\). No fixed-power restriction is required.

## Verification
The self-contained Python 3 verifier `verify.py` recomputes the signed recurrence and enumerates independent-set incidence vectors independently. It checks 600 generated interval families of orders zero through nine (complete Walsh scans for orders through seven), 396 independent-set path-power parameter pairs, and all 64 characters of \(K_{2,2,2}\). Its recorded output is:

```
PASS: interval examples and path powers: 996
PASS: octahedral obstruction: {-2: 27, 2: 27, 6: 9, 10: 1}
```

These finite tests corroborate the definitions and boundary, but the universal interval-graph theorem is proved by the recurrence and induction above, not by finite enumeration. Run with `python3 verify.py`; no third-party packages are needed.

## Relationship to prior work
Codara and D'Antona (2012, 2014) study the independent-subset counts and Hasse diagrams for powers of paths and cycles. Their unsigned deletion recurrence is a special case of the present interval-prefix recurrence, but their inspected enumerative statements do not give a signing realizing the parity lower bound, an interval-graph Fourier criterion, or the octahedral boundary. Gupta, Lee, and Leung (1982) give efficient interval-graph optimization algorithms, not signed Walsh spectra. Published results for squared-path independent sets and for clique windmills establish specialized Fourier criteria; their statements do not imply a theorem for all interval representations. The octahedral counterexample shows why one cannot infer the criterion from parity alone for arbitrary graphs.

## Limitations
The sharp \(\ell^2\) inverse norm is asserted only when the operator is invertible; no uniform sharp pseudoinverse or \(\ell^1\)/\(\ell^\infty\) projection norm is claimed in singular cases. The statement does not extend to all graphs, as the octahedral counterexample proves. Search-based historical comparison cannot exclude an unindexed equivalent formulation; a small number of adjacent records were available only as public summaries rather than complete proofs. No independent mathematical audit has been performed.

## References
1. P. Codara and O. M. D'Antona, *On the independent subsets of powers of paths and cycles*, arXiv:1210.5561, first posted 2012-10-19, https://arxiv.org/abs/1210.5561.
2. P. Codara and O. M. D'Antona, *Generalized Fibonacci and Lucas cubes arising from powers of paths and cycles*, arXiv:1410.4080, first posted 2014-10-15, https://arxiv.org/abs/1410.4080.
3. U. I. Gupta, D. T. Lee, and J. Y.-T. Leung, *Efficient algorithms for interval graphs and circular-arc graphs*, Networks 12 (1982), 459–467, https://doi.org/10.1002/net.3230120410.
4. *Independence Polynomial*, Wolfram MathWorld, https://mathworld.wolfram.com/IndependencePolynomial.html (background definitions).
