# Exact minimum-absorber placement census on the Heawood quantum network

## Finding

Let \(H\) be the 14-vertex Heawood graph, the point–line incidence graph of the Fano plane. A continuous-time one-particle quantum walk has uniform nonzero hopping \(J\), and sites in a set \(S\) carry arbitrary strictly positive local loss rates. Say that \(S\) is *completely absorbing* if the surviving norm tends to zero for every initial state.

The minimum possible cardinality of a completely absorbing set is **six**. Among the \(\binom{14}{6}=3003\) six-site sets, **exactly 1890** are completely absorbing; the other \(1113\) leave at least one coherent dark state. If \(k\) absorbers are at point vertices and \(6-k\) at line vertices, the exact successful-placement polynomial is
\[
B(t)=7+84t+420t^2+868t^3+420t^4+84t^5+7t^6.
\]
Thus a uniformly selected six-site set captures every initial state with probability \(1890/3003=90/143\). Under the 336 automorphisms of the Heawood graph, all six-site sets fall into exactly 24 orbits, comprising 14 successful and 10 unsuccessful orbits. The successful orbit sizes are \(336\), eight copies of \(168\), \(84\), \(56\), two copies of \(28\), and \(14\). The unsuccessful orbit sizes are five copies of \(168\), two copies of \(84\), two copies of \(42\), and \(21\).

There is also a direct, complete geometric decision criterion for an individual six-site set: form the seven-by-seven matrix whose first row consists entirely of ones and whose other six rows are the coordinate indicators for chosen point sites or the three-point incidence indicators for chosen line sites. The set is completely absorbing **if and only if** this integer matrix is nonsingular.

## Assumptions and scope

Take Fano points \(P=\{1,2,\ldots,7\}\), regarded as the seven nonzero three-bit vectors, and Fano lines \(\ell_{ab}=\{a,b,a\mathbin{\mathrm{xor}}b\}\) for distinct points \(a,b\). The seven distinct lines are obtained by deduplication. The 14 graph vertices are the seven points and seven lines; adjacency is incidence. The adjacency matrix in point–line order is
\[
A=\begin{pmatrix}0&B\\ B^\mathsf T&0\end{pmatrix},
\qquad B_{p\ell}=\mathbf 1_{\{p\in\ell\}}.
\]
Let \(J>0\) be uniform hopping and let \(\Gamma=\sum_{s\in S}\gamma_s|s\rangle\langle s|\), with every \(\gamma_s>0\). The effective no-jump Hamiltonian is \(H_{\mathrm{eff}}=JA-i\Gamma\). Complete absorption means \(\lim_{t\to\infty}\|e^{-iH_{\mathrm{eff}}t}\psi\|^2=0\) for every vector \(\psi\), equivalently vanishing surviving trace for every initial density matrix. It does not mean capture within a uniform bounded time.

## Proof

**1. Dark-state criterion.** For any eigenvector \(v\) of \(H_{\mathrm{eff}}\) with eigenvalue \(\lambda\), the imaginary part of its Rayleigh quotient is
\[
\operatorname{Im}\lambda=-\frac{\langle v,\Gamma v\rangle}{\|v\|^2}\le0.
\]
Equality holds exactly when \(v\) vanishes on all trap sites. In that case \(Av=(\lambda/J)v\), so it is an adjacency eigenvector. Conversely any adjacency eigenvector vanishing on \(S\) remains nondecaying. As the space is finite dimensional, all initial states decay exactly when no such adjacency eigenvector exists: absence of a real eigenvalue of the dissipative matrix places its entire spectrum strictly below the real axis, and its matrix exponential tends to zero even in the presence of Jordan blocks.

**2. Spectral reduction.** The Fano incidence identities give
\[
BB^\mathsf T=B^\mathsf TB=2I_7+\mathbf1\mathbf1^\mathsf T.
\]
Thus \(A\) has eigenvalues \(3,-3\) of multiplicity one each, and \(\sqrt2,-\sqrt2\) of multiplicity six each. The \(\pm3\) eigenvectors have nonzero amplitude at every vertex. For \(\lambda=\pm\sqrt2\), every eigenvector has the form
\[
\begin{pmatrix}u\\\lambda^{-1}B^\mathsf Tu\end{pmatrix},
\qquad u\in\mathbf1^\perp\subset\mathbb C^7.
\]
It vanishes at selected point \(p\) precisely when \(u_p=0\), and at selected line \(\ell\) precisely when \(\sum_{p\in\ell}u_p=0\). The signs of \(\lambda\) cannot change this zero condition. Therefore the dark subspace vanishes exactly when the chosen indicator rows restrict injectively to the six-dimensional zero-sum space.

**3. Sharp lower bound and matrix test.** Fewer than six detector rows cannot inject a six-dimensional eigenspace into a smaller-dimensional observation space. Six selected point vertices are sufficient (they force six coordinates to zero, with zero sum forcing the seventh); six selected line vertices likewise suffice by invertibility of \(B\). For any six-site selection, the preceding injectivity criterion is equivalent to rank seven of the matrix consisting of the all-ones row followed by its six point-coordinate or line-incidence rows. This proves both the sharp minimum six and the exact if-and-only-if geometric criterion.

**4. Exhaustive finite classification.** Label the first seven sites by the points \(1,\ldots,7\) and the last seven by the lexicographically ordered distinct Fano lines. For each of the exactly \(\binom{14}{6}=3003\) six-element subsets, compute the rank of the seven-by-seven integer matrix in Step 3 by fraction-free elimination. The attached standalone code implements these complete loops and checks the counts:

| Chosen points \(k\) | Successful | Unsuccessful |
|---:|---:|---:|
| 0 | 7 | 0 |
| 1 | 84 | 63 |
| 2 | 420 | 315 |
| 3 | 868 | 357 |
| 4 | 420 | 315 |
| 5 | 84 | 63 |
| 6 | 7 | 0 |
| **Total** | **1890** | **1113** |

A complementary symmetry census constructs all \(168\) invertible linear maps of \(\mathbb F_2^3\), their induced permutations of point and line vertices, and the point–line polarity \(p\mapsto\{q:p\cdot q=0\}\). These produce 336 checked graph automorphisms. Their action splits the entire 3003-element selection set into 24 disjoint orbits, with 14 good and 10 bad; orbit sizes sum to 1890 and 1113 as stated. Every orbit's classification is checked to be constant. This is finite exhaustive reasoning rather than a statistical sample.

## Verification

Run `python3 verify_heawood.py` with Python 3.9 or newer and no nonstandard dependencies. The code reconstructs the graph directly from Fano arithmetic, enumerates all 3003 selections and performs exact integer ranks, then independently reconstructs each selection's adjacency Krylov space and checks its rank modulo the prime 1000003. It finally constructs and verifies all 336 automorphisms and 24 six-site orbits. Its observed outputs include `VERIFY_OK six_subsets=3003 successful=1890 unsuccessful=1113` and `VERIFY_OK symmetry_order=336 orbits=24 good_orbits=14`. The modular Krylov comparison is independent corroboration; the exact integer rank loop together with Steps 1–3 is the exhaustive proof.

## Relationship to prior work

The standard Heawood point–line description, adjacency eigenvalues and automorphism group were known long before this calculation; see Brouwer's graph catalogue. Krovi and Brun (2006) discuss quantum dark-state / hitting-time obstructions, and Agliari, Mülken and Blumen (2009) formulate non-Hermitian absorption and trap-geometry dependence. Neither the underlying degeneracy bound nor the general non-Hermitian trapping formalism is claimed as new. The narrower contribution here is the exact optimal-size placement census, its point–line generating polynomial, the full 24-orbit success/failure split, and the Fano incidence rank test on this physical network. An unindexed exact controllability-matroid enumeration could predate these numbers; that historical priority question is not conclusively settled.

## Limitations

This treats one-particle coherent uniform nearest-neighbor hopping on the exact Heawood incidence graph and strictly positive diagonal losses. It classifies eventual absorption for every initial pure or mixed state, not finite-time decay rates, optimality among other graphs, noisy or disordered Hamiltonians, interacting particles, or finite-rate detection protocols involving repeated projections. The independent modular Krylov check alone would not prove an infinite statement; the analytic spectral reduction and exhaustive exact integer calculation supply the proof for this finite graph.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094 (first posted 2006-06-10); https://arxiv.org/abs/quant-ph/0606094.
2. E. Agliari, O. Mülken and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288 (first posted 2009-03-19); https://arxiv.org/abs/0903.3288.
3. A. E. Brouwer, *Heawood graph*, distance-regular graph catalogue; https://aeb.win.tue.nl/drg/graphs/Heawood.html.
