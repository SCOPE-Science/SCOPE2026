# Scalar proximal-semigroup rigidity and a sharp one-kink composition defect

## Finding

Let \(f:\mathbb R\to\mathbb R\) be an everywhere finite convex function, and define its Euclidean proximal maps, for \(t\geq0\), by
\[
P_t^f(x)=\operatorname*{argmin}_{z\in\mathbb R}
\left\{\tfrac12(z-x)^2+t f(z)\right\}.
\]
The minimizer is unique. The following statements are equivalent:

1. \(P_s^f(P_t^f(x))=P_{s+t}^f(x)\) for every \(x\in\mathbb R\) and all \(s,t\geq0\).
2. Either \(f\) is affine, or there are finite \(c\leq d\), coefficients \(\alpha,\beta\geq0\), and \(C\in\mathbb R\) such that
\[
f(x)=C+\alpha(c-x)_++\beta(x-d)_+,
\qquad (u)_+=\max\{u,0\}.
\]

Thus every nonaffine finite scalar convex penalty with exactly time-additive proximal maps is a possibly asymmetric distance-type penalty to a closed minimizer interval (including ray-valued minimum sets when a coefficient vanishes).

There is also an exact quantitative obstruction for the basic nonminimizing kink. For \(a\leq b\), set \(h(x)=a x+(b-a)(x)_+\), and for \(s,t\geq0\) let
\[
\Delta_{s,t}(h)=\sup_{x\in\mathbb R}
\left|P_s^h(P_t^h(x))-P_{s+t}^h(x)\right|.
\]
Then
\[
\Delta_{s,t}(h)=
\begin{cases}
0,&a\leq0\leq b,\\
\min\{s a,t(b-a)\},&0<a\leq b,\\
\min\{s(-b),t(b-a)\},&a\leq b<0.
\end{cases}
\]
In the second case \(x=t b\) attains the supremum; in the third case \(x=t a\) attains it. The formula includes degenerate endpoints \(s=0\), \(t=0\), and \(a=b\).

## Assumptions and scope

All spaces and variables are real. Finite convex functions are continuous, differentiable almost everywhere, and have monotone one-sided derivatives. No coercivity or attainment of \(\inf f\) is assumed in the classification. All proximal maps are the quadratic-fidelity maps shown above; the time parameter multiplies the penalty rather than its quadratic term. The classification does not claim to cover extended-valued convex penalties, dimensions above one, nonconvex penalties, or approximate time-additivity.

## Proof

**1. Optimality and a rigidity lemma.** The unique proximal point satisfies
\[
z=P_t^f(x)\quad\Longleftrightarrow\quad x-z\in t\,\partial f(z)
\]
for \(t>0\). Assume the semigroup identity. Take a point \(z\) at which \(f\) is differentiable and write \(p=f'(z)\ne0\). For arbitrary \(s,t>0\), set \(x=z+(s+t)p\). Optimality gives \(P_{s+t}^f(x)=z\). The semigroup law and the singleton subdifferential \(\partial f(z)=\{p\}\) force
\[
P_t^f(x)=z+s p,
\]
since \(P_s^f(P_t^f(x))=z\) implies \(P_t^f(x)-z=s p\). Applying optimality to the inner step yields
\[
p\in\partial f(z+s p)\qquad(s>0).
\]
If \(p>0\), every point of \((z,\infty)\) therefore has the same supporting slope \(p\). The two subgradient inequalities at two such points force \(f\) to be affine with slope \(p\) on that entire ray. If \(p<0\), the identical argument gives affine slope \(p\) on \(( -\infty,z)\).

**2. Classification necessity.** At differentiability points, \(f'\) is nondecreasing. The previous lemma says every positive derivative value propagates unchanged to the right, while every negative value propagates unchanged to the left. In particular there can be at most one strictly positive derivative value and at most one strictly negative derivative value. Wherever neither sign occurs, the derivative is zero almost everywhere, hence \(f\) is constant there (finite convex functions are locally absolutely continuous). Therefore either \(f'\) has one constant value almost everywhere, so \(f\) is affine, or the line is partitioned, in order, into an optional constant-slope negative ray, an optional zero-slope interval, and an optional constant-slope positive ray. The zero-slope region may collapse to one point; it may be unbounded when only one nonzero sign occurs. Continuity and integration of the slopes give exactly the representation in item 2, with finite \(c\leq d\) chosen at the boundaries. The affine case includes any nonzero constant slope.

**3. Classification sufficiency.** For \(f(x)=C+\alpha(c-x)_++\beta(x-d)_+\), with \(\alpha,\beta\geq0\) and \(c\leq d\), direct optimality gives
\[
P_t^f(x)=
\begin{cases}
\min\{c,x+t\alpha\},&x<c,\\
x,&c\leq x\leq d,\\
\max\{d,x-t\beta\},&x>d.
\end{cases}
\]
Thus the two exterior rays translate toward their respective endpoints and stop on reaching them; the interval is fixed. Composition adds the travel times, which proves the semigroup law, including the zero-weight cases. For an affine \(f(x)=A x+B\), \(P_t^f(x)=x-t A\), so the law also follows.

**4. Exact one-kink defect.** Subgradient optimality for \(h(x)=a x+(b-a)(x)_+\) gives
\[
P_t^h(x)=\begin{cases}
x-t a,&x<t a,\\
0,&t a\leq x\leq t b,\\
x-t b,&x>t b.
\end{cases}
\]
For \(a\leq0\leq b\) this is the previous interval model with \(c=d=0\), so its defect vanishes. Suppose \(0<a\leq b\). The composite map \(P_s^h\circ P_t^h\), in successive input intervals, equals
\[
\begin{cases}
x-(s+t)a,&x\leq t a,\\
-s a,&t a\leq x\leq t b,\\
x-t b-s a,&t b\leq x\leq t b+s a,\\
0,&t b+s a\leq x\leq t b+s b,\\
x-(s+t)b,&x\geq t b+s b.
\end{cases}
\]
Compare this with the three-branch direct formula for \(P_{s+t}^h\), whose breakpoints are \((s+t)a\) and \((s+t)b\). The difference is nonpositive, vanishes outside the region between \(t a\) and \(t b+s a\), and its minimum is \(-\min\{s a,t(b-a)\}\), attained at \(x=t b\). If \(a\leq b<0\), reflect \(x\mapsto-x\), which changes the slopes to \(-b,-a>0\), and obtain the third branch and its stated witness. This proves the sharp formula.

## Verification

Run `python3 verify_scalar_prox.py` using the Python standard library only. The script uses exact rational arithmetic to compare the sharp defect against all breakpoints of the relevant piecewise-affine compositions for a grid of slope pairs and times; it also checks interval-model semigroups and affine cases. A successful run reports `PASS 16529 exact rational checks`. These checks supplement, but do not replace, the all-parameter proof above. In particular, finite grids cannot establish the universal classification.

## Relationship to prior work

The resolvent characterization \(P_t^f=(I+t\partial f)^{-1}\) and general nonlinear-semigroup theory are established. Bungert, Burger, Chambolle, and Novaga (arXiv:1901.06979, initial public version 2019-01-21) analyze sufficient spectral/gradient-flow equivalences for absolutely one-homogeneous functionals; their Section 4.2 treats a different scope. Planiden and Wang (arXiv:1909.05795) give explicit proximal mappings for single-variable piecewise-cubic functions, but do not state the all-convex scalar semigroup classification or the optimized sharp one-kink time-composition defect. Combettes (arXiv:2209.06200) studies proximal *composition with a linear operator*, which differs from composition of two parameter-scaled proximal maps. These works provide context and established tools, not the necessity argument above.

## Limitations

The theorem applies only to finite convex functions on the full real line; indicator penalties and multivariate prox operators may exhibit additional semigroup families. The sharp kink formula controls the supremum over inputs for one two-slope penalty, not for general piecewise-linear or smoothly curved functions. The derivations have been reviewed within this package but have not received independent mathematical validation. Historical priority remains uncertain where scalar monotone-resolvent graph classifications may be recorded under different terminology.

## References

1. L. Bungert, M. Burger, A. Chambolle, and M. Novaga, *Nonlinear Spectral Decompositions by Gradient Flows of One-Homogeneous Functionals*, arXiv:1901.06979 (initially public 2019-01-21), https://arxiv.org/abs/1901.06979.
2. C. Planiden and X. Wang, *Proximal mappings and Moreau envelopes of single-variable convex piecewise cubic functions and multivariable gauge functions*, arXiv:1909.05795 (initially public 2019-09-11), https://arxiv.org/abs/1909.05795.
3. P. L. Combettes, *Resolvent and Proximal Compositions*, arXiv:2209.06200 (initially public 2022-09-13), https://arxiv.org/abs/2209.06200.
4. H. Brézis, *Opérateurs maximaux monotones et semi-groupes de contractions dans les espaces de Hilbert*, North-Holland, 1973 (foundational background).
