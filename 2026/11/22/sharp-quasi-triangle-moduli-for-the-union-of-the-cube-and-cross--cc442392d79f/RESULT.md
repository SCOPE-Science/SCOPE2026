# Sharp quasi-triangle moduli for the union of the cube and cross-polytope balls

## Finding
For each integer \(d\ge2\), scalar field \(\mathbb F\in\{\mathbb R,\mathbb C\}\), and \(t>0\), define the continuous absolutely homogeneous functional on \(\mathbb F^d\)
\[
q_{d,t}(x)=\min\{\|x\|_1,t\|x\|_\infty\}.
\]
Its **sharp binary quasi-triangle modulus** is
\[
K_d(t)=\sup_{q_{d,t}(x)+q_{d,t}(y)>0}\frac{q_{d,t}(x+y)}{q_{d,t}(x)+q_{d,t}(y)}
=\begin{cases}
1,&0<t\le1\ \text{or}\ t\ge d,\\
\displaystyle\frac{t(d-1)}{d-1+(t-1)^2},&1<t<d.
\end{cases}
\]
It is strictly greater than one precisely when \(1<t<d\). The unique maximizing parameter over all \(t>0\) is \(t=\sqrt d\), and
\[
\max_{t>0}K_d(t)=\frac{\sqrt d+1}{2}.
\]
Furthermore, if \(B_1^d\) and \(B_\infty^d\) denote the standard unit balls and \(h_{d,t}\) the Minkowski gauge of \(\operatorname{conv}(B_1^d\cup t^{-1}B_\infty^d)\), then the full convexification distortion also equals \(K_d(t)\):
\[
\sup_{x\ne0}\frac{q_{d,t}(x)}{h_{d,t}(x)}=K_d(t).
\]
For the infinite-dimensional vector space \(\ell_1(\mathbb N;\mathbb F)\), the same formula \(q_t(x)=\min\{\|x\|_1,t\|x\|_\infty\}\) has optimal binary quasi-triangle modulus \(K_\infty(t)=\max\{1,t\}\). For \(t>1\), the supremum \(t\) is never attained by a pair with positive denominator, but is approached by finitely supported pairs as their support grows.

## Assumptions and scope
The scalar field is real or complex, and all coordinate norms use absolute values. The parameter is any real \(t>0\); the sharp constants concern **two summands**, not arbitrarily many summands. The finite-dimensional assertion starts at \(d=2\). For \(d=1\), \(q_{1,t}=\min\{1,t\}|\cdot|\), which is a norm. The infinite-dimensional statement concerns the vector space \(\ell_1\) with the displayed quasi-norm, **not** a claim about its completeness or a quasi-Banach completion.

## Proof
**1. Endpoint norm regimes.** Since \(\|x\|_\infty\le\|x\|_1\le d\|x\|_\infty\), the functional is \(t\|\cdot\|_\infty\) for \(0<t\le1\) and \(\|\cdot\|_1\) for \(t\ge d\). Both have modulus one. We henceforth assume \(1<t<d\).

**2. Convexification norm and a sharp comparison.** The unit ball of \(q_{d,t}\) is exactly \(B_1^d\cup t^{-1}B_\infty^d\). Let \(h=h_{d,t}\) be the gauge of its convex hull. This is a norm and satisfies \(h(x)\le q_{d,t}(x)\) for all \(x\). By polar duality,
\[
h(x)=\sup\{\operatorname{Re}\langle x,z\rangle:\|z\|_\infty\le1,\ \|z\|_1\le t\}.
\]
Set \(c=(t-1)/(d-1)\), so \(0<c<1\). For each nonzero \(x\), choose an index \(j\) where \(|x_j|=M=\|x\|_\infty\). Choose \(z_j\) of modulus one with \(\operatorname{Re}(x_j\overline{z_j})=|x_j|\) and for all other coordinates choose \(z_i\) of modulus \(c\) with aligned phases. Then \(\|z\|_\infty=1\), \(\|z\|_1=1+(d-1)c=t\), whence
\[
h(x)\ge M+c(\|x\|_1-M).
\]
Writing \(r=\|x\|_1/M-1\in[0,d-1]\), one gets
\[
\frac{q_{d,t}(x)}{h(x)}\le\frac{\min\{1+r,t\}}{1+cr}\le\frac{t}{1+c(t-1)}
=\frac{t(d-1)}{d-1+(t-1)^2}=:K.
\]
The middle ratio is strictly increasing in \(r\) until \(r=t-1\), then strictly decreasing, since \(0<c<1\). Thus \(q_{d,t}\le Kh\), and, because \(h\) is subadditive and \(h\le q_{d,t}\),
\[
q_{d,t}(x+y)\le K h(x+y)\le K\bigl(h(x)+h(y)\bigr)\le K\bigl(q_{d,t}(x)+q_{d,t}(y)\bigr).
\]

**3. Sharp two-vector witness and exact convexification.** Put \(u=(1-c)e_1\) and \(v=c(1,1,\ldots,1)\). The two vectors are nonzero, \(q_{d,t}(u)=1-c\), and \(q_{d,t}(v)=tc\), because \(t<d\). The sum \(w=u+v=(1,c,\ldots,c)\) obeys \(\|w\|_1=t\), \(\|w\|_\infty=1\); hence \(q_{d,t}(w)=t\), so
\[
\frac{q_{d,t}(w)}{q_{d,t}(u)+q_{d,t}(v)}
=\frac{t}{1+(t-1)c}=K.
\]
Moreover \(h(w)\le h(u)+h(v)\le q(u)+q(v)\), while the bound from Step 2 gives \(h(w)\ge 1+(t-1)c\). Thus \(h(w)=1+(t-1)c\) and the convexification distortion is also exactly \(K\).

**4. Optimal scaling parameter.** Direct differentiation yields
\[
\operatorname{sgn}K_d'(t)=\operatorname{sgn}(d-t^2),\qquad1<t<d.
\]
The unique maximum is at \(t=\sqrt d\), where substitution gives \((\sqrt d+1)/2\). Endpoint moduli equal one, so the global maximum is unique.

**5. Infinite-dimensional sharpness and nonattainment.** On \(\ell_1(\mathbb N;\mathbb F)\), for \(t\le1\) the functional is \(t\|\cdot\|_\infty\), hence has modulus one. For \(t>1\), \(q_t(a)\ge\|a\|_\infty\), and therefore
\[
q_t(x+y)\le t\|x+y\|_\infty\le t\bigl(\|x\|_\infty+\|y\|_\infty\bigr)\le t\bigl(q_t(x)+q_t(y)\bigr).
\]
For each integer \(d>t\), the finitely supported witness of Step 3 has ratio \(K_d(t)\to t\), proving the sharp value. Suppose \(t>1\) and equality in the displayed upper bound held for a pair of nonzero vectors. Then \(q_t(x)=\|x\|_\infty\) and \(q_t(y)=\|y\|_\infty\), which (because \(t>1\)) forces each to be supported on exactly one coordinate. Equality in the sup-norm triangle inequality would require those supports to coincide. But then their sum is supported on one coordinate, so \(q_t(x+y)=\|x+y\|_\infty\), strictly below \(t(q_t(x)+q_t(y))\) (or zero). The case of a zero summand has quotient one. Thus the infinite-dimensional sharp modulus is not attained for \(t>1\).

## Verification
The standalone standard-library-only script `check.py` performs exact-rational checks of sharp finite-dimensional witness identities and the quasi-triangle and convexification inequalities for dimensions \(2\) through \(8\), including parameter values in and outside the nonconvex regime. It checks the fractional-ordered-coordinate expression for the convexified gauge and uses reproducible rational sample vectors. The observed diagnostic is `QUASINORM_CUBE_CROSSPOLYTOPE_CHECK_OK 88221`. This is supporting finite testing only; the proof above establishes the infinite quantified statements.

## Relationship to prior work
Unser, *Quasi-norms on R^d: Characterization and Approximation by Conic Splines* (arXiv:2611.06212v1, first posted 4 November 2026), Definition 2.3 and Theorem 2.4, identifies the quasi-triangle modulus and gives a general norm-comparison upper bound. Its Appendix A addresses arbitrary vector spaces, and Appendix B treats the \(\ell_p\) quasi-norm. It does not state the modulus of this minimum-of-two-norms family, the sharp cube–cross-polytope convexification equality, the optimizing scale, or the infinite nonattainment law. Malčeski's *Sharp Triangle Inequalities in Quasi-Normed Spaces* (2015), Theorems 2–4, establishes general inequalities conditional on a given modulus, not its explicit computation for this family. Barza, Kolyada, and Soria (2007) address Lorentz quasi-norms with different defining functionals. Separately, published work on cube–cross-polytope **intersections** studies different norm-geometric constants, not the gauge of their **union** or this sharp quasi-triangle modulus. No stronger implication covering the displayed family was identified in the inspected literature.

## Limitations
No classification of all extremizer pairs is asserted; the exhibited pair proves sharpness. The infinite-dimensional assertion is about \(\ell_1\) as a vector space, whose topology under this quasi-norm is that of \(\ell_\infty\) restricted to \(\ell_1\); it is not asserted to be complete. No claims are made for general unions of arbitrary norm balls, arbitrary-summand constants, or applications to reconstruction algorithms. Unindexed equivalent treatments of the cube–cross-polytope union remain a bibliographic risk.

## References
- M. Unser, *Quasi-norms on R^d: Characterization and Approximation by Conic Splines*, arXiv:2611.06212v1, first publicly posted 2026-11-04. https://arxiv.org/html/2611.06212v1
- R. Malčeski, *Sharp Triangle Inequalities in Quasi-Normed Spaces*, British Journal of Mathematics & Computer Science **7** (2015), 258–265, https://doi.org/10.9734/BJMCS/2015/15579
- S. Barza, V. Kolyada, J. Soria, *Sharp constants related to the triangle inequality in Lorentz spaces*, arXiv:0709.0647, 2007. https://arxiv.org/abs/0709.0647
