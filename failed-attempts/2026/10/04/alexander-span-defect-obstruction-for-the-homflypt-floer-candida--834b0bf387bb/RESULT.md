# Alexander-span defect obstruction for the HOMFLYPT–Floer candidates
## Finding
For a knot \(K\), set
\[
d_\Delta=\operatorname{sp}\Delta_t(K),\qquad d_H=\deg P_z(K).
\]
Then the two HOMFLYPT–concordance candidate inequalities
\[
2|\tau(K)|\le d_H
\]
and
\[
|s(K)|\le d_H
\]
have the following necessary counterexample conditions:
\[
2|\tau(K)|>d_H\quad\Longrightarrow\quad
d_\Delta<2|\tau(K)|\le2g(K),
\]
and
\[
|s(K)|>d_H\quad\Longrightarrow\quad
d_\Delta<|s(K)|\le2g(K).
\]
Because the Alexander span of a knot and \(2g(K)\) are even, every counterexample to either candidate satisfies the quantitative defect bound
\[
2g(K)-d_\Delta\ge2.
\]

Consequently both candidates hold for every Alexander-sharp knot,
\[
\operatorname{sp}\Delta_t(K)=2g(K).
\]
In particular, both candidates hold for every fibered knot.

## Assumptions and scope
The HOMFLY–PT normalization is the one used in the recent source: \(P_U(a,z)=1\), with \(P_K(1,z)=\nabla_K(z)\), the Conway polynomial. Thus the maximal \(z\)-degree of the HOMFLY–PT polynomial dominates the Conway degree, which equals the span of the Alexander polynomial in the corresponding normalization:
\[
d_H\ge d_\Delta.
\]

The smooth slice genus is denoted by \(g_4(K)\). We use the standard concordance bounds
\[
|\tau(K)|\le g_4(K),\qquad |s(K)|\le2g_4(K),
\]
together with \(g_4(K)\le g(K)\).

No assertion is made that the two candidate inequalities hold for all knots. The result only gives exact necessary conditions on any counterexample and a broad class on which both candidates are proved.

## Proof
The HOMFLY–PT specialization \(P_K(1,z)=\nabla_K(z)\) implies
\[
d_\Delta\le d_H.
\]
If the first candidate fails, then
\[
d_H<2|\tau(K)|.
\]
Combining these inequalities gives
\[
d_\Delta<2|\tau(K)|.
\]
The Ozsváth–Szabó four-ball-genus bound and \(g_4(K)\le g(K)\) give
\[
2|\tau(K)|\le2g_4(K)\le2g(K),
\]
hence
\[
d_\Delta<2|\tau(K)|\le2g(K).
\]

Likewise, if the second candidate fails, then
\[
d_H<|s(K)|.
\]
Therefore
\[
d_\Delta<|s(K)|.
\]
Rasmussen's slice-genus bound and \(g_4(K)\le g(K)\) give
\[
|s(K)|\le2g_4(K)\le2g(K),
\]
so
\[
d_\Delta<|s(K)|\le2g(K).
\]

The Alexander polynomial of a knot is symmetric up to multiplication by a monomial, so its span \(d_\Delta\) is even. Hence a strict inequality \(d_\Delta<2g(K)\) implies
\[
d_\Delta\le2g(K)-2.
\]
This proves the defect bound.

If \(d_\Delta=2g(K)\), either failure would simultaneously force \(d_\Delta<2g(K)\), a contradiction. Thus both candidates hold on the Alexander-sharp class.

Finally, a classical theorem for fibered knots says that the Alexander polynomial is monic and has degree, equivalently span, exactly twice the genus. Therefore every fibered knot is Alexander-sharp and satisfies both candidate inequalities.

## Verification
The proof is symbolic. Its critical inputs were checked directly against the current source and standard primary references:

1. the recent source uses \(P_K(1,z)=\nabla_K(z)\), so \(d_H\ge d_\Delta\);
2. it records the universal bounds \(2g_4\ge2|\tau|\) and \(2g_4\ge|s|\);
3. the classical fibered-knot theorem gives \(d_\Delta=2g\) for fibered knots.

The bundled regression script checks the arithmetic implications and parity conclusion over a finite range. It prints:

`VERIFY_OK tuples=85305 tau_failure_tuples=10560 s_failure_tuples=10560`

That finite enumeration is not evidence for the infinite knot-theoretic premises; it only guards against an algebraic or packaging error in the displayed deductions.

## Relationship to prior work
Jabłonowski's 2026 paper formulates the two candidate inequalities
\[
2|\tau|\le\deg P_z,\qquad |s|\le\deg P_z
\]
and proves several family cases. Its current counterexample restriction states that failure of the first requires \(2|\tau|>|\sigma|\), while failure of the second requires \(|s|>|\sigma|\).

The present result replaces the signature threshold in this screening step by the Alexander span itself:
\[
2|\tau|>\operatorname{sp}\Delta_t
\]
or
\[
|s|>\operatorname{sp}\Delta_t,
\]
respectively. This follows because the Alexander polynomial is a HOMFLY–PT specialization. It also yields the genus-defect conclusion and the fibered-knot corollary in one step.

Targeted searches using the candidate formulas, Alexander span, fibered knots, \(\tau\), Rasmussen's \(s\), and HOMFLY–PT \(z\)-degree did not locate an earlier statement of this exact counterexample filter or the resulting Alexander-sharp family theorem. The closest inspected source is the 2026 paper itself, which states the signature-only necessary conditions.

## Limitations
This is a conditional obstruction, not a proof of the two universal candidate inequalities. Knots with positive Alexander genus defect remain possible counterexamples.

The Alexander-sharp condition is sufficient here but is not equivalent to fiberedness: there are nonfibered knots whose Alexander polynomial has span \(2g\). Thus the theorem applies beyond fibered knots, while making no fibering claim for the larger class.

A later revision of the recent preprint, or an unindexed note, could independently state the same Alexander-span filter.

## References
1. M. Jabłonowski, *Integer Knot Invariants: Inequalities, Computations, and Open Problems*, arXiv:2605.22652, first posted 2026-05-21; current text dated 2026-09-15.
2. P. Ozsváth and Z. Szabó, *Knot Floer homology and the four-ball genus*, Geometry & Topology 7 (2003), 615–639.
3. J. Rasmussen, *Khovanov homology and the slice genus*, Inventiones Mathematicae 182 (2010), 419–447.
4. S. Friedl and S. Vidussi, *Twisted Alexander polynomials detect fibered 3-manifolds*, Annals of Mathematics 173 (2011), 1587–1643; its abstract recalls the classical theorem that a fibered knot has Alexander degree twice its genus.
