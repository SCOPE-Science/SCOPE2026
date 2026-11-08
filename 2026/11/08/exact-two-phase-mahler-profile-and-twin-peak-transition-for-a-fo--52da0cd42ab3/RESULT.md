# Exact two-phase Mahler profile and twin-peak transition for a four-dimensional cube-apex family

## Finding
For every real \(t>0\), let
\[
P_t=\operatorname{conv}\!\left([-1,1]^4\cup\{\pm(1,1,1+t,1),\ \pm(1,1,1,1+t)\}\right).
\]
Writing \(V(t)=\operatorname{vol}_4(P_t)\), \(W(t)=\operatorname{vol}_4(P_t^\circ)\), and \(\Phi(t)=V(t)W(t)\), the exact primal volume is
\[
V(t)=\begin{cases}
16+8t+\frac23t^2,&0<t\le2,\\
\frac43t^2+8t+\frac{40}3,&t\ge2.
\end{cases}
\]
The polar volume is
\[
W(t)=\begin{cases}
\displaystyle \frac{-t^5-4t^4+44t^3+272t^2+464t+256}{3(t+2)^3(t+4)^2},&0<t\le2,\\[4pt]
\displaystyle \frac{8(3t^6+26t^5+80t^4+72t^3-88t^2-64t+128)}{3t^3(t+2)^3(t+4)^2},&t\ge2.
\end{cases}
\]
In particular, the exact difference from the cubical Mahler constant is
\[
\Phi(t)-\frac{32}{3}=\begin{cases}
\displaystyle \frac{-2t(t^6+16t^5+76t^4-32t^3-1136t^2-2752t-1920)}{9(t+2)^3(t+4)^2},&0<t\le2,\\[5pt]
\displaystyle \frac{64(t^7+19t^6+106t^5+188t^4-128t^3-568t^2+64t+640)}{9t^3(t+2)^3(t+4)^2},&t\ge2.
\end{cases}
\]
Both gaps are strictly positive; nevertheless \(\Phi(t)\to32/3\) both as \(t\downarrow0\) and as \(t\to\infty\), with the latter approach precisely
\[\Phi(t)=\frac{32}{3}+\frac{64}{9t}+O(t^{-2}).\]

There is a strict local maximum at the unique \(a\in(1.577,1.578)\) solving
\[
A(a)=a^8+21a^7+188a^6+932a^5+2528a^4+2480a^3-4288a^2-12416a-7680=0.
\]
There is a strict local *minimum* at the transition \(t=2\), where \(\Phi(2)=1027/81\), and a second strict local maximum at the unique \(b\in(2.607,2.609)\) solving
\[
B(b)=b^9+30b^8+248b^7+720b^6-456b^5-6960b^4-12048b^3+2368b^2+22784b+15360=0
\]
with \(b>2\). **The second maximum is the unique global maximum** of \(\Phi\) on \((0,\infty)\), approximately \(12.82087\). Thus the exact profile has two smooth peaks separated by a nonsmooth notch, not a simple unimodal shape.

## Assumptions and scope
All volumes are ordinary four-dimensional Lebesgue volumes. The polar is taken with respect to the origin: \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for all }x\in K\}\). The parameter \(t\) is any real number strictly greater than zero; the family is centrally symmetric and full dimensional. In particular, no product-compatibility or finite-height hypothesis is imposed. The phase point \(t=2\) belongs to both branches. The origin is the Santaló point by symmetry.

## Proof
**Primal volume and exhaustive parameter chambers.** The twenty input points have integer-affine coordinates in \(t\); all affine five-point determinants have degree at most four. For every one of the \(\binom{20}{5}=15504\) five-point subsets, an exact fraction-free determinant computed at five integers, followed by inverse-Vandermonde interpolation over the rationals, recovers its complete polynomial. There are 11080 nonzero determinant instances and 30 distinct nonzero polynomial classes. Complete exact factorization shows that the positive roots over all nonzero classes are precisely
\[
2\sqrt2-2,\qquad1,\qquad\sqrt5-1,\qquad2,\qquad4.
\]
Thus the oriented matroid and all supporting faces are constant on the six open parameter chambers separated by these numbers. At rational representatives \(1/2,9/10,11/10,3/2,3,5\), a simplicial boundary complex is proposed and then checked using **exact rational supporting-hyperplane determinant signs** for every vertex. Every triangular ridge occurs exactly twice, and the complex is connected. Some candidate cells are flat: their exact conical determinant vanishes and they contribute zero to volume; the nonflat cells are boundary tetrahedra. Summing signed four-by-four determinants of the conical simplices from the origin, divided by \(24\), produces the exact polynomials
\[
16+8t+\tfrac23t^2 \quad \text{in the first four chambers},\qquad
\tfrac43t^2+8t+\tfrac{40}3 \quad \text{in the final two}.
\]
Since all determinant signs are constant within each chamber, the supporting triangulation remains a valid boundary complex (allowing zero-volume cells) throughout that chamber. Continuity of convex-hull volume at the five intermediate roots establishes the asserted two-branch formula on all \(t>0\). The supplied reproducible finite certificate implements each determinant and sum in exact arithmetic; floating-point hull computations **propose**, but never certify, the facets. The determinant roots, supporting planes, adjacency closure and volume identities are all verified exactly.

**Polar volume by a one-dimensional integral.** Put \(u=y_3\), \(v=y_4\), \(s=1-|u|-|v|\), and \(p=y_1+y_2\), \(q=y_1-y_2\). The cubical polar condition is \(|p|,|q|\le s\); the two added apex pairs impose
\[
|p+(1+t)u+v|\le1,\qquad |p+u+(1+t)v|\le1.
\]
The change from \((y_1,y_2)\) to \((p,q)\) has Jacobian \(1/2\). Integrating \(q\) first contributes the factor \(s\) times the admissible length of the \(p\)-interval. On each quadrant in the \((u,v)\)-plane write \(r=|u|+|v|\) and \(x=|u|/r\), with Jacobian \(r\). When \(u,v\) have the same sign, this length is \([2(1-r)-tr\max(x,1-x)]_+\). When they have opposite signs, it is \([2(1-r)-rk_t(x)]_+\), where
\[
k_t(x)=[(t+2)x-2]_+ +[t-(t+2)x]_+.
\]
The elementary radial primitive is
\[
F(k)=\int_0^{2/(k+2)}r(1-r)(2-(k+2)r)\,dr
=\frac{4(k+1)}{3(k+2)^3};\qquad
G(k)=\frac43\left(-\frac1{k+2}+\frac1{2(k+2)^2}\right),\quad G'=F.
\]
Accounting for both types of quadrant, the exact polar integral reduces to
\[
W(t)=4\int_{1/2}^1F(tx)\,dx+2\int_0^1F(k_t(x))\,dx.
\]
For \(0<t\le2\), \(k_t\) has two linear boundary pieces and a central zero interval; for \(t\ge2\), its central interval equals \(t-2\). In detail, these integrate to
\[
W_<(t)=\frac4t[G(t)-G(t/2)] +\frac4{t+2}[G(t)-G(0)]+\frac{2(2-t)}{t+2}F(0),
\]
\[
W_>(t)=\frac4t[G(t)-G(t/2)] +\frac4{t+2}[G(t)-G(t-2)]+\frac{2(t-2)}{t+2}F(t-2).
\]
Substitution and rational simplification give exactly the polar formulas above; they coincide at \(t=2\).

**Strict gaps and two-peak classification.** Multiply the obtained \(V\) and \(W\). On \(0<t\le2\), the parenthesized polynomial in the numerator of the Mahler gap is strictly negative: its positive terms obey
\(t^6+16t^5+76t^4\le1792<1920\), while all remaining terms are negative. On \(t\ge2\), setting \(z=t-2\) turns the parenthesized numerator into
\[
z^7+33z^6+418z^5+2668z^4+9216z^3+16888z^2+14848z+5216,
\]
which is strictly positive. The displayed rational formulas then give the endpoint limits and expansion.

The derivatives of the two product branches are exactly
\[
\Phi_<'(t)=-\frac{4A(t)}{9(t+2)^4(t+4)^3},\qquad
\Phi_>'(t)=-\frac{64B(t)}{9t^4(t+2)^4(t+4)^3}.
\]
The coefficient sequences of \(A\) and \(B\) have respectively one and two sign changes. By Descartes' rule, \(A\) has at most one positive zero and \(B\) has at most two; the exact endpoint signs \(A(0)<0<A(2)\) and \(B(0)>0>B(2)\), together with \(B(3)>0\), force exactly the claimed relevant roots and signs. At the phase point, the left derivative is negative and the right derivative positive, giving the strict local minimum.

To compare the two peaks globally, an exact rational certificate shows \(\Phi_<(t)<64/5\) throughout \([0,2]\). In fact,
\[
\frac{64}{5}-\Phi_<(t)=\frac{2p(t)}{45(t+2)^3(t+4)^2},\quad
p(t)=5t^7+80t^6+428t^5+512t^4-2032t^3-4160t^2+2688t+6144.
\]
On each of \([0,1]\), \([1,3/2]\), and \([3/2,2]\), write \(t=(a+bu)/(1+u)\) with \(u\ge0\); the polynomial \((1+u)^7p((a+bu)/(1+u))\) has **strictly positive rational coefficients**, as verified in the standalone certificate. On the other hand \(\Phi_>(13/5)>64/5\) exactly. Hence the second maximum dominates the first and is the unique global maximum.

## Verification
The accompanying standalone script `verify.py` requires Python 3.10+, NumPy, SciPy and SymPy, with versions listed in `requirements.txt`. Run `OPENBLAS_NUM_THREADS=1 python verify.py`. It exhaustively enumerates all 15504 affine five-point subsets and their exact parameter-chamber root structure; checks six supporting boundary complexes (including zero-volume cells) and rational volume polynomials; checks the integral primitives, closed polar rational functions, gap and asymptotic identities; and verifies all rational sign and root-isolation certificates for the two-peak classification. The exact computational steps have no unprovided external input, dataset, or stochastic component.

## Relationship to prior work
Shen and Dubovski (2026), arXiv:2610.11014, introduce this exact four-dimensional two-apex family and prove its strict Mahler inequality only for \(0<t\le12/7\) (Corollary 4). Their general results concern height-constrained minima and sufficient lower certificates, not this complete two-phase exact product, the transition at \(t=2\), or the unique global two-peak optimizer. The later published manuscript *The symmetric Mahler conjecture and its equality cases* (2026) states the all-dimensional symmetric Mahler bound with Hanner equality; if accepted, its stronger theorem already implies the **strict inequality** for this non-Hanner family, so strictness alone is not a novelty claim. It does not give the exact rational profile or the two-peak phase diagram. Related public studies of cube–cross-polytope intersections and cube-to-Hanner interpolation have different families, and neither statement implies these family-specific formulas. The elementary Fubini integration and the chamber enumeration here give independent calculations; searches cannot certify historical uniqueness.

## Limitations
Only the specified four-dimensional two-apex family is classified; there is no claim about arbitrary apex arrays, dimensions, or a universal global Mahler stability modulus. The exact primal formula relies on a finite computer-reproducible rational certificate, not a short manual polyhedral shelling. The all-dimensional Mahler theorem is cited as a published preprint rather than independently verified here. Historical priority is provisional; independent mathematical audit has not been performed.

## References
1. Hanyue Shen and Pavel Dubovski, *A sharp minimum for cube-apex bodies in every dimension*, arXiv:2610.11014v1 (first posted 2026-10-07), https://arxiv.org/abs/2610.11014 . Especially Section 3, Corollary 4.
2. *The symmetric Mahler conjecture and its equality cases*, 2026 preprint, Theorem 1.1 and equality statement; full text mirrored at https://wcook04.github.io/plectis-atlas/papers/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026.html .
3. F. Nazarov, F. Petrov, D. Ryabogin and A. Zvavitch, *A remark on the Mahler conjecture: local minimality of the unit cube*, Duke Math. J. 154 (2010), 419–430.
