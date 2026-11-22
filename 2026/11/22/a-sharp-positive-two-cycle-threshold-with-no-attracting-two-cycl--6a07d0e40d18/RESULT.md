# A sharp positive two-cycle threshold with no attracting two-cycle in a modified Lorenz Euler map

## Finding
For the real planar polynomial map
\[
F_a(x,y)=\bigl(x(1+a-ax-y),x^2\bigr),\qquad a>0,
\]
let \(a_*\) be the unique positive root of
\[
3a^3-10a^2-8a-4=0 \quad (a_*=4.0691882839\ldots).
\]
There is **no strictly positive primitive period-two orbit** when \(0<a\leq a_*\), and **exactly one** when \(a>a_*\). That orbit is never locally attracting: its two-step Jacobian always has spectral radius strictly greater than one. For \(a>a_*\), put
\[
B=a^2-a-3,\quad \Delta=(a^2-3a-1)(a^2+a-1),\quad
v=\frac{B-\sqrt\Delta}{2},\quad u=1+\frac{v+2}{a},
\]
\[
p=\frac{u+\sqrt{u^2-4v}}2,\qquad
q=\frac{u-\sqrt{u^2-4v}}2.
\]
Then the unique positive primitive two-cycle is
\[
(p,q^2)\longmapsto(q,p^2)\longmapsto(p,q^2),\qquad p>q>0.
\]
Thus the positive two-cycle created at the fixed-point flip never supplies a stable two-state alternation at this natural unit Euler step. The result says nothing about longer cycles or global attraction.

## Assumptions and scope
The original modified reduced Lorenz Euler map is
\[
(x,y)\mapsto\left((1+ah)x-hxy-ahx^2,\,(1-h)y+hx^2\right),
\]
with \(a>0\) and \(h>0\). We set the physical step to \(h=1\), at which the second component resets to the preceding squared first component. Strict positivity means both coordinates at both cycle points are positive. A primitive two-cycle has least period exactly two. Stability means linear (Floquet) attraction for the second iterate; spectral radius greater than one excludes local asymptotic attraction.

## Proof
**Exact cycle elimination.** Write a putative strictly positive two-cycle as \((p,q^2)\), \((q,p^2)\). This form is necessary because the second component of \(F_a\) is the square of the first. The two first-coordinate equations are
\[
q=p(1+a-ap-q^2),\qquad p=q(1+a-aq-p^2).
\]
Define \(u=p+q\) and \(v=pq\). Addition gives \(a(u-u^2+2v)-uv=0\). Subtraction, using \(p\ne q\), gives \(v=a(u-1)-2\). Eliminating \(u\) yields
\[
P_a(v)=v^2-(a^2-a-3)v+(a+2)=0,
\qquad u=1+\frac{v+2}{a}.
\]
Conversely, each positive root \(v\) of this quadratic for which \(u>0\) and \(u^2-4v>0\) reconstructs a distinct positive primitive two-cycle, because the two symmetric equations recover the original two equations when \(p\ne q\). There are no other positive two-cycles.

**Exactly one creation threshold.** The discriminant of \(P_a\) factors as \(\Delta=(a^2-3a-1)(a^2+a-1)\). Put \(a_\Delta=(3+\sqrt{13})/2\). For \(0<a\leq(\sqrt5-1)/2\), both real roots of \(P_a\), when present, are negative because their sum \(a^2-a-3\) is negative and their product \(a+2\) is positive. For \((\sqrt5-1)/2<a<a_\Delta\), \(\Delta<0\). At \(a=a_\Delta\) the repeated positive \(v\)-root gives \(u^2-4v=3(1-\sqrt{13})/2<0\).

For \(a>a_\Delta\), both \(v_\pm=(B\pm\sqrt\Delta)/2\) are strictly positive. With \(u_\pm=1+(v_\pm+2)/a\), define \(d_\pm=u_\pm^2-4v_\pm\). Direct polynomial elimination gives
\[
\operatorname{Res}_u\left(-au^2+(a^2+a+1)u-a^2-2a,\quad u^2-4[a(u-1)-2]\right)
=-(a+2)(3a^3-10a^2-8a-4).
\]
Hence either \(d_+\) or \(d_-\) can vanish at only one positive \(a\), namely \(a_*\in(4,5)\) (Descartes' rule gives one positive cubic root). Both discriminants are negative at \(a_\Delta\). At \(a=5\), explicit substitution gives
\[
d_-(5)=\frac{-1089+207\sqrt{29}}{50}>0,
\]
while \(d_+(5)<0\). Continuity, the unique possible zero, and the fact that \(v_+>v_-\) for \(a>a_\Delta\) prove \(d_+<0\) throughout, while \(d_-<0\) before \(a_*\), is zero at \(a_*\), and is positive thereafter. At equality \(p=q\) is a fixed point rather than a primitive orbit. This proves the complete positive two-cycle census.

**No attracting positive two-cycle.** For \(a>a_*\) take \(v=v_-(a)\). The one-step Jacobian is
\[
J(x,y)=\begin{pmatrix}1+a-2ax-y&-x\\2x&0\end{pmatrix}.
\]
For the two-cycle, set \(K=J(q,p^2)J(p,q^2)\). Thus \(\det K=4p^2q^2=4v^2\). Write \(B=a^2-a-3\) and \(C=a+2\). The smaller root satisfies \(v> C/B\), and differentiation of \(P_a(v)=0\) gives
\[
v'(a)=\frac{(2a-1)v-1}{2v-B}<0,
\]
where the numerator is positive because \((2a-1)C/B>1\) and the denominator is negative. Since \(v(a_\Delta)=a_\Delta-1\) and \(v(a)\to0\), \(v\) crosses \(1/2\) exactly once at
\[
a_d=\frac{3+\sqrt{39}}2=4.622498999\ldots,
\]
obtained from \(P_a(1/2)=(-2a^2+6a+15)/4\). Therefore \(a_*<a<a_d\) implies \(\det K>1\), already excluding attraction.

For \(a\ge a_d\), a stronger exact sign certificate applies. Put \(T=\operatorname{tr}K\). Using the two-cycle relations,
\[
T=1-\frac{a(u^3-3uv)}{v}+a^2v-2(u^2-2v),\qquad u=1+\frac{v+2}{a}.
\]
Let \(H(a,v)=a^2v(1+T+4v^2)\); substituting the displayed \(u\) makes \(H\) a polynomial. Direct expansion and elimination give
\[
\operatorname{Res}_v(P_a(v),H(a,v))=-a^2(a+2)Q(a),
\]
where
\[
Q(a)=5a^8-14a^7-55a^6+60a^5+93a^4-86a^3-72a^2+22a+10.
\]
Every coefficient of \(Q(t+9/2)\) is strictly positive, so \(Q(a)\ne0\) for \(a\ge9/2\). Consequently \(1+T+\det K\) has no zeros on \([a_d,\infty)\). At \(a=5\), it is
\[
1+T+\det K=\frac{39269-7347\sqrt{29}}{50}<0.
\]
By continuity, \(1+T+\det K=\det(I+K)<0\) for every \(a\ge a_d\). Since this is a real \(2\times2\) matrix, one Floquet multiplier is real and less than \(-1\), and the other is greater than \(-1\). In particular the two-cycle is never attracting, including \(a=a_d\).

## Verification
Run `python checker.py` with SymPy. The self-contained checker verifies the symmetric elimination, discriminant factorization, cubic and eighth-degree resultants, positivity of the shifted polynomial, exact sign witnesses and sample reconstruction identities. These exact algebraic identities are supplemental checks of the written proof; finite samples are diagnostics only. No numerical experiment is used to claim the complete census or global instability.

## Relationship to prior work
Al-Kaff et al. (2024) introduce the modified reduced Lorenz Euler map, classify fixed-point stability and analyze local flip and Neimark–Sacker bifurcations. They do not establish the global strictly positive primitive-two census on \(h=1\) or prove that the unique existing two-cycle can never be a sink. Elabbasy, Elsadany and Zhang (2014) analyze the earlier *unmodified* discrete reduced Lorenz system; that map does not have the additional quadratic self-limitation term and its statements do not give this theorem. Generic local flip criteria also do not imply global uniqueness or instability for all larger \(a\).

## Limitations
The theorem is restricted to the unit Euler step and the strictly positive quadrant. Negative or mixed-sign two-cycles, other step sizes, periods three or higher, basin geometry, and full nonlinear dynamics are not classified. The model arises from Euler discretization, so the unstable discrete two-cycle does not describe periodic behavior of the underlying continuous system. The scientific argument has not undergone independent validation; equivalently formulated work not found through indexed searches may exist.

## References
- M. O. Al-Kaff, G. AlNemer, H. A. El-Metwally, A.-E. A. Elsadany and E. M. Elabbasy, “Dynamic Behavior and Bifurcation Analysis of a Modified Reduced Lorenz Model,” *Mathematics* 12 (2024), 1354, https://doi.org/10.3390/math12091354 (online 29 April 2024).
- E. M. Elabbasy, A. A. Elsadany and Y. Zhang, “Bifurcation analysis and chaos in a discrete reduced Lorenz system,” *Applied Mathematics and Computation* 228 (2014), 184–194, https://doi.org/10.1016/j.amc.2013.11.088 (different, unmodified map).
