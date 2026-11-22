# Two-sum spectral strata of a finite-field twisted cubic and its tangent

## Finding

The affine cubic moment curve together with its tangent at the origin has a completely explicit, arithmetic-dependent twofold additive convolution. Let \(q\) be an odd prime power and put
\[
C=\{(t,t^2,t^3):t\in\mathbb F_q\},\qquad
L=\{(s,0,0):s\in\mathbb F_q\},\qquad S=C\cup L.
\]
The set has \(|S|=2q-1\). With \(\chi\) the quadratic character (including \(\chi(0)=0\)), let
\[
\varepsilon_q=
\begin{cases}
1,&\operatorname{char}\mathbb F_q\ne3\ \text{and}\ \chi(-2)=1,\\
0,&\text{otherwise}.
\end{cases}
\]
For the ordered representation count \(r_S(v)=\#\{(a,b)\in S^2:a+b=v\}\), its *complete* positive-value histogram is
\[
\begin{array}{c|c}
r_S(v)&\#\{v:r_S(v)=\text{row value}\}\\\hline
1&q-1\\
2&\frac{(q-1)(3q-2-4\varepsilon_q)}2\\
4&(q-1)\varepsilon_q\\
q&q
\end{array}
\]
(The table rows refer to distinct levels; the zero level fills the remaining ambient points.) Consequently
\[
\boxed{|S+S|=\frac{3q^2-q}{2}-(q-1)\varepsilon_q},
\qquad
\boxed{E(S)=q^3+6q^2-9q+3+8(q-1)\varepsilon_q}.
\]
In particular the extra \(q-1\) four-representation targets occur precisely when \(\operatorname{char}\mathbb F_q\ne3\) and \(-2\) is square. In characteristic three there are none, although \(-2=1\) is square.

## Assumptions and scope

All additions, powers, and character values are in \(\mathbb F_q\). The characteristic is odd, including \(3\), and the degree-three moment curve is the parametrized affine curve above. The line \(L\) is its tangent at parameter zero, so \(C\cap L=\{(0,0,0)\}\). Define
\[
T=\{(x,t^2,t^3):x,t\in\mathbb F_q\},\quad
V=\{(x,y,z):2z=3xy-x^3\}.
\]
The map \(t\mapsto(t^2,t^3)\) is injective because the field has odd characteristic. Thus \(|T|=q^2\), \(L\subset T\), and each point of \(T\setminus L\) has one uniquely determined nonzero parameter \(t\).

More precisely than the histogram: \(r_S=q\) at every point of \(L\); on \(T\setminus L\), \(r_S=4\) precisely for \(x=-2t\), \(t\ne0\), with \(\varepsilon_q=1\), and equals \(2\) otherwise; on the complement of \(T\),
\[
r_S(x,y,z)=\mathbf1_V(x,y,z)\big(1+\chi(2y-x^2)\big).
\]
This is a pointwise complete convolution formula, including zero multiplicities.

## Proof

Write \(A=\mathbf1_C\), \(B=\mathbf1_L\), and \(\delta_0\) for the delta mass at the origin. The overlap is exactly the origin, so
\[
\mathbf1_S=A+B-\delta_0,
\quad r_S=A*A+2A*B+qB-2A-2B+\delta_0.
\tag{1}
\]
To evaluate \(A*A\), let \(x=u+v\), \(y=u^2+v^2\), and \(z=u^3+v^3\). Since \(2uv=x^2-y\), Newton's two-variable identity yields
\[
2z=3xy-x^3,
\quad (u-v)^2=2y-x^2.
\]
Conversely, for each \((x,y,z)\) satisfying the first equation, the ordered pair \((u,v)\) is obtained from roots of the quadratic with sum \(x\) and product \((x^2-y)/2\). Hence
\[
(A*A)(x,y,z)=\mathbf1_{\{2z=3xy-x^3\}}
\big(1+\chi(2y-x^2)\big).
\tag{2}
\]
This remains valid in characteristic three because only division by \(2\) is required. Also \(A*B=\mathbf1_T\), by the injectivity of \(t\mapsto(t^2,t^3)\), while \(B*B=qB\). Formula (1) then implies the asserted multiplicity \(q\) on \(L\): the only point of \(V\cap L\) is the origin, at which the overlap corrections exactly cancel.

Fix \(t\ne0\). A point of \(T\setminus L\) has coordinates \((x,t^2,t^3)\). The support condition in (2) reduces to
\[
x^3-3t^2x+2t^3=(x-t)^2(x+2t)=0.
\tag{3}
\]
At \(x=t\), the curve–curve convolution counts exactly the two ordered pairs \((0,t)\) and \((t,0)\), but (1) subtracts \(2A\), leaving \(r_S=2\). If the characteristic is not three, the other candidate \(x=-2t\) is different and has discriminant \(-2t^2\). Its curve–curve contribution is \(1+\chi(-2)\), so the total is \(3+\chi(-2)\), equal to \(4\) if \(-2\) is square and \(2\) otherwise. In characteristic three the two candidates coincide, so the multiplicity is always \(2\). Every other point of \(T\setminus L\) has multiplicity \(2\). This proves the full pointwise formula.

For the histogram, the surface \(V\) has exactly \(q^2\) points, one for every \((x,y)\). The discriminant \(\Delta=2y-x^2\) runs over \(\mathbb F_q\) bijectively for each \(x\). Therefore (2) takes the value \(1\) on \(q\) points (\(\Delta=0\)), the value \(2\) on \(q(q-1)/2\) points, and zero elsewhere on \(V\). The unique diagonal point of \(V\cap L\) is the origin; no other discriminant-zero point belongs to \(T\). For each \(t\ne0\), \(V\cap T\) contains \(x=t\), and also \(x=-2t\) precisely in the square-residue, non-characteristic-three case. Their respective curve–curve multiplicities are \(2\) and \(2\). Thus outside \(T\) there are \(q-1\) points of multiplicity \(1\) and
\[
\frac{q(q-1)}2-(q-1)(1+\varepsilon_q)
\]
points of multiplicity \(2\). Within \(T\setminus L\), exactly \((q-1)\varepsilon_q\) points have multiplicity \(4\), and the other \(q(q-1)-(q-1)\varepsilon_q\) points have multiplicity \(2\). Adding the \(q\) points of \(L\) gives the displayed histogram. In particular,
\[
\begin{aligned}
|S+S|&=q+(q-1)+\frac{(q-1)(3q-2-4\varepsilon_q)}2+(q-1)\varepsilon_q\\
&=\frac{3q^2-q}{2}-(q-1)\varepsilon_q,\\
E(S)&=q\cdot q^2+(q-1)+4\frac{(q-1)(3q-2-4\varepsilon_q)}2+16(q-1)\varepsilon_q\\
&=q^3+6q^2-9q+3+8(q-1)\varepsilon_q.
\end{aligned}
\]
All steps are exact in every finite field of odd characteristic.

For any fixed nontrivial additive character \(\psi\), take the *unnormalized* transform \(\mathcal F\mathbf1_S(\xi)=\sum_{s\in S}\overline{\psi(\xi\cdot s)}\). Orthogonality of additive characters gives
\[
\frac1{q^3}\sum_{\xi\in\mathbb F_q^3}|\mathcal F\mathbf1_S(\xi)|^4
=\sum_v r_S(v)^2=E(S).
\]
Equivalently, for four independent uniform random increments from \(S\), the probability that their first pair-sum equals their second pair-sum is \(E(S)/(2q-1)^4\).

## Verification

The standalone \(checker.py\) implements prime and quadratic-extension field arithmetic independently, enumerates every ordered sum from \(S^2\), and compares *every ambient-target multiplicity* to the pointwise formula. It checks the complete histogram, sumset size, energy, and total pair count for fields of orders \(3,5,7,9,11,13,17,19,23,25,29,31,37,49\). Run `python3 checker.py` with Python 3 standard library. The checker exercises both values of \(\varepsilon_q\) and characteristic three. It provides finite corroboration only; the preceding algebra proves the unbounded family.

## Relationship to prior work

Biswas–Carneiro–Flock–Madrid–Oliveira e Silva–Stovall–Tautges, arXiv:2609.29882, settle the *sharp weighted \(L^2\to L^{2d}\)* finite-field moment-curve extension problem for the curve alone, using Newton identities and a probabilistic extremal theorem. For \(d=3\), that concerns the sixth moment and not the fourth moment of a union with a tangent line. Their predecessor arXiv:2508.08377 develops the same pure-curve framework. The elementary curve-only two-sum count \(E(C)=2q^2-q\) is part of the known Newton-fiber theory and is not claimed as new here.

Blokhuis–Pellikaan–Szőnyi, arXiv:2103.16904, classify twisted-cubic projective chords and lines for a coding-theoretic weight enumerator. Their chord-geometry information overlaps the curve-curve component of our proof, but projective secant incidences do not state the affine, ordered sum-convolution of the pointwise union \(C\cup L\), including the correction for the common origin or the characteristic-three/square-residue levels. Cuenin–Denson–Hickman, arXiv:2610.27968, study real smooth space-curve Fourier restriction, not this finite-field mixed-support enumeration.

## Limitations

The theorem addresses a specific canonical union: an affine twisted cubic and its tangent at zero, not arbitrary affine lines or weights. The fourth-moment identity is for the indicator; it does not compute the sharp weighted extension operator norm or classify weighted extremizers. The universal algebraic proof is not an independent audit. Equivalent results concealed in general projective-incidence or finite-field extension theorems cannot be categorically excluded by the literature search; in particular, the 2021 twisted-cubic geometry work merits expert priority review.

## References

1. Chandan Biswas, Emanuel Carneiro, Taryn C. Flock, José Madrid, Diogo Oliveira e Silva, Betsy Stovall, James Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution* (first public 2026-09-24), https://arxiv.org/abs/2609.29882.
2. Chandan Biswas, Emanuel Carneiro, Taryn C. Flock, Diogo Oliveira e Silva, Betsy Stovall, James Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields* (2025), https://arxiv.org/abs/2508.08377.
3. Aart Blokhuis, Ruud Pellikaan, Tamás Szőnyi, *The extended coset leader weight enumerator of a twisted cubic code* (2021), https://arxiv.org/abs/2103.16904.
4. Jean-Claude Cuenin, Jacob Denson, Jonathan Hickman, *Remarks on space curve \(L^2\) Fourier restriction* (2026), https://arxiv.org/abs/2610.27968.
