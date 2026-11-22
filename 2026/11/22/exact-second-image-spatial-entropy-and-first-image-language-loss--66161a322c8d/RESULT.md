# Exact second-image spatial entropy and first image-language loss for elementary Rule 22

## Finding

Let \(F\) be the synchronous elementary cellular automaton Rule 22 on the two-sided full binary shift \(\{0,1\}^{\mathbb Z}\), and let \(Y_t=F^t(\{0,1\}^{\mathbb Z})\). Its one- and two-step spatial-image topological entropies satisfy
\[
 h_{\mathrm{top}}(Y_1)=\log\lambda_1,\qquad h_{\mathrm{top}}(Y_2)=\log\lambda_2,
\]
with rigorously certified enclosures
\[
 \frac{191716}{100000}<\lambda_1<\frac{191718}{100000},\qquad
 \frac{186746}{100000}<\lambda_2<\frac{186748}{100000}.
\]
Here \(\lambda_t\) is the Perron root of the explicitly defined finite nonnegative integer matrix \(B_t\) below, of order \(15\) when \(t=1\) and \(273\) when \(t=2\). The matrix is reproduced exactly as a compressed deterministic transition table and a list of its Perron-component states in `CERTIFICATE.json`. Approximate values are
\[
 h_{\mathrm{top}}(Y_1)\approx 0.65084931579,\quad
 h_{\mathrm{top}}(Y_2)\approx 0.62458238165,\quad
 h_{\mathrm{top}}(Y_1)-h_{\mathrm{top}}(Y_2)\approx 0.02626693415.
\]
In particular, the *strict exponential loss* \(h_{\mathrm{top}}(Y_2)<h_{\mathrm{top}}(Y_1)\) is an exact theorem, not an inference from finite word counts. The first loss in the finite image languages is at length seven: every word of length at most six in \(Y_1\) also occurs in \(Y_2\), but precisely the two length-seven words `1010111` and `1110101` are in \(Y_1\) and not in \(Y_2\).

## Assumptions and scope

The alphabet is binary, the spatial lattice is \(\mathbb Z\), both configurations and images are bilateral, and every initial configuration is permitted. The synchronous local rule is
\[
 f(a,b,c)=\begin{cases}1,&a+b+c=1,\\0,&\text{otherwise}.\end{cases}
\]
The coordinate update is \((Fx)_i=f(x_{i-1},x_i,x_{i+1})\), and \(F^t\) denotes \(t\) synchronous iterations, not asynchronous sweeps. The word complexity of the spatial image \(Y_t\) is \(p_t(n)=\#\mathcal L_n(Y_t)\), with spatial entropy \(h_{\mathrm{top}}(Y_t)=\lim_{n\to\infty}n^{-1}\log p_t(n)\). All logarithms are natural. We make no claim about invariant measure entropy of the time-evolution map or the infinite-time limit set.

## Proof

**1. Exact language automata.** Fix \(t\in\{1,2\}\) and write \(w=2t\). The \(t\)-step composed local rule maps a block of length \(w+1\) to one bit; denote that bit \(\phi_t(a_0\ldots a_w)\). Its exact evaluation is performed by \(t\) applications of the given three-bit rule, reducing the block length by two at each application.

Construct a finite nondeterministic labeled graph \(G_t\): its vertices are the \(2^w\) words of length \(w\). For each vertex \(u=a_0\ldots a_{w-1}\) and appended bit \(b\in\{0,1\}\), draw one edge to \(a_1\ldots a_{w-1}b\), labeled \(\phi_t(ub)\). A word \(z\) of length \(n\) belongs to \(\mathcal L_n(Y_t)\) exactly when it labels a path of length \(n\) starting at *some* vertex of \(G_t\): such a path specifies an input word of length \(n+2t\), extendible arbitrarily in both directions to an input in the full shift. Conversely, each image block determines such a path. This is a bijective criterion for admissibility, though not a bijection of paths and words.

Determinize \(G_t\) starting from the subset of all its vertices. A transition on symbol \(b\) takes a subset to the union of the \(b\)-labeled successors of its members; the empty subset is rejecting, and every nonempty subset is accepting. The resulting deterministic automaton accepts *one path per distinct admissible output word*, avoiding predecessor multiplicities. Enumerating its reachable subsets gives 16 states for \(t=1\) and 361 states for \(t=2\), including the dead state. Standard iterative partition refinement by acceptance and both successor classes gives minimal automata with 16 and 281 states, respectively. The finite, explicit transitions, starting states and representatives are in `CERTIFICATE.json`; `rule22_verify.py` independently regenerates all of them from the local truth table and checks every equality.

**2. Spectral reduction and entropy.** From each minimized automaton delete the rejecting dead state and form an adjacency matrix \(M_t\) that counts both labeled successor transitions, with multiplicity if both symbols lead to the same state. Every reachable accepted length-\(n\) word is then counted exactly by the sum of the coordinates of \(e_{s_t}^{\mathsf T}M_t^n\), where \(s_t\) is its start state. Therefore the exponential growth rate of \(p_t(n)\) equals the maximum spectral radius among the accessible strongly connected components of \(M_t\).

The exact SCC computation has one nontrivial Perron component of cardinality 15 for \(t=1\), and one of cardinality 273 for \(t=2\); every other component is a singleton containing at most one internal labeled loop. Thus the corresponding other spectral radii are at most one. Both large components are reachable, are strongly connected and have spectral radius greater than one. Restricting \(M_t\) to the large component gives the irreducible integer matrix \(B_t\). Precisely, list the component vertex IDs in `CERTIFICATE.json` under `core` and, for each such vertex \(v\), put in row \(v\) one unit in column \(u\) for each of the two symbol transitions from \(v\) to \(u\) when \(u\) belongs to the same component. This specifies every matrix entry unambiguously and in a standalone reproducible manner. Perron–Frobenius theory therefore yields \(h_{\mathrm{top}}(Y_t)=\log\rho(B_t)\).

**3. Integer spectral certificates.** Let \(\mathbf1\) be the all-ones vector of the appropriate core dimension, and let \(v_t=B_t^{99}\mathbf1\), a positive integer vector. The exact entries of \(v_t\) appear in `CERTIFICATE.json`, with the canonical row order just specified. Integer arithmetic verifies coordinatewise
\[
 \frac{191716}{100000}v_1<B_1v_1<\frac{191718}{100000}v_1,
\qquad
 \frac{186746}{100000}v_2<B_2v_2<\frac{186748}{100000}v_2.
\]
Here inequalities between vectors are strict in every coordinate; multiplying out denominators is sufficient to check them. Collatz–Wielandt bounds for irreducible nonnegative matrices give the claimed exact enclosures for their spectral radii, hence the entropy formula and strict difference. No floating-point eigenvalue estimate is needed for the proof.

**4. Shortest missing output words.** The same exact deterministic automata accept every one of the \(2^n\) binary output words for \(n\le6\) in both images. At \(n=7\), the one-step automaton accepts all 128 words, while the two-step automaton accepts 126, excluding exactly `1010111` and `1110101`. Because the two-step image is contained in the one-step image, these are precisely the first lost blocks.

## Verification

The standalone `rule22_verify.py` recomputes the finite graphs and validates the complete certificate: 16/361 reachable subsets, 16/281 minimized states, 15/273 leading SCC sizes, all transitions and representatives, all 99-power integer vectors, strict rational Perron inequalities, all word-count entries through length 18, and the two excluded length-seven words. It uses Python's arbitrary-precision integers and the standard library only. Execute `python rule22_verify.py CERTIFICATE.json`.

A separately implemented `rule22_independent.py` directly enumerates all \(2^{n+2t}\) possible input blocks and performs synchronous updates using an independently coded one-count local rule, for both \(t=1,2\) and all \(1\le n\le12\). It checks those counts and image inclusion; execute `python rule22_independent.py`. The respective length-18 accepted word counts are \(p_1(18)=195787\) and \(p_2(18)=160499\); these are cross-checks of exact automata, not substitutes for the infinite-length proof.

## Relationship to prior work

Rule 22's symmetric cubic Boolean description and its exact *single-seed* patterns are treated by Chan-López and Martín-Ruiz (arXiv:2604.00165, first submitted 31 March 2026); that object is different from the spatial image of the full shift. Badii and Politi (1997) give Rule 22's one-step image entropy approximately \(0.6508\) and a hierarchy of *forbidden-language entropies*. Their second-level index \(C^{(2)}\) is **not** the entropy of \(F^2\); their hierarchies apply to a fixed output language, not to synchronous time steps. De Oliveira and collaborators (2015) generate finite-time process graphs, including a Rule 22 graph at time two, but their reported invariant is graph-state complexity rather than the evaluated spatial-image Perron root and its strict first-to-second exponential gap. Martínez and collaborators (2019) survey Rule 22 patterns, basins, de Bruijn and subset diagrams, not this exact two-step all-input spatial growth rate.

Published indexed findings supply the exact first-image entropy spectrum of all elementary rules (published-finding corpus ID `2026/10/27/SCOPE-exact-nineteen-value-spatial-image-entropy-spectrum-of-elementar--d4f1725c3486`) and a uniform short-word witness for unstable two-step images (published-finding corpus ID `2026/10/26/SCOPE-a-sharp-twelve-symbol-threshold-for-second-update-image-loss-in--5742d176c6e4`). The former covers \(h(Y_1)\); the latter implies finite-language loss where applicable but does not by itself determine \(h(Y_2)\). Both are therefore used only as context. The elementary construction of finite-time automata is known; the claimed contribution is this evaluated, exactly certified two-step Rule 22 entropy and quantitative gap, together with its first missing blocks.

## Limitations

The result covers only the first and second synchronous full-shift images of Rule 22, not the limit set, any later iterate, ring-periodic image counts, or temporal Kolmogorov–Sinai entropy. The Perron root is specified by a completely explicit 273-state integer matrix and a strict rational certificate, not by a small minimal polynomial. The reported decimals are approximations; rational inequalities provide the exact assertion. Earlier language-graph constructions or unpublished computations may implicitly contain equivalent numerical values; historical priority requires further human checking. A review of indexed and relevant accessible primary literature found no explicit evaluated second-image constant, but an unsuccessful search is not proof of novelty.

## References

1. E. Chan-López and A. Martín-Ruiz, *Symmetric Nonlinear Cellular Automata as Algebraic References for Rule 30*, arXiv:2604.00165, v1 submitted 2026-03-31. https://arxiv.org/abs/2604.00165
2. R. Badii and A. Politi, *Thermodynamics and Complexity of Cellular Automata*, Physical Review Letters **78** (1997), 444–447. https://doi.org/10.1103/PhysRevLett.78.444
3. P. P. B. de Oliveira et al., *Advances in the Study of Elementary Cellular Automata Regular Language Complexity*, Complexity **21** (2016), 267–279; online 2015-05-06. https://doi.org/10.1002/cplx.21686
4. G. J. Martínez et al., *On Patterns and Dynamics of Rule 22 Cellular Automaton*, Complex Systems **28** (2019), 125–174. https://doi.org/10.25088/ComplexSystems.28.2.125
5. Indexed exact one-step image entropy spectrum: https://github.com/published-finding corpus/2026/tree/main/2026/10/27/SCOPE-exact-nineteen-value-spatial-image-entropy-spectrum-of-elementar--d4f1725c3486
6. Indexed first loss of two-step image words: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-twelve-symbol-threshold-for-second-update-image-loss-in--5742d176c6e4
