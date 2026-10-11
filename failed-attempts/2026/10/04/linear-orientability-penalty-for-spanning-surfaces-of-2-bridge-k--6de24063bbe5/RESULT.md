# Linear orientability penalty for spanning surfaces of 2-bridge knots
## Finding
For each integer \(c\ge 3\), let \(\mathcal K_c\) be the set of 2-bridge knots of crossing number \(c\), counting non-isotopic mirror images separately. For \(K\in\mathcal K_c\), define
\[
D(K)=2g(K)-\Gamma(K),
\]
where \(g(K)\) is the Seifert genus and \(\Gamma(K)\) is the unoriented genus, namely the minimum first Betti number among all spanning surfaces of \(K\).

Then
\[
rac{1}{|\mathcal K_c|}\sum_{K\in\mathcal K_c}D(K)
=
rac{c}{6}+rac{1}{18}+o(1).
\]
Thus the average extra first-Betti complexity forced by requiring a spanning surface to be orientable is linear in crossing number.

This average statement forces a knot-level prevalence statement. For every fixed \(0<\delta<1/6\),
\[
\liminf_{c	o\infty}
rac{|\{K\in\mathcal K_c:D(K)\ge \delta c\}|}{|\mathcal K_c|}
\ge
rac{1/6-\delta}{1-\delta}.
\]
In particular,
\[
\liminf_{c	o\infty}
rac{|\{K\in\mathcal K_c:D(K)\ge c/12\}|}{|\mathcal K_c|}
\ge rac{1}{11}.
\]

## Assumptions and scope
The ensemble \(\mathcal K_c\) is exactly the mirror-distinguishing ensemble used in the recent average-unoriented-genus paper: if a \(c\)-crossing 2-bridge knot is chiral, both it and its mirror occur, while an amphichiral knot occurs once.

For a knot, every orientable spanning surface of genus \(g\) has first Betti number \(2g\). Hence \(2g(K)\) is the minimum first Betti number among orientable spanning surfaces, while \(\Gamma(K)\) is the minimum with no orientability constraint. Therefore \(D(K)\ge0\) has the direct interpretation of an orientability penalty.

The result uses two established asymptotics on the same mirror-distinguishing 2-bridge-knot ensemble:
\[
\overline g(c)=rac{c}{4}+rac{1}{12}+o(1)
\]
and
\[
\overline\Gamma(c)=rac{c}{3}+rac{1}{9}+o(1).
\]
The first is the oblique asymptote of Suzuki--Tran's exact average-genus formula; the second is Theorem 1.4 of Cohen--Kindred--Lowrance--Shanahan--Van Cott.

## Proof
Averaging \(D(K)=2g(K)-\Gamma(K)\) over \(\mathcal K_c\) and using linearity of expectation gives
\[
\overline D(c)=2\overline g(c)-\overline\Gamma(c).
\]
Substituting the two source asymptotics yields
\[
\overline D(c)
=2\left(rac{c}{4}+rac{1}{12}+o(1)ight)
-\left(rac{c}{3}+rac{1}{9}+o(1)ight)
=rac{c}{6}+rac{1}{18}+o(1).
\]

For the density conclusion, put \(X_c(K)=D(K)/c\). Since \(\Gamma(K)\ge0\) and every \(c\)-crossing knot satisfies \(2g(K)\le c-1\),
\[
0\le X_c(K)<1.
\]
Let
\[
p_c(\delta)=rac{|\{K\in\mathcal K_c:X_c(K)\ge\delta\}|}{|\mathcal K_c|}.
\]
On the complement of this event, \(X_c(K)<\delta\), while on the event itself \(X_c(K)<1\). Therefore
\[
\mathbb E[X_c]\le \delta(1-p_c(\delta))+p_c(\delta)
=\delta+(1-\delta)p_c(\delta).
\]
Because \(\mathbb E[X_c]	o1/6\), rearranging and taking lower limits gives
\[
\liminf_{c	o\infty}p_c(\delta)
\gerac{1/6-\delta}{1-\delta}.
\]
Setting \(\delta=1/12\) gives \(1/11\).

## Verification
The recent primary source was inspected in full through its arXiv HTML rendering. Its Definition 1.1 defines \(\Gamma\) as minimum first Betti number over all spanning surfaces, states that an orientable spanning surface of a knot has first Betti number \(2g\), specifies the mirror-distinguishing ensemble \(\mathcal K_c\), and its Theorem 1.4 proves
\[
\overline\Gamma(c)=rac{c}{3}+rac{1}{9}+o(1).
\]
The source also explicitly cites the earlier exact average-genus computations.

Suzuki--Tran's full preprint was inspected at Theorem 1 and its mirror-convention appendix. The main theorem gives the exact average genus and the oblique asymptote
\[
\overline g(c)=rac{c}{4}+rac{1}{12}+o(1),
\]
while the appendix confirms that the main calculation distinguishes non-isotopic mirrors, matching the recent source's ensemble.

The bundled arithmetic regression prints:

`VERIFY_OK mean_gap=c/6+1/18+o(1) threshold=c/12 density_lower_bound=1/11`

The script checks only the coefficient subtraction and the elementary density inequality. It does not replace the cited topological theorems.

## Relationship to prior work
Cohen--Kindred--Lowrance--Shanahan--Van Cott place classical genus, unoriented genus, and crosscap number in the same spanning-surface framework and explicitly recall earlier average-genus work before proving the average-unoriented-genus asymptotic. Their paper does not state the asymptotic difference \(2\overline g-\overline\Gamma\), the resulting linear orientability penalty, or the positive-density consequence above. Searches of the full text for the constants \(2/3\), \(c/6\), and for an orientability-gap formulation did not locate those statements.

Suzuki--Tran compute average Seifert genus, but do not compare it to the later average unoriented genus. Targeted literature searches for combinations of 2-bridge knots, average genus, average crosscap/unoriented genus, orientability gap, the ratio \(2/3\), the gap \(c/6\), and positive-proportion formulations did not locate an equivalent statement.

The mean relation also gives the equivalent normalized comparison
\[
rac{\overline\Gamma(c)}{2\overline g(c)}\longrightarrowrac{2}{3},
\]
but the density theorem is stronger than a ratio of averages: it guarantees a positive asymptotic proportion of individual knots with a linearly large orientability penalty.

## Limitations
The density lower bound is deliberately distribution-free and is unlikely to be sharp. Determining the limiting distribution of \(D(K)/c\), or the optimal proportion above a fixed linear threshold, requires joint information about \(g(K)\) and \(\Gamma(K)\) that the two marginal average theorems do not provide.

The result concerns 2-bridge knots with the mirror convention stated above. It does not assert analogous behavior for arbitrary knots or links.

The recent source was first posted on 2025-01-06. Its arXiv record is in geometric topology; the present claim is classified under knot theory \(57K10\).

## References
1. M. Cohen, T. Kindred, A. M. Lowrance, P. D. Shanahan, and C. A. Van Cott, *Average crosscap number of a 2-bridge knot*, arXiv:2501.03099v1, first posted 2025-01-06; accepted in *Algebraic & Geometric Topology*.
2. M. Suzuki and A. T. Tran, *Genera and crossing numbers of 2-bridge knots*, arXiv:2204.09238v1, 2022.
3. M. Cohen and A. M. Lowrance, *The average genus of a 2-bridge knot is asymptotically linear*, New York Journal of Mathematics 30 (2024), 1029--1055.
