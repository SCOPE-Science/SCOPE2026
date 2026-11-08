# Sharp asymmetric two-sided imaginary-axis stability for two complex Euler substeps

## Finding

For any real spectral limits \(a,b\geq0\) with \(a+b>0\), consider first-order two-stage stability polynomials
\[
P_k(z)=1+z+kz^2,\qquad k\in\mathbb C.
\]
The largest \(h\geq0\) for which \(|P_k(iy)|\leq1\) for **every** \(y\in[-bh,ah]\), with \(k\) freely optimized, is
\[
\boxed{h_*=\frac{2}{a+b}},\qquad
\boxed{k_* = \frac{(a+b)^2+i(a^2-b^2)}{2(a^2+b^2)}}.
\]
The optimizing coefficient is unique, including the one-sided endpoint cases \(a=0\) or \(b=0\). Write \(A=2a/(a+b)\), \(B=2b/(a+b)\), \(u=2/(A^2+B^2)>0\). Then, exactly for all real \(y\),
\[
|P_{k_*}(iy)|^2-1=u y^2(y-A)(y+B).
\]
Thus the intersection of the absolute-stability region with the imaginary axis is exactly \([-iB,iA]\). If \(k\) must be real, the unique optimal coefficient is \(k=1\), with \(h_{\rm real}=1/\max(a,b)\); the sharp complex-to-real step gain is \(2\max(a,b)/(a+b)\), strictly exceeding one when \(a\ne b\) and reaching two at a one-sided limit. For example \(a=3,b=1\) yields \(h_*=1/2\) and \(k_*=4/5+2i/5\), versus real-coefficient optimum \(h=1/3\).

## Assumptions and scope

The stability requirement is uniform over the **whole closed interval** of imaginary frequencies \([-b,a]\); it is a robust interval guarantee, not necessarily the optimal step for an individual discrete spectrum with gaps. Both spectral widths are nonnegative and are not simultaneously zero. The method has only first-order accuracy, permits complex coefficients, and is assessed for the scalar linear test equation \(u'=\lambda u\). For a normal constant matrix whose spectrum is contained in \(i[-b,a]\), the same interval bound gives spectral (and operator-norm) nonexpansion. No claim is made for nonlinear equations, nonnormal transient bounds, or second-order accuracy.

Every coefficient \(k\in\mathbb C\) is realizable by two complex forward-Euler substeps with fractional time weights \(w_1+w_2=1\) and \(w_1w_2=k\): the weights are the two complex roots of \(w^2-w+k=0\). Their composition has stability polynomial \((1+w_1z)(1+w_2z)=P_k(z)\).

## Proof

**1. Endpoint disks and the global bound.** Let \(k=u+iv\), with \(u,v\in\mathbb R\). Direct multiplication gives, for real \(y\),
\[
|P_k(iy)|^2-1=y^2\big[(u^2+v^2)y^2-2vy+(1-2u)\big]. \tag{1}
\]
Suppose first that \(a,b>0\) and \(h>0\), and put \(A=ah\), \(B=bh\). Endpoint stability at \(y=A,-B\) is equivalent to membership in two closed disks in the coefficient plane:
\[
\left|k-\Big(\frac1{A^2}+\frac iA\Big)\right|\leq\frac1{A^2},\qquad
\left|k-\Big(\frac1{B^2}-\frac iB\Big)\right|\leq\frac1{B^2}. \tag{2}
\]
For the disks to intersect, their centers' distance cannot exceed the sum of the radii. Squaring and subtracting the squared difference of radii yields
\[
\Big(\frac1A+\frac1B\Big)^2\leq\frac4{A^2B^2},
\quad\text{hence}\quad A+B\leq2.
\]
Consequently \(h\leq2/(a+b)\) for every admissible coefficient. At equality, the disks are externally tangent and their intersection is one point. Algebra gives this unique tangency point as
\[
k=\frac{2+i(A-B)}{A^2+B^2}
=\frac{(a+b)^2+i(a^2-b^2)}{2(a^2+b^2)}. \tag{3}
\]

**2. Entire-interval sufficiency and exactness.** For \(A+B=2\), write \(k_*=u+iv\). Equation (3) gives \(u=2/(A^2+B^2)\), \(v=(A-B)/(A^2+B^2)\), \(|k_*|^2=u\), and \(1-2u=-uAB\). Substitution in (1) gives
\[
|P_{k_*}(iy)|^2-1=u y^2(y-A)(y+B).
\]
The right-hand side is nonpositive precisely for \(-B\leq y\leq A\), including the degenerate one-sided cases, and is positive elsewhere except at \(y=0\). This proves the stated interval and achieves the upper bound. Tangency in (2) proves uniqueness when both widths are positive.

**3. One-sided endpoints.** If \(b=0,a>0\), stability at every sufficiently small \(y>0\) in (1) requires \(u\geq1/2\). The positive endpoint condition gives the first disk in (2), whose rightmost real coordinate is \(2/A^2\). Hence \(1/2\leq2/A^2\), or \(A\leq2\). Equality forces the unique intersection \(k=(1+i)/2\), which is the special case of (3). For \(a=0,b>0\), conjugation yields \(B\leq2\) and the unique optimizer \(k=(1-i)/2\).

**4. Real-coefficient comparison.** When \(v=0\), (1) reduces to \(y^2[u^2y^2+1-2u]\). A nonzero imaginary stability interval requires \(u\geq1/2\), and its largest possible symmetric radius is \(\sqrt{2u-1}/u\leq1\). Equality is equivalent to \((u-1)^2=0\), proving the unique real-coefficient optimum \(k=1\). Scaling by \(\max(a,b)\) gives the claimed ratio.

## Verification

The standalone Python standard-library script `verify.py` uses exact rational arithmetic to check the coefficient identities, stability factorization, endpoint-disk tangency, and complex-versus-real gain on a finite rational family including the two one-sided limits. The proof above is symbolic and valid for all real \(a,b\geq0\), not dependent on numerical sampling. Execute `python verify.py` from the folder containing this file; a successful run prints `CHECKS_OK` and its exact-check count.

## Relationship to prior work

George, Koellermeier, Jung and Mangan [1] established the same first-order two-stage polynomial family, including the optimal one-sided imaginary intervals of length two and the real-coefficient interval of radius one. Those endpoint results and the idea of complex timestepping are prior art. The new statement is a **complete, unique two-sided asymmetric frontier**, proving that the endpoint capacities trade off according to \(A+B\leq2\) and obtaining its exact complex coefficient and gain for arbitrary prescribed relative widths. The 2012 optimal-stability-polynomial framework of Ketcheson and Ahmadia [2] treats general spectral containment but uses real coefficients in its explicit symmetric-imaginary-axis examples; its general optimization formulation does not state the two-sided complex-coefficient closed form. An independently applicable earlier general extremal-polynomial theorem may still affect historical priority.

## Limitations

First-order methods need not be appropriate when accuracy rather than spectral absolute stability limits the timestep. Endpoint-only stability is a necessary condition for interval inclusion, but sufficiency here uses the special factored candidate, not arbitrary coefficients. The result is about **uniform interval inclusion** and scalar or normal linear evolution; it does not imply nonnormal or nonlinear contractivity, internal-stage stability, or efficiency once complex arithmetic costs are included. The standard one-sided and symmetric cases were already known.

## References

[1] J. D. George, J. Koellermeier, S. Y. Jung and N. M. Mangan, *Explicit complex time integrators for stiff problems*, arXiv:2601.07730 (first public version January 12, 2026; Section 3.2, Theorem 1 in version 2). https://arxiv.org/html/2601.07730v2

[2] D. I. Ketcheson and A. J. Ahmadia, *Optimal stability polynomials for numerical integration of initial value problems*, Commun. Appl. Math. Comput. Sci. 7 (2012), 247–271. https://doi.org/10.2140/camcos.2012.7.247
