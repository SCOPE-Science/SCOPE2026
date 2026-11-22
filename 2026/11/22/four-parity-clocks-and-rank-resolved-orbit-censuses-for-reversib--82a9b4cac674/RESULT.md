# Four parity clocks and rank-resolved orbit censuses for reversible waves on symmetric designs

## Finding
Let \(D\) be any nontrivial symmetric \(2\)-\((v,k,\lambda)\) design, \(2\leq k<v\), with binary point-block incidence matrix \(B\) and binary rank \(\rho\). Its point-block incidence graph has adjacency matrix \(A=\begin{psmallmatrix}0&B\\ B^{\mathsf T}&0\end{psmallmatrix}\). For any finite field \(\mathbb F_Q\) of order \(Q=2^f\), \(f\geq1\), consider the reversible two-row update
\[
T(u,w)=(Au+w,u),\qquad (u,w)\in(\mathbb F_Q^{2v})^2.
\]
All \(Q^{4v}\) states are periodic from time zero. The **exact order of this permutation** is determined by the parities of \((k,\lambda)\):

| \(k\) | \(\lambda\) | Exact global order |
|---|---|---|
| even | even | \(4\) |
| odd | even | \(6\) |
| even | odd | \(6\) |
| odd | odd | \(12\) |

More precisely, write \(b_1(t)=\min\{2,2^{\nu_2(t)}\}\), \(b_2(t)=\min\{4,2^{\nu_2(t)}\}\), and \(c(t)=2b_1(t)\mathbf1_{3\mid t}\). The number of configurations fixed after exactly \(t\geq1\) updates is \(Q^{E(t)}\), where
\[
E(t)=\begin{cases}
2\rho b_2(t)+(2v-4\rho)b_1(t), & k,\lambda\text{ even},\\
v c(t), & k\text{ odd},\ \lambda\text{ even},\\
2b_1(t)+(v-1)c(t), & k\text{ even},\ \lambda\text{ odd},\\
c(t)+2(\rho-1)b_2(t)+(2v+2-4\rho)b_1(t),& k,\lambda\text{ odd}.
\end{cases}
\]
Thus for every \(d\geq1\), the number of *primitive temporal orbits* of length \(d\) equals
\[
\frac1d\sum_{e\mid d}\mu(d/e)Q^{E(e)}.
\]
It is zero unless \(d\) divides the corresponding global order. The sets of realized least periods in the four rows of the table are, respectively, \(\{1,2,4\}\), \(\{1,3,6\}\), \(\{1,2,3,6\}\), and \(\{1,2,3,4,6,12\}\). In all four cases the fixed-state count recovers the binary incidence rank by the simple identity \(|\operatorname{Fix}(T)|=Q^{2(v-\rho)}\). For a fixed parameter set, two such design waves have the same complete periodic-point census precisely when their binary incidence ranks agree.

A concrete contrast already appears among seven-point designs: the Fano plane \(2\)-\((7,3,1)\) has period \(12\), whereas its symmetric complementary design \(2\)-\((7,4,2)\) has period \(4\). More generally the classification covers symmetric designs with \(\lambda>1\), not only projective planes.

## Assumptions and scope
A symmetric \(2\)-\((v,k,\lambda)\) design has \(v\) labelled points and \(v\) labelled blocks, each incident with \(k\) members of the other side; any distinct pair of points (and any distinct pair of blocks) have exactly \(\lambda\) common incident members. Nontrivial means \(2\le k<v\). Necessarily \(k(k-1)=\lambda(v-1)\). The graph is undirected, simple and bipartite. Neither graph symmetry nor temporal phase is identified in the labelled counts. Characteristic is exactly two, but the field may be any finite extension. The rank \(\rho\) is over \(\mathbb F_2\) and is unchanged after scalar extension to \(\mathbb F_Q\).

## Proof
**1. Incidence reduction.** Counting common blocks (and dual common points) gives the standard symmetric-design identities
\[
 BB^{\mathsf T}=B^{\mathsf T}B=(k-\lambda)I+\lambda J,
 \qquad B\mathbf1=B^{\mathsf T}\mathbf1=k\mathbf1.
\]
After reduction modulo two, this implies \(A^2=\operatorname{diag}(BB^{\mathsf T},B^{\mathsf T}B)\). We classify all adjacency Jordan blocks over \(\mathbb F_2\).

**2. Both parameters even.** Here \(A^2=0\) and \(\operatorname{rank}(A)=2\rho\). Hence \(A\) has exactly \(2\rho\) nilpotent Jordan blocks of size two and \(2v-4\rho\) of size one. Nontrivial incidence ensures \(\rho\geq1\).

**3. Odd \(k\), even \(\lambda\).** Here \(BB^{\mathsf T}=I\), so \(B\) is invertible and \(A^2=I\). Since \(\operatorname{rank}(A+I)=v\), there are exactly \(v\) size-two Jordan blocks with eigenvalue one.

**4. Odd \(\lambda\).** The design equation implies \(v\) is odd. Therefore each shore decomposes as the direct sum of the constants \(U=\langle\mathbf1\rangle\) and the zero-sum subspace \(W=\ker\mathbf1^{\mathsf T}\), preserved by both incidence maps. On \(W\), the all-ones matrix \(J\) vanishes.

If \(k\) is even, \(A\) is zero on the two constant vectors, while \(A^2=I\) on \(W\oplus W\); thus \(A\) has two size-one zero blocks and \(v-1\) size-two one-eigenvalue blocks. In particular \(\rho=v-1\).

If \(k\) is odd, \(A\) swaps the two constants (one size-two one-eigenvalue block), and is square-zero on \(W\oplus W\). As \(B\) restricts to a map of rank \(\rho-1\) on \(W\), the remaining Jordan blocks are \(2(\rho-1)\) zero-eigenvalue blocks of size two and \(2v+2-4\rho\) of size one. The last multiplicity is nonnegative by square-zero rank-nullity. Nontrivial block incidence ensures \(\rho-1\geq1\).

**5. Exact reversible-wave block transfer.** Put \(p(X)=X^2+X+1\). Since \(T\) has inverse \((u,w)\mapsto(w,u+Aw)\), every finite state is already periodic. Direct substitution, or \(T+T^{-1}=\operatorname{diag}(A,A)\), gives the three elementary transfers of adjacency Jordan blocks to temporal cyclic modules:
\[
 J_1(0)\mapsto\mathbb F_Q[X]/(X+1)^2,\quad
 J_2(0)\mapsto\mathbb F_Q[X]/(X+1)^4,\quad
 J_2(1)\mapsto\mathbb F_Q[X]/p(X)^2.
\]
For a size-two block at zero, the temporal characteristic polynomial is \((X+1)^4\) and \((T+I)^2\) has rank two on its four-space, forcing a single size-four block. For a size-two block at one, \(p(T)=T\operatorname{diag}(A+I,A+I)\) has rank two and square zero on its four-space; hence its module is \(p(X)^2\), not two independent \(p(X)\)-blocks. The size-one zero transfer is the immediate two-dimensional calculation. These module identities hold after every characteristic-two field extension, even if \(p\) becomes reducible over that extension.

**6. Counts, sharpness and rank.** A temporal cyclic module \(\mathbb F_Q[X]/g(X)\) contributes \(\deg\gcd(g(X),X^t-1)\) to \(\dim\ker(T^t-I)\). In characteristic two, \((X+1)\) occurs in \(X^t-1\) with multiplicity \(2^{\nu_2(t)}\); \(p(X)\) occurs with this multiplicity exactly when \(3\mid t\). Substituting the block counts from steps 2–4 yields the four formulas for \(E(t)\). The three temporal primary blocks have exact orders \(2,4,6\), respectively. In each case all asserted necessary blocks occur, so their least common multiple is the stated sharp order. The size-four \((X+1)\)-block realizes periods \(1,2,4\), and the \(p(X)^2\)-block realizes only \(1,3,6\); combining the available primary blocks yields the exact period sets listed above. In particular, the odd-\(k\), even-\(\lambda\) case has no period-two nonzero states despite global order six. Divisor Möbius inversion gives the primitive populations. Finally, substitution at \(t=1\) yields \(E(1)=2(v-\rho)\) in every case. Since the expressions otherwise depend only on \((v,k\bmod2,\lambda\bmod2,\rho)\), equality of ranks is also sufficient for equality of all fixed counts for a common parameter set.

## Verification
The included separately written scripts `check_matrix.py` and `verify_orbits.py` require only Python 3. The first constructs six actual symmetric designs with parameters \((3,2,1)\), \((4,3,2)\), \((7,3,1)\), \((7,4,2)\), \((11,5,2)\), and \((15,7,3)\), checks all incidence multiplicities, and directly compares exact Gaussian-elimination nullities of \(T^t-I\) with \(E(t)\) for all \(1\leq t\leq12\), including sharp matrix orders. The second implements the per-vertex wave update directly for \(v=3,4\), exhausts respectively \(2^{12}=4096\) and \(2^{16}=65536\) states, and verifies every periodic-point count via its least-period census. Both were executed successfully. The all-design proof is algebraic; tests are corroboration and do not constitute an extrapolation from finite samples.

## Relationship to prior work
General reversible two-time-level cellular automata and their matrix equivalents are established by Macfarlane (2004), and by Vlasov (2013). Symmetric-design incidence matrices and their Gram identities are classical, as detailed in Tonchev's lecture notes. The published *incidence-rank clock* result for projective planes supplies the \(\lambda=1\) subfamily, and is explicitly not claimed here as novel. The strongly regular graph wave classification concerns diameter-two graphs, rather than the bipartite incidence graphs here (which have diameter three in every nontrivial symmetric design). The asserted new classification concerns **all nontrivial symmetric designs**, particularly positive even intersection number \(\lambda\), with four parity regimes and rank-resolved complete temporal orbits; none of the inspected sources tabulates or states this result for the full design family.

## Limitations
Only finite fields of characteristic two and the specified reversible linear dynamics are covered; the result is not a characterization of all designs or of all possible incidence ranks. The universal clocks do not distinguish nonisomorphic designs of identical parameter and binary rank. Independent mathematical validation has not been performed, and an equivalent in unindexed historical work is possible. Verification runs include six particular designs, not an exhaustive enumeration of all designs.

## References
- A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (2004), 10791–10814, first published 2004-10-28. https://doi.org/10.1088/0305-4470/37/45/006
- A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18. https://arxiv.org/abs/1311.4297
- V. D. Tonchev, *An Introduction to Coding Theory*, lecture notes, sections on symmetric designs and incidence matrices. https://pages.mtu.edu/~tonchev/Coding-Theory-Tohoku-June-09.pdf
- *The incidence-rank clock of reversible waves on finite projective planes*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-incidence-rank-clock-of-reversible-waves-on-finite-projectiv--fe075b4d8619
- *Three universal wave periods and spectrally invisible orbit counts on strongly regular graphs*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-universal-wave-periods-and-spectrally-invisible-orbit-coun--6be21916ed4f
