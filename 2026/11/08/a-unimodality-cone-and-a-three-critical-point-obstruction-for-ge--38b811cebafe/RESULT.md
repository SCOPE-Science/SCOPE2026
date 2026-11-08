# A unimodality cone and a three-critical-point obstruction for geometric four-block weighted shifts

## Finding
For real parameters \(0<d<1\), \(a,c>0\), and \(b\ge\sqrt d\), consider the positive geometrically decaying four-block unilateral shift with weights
\[
  (1,a,b,c,d,ad,bd,cd,d^2,ad^2,bd^2,cd^2,\ldots).
\]
Its geometric-vector numerical-radius lower bound
\[
 F(z)=\frac{(1-z)\sqrt z\,(1+az+bz^2+cz^3)}{1-dz^4},\qquad 0<z<1,
\]
has exactly one critical point on \((0,1)\). This is a strict global maximum, lying in \((1/3,1)\). Consequently the lower-bound optimization for this four-parameter family reduces to the unique real root of the explicit polynomial in the proof.

The middle-block hypothesis is substantive: for the strictly positive weights determined by
\[
 d=\frac{49}{50},\qquad a=b=\frac1{1000},\qquad c=\frac{73}{100},
\]
the same positive lower-bound function has **at least three distinct critical points in** \((1/3,1)\). The theorem makes no assertion that \(b\ge\sqrt d\) is a necessary or sharp universal threshold.

## Assumptions and scope
All operators act on the complex Hilbert space \(\ell^2(\mathbb N)\). The weighted forward shift \(T\) has \(Te_n=w_ne_{n+1}\) and positive weights \(w_{4k+1}=d^k\), \(w_{4k+2}=ad^k\), \(w_{4k+3}=bd^k\), \(w_{4k+4}=cd^k\), for every integer \(k\ge0\). It is compact. For \(0<z<1\), the vector \(v(z)_n=(1-z)^{1/2}z^{(n-1)/2}\) has norm one and satisfies \(\langle Tv(z),v(z)\rangle=F(z)\). Therefore \(w(T)\ge\max_{0<z<1}F(z)\). The claim concerns this natural trial-vector bound, not the exact operator numerical radius.

## Proof
Write \(u=\sqrt d\), so \(0<u<1\), and set, for \(k=0,1,2,3\),
\[
 G_k(z)=z^k\left((2k+1)-(2k+3)z+u^2z^4\bigl((7-2k)-(5-2k)z\bigr)\right).
\]
Differentiation gives
\[
  2\sqrt z\,(1-u^2z^4)^2F'(z)
  =G_0(z)+aG_1(z)+bG_2(z)+cG_3(z). \tag{1}
\]
Introduce
\[
 h(z)=\frac{z}{1-z}-\frac12-\frac{4u^2z^4}{1-u^2z^4}.
\]
Then
\[
 G_k(z)=2z^k(1-z)(1-u^2z^4)\bigl(k-h(z)\bigr). \tag{2}
\]
In particular, \(h(0+)=-1/2\), \(h(1-)=+\infty\), and \(h(1/3)<0\). Moreover
\[
 h'(z)=\frac1{(1-z)^2}-\frac{16u^2z^3}{(1-u^2z^4)^2}>0.
\]
Indeed, AM–GM gives \(1+z+z^2+z^3\ge4z^{3/2}\), whence
\(1-u^2z^4>1-z^4\ge4(1-z)z^{3/2}>4u(1-z)z^{3/2}\).
Consequently, for each \(k=0,1,2,3\), \(G_k\) has one zero \(r_k\in(1/3,1)\), with \(r_0<r_1<r_2<r_3\), positive before it and negative after it.

For differentiable functions, use \(W(P,Q)=P'Q-PQ'\). Direct polynomial expansion (reproducible in the accompanying exact-arithmetic script) gives
\[
\begin{aligned}
-W(G_0+uG_2,G_3)&=z^2(1-u^2z^4)Q_A(u,z),\\
-W(G_1,G_3)&=2z^3(1-u^2z^4)Q_{13}(u,z),\\
-W(G_2,G_3)&=z^4(1-u^2z^4)Q_{23}(u,z),
\end{aligned} \tag{3}
\]
where
\[
\begin{aligned}
Q_A={}&u^3z^8-6u^3z^7-3u^3z^6+15u^2z^6-18u^2z^5-21u^2z^4\\
 &+63uz^4-90uz^3+35uz^2+81z^2-78z+21,\\
Q_{13}={}&u^2z^4(3z^2-6z-5)+45z^2-58z+21,\\
Q_{23}={}&u^2z^4(z^2-6z-3)+63z^2-90z+35.
\end{aligned}
\]
All three are strictly positive for \(0<z,u<1\). Here is a short analytic certificate. The last two decrease with \(u\); at \(u=1\) their respective values are
\[
 (1-z)^3(21+5z-3z^2-3z^3),\quad
 (1-z)^3(35+15z+3z^2-z^3),
\]
both positive. As a polynomial in \(u\), \(Q_A\) is strictly concave, since
\[
 \frac{\partial^2 Q_A}{\partial u^2}=
 6uz^6(z^2-6z-3)+6z^4(5z^2-6z-7)<0.
\]
Its endpoint values are
\[
 Q_A(0,z)=3(27z^2-26z+7)>0,
 \quad Q_A(1,z)=(1-z)^3(21-15z+8z^2+3z^4-z^5)>0.
\]
The first quadratic has negative discriminant and positive leading coefficient; the second expression is manifestly positive on \((0,1)\). Concavity yields \(Q_A(u,z)>0\).

Since \(b\ge u\), the Wronskians in (3) imply
\[
  -W(G_0+aG_1+bG_2,G_3)
  =z^2(1-u^2z^4)\bigl[Q_A+(b-u)z^2Q_{23}+2az Q_{13}\bigr]>0.\tag{4}
\]
Let \(H=G_0+aG_1+bG_2\). On \((0,r_3)\), \(G_3>0\), and (4) shows that \(H/G_3\) decreases strictly. This ratio tends to \(+\infty\) as \(z\downarrow0\), because \(H(0)=1\) and \(G_3(z)\sim7z^3\). It tends to \(-\infty\) as \(z\uparrow r_3\), because the three earlier zero locations yield \(H(r_3)<0\). Thus \(H/G_3+c\) vanishes exactly once on \((0,r_3)\). For \(z\ge r_3\), all \(G_k(z)\le0\), with at least one strictly negative, so (1) has no other zero. Since (1) is positive at \(z=1/3\), the unique critical point lies in \((1/3,1)\). Finally \(F(z)>0\) inside the interval and \(F(z)\to0\) at both ends, so it is the unique strict global maximum.

For the obstruction, keep the displayed strictly positive rational parameters and let \(G=G_0+aG_1+bG_2+cG_3\), now with \(u^2=d=49/50\). Exact rational evaluations give
\[
\begin{aligned}
G(1/2)&=41293/3200000>0,\\
G(3/5)&=-6831851/976562500<0,\\
G(3/4)&=3588259/1638400000>0,\\
G(9/10)&=-6947621417/250000000000<0.
\end{aligned}
\]
By the intermediate value theorem, \(G\) has a zero in each of the three disjoint intervals determined by these four points. By (1), these are three distinct critical points of \(F\), all in \((1/3,1)\).

## Verification
Running `python verify_polynomials.py` with SymPy checks eight exact polynomial identities, including all Wronskian factorizations and endpoint formulas, and verifies four exact rational signs. The successful output begins `FOUR_PERIOD_TRIAL_EXACT_OK 8 identities 4 rational sign certificates`. Every positivity step needed beyond polynomial identities is supplied analytically above. The checker is corroboration; no finite parameter sample is used to establish the universal theorem.

## Relationship to prior work
Ghosh, Birbonshi and Ojha (arXiv:2608.17486v1, 18 August 2026) obtained the geometric-vector lower bound for the more restricted weights \((1,sq,q^2,tq^3,q^4,\ldots)\) and posed unrestricted uniqueness of its critical polynomial as Open Question 1. A separate public proof has since affirmatively resolved that **restricted scalar question**. The present result does not claim that resolution as new: its free middle coefficient and free block decay cover the full cone \(b\ge\sqrt d\), beyond the earlier equalities \(b=\sqrt d\) and \(d=q^4\), and the explicit three-critical-point example shows why unrestricted positivity of four-block weights does not suffice. Earlier work on two-period generalized geometric weights and geometric shifts does not state this four-block cone-and-obstruction pair. Searches and comparison are not a proof of publication priority.

## Limitations
The result gives the unique maximizer of a particular lower bound for \(w(T)\), not the maximizing vector or the exact numerical radius of \(T\). Neither necessity nor sharpness of the sufficient inequality \(b\ge\sqrt d\) is claimed. The example proves at least three critical points, without classifying every admissible parameter regime or all roots outside \((1/3,1)\). Publication priority has not undergone independent review; a more general historical theorem on ratios of positive polynomials could conceivably subsume part of the positivity argument.

## References
1. A. Ghosh, R. Birbonshi, S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1 (public 2026-08-18), https://arxiv.org/abs/2608.17486 .
2. *Ghosh, Birbonshi and Ojha: the unique polynomial root*, public exact scalar-resolution record, https://www.trureturing.org/research/ghosh-birbonshi-ojha-2026-weighted-shift-root-uniqueness/ .
3. B. Chakraborty and S. Ojha, *On the numerical radius of weighted shift operators with generalized geometric weights*, Journal of Mathematical Analysis and Applications 543 (2025), article 129021, DOI:10.1016/j.jmaa.2024.129021 .
4. M.-T. Chien and H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra 18 (2009), 58–63, DOI:10.13001/1081-3810.1293 .
