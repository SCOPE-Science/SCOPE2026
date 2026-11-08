# Hypercube shortcuts, discrepancy, and the sharp variance-preservation boundary

## Finding

Let \(d\ge3\) be an integer, let \(Q_d\) be the graph on \(\{0,1\}^d\) whose edges join vectors differing in one coordinate, and let \(\mathcal H\subseteq\binom{[d]}3\) be a family of distinct triples. For \(S\in\mathcal H\), write \(\mathbf1_S\) for its incidence vector, and form the connected simple graph \(G_{\mathcal H}\) by adding the unit edge \(\{\mathbf0,\mathbf1_S\}\) for every \(S\in\mathcal H\). The new edges join cube vertices originally at distance three. The vertex distribution remains uniform on all \(2^d\) vertices.

For any connected graph \(G\) with uniform vertex measure, let
\[
\operatorname{spr}(G)=\max_{|f(u)-f(v)|\le1\ (uv\in E(G))}\operatorname{Var}(f(X)),
\]
where \(X\) is a uniformly random vertex. Then the following *sharp-preservation and quantitative-loss theorem* holds:

**Theorem.** The following are equivalent:

1. \(\operatorname{spr}(G_{\mathcal H})=d/4\).
2. There is \(\varepsilon\in\{-1,1\}^d\) such that \(\bigl|\sum_{i\in S}\varepsilon_i\bigr|=1\) for every \(S\in\mathcal H\).
3. The three-uniform hypergraph \(([d],\mathcal H)\) is properly two-colorable (has Property B).

When these conditions hold, **all** spread-maximizing real functions, and only those, are
\[
 f(x)=c+\sum_{i=1}^d\varepsilon_i x_i,\qquad c\in\mathbb R,
\]
with \(\varepsilon\) satisfying condition 2. In particular the number of maximizers modulo addition of constants equals the number of proper labeled two-colorings of \(\mathcal H\).

When these conditions fail, there is a uniform explicit strict gap
\[
 \boxed{\operatorname{spr}(G_{\mathcal H})\le \frac d4-2^{-d-1}.}
\]
The displayed gap is a certified lower bound on the loss, **not** asserted to be optimal.

Consequently the decision problem **FULL-SPREAD-3-CHORD** (input the binary integer \(d\) and a list of distinct triples \(\mathcal H\); ask whether the graph represented by this pair has spread \(d/4\)) is NP-complete. This complexity claim concerns this succinct cube-plus-chords encoding, not the explicitly expanded adjacency matrix on \(2^d\) vertices. The YES and NO cases have the displayed explicit separation.

For context, adding just **one** unit shortcut between any two distinct nonadjacent cube vertices never changes \(\operatorname{spr}(Q_d)=d/4\), irrespective of their original Hamming distance: a suitable balanced choice of coordinate signs remains admissible. On the other hand, the seven triples \(\{i,i+1,i+3\}\) modulo \(7\) form a Fano-plane family and enforce a strict loss with only seven distance-three shortcuts.

## Assumptions and scope

Graphs are finite, connected, simple, unweighted, and undirected. The probability measure is uniform on the original cube vertices, and functions take real values. Each added shortcut has Lipschitz bound one, regardless of its former cube distance. For arbitrary added edges \(\{u,v\}\), equality with the original cube spread holds exactly when some \(\varepsilon\in\{-1,1\}^d\) obeys
\[
\left|\sum_{i=1}^d\varepsilon_i(u_i-v_i)\right|\le1
\]
for every added edge. The three-uniform, common-origin specialization turns this into Property B and supports the quantitative gap and complexity results.

## Proof

**1. Exact cube variance bound, with all equality cases.** For a real \(f\) on the cube let \(\chi_S(x)=\prod_{i\in S}(2x_i-1)\), and expand in the orthonormal Walsh basis
\[
 f(x)=\sum_{S\subseteq[d]}a_S\chi_S(x).
\]
Write \(\Delta_i f(x)=f(x_1,\ldots,1,\ldots,x_d)-f(x_1,\ldots,0,\ldots,x_d)\), independent of \(x_i\). Parseval gives
\[
\operatorname{Var}(f)=\sum_{S\ne\varnothing}a_S^2,
\qquad
\frac14\sum_{i=1}^d\mathbb E(\Delta_i f)^2
   =\sum_{S\ne\varnothing}|S|a_S^2.
\]
If \(f\) is one-Lipschitz on all original cube edges, then \(|\Delta_i f|\le1\). Therefore
\[
\operatorname{Var}(f)\le\frac14\sum_i\mathbb E(\Delta_i f)^2\le\frac d4.
\]
Equality in the first inequality forces \(a_S=0\) whenever \(|S|\ge2\); equality in the second forces \(|\Delta_i f|=1\) for every \(i\) and every cube vertex. Hence equality holds **precisely** for \(f(x)=c+\sum_i\varepsilon_i x_i\) with \(\varepsilon_i\in\{-1,1\}\). Every such function has variance \(d/4\), so this characterization is bidirectional.

**2. Added-edge criterion and two-coloring equivalence.** Any function Lipschitz on \(G_{\mathcal H}\) is Lipschitz on \(Q_d\), hence has variance at most \(d/4\). Equality requires precisely a signed coordinate sum as in step 1. The added edge from \(\mathbf0\) to \(\mathbf1_S\) is admissible exactly when \(\bigl|\sum_{i\in S}\varepsilon_i\bigr|\le1\); for a triple the possible absolute values are \(1\) and \(3\). The inequality is thus equivalent to \(S\) containing both signs. This proves all three equivalent conditions and the complete equality-case classification.

**3. An explicit gap in every non-two-colorable case.** Let \(f\) be any one-Lipschitz function on \(G_{\mathcal H}\), and put \(\delta=d/4-\operatorname{Var}(f)\ge0\). Split its Walsh expansion into its constant term, its first-degree terms, and \(h=\sum_{|S|\ge2}a_S\chi_S\). The two inequalities in step 1 give the exact nonnegative deficit decomposition
\[
\delta=
\underbrace{\frac14\sum_i\bigl(1-\mathbb E(\Delta_i f)^2\bigr)}_{\ge0}
 +\underbrace{\sum_{|S|\ge2}(|S|-1)a_S^2}_{\ge0}.
\]
It follows that \(\|h\|_2^2\le\delta\). Set \(t_i=2a_{\{i\}}\). Since \(t_i=\mathbb E\Delta_i f\) and \(|\Delta_i f|\le1\), we have \(|t_i|\le1\). Moreover
\[
\sum_i(1-t_i^2)
  =4\delta+4\|h\|_2^2\le8\delta.
\]
Choose \(\sigma_i\in\{-1,1\}\) to have the sign of \(t_i\), breaking any zero ties arbitrarily. Then
\[
 \sum_i|\sigma_i-t_i|=\sum_i(1-|t_i|)\le8\delta.
\]
If \(\mathcal H\) is not two-colorable, one triple \(S\) is monochromatic under \(\sigma\), so \(\bigl|\sum_{i\in S}\sigma_i\bigr|=3\). Uniform measure and Cauchy--Schwarz imply the pointwise bound \(|h(x)|\le2^{d/2}\|h\|_2\le2^{d/2}\sqrt\delta\). Consequently the shortcut constraint forces
\[
1\ge|f(\mathbf1_S)-f(\mathbf0)|
 \ge3-8\delta-2^{1+d/2}\sqrt\delta,
\]
so \(8\delta+2^{1+d/2}\sqrt\delta\ge2\). But if \(d\ge3\) and \(\delta\le2^{-d-1}\), the left-hand side is at most \(2^{2-d}+\sqrt2\le\tfrac12+\sqrt2<2\), a contradiction. Thus every admissible \(f\) has \(\delta>2^{-d-1}\), yielding the asserted (non-sharp) closed bound on spread by compactness.

**4. Complexity.** A YES certificate assigns a sign to each coordinate that actually occurs in a listed triple, so it contains at most three times as many bits as there are triple records. Signs on unused coordinates can be chosen freely; this avoids requiring a length-\(d\) witness when the integer \(d\) is binary-encoded. All triple constraints can be checked in time polynomial in the succinct input length, so the problem is in NP. The map sending an instance of three-uniform hypergraph two-colorability (monotone not-all-equal three-satisfiability) to the identical list \((d,\mathcal H)\) is a polynomial-time many-one reduction. By step 2 it preserves YES/NO answers exactly. The source problem, Property B on three-uniform hypergraphs, is NP-complete: for example Darmann and Döcker (2019, Theorem 1) prove this even for positive clauses with three distinct variables appearing four times each, building on the classical Schaefer dichotomy. The promised analytic gap from step 3 applies to every NO instance; no assertion is made that its binary rational representation has polynomial length in a succinct input with very large \(d\).

**5. Opposite behaviors of few shortcuts.** For an arbitrary extra cube edge \(\{u,v\}\), let \(D=\{i:u_i\ne v_i\}\). If \(|D|\ge2\), choose \(\varepsilon_i(u_i-v_i)\in\{-1,1\}\) on \(D\) with as many positive as negative terms as possible. Then \(\bigl|\sum_{i\in D}\varepsilon_i(u_i-v_i)\bigr|\le1\), establishing one-shortcut invisibility. For the Fano family \(S_i=\{i,i+1,i+3\}\pmod7\), each unordered pair of the seven points lies in exactly one of the seven triples. If a two-coloring made all triples nonmonochromatic, each triple would contribute exactly one monochromatic pair, so there would be exactly seven such pairs. But if one color occurs \(r\) times, the total is \(\binom r2+\binom{7-r}2=r^2-7r+21\ge9\), a contradiction. The gap bound applies with \(d=7\).

## Verification

A standalone exact-arithmetic Python program, `check_hypercube_chord.py`, is included. Execute `python check_hypercube_chord.py`. It enumerates all anchored integer-valued Lipschitz maps on \(Q_d\) for \(d=1,2,3\), exactly verifies preservation on a three-dimensional cube with one distance-three shortcut, checks balanced witnesses for every possible single shortcut support through \(d=8\), verifies Fano non-two-colorability and the pair-incidence property, and checks the Fourier/Poincaré deficit identity on an explicit rational instance. These finite checks **do not** prove the all-dimension theorem or the NP-completeness result; the proof above does.

## Relationship to prior work

Alon, Boppana and Spencer introduced graph spread as the maximal variance of a Lipschitz observable and established fundamental product-space principles. Addario-Berry, Janson and McDiarmid explicitly state \(\operatorname{spr}(Q_d)=d/4\), the Cartesian-product tensorization formula, and edge monotonicity. Those known results form the starting point; **the unaugmented cube formula is not new**. Schaefer's 1978 dichotomy theorem establishes classical not-all-equal hardness, and Darmann and Döcker's 2019 Theorem 1 confirms NP-completeness under the exact three-distinct-positive-variable restrictions used here; **that hardness is not new**. The contribution here is the *exact equality/optimizer criterion after adding cube shortcuts*, its uniform quantitative loss in the non-colorable case, and the resulting exact graph-norm decision problem. The graph-side statement is not a restatement of either cited preexisting theorem alone.

## Limitations

The theorem does not determine the exact spread below the preserved maximum in non-two-colorable cases. The exponential lower bound on the loss is explicit but not known to be optimal. The NP-completeness statement is for the succinct \((d,\mathcal H)\) encoding, which describes an exponentially larger graph, and makes no NP-hardness claim for standard explicitly presented graphs. Weighted measures, weighted edges, alternate nonlinear objectives, and hyperedge lists outside the stated three-uniform common-origin case are not covered by the gap theorem. Complete exhaustion of all potentially equivalent literature cannot be guaranteed.

## References

1. N. Alon, R. Boppana, J. Spencer, *An asymptotic isoperimetric inequality*, Geometric and Functional Analysis **8** (1998), 411–436. DOI: `10.1007/s000390050062`. Author manuscript: `https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf`.
2. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, first public arXiv submission 2009-02-06, `arXiv:0902.1156`. Full text: `https://arxiv.org/pdf/0902.1156`.
3. T. J. Schaefer, *The complexity of satisfiability problems*, Proceedings of STOC (1978), 216–226. DOI: `10.1145/800133.804350`.

4. A. Darmann and J. Döcker, *On simplified NP-complete variants of Not-All-Equal 3-Sat and 3-Sat*, first public arXiv submission 2019-08-12, `arXiv:1908.04198`. Theorem 1, Section 3.1. Full text: `https://arxiv.org/pdf/1908.04198`.
