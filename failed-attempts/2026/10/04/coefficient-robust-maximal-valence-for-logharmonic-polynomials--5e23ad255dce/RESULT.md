# Coefficient-robust maximal valence for logharmonic polynomials

## Finding

For every integer \(n>1\), let
\[
\mathcal P_n
=
\{(p,q):\deg p=n,\ \deg q=1\}
\]
with the Euclidean topology on the complex coefficients. There is a nonempty open set
\[
\mathcal U_n\subset\mathcal P_n
\]
such that, for every \((p,q)\in\mathcal U_n\), the fixed-target equation
\[
p(z)\overline{q(z)}=1
\]
has exactly \(3n-1\) distinct nonsingular solutions.

If
\[
F_{p,q}(z)=p(z)\overline{q(z)}-1,
\]
then throughout a sufficiently small such neighborhood its real Jacobian is positive at exactly \(2n-1\) roots and negative at exactly \(n\) roots.

After labeling the roots of one base extremizer, each root is a real-analytic function of all real and imaginary coefficients of \(p\) and \(q\) on a sufficiently small neighborhood. In particular, maximal \(3n-1\) valence is not a fine-tuned phenomenon: the extremal locus has nonempty interior in the full coefficient space at the fixed target \(1\).

## Assumptions and scope

The coefficient space is restricted to pairs for which
\[
\deg p=n,
\qquad
\deg q=1.
\]
The leading coefficients therefore remain nonzero after shrinking the coefficient neighborhood.

A solution \(z_0\) is called nonsingular when the real differential
\[
dF_{p,q}(z_0):\mathbb R^2\to\mathbb R^2
\]
is invertible. Its orientation is the sign of the determinant of this differential.

The theorem is local in coefficient space. It does not classify the entire maximal-valence locus, give a quantitative perturbation radius, or address \(\deg q>1\).

## Proof

The recent sharpness construction supplies, for every \(n>1\), a degree-\(n\) polynomial \(p_0\), a constant \(c\in\mathbb C\), and the anti-rational fixed-point equation encoded by
\[
H(z)
=
z-\overline c-\frac{1}{\overline{p_0(z)}}.
\]
The source proves that \(H\) has exactly \(3n-1\) zeros, all nonsingular. It also proves that exactly \(n\) of these zeros are orientation-preserving for \(H\), while the remaining \(2n-1\) are orientation-reversing.

Set
\[
q_0(z)=z-\overline c
\]
and
\[
F_0(z)=p_0(z)\overline{q_0(z)}-1.
\]
The zeros of \(F_0\) are exactly the zeros of \(H\), because
\[
F_0(z)=p_0(z)\overline{H(z)}.
\]
At a common zero \(z_0\), the term obtained by differentiating \(p_0\) vanishes because \(H(z_0)=0\). Hence
\[
dF_0(z_0)
=
p_0(z_0)\,d\overline H(z_0).
\]
Complex multiplication by \(p_0(z_0)\) has positive determinant \(|p_0(z_0)|^2\), while complex conjugation reverses orientation. Therefore
\[
\det dF_0(z_0)
=
-|p_0(z_0)|^2\det dH(z_0).
\]
Every zero of \(F_0\) is consequently nonsingular. The orientation counts are reversed from those of \(H\): \(F_0\) has exactly \(2n-1\) positive-Jacobian zeros and exactly \(n\) negative-Jacobian zeros.

Write all real and imaginary coefficients of \(p\) and \(q\) as a finite-dimensional real parameter vector \(\alpha\), and write
\[
G(\alpha,z)=p_\alpha(z)\overline{q_\alpha(z)}-1
\]
as a map into \(\mathbb R^2\). Let
\[
z_1,\ldots,z_{3n-1}
\]
be the distinct zeros at the base parameter \(\alpha_0\). Since the derivative in the \(z\)-variables is invertible at each \((\alpha_0,z_j)\), the real-analytic implicit-function theorem gives neighborhoods of \(\alpha_0\) and real-analytic branches
\[
z_j=z_j(\alpha)
\]
satisfying
\[
G(\alpha,z_j(\alpha))=0.
\]
Shrink the common coefficient neighborhood so that the branches remain pairwise distinct, all Jacobian determinants remain nonzero with the same signs, and the leading coefficients of \(p\) and \(q\) remain nonzero.

Every nearby pair therefore has at least \(3n-1\) solutions of the fixed equation
\[
p(z)\overline{q(z)}=1.
\]
The sharp general upper bound for degree \(n\) and linear \(q\) says that every target equation of this form has at most \(3n-1\) solutions. Hence no additional solutions can occur, and every pair in the chosen neighborhood has exactly \(3n-1\) solutions.

This proves openness of the maximal-valence locus and the stated orientation split.

## Verification

The proof requires no numerical experiment.

The key sign computation was checked directly:
\[
F_0=p_0\overline H,
\]
so at a zero of \(H\),
\[
dF_0=p_0\,d\overline H
\]
and therefore
\[
J_{F_0}=-|p_0|^2J_H.
\]
Thus the source counts \(n\) orientation-preserving and \(2n-1\) orientation-reversing zeros for \(H\) become \(2n-1\) positive and \(n\) negative Jacobians for the logharmonic equation.

The source explicitly proves nonsingularity of all zeros in its extremal construction. This is exactly the hypothesis needed for the real-analytic implicit-function theorem.

The global upper bound
\[
3n-1
\]
is essential: local continuation alone gives at least that many roots, while the upper theorem rules out creation of additional roots elsewhere.

## Relationship to prior work

Lazebnik and Lundberg prove sharpness of the upper bound by constructing, for each \(n>1\), one degree-\(n\) polynomial and one linear factor for which a target has \(3n-1\) preimages. Their proof also establishes that the corresponding anti-rational fixed points are all nonsingular. A remark in the same paper notes openness when the single construction parameter \(c\) is varied.

Khavinson, Lundberg, and Perry prove the general \(3n-1\) upper bound for a degree-\(n\) polynomial paired with a linear factor. They also prove a stability lemma in the target variable: for one fixed harmonic map, the set of target values with maximal preimage count is open.

Neither statement gives the conclusion above. Here the target is held fixed at \(1\), while all coefficients of both polynomials may vary simultaneously. The combination of nonsingularity, implicit continuation in the full coefficient vector, and the global upper bound produces a full-dimensional open set of extremizers.

## Limitations

No quantitative radius for the coefficient neighborhood is obtained.

The theorem does not classify connected components or the boundary of the maximal-valence locus. It also does not claim that every extremizer is nonsingular.

Only the linear-factor case \(\deg q=1\) is treated, because this is the setting in which the sharp global upper bound \(3n-1\) is available and known to be attained.

## References

1. K. Lazebnik and E. Lundberg, *Sharp bounds for the valence of certain logharmonic polynomials*, arXiv:2508.10151v1, 2025.
2. D. Khavinson, E. Lundberg, and S. Perry, *On the valence of logharmonic polynomials*, arXiv:2302.04339v2, 2025.
