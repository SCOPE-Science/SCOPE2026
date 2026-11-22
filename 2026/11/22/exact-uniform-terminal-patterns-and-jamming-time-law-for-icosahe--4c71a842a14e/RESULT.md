# Exact uniform terminal patterns and jamming-time law for icosahedral face trimers

## Finding

On the twelve vertices of a regular icosahedron, allow a trimer to occupy exactly the three vertices of any one of its twenty triangular faces. Each face independently attempts deposition at rate one; a proposed trimer is accepted exactly when all its vertices are vacant, and accepted trimers never desorb. Let \(K\) denote the terminal number of trimers and let \(T\) be the time of the last successful adsorption.

The complete terminal size law is
\[
\Pr(K=2)=\frac1{10},\qquad \Pr(K=3)=\frac35,\qquad \Pr(K=4)=\frac3{10}.
\]
No other terminal sizes occur. There are exactly 10 terminal occupied-site patterns with 6 occupied sites, 60 with 9 occupied sites, and one with 12 occupied sites. Every one of the 70 non-full terminal occupied-site patterns has probability exactly \(1/100\); the fully occupied pattern has probability \(3/10\). Each of the three terminal classes is one orbit of the full icosahedral symmetry group. The six remaining vacant sites in the first class induce a six-cycle; the three remaining vacant sites in the second class have pairwise graph distances \(1,2,3\), respectively. Hence the mean terminal coverage fraction is \(4/5\).

For \(s\ge0\), the exact jamming-time Laplace transform is
\[
\mathbb E[e^{-sT}]=\frac{20}{20+s}\frac{10}{10+s}\left[\frac1{10}+\frac3{10}\frac4{4+s}+\frac3{10}\frac2{2+s}+\frac3{10}\frac4{4+s}\frac1{1+s}\right].
\]
Consequently, \(\mathbb E[T]=3/4\) and \(\operatorname{Var}(T)=251/400\) in the unit face-attempt time normalization.

## Assumptions and scope

The surface is the abstract simplicial boundary of the regular icosahedron, not a planar triangular lattice or a continuously positioned trimer model. The twelve sites are distinct and all twenty faces have identical, independent, rate-one Poisson arrival processes for their proposed rigid three-site adsorbates. A rejected attempt changes nothing; a successful one permanently occupies three vertices. Later attempts on occupied or overlapping faces have no effect. The process begins empty at time zero. Time \(T\) is the last **successful** attempt, not the last proposal among the infinitely continuing Poisson streams.

The following labelled realization fixes the geometry and makes all finite calculations reproducible. Put a north vertex \(0\), an upper ring \(U_i=1+(i\bmod5)\), a lower ring \(L_i=6+(i\bmod5)\), and a south vertex \(11\). For each \(i=0,\ldots,4\), take the four faces
\[
\{0,U_i,U_{i+1}\},\quad
\{11,L_i,L_{i+1}\},\quad
\{U_i,U_{i+1},L_i\},\quad
\{U_i,L_{i-1},L_i\}.
\]
Each of the thirty induced edges belongs to exactly two of these twenty faces; every site has graph degree five. Cyclic subscripts are interpreted modulo five. This is an explicit labelled icosahedral triangulation, independent of coordinates or software libraries.

## Proof

For an occupied-site subset \(S\), let \(a(S)\) be the number of faces disjoint from \(S\). Conditional on the next successful adsorption existing, it chooses uniformly among those \(a(S)\) faces; the waiting time is an independent exponential random variable of rate \(a(S)\). This follows by superposition and memorylessness of independent rate-one Poisson proposal streams. Therefore all terminal probabilities follow from a finite, exact recurrence on occupied masks; no continuum or asymptotic approximation enters.

The icosahedral automorphism group is transitive on the twenty faces. Fix the first accepted face as \(\{0,1,2\}\). Exactly ten faces avoid it. Among those ten choices for the second face, the number of subsequently admissible faces is four for six choices, two for three choices, and zero for one choice. In the four-admissible branch, exactly two of the four third-face choices leave one final admissible face and two leave none; in the two-admissible branch, both third-face choices leave none. All these claims are checked directly from the four face families above: the ten second faces and their residual counts are:

| Second face | Admissible faces after second |
|---|---:|
| \(\{3,4,8\}\), \(\{3,7,8\}\), \(\{4,5,9\}\), \(\{5,9,10\}\), \(\{6,7,11\}\), \(\{6,10,11\}\) | 4 each |
| \(\{4,8,9\}\), \(\{7,8,11\}\), \(\{9,10,11\}\) | 2 each |
| \(\{8,9,11\}\) | 0 |

It follows that two trimers are terminal with probability \(1/10\). Three trimers are terminal either after the two-admissible branch, probability \(3/10\), or after half of the four-admissible branch, probability \(3/10\). The remaining probability \(3/10\) yields four trimers and full occupancy. The expected number of trimers is \(16/5\), hence twelve-site coverage \(3(16/5)/12=4/5\).

For the finer terminal-law assertion, apply the same finite-face recurrence to vertex masks. Its complete reachable mask set contains 202 masks: 1 empty, 20 after one trimer, 100 after two, 80 after three, and 1 full. Exactly 71 are terminal, falling into 10 six-site, 60 nine-site and 1 twelve-site masks. Propagating the images of any ordered triangular face across adjacent pairs of faces enumerates the 120 full icosahedral graph automorphisms. Their action has exactly one orbit on each terminal mask size, of sizes 10, 60 and 1. These finite counts can be independently obtained from the fully explicit face table using `verify.py`; its two exact-rational enumeration methods agree on each of the 71 terminal mask probabilities. Symmetry and the already proved size probabilities then give \(\frac{1/10}{10}=1/100\) and \(\frac{3/5}{60}=1/100\). Inspecting a representative mask of each orbit yields the asserted six-cycle and three-distance vacancy geometries.

Let \(E_a\) denote an independent exponential waiting time of rate \(a\). Every history begins with \(E_{20}+E_{10}\). The remaining independent waiting time has four alternatives: zero with probability \(1/10\), \(E_4\) with probability \(3/10\), \(E_2\) with probability \(3/10\), and \(E_4+E_1\) with probability \(3/10\). Taking Laplace transforms gives the displayed formula. Summing the corresponding first and second moments proves \(\mathbb E[T]=3/4\) and \(\operatorname{Var}(T)=251/400\).

## Verification

Run `python3 verify.py` from this package. The script requires only the Python standard library and reconstructs the twenty faces from the two pentagonal rings. It uses both (1) a memoized backward recurrence on occupied twelve-bit masks and (2) a direct enumeration of ordered accepted-face sequences with exact rational path weights. It tests all ten second-face cases for every first face; reconstructs all 120 automorphisms from oriented faces; verifies 202 reachable masks and 71 terminal masks; checks the complete terminal probability mass function; and compares the proposed Laplace transform to the direct path mixture at six exact rational transform arguments. It also checks exact time moments. Its successful execution is a finite exhaustive certificate for the stated fixed geometric substrate, not an extrapolation to other triangulations.

## Relationship to prior work

Random sequential adsorption is a standard stochastic deposition model. Cieśla and Barbasz study trimer and hexamer adsorption numerically on a **continuous flat two-dimensional substrate** (first arXiv version 26 September 2013, `arxiv:1309.7021`). Their object placement space, terminal statistics, and time normalization differ from this fixed twenty-face, twelve-site substrate. Penrose and Sudbury (`arxiv:math/0503519`, first public 24 March 2005) analyze **monomer and dimer** deposition on graphs and explicitly describe the random ordering/exponential-clock construction, but do not treat the icosahedral face-trimer model. Budinski-Petković and Kozmidis-Luburić (`doi:10.1103/PhysRevE.56.6904`, 1997) simulate deposition of shapes on an **extended planar triangular lattice**, not the discrete surface of an icosahedron. Their accessible abstract is not treated as a complete-paper exclusion check.

Exact absorbing-state counting on a face hypergraph is algorithmically elementary in principle, but the explicit, symmetry-uniform 71-pattern distribution and time law for this canonical spherical triangulation are distinct concrete quantities. No claim is made that the finite Markov-chain recurrence itself is new or that a failed bibliographic search proves historical priority.

## Limitations

The result is finite and substrate-specific; it gives no thermodynamic limit, generalized Platonic-solid theorem, time-dependent occupancy correlations, or universality across trimer shapes. Face attempts must have equal rates. The time law is for Poisson clocks and cannot be inferred solely from the terminal ordering law under arbitrary nonexponential arrivals. The work has received no independent scientific audit. Equivalent earlier tabulations in unindexed material remain a residual priority risk.

## References

1. M. Cieśla and J. Barbasz, *Random sequential adsorption of trimers and hexamers*, arXiv:1309.7021 (first public 2013-09-26); https://arxiv.org/abs/1309.7021 ; Journal of Molecular Modeling 19 (2013), 5423–5427, https://doi.org/10.1007/s00894-013-2031-5 .
2. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519 (first public 2005-03-24), https://arxiv.org/pdf/math/0503519 ; Annals of Applied Probability 15 (2005), 853–889.
3. Lj. Budinski-Petković and U. Kozmidis-Luburić, *Random sequential adsorption on a triangular lattice*, Physical Review E 56 (1997), 6904, https://doi.org/10.1103/PhysRevE.56.6904 .
