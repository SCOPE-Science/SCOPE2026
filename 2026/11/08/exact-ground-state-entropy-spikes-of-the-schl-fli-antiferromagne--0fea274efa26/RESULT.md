# Exact ground-state entropy spikes of the Schläfli antiferromagnet

## Finding

Let \(G\) be the Schläfli graph on \(27\) vertices, the unique strongly regular graph with parameters \((27,16,10,8)\). For the classical antiferromagnetic Ising Hamiltonian
\[
\mathcal H_{J,h}(\sigma)=J\sum_{uv\in E(G)}\sigma_u\sigma_v-h\sum_{v\in V(G)}\sigma_v,
\qquad \sigma_v\in\{-1,+1\},\quad J>0,\ h\geq0,
\]
write \(t=h/J\) and let \(\mathcal E_0(t)\) be the minimum of \(\mathcal H_{J,h}/J\). Then
\[
\mathcal E_0(t)=
\begin{cases}
-24-3t,&0\leq t\leq4,\\
-9t,&4\leq t\leq8,\\
48-15t,&8\leq t\leq12,\\
120-21t,&12\leq t\leq16,\\
216-27t,&16\leq t.
\end{cases}
\]
For strictly positive noncritical \(t\), the total magnetization \(M=\sum_v\sigma_v\) and ground-state multiplicity are exactly:

| Field interval \(t\) | Magnetization \(M\) | Number of ground states |
| --- | ---: | ---: |
| \((0,4)\) | \(3\) | \(22,968\) |
| \((4,8)\) | \(9\) | \(8,400\) |
| \((8,12)\) | \(15\) | \(1,080\) |
| \((12,16)\) | \(21\) | \(45\) |
| \((16,\infty)\) | \(27\) | \(1\) |

Exactly at the fields \(t=0,4,8,12,16\), the ground-state multiplicities are respectively
\[
1,037,376;\qquad630,444;\qquad138,000;\qquad10,035;\qquad208.
\]
The sets of admissible down-spin counts \(k=|\{v:\sigma_v=-1\}|\) at these fields are, respectively, \(\{12,13,14,15\}\), \(\{9,10,11,12\}\), \(\{6,7,8,9\}\), \(\{3,4,5,6\}\), and \(\{0,1,2,3\}\). For negative fields the law follows by global spin reversal.

In fact, for each integer \(0\leq k\leq27\), the maximum cut with exactly \(k\) vertices on one side is
\[
C(k)=2\left\lfloor\frac{k(27-k)}3\right\rfloor.
\]
This cut profile is a short consequence of the known spectrum and proper nine-coloring of \(G\); **the claim of new mathematical content is the exact joint ground-state energy/degeneracy classification**, particularly the transition entropies, not the already documented spectrum, coloring, or isolated graph parameters.

## Assumptions and scope

The graph is fixed and finite, with no thermodynamic-limit claim. An explicit labeling is used for reproducibility. Index \(0,\ldots,5\) by \(E_i\), index \(6,\ldots,20\) by \(L_{ij}\) for \(0\leq i<j\leq5\) in lexicographic order, and index \(21,\ldots,26\) by \(C_i\). Distinct vertices are adjacent in \(G\) if and only if the corresponding lines of the abstract cubic-surface model are *skew* (do not intersect). The line-intersection relation is:

- \(E_i\) intersects \(L_{jk}\) exactly when \(i\in\{j,k\}\), and intersects \(C_j\) exactly when \(i\ne j\).
- \(L_{ij}\) intersects \(L_{kl}\) exactly when the two index pairs are disjoint; it intersects \(C_k\) exactly when \(k\in\{i,j\}\).
- Distinct \(E_i\) do not intersect one another, and distinct \(C_i\) do not intersect one another.

The resulting graph has degree \(16\), \(216\) edges, and common-neighbor parameters \(10\) (adjacent pairs), \(8\) (nonadjacent pairs), uniquely identifying the Schläfli graph. The ground-state multiplicities count **labeled spin configurations** without quotienting by graph automorphisms or global spin reversal.

## Proof

**1. Conversion to cuts.** Let \(S\) be the set of down spins, \(|S|=k\), and let \(c(S)\) count edges from \(S\) to its complement. Because \(|E(G)|=216\),
\[
\mathcal H_{J,h}(\sigma)/J=216-2c(S)-t(27-2k).
\]
Thus at each fixed \(k\), a ground state corresponds exactly to a maximum-cut subset of size \(k\).

**2. Exact size-constrained cut profile.** The strongly regular parameters imply adjacency spectrum \(\{16^1,4^6,(-2)^{20}\}\). Hence the largest Laplacian eigenvalue is \(18\). Orthogonally decomposing a subset indicator into its constant and mean-zero components yields
\[
c(S)\leq\frac{18}{27}k(27-k)=\frac23 k(27-k).
\]
The cut is even because \(c(S)=16k-2|E(G[S])|\), so
\[
c(S)\leq2\left\lfloor\frac{k(27-k)}3\right\rfloor.
\]
To attain equality, partition the vertices into the following nine independent triples, in the index labeling above:
\[
\begin{gathered}
(0,6,22),(1,11,23),(3,8,21),\\
(4,18,24),(5,20,25),(2,17,26),\\
(7,13,19),(9,14,15),(10,12,16).
\end{gathered}
\]
Direct substitution in the intersection rules shows that every vertex in one triple has exactly two neighbors in each different triple and no neighbor in its own triple. For \(k=3m+r\), \(0\leq r\leq2\), choose \(m\) entire triples and \(r\) arbitrary vertices from a further triple. The induced edge count is \(3m(m-1)+2mr\), and the cut size is
\[
16(3m+r)-2[3m(m-1)+2mr]
=2\left\lfloor\frac{k(27-k)}3\right\rfloor.
\]
This proves the upper bound is attained for every \(k\), including the endpoints \(k=0,27\).

**3. Ground-energy lower envelope.** The consecutive differences \(C(k)-C(k-1)\), as \(k\) increases, are \(16,12,8,4,0,-4,-8,-12,-16\), each repeated three times. For \(t>0\), maximizing \(C(k)-tk\) therefore selects \(k=12,9,6,3,0\) over the five successive open intervals separated by \(t=4,8,12,16\). At a boundary, the four consecutive values of \(k\) across the relevant group of three tied differences all minimize energy. At \(t=0\), \(k=12,13,14,15\) all have cut size \(120\). Substitution into the energy formula yields the five affine pieces above and magnetizations \(27-2k\).

**4. Exact degeneracies.** The following independently reproducible exhaustive finite census counts subsets achieving \(C(k)\). Both algorithms construct the graph from the explicit line-intersection rules, visit every one of the \(2^{27}=134,217,728\) subsets, and return the same tuple \((k,C(k),N_k)\).

| Down spins \(k\) | \(C(k)\) | \(N_k\) |
| ---: | ---: | ---: |
| 0 | 0 | 1 |
| 1 | 16 | 27 |
| 2 | 32 | 135 |
| 3 | 48 | 45 |
| 4 | 60 | 2,160 |
| 5 | 72 | 6,750 |
| 6 | 84 | 1,080 |
| 7 | 92 | 42,120 |
| 8 | 100 | 86,400 |
| 9 | 108 | 8,400 |
| 10 | 112 | 247,860 |
| 11 | 116 | 351,216 |
| 12 | 120 | 22,968 |
| 13 | 120 | 495,720 |

For \(14\leq k\leq27\), spin reversal gives \(N_k=N_{27-k}\) and \(C(k)=C(27-k)\). At a noncritical positive field, \(N_k\) is the stated multiplicity. At a transition field, sum the four relevant consecutive counts: \(N_9+N_{10}+N_{11}+N_{12}=630,444\); \(N_6+\cdots+N_9=138,000\); \(N_3+\cdots+N_6=10,035\); \(N_0+\cdots+N_3=208\). At zero field, \(N_{12}+N_{13}+N_{14}+N_{15}=1,037,376\).

For rigor of the *finite* enumeration, the subset-DP implementation stores \(e(S)=|E(G[S])|\) and uses the exact induction
\[
e(S)=e(S\setminus\{v\})+|N(v)\cap(S\setminus\{v\})|,
\]
where \(v\) is the least indexed member of \(S\). Because every nonempty mask has a strictly smaller predecessor, the recurrence exhausts all masks from zero to \(2^{27}-1\). The independent Gray-code enumeration toggles the lowest changed bit and updates the cut by the degree-minus-twice-neighbor-count identity; the Gray sequence is a bijection on all masks. Neither routine samples or extrapolates. Both produce the same entire \(28\)-row count profile. Consequently the finite multiplicity claims follow from exhaustive exact integer calculations; the structural cut-profile and phase-boundary arguments do not depend on exhaustive calculations.

## Verification

The included `verify.py`, `verify_gray.cpp`, and `verify_dp.cpp` are standalone. With Python 3 and a C++17 compiler, run `python verify.py` in the containing folder. The script confirms graph degrees/common-neighbor parameters, all nine independent triples and their inter-triple counts, the analytical cut upper bound and matching constructions for every size, all \(28\) exact maximum-cut multiplicities by two exhaustive algorithms, and the five transition degeneracies. Both C++ enumerators were run from their actual packaged source files and agreed exactly. The checker's final output is `VERIFIED: 134217728 spin states; both exhaustive methods agree; all analytical profile/degeneracies verified.`

## Relationship to prior work

The Schläfli graph's parameters, spectrum, complement-of-generalized-quadrangle interpretation, \(45\) maximal three-cocliques, and proper nine-colorings are documented in A. E. Brouwer's graph description. Those results suffice to motivate (and, with the elementary spectral bound, derive) the size-constrained cut maxima; this known graph structure is **not** presented as an independently novel invariant. The additional exact ground-state multiplicities at nonzero fields and at each of the four transition fields are the newly investigated invariant.

Honecker, Schulenburg, and Richter (first public arXiv version 18 September 2003) investigate magnetization plateaux on frustrated quantum spin lattices. Schmidt, Richter, and Schnack (17 January 2005) investigate quantum antiferromagnets on magnetic polyhedra. Neither examined full text treats the classical Schläfli-graph Ising model or supplies its field-resolved degeneracy census. Metcalf and Yang (1978) study critical-field degeneracy on square and triangular Ising lattices, not this finite graph; only abstract-level material was accessible for this comparison. A separate literature/database search for the exact cardinality-constrained cut counts and field-transition multiplicities found no directly covering result. Search non-detection is not proof of historical novelty.

## Limitations

All results concern the finite, uniformly coupled, classical \(27\)-spin model at strictly zero temperature and real \(h\). No finite-temperature partition-function formula, infinite-volume phase transition, quantum spin dynamics, or perturbation stability claim is made. Ground-state counts are exact for the specified graph and spin convention; they are not graph-isomorphism orbits. The structural cut profile follows quickly from previously known graph data, while historical originality of the *specific degeneracy census* remains subject to independent checking against unindexed graph-cut tables and specialized physics literature.

## References

- A. E. Brouwer, *Schläfli graph*, graph description, https://aeb.win.tue.nl/drg/graphs/Schlaefli.html (known parameters, coloring and cocliques).
- A. Honecker, J. Schulenburg, J. Richter, *Magnetization plateaus in frustrated antiferromagnetic quantum spin models*, arXiv:cond-mat/0309425, first submitted 2003-09-18, https://arxiv.org/html/cond-mat/0309425v2.
- R. Schmidt, J. Richter, J. Schnack, *Frustration effects in magnetic molecules*, arXiv:cond-mat/0501376, first submitted 2005-01-17, https://arxiv.org/abs/cond-mat/0501376.
- B. D. Metcalf, C. P. Yang, *Degeneracy of antiferromagnetic Ising lattices at critical magnetic field and zero temperature*, Phys. Rev. B 18 (1978) 2304, https://doi.org/10.1103/PhysRevB.18.2304.
