# An orientation-reversing three-cycle sink window with quadratic onset and cubic collapse

## Finding
For the real polynomial diffeomorphism
\[
F_{a,b}(x,y,z)=(a-y^2-bz,x,y),\quad 0<b<1,\quad a\in\mathbb R,
\]
put \(c=a/(1+b)^2\). For \(c>7/4\), let \(t=\sqrt{4c-7}\), \(\phi(t)=t^3+t^2+7t\), and define \(t_-(b),t_+(b)\) as the unique positive solutions of
\[
\phi(t_-)=1-\left(\frac{1-b}{1+b}\right)^3,\qquad
\phi(t_+)=1+(1-b)^3.
\]
Set \(a_\pm(b)=(1+b)^2(7+t_\pm(b)^2)/4\). Then \(a_-<a_+\) and **exactly one primitive period-three orbit is a hyperbolic sink** if and only if
\[
\boxed{a_-(b)<a<a_+(b).}
\]
There are no real primitive period-three orbits for \(c<7/4\), one nonhyperbolic primitive orbit at \(c=7/4\), and two for \(c>7/4\). The other orbit is never attracting. The sink branch is not attracting immediately after its birth: it gains stability at \(a=a_-\) when a simple multiplier crosses \(-1\), and loses stability at \(a=a_+\) when a complex conjugate pair reaches the unit circle. At the second boundary the remaining multiplier equals \(-b^3\).

The two stability boundaries have different singular scales:
\[
\boxed{a_-(b)-\frac74(1+b)^2\sim\frac9{49}b^2\quad (b\downarrow0),}
\]
\[
\boxed{a_+(b)-a_-(b)\sim\frac{9t_0}{4\phi'(t_0)}(1-b)^3\quad (b\uparrow1),}
\]
where \(t_0\) is the unique positive root of \(\phi(t_0)=1\) and \(\phi'(t_0)=3t_0^2+2t_0+7\). Numerically \(t_0\approx0.139680581996\) and the second coefficient is about \(0.042829910805\). No nonlinear bifurcation or invariant-circle existence is asserted at the multiplier crossings.

## Assumptions and scope
All orbits and parameters are real; \(0<b<1\), with no phase-space boundedness restriction. A primitive period-three orbit consists of three distinct points of least period exactly three. A hyperbolic sink means all three eigenvalues of the return derivative \(DF^3\) have modulus strictly less than one. The scalar parameter \(c\) is not constrained except as stated; the physical parameter is \(a=(1+b)^2c\). Endpoints are excluded from the hyperbolic-sink claim. The map is invertible for \(b>0\), with Jacobian determinant \(-b\).

## Proof
**1. Exact reduction.** If \((x_n)\) is the first coordinate of a 3-periodic trajectory then the shift relations give \(x_{n+1}=a-x_{n-1}^2-bx_{n-2}\). Because \(x_{n-2}=x_{n+1}\) on this orbit,
\[
\frac{x_{n+1}}{1+b}=c-\left(\frac{x_{n-1}}{1+b}\right)^2.
\]
Thus, in the scaled coordinates \(u_n=x_n/(1+b)\), the three entries are permuted cyclically by \(q_c(u)=c-u^2\), with orientation reversed relative to the full map. Conversely any scalar 3-cycle \((u,v,w)\) under \(q_c\), where \(q_c(u)=v\), \(q_c(v)=w\), \(q_c(w)=u\), defines the full orbit from \((1+b)(u,v,w)\) under the rotation \((u,v,w)\mapsto(w,u,v)\). This correspondence is bijective up to cyclic choice of starting point.

**2. Exhaustive real orbit census.** The monic degree-six dynatomic polynomial is
\[
D_c(u)=\frac{q_c^3(u)-u}{q_c(u)-u}
=u^6-u^5+(1-3c)u^4+(2c-1)u^3
 +(3c^2-3c+1)u^2+(-c^2+2c-1)u
 -c^3+2c^2-c+1.
\]
Its discriminant, computed by the resultant or polynomial Euclidean algorithm, is
\[
\operatorname{disc}_uD_c=(4c-7)^3(16c^2-4c+7)^2.
\]
The second factor is strictly positive for every real \(c\). At \(c=0\), \(D_0(u)=(u^7+1)/(u+1)>0\) for all real \(u\) (the value at \(u=-1\) is seven). Since there are no multiple roots for \(c<7/4\), the number of real roots remains zero throughout that interval. For \(c\ge7/4\), set \(t=\sqrt{4c-7}\). Direct polynomial division gives \(D_c=G_+G_-\), with
\[
G_\epsilon(u)=u^3-\frac{1+\epsilon t}{2}u^2
 +\frac{-t^2+2\epsilon t-9}{4}u
 -\frac{t^2-1-\epsilon t(t^2+7)}8,\qquad \epsilon=\pm1.
\]
The discriminant of each cubic is \((t^2-\epsilon t+7)^2>0\), so each has three distinct real roots. Polynomial reduction shows \(G_\epsilon(q_c(u))\equiv0\pmod{G_\epsilon(u)}\). No real root of \(D_c\) is fixed by \(q_c\): at a fixed point the quotient has value \(1+q_c'(u)+q_c'(u)^2>0\). Thus each cubic's three roots form a single primitive 3-cycle. For \(t>0\) the two cubics are distinct and have disjoint roots; at \(t=0\) they coincide, giving one primitive cycle. This proves the complete count.

**3. Exact multiplier polynomial.** The scalar multiplier of the cycle arising from \(G_\epsilon\), computed from its constant term, is
\[
m_\epsilon=(-2u)(-2v)(-2w)
=8-4c+\epsilon4c\sqrt{4c-7}.
\]
The derivative at a point of second coordinate \(y\) is \(J(y)=\begin{pmatrix}0&-2y&-b\\1&0&0\\0&1&0\end{pmatrix}\). Direct matrix multiplication for three successive steps yields
\[
\det(\lambda I-DF^3)=(\lambda+b)^3+8\lambda xyz
=(\lambda+b)^3-(1+b)^3m_\epsilon\lambda,
\]
where \(x,y,z\) are the three physical cycle coordinates. At \(c=7/4\) both \(m_\epsilon=1\), so the return characteristic has \(\lambda=1\) and the cycle is not a hyperbolic sink.

**4. Sharp Schur inequalities.** Write \(M=(1+b)^3m_\epsilon\). The cubic is \(p(\lambda)=\lambda^3+3b\lambda^2+(3b^2-M)\lambda+b^3\). The four strict real cubic Schur conditions are
\[
|b^3|<1,\quad p(1)>0,\quad -p(-1)>0,\quad
1-(3b^2-M)+3b\,b^3-b^6>0.
\]
Because \(0<b<1\), they reduce exactly to
\[
-(1-b)^3<m_\epsilon<\left(\frac{1-b}{1+b}\right)^3.
\]
For \(c>7/4\), \(m_+\ge1\), excluding the \(+\) branch. The other multiplier is \(m_-=1-\phi(t)\), strictly decreasing from one to minus infinity as \(t>0\) increases, since \(\phi'(t)>0\). Therefore the sink inequality is equivalent to \(t_-<t<t_+\), yielding exactly the asserted nonempty interval.

At \(a=a_-\), \(M=(1-b)^3\) and \(p(-1)=0\); \(p'(-1)=(1-b)^2(2+b)>0\), so the crossing multiplier is simple and equals \(-1\). At \(a=a_+\), \(M=-(1-b^2)^3\) and the exact factorization is
\[
p(\lambda)=(\lambda+b^3)\left(\lambda^2+(3b-b^3)\lambda+1\right).
\]
Since \(0<3b-b^3<2\), the quadratic roots form a distinct conjugate pair on the unit circle, while \(-b^3\) lies strictly inside. This describes the two stability boundaries without asserting their nonlinear criticalities.

**5. Both singular limits.** As \(b\downarrow0\), \(1-((1-b)/(1+b))^3=6b+O(b^2)\). Since \(\phi(t)=7t+O(t^2)\), \(t_-=(6/7)b+O(b^2)\); hence \(a_--\tfrac74(1+b)^2=(1+b)^2t_-^2/4\sim9b^2/49\). As \(b\uparrow1\), write \(\varepsilon=1-b\). The two right-hand sides defining \(t_\pm\) differ by \(\varepsilon^3+(\varepsilon/(2-\varepsilon))^3=(9/8)\varepsilon^3+o(\varepsilon^3)\). Both roots tend to \(t_0\), so the mean value theorem gives \(t_+-t_-\sim(9/8)\varepsilon^3/\phi'(t_0)\). Therefore \(a_+-a_-=(1+b)^2(t_+^2-t_-^2)/4\sim9t_0\varepsilon^3/(4\phi'(t_0))\), as required. \(\square\)

## Verification
Run `python verify.py` using Python 3 with SymPy installed. It checks the dynatomic identity and discriminant; exact cubic factorization, discriminants, and invariance under the scalar quadratic map; scalar multiplier expressions; the three-step Jacobian polynomial and the unit-circle factorization; and the two asymptotic prefactors. Eighteen supplementary direct numerical Schur/Floquet comparisons exercise three distinct coupling values. Algebraic and inequality proofs above apply to the full parameter range; sample computations do not serve as a proof of real-root counts or infinite-parametric stability.

## Relationship to prior work
Muni's 2024 study [1] analyzes this orientation-reversing generalized Hénon map and its hyperchaotic routes, especially saddle fixed points and mode-locked periods four and eight, without a closed complete period-three stability window. Muni–Banerjee [2] analyzes mode-locked four/eight orbit bifurcations of the same map. Zheng et al. [3] study the sign-reversed \(+bz\) convention, primarily fixed points and numerical periodic windows. A previously available exact period-three classification for \(a-y^2+bz\) with \(0\le b<1\) [4] provides the scalar three-cycle census and a different, orientation-preserving sink interval; it neither states nor implies the present flip-delayed orientation-reversing window or its quadratic and cubic endpoint laws. The orientation-reversing period-two index theorem [5] concerns distinct orbit period and is likewise not a covering result. The scalar period-three dynatomic factorization is classical background here, not claimed as a new scalar theorem. The contribution is the complete Schur interval with its two different Floquet endpoint mechanisms and singular boundary scaling for \(-bz\).

## Limitations
All assertions are confined to \(0<b<1\) and primitive period-three orbits; they do not classify global basins, invariant circles, or higher periods. At the two boundary curves the derivative is nonhyperbolic, and no nonlinear flip/Neimark–Sacker bifurcation theorem is claimed. The underlying scalar period-three census was known in other contexts. Earlier general studies, particularly Richter [6], may contain relevant further computations; only preview/abstract and figure material of that paper was accessible during comparison. A full originality assessment requires checking it and any unindexed period-three calculations. Independent validation has not been conducted.

## References
[1] S. S. Muni, *Pathways to hyperchaos in a three-dimensional quadratic map*, arXiv:2406.08317 (first public version 12 June 2024), Sections 1–2. https://arxiv.org/abs/2406.08317

[2] S. S. Muni and S. Banerjee, *Bifurcations of mode-locked periodic orbits in three-dimensional maps*, arXiv:2304.10210v1 (20 April 2023), Section IV. https://arxiv.org/html/2304.10210v1

[3] J. Zheng, Z. Wang, Y. Li and J. Wang, *Bifurcations and chaos in a three-dimensional generalized Hénon map*, Advances in Difference Equations 2018:185, DOI:10.1186/s13662-018-1622-y, Sections 2–4. https://doi.org/10.1186/s13662-018-1622-y

[4] *An exact primitive three-cycle classification in a three-dimensional generalized Hénon map with positive last-coordinate coupling*, privately archived result, source claim ID 16224d86-4e1d-48f8-bcc7-42dcca7dade4 (comparison limited to the claim).

[5] *Exact saddle-index transition of the unique two-cycle in a three-dimensional Hénon map*, public mathematical result. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-saddle-index-transition-of-the-unique-two-cycle-in-a-three--de1f76d39e95/RESULT.md

[6] H. Richter, *The generalized Hénon maps: examples for higher-dimensional chaos*, International Journal of Bifurcation and Chaos 12 (2002), 1371–1384, DOI:10.1142/S0218127402005121. https://doi.org/10.1142/S0218127402005121
