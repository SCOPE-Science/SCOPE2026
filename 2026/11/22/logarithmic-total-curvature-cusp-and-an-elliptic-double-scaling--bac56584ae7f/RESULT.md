# Logarithmic total-curvature cusp and an elliptic double-scaling law for torus knots

## Finding
For integers \(p,q\) satisfying \(2\le p<q\), \(\gcd(p,q)=1\), let the standard unit-major-radius torus knot be
\[
\gamma_{p,q,r}(t)=((1+r\cos(qt))\cos(pt),\ (1+r\cos(qt))\sin(pt),\ r\sin(qt)),\quad 0\le t\le 2\pi,\quad 0<r<1.
\]
Its **total absolute curvature** is
\[
T_{p,q}(r)=\int_0^{2\pi}\frac{\|\gamma'_{p,q,r}(t)\times\gamma''_{p,q,r}(t)\|}{\|\gamma'_{p,q,r}(t)\|^2}\,dt.
\]
The zero-curvature/inflection radius \(r_*=p^2/(p^2+q^2)\), and its exactly \(q\) inflection points, are **previously established** by Fuller (1998), not new findings here.

**New sharp fixed-winding cusp.** The function \(T_{p,q}\) is real analytic for \(0<r<1\), \(r\ne r_*\), and continuously differentiable on \((0,1)\), but not twice differentiable at \(r_*\). For \(\delta\to0\) through nonzero real values,
\[
T_{p,q}(r_*+\delta)=T_{p,q}(r_*)+T'_{p,q}(r_*)\delta+C_{p,q}\delta^2\log(1/|\delta|)+O_{p,q}(\delta^2),
\qquad C_{p,q}=\frac{(p^2+q^2)^4}{p^3q^2(2p^2+q^2)}>0.
\]
Thus a known curvature-zero contact manifests as a logarithmically divergent second radial derivative of the **integrated** curvature.

**New high-winding crossover.** Fix \(p\ge2\) and \(L>0\), and take \(q\to\infty\) through coprime integers, with \(r=\lambda p^2/q^2\) and \(0<\lambda\le L\) (also allowing the limit at \(\lambda=0\)). Uniformly in this range,
\[
T_{p,q}(\lambda p^2/q^2)=pF(\lambda)+O_{p,L}(q^{-1}),\quad
F(\lambda)=\int_0^{2\pi}\sqrt{1+2\lambda\cos u+\lambda^2}\,du.
\]
Equivalently, with \(E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2v}\,dv\),
\[
F(\lambda)=4(1+\lambda)E\left(\frac{2\sqrt\lambda}{1+\lambda}\right).
\]
The profile is strictly increasing for \(\lambda>0\), strictly convex for \(\lambda\ge0\), and satisfies \(F(0)=2\pi\), \(F(1)=8\), \(F(\lambda)=\lambda F(1/\lambda)\). Moreover,
\[
F(1+\eta)=8+4\eta+\eta^2\left[\log(8/|\eta|)-\frac12\right]+o(\eta^2).
\]
Consequently, the measured renormalized total curvature \(T/p\) identifies the scaled tube radius \(\lambda\) uniquely in the limiting regime. The transition is centered at the same scale as Fuller's known inflection radius, \(r_*\sim p^2/q^2\).

## Assumptions and scope
Lengths have been normalized by the major torus radius; total curvature is invariant under a global spatial dilation. All norms and cross products are Euclidean in \(\mathbb R^3\). Both \(p,q\) are fixed in the first assertion; \(p\) is fixed and \(q\) varies in the second. The \(\lambda=0\) assertion refers only to the continuous extension: the actual \(r=0\) curve has repeated covering and is not a torus knot. There is no claim about arbitrary embeddings of the same knot type.

## Proof
Set \(u=qt\), \(c=\cos u\), \(s=\sin u\), and use the rotating cylindrical orthonormal basis \((e_r,e_\phi,e_z)\). The velocity and acceleration have components
\[
v=(-rq s,\ p(1+rc),\ rq c),\quad
a=(-p^2(1+rc)-rq^2c,\ -2prq s,\ -rq^2s).
\]
Since the scalar integrand is periodic in \(u\), the \(q\) fundamental periods cancel the Jacobian \(dt=du/q\), and
\[
T_{p,q}(r)=\int_0^{2\pi} H_{p,q}(r,u)\,du,\quad
H_{p,q}(r,u)=\frac{\|v\times a\|}{v\cdot v}.
\]
For \(0<r<1\), \(v\ne0\): indeed \(v_\phi=p(1+rc)>0\). Furthermore,
\[
(v\times a)_r=-prq^2s(1-rc).
\]
A zero therefore requires \(s=0\). At \(c=1\) the radial acceleration is strictly negative. At \(c=-1\), it equals \((p^2+q^2)r-p^2\), so the sole zeros occur at \(r=r_*\), \(u=\pi\). This recovers, but does not newly claim, Fuller's inflection classification.

For the critical asymptotic let \(D=p^2+q^2\), \(x=u-\pi\), and \(\delta=r-r_*\), and put
\[
V^2=p^2(1-r_*)^2+r_*^2q^2,\quad A=DV,\quad B=pr_*q^2(1+r_*).
\]
At \((x,\delta)=(0,0)\) the vector \(v\times a\) vanishes. Its parameter derivative \(\partial_\delta(v\times a)\) has length \(A\), is tangent to the span of \(e_\phi,e_z\), whereas \(\partial_x(v\times a)\) has length \(B\) and points along \(e_r\). They are orthogonal. Hence
\[
\|v\times a\|^2=A^2\delta^2+B^2x^2+O_{p,q}((|x|+|\delta|)^3),\quad
v\cdot v=V^2+O_{p,q}(|x|+|\delta|).
\]
This nondegenerate quadratic normal form is sufficient for the leading logarithmic coefficient, but the remainder estimate requires a localized argument rather than taking a square root of a global Taylor remainder. In a fixed small neighborhood of \(x=0\), analytic completion of the square (the one-dimensional parameterized Morse lemma) changes the \(x\) coordinate smoothly, with Jacobian \(1+O(|x|+|\delta|)\), and reduces the numerator to a positive smooth multiplier times \(\sqrt{B^2y^2+(A^2+O(\delta))\delta^2}\). The denominator and coordinate Jacobian likewise have a positive smooth expansion. The only nonanalytic second-order term is obtained from
\[
\int_{-h}^{h}\sqrt{B^2y^2+A^2\delta^2}\,dy
=\text{a smooth function through first order}+\frac{A^2}{B}\delta^2\log(1/|\delta|)+O(\delta^2),
\]
with \(h>0\) fixed. Terms involving nonconstant smooth weights have no additional second-order logarithmic term; odd leading terms cancel and the remaining weighted errors are \(O(\delta^2)\). Away from \(u=\pi\), the integrand is real analytic in \(r\). Dividing by \(V^2\) gives the announced coefficient
\[
\frac{A^2}{BV^2}=\frac{D^2}{B}=\frac{D^4}{p^3q^2(2p^2+q^2)}.
\]
Differentiability follows either by differentiating the smooth-norm integral with a dominated first derivative or from the displayed local normal form. The positive logarithmic term makes the second derivative diverge, so \(T\) is not \(C^2\).

For the double-scaling regime set \(r=\lambda p^2/q^2\), \(0\le\lambda\le L\). In the moving frame, uniformly in \(u\) and \(\lambda\),
\[
v=p e_\phi+O_{p,L}(q^{-1}),\quad
 a=-p^2(1+\lambda\cos u)e_r-p^2\lambda\sin u\,e_z+O_{p,L}(q^{-1}).
\]
The norm is globally Lipschitz, including at the critical zero \(\lambda=1\), and the velocity denominator is uniformly bounded away from zero. Thus
\[
H_{p,q}(\lambda p^2/q^2,u)
=p\sqrt{1+2\lambda\cos u+\lambda^2}+O_{p,L}(q^{-1})
\]
uniformly, proving the integral limit. Factoring the radicand as \((1+\lambda)^2[1-k^2\sin^2(u/2)]\) gives the complete elliptic integral. Differentiating under the integral for \(\lambda\ne1\) gives
\[
F''(\lambda)=\int_0^{2\pi}\frac{\sin^2u}{(1+2\lambda\cos u+\lambda^2)^{3/2}}\,du>0.
\]
Continuity across \(\lambda=1\) implies strict global convexity. Symmetry forces \(F'(0)=0\), hence strict increase on \((0,\infty)\). The symmetry \(F(\lambda)=\lambda F(1/\lambda)\) is immediate. Lastly, the classical logarithmic endpoint expansion
\[
E(k)=1+\frac{k'^2}{2}\left(\log\frac4{k'}-\frac12\right)+O(k'^4\log(1/k')),\quad k'=\sqrt{1-k^2}\downarrow0,
\]
with \(k'=|\lambda-1|/(1+\lambda)\), proves the displayed \(F(1+\eta)\) cusp. It is also consistent with the fixed-winding coefficient: \(p^3C_{p,q}/q^4\to1\).

## Verification
`checker.py` is standalone Python 3 with standard library only. Run `python checker.py` from the extracted package. It checks the rotating-frame cross-product against numerical finite differences of its local parameters, the exact normal-form coefficient at multiple coprime windings, positive curvature away from the singular point, the uniform high-winding approximation, elliptic symmetry, and the singular profile expansion. All checks are finite diagnostics; the exact infinite statements are proved above, not inferred from numerical tests.

## Relationship to prior work
Edgar J. Fuller, *Torus Curves With Vanishing Curvature* (1998), Theorem 2.1, already proves the unique radius \(p^2/(p^2+q^2)\) and exactly \(q\) curvature-zero points. This is a central **premise and credited result**, not part of the asserted novelty. Oberti and Ricca, *On torus knots and unknots* (2016), Sections 3 and 4.2, reproduce the critical inflection configuration and investigate total curvature numerically as a function of winding for fixed torus aspect ratio, including their general integral formula (4.7). Their stated comparisons do not evaluate the singular \(C^1\)-versus-\(C^2\) behavior as the radius passes its critical value, nor the double-scaling \(r\asymp p^2/q^2\) elliptic profile with an explicit uniform error. Gerlach, Reiter and von der Mosel, *The elastic trefoil is the twice covered circle* (2015), use the same curve parametrization and fixed-winding small-radius bending-energy estimates; the estimates' constants depend on the winding numbers and do not imply a joint high-frequency total-curvature limit or its logarithmic cusp. Sullivan, *Curves of Finite Total Curvature* (2006), provides the general theory and context. These comparisons are evidence of a distinct statement, not a universal originality certificate.

## Limitations
Only the standard circular-torus parametrization, its Euclidean total absolute curvature, and the specified limits are treated. The inflection classification was already published in 1998. The result neither minimizes total curvature among representatives of a knot type nor identifies knot energy minimizers. The uniform error is asserted for bounded scaled radii with fixed longitudinal winding, not for simultaneously growing \(p\). The claimed originality of the two integrated-curvature laws remains conditional on independent historical assessment; other literature might contain an equivalent formulation. Numerical tests alone cannot establish the asymptotic or the originality.

## References
- E. J. Fuller, *Torus Curves With Vanishing Curvature*, 1998, arXiv:math/9803021, https://arxiv.org/abs/math/9803021 (first public submission March 6, 1998; primary differential geometry classification).
- C. Oberti and R. L. Ricca, *On torus knots and unknots*, *Journal of Knot Theory and Its Ramifications* **25** (2016), 1650036, https://doi.org/10.1142/S021821651650036X (open text: https://boa.unimib.it/bitstream/10281/135485/1/2016%20ObertiRicca%20JKTR.pdf).
- H. Gerlach, P. Reiter and H. von der Mosel, *The elastic trefoil is the twice covered circle*, 2015 preprint, arXiv:1510.06171, https://arxiv.org/abs/1510.06171.
- J. M. Sullivan, *Curves of Finite Total Curvature*, 2006 preprint, arXiv:math/0606007, https://arxiv.org/abs/math/0606007.
