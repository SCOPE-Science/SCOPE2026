# Complete arithmetic entanglement census for the Möbius–Kantor graph state

## Finding

Let \(G\) be the Möbius–Kantor graph \(\mathrm{GP}(8,3)\), with sixteen vertices and twenty-four edges. For each prime \(p\), prepare the pure unit-weight \(p\)-level graph state by applying one generalized controlled-phase gate along each edge to the uniform product state. There are exactly \(\binom{16}{8}/2=6435\) unordered balanced bipartitions \(A\mid A^c\), where both sides contain eight vertices. Every cut has a flat nonzero Schmidt spectrum, with \(p^r\) equal nonzero eigenvalues of the reduced density operator, each \(p^{-r}\). The exponent \(r\) is the rank over \(\mathbb F_p\) of the eight-by-eight adjacency block across the cut.

**Complete integral classification.** Across the 6435 cuts, the integer cross-adjacency matrices have exactly the fifteen Smith-normal-form classes in the following table. Each class is specified by its rank over \(\mathbb Q\) and its ordered nonunit nonzero invariant factors; all other nonzero factors equal one, and the remaining diagonal entries are zero. Thus the table determines the entanglement at *every* prime without finite-field extrapolation.

| Rank over \(\mathbb Q\) | Nonunit Smith factors | Cuts |
|---:|:---|---:|
| 7 | none | 2232 |
| 6 | none | 1491 |
| 8 | none | 999 |
| 8 | \((2)\) | 432 |
| 7 | \((3)\) | 328 |
| 7 | \((2)\) | 312 |
| 8 | \((3)\) | 300 |
| 5 | none | 124 |
| 6 | \((3)\) | 48 |
| 8 | \((2,2)\) | 48 |
| 8 | \((6)\) | 48 |
| 8 | \((3,3)\) | 32 |
| 8 | \((2,4)\) | 24 |
| 7 | \((3,3)\) | 16 |
| 8 | \((3,3,3)\) | 1 |
| **Total** | **15 classes** | **6435** |

Consequently the exact frequency distributions of \(r\) are:

| Rank \(r\) | \(p=2\) | \(p=3\) | Every prime \(p\ge5\) |
|---:|---:|---:|---:|
| 5 | 124 | 189 | 124 |
| 6 | 1923 | 1851 | 1539 |
| 7 | 3056 | 2892 | 2888 |
| 8 | 1332 | 1503 | 1884 |
| **Total** | **6435** | **6435** | **6435** |

In particular there is **exactly one** unordered balanced cut for which the characteristic-three Schmidt exponent falls by **three** relative to all primes \(p\ge5\); all other cuts have a drop of at most two. This exceptional cut is the canonical point-versus-block bipartition of the Möbius–Kantor \((8_3)\) incidence configuration. Its eight-by-eight incidence matrix has Smith invariants
\[
(1,1,1,1,1,3,3,3).
\]
It therefore has Schmidt exponent eight for qubits and every prime \(p\ge5\), but exponent five for qutrits. The exact entropy of a cut is \(r\log_2 p\) bits, and this value also gives every positive-order Rényi entropy.

## Assumptions and scope

Use sixteen labeled vertices \(u_i,v_i\), with \(i\in\mathbb Z/8\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). This defines \(\mathrm{GP}(8,3)\); edge weights are all one. The local dimension \(p\) is prime and the full graph-state vector is pure. Each edge applies \(\mathrm{CZ}_p|a,b\rangle=\exp(2\pi iab/p)|a,b\rangle\), with \(a,b\in\mathbb F_p\). A cut is unordered: \(A\mid A^c\) and \(A^c\mid A\) are the same cut. Throughout, matrix ranks over \(\mathbb Q\) are distinguished from ranks over \(\mathbb F_p\). No statement about mixed states, noisy gates or arbitrary weighted graphs is asserted.

## Proof

**1. The quantum entropy reduction.** Fix any balanced cut and write \(C\) for its cross-adjacency block. Edges wholly within either side apply local diagonal unitaries, which do not affect the Schmidt spectrum. After removing these phases, computational-basis coefficients are proportional to \(\omega^{a^{\mathsf T}Cb}\), where \(\omega=\exp(2\pi i/p)\) and \(a,b\in\mathbb F_p^8\). Character orthogonality gives
\[
\rho_A(a,a')=p^{-8}\mathbf1_{\{C^{\mathsf T}(a-a')=0\}}.
\]
The kernel of \(C^{\mathsf T}\) has \(p^{8-r}\) elements and yields \(p^r\) equal-size cosets; on each coset \(\rho_A\) is a rank-one constant matrix whose unique positive eigenvalue is \(p^{-r}\). This proves the complete spectrum and all entropy formulas without approximation.

**2. Exact finite exhaustive certificate.** Label \(u_0,\ldots,u_7\) by \(0,\ldots,7\) and \(v_0,\ldots,v_7\) by \(8,\ldots,15\). Every unordered balanced cut has exactly one representative containing vertex zero. The program `verification/smith_census.py` iterates over *every* seven-element subset of the other fifteen vertices, constructs the cross block from the twenty-four edges, and computes its integer Smith normal form. It explicitly checks the fifteen-class frequency table and that the class containing three invariant factors equal to three occurs once. The loop length is \(\binom{15}{7}=6435\), equal to the total number of unordered cuts. This is an exhaustive finite proof of the table, not a sample.

**3. Independent incidence-model certificate.** Equivalently, construct eight points \(P_j\) and eight blocks \(L_j=\{P_j,P_{j+1},P_{j+3}\}\), indices modulo eight. Their Levi graph is isomorphic to \(\mathrm{GP}(8,3)\). The standalone program `verification/modular_census.py` constructs these incidence edges directly, checks an explicit sixteen-vertex isomorphism, enumerates the \(6435\) complementary pairs independently and performs elementary finite-field elimination for primes two, three, five and seven. It independently reproduces all four rank histograms and verifies that the only three-unit qutrit deficit occurs for the point-versus-block cut. Thus the integral classification and its modular consequences have differently constructed computational witnesses.

**4. All-prime and geometric conclusions.** For an integer matrix with nonzero Smith factors \(d_1,\ldots,d_s\), its rank modulo a prime \(p\) is the number of factors not divisible by \(p\). The first table shows that every nonunit factor is among \(2,3,4,6\); hence no prime above three can alter its rational rank. Only the unique class \((3,3,3)\) loses three ranks modulo three. For the incidence cut, the eight-by-eight point-block matrix with entries \(C_{i,j}=1\) exactly when \(i-j\equiv0,1,3\pmod8\) has integral Smith factors \((1,1,1,1,1,3,3,3)\), confirming the geometric interpretation and the all-prime jump. This completes the claim.

## Verification

From the directory containing this document, run `python verification/smith_census.py` with `sympy` installed; it prints fifteen nonnegative integer multiplicities and ends with `PASS: 6435 balanced cuts, 15 integral classes; unique three-factor cut`. Run `python verification/modular_census.py` with Python 3.9 or later and no additional packages; it prints the complete rank tables for the four tested primes and ends with `PASS: independent 6435-cut modular census; unique point/line qutrit triple drop`. Both programs ran successfully from their own package paths. The Smith normal form, rather than the finite list of tested primes, proves the statement for every prime.

## Relationship to prior work

Hein, Eisert and Briegel [1] establish the foundational bipartite adjacency-rank rule for qubit graph states, and Looi, Yu, Gheorghiu and Griffiths [2] generalize graph-state constructions to qudits. Chen and Zhou [3] study finite-field qudit graph states and entanglement, without a balanced-cut census on this sixteen-vertex incidence graph. A publicly accessible mathematical finding, *Cyclotomic entanglement resonances in generalized Petersen qudit graph states* [4], already derives prime-dependent entanglement for **one specified alternating-layer cut** of every generalized Petersen graph; in particular its formula applies to the special point-versus-block cut considered here. The special-cut rank formula is therefore not presented as independently novel. The new assertion assessed here is the **exhaustive fifteen-class integral distribution of all balanced cuts**, including uniqueness of that triple-defect cut among the other \(6434\) cuts. The general prime-characteristic line-graph construction [5] does not cover this cubic girth-six graph, which is not a line graph. The established balanced-cut Heawood incidence-graph classification concerns a different graph and does not imply these sixteen-vertex counts. Neither matching formalism nor general cyclic-cut results alone supply the full histogram in the theorem.

## Limitations

This is a complete finite classification for exactly the Möbius–Kantor graph, not an all-size theorem for generalized Petersen graphs. The enumeration and exact integer Smith computation are part of the proof and are independently reproducible; they are not a closed-form symbolic derivation of the entire fifteen-class table. The entanglement is for pure prime-dimensional, unweighted graph states. Composite qudit dimensions require an analysis over rings and are not claimed. General experimental advantages, robustness and noise thresholds are not inferred. A historically unindexed equivalent table cannot be excluded by the documented searches; independent scientific validation has not been performed.

## References

[1] M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first submitted 2003-07-18), https://arxiv.org/abs/quant-ph/0307130; HTML at https://arxiv.org/html/quant-ph/0307130v7.

[2] S. Y. Looi, L. Yu, V. Gheorghiu and R. B. Griffiths, *Quantum Error Correcting Codes Using Qudit Graph States*, arXiv:0712.1979 (first submitted 2007-12-12), https://arxiv.org/abs/0712.1979.

[3] L. Chen and D. L. Zhou, *Graph states of prime-power dimension from generalized CNOT quantum circuit*, arXiv:1507.05386 (first submitted 2015-07-20), https://arxiv.org/abs/1507.05386.

[4] *Cyclotomic entanglement resonances in generalized Petersen qudit graph states* (2026), public full statement at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclotomic-entanglement-resonances-in-generalized-petersen-qudit--2bc8f85cb693.

[5] *Prime-characteristic entanglement of line-graph qudit states from signed component overlaps* (2026), public full statement at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-prime-characteristic-entanglement-of-line-graph-qudit-states-fro--d25a6aa6f8d4.
