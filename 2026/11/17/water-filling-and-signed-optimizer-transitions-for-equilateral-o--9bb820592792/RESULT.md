# Water-filling and signed-optimizer transitions for equilateral one-point Lipschitz extensions

## Finding

Let \(X=\{x_1,\ldots,x_n\}\), \(n\ge2\), have the equilateral metric \(d(x_i,x_j)=1\) for distinct points. Adjoin a point \(o\) with \(d(o,x_i)=r_i>0\), where the radii satisfy the metric conditions \(r_i+r_j\ge1\) and \(|r_i-r_j|\le1\) for all \(i\ne j\). Let \(E\) range over all bounded real-linear operators extending scalar Lipschitz functions on \(X\) to \(X\cup\{o\}\), with the Lipschitz seminorm as operator norm. These operators preserve constants and have unique coefficient representations
\[
(Ef)(o)=\sum_{i=1}^n w_i f(x_i),\qquad \sum_i w_i=1,
\]
with arbitrary real (possibly negative) coefficients.

Write \(r_{(1)}\le\cdots\le r_{(n)}\) for the ordered radii and define
\[
z=\max_{2\le k\le n}\frac{k-1}{\sum_{i=1}^k r_{(i)}},\qquad w_i^*=(1-zr_i)_+.
\]
Then \(\sum_i w_i^*=1\), and the **exact optimal operator norm** is
\[
\inf_E\|E\|=\max\{1,z\}.
\]
The vector \(w^*\) uniquely minimizes the new-point component of the norm, even among all signed coefficients.

The **full optimizer phase diagram** is:

1. If \(z\ge1\), \(w^*\) is the *unique* optimal extension coefficient vector. This includes the critical case \(z=1\).
2. If \(z<1\), the set of all optimal coefficient vectors is the full-dimensional (in the affine hyperplane \(\sum_iw_i=1\)) compact polytope
\[
\mathcal P_r=\left\{w\in\mathbb R^n:\sum_iw_i=1,\quad |1-w_i|+\sum_{j\ne i}|w_j|\le2r_i\quad(1\le i\le n)\right\}.
\]
Its affine dimension is \(n-1\). It contains a coefficient vector with a negative entry **if and only if** some \(r_i>1\). Thus \(z<1\) and \(\max_i r_i>1\) are the exact simultaneous conditions for signed optimal operators.

Equivalently, a norm-one extension exists exactly when every ordered prefix satisfies \(\sum_{i=1}^k r_{(i)}\ge k-1\) for \(2\le k\le n\). Strict inequalities for every prefix distinguish the full-dimensional phase from the unique critical operator. If \(\inf_E\|E\|>1\), at least three old points have positive optimal weights, since the two-point prefix constraint follows from the metric triangle inequality.

## Assumptions and scope

Everything is over real scalars. The operator acts on all scalar Lipschitz functions (equivalently, on pointed Lipschitz spaces after fixing the constant-representative convention). The radii are arbitrary positive real numbers satisfying the displayed necessary and sufficient metric inequalities. No general Banach-valued or multiple-new-point extension theorem is asserted. The operator norm is the ratio of Lipschitz seminorms, with the identity on \(X\).

## Proof

**Step 1: exact signed operator norm.** The zero-mass signed measure \(\delta_{x_i}-\sum_jw_j\delta_{x_j}\) on an equilateral metric has Kantorovich--Rubinstein norm equal to half its total variation. Consequently, with
\[
\phi_i(w)=\frac{|1-w_i|+\sum_{j\ne i}|w_j|}{2},
\]
one has
\[
\|E_w\|=\max\left\{1,\max_i\frac{\phi_i(w)}{r_i}\right\}.
\]
This is an equality because the extreme one-Lipschitz potentials on \(X\) are precisely the nonconstant two-level zero--one functions, modulo additive constants. The original-pair quotient contributes the initial \(1\).

**Step 2: strict removal of negative coefficients.** If some \(w_i<0\), let \(t=\sum_i(-w_i)_+>0\), so \(\sum_i(w_i)_+=1+t\), and define \(v_i=(w_i)_+/(1+t)\). Then \(v_i\ge0\), \(\sum_i v_i=1\), and **\(\phi_i(v)<\phi_i(w)\) for every \(i\)**. Indeed, when \(w_i<0\) the two values are \(1\) and \(1+t\); when \(0\le w_i\le1\), they are \(1-w_i/(1+t)\) and \(1+t-w_i\); when \(w_i\ge1\), they are \(1-w_i/(1+t)\) and \(t\), with strict inequality because \(w_i\ge1\). Thus every minimizer of \(\max_i\phi_i(w)/r_i\) is nonnegative.

**Step 3: sorted active-set formula and uniqueness.** For nonnegative weights summing to one, \(\phi_i(w)=1-w_i\). The inequalities \((1-w_i)/r_i\le u\) are feasible exactly when
\[
F(u)=\sum_i(1-ur_i)_+\le1.
\]
As \(F\) decreases continuously from \(n\) to \(0\), its equation \(F(z)=1\) has one positive solution. The identity
\[
F(u)=\max_{S\subseteq\{1,\dots,n\}}\left\{|S|-u\sum_{i\in S}r_i\right\}
\]
implies \(F(u)\le1\) exactly when \(u\ge(k-1)/\sum_{i=1}^k r_{(i)}\) for every \(2\le k\le n\). This proves the displayed explicit formula. At \(u=z\), each weight is bounded below by \((1-zr_i)_+\), whose sum already equals one; hence \(w^*\) is the unique minimizer. Step 2 rules out signed alternatives.

**Step 4: complete norm-one phase.** If \(z\ge1\), optimality of \(\|E\|=\max\{1,\max_i\phi_i/r_i\}\) forces the unique minimizer \(w^*\), including at \(z=1\). If \(z<1\), \(\phi_i(w^*)/r_i\le z<1\) for every \(i\), so a relative open neighborhood of \(w^*\) in \(\sum_iw_i=1\) is optimal. The inequalities defining \(\mathcal P_r\) give all optimal weights and show its compactness.

If any \(w_j<0\), the calculation in Step 2 gives \(\phi_j(w)=1+t>1\); hence its feasibility implies \(r_j>1\). Conversely, suppose \(z<1\) and \(r_j>1\). Then \(F(1)<1\) and the \(j\)-th summand in \(F(1)\) vanishes. Choose nonnegative weights with \(w_j=0\), sum one, and strict inequalities \(1-w_i<r_i\) for every \(i\), using the positive slack \(1-F(1)\) to increase all active lower-bound weights. Now decrease \(w_j\) slightly below zero and increase another coordinate by the same amount. All strict inequalities persist by continuity, yielding a signed norm-one extension.

## Verification

The accompanying `checker.py` evaluates the exact active-set formula using rational arithmetic and compares it against an independently formulated finite linear program. The LP enumerates all zero--one Lipschitz potentials as subsets and permits unrestricted signed coefficients, rather than building positivity into the optimization. Sixty rational attachment profiles of sizes \(2\) to \(6\) passed. The checker also tests strict negative-part normalization and explicit supercritical, critical and signed norm-one examples. Finite tests corroborate but do not replace Steps 1--4.

For example, radii \((1/2,1/2,1/2,3/2)\) give \(z=4/3\) and the unique optimal vector \((1/3,1/3,1/3,0)\). Radii \((1/2,1/2,3/2,3/2)\) give \(z=1\) and unique weights \((1/2,1/2,0,0)\). Radii \((3/5,3/5,3/2,3/2)\) give \(z<1\); the signed vector \((1/2,1/2,-1/20,1/20)\) is norm-one.

## Relationship to prior work

The underlying Lipschitz-free norm and random-projection representation are classical. Ambrosio--Puglisi develop strong and weak random projections and Kantorovich--Rubinstein tools; Bruè--Di Marino--Stra obtain general linear extension estimates for doubling subsets, without this sharp nonuniform one-point formula. Basso relates finite-space extension moduli to projection constants and provides general LP methods; the generic LP description does not directly state the ordered-prefix formula or signed-optimality transition here. A previously established equal-radius, cluster-based one-point formula covers the homogeneous-radius subcase, not unequal radii. This finding is claimed only for the complete nonuniform-radius equality-set classification, not for the general finite-dimensional reduction to linear programming or for the equiradial subcase.

## Limitations

This is an exact finite-metric result for the equilateral base, not a general arbitrary-metric classification. The method uses complete knowledge of all one-point radii; no universal extension factor or independence of the ambient metric is claimed. The analytic argument is elementary, though the simultaneous active-set, uniqueness and signed-phase classification is a separate natural exact problem. An overlooked equivalent formulation in weighted discrete optimal-transport or facility-location literature remains a priority risk. Independent mathematical validation has not been performed.

## References

1. L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (first posted 2016-09-06), §§1--2. [https://arxiv.org/abs/1609.01450](https://arxiv.org/abs/1609.01450).
2. E. Bruè, S. Di Marino and F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533 (first posted 2018-01-23), §§1, 3--4. [https://arxiv.org/html/1801.07533v1](https://arxiv.org/html/1801.07533v1).
3. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (first posted 2021-04-29), §§1, 5. [https://arxiv.org/abs/2104.14238](https://arxiv.org/abs/2104.14238).
