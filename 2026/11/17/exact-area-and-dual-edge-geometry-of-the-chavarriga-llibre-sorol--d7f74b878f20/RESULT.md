# Exact area and dual-edge geometry of the Chavarriga–Llibre–Sorolla quartic oval

## Finding
For the classical quadratic differential system
\[
\dot x=2(1+2x-2a x^2+6xy),\qquad
\dot y=8-3a-14ax-2axy-8y^2,
\]
with \(0<a<1/4\), denote by \(\Omega_a\) the bounded domain enclosed by its quartic algebraic limit cycle and let \(\mathcal A(a)=\operatorname{area}(\Omega_a)\) be ordinary Euclidean area in the coordinates displayed. The following statements hold simultaneously.

1. The area \(\mathcal A\) is a strictly decreasing bijection from \((0,1/4)\) onto \((0,\infty)\), with the exact elliptic-integral representation
\[
\boxed{\mathcal A(a)=\frac{4\beta^{3/2}}{3a}
\left[(2-m)E(m)-2(1-m)K(m)\right]},
\]
where \(\alpha=(1-\sqrt{1-4a})/2\), \(\beta=(1+\sqrt{1-4a})/2\), \(m=1-\alpha/\beta\), and \(K,E\) are the complete Legendre elliptic integrals with *parameter* \(m\), not modulus \(m\).

2. At the unbounded-oval endpoint,
\[
\boxed{\mathcal A(a)=\frac4{3a}+\log a-1-\log16+O(a|\log a|)}
\qquad(a\downarrow0).
\]
In particular, under the physical coordinate rescaling \((X,Y)=(ax,y)\), the indicator functions of the enclosed domains converge almost everywhere to that of the parabolic lens \(\{0<X<1,\ |Y|<\sqrt{1-X}\}\), and the rescaled enclosed areas converge to \(4/3\).

3. At the collapsing-oval endpoint,
\[
\boxed{\mathcal A(a)\sim4\sqrt2\,\pi(1/4-a)}
\qquad(a\uparrow1/4).
\]
More precisely, put \(\delta=1/4-a\), \(c=1/(2a)\), \(h=\sqrt\delta/a\), and use the shear-adjusted coordinates
\[
U=(x-c)/h,\qquad V=\bigl(y+1/(2x)\bigr)/\sqrt{2\delta}.
\]
The transformed bounded domains converge to the unit disk. Both the infinite-area degeneration and the finite-area collapse concern the *same* isolated algebraic cycle family, not different normalizations of the vector field.

## Assumptions and scope
The parameter is real and satisfies \(0<a<1/4\). No statement is made that the limiting vector fields at either endpoint retain an isolated periodic orbit. Euclidean area is fixed in the original \((x,y)\) coordinates; no affine or time reparametrization is silently imposed. The oval is the bounded connected component of the invariant quartic
\[
f_a(x,y)=\tfrac14+x-x^2+ax^3+xy+x^2y^2=0.
\]
Its existence as a genuine algebraic limit cycle is a known result of the Chavarriga–Llibre–Sorolla family; the new statements are the exact global area function, strict nesting, the two endpoint profiles, and the explicit logarithmic finite correction.

## Proof
**Step 1: Exact oval and slice area.** Completing the square gives
\[
f_a(x,y)=(xy+1/2)^2+x(1-x+ax^2).
\]
For \(x>0\), the bounded oval has horizontal endpoints
\[
r_{\pm}(a)=\frac{1\pm\sqrt{1-4a}}{2a}
\]
and vertical branches
\[
y_{\pm}(x)=-\frac1{2x}\pm\sqrt{\frac{x-1-ax^2}{x}},
\quad r_-(a)\le x\le r_+(a).
\]
Consequently the enclosed area is exactly
\[
\mathcal A(a)=2\int_{r_-}^{r_+}
\sqrt{\frac{x-1-ax^2}{x}}\,dx.
\tag{1}
\]
The original vector field and the cofactor \(k=4(2-3ax+2y)\) obey \(\dot f_a=k f_a\) identically. The known result that this regular oval is a limit cycle is used, rather than reproved from its defining equation.

**Step 2: Elliptic reduction.** Substituting \(z=ax\) turns (1) into
\[
\mathcal A(a)=\frac2a\int_\alpha^\beta
\sqrt{\frac{(\beta-z)(z-\alpha)}z}\,dz.
\tag{2}
\]
Here \(\alpha\beta=a\), \(\alpha+\beta=1\), and \(0<\alpha<\beta<1\). Set \(z=\beta(1-m\sin^2\theta)\), with \(m=1-\alpha/\beta\). Then (2) equals
\[
\frac{4\beta^{3/2}m^2}{a}\int_0^{\pi/2}
\frac{\sin^2\theta\cos^2\theta}{\sqrt{1-m\sin^2\theta}}\,d\theta.
\tag{3}
\]
Define \(K(m)=\int_0^{\pi/2}(1-m\sin^2\theta)^{-1/2}\,d\theta\) and \(E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2\theta}\,d\theta\). Direct reduction of the second and fourth sine moments yields
\[
\int_0^{\pi/2}\frac{\sin^2\theta\cos^2\theta}{\sqrt{1-m\sin^2\theta}}\,d\theta
=\frac{(2-m)E(m)-2(1-m)K(m)}{3m^2},
\]
proving the boxed exact formula. For completeness, write \(I_j=\int_0^{\pi/2}\sin^j\theta/\sqrt{1-m\sin^2\theta}\,d\theta\). Then \(I_2=(K-E)/m\), while integrating the derivative of \(\sin\theta\cos\theta\sqrt{1-m\sin^2\theta}\) over the quarter-period gives \(K-2(1+m)I_2+3mI_4=0\); eliminating \(I_2,I_4\) yields the displayed reduction without any unevaluated integral lemma.

**Step 3: Strict monotonicity.** On any common \(x\)-slice, increasing \(a\) strictly decreases the positive height \(2\sqrt{(x-1-ax^2)/x}\); the admissible interval shrinks strictly. Hence \(\Omega_{a_2}\subsetneq\Omega_{a_1}\) whenever \(0<a_1<a_2<1/4\), so \(\mathcal A\) strictly decreases. Endpoint continuity follows directly from (2) and the rescalings below. In fact differentiation of (1), justified by integrable square-root endpoint singularities, gives
\[
\mathcal A'(a)=-\int_{r_-}^{r_+}
\frac{x}{\sqrt{(x-1-ax^2)/x}}\,dx<0.
\]

**Step 4: Small-parameter logarithmic correction.** As \(a\downarrow0\), one has \(\beta=1-a+O(a^2)\) and \(1-m=\alpha/\beta=a+O(a^2)\). Write \(\lambda=1-m\) and \(L=\log(4/\sqrt\lambda)\). The standard complete elliptic expansions, with quantitative remainders, are
\[
K(m)=L+O(\lambda|\log\lambda|),\quad
E(m)=1+\frac\lambda2(L-1/2)+O(\lambda^2|\log\lambda|).
\]
In the exact area formula the bracket is \((1+\lambda)E-2\lambda K\), hence
\[
(1+\lambda)E-2\lambda K
=1+\lambda(3/4-3L/2)+O(\lambda^2|\log\lambda|).
\]
Combining with \(\beta^{3/2}=1-3a/2+O(a^2)\) and \(L=\log4-\frac12\log a+O(a)\) gives
\[
\mathcal A(a)=\frac4{3a}+\log a-1-2\log4+O(a|\log a|),
\]
which is precisely the claimed constant. Alternatively, the scaled region \((X,Y)=(ax,y)\) has branches \(Y=-a/(2X)\pm\sqrt{1-X-a/X}\) for \(\alpha\le X\le\beta\). Dominated convergence of its vertical height establishes the parabolic-lens limit and the leading \(a\mathcal A(a)\to4/3\).

**Step 5: Collapsing-oval geometry.** Put \(\delta=1/4-a\), \(c=1/(2a)\), \(h=\sqrt\delta/a\). Writing \(x=c+hU\) and \(V=(y+1/(2x))/\sqrt{2\delta}\) turns the oval interior *exactly* into
\[
-1\le U\le1,\qquad V^2\le\frac{c}{c+hU}(1-U^2).
\]
Because \(h/c=2\sqrt\delta\to0\), this region converges uniformly in its vertical boundaries to the closed unit disk. The Jacobian gives \(dx\,dy=h\sqrt{2\delta}\,dU\,dV\). Therefore
\[
\mathcal A(a)=h\sqrt{2\delta}\,[\pi+o(1)]
=\frac{\sqrt2\delta}{a}[\pi+o(1)]
\sim4\sqrt2\pi\delta.
\]
These two endpoint behaviors and strict monotonicity give the asserted bijection.

## Verification
A standalone script `check.py` rechecks the polynomial cofactor identity exactly with symbolic algebra and compares the slice integral with the elliptic formula at multiple admissible parameters at high precision. It also checks the logarithmic finite constant and linear small-oval scaling numerically. The analytical endpoint proof does not rely on finite samples; the checks provide independent error detection rather than an infinite certificate. Running `python check.py` requires `sympy` and `mpmath`.

## Relationship to prior work
Chavarriga, Llibre and Sorolla (2004) established the degree-four algebraic limit-cycle family. Alberich-Carramiñana, Ferragut and Llibre (public preprint 2019-06-24, arXiv:1906.10171) give its vector field and qualitative phase portrait. Gasull and Giacomini (public preprint 2022-10-27, arXiv:2210.15803) give the same exact invariant quartic and a general uniqueness theorem. The cited full-text presentations were compared against the exact area, logarithmic correction, monotonicity and rescaled edge profiles; they concern existence/classification rather than these quantitative geometric conclusions. The use of elliptic integrals and their singular expansions is classical (NIST DLMF §19.12); the new object-specific evaluation and correction are not claimed to be new special-function theory. A published result on area growth for the different Filiptsov oval has no implication for this polynomial family.

## Limitations
The full original 2004 article was not accessible for text-level comparison, although its bibliographic abstract was checked; an independent priority search of that full text remains a limitation. This is an exact Euclidean geometric result about one classical isolated cycle family, not a classification of arbitrary quartics or a new limit-cycle existence theorem. The asymptotics describe the approach to excluded parameter endpoints and do not assert persistence of a cycle at either endpoint. No independent mathematical audit has been performed.

## References
1. M. Alberich-Carramiñana, A. Ferragut and J. Llibre, *Quadratic Planar Differential Systems with Algebraic Limit Cycles via Quadratic Plane Cremona Maps*, arXiv:1906.10171, publicly posted 2019-06-24, Proposition 5 and the discussion of phase portraits. https://arxiv.org/abs/1906.10171
2. A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803, publicly posted 2022-10-27, Theorem 1.2 and Case 5. https://arxiv.org/abs/2210.15803
3. J. Chavarriga, J. Llibre and J. Sorolla, *Algebraic limit cycles of degree 4 for quadratic systems*, Journal of Differential Equations **200** (2004), 206–244, DOI 10.1016/j.jde.2004.01.003 (bibliographic abstract inspected, full text unavailable).
4. NIST Digital Library of Mathematical Functions, §19.12, complete elliptic-integral asymptotics. https://dlmf.nist.gov/19.12
