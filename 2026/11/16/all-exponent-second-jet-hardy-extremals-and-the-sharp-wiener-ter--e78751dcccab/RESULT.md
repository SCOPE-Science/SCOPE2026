# All-exponent second-jet Hardy extremals and the sharp Wiener terminal threshold

## Finding

Let \(0<p<1\), \(q=2/p>2\), and \(f(z)=\sum_{j\ge0}a_j(f)z^j\in H^p(\mathbb D)\). For \(\tau\ge0\), let \(N_p(\tau)\) be the exact norm of \(f\mapsto a_0(f)+\tau a_2(f)\) on the unit ball of \(H^p\). Put \(\tau_c=1/(q-2)\) and \(r_*=1/(q-1)\).

For \(0\le\tau\le\tau_c\), let \(r\in[0,r_*]\) be the unique solution of \(\tau=r/[1-(q-1)r^2]\). Then
\[
 N_p(\tau)=\frac{1+q\tau r}{(1+r^2)^{q/2}}.
\]
For \(\tau\ge\tau_c\), writing \(\Delta=q^2-2(q-1)/[\tau(q-2)]\),
\[
 N_p(\tau)=\tau(q-1)\left(\frac{q-1}{\sqrt\Delta}\right)^{q-2}.
\]
The values agree at \(\tau=\tau_c\). For positive \(\tau<\tau_c\) the only norming function, up to a unimodular scalar, is
\[
 f(z)=\left(\frac{1+rz^2}{\sqrt{1+r^2}}\right)^q.
\]
For \(\tau>\tau_c\), precisely two norming functions occur, up to a unimodular scalar:
\[
 f_\pm(z)=(x\pm yz+wz^2)^q,\quad
 x=\frac{q-1}{\sqrt\Delta},\quad w=\frac1{\sqrt\Delta},\quad
 y=\sqrt{\frac{2(q-1)}\Delta\left(1-\frac1{\tau(q-2)}\right)}.
\]
Both polynomials defining the analytic powers are zero-free in the closed disk. At \(\tau=\tau_c\) the two branches coincide, and at \(\tau=0\) the norm is one and only constants are norming.

Define the fixed-origin second-coefficient frontier \(\Phi_2(p,t)=\sup\{\operatorname{Re}a_2(f):\|f\|_{H^p}\le1,\ f(0)=t\}\). Set
\[
 t_{\min}=\left(\frac{q-1}{q}\right)^q,\qquad
 t_*=\left(1+\frac1{(q-1)^2}\right)^{-q/2}.
\]
For all \(t\in[t_{\min},1]\), putting \(x=t^{1/q}\), the exact frontier is
\[
 \Phi_2(p,t)=
 \begin{cases}
 qx^{q-2}\left(\dfrac{q-1}2(1-x^2)+\dfrac{x^2}{2(q-1)}\right),&t_{\min}\le t\le t_*,\\[4pt]
 qx^{q-1}\sqrt{1-x^2},&t_*\le t\le1.
 \end{cases}
\]
In particular, if \(\Phi_1(p,t)\) is the known sharp first-coefficient frontier, then
\[
 \boxed{\Phi_2(p,t)=\Phi_1(p,t)\quad\text{for every }t_*\le t\le1.}
\]
The threshold \(t_*\) is sharp: equality fails for all \(t<t_*\) sufficiently close to \(t_*\). This settles the order-two case, for every \(0<p<1\), of the terminal-equality question posed by Brevig, Grepstad, and Instanes. The numerical form of the threshold was anticipated in that work; the new contribution is its proof, complete mixed-functional extremizers for all exponents, and the fixed-origin formula on the stated interval.

## Assumptions and scope

The Hardy quasi-norm is \(\|f\|_{H^p}=(\int_0^{2\pi}|f(e^{i\theta})|^p\,d\theta/(2\pi))^{1/p}\), using radial boundary limits. All exponent and parameter quantifiers are \(0<p<1\) and \(\tau\ge0\); no integer assumption is placed on \(q=2/p\). The powers of zero-free polynomials are the analytic branches positive at the origin. A norming function has unit quasi-norm and attains the modulus of the indicated linear functional. The frontier formula is **not asserted** for \(0\le t<t_{\min}\); terminal equality is established independently of such a classification.

## Proof

**Reduction from all Hardy functions.** Each Taylor coefficient is a continuous linear functional on \(H^p\); normal-family compactness and Fatou's lemma give a unit-quasi-norm extremizer for the nonzero functional \(a_0+\tau a_2\). The outer-extremal theorem of Brevig and Søvik [1, Theorem 1] applies for every \(0<p<1\), so every extremizer is outer, hence zero-free. It has an analytic \(q\)-th root \(h=f^{1/q}\in H^2\), with \(\|h\|_2=1\), since \(pq=2\). Conversely every zero-free \(H^2\) function produces an admissible \(q\)-th power; the coefficient inequality below is an upper bound for all such roots and its optimizers turn out zero-free.

Write \(h(z)=a+bz+cz^2+\cdots\). Direct Taylor expansion gives \(a_0(f)=a^q\) and \(a_2(f)=qa^{q-1}c+q(q-1)a^{q-2}b^2/2\). The triangle inequality and Parseval bound their linear combination by
\[
 F(x,y,w)=x^q+\tau qx^{q-1}w+\frac{\tau q(q-1)}2x^{q-2}y^2,
 \qquad x^2+y^2+w^2\le1,
\]
where \(x=|a|\), \(y=|b|\), \(w=|c|\). For \(\tau>0\), an optimizer has \(x>0\) and uses all coefficient mass; the tail must vanish. Equality of complex phases forces, after a common unimodular normalization, \(a,c>0\) and \(b\) real with either sign. Thus every equality case will be among the real triples maximizing \(F\).

**Exact scalar optimization.** For a fixed \(x\in(0,1]\), substitute \(y^2=1-x^2-w^2\). The expression is strictly concave in \(w\in[0,\sqrt{1-x^2}]\), with unconstrained maximizer \(w=x/(q-1)\). Define \(x_c=(q-1)/\sqrt{(q-1)^2+1}\). On \(0<x\le x_c\), the maximized expression is
\[
 G_<(x)=\frac{\tau q(q-1)}2x^{q-2}+
 \left(1-\frac{\tau q^2(q-2)}{2(q-1)}\right)x^q.
\]
Its derivative has the sign of an affine function of \(x^2\), positive near zero. If \(\tau\le\tau_c\) it is increasing up to \(x_c\). If \(\tau>\tau_c\) it has one interior maximum at \(x=(q-1)/\sqrt\Delta<x_c\); at this point \(w=x/(q-1)=1/\sqrt\Delta\) and \(y\) equals the displayed value. Substitution yields \(G_<(x)=\tau(q-1)x^{q-2}\) at this interior maximum.

On \(x_c\le x\le1\), \(y=0\) and \(w=\sqrt{1-x^2}\). Put \(r=w/x\in[0,r_*]\); then
\[
 G_>(r)=\frac{1+q\tau r}{(1+r^2)^{q/2}},\qquad
 \operatorname{sign}G_>'(r)=\operatorname{sign}(\tau[1-(q-1)r^2]-r).
\]
For \(\tau\le\tau_c\) the unique maximum is the stated root \(r\le r_*\), while the lower-\(x\) branch increases into it. For \(\tau>\tau_c\) the upper-\(x\) branch has its maximum at \(r=r_*\), where the lower-\(x\) branch is already decreasing toward the boundary, so the unique interior lower-\(x\) optimizer is globally optimal. At \(\tau_c\) both optimizers meet. This proves the norm formulas and exhausts the real equality cases.

**Analytic admissibility and equality rigidity.** The first-branch base \(1+rz^2\) has no zero in \(|z|\le1\) because \(r\le r_*<1\). In the second branch \(x>w>0\) and \(0<y<x+w\). The real quadratic Schur criterion therefore shows that \(x\pm yz+wz^2\) has no roots in the closed disk (equivalently, the reciprocal quadratic is Schur stable). By Parseval their \(H^2\) norms are one; their \(q\)-th powers have \(H^p\) quasi-norm one and attain the upper bounds. Strict radial optimization and equality in coefficient phases leave exactly one or two choices as claimed, with common unimodular phase disregarded. The case \(\tau=0\) follows from the sharp bound \(|f(0)|\le\|f\|_{H^p}\).

**Sharp fixed-origin frontier.** Every support extremizer above has positive origin \(f(0)=x^q\). The first branch runs continuously over \(x\in[x_c,1]\); the second runs over \(x\in((q-1)/q,x_c)\) as \(\tau\) increases from \(\tau_c\) to infinity. For any such \(t\), the support inequality \(a_0(f)+\tau\operatorname{Re}a_2(f)\le N_p(\tau)\), together with the exhibited maximizing function of origin \(t\), establishes the exact fixed-origin coefficient maximum. Computing \(a_2\) from the optimizing triples yields precisely the displayed two formulas. The endpoint \(t=t_{\min}\) follows by continuity and the limiting support inequality \(\Phi_2(p,t)\le\lim_{\tau\to\infty}N_p(\tau)/\tau\); the displayed limiting extremizer attains equality. The endpoint \(t=1\) is the constant function.

**Terminal equality and sharpness.** The exact \(\Phi_1\) formula in Brevig–Grepstad–Instanes [2, Theorem 12(ii)] gives \(\Phi_1(p,t)=qx^{q-1}\sqrt{1-x^2}\) for \(t\ge t_p\), with \(t_p\) strictly below \(2^{-1/p}\sqrt p(2-p)^{1/p-1/2}\). The latter is smaller than \(t_*\), because \(x_c^2>(q-1)/q\) for \(q>2\). Thus the high-origin \(\Phi_1\) branch holds throughout \([t_*,1]\) and matches \(\Phi_2\). Immediately below \(t_*\) it still holds, whereas the two expressions differ by the strictly positive square
\[
 \Phi_2(p,t)-\Phi_1(p,t)
 =\frac{q x^{q-2}}{2(q-1)}
 \left((q-1)\sqrt{1-x^2}-x\right)^2,
 \quad t<t_*\text{ sufficiently close to }t_*.
\]
Therefore no smaller terminal threshold works. This completes the proof.

## Verification

`CHECK.py` (standard-library Python) independently evaluates the two branches, normalizes the optimizer triples, tests their Taylor coefficients and fixed-origin junctions, and compares the proposed global bound against deterministic random real and complex triples. It passed 94,010 finite assertions on a sampled exponent and parameter grid. The infinite-dimensional reduction, branch exhaustiveness, and final equality are mathematical arguments above, not consequences of these tests.

## Relationship to prior work

Brevig and Søvik [1] establish outer extremality for arbitrary bounded linear functionals in \(H^p\), \(0<p<1\), but do not compute the present mixed second-jet functional. Brevig, Grepstad, and Instanes [2] give the complete first-coefficient frontier and ask explicitly whether higher coefficients coincide with it for origins sufficiently near one; they anticipate the order-two threshold using numerical and partial analytical evidence but leave the possible one-zero extremal case unresolved. The present proof turns their anticipated threshold into a theorem for **every** \(0<p<1\), using the subsequently available outer-extremal result and an exact scalar optimization. Brevig and Saksman [3] determine unconditional sharp coefficient norms, which do not imply the mixed-functional profile or terminal threshold. A published 2026 account of the mixed \(H^{1/2}\) second-jet problem already establishes the one-exponent slice and is not claimed anew here; the full open exponent range and the general analytic classification are the asserted advance.

## Limitations

No formula is claimed for the fixed-origin second-coefficient frontier below \(t_{\min}\), nor for Taylor orders exceeding two. The result depends on the published outer-extremal theorem [1] and the first-coefficient frontier [2], which are not reproved here. Historical originality might be affected by classical extremal-coefficient literature or unpublished calculations not fully searchable. Computational tests cover only finitely many sample exponents and triples. Independent mathematical audit has not been performed.

## References

[1] O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, arXiv:2610.21788, first publicly submitted October 15, 2026, Theorem 1. https://arxiv.org/abs/2610.21788

[2] O. F. Brevig, S. Grepstad, and S. M. Instanes, *F. Wiener’s trick and an extremal problem for \(H^p\)*, arXiv:2011.07790, first submitted November 16, 2020, Theorem 12 and Question 2. https://arxiv.org/abs/2011.07790

[3] O. F. Brevig and E. Saksman, *Coefficient estimates for \(H^p\) spaces with \(0<p<1\)*, arXiv:1905.09547, first submitted May 23, 2019. https://arxiv.org/abs/1905.09547
