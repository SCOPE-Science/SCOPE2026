# Sharp EFX orientation entropy on weighted paths and its collapse under monotone perturbations

## Finding

**Theorem (sharp census range and weight sensitivity).** For every integer \(m\ge1\) and every strictly positive symmetric path-edge weight vector \(w=(w_0,\ldots,w_{m-1})\), the number \(N_m(w)\) of complete endpoint-oriented allocations satisfying zero-inclusive EFX obeys

\[
m+1\le N_m(w)\le U_m:=\sum_{k=0}^{\lfloor m/4\rfloor}\binom{m-2k+1}{2k+1}.
\]

Both bounds are attained: strictly increasing weights attain the lower bound, and constant weights attain the upper bound. The upper counts have the exact generating function and recurrence

\[
\sum_{m\ge0}U_m z^m=\frac{1}{1-2z+z^2-z^4},\qquad
U_m=2U_{m-1}-U_{m-2}+U_{m-4}\quad(m\ge5),
\]

with \(U_0=1\), \(U_1=2\), \(U_2=3\), \(U_3=4\), and \(U_4=6\). Writing \(\varphi=(1+\sqrt5)/2\),

\[
U_m=\left(\frac12+\frac1{\sqrt5}\right)\varphi^m+O(1).
\]

For every \(\varepsilon>0\), the weights \(w_i=1+\varepsilon(i+1)/m\) differ from unit weights by at most \(\varepsilon\), yet have only \(m+1\) EFX orientations. Therefore the ratio of EFX counts at these perturbed and unperturbed instances is asymptotic to

\[
\frac{m+1}{(1/2+1/\sqrt5)\varphi^m}.
\]

This is a directed, coherent perturbation statement, not a claim that every nonconstant perturbation has the same effect.

## Assumptions and scope

The path has vertices \(v_0,\ldots,v_m\) and edges \(e_i=\{v_i,v_{i+1}\}\) for \(0\le i<m\). Each edge is an indivisible good allocated to exactly one of its two endpoints. Every agent has an additive valuation; both endpoints of \(e_i\) assign it value \(w_i>0\), and all other vertices assign it value zero. Different edge weights are allowed; symmetry refers only to the agreement of the two endpoints of a given edge.

An orientation is **zero-inclusive EFX** if, for every two distinct vertices \(u,v\) and every good \(g\) in the bundle allocated to \(v\), the value to \(u\) of its own bundle is at least the value to \(u\) of \(v\)'s bundle with \(g\) removed. In particular, removing a good that \(u\) values at zero is a legitimate EFX comparison. We count each edge-direction word separately, with path vertices fixed and labeled.

Encode an allocation as \(b_0\cdots b_{m-1}\) where \(b_i=0\) means that \(e_i\) is assigned to \(v_{i+1}\), and \(b_i=1\) means it is assigned to \(v_i\). An occurrence \(b_{j-1}b_j=01\) is a **sink** at \(v_j\): both adjacent edge-goods are allocated to this vertex.

## Proof

**1. Exact local criterion.** On a simple graph with the stated valuation rule, only adjacent agents can value a good assigned to one another. If an edge \(e=\{u,v\}\) is allocated to \(v\), then \(u\) values exactly that edge within \(v\)'s bundle. If \(v\)'s bundle consists solely of \(e\), deleting it leaves value zero to \(u\). If \(v\) owns a second edge, deleting that second (nonincident-to-\(u\)) good leaves value \(w_e\) to \(u\). Thus, in the latter case, EFX holds from \(u\) toward \(v\) exactly when \(u\)'s own bundle has value at least \(w_e\). These are all possible nontrivial EFX comparisons.

On the path, the only vertices able to receive two edges are internal sinks \(v_j\), identified by \(b_{j-1}b_j=01\). The left neighbor \(v_{j-1}\) must hold \(e_{j-2}\), hence \(j\ge2\), \(b_{j-2}=0\), and \(w_{j-2}\ge w_{j-1}\). The right neighbor \(v_{j+1}\) must hold \(e_{j+1}\), hence \(j\le m-2\), \(b_{j+1}=1\), and \(w_{j+1}\ge w_j\). Conversely, these two comparisons at every sink eliminate all possible strong envy. Therefore an orientation is EFX if and only if every 01 is flanked to form 0011 with precisely the indicated two weight inequalities. When \(m<4\), no sink is possible, consistently with the criterion.

**2. Lower bound.** A word containing no 01 has the unique form \(1^a0^{m-a}\), for an integer \(0\le a\le m\). All \(m+1\) such words are EFX, since no vertex owns two goods. For strictly increasing positive weights, the required left-sink comparison \(w_{j-2}\ge w_{j-1}\) is impossible at every sink, so these are *all* the EFX orientations. This proves the sharp lower bound.

**3. Upper bound and exact count.** The local criterion implies that any word accepted at arbitrary positive weights is accepted when all weights are equal: the purely directional restrictions are identical, and the two weight inequalities then always hold. For equal weights, a valid word is exactly a binary word in which every 01 transition is flanked to form 0011. Its unique run decomposition is

\[
1^{a_0}\,(0^{b_1}1^{c_1})\cdots(0^{b_k}1^{c_k})\,0^{a_1},
\]

where \(k\ge0\), \(a_0,a_1\ge0\), and every \(b_i,c_i\ge2\). For \(k=0\), the word is \(1^{a_0}0^{a_1}\). An unrestricted run contributes generating function \((1-z)^{-1}\); each pair of long runs contributes \(z^4(1-z)^{-2}\). Thus the ordinary generating function is

\[
\frac{1}{(1-z)^2}\sum_{k\ge0}\left(\frac{z^4}{(1-z)^2}\right)^k
=\frac{1}{(1-z)^2-z^4}
=\frac{1}{1-2z+z^2-z^4}.
\]

Expanding the geometric sum, coefficient extraction gives

\[
U_m=\sum_{k=0}^{\lfloor m/4\rfloor}
[z^{m-4k}](1-z)^{-2k-2}
=\sum_{k=0}^{\lfloor m/4\rfloor}\binom{m-2k+1}{2k+1}.
\]

The rational denominator supplies the recurrence and its initial values.

**4. Growth and instability.** The generating-function denominator factors as

\[
(1-z-z^2)(1-z+z^2).
\]

Its unique smallest-modulus pole is \(\rho=\varphi^{-1}\); the other roots have modulus one or \(\varphi\). A simple-pole residue calculation gives coefficient \(\frac12+\frac1{\sqrt5}\) multiplying \(\varphi^m\); the unit-modulus poles produce a bounded periodic correction and the last real pole a decaying term. Thus the stated \(O(1)\) asymptotic is valid. The strictly increasing weights \(w_i=1+\varepsilon(i+1)/m\) are positive and uniformly within \(\varepsilon\) of 1, so Step 2 shows their count equals \(m+1\). Dividing by the equal-weight count and applying the asymptotic proves the exponential collapse.

## Verification

The standalone `verify.py` performs a literal all-agent-pairs, all-bundle-removals EFX test independently of the sink criterion, for every edge orientation in every positive integer weight vector from \(\{1,2,3\}^m\) with \(1\le m\le7\). It also compares the two tests for sampled longer paths, checks all resulting counts against the two bounds, confirms both extremizers, checks the coefficient formula against direct enumeration through \(m=13\), and checks the recurrence through \(m=200\). The run returned `VERIFY_OK`, processing 397,362 weighted orientation states from 3,343 weighted configurations. These finite checks complement, but do not replace, the infinite proof.

Some upper counts are \(U_4=6\), \(U_8=45\), \(U_{12}=305\), and \(U_{14}=799\). The corresponding minimum count is always \(m+1\).

## Relationship to prior work

Graphical EFX goods allocations and the desirability of endpoint orientations were introduced by Christodoulou, Fiat, Koutsoupias, and Sgouritsa (2023). Zeng and Mehta (2024) proved that every bipartite graph is strongly EFX orientable, and their constructive Lemma 4.1 is an existence result, not an enumeration or a sharp count range. Deligkas, Eiben, Goldsmith, and Korchemna (2024) focus on the complexity of finding orientations; Afshinmehr and collaborators (2024) study existence in bipartite multigraphs. The claimed additional result is the *complete weighted-path local test and sharp extremal count, including the exponentially unstable prevalence*, not the already-established existence of fair orientations.

The binary-word generating-function computation uses elementary regular-language enumeration. Its value here is an exact fair-allocation census with a weight-perturbation consequence; no claim is made that the underlying rational-function technique is new.

## Limitations

The theorem requires a simple path, symmetric strictly positive additive edge valuations and complete endpoint allocation. The exponential collapse follows for increasing perturbations; it does not assert that any arbitrary perturbation causes the minimum count. The reported priority comparison does not rule out an equivalent statement hidden in unindexed work or in uninspected source material. The result is an exact mathematical count, not an independent or machine-verified formal proof.

## References

1. G. Christodoulou, A. Fiat, E. Koutsoupias, and A. Sgouritsa, *EFX Allocations on Graphs*, EC 2023. https://doi.org/10.1145/3580507.3597764 ; https://www.cs.ox.ac.uk/people/elias.koutsoupias/Personal/Papers/fair-allocations-on-graphs.pdf
2. J. A. Zeng and R. Mehta, *On the Structure of EFX Orientations on Graphs*, arXiv:2404.13527, first version April 21, 2024. https://arxiv.org/abs/2404.13527
3. A. Deligkas, E. Eiben, T.-L. Goldsmith, and V. Korchemna, *EF1 and EFX Orientations*, arXiv:2409.13616, first version September 20, 2024. https://arxiv.org/abs/2409.13616
4. M. Afshinmehr, A. Danaei, M. Kazemi, K. Mehlhorn, and N. Rathi, *EFX Allocations and Orientations on Bipartite Multi-graphs: A Complete Picture*, arXiv:2410.17002, first version October 22, 2024. https://arxiv.org/abs/2410.17002
