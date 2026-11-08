# Finite-order exceptions and the shattering polynomial of two-line unions in projective planes

## Finding

Let \(\Pi\) be **any finite projective plane of order** \(q\ge2\), including a non-Desarguesian plane when one exists. Write \(P\) for its set of points, \(\mathscr L\) for its set of lines, and \(v=q^2+q+1\). Let the concepts be the unions of two not necessarily distinct lines,
\[
\mathcal F_2(\Pi)=\{L\cup M:L,M\in\mathscr L\}.
\]
For \(0\le k\le v\), let \(s_k\) be the number of unordered \(k\)-element subsets \(S\subseteq P\) for which every subset of \(S\) occurs as \(S\cap C\) for some \(C\in\mathcal F_2(\Pi)\). Set \(\Phi_{\Pi}(z)=\sum_{k=0}^v s_kz^k\).

**Complete classification.** The polynomial depends only on \(q\), not on the isomorphism class of \(\Pi\). For \(q=2\),
\[
\Phi_{\Pi}(z)=1+7z+21z^2+28z^3.
\]
For \(q=3\),
\[
\Phi_{\Pi}(z)=1+13z+78z^2+286z^3+702z^4+702z^5.
\]
For every order \(q\ge4\) for which a projective plane exists,
\[
\begin{aligned}
\Phi_{\Pi}(z)={}&1+vz+\binom v2z^2+\binom v3z^3\\
&+\left[\binom v4-v\binom{q+1}{4}\right]z^4\\
&+v\left[\binom{q+1}{3}\binom{q^2}{2}-\binom{q+1}{2}\binom q2^2\right]z^5.
\end{aligned}
\]
All coefficients of degree six or higher vanish. Consequently the VC dimension is three for order two and five for every order at least three.

**Precisely which five-point supports are shattered.** A five-point support cannot contain four collinear points and must contain a collinear triple. Such a support has either one collinear triple or exactly two, with the latter intersecting in a single point. At order three, precisely the two-triple (bow-tie) supports are shattered, and there are exactly 702. At every order at least four, both types are shattered; the number with two triples is
\[
B_q=v\binom{q+1}{2}\binom q2^2,
\]
and the number with exactly one triple is
\[
U_q=v\binom{q+1}{3}\binom{q^2}{2}-2B_q.
\]
For order four these counts are \(7560\) and \(10080\), respectively. For order five they are \(46500\) and \(93000\). In particular the density of shattered five-point supports among all five-point supports is asymptotic to \(10/q\) as \(q\) tends to infinity through orders of existing planes.

## Assumptions and scope

A finite projective plane of order \(q\) has \(v=q^2+q+1\) points and lines; every line contains \(q+1\) points, every point is incident with \(q+1\) lines, every pair of distinct points lies on a unique line, and distinct lines intersect in one point. We assume \(q\ge2\) and existence of such a plane; no existence assertion for arbitrary integers \(q\) is made. All statements are intrinsic to incidence, without any field-coordinate assumption. Repetition of a line is allowed in a two-line union, so a single line is also a concept.

## Proof

**1. Six-point obstruction and five-point necessary conditions.** Suppose \(S\) is shattered. Then \(S\) itself is covered by two lines. If a line \(L\) contains at least four points of \(S\), remove one of those points, say \(a\). A concept with trace \(S\setminus\{a\}\) cannot use \(L\), but any two other lines together meet \(L\) in at most two distinct points. They cannot cover the at least three remaining chosen points of \(L\), a contradiction. Thus every line meets a shattered support in at most three points. If a six-point support were shattered, two lines would cover six points and therefore each would carry exactly three. Deleting a point of the first triple would require one of the two realizing lines to contain the entire second triple, hence to be that second triple's original line. The other realizing line would have to contain the remaining two points of the first triple, hence would be its original line, which also contains the excluded point. This is impossible. Thus no support of size six is shattered, and a five-point shattered support must be covered by two lines, contain a triple, and contain no four collinear points.

**2. Two possible five-point incidence types.** In a five-point set with no four collinear, each line containing at least three selected points contains exactly three. There cannot be three distinct such lines: two triples must meet in at most one point, and three distinct triples would require at least six points (if the pairwise intersections are distinct) or seven (if concurrent). Thus the number \(t\) of selected collinear triples is either zero, one, or two. A support covered by two lines and with no four collinear has \(t\in\{1,2\}\). If \(t=2\), the two triples share exactly one point.

**3. Isolation lemma.** Let \(S\) contain five points, have no four collinear, and have at least one collinear triple \(A\) on a line \(L\), with the remaining two points \(u,v\) outside \(L\). Suppose (i) for every \(a\in S\), some line meets \(S\) exactly in \(\{a\}\), and (ii) some line misses \(S\). We show that the two-line unions shatter \(S\). The empty trace is realized by repeating the disjoint line. Traces of one or two points are realized by repeating one private line or taking two private lines. A collinear selected triple is realized by its line, because no four selected points are collinear. For a noncollinear selected triple, some pair belongs to no collinear selected triple: otherwise the three selected pairs would require three different collinear triples in \(S\), contrary to step 2. Its connecting line, together with a private line through the third point, realizes precisely the selected triple. To isolate four points, if the excluded point is \(u\) or \(v\), use \(L\) and a private line through the remaining exterior point. If the excluded point lies in \(A\), join the two included points of \(A\) separately to \(u\) and \(v\). Each resulting line meets \(L\) only in its included point, so both avoid the excluded point. Finally, \(L\) together with the line through \(u,v\) contains all five points.

**4. Why the isolation lemma applies in the stated orders.** If \(q\ge4\), through a selected point pass \(q+1\ge5\) lines, while its four companions determine at most four forbidden lines. Hence every point has a private line. At order three, this argument has no spare line in general. A five-point support with two collinear triples does have a private line at every point: at the shared point, the four companions occupy only two lines; at any other point, at least two of its four companions occupy the same line, leaving at most three occupied lines among its four incident lines. Conversely, a support with exactly one collinear triple has no private line through either exterior point: its three joining lines to the triple, and its line to the other exterior point, are all distinct, exhausting the four lines through it. Such a support cannot isolate the singleton exterior point even by a union of two lines.

For the empty-trace requirement, consider any five-point set with no four collinear and \(t\in\{1,2\}\). Let \(n_i\) be the number of projective lines meeting it in exactly \(i\) points. Counting all lines, point-line incidences, and point pairs yields
\[
 n_3=t,\quad n_2=10-3t,\quad n_1=5q-15+3t,\quad n_0=q^2-4q+6-t.
\]
For \(q\ge3\), \(n_0\ge1\); hence the isolation lemma applies exactly to both types for \(q\ge4\), and only the two-triple type for \(q=3\). For \(q=2\), any five-point support meets every line, because its complement contains just two points and no line; it cannot isolate the empty trace.

**5. Supports of sizes at most four.** Every singleton and pair is shattered, in every order \(q\ge2\): each singleton has a line meeting it, and every pair has a joining line, lines isolating either endpoint, and a line missing both. For a triple at order two, a collinear triple is an entire projective line and meets every line, so it cannot isolate the empty trace. A noncollinear triple has private singleton lines, clean pair lines, and exactly one disjoint line (count incidences); it is shattered by two-line unions. Thus there are \(\binom73-7=28\) shattered triples. For order at least three, every triple is shattered: private singleton lines exist, noncollinear pairs are clean, collinear pairs use two private lines, and there is a line disjoint from the triple. (For a collinear triple, choose a line meeting its carrier at an unselected point; for a noncollinear triple, incidence counting gives \((q-1)^2\) disjoint lines.)

At order two, no four-point support is shattered. If a four-point set contains three collinear points, its remaining point has no private line because its three joining lines to that triple exhaust the three lines through it. If it has no collinear triple, every point has its other three points in three different directions and likewise lacks a private line. For \(q\ge3\), a four-point support is shattered if and only if its points are not all collinear. Necessity follows from step 1. For sufficiency, each selected point has a private line since only three other selected points determine forbidden lines; every selected noncollinear triple has a clean pair (at most one line contains a selected triple) and hence can be isolated with a private line; four selected points can be paired and joined by two lines. A line avoiding all four exists: for \(q\ge4\), \(4(q+1)<v\); for \(q=3\), if \(t\in\{0,1\}\) is its number of collinear triples, incidence counting gives exactly \(3-t\) disjoint lines. The coefficient is therefore \(\binom v4-v\binom{q+1}{4}\) for \(q\ge3\).

**6. Exact census.** In every plane the number of ordered choices of (a line, three of its points, two points outside it) is
\[
T_q=v\binom{q+1}{3}\binom{q^2}{2}.
\]
A five-point set containing one collinear triple contributes once to \(T_q\), whereas one containing two distinct triples contributes twice. To count the latter, select the unique common point, two unordered distinct lines through it, and two further points on each line. This yields
\[
B_q=v\binom{q+1}{2}\binom q2^2.
\]
Thus there are \(T_q-2B_q\) single-triple supports and \(B_q\) double-triple supports. Step 4 determines which of these are shattered, giving \(s_5=B_3=702\) at order three and \(s_5=T_q-B_q\) for all \(q\ge4\). The lower-degree coefficients and zero coefficients above degree five follow from steps 1 and 5. The leading terms \(s_5\sim q^9/12\) and \(\binom v5\sim q^{10}/120\) give the stated asymptotic proportion.

## Verification

The standalone Python program `verify_projective_two_lines.py` uses cyclic difference-set models of the Desarguesian planes of orders two, three, four, and five. It checks the projective incidence axioms, generates all unions of two lines, directly computes all traces for every support up to size six for orders two, three, and four, and for every support through size five at order five. For size six at order five it tests 350 fixed-seed samples, without treating them as exhaustive. It compares each direct result with the structural characterization and all coefficients of the proved formulas. The program reports 293101 tested supports, finishing with `ALL_TWO_LINE_PROJECTIVE_SHATTERING_CHECKS_PASS`. Exact output is in `verification_output.txt`. The all-orders proof is incidence-theoretic, not dependent on the computation.

## Relationship to prior work

Csikós, Kupavskii and Mustafa (2018, arXiv:1807.07924) study VC complexity under unions/intersections of geometric concepts, giving the motivating broad framework but not this finite-projective-plane census. Cambie, Girão and Kang (2019) study general VC bounds for set-system operations, including unions, not the present incidence-specific coefficients. More directly, Eleftheriou, Papadopoulos and Westhead (first publicly posted January 16, 2025, arXiv:2501.09847), Proposition 5.2 and Proposition 7.1, already prove a five-point characterization and two incidence-isomorphism types for unions of two **real Euclidean** lines. We explicitly do **not** claim that their five-point types, or the universal VC upper bound five, are new. Their theorem does not assert the finite-projective-plane coefficients, covers a different point-line universe, and cannot be applied unchanged at projective order three: only the two-triple type is shattered there. The present statement proves the finite-order correction and exact multiplicities for every finite projective plane, including non-Desarguesian examples, with a sharp change from order three to order four. A broader hidden priority result under alternative language remains possible.

## Limitations

The result assumes that a finite projective plane of the specified order exists. The proof does not claim the existence of planes at arbitrary orders, does not address unions of three or more lines, does not determine Littlestone dimension, and does not assert that the general two-line five-point incidence classification was previously unknown. No external independent audit has been performed. The small-order computations do not constitute a substitute for the universal proof. The historical-priority comparison is limited to the inspected literature and mathematical-record search and cannot establish global uniqueness.

## References

1. M. Csikós, A. Kupavskii, and N. H. Mustafa, *Optimal Bounds on the VC-dimension*, arXiv:1807.07924, first posted 2018-07-20. https://arxiv.org/html/1807.07924
2. S. Cambie, A. Girão, and R. J. Kang, *VC Dimension and a Union Theorem for Set Systems*, Electronic Journal of Combinatorics 26(3), P3.24 (2019). https://doi.org/10.37236/8288
3. P. E. Eleftheriou, A. Papadopoulos, and F. Westhead, *Exact VC-Dimensions of Certain Geometric Set Systems*, arXiv:2501.09847, first posted 2025-01-16; especially Proposition 5.2 and Proposition 7.1. https://arxiv.org/html/2501.09847
