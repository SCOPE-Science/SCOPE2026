# Universal Löwner ellipsoid of a homothetic convex frustum, with both rim contact sets

## Finding
Let \(d\ge2\), let \(K\subset\mathbb R^d\) be a full-dimensional compact convex body, and write its unique minimum-volume enclosing ellipsoid as \(L(K)=e+A\mathbb B_d\), where \(A\) is positive definite and \(\mathbb B_d\) is the Euclidean unit ball. For \(r>s\ge0\), form the \((d+1)\)-dimensional homothetic frustum
\[
F_{r,s}(K)=\operatorname{conv}\bigl((sK)\times\{-1\},(rK)\times\{1\}\bigr).
\]
Put \(q=s/r\), and define the positive number
\[
c=\frac{\sqrt{(1+q^2)^2+d(d+2)(1-q^2)^2}-(1+q^2)}{(d+2)(1-q^2)},
\qquad a^2=\frac{r^2(d+1)(1+c)}{d+(d+2)c},\qquad b^2=(d+1)(1-c^2).
\]
Set \(\rho(t)=\tfrac12(r+s)+\tfrac12(r-s)t\). Then the **unique Löwner ellipsoid** of the full frustum is
\[
\boxed{L(F_{r,s}(K))=\left\{(x,t):\frac{\|A^{-1}(x-\rho(t)e)\|^2}{a^2}+\frac{(t-c)^2}{b^2}\le1\right\}.}
\]
In particular, its complete ellipsoid is determined by the base Löwner ellipsoid alone, for **any** base \(K\), even an asymmetric or nonsmooth one. Every Löwner contact point of \(K\) lifts to an upper-rim contact, and, for \(s>0\), to a lower-rim contact. Both rims carry strictly positive mass in a minimum-volume contact certificate for all \(s>0\). At \(s=0\), the lower level is a contacting apex. No outer contact phase transition occurs as the truncation ratio changes. At the prism limit \(q\uparrow1\), the formulas tend to \(c=0\), \(a^2=r^2(d+1)/d\), \(b^2=d+1\).

## Assumptions and scope
Here \(r>s\ge0\), with the height coordinates \(-1,+1\); the theorem also covers congruent, translated top and bottom bases after an invertible affine shear. Multiplication of a set \(K\) by \(s\) means \(sK=\{sx:x\in K\}\). The base is assumed compact and convex with nonempty interior and is not assumed to be symmetric, polygonal, smooth, or centered at the origin. The Euclidean metric in the displayed equation is the unit-ball normalization after the explicit affine transformation; minimum-volume containing ellipsoids are affine equivariant. The stated parameter \(c\) belongs to \((0,d/(d+2)]\) for \(q\in[0,1)\), with the upper endpoint at \(q=0\). The equal-base cylinder \(q=1\), although excluded from \(s<r\), follows by the indicated limit and the same contact proof.

## Proof
**1. Reduction to Löwner position.** Apply the invertible shear/linear transformation \((x,t)\mapsto(A^{-1}(x-\rho(t)e),t)\). It sends the two bases to \(sK_0\) and \(rK_0\), where \(K_0=A^{-1}(K-e)\) and \(L(K_0)=\mathbb B_d\). It therefore suffices to prove that
\[
E=\bigl\{(y,t):\|y\|^2/a^2+(t-c)^2/b^2\le1\bigr\}
\]
is the Löwner ellipsoid of \(\operatorname{conv}((sK_0,-1),(rK_0,1))\).

**2. Algebraic identities.** The stated radical is the unique nonnegative solution of
\[
(d+2)(1-q^2)c^2+2(1+q^2)c-d(1-q^2)=0.
\]
It is equivalent to the parameter relation
\[
q^2=\frac{(1+c)\bigl(d-(d+2)c\bigr)}{(1-c)\bigl(d+(d+2)c\bigr)}.
\]
Substituting this relation and the definitions of \(a,b\) yields both exact endpoint identities
\[
\frac{r^2}{a^2}+\frac{(1-c)^2}{b^2}=1,\qquad
\frac{s^2}{a^2}+\frac{(1+c)^2}{b^2}=1.
\]
Thus \(E\) contains both Euclidean disks \((r\mathbb B_d,1)\) and \((s\mathbb B_d,-1)\). By convexity it contains their convex hull, hence the entire frustum. This proves feasibility without making symmetry assumptions on \(K_0\).

**3. Lift of an arbitrary Löwner contact measure.** The Löwner–John characterization of \(L(K_0)=\mathbb B_d\) provides finitely many \(u_i\in K_0\cap S^{d-1}\) and weights \(\alpha_i>0\) such that
\[
\sum_i\alpha_i=1,\qquad\sum_i\alpha_i u_i=0,\qquad
\sum_i\alpha_i u_i u_i^{\mathsf T}=I_d/d.
\]
Normalize \(E\) to \(\mathbb B_{d+1}\). For each \(i\), the upper- and lower-rim points map to
\[
v_{+,i}=\left(\frac{r}{a}u_i,\frac{1-c}{b}\right),\qquad
v_{-,i}=\left(\frac{s}{a}u_i,\frac{-1-c}{b}\right).
\]
Both are unit vectors by the endpoint identities. Give \(v_{+,i}\) the probability mass \((1+c)\alpha_i/2\) and \(v_{-,i}\) the mass \((1-c)\alpha_i/2\). The weights are strictly positive. Since \(\sum\alpha_i u_i=0\), the transverse first moments and all mixed second moments vanish. The vertical first moment vanishes because
\[
(1+c)(1-c)-(1-c)(1+c)=0.
\]
The vertical variance equals
\[
\frac{(1+c)(1-c)^2+(1-c)(1+c)^2}{2b^2}=\frac{1-c^2}{b^2}=\frac1{d+1}.
\]
The transverse variance matrix is a scalar multiple of \(I_d\), with scalar
\[
\frac{(1+c)r^2+(1-c)s^2}{2d a^2}=\frac1{d+1},
\]
by the parameter relation in step 2. The complete lifted contact probability measure therefore has mean zero and covariance \(I_{d+1}/(d+1)\). The sufficient direction of the classical Löwner contact theorem certifies that the normalized unit ball, and hence \(E\), is the **globally** minimum-volume covering ellipsoid. Uniqueness holds for every convex body of full dimension. When \(s=0\), all lower-rim contacts coincide at the apex; their total mass remains positive. The proof also works verbatim for \(s=r>0\) by setting \(c=0\).

**4. No rim-contact transition.** The two total rim masses \((1+c)/2\) and \((1-c)/2\) are strictly positive for the entire parameter range, with \(c\le d/(d+2)<1\). Both contact sets persist until the lower level degenerates into an apex. This differs structurally from the sharp contact transition of the *inscribed* John ellipsoid of a homothetic frustum.

## Verification
The supplied standard-library Python 3 script `verify_frustum.py` performs exact rational tests of the endpoint gauge equalities, all lifted first- and second-moment identities, and convex-hull containment at intermediate section levels for \(d=2,\ldots,20\) at 51 rational center parameters per dimension. It also checks the cone and cylinder endpoint formulas through dimension 29 and the radical equation numerically at a separate parameter grid. The output is `VERIFY_OK`. These finite tests are independent consistency checks; the all-base, all-dimension assertion follows from the analytic Löwner certificate.

## Relationship to prior work
Güler and Gürtuna (2007, §8, Theorem 8.1) determine covering ellipsoids for **ellipsoidal** truncated second-order cones and cylinders. Those are the case in which the base is itself an ellipsoid. Their theorem does not state or establish that an arbitrary asymmetric or nonsmooth base may be replaced by its Löwner ellipsoid without changing the covering ellipsoid of the frustum. The full-base invariance and the lifted two-rim contact design are the new asserted content here; the exact circular-frustum formulas are credited antecedents, not separately claimed as novel.

Ivanov and Naszódi (2022) supply a modern general-purpose framework for Löwner contact conditions, but no arbitrary-base homothetic-frustum formula in the inspected text. A previously published result entitled *Exact John–Löwner ellipsoids and a sharp volume-ratio spectrum for one-vertex simplex frusta* gives the covering ellipsoid for the much more restricted regular-simplex-base family; it is covered as a special case of the present arbitrary-base statement, and its original simplex formula is fully credited. Separately published universal homothetic-frustum formulas apply to **John inscribed** ellipsoids, whose lower/upper contact transitions do not imply this covering result. Thus the novelty assessment concerns the universal arbitrary-base replacement principle, not the basic extremal-ellipsoid theorem or the formula for a circular frustum.

## Limitations
The two levels must be parallel homothetic copies of a common base, with at most affine shear. Different, nonhomothetic bases or warped intermediate sections are not included. Contact frames are sufficient certificates and need not list every geometric contact point. No historical uniqueness is claimed: earlier optimal-design/ellipsoid literature might contain an equivalent general lifting principle, which should be checked independently. The result has not received independent mathematical audit.

## References
1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1 (2007-09-05), especially §8 and Theorem 8.1, https://arxiv.org/abs/0709.0707.
2. G. Ivanov and M. Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781v1 (first posted 2022-12-22), https://arxiv.org/abs/2212.11781.
3. R. Gartsman and N. Linial, *On the Löwner-John Ellipsoids of the Metric Polytope*, arXiv:2305.02113v1 (2023-04-19), https://arxiv.org/abs/2305.02113.
4. *Exact John–Löwner ellipsoids and a sharp volume-ratio spectrum for one-vertex simplex frusta*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-john-l-wner-ellipsoids-and-a-sharp-volume-ratio-spectrum-f--bfb9af719d89.
5. *Base-independent John ellipsoids of homothetic frusta with a sharp contact transition*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-base-independent-john-ellipsoids-of-homothetic-frusta-with-a-sha--976839cd459e.
6. *Universal John ellipsoids of homothetic frusta and a sharp contact transition*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-universal-john-ellipsoids-of-homothetic-frusta-and-a-sharp-conta--07410bf05003.
