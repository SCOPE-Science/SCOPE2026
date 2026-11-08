# Exact facet spectrum and cyclic transfer polynomial for wheel general-position sets

## Finding

For every integer \(m\ge3\), write \(W_m=K_1\vee C_m\), with hub \(h\) and distinguishable cyclic rim vertices \(v_0,\dots,v_{m-1}\). An ordinary *general-position set* is a vertex subset containing no triple on any common shortest path. A *facet* is a general-position set maximal under inclusion. Define its cardinality polynomial by
\[
M_m(z)=\sum_{S\text{ a facet of }W_m}z^{|S|}.
\]
Then
\[
M_3(z)=z^4,\qquad M_4(z)=2z^2+4z^3,
\]
and for every \(m\ge5\),
\[
\boxed{M_m(z)=mz^3+R_m(z)},\qquad
\boxed{R_m(z)=-m[u^m]\log(1-zu^2-z^2u^3-z^2u^4+z^3u^6)}.
\]
Here \([u^m]\) is ordinary formal coefficient extraction and the logarithm has zero constant term. In particular, \(R_m(z)\) is a polynomial with nonnegative integer coefficients.

All facets containing \(h\) are exactly \(\{h,v_i,v_{i+1}\}\), for \(i\) modulo \(m\), when \(m\ge4\). A rim-only general-position subset is a facet for \(m\ge5\) exactly when its cyclic binary word has only 1-runs of lengths one or two and 0-runs of lengths one or two, and each 0-run of length two is flanked by 1-runs of length two. At \(m=4\), precisely the two rim-only opposite pairs remain facets of the wheel.

The exact facet-cardinality spectrum for every \(m\ge5\) is
\[
\boxed{\{3\}\cup\{k\in\mathbb Z: \lceil m/2\rceil\le k\le\lfloor2m/3\rfloor\}}.
\]
Consequently the simplicial complex of general-position subsets is pure if and only if \(m=3\) or \(m=5\). Its lower general-position number (minimum cardinality of any facet) equals \(4\), \(2\), or \(3\) according as \(m=3\), \(m=4\), or \(m\ge5\). For arbitrarily large \(m\), there are no facet cardinalities strictly between \(3\) and \(\lceil m/2\rceil\).

## Assumptions and scope

All graphs are finite, undirected, and simple. The wheel notation fixes *rim length* \(m\), not total graph order. Distances and general position use ordinary graph shortest paths, not induced paths or the stronger total-general-position variants. Facets are inclusion-maximal, which need not have maximum cardinality. All cycle indices are modulo \(m\), and vertex subsets are labelled. The polynomial counts the selected vertex sets themselves, not their orbits under rotations or reflections.

## Proof

**1. Feasible configurations.** For \(m\ge4\), the wheel has diameter two. Any three selected rim vertices on a common shortest path must therefore be a rim triple \(v_i,v_{i+1},v_{i+2}\), and each such triple indeed lies on a shortest path between its endpoints (they are nonadjacent). Thus a rim-only set is in general position if and only if its cyclic 0/1 indicator word avoids \(111\). If the hub belongs to a set, two chosen rim vertices that are nonadjacent would have the length-two hub geodesic between them. Hence a hub-containing set is in general position exactly when its rim part is a clique of \(C_m\). As \(m\ge4\), its maximal realizations are precisely the \(m\) triangles \(\{h,v_i,v_{i+1}\}\).

**2. Exact rim-only maximality.** Let \(m\ge4\). A 111-free cyclic word maximal against changing any 0 to 1 has both 0s and 1s (all-zero is not maximal; all-one is forbidden). It has no 1-run longer than two. It also has no 0-run of length three or more: flipping an interior 0 in such a run produces no 111. If a 0-run has length one, flipping its 0 makes 111 through that zero, since both adjacent positions are 1. If a 0-run has length two, flipping the first 0 is prohibited exactly when the preceding two positions are 11, and flipping the second is prohibited exactly when the following two positions are 11. Thus the double 0-run is permitted only between two length-two 1-runs. These conditions are sufficient to block every single-vertex insertion and necessary by the same local tests. This proves the cyclic-run criterion.

When \(m\ge5\), any rim-only maximal 111-free word has at least three 1s. Indeed, with only one or two 1s, there is necessarily either a 0-run of length at least three, or (for two 1s) a 0-run of length two lacking a length-two 1-run on an adjacent side, except at \(m=4\). A rim-only subset of size at least three cannot acquire the hub while staying in general position (its chosen rim vertices would have to form a clique of the rim, which has clique number two). Thus all such cyclic maximal words are exactly the rim-only wheel facets for \(m\ge5\). At \(m=4\), all six rim two-element subsets are maximal 111-free; four adjacent rim pairs extend with the hub, whereas the two opposite pairs do not. As \(W_3=K_4\), its sole facet is the full four-vertex set. The boundary formulas follow.

**3. Transfer polynomial.** For a cyclic maximal rim word, represent each 1-run of length \(a\in\{1,2\}\) and following 0-run of length \(b\in\{1,2\}\) as a block \(1^a0^b\). A double 0-run is admissible precisely when both its current and next 1-run have length two. Weight a block by \(u^{a+b}z^a\). The two-state transition matrix (rows and columns indexed by \(a\in\{1,2\}\)) is
\[
T(u,z)=\begin{pmatrix}zu^2&zu^2\\z^2u^3&z^2u^3+z^2u^4\end{pmatrix}.
\]
A cycle of \(j\) blocks is enumerated by \(\operatorname{tr}(T^j)\). Every labelled binary word of length \(m\) having \(j\) 1-runs is counted exactly \(j\) times if one chooses a 1-run beginning after an origin among the \(m\) labelled positions, so its contribution is \(m\operatorname{tr}(T^j)/j\) after extracting \([u^m]\). Consequently
\[
R_m(z)=m[u^m]\sum_{j\ge1}\frac{\operatorname{tr}(T^j)}j=-m[u^m]\log\det(I-T).
\]
A direct determinant calculation gives \(\det(I-T)=1-zu^2-z^2u^3-z^2u^4+z^3u^6\), proving the formula. Equivalently, formal differentiation implies the recurrence
\[
R_m=zR_{m-2}+z^2R_{m-3}+z^2R_{m-4}-z^3R_{m-6}\qquad(m\ge7),
\]
with \(R_2=2z\), \(R_3=3z^2\), \(R_4=6z^2\), \(R_5=5z^3\), \(R_6=2z^3+3z^4\). The auxiliary coefficients \(R_2\) and \(R_3\) are formal-series initial data; they are not facet counts for small wheels.

**4. Exact spectrum.** Suppose a maximal rim word has \(k\) ones, \(m-k\) zeros, and \(j\) 1-runs. Every 1-run has length at most two and every 0-run length at least one, so \(k\le2j\le2(m-k)\), or \(k\le\lfloor2m/3\rfloor\). Every 0-run has length at most its following 1-run (in particular a double 0-run requires a double 1-run), so \(m-k\le k\), or \(k\ge\lceil m/2\rceil\). Conversely, for every integer \(k\) in this interval, put \(a=2m-3k\) and \(b=2k-m\). These are nonnegative integers and \((10)^a(110)^b\) is a cyclic word of length \(m\) containing exactly \(k\) ones. Its 1-runs have length one or two and all 0-runs are singletons, so it is maximal. Hence every intermediate cardinality occurs. Adding the \(m\) hub triangles supplies the additional size three, establishing the spectrum.

For \(m=5\), the interval is just \(\{3\}\), and every facet has size three. For \(m=3\), the only facet has size four. All remaining \(m\) have at least two distinct facet sizes: for \(m=4\) they are two and three; for every \(m\ge6\) they are three and at least four. Thus the purity claim follows. The minimum facet cardinality also follows directly.

## Verification

Execute the standalone standard-library Python 3 file `verify.py` in the same directory. Its oracle uses the original shortest-path definition in an independently constructed wheel graph, with no run decomposition assumed. It exhaustively compares wheel subsets for rim lengths \(4\) through \(11\), checks the cyclic-run criterion and closed recurrence for rim lengths \(4\) through \(17\), and checks the exact facet spectra. Its successful output is recorded in `VERIFICATION.md`. Exhaustion at finitely many orders is corroboration; the proof above establishes the infinite-family statements.

## Relationship to prior work

Yao, He, Ji and Li established the maximum general-position number of wheels, including \(\lfloor2m/3\rfloor\) for \(m\ge6\), in arXiv:2002.03108, Theorem 4.1. Their observation that selected rim vertices avoid three consecutive vertices is a starting fact, not itself new. Di Stefano et al. introduced and investigated the lower general-position invariant in arXiv:2306.09965; the inspected treatment is not an enumeration of every wheel facet. Iršič et al. established a general position polynomial under graph joins in arXiv:2401.05696; consequently, **an all-feasible-set polynomial for wheels is not claimed here**. The contribution assessed here is the facet (inclusion-maximal-set) polynomial, complete cyclic run classification, sharp facet-size spectrum and purity boundary.

## Limitations

No claim is made about the ordinary all-general-position-set polynomial, which is handled by existing join methods. The result is for wheels specifically, not arbitrary cones over graphs. Although full texts of the principal 2020, 2023 and 2024 preprints were inspected, a highly relevant October 2026 article by González Yero about numbers of maximal general-position sets of connected graphs was available only through bibliographic abstracts, which indicate examples involving grids, trees and hypercubes; its full content was not accessed. Therefore a possible equivalent result in that article or other unindexed literature remains a publication-priority risk. No independent audit has been performed.

## References

1. Yan Yao, Mengya He, Shengjin Ji, Guang Li, *On the general position set of two classes of graphs*, arXiv:2002.03108 (first posted 2020-02-08), especially Section 4, Theorem 4.1.
2. Gabriele Di Stefano, Sandi Klavžar, Aditi Krishnakumar, James Tuite, Ismael Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (first posted 2023-06-16).
3. Vesna Iršič, Sandi Klavžar, Gregor Rus, James Tuite, *General position polynomials*, arXiv:2401.05696 (first posted 2024-01-11), especially Proposition 3.3.
4. Ismael González Yero, *Concerning the number of maximal general position sets of connected graphs*, The Art of Discrete and Applied Mathematics, DOI 10.26493/2590-9770.1957.bc9 (reported October 2026; full text not inspected).
