# Exact Cauchy reduction of the incommensurate Kagome spectral-density constant
## Finding
For the incommensurate Kagome quantum graph with preferred-orientation coupling studied by Baradaran and Exner, take edge lengths \(b,c>0\) with \(b/c\notin\mathbb Q\) and set \(d=b+c\). Their high-energy band criterion is the sign condition
\[
\left(2\cos\frac{k(c-2d)}2+\cos\frac{kc}2\right)
\left(\cos\frac{k(c-d)}2+2\cos\frac{k(c+d)}2\right)
\left(\cos\frac{k(2c-d)}2+2\cos\frac{kd}2\right)\ge0.
\]
They evaluate the corresponding incommensurate density numerically as approximately \(0.639081\). The sign region admits an exact reduction. Put \(u=kb/2\), \(v=kc/2\), \(X=\tan u\), and \(Y=\tan v\). Then, away from the measure-zero tangent poles, the criterion is exactly
\[
(3-XY)(3-X^2-4XY)(3-Y^2-4XY)\ge0.
\]
Because the irrational flow \(k\mapsto(u,v)\bmod\pi\) is equidistributed on the two-torus, \(X\) and \(Y\) have the independent standard Cauchy law for the purpose of the density calculation.

Let
\[
x_0=\sqrt{\frac35},\qquad r_A(x)=\frac3x,\qquad r_B(x)=\frac{3-x^2}{4x},\qquad c_\pm(x)=-2x\pm\sqrt{4x^2+3}.
\]
For every \(x>0\), the set of \(y\) satisfying the polynomial inequality is
\[
(c_-(x),c_+(x))\cup(r_B(x),r_A(x)),\qquad 0<x<x_0,
\]
and
\[
(c_-(x),r_B(x))\cup(c_+(x),r_A(x)),\qquad x>x_0.
\]
Using the Cauchy density and the symmetry \((x,y)\mapsto(-x,-y)\), the universal density is therefore
\[
P=\frac{2}{\pi^2}\left[\int_0^{x_0}\frac{\pi-\arctan\sqrt{4x^2+3}+\arctan x}{1+x^2}\,dx
+\int_{x_0}^\infty\frac{\arctan(3/x)+\arctan((3-x^2)/(4x))+\arctan x}{1+x^2}\,dx\right].
\]
A deterministic numerical evaluation gives
\[
P=0.6390804227921295\ldots,
\]
consistent with, and substantially sharpening, the published value \(0.639081\).

## Assumptions and scope
The statement concerns the source's incommensurate Kagome model with the same preferred-orientation vertex condition, positive edge lengths \(b,c\), and \(b/c\notin\mathbb Q\). It evaluates the universal high-energy density determined by the source's leading band condition (3.13). Flat-band momenta and tangent poles form sets of zero density and do not affect the value. The proof does not claim an elementary closed form for the final one-dimensional integral.

## Proof
Write \(u=kb/2\) and \(v=kc/2\). Since \(d=b+c\), the three factors of the source criterion become
\[
2\cos(2u+v)+\cos v,\qquad \cos u+2\cos(u+2v),\qquad \cos(v-u)+2\cos(u+v).
\]
On a fundamental square \((-\pi/2,\pi/2)^2\), put \(x=\tan u\) and \(y=\tan v\). Direct trigonometric reduction gives
\[
2\cos(2u+v)+\cos v=\frac{3-x^2-4xy}{(1+x^2)\sqrt{1+y^2}},
\]
\[
\cos u+2\cos(u+2v)=\frac{3-y^2-4xy}{\sqrt{1+x^2}(1+y^2)},
\]
and
\[
\cos(v-u)+2\cos(u+v)=\frac{3-xy}{\sqrt{(1+x^2)(1+y^2)}}.
\]
Their product is the polynomial \(Q(x,y)=(3-xy)(3-x^2-4xy)(3-y^2-4xy)\) divided by the strictly positive denominator \((1+x^2)^2(1+y^2)^2\). Thus the sign is exactly the sign of \(Q\).

Fix \(x>0\). The three factors vanish at
\[
r_A=\frac3x,\qquad r_B=\frac{3-x^2}{4x},\qquad c_\pm=-2x\pm\sqrt{4x^2+3}.
\]
One always has \(c_-<r_A\), \(c_-<r_B<r_A\), and \(c_+<r_A\). The only root-order transition occurs when \(r_B=c_+\). Equivalently, substituting \(r_B\) into \(3-y^2-4xy\) gives
\[
\frac{3(x^2+1)(5x^2-3)}{16x^2},
\]
so the transition is exactly \(x=x_0=\sqrt{3/5}\). Starting from \(y\to-\infty\), where \(Q<0\), and alternating signs across the simple roots gives the two interval decompositions in the finding.

The original sign product is \(\pi\)-periodic in each of \(u\) and \(v\). Since \(b/c\) is irrational, Kronecker--Weyl equidistribution makes \((u,v)\bmod\pi\) uniform on the torus. Under \(x=\tan u\), the push-forward of normalized Lebesgue measure is the standard Cauchy density \(dx/(\pi(1+x^2))\), independently in the two coordinates. Integrating the Cauchy mass of the allowed \(y\)-intervals and using \(Q(-x,-y)=Q(x,y)\) gives the prefactor \(2/\pi^2\).

For \(0<x<x_0\), the conditional angular length simplifies to
\[
\arctan c_+-\arctan c_-+\arctan r_A-\arctan r_B
=\pi-\arctan\sqrt{4x^2+3}+\arctan x.
\]
For \(x>x_0\), it simplifies to
\[
\arctan r_B-\arctan c_-+\arctan r_A-\arctan c_+
=\arctan(3/x)+\arctan((3-x^2)/(4x))+\arctan x.
\]
Substitution yields the displayed exact integral.

## Verification
The bundled `verify.py` checks the trigonometric-to-polynomial identity on a deterministic grid, checks the two root-order regimes on representative values, and evaluates the exact one-dimensional integral by composite Simpson quadrature after the substitution \(x=\tan t\). It prints `VERIFY_OK` and reproduces \(0.63908042279213\) stably under mesh refinement. These numerical checks corroborate the algebra and decimal evaluation; the proof of the exact integral is analytic and does not rely on finite sampling.

## Relationship to prior work
Baradaran and Exner derive the high-energy sign condition and state that, for incommensurate edge lengths, its sign-region area gives a universal density approximately \(0.639081\). They explicitly describe the rewritten inequality as too complicated to solve and evaluate the area numerically. The present result gives an exact algebraic sign reduction, a complete one-parameter root-order classification, and an exact one-dimensional integral for the same constant.

Band and Berkolaiko establish the general momentum-band-density viewpoint and generic length-independence for periodic Kirchhoff networks. Their theorem does not contain the preferred-orientation Kagome sign polynomial, its Cauchy representation, or the explicit integral above.

## Limitations
No claim is made that the one-dimensional integral reduces to elementary constants or to a named special-value identity. The displayed decimal is a numerical evaluation of the exact integral rather than an independently interval-certified constant. The result is restricted to the incommensurate high-energy Kagome density governed by the source criterion; commensurate length ratios have different orbit closures and are not covered.

## References
1. M. Baradaran and P. Exner, *Kagome network with vertex coupling of a preferred orientation*, arXiv:2106.16019v1; Journal of Mathematical Physics 63 (2022), 083502, DOI: 10.1063/5.0093546.
2. R. Band and G. Berkolaiko, *Universality of the momentum band density of periodic networks*, arXiv:1304.6028v1; Physical Review Letters 111 (2013), 130404, DOI: 10.1103/PhysRevLett.111.130404.
