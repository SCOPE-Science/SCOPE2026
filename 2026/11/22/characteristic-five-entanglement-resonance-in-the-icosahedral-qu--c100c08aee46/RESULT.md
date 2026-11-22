# Characteristic-five entanglement resonance in the icosahedral qudit graph state

## Finding

Put a prime-dimensional qudit at each of the twelve vertices of the ordinary icosahedral graph, and prepare its pure, unit-weight controlled-phase graph state. For any vertex subset \(A\), write \(k=\min\{|A|,12-|A|\}\) and let \(M_A\) be the binary-integer adjacency block between \(A\) and its complement, with its smaller side as rows. Its reduction over \(\mathbb F_p\) has rank \(r_p(A)\). **The complete nonzero Schmidt spectrum is flat:** there are exactly \(p^{r_p(A)}\) eigenvalues, each \(p^{-r_p(A)}\), and the base-\(p\) entropy is exactly \(r_p(A)\).

The following are the complete numbers of **labelled** subsets on the smaller side with the indicated entropy, for every prime \(p\). For \(k=6\) each of the \(924\) subsets is counted; complementary six-sets are distinct labelled subsets but define the same unordered bipartition.

| Smaller-side size | Prime characteristic | Entropy histogram (base-\(p\) units: count) |
|---|---|---|
| \(0\) | every \(p\) | \(0:1\) |
| \(1\) | every \(p\) | \(1:12\) |
| \(2\) | every \(p\) | \(2:66\) |
| \(3\) | every \(p\) | \(3:220\) |
| \(4\) | every \(p\) | \(3:15,\ 4:480\) |
| \(5\) | every \(p\) | \(4:120,\ 5:672\) |
| \(6\) | \(p=2\) | \(4:172,\ 5:240,\ 6:512\) |
| \(6\) | \(p=5\) | \(4:140,\ 5:264,\ 6:520\) |
| \(6\) | \(p\ne2,5\) | \(4:140,\ 5:252,\ 6:532\) |

More precisely, the **complete integer Smith-diagonal distribution** of the cross-cut adjacency block has these types and multiplicities:

| \(k\) | Smith diagonal (omitting no zero entries) | Number of subsets |
|---|---|---:|
| \(0\) | empty | 1 |
| \(1\) | \((1)\) | 12 |
| \(2\) | \((1,1)\) | 66 |
| \(3\) | \((1,1,1)\) | 220 |
| \(4\) | \((1,1,1,0)\); \((1,1,1,1)\) | 15; 480 |
| \(5\) | \((1,1,1,1,0)\); \((1,1,1,1,1)\) | 120; 672 |
| \(6\) | \((1,1,1,1,0,0)\) | 140 |
| \(6\) | \((1,1,1,1,1,0)\) | 240 |
| \(6\) | \((1,1,1,1,1,1)\) | 500 |
| \(6\) | \((1,1,1,1,1,5)\) | 12 |
| \(6\) | \((1,1,1,1,2,0)\) | 12 |
| \(6\) | \((1,1,1,1,2,2)\) | 20 |

In particular, characteristic five destroys exactly one rank unit in **twelve** formerly full-rank balanced cuts. They are precisely the sets \(N(v)\cup\{\bar v\}\), where \(N(v)\) is the five-vertex neighbor pentagon of a vertex \(v\) and \(\bar v\) is its unique antipode, at graph distance three. Their characteristic-five entanglement is \(5\) rather than \(6\) base-\(p\) units. Characteristic two has a distinct defect distribution; no other prime is exceptional. The standard qubit rank-index classification is earlier work, not claimed as novel here; the assessed contribution is the full integral Smith distribution and its characteristic-five qudit consequence.

## Assumptions and scope

The graph has twelve vertices and thirty unit-weight undirected edges. A concrete combinatorial labeling is the north pole \(0\), south pole \(11\), upper pentagon \(a_i=1+i\), and lower pentagon \(b_i=6+i\), with \(i\in\mathbb Z/5\). Its edges are \(0a_i\), \(11b_i\), \(a_i a_{i+1}\), \(b_i b_{i+1}\), \(a_i b_i\), and \(a_i b_{i-1}\). This is the five-regular icosahedral skeleton.

For prime \(p\), each vertex carries \(\mathbb C^p\), with \(\lvert+\rangle=p^{-1/2}\sum_{j\in\mathbb F_p}\lvert j\rangle\). Each graph edge applies \(CZ_p\lvert a,b\rangle=\omega^{ab}\lvert a,b\rangle\), where \(\omega=\exp(2\pi i/p)\). The state is pure and has no other edges, local potentials, noise or nonuniform interaction phases. Entropies in this statement use logarithm base \(p\); measured in bits they must be multiplied by \(\log_2p\). The finite-field ranks of a cut are unchanged on exchanging its two sides.

## Proof

**1. Exact Schmidt spectrum for any prime.** For a cut with smaller side of size \(k\), gates whose endpoints are both on one side are local unitaries and do not alter entanglement. After removing those gates, the normalized state coefficient matrix is \(\Psi_{x,y}=p^{-6}\omega^{x^{\mathsf T}M_Ay}\), for \(x\in\mathbb F_p^k\), \(y\in\mathbb F_p^{12-k}\). Orthogonality of additive characters gives
\[
(\rho_A)_{x,x'}=p^{-k}\mathbf1_{\{M_A^{\mathsf T}(x-x')=0\}}.
\]
There are \(p^{r_p(A)}\) cosets of the kernel of \(M_A^{\mathsf T}\). Each coset contributes one eigenvalue \(p^{-r_p(A)}\) and the remaining eigenvalues vanish. This proves the flat-spectrum and entropy statements exactly, with no numerical quantum-state approximation.

**2. Complete integer classification, not a sample.** For every integer \(0\le k\le6\), enumerate all \(\binom{12}{k}\) subsets of the explicitly specified graph. Construct its integer \(k\)-by-\((12-k)\) cross-cut matrix. If \(\Delta_j\) denotes the greatest common divisor of the determinants of **all** \(j\)-by-\(j\) minors, set \(\Delta_0=1\) and take each nonzero Smith invariant \(d_j=\Delta_j/\Delta_{j-1}\), with trailing zeros. When \(\Delta_j=1\), all earlier \(\Delta_i\) equal one, justifying the verifier's shortcut. The separate standard-library program `verify_smith.py` executes this deterministic procedure for all \(2510\) subsets of sizes at most six, using exact Bareiss integer determinants. It computes the stated Smith table and checks every row sum against the appropriate binomial coefficient. The graph is built independently from the twelve exact golden-ratio coordinates, with adjacency determined by squared Euclidean distance \(4\), using the integral identity \(\varphi^2=\varphi+1\), so the two graph constructions are independent. Every integer minor and its gcd are computed exactly; there is no statistical sampling, floating-point determinant, or untested finite-size extrapolation.

**3. From Smith forms to all prime characteristics.** A Smith diagonal is produced by unimodular integer row and column transformations. Those remain invertible over every prime field, so the rank modulo \(p\) is exactly the number of diagonal entries not divisible by \(p\). In the completed integer table the only nonunit diagonal entries are \(2\) and \(5\), giving exactly the three stated cases. The separate `verify_modular.py` computes the cut matrix directly from the pole-and-pentagon graph and checks modular Gaussian-elimination ranks for all subsets and every prime at most \(216\), as well as prime \(223\). This is logically independent of the Smith computations. Independently of that table, Hadamard's inequality bounds every nonzero \(j\)-by-\(j\) minor of a zero-one cut matrix by \(j^{j/2}\le216\) for \(j\le6\). Hence no prime greater than \(216\) can divide a nonzero minor, so all such primes have the same rank as the rational matrix. Together these checks prove the rank histogram for **every** prime; the Smith computation also gives the stronger integral classification.

**4. Geometry of the exceptional five-primary cuts.** In the icosahedron each vertex has five neighbors arranged in a pentagonal cycle, and one vertex at distance three. For each of the twelve vertices, the six-set \(N(v)\cup\{\bar v\}\) is distinct. The independently constructed rank verifier checks that each has rank six over characteristic seven and rank five over characteristic five. The Smith computation establishes that precisely twelve balanced subsets have diagonal \((1,1,1,1,1,5)\). Thus these and only these twelve sets produce the five-primary loss, giving a geometric characterization rather than merely an arithmetic count.

## Verification

The package contains `verify_modular.py` and `verify_smith.py`, executable by `python3 verify_modular.py` and `python3 verify_smith.py`, requiring only the Python standard library. Both were executed successfully after construction. The first verifies the complete prime-rank histograms and independently identifies the twelve exceptional pentagonal cuts. The second computes complete integral Smith invariant factors by determinants of all relevant minors on an independently generated graph. The exact computations reproduce every entry of the two tables. The programs are transparent exhaustive certificates for a fixed twelve-vertex object; the field-rank and character-orthogonality arguments above establish the statement for arbitrary prime dimension.

## Relationship to prior work

Hein, Eisert and Briegel [1] established the general graph-state cut-rank correspondence in the qubit setting; the character-orthogonality reduction here is an elementary prime-dimensional version, not itself claimed as new. Looi, Yu, Gheorghiu and Griffiths [2] provide the prime-dimensional qudit controlled-phase graph-state framework. Cabello, Danielsen, López-Tarrida and Portillo [3], together with the public twelve-qubit graph-state database [4], classify binary rank indices for graphs through twelve vertices. Consequently the \(p=2\) row and the binary part of the census may already be recovered from that earlier classification; these are presented for completeness, not as independently novel. Their records do not, by themselves, supply an integral Smith histogram or characteristic-five qudit entanglement.

Published investigations of generalized Petersen qudit graph states [5] evaluate alternating cuts by cyclic-polynomial gcds, while work on line-graph qudit states [6] uses signed component overlaps. Neither has an icosahedral graph-state cut as a specialization: the icosahedron's vertex neighborhood is an induced five-cycle, whereas a line graph of a simple graph has each vertex neighborhood coverable by at most two cliques. Those results do not imply the displayed icosahedral integer Smith distribution. The geometric characteristic-five exception is thus the specific contribution assessed here. An equivalent result in specialized finite-graph Smith tables or unindexed qudit literature remains possible and is not ruled out by unsuccessful searches.

## Limitations

The claims apply only to the simple twelve-vertex icosahedral graph, its unit-weight pure prime-dimensional qudit graph state, and its vertex bipartitions. The identified characteristic-five resonance does not establish a corresponding statement for other Platonic graphs, arbitrary edge weights, composite local dimensions, noisy circuits, multipartite entanglement measures, or protocols for enhanced quantum performance. The values at \(p=2\) overlap earlier twelve-qubit rank-index work. Historical priority of the integral and qudit-specific evaluation is provisional, and independent mathematical assessment has not been performed.

## References

[1] M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first submitted 2003-07-18), https://arxiv.org/abs/quant-ph/0307130.

[2] S. Y. Looi, L. Yu, V. Gheorghiu, R. B. Griffiths, *Quantum Error Correcting Codes Using Qudit Graph States*, arXiv:0712.1979 (first submitted 2007-12-12), https://arxiv.org/abs/0712.1979.

[3] A. Cabello, L. E. Danielsen, A. J. López-Tarrida, J. R. Portillo, *Optimal preparation of graph states*, arXiv:1011.5464 (first submitted 2010-11-24), https://arxiv.org/abs/1011.5464.

[4] L. E. Danielsen and collaborators, *Database of Entanglement in Graph States*, twelve-qubit rank-index and equivalence-class tables (site last modified 2011-01-12), https://www.codetables.de/larsed/entanglement/.

[5] *Cyclotomic entanglement resonances in generalized Petersen qudit graph states*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclotomic-entanglement-resonances-in-generalized-petersen-qudit--2bc8f85cb693.

[6] *Prime-characteristic entanglement of line-graph qudit states from signed component overlaps*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-prime-characteristic-entanglement-of-line-graph-qudit-states-fro--d25a6aa6f8d4.
