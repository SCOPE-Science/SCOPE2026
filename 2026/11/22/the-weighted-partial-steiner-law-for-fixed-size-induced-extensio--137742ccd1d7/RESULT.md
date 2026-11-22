# The weighted partial-Steiner law for fixed-size induced extensions

## Finding
Let \(A_n\) be the empty partial Steiner triple system on \(n\) individually named old vertices. A *partial Steiner triple system* here means a finite set of unordered triples in which any unordered pair occurs in at most one triple. Let \(T_{r,n}\) count all induced extensions on the old labelled vertices and \(r\) *ordered and individually distinguished* new vertices, with no new triple entirely inside the old set. Distinct extension diagrams are counted separately without quotienting by automorphisms.

Let \(I_n\) denote the number of involutions of an \(n\)-element set, including fixed points, so
\[
I_n=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n!}{2^kk!(n-2k)!}.
\]
For each fixed integer \(r\ge1\), let \(\mathcal L_r\) consist of all labelled linear triple systems on the new vertex set \([r]\), and define the natural packing polynomial
\[
P_r(z)=\sum_{H\in\mathcal L_r}z^{|E(H)|},\qquad m=\binom r2.
\]
Then the exact *all-fixed-arities asymptotic extension law* is
\[
\boxed{\lim_{n\to\infty}\frac{T_{r,n}}{I_n^r}=e^{-m/2}\,2^mP_r(1/8).}
\]
For the first four arities the limits are respectively \(1\), \(2e^{-1/2}\), \(9e^{-3/2}\) and \(96e^{-3}\); for arity five the limit is \(2544e^{-5}\).

The law has a finer profile interpretation. Uniformly sample one of the \(T_{r,n}\) extension diagrams. Let \(H\) be its induced system on the \(r\) new points. In the limit, \(H\) has probability proportional to \(2^{m-3|E(H)|}\). Conditional on \(H\), each of the \(m-3|E(H)|\) new-point pairs not covered by a triple in \(H\) independently has probability \(1/2\) of appearing in a triple with one old vertex, in the limiting distribution of the associated *binary presence indicators*.

In particular, when \(r=3\), there are **exactly nine asymptotically equally likely presence patterns**: a triple entirely on the three new points, or any of the eight possible subsets of pairs of new vertices which occur in triples with old vertices. Each has limiting probability \(1/9\). No assertion of independence of the old witness labels themselves is made.

## Assumptions and scope
All old vertices are individually named. A diagram on \([n]\sqcup[r]\) must induce the *empty* triple system on \([n]\). A triple with two old vertices and one new vertex is permitted; the old set need not remain a subsystem of a *total* Steiner quasigroup. The count is of finite labelled relational extension diagrams, **not** complete first-order types over a countable homogeneous partial-Steiner structure. No homogeneous limit or free-amalgamation property of all partial triple systems is assumed.

Every such finite diagram can be embedded in some sufficiently large complete Steiner triple system by the classical partial-design embedding theorem, but no fixed complete ambient structure or completion multiplicity is counted. Limits hold for each fixed \(r\) as \(n\to\infty\); no uniformity in a growing \(r\) is claimed. Equality and repetition among the newly adjoined vertices are excluded.

## Proof
**1. An exact matching-and-assignment reduction.** The triples containing one particular new vertex \(x_i\) and two old vertices have the form \(\{x_i,a,b\}\) with \(\{a,b\}\) ranging over a matching \(M_i\subseteq\binom{[n]}2\). The matchings \(M_1,\ldots,M_r\) must be pairwise **edge-disjoint**, because two different triples cannot contain the same old pair. Conversely, any such tuple of matchings satisfies every constraint for triples of this first kind. Let \(F_i\subseteq[n]\) be the set of unmatched old vertices of \(M_i\).

The triples entirely on the new points form an arbitrary \(H\in\mathcal L_r\). Let \(E_2(H)\) denote the collection of new-point pairs covered by triples of \(H\). For each uncovered pair \(ij\notin E_2(H)\), we may either choose no additional triple or choose exactly one old vertex \(a_{ij}\in F_i\cap F_j\) and add \(\{x_i,x_j,a_{ij}\}\). For each fixed old vertex \(a\), the selected pairs \(ij\) for which \(a_{ij}=a\) must form a matching on the new points, because otherwise some new-old pair \(\{x_i,a\}\) would be repeated. These conditions are also sufficient: they test, respectively, old-old, new-new and new-old pair uniqueness. This gives an **exact finite combinatorial counting formula for every \(n,r\)** as a sum over edge-disjoint \(M_i\), linear \(H\), and the just-described allowed partial witness assignments. No asymptotics or independence is used here.

**2. Sparse common-fixed and shared-edge motifs.** Sample \(r\) independent uniformly random involutions \(\sigma_1,\ldots,\sigma_r\) of \([n]\), interpreting their two-cycles as the matchings \(M_i\). For each \(1\le i<j\le r\), let \(X_{ij}\) count old vertices fixed by *both* involutions, and let \(Y_{ij}\) count common two-cycles of those involutions. Pairwise edge-disjointness of the \(M_i\) is exactly the event \(\mathcal D=\{Y_{ij}=0\text{ for all }i<j\}\).

A prescribed collection of \(s\) distinct fixed vertices and \(t\) disjoint two-cycles in one involution has probability exactly \(I_{n-s-2t}/I_n\). The involution recurrence \(I_n=I_{n-1}+(n-1)I_{n-2}\), with \(I_0=I_1=1\), gives \(I_{n-k}/I_n=n^{-k/2}(1+o(1))\) for every fixed \(k\). Indeed \(\sqrt n\le I_n/I_{n-1}\le1+\sqrt n\), and multiplying the fixed finite number of reciprocal ratios proves the estimate.

For any fixed mixed falling-factorial moment of all \(X_{ij}\) and \(Y_{ij}\), expand it into marked fixed-vertex coincidences and marked shared transpositions. Terms with disjoint old label supports contribute exactly the factorial-moment product \(\prod_{i<j}1^{a_{ij}}(1/2)^{b_{ij}}\): each common fixed site uses one old label with probability asymptotic to \(n^{-1}\), and each shared transposition uses an unordered old pair with probability asymptotic to \(n^{-2}\), accounting for the factor \(1/2\). Any overlap between different marked motifs either violates the involution condition or loses at least half a power of \(n\). For example, two distinct common-fixed pair motifs on the same old vertex require at least three involutions to fix it, with total contribution \(O(n^{-1/2})\); two shared-edge motifs on the same pair require at least three involutions to contain the transposition, with contribution \(O(n^{-1})\). Intersections between a fixed-site and a transposition motif, and partially intersecting transposition motifs, are either impossible or have still smaller order. Thus every mixed factorial moment converges to that of independent variables
\[
(X_{ij},Y_{ij})\ \Longrightarrow\ (Z_{ij},W_{ij}),
\quad Z_{ij}\sim\operatorname{Pois}(1),\quad W_{ij}\sim\operatorname{Pois}(1/2),
\]
independently for all pairs and both types. The multivariate Poisson law is moment-determinate. The same fixed-pattern estimates give bounded moments of every fixed degree, hence uniform integrability of the fixed-degree polynomials used below.

**3. Repeated witness labels vanish.** For fixed \(r\), the expected number of old vertices fixed simultaneously by at least three among the \(r\) independent involutions is at most
\[
\binom r3\,n\left(\frac{I_{n-1}}{I_n}\right)^3=O_r(n^{-1/2}).
\]
If the witness choices in step 1 assign the same old vertex to two different new-point pairs, that vertex must be fixed by at least three involutions. The contribution of all such colliding witness assignments, even without imposing \(\mathcal D\), tends to zero after division by \(I_n^r\): expand the finite-degree witness-choice polynomial into labelled motifs, and apply the overlap estimate of step 2. In particular, for each fixed internal \(H\), the normalized expected count of allowed witness assignments differs by \(o(1)\) from
\[
\mathbb E\left[\mathbf1_{\mathcal D}\prod_{ij\notin E_2(H)}(1+X_{ij})\right].
\]
This also explains why distinct old labels for distinct selected new-point pairs can be assumed only *asymptotically*, not in the exact formula for \(r\ge4\).

**4. Summation and normalized profile.** The independent Poisson limit and uniform integrability give
\[
\lim_{n\to\infty}\mathbb E\left[\mathbf1_{\mathcal D}\prod_{ij\notin E_2(H)}(1+X_{ij})\right]
=e^{-m/2}\,2^{m-|E_2(H)|}.
\]
Because \(H\) is linear, its triples cover pairwise distinct new-point pairs, so \(|E_2(H)|=3|E(H)|\). Summing over all finite \(H\in\mathcal L_r\) and observing that the number of unrestricted matching tuples is \(I_n^r\) gives
\[
\lim_{n\to\infty}\frac{T_{r,n}}{I_n^r}
=e^{-m/2}\sum_{H\in\mathcal L_r}2^{m-3|E(H)|}
=e^{-m/2}2^mP_r(1/8).
\]
More finely, marking each uncovered pair by \(t_{ij}\), the same calculation replaces its factor \(2\) with \(1+t_{ij}\). This proves independent fair presence indicators conditional on \(H\), including the nine-pattern law when \(r=3\): for empty \(H\), all eight pair-presence patterns have equal asymptotic weight \(e^{-3/2}\); the sole nonempty \(H\) has the same weight. This completes the proof.

## Verification
`verify.py` independently computes the exact three-new-vertex extension counts in two ways: (a) enumerating all valid labelled triples on the old plus new vertices for \(0\le n\le3\), and (b) enumerating three pairwise edge-disjoint old matchings and all legal old-witness assignments for \(0\le n\le6\). For \(n=0,1,2,3\), the respective total counts are \(2,5,26,236\); the comparisons return `VERIFICATION_OK`. The counts for \(n=4,5,6\) from the matching method are \(3140,55982,1303460\).

`verify_general.py` separately enumerates partial Steiner triple systems on up to six new vertices, checking the packing polynomials: \(P_3(z)=1+z\), \(P_4(z)=1+4z\) and \(P_5(z)=1+10z+15z^2\). It also directly enumerates several small finite extension totals at arities \(2,3,4,5\); the output is `GENERAL_FINITE_CHECKS_OK`. Both scripts use Python's standard library. Run `python3 verify.py` and `python3 verify_general.py`. Finite checks corroborate exact finite formulas but cannot certify the infinite limiting law; steps 2–4 provide its proof.

## Relationship to prior work
Michael Lugo (2009) develops the graph-of-two-involutions decomposition, generating functions, and cycle statistics. The standard involution asymptotics and the two-involution local Poisson phenomena are prior work; they are not claimed novel here. Daniel Horsley (2014) describes partial Steiner triple systems and their embedding into finite Steiner systems, supplying the relational finite-diagram setting. Puder and Zimhoni (2022), notably their Theorem 2.6, give broad asymptotics for finite sub-cover patterns in random actions of free products; those methods could recover the fixed-colour coincidence moment estimates in step 2. They do **not state** the specific all-arity induced partial-Steiner extension profile or its weighted packing-polynomial factor, which also uses the exact finite diagram reduction of step 1.

A published result titled *Real-rooted one-point extension spectra of partial Steiner triple systems* gives the matching polynomial for one-new-vertex diagrams over arbitrary finite bases, but explicitly excludes claims about generic functional one-types. The present formula uses the more difficult cross-new-vertex constraints for every fixed arity, and its triple law cannot be obtained by independently multiplying one-point counts. The originality assessment is **provisional**: older coloured-matching enumeration, random lift and general finite-structure extension literature might contain an equivalent weighted formula. The claim of contribution is limited to the explicit weighted packing-partition extension law and its joint presence-profile interpretation, not the classical matching correspondence or Poisson machinery.

## Limitations
The result is an asymptotic classification with \(r\) fixed as \(n\to\infty\); no finite-size error rate is asserted. The displayed law concerns uniformly sampled *labelled finite relational extension diagrams*, not random uniform completions of Steiner triple systems, complete types in a homogeneous limit, or a probability measure on infinite Steiner structures. Old parameters have no triples; arbitrary nonempty old partial systems are not covered. The classification does not count automorphism orbits of unlabelled new vertices. Historical priority remains provisional and there has been no independent scientific validation.

## References
1. Michael Lugo, *The cycle structure of compositions of random involutions* (first public 2009-11-18), arXiv:0911.3604, https://arxiv.org/abs/0911.3604.
2. Daniel Horsley, *Embedding partial Steiner triple systems with few triples* (first public 2014-02-12), arXiv:1402.2739, https://arxiv.org/abs/1402.2739.
3. Doron Puder and Tomer Zimhoni, *Local Statistics of Random Permutations from Free Products* (2022), arXiv:2203.12250, especially Sections 2, 5 and 6, https://arxiv.org/html/2203.12250v2.
4. *Real-rooted one-point extension spectra of partial Steiner triple systems*, published research note (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-real-rooted-one-point-extension-spectra-of-partial-steiner-tripl--9599713a6632.
