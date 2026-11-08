# Periodic interval continua and cyclotomic entropy factors at noncoprime modular steps

## Finding
For integers \(n\ge4\) and \(1\le q<n\) with \(g=\gcd(n,q)>1\), set \(\ell=n/g\). Let \(f_{n,q}\colon[0,n-1]\to[0,n-1]\) be the continuous map affine on each unit interval, with \(f_{n,q}(j)=(j+q)\bmod n\) for all integer vertices \(0\le j<n\). Let \(J_i=[i,i+1]\) for \(0\le i\le n-2\), and define the \((n-1)\)-square binary interval Markov matrix by \((A_{n,q})_{ij}=1\) precisely when \(f_{n,q}(J_i)\supseteq J_j\).

**Theorem (complete noncoprime boundary structure).** The grid-interval dynamics contain exactly \(g-1\) disjoint cycles of \(\ell\) unit intervals on which \(f_{n,q}^{\circ\ell}\) is the identity pointwise; every interior point of these intervals has least period \(\ell\). The remaining \(\ell-1\) interval states form a renewal block with one first-return path of each length \(1,\ldots,\ell-1\), and transitions out of that block may enter the periodic interval cycles but never return. In particular,
\[
\det(xI-A_{n,q})=
\left(x^{\ell-1}-\sum_{j=0}^{\ell-2}x^j\right)
(x^\ell-1)^{g-1}.
\]
The finite **symbolic graph** periodic-path zeta function is
\[
\zeta_{A_{n,q}}(z)=\exp\!\left(\sum_{k\ge1}\frac{\operatorname{tr}(A_{n,q}^k)}{k}z^k\right)
=\frac1{(1-z-\cdots-z^{\ell-1})(1-z^\ell)^{g-1}}.
\]
If \(\lambda_d\) is the unique positive root of \(x^d-\sum_{j=0}^{d-1}x^j\), with \(\lambda_1=1\), then
\[
 h_{\mathrm{top}}(f_{n,q})=\log\lambda_{\ell-1}.
\]
Hence the entropy is exactly zero when \(\ell=2\), and for \(\ell\ge3\) it depends only on the reduced order \(\ell\) of the modular translation, **not** the number \(g\) of its orbits. By contrast, for every \(g>1\) the map has uncountably many fixed points of its \(\ell\)-th iterate, so its ordinary physical-point Artin–Mazur zeta series is not defined by finite fixed-point counts. The rational expression above is strictly the zeta function of the finite Markov graph.

## Assumptions and scope
All parameters are integers with \(n\ge4\), \(1\le q<n\), and \(g=\gcd(n,q)>1\). Thus \(2\le\ell=n/g\le n/2\). Interval boundaries and the map are as defined in the theorem. “Periodic interval cycle” means a cycle of distinct full grid intervals carried homeomorphically onto the next and returned by the exact identity after \(\ell\) steps. “Graph zeta” counts indexed closed walks of the directed Markov graph; it is not asserted to count individual periodic points of the interval map.

## Proof
**1. One exceptional full-covering branch.** Put \(b=n-q-1\). For every \(i\in\{0,\ldots,n-2\}\setminus\{b\}\), the adjacent images \((i+q)\bmod n\) and \((i+q+1)\bmod n\) are consecutive with increasing order. Therefore \(f_{n,q}|_{J_i}\) is a unit-slope translation and sends \(J_i\) onto \(J_{(i+q)\bmod n}\). The target subscript is never \(n-1\) because its sole predecessor among the vertices is \(b\), which was excluded. At \(i=b\), the adjacent images are \(n-1\) and \(0\): the affine branch has slope \(-(n-1)\) and maps \(J_b\) onto the whole interval \([0,n-1]\). Thus its Markov row is all ones.

**2. The modular orbit decomposition.** Addition by \(q\) on \(\mathbb Z/n\mathbb Z\) has precisely \(g\) distinct cycles, each of length \(\ell\), indexed by residue classes modulo \(g\). Exactly one such vertex cycle contains \(n-1\). Removing \(n-1\) from the interval-label set leaves that cycle as a directed path of \(\ell-1\) labels. Its last label is \(b=n-q-1\); its first label is \(q-1\). Every other modular cycle survives completely as a directed cycle of \(\ell\) interval labels, and its edges come from slope-one translations. The exceptional full-covering row may point from the shortened path to any surviving cycle, but no edge from a surviving cycle points back to the path. Consequently a simultaneous permutation of rows and columns makes \(A_{n,q}\) block upper triangular with the shortened-path block \(R_{\ell-1}\) and \(g-1\) disjoint cyclic permutation blocks of size \(\ell\). Here \(R_d\) has edges from state \(r\) to \(r+1\) for \(1\le r<d\) and from state \(d\) to every state \(1,\ldots,d\). This statement also covers \(d=1\), when \(R_1=[1]\).

**3. Periodic continua and determinant.** Every surviving modular cycle carries \(\ell\) unit intervals homeomorphically to one another by translations; the signed translation offsets telescope to zero after \(\ell\) steps, so \(f_{n,q}^{\circ\ell}=\mathrm{id}\) on each of them. Distinct intervals in one orbit have disjoint interiors, hence every interior point has least period \(\ell\). There are \(g-1\) such cycles. Every grid interval in the shortened path eventually maps via the exceptional full-covering branch if it continues within that path, so no other full grid-interval translation cycle exists. For the renewal block, direct cofactor expansion (or the eigenvector recurrence) gives \(\det(xI-R_d)=x^d-x^{d-1}-\cdots-x-1\). The determinant of each cyclic permutation block is \(x^\ell-1\). Multiplying the diagonal-block determinants proves the stated characteristic polynomial.

**4. Zeta and entropy.** For every finite adjacency matrix \(A\), the formal identity \(\exp(\sum_{k\ge1} \operatorname{tr}(A^k)z^k/k)=1/\det(I-zA)\) holds, e.g. by the formal logarithm expansion of the determinant. Applying the established factorization yields the symbolic zeta formula. The renewal block is strongly connected and has a self-loop at its terminal state; its Perron root is \(\lambda_d\) (for \(d=1\), this is 1). All surviving cycles have spectral radius 1, so \(\rho(A_{n,q})=\lambda_{\ell-1}\). The usual finite Markov-interval lap-count upper bound gives \(h_{\rm top}(f_{n,q})\le\log\rho(A_{n,q})\). For \(\ell\ge3\), every sufficiently long admissible path that stays in the renewal component visits the full-covering branch at least once every \(\ell-1\) steps; the corresponding inverse branches thus uniformly contract by at least \((n-1)^{-1}\) per \(\ell-1\) steps. Their compact nested cylinders separate different interior symbolic paths and form an expanding Markov subsystem with entropy \(\log\lambda_{\ell-1}\), giving the matching lower bound. If \(\ell=2\), the upper bound already gives zero. This proves the entropy formula.

Finally, the \(g-1\ge1\) periodic interval cycles contain uncountably many points fixed by \(f_{n,q}^{\circ\ell}\). Thus the physical-point fixed-count series has an infinite coefficient at index \(\ell\); the graph zeta cannot be identified with that series. For example, \((n,q)=(6,2)\) has \(g=2\), \(\ell=3\), entropy \(\log((1+\sqrt5)/2)\), and a whole period-three interval cycle; \((n,q)=(6,3)\) has \(g=3\), \(\ell=2\), zero entropy, and two independent period-two interval cycles.

## Verification
The included standard-library Python script `verify.py` independently constructs the Markov adjacency matrix and checks the claimed integer characteristic polynomial for **all** \(3\le n\le14\) and \(1\le q<n\), using exact fraction-free integer determinants at enough integer inputs to identify each characteristic polynomial. It also replays the identity \(f_{n,q}^{\circ\ell}(x)=x\) on nonexceptional modular cycles for exact rational test points. It prints `MODULAR_INTERVAL_GCD_BLOCK_FACTORIZATION_OK` and `EXACT_NONCOPRIME_PERIODIC_INTERVAL_CYCLES_OK`. The proof above, not the finite checks, establishes the theorem for all permitted dimensions.

## Relationship to prior work
Yihan Wang's 2023 paper develops covering-system periodic-point methods for **single-cycle permutations** and states that modular translations with \(\gcd(n,q)=1\) have the full staircase of characteristic return times (Example 3.6). The original interval-map polynomial and Markov-matrix method goes back at least to Byers (1986). A recent paper of Takenouchi (2025) develops characteristic-polynomial formulas for **refinements of** Markov partitions. Those statements do not give the noncoprime arithmetic block factorization or the resulting periodic continuum / physical-zeta obstruction. The coprime-step case is a different, previously treated case and is not claimed here. Classical matrix spectral and zeta identities are standard tools, not new results.

## Limitations
Only integer-vertex modular-translation connect-the-dots maps are covered; no claim is made for arbitrary permutations, arbitrary continuous realizations of the vertex data, or continuous perturbations. The full physical Artin–Mazur zeta does not have finite coefficients in this noncoprime regime, and the rational graph zeta must not be substituted for it. Independent assessment of novelty and proof has not been performed. An equivalent unindexed calculation remains a publication-priority risk.

## References
1. Y. Wang, *On Periodic Points in Covering Systems*, arXiv:2306.10523v1, first posted 18 June 2023, https://arxiv.org/html/2306.10523v1 (especially Example 3.6 and Section 4).
2. B. Byers, *A Note on Permutations and Topological Entropy of Continuous Maps of the Interval*, Canadian Mathematical Bulletin 29 (1986), 91–94, https://doi.org/10.4153/CMB-1986-017-6.
3. Y. Takenouchi, *Canonical Form for the Zero-One Matrix Induced by the Markov Map*, Contributions to Mathematics 11 (2025), 8–13, https://doi.org/10.47443/cm.2025.015.
4. L. Block, A. M. Blokh, E. M. Coven, *Zero Entropy Permutations*, International Journal of Bifurcation and Chaos 5 (1995), 901–919, https://doi.org/10.1142/S0218127495000703.
