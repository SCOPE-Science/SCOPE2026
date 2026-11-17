# Exact prime-three census and the sharp attracting tongue of a three-dimensional generalized Hénon map

## Finding
For the real quadratic three-dimensional map
\[
T_{a,b}(x,y,z)=(a-y^2+bz,\,x,\,y),\qquad a>0,\quad 0\le b<1,
\]
put \(k=1-b\), \(A=a/k^2\), and for \(A\ge7/4\) set
\[
U_{\pm}(A)=\frac{A-2\pm A\sqrt{4A-7}}2.
\]
There are no real primitive period-three orbits when \(A<7/4\), precisely one when \(A=7/4\), and precisely two when \(A>7/4\) (orbits are counted up to cyclic rotation, not by their three points). The two orbit coordinate products are \(P_{\pm}=k^3U_{\pm}(A)\).

For each \(0\le b<1\), there is exactly one \(A_*(b)\in(7/4,2)\), characterized by
\[
\boxed{U_+(A_*(b))=\frac{(1+b)^3}{8}},
\]
and the map has **exactly one hyperbolic attracting primitive period-three orbit** if and only if
\[
\boxed{\frac74<\frac{a}{(1-b)^2}<A_*(b).}
\]
All other real primitive period-three orbits are non-attracting. The threshold \(A_*(b)\) is strictly increasing in \(b\) and tends to \(2\) as \(b\uparrow1\), although the attracting window in the original parameter \(a\) contracts to zero at quadratic order.

At the upper threshold, for \(b>0\), the two critical three-step multipliers form the unit conjugate pair \(e^{\pm i\theta(b)}\), and the remaining multiplier is \(b^3\), where
\[
\boxed{\cos\theta(b)=\frac{3b-b^3}{2}}.
\]
At the singular endpoint \(b=0\), the corresponding multipliers are \(i,-i,0\). This is a precise period-three stability boundary and a universal unit-circle frequency law; no claim of a nonlinear Neimark–Sacker normal form is made.

## Assumptions and scope
The state space is all of \(\mathbb R^3\); the parameters satisfy \(a>0\) and \(0\le b<1\). A primitive period-three orbit has least period exactly three under \(T_{a,b}\). A hyperbolic attracting orbit means all three eigenvalues of its three-step derivative lie strictly inside the unit disk. At either threshold, neutral periodic points are not counted as hyperbolic attracting. No statement is made about other primitive periods, basins, or global attractors.

## Proof
**1. Reduction without dropping periodic points.** Write a three-periodic scalar first-coordinate sequence as \(p,q,r,p,q,r,\ldots\). The recurrence \(x_{n+1}=a-x_{n-1}^2+b x_{n-2}\) gives \(kq=a-r^2\), \(kr=a-p^2\), and \(kp=a-q^2\). After dividing the coordinates by \(k\), their cyclic equations are exactly those of \(f_A(u)=A-u^2\) and its third iterate. Conversely every real three-cycle of \(f_A\) produces one real three-cycle of \(T_{a,b}\), with identical orbit cardinality; cyclic order is reversed but this does not change the coordinate product.

**2. Exact census and product formula.** Polynomial division yields the monic degree-six polynomial
\[
\begin{aligned}
H_A(u)&=\frac{f_A^3(u)-u}{f_A(u)-u}\\
&=u^6-u^5+(1-3A)u^4+(2A-1)u^3\\
&\quad +(3A^2-3A+1)u^2+(-A^2+2A-1)u\\
&\quad-A^3+2A^2-A+1.
\end{aligned}
\]
For any zero \(u\) of this polynomial, the product \(W=u f_A(u)f_A^2(u)\) obeys the **exact elimination identity**
\[
W^2+(2-A)W-A^3+2A^2-A+1=0.
\]
This follows by reducing the left side modulo \(H_A(u)\) and obtaining zero; the converse count is supplied below by factorization. Its two roots are \(U_{\pm}(A)\), and its discriminant is \(A^2(4A-7)\). Since \(A>0\), no real three-cycle is possible for \(A<7/4\).

For \(A\ge7/4\), let \(t=\sqrt{4A-7}\), and define
\[
\begin{aligned}
S_{\pm}&=\frac{1\mp t}{2},\\
Q_{\pm}&=\frac{S_{\pm}^2+S_{\pm}-3A}{2},\\
C_{\pm}(u)&=u^3-S_{\pm}u^2+Q_{\pm}u-U_{\pm}.
\end{aligned}
\]
A direct expansion gives \(H_A=C_+C_-\). Their discriminants, upon substituting \(A=(t^2+7)/4\), are \((t^2+t+7)^2\) and \((t^2-t+7)^2\). Both are strictly positive for \(t\ge0\). Thus for \(t>0\), each cubic has three distinct real roots, and the two cubics are disjoint because their constant-product values \(U_+\ne U_-\); they are exactly the two primitive three-cycles. At \(t=0\), the two cubics coincide, with three distinct real roots, giving one neutral three-cycle. Fixed points are not accidentally counted here: a shared zero of \(f_A(u)-u\) and \(H_A(u)\) requires the multiplier of that fixed point to have cube one, so the real multiplier must be one, which requires \(A=-1/4\), outside the domain.

**3. Three-step Floquet polynomial.** The one-step Jacobian is
\[
J(y)=\begin{pmatrix}0&-2y&b\\1&0&0\\0&1&0\end{pmatrix}.
\]
If \(p,q,r\) are the three successive second coordinates on any period-three orbit, direct matrix multiplication shows
\[
\boxed{\det(\lambda I-J(p)J(q)J(r))=(\lambda-b)^3+8pqr\lambda.}
\]
In the normalized product notation, set \(c=8k^3U\). The characteristic polynomial becomes
\(\lambda^3-3b\lambda^2+(3b^2+c)\lambda-b^3\).

**4. Exact cubic Schur test.** The real monic-cubic Jury–Schur inequalities are \(|a_3|<1\), \(1+a_1+a_2+a_3>0\), \(1-a_1+a_2-a_3>0\), and \(1-a_2+a_1a_3-a_3^2>0\). Inserting \(a_1=-3b\), \(a_2=3b^2+c\), \(a_3=-b^3\), with \(0\le b<1\), reduces these inequalities *equivalently* to
\[
-(1-b)^3<c<(1-b^2)^3.
\]
Because \(c=8(1-b)^3U\), this is exactly
\[
\boxed{-\frac18<U<\frac{(1+b)^3}{8}}.
\]
For \(A>7/4\), \(U_-<-1/8\): the derivative of \(U_-\) is negative on the full interval, and its value at \(7/4\) is \(-1/8\). On the other branch, \(U_+\) is strictly increasing from \(-1/8\) to \(U_+(2)=1\), while \((1+b)^3/8<1\). Hence there exists a unique \(A_*(b)\in(7/4,2)\), and the asserted sharp stability region and uniqueness follow. Since the right side increases strictly with \(b\), so does \(A_*(b)\); it tends to two, and the physical interval has width \((1-b)^2(A_*(b)-7/4)\sim(1-b)^2/4\).

**5. Upper boundary spectrum.** At \(A=A_*(b)\), \(c=(1-b^2)^3\). The cubic has root \(\lambda=b^3\); the other two have product one and sum \(3b-b^3\), hence \(e^{\pm i\theta(b)}\) with the stated cosine. For \(0<b<1\), this cosine lies strictly between zero and one; at \(b=0\) the polynomial is \(\lambda(\lambda^2+1)\), giving \(0,i,-i\). The unit-circle pair moves outside the disk past the upper boundary by the strict Jury criterion; this does not assert existence or criticality of nearby invariant curves.

## Verification
The included reproducibility script \(`check.py`\) performs symbolic expansion of the dynatomic factorization, discriminants, the eliminated product equation, the three-step matrix characteristic polynomial, and the cubic Schur expressions. It also tests rational parameter examples on both sides of the stable threshold against numerical Floquet eigenvalues; these numerical examples corroborate, rather than prove, the global statements. The infinite parameter claims follow from the explicit algebra and positivity/monotonicity arguments given above.

## Relationship to prior work
Zheng, Wang, Li and Wang (2018) specify exactly this map and analyze fixed points, local fold/flip/Neimark–Sacker bifurcations, and numerical periodic windows. Their accessible complete article does not present the primitive period-three census or a sharp period-three sink tongue. Muni (2024) investigates routes to higher-dimensional chaos for related three-dimensional quadratic maps, including the present generalized Hénon map, but its indexed abstract alone does not adjudicate full-document novelty; it is not used for a whole-document negative assertion. Classical one-dimensional quadratic-map period-three algebra is background, and the period-three existence threshold is not claimed novel in isolation. The contribution is the exact full three-dimensional three-cycle stability classification and the unit-circle crossing law with delay coupling.

## Limitations
These results have not been independently audited or given publication-priority certification. A 2002 overview by Richter, identified from its abstract, could not be examined in full; any equivalent unpublished, inaccessible, or non-indexed calculation remains a publication-priority risk. The analysis is confined to \(a>0\), \(0\le b<1\) and primitive three-cycles; it does not classify higher-period orbits, global attractors, or nonlinear criticality at the neutral threshold. The boundary case \(b=1\) is excluded because the normalization degenerates.

## References
- J. Zheng, Z. Wang, Y. Li and J. Wang, *Bifurcations and chaos in a three-dimensional generalized Hénon map*, Advances in Difference Equations **2018**, article 185 (first online 2018-05-16). https://doi.org/10.1186/s13662-018-1622-y
- S. S. Muni, *Pathways to hyperchaos in a three-dimensional quadratic map*, arXiv:2406.08317 (posted 2024-06-12). https://arxiv.org/abs/2406.08317
- H. Richter, *The generalized Hénons: Examples for higher-dimensional chaos*, International Journal of Bifurcation and Chaos **12** (2002), 1371–1384. https://doi.org/10.1142/S0218127402005121
