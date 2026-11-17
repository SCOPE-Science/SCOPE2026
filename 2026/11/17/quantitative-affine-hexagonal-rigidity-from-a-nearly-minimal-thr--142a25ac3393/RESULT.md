# Quantitative affine-hexagonal rigidity from a nearly minimal three-vector separation

## Finding

Let \(X\) be a real normed space and let three nonzero, noncollinear vectors \(v_1,v_2,v_3\in X\) obey \(v_1+v_2+v_3=0\). Write
\[
R=\max_{\{i,j,k\}=\{1,2,3\}}\frac{\|v_i-v_j\|}{\|v_k\|},\qquad \delta=R-\frac32.
\]
Then \(R\ge3/2\). If \(0\le\delta\le 1/100\), define
\[
c=\frac{\|v_1\|+\|v_2\|+\|v_3\|}{3},\quad
q_1=\frac{2(v_1-v_2)}{3c},\quad q_2=\frac{2(v_2-v_3)}{3c},
\quad H=\operatorname{conv}\{\pm q_1,\pm q_2,\pm(q_1+q_2)\}.
\]
The vectors \(q_1,q_2\) are independent, and \(H\) is an affine-regular centrally symmetric hexagon in \(E=\operatorname{span}\{v_1,v_2\}\). If \(B_E\) is the unit ball of the inherited norm, then
\[
\boxed{\frac{1}{1+6\delta/5}H\ \subseteq\ B_E\ \subseteq\ \frac{1}{1-9\delta}H.}
\]
In particular, with \(H_0\) the standard affine-regular hexagonal normed plane,
\[
\boxed{d_{\mathrm{BM}}(E,H_0)\le\frac{1+6\delta/5}{1-9\delta}\le1+12\delta.}
\]
A converse *gap certificate* follows: if \(d_{\mathrm{BM}}(E,H_0)\ge1+\tau\) with \(0<\tau\le3/25\), every admissible triple satisfies \(R\ge3/2+\tau/12\).

## Assumptions and scope

Only real norms are considered; neither smoothness nor strict convexity nor completeness of the ambient space is assumed. Noncollinearity is essential because the conclusion controls a two-dimensional norm. \(d_{\mathrm{BM}}\) denotes the infimum of \(\|T\|\|T^{-1}\|\) over linear isomorphisms of finite-dimensional normed spaces. The inequalities are for all triples with the displayed hypotheses, and the explicit constants are not claimed optimal. A finite-dimensional plane is automatically complete even when the ambient space is not.

## Proof

Put \(a_i=\|v_i\|\), \(S=a_1+a_2+a_3=3c\), and \(t=R=3/2+\delta\). The zero-sum identity gives \(3v_i=(v_i-v_j)+(v_i-v_k)\), whence for each \(i\),
\[
3a_i\le\|v_i-v_j\|+\|v_i-v_k\|\le t(a_j+a_k)=t(S-a_i).
\]
Summing gives \(3S\le2tS\), hence \(t\ge3/2\). The same inequalities yield
\[
\frac{a_i}{c}\le\frac{3t}{3+t}=\frac{3(3+2\delta)}{9+2\delta}=1+\frac{4\delta}{9+2\delta}.
\]
For a slightly coarser estimate convenient below, put \(u=4\delta/(9/2+\delta)\). Since \(3a_i\le t(S-a_i)\), in fact \(a_i/c\le 3t/(3+t)\le1+u/2\). Averaging the three \(a_i/c\) then yields \(a_i/c\ge1-u\), because the other two are each at most \(1+u/2\). For \(0\le\delta\le1/100\), \(u\le\delta\).

The three nonopposite vertices of \(H\) are proportional to the differences \(v_i-v_j\). Thus
\[
\|q_1\|,\|q_2\|,\|q_1+q_2\|\le\frac{2t}{3}\max_i\frac{a_i}{c}\le(1+2\delta/3)(1+u/2)=1+\varepsilon,
\]
with \(\varepsilon\le(6/5)\delta\). It follows by convexity that \(H/(1+\varepsilon)\subseteq B_E\), proving the first inclusion.

Use coordinates \(z=xq_1+yq_2\). In these coordinates
\[
H=\{(x,y):N_H(x,y):=\max(|x|,|y|,|x-y|)\le1\}.
\]
The three midpoints of the successive positive-facing edges of \(H\) are
\[
\frac{2q_1+q_2}{2}=\frac{v_1}{c},\qquad
\frac{q_1+2q_2}{2}=-\frac{v_3}{c},\qquad
\frac{q_2-q_1}{2}=\frac{v_2}{c}.
\]
Their norms lie in \([1-u,1+u/2]\). Choose norm-one real support functionals \(f_x,f_y,f_{y-x}\) at these midpoints. For any edge endpoints \(a,b\) and its midpoint \(m=(a+b)/2\), the equalities \(2f(m)=f(a)+f(b)\ge2(1-u)\) and vertex bounds \(|f(a)|,|f(b)|\le1+\varepsilon\) force each endpoint value to lie in
\[
[1-\eta,1+\varepsilon],\quad \eta=2u+\varepsilon.
\]
Since \(f_x(q_1)\) and \(f_x(q_1+q_2)\) are both in this interval, their difference \(f_x(q_2)\) has absolute value at most \(\kappa=\eta+\varepsilon\). The same argument for the other two edges yields, for all \((x,y)\),
\[
|f_x(z)-x|\le\kappa(|x|+|y|),\quad
|f_y(z)-y|\le\kappa(|x|+|y|),\quad
|f_{y-x}(z)-(y-x)|\le\kappa(|x|+|y|).
\]
(For the last edge, its endpoints are \(q_2\) and \(-q_1\).) Since \(|x|+|y|\le2N_H(x,y)\) and each \(f\) has dual norm one, for \(z\in B_E\),
\[
N_H(z)\le1+2\kappa N_H(z).
\]
Here \(2\kappa=4u+4\varepsilon\le 9\delta<1\). Therefore \(N_H(z)\le1/(1-9\delta)\), proving the second inclusion. The Banach--Mazur bound follows by applying the linear coordinate identification and taking the ratio of the two inclusion scales. Elementary multiplication shows \((1+6\delta/5)/(1-9\delta)\le1+12\delta\) for \(\delta\le1/100\).

For the converse gap certificate, if \(\delta\le1/100\) the estimate gives \(1+\tau\le1+12\delta\); if \(\delta>1/100\), then \(\delta>\tau/12\) because \(\tau\le3/25\). This proves the assertion.

## Verification

The analytic proof uses only triangle inequalities, convexity, and norm-one support functionals, and does not depend on finite enumeration. The accompanying `checker.py` uses exact rational arithmetic to check the coefficient inequalities at 101 rational defect parameters and to inspect 501 admissible polygonal instances of the claimed inclusions. Run `python checker.py` with Python 3's standard library. These samples are not a substitute for the proof and do not establish optimality of constants.

## Relationship to prior work

Fang–Qi–Liu (2026) use norming-functionals and geometric separation of triples in the Fermat–Torricelli problem; they establish a Birkhoff–James characterization of inner-product spaces without a quantitative affine-hexagonal proximity theorem. Kobos (2025, revised 2026) establishes uniqueness of the affine-regular hexagonal norm among real two-dimensional spaces with maximal projection constant, a different extremal functional. The present theorem gives an explicit *single-triple* near-extremality-to-Banach–Mazur-distance implication, with no maximal-projection-constant assumption. Classical normed-plane and convex-body distance literature provides background but does not supply the displayed single-triple modulus in the sources inspected.

## Limitations

The stated constants \(6/5,9,12\) are proved but not asserted optimal. The converse gap applies to a two-dimensional span, not automatically the entire ambient space. No converse existence result for every plane close to a hexagon is claimed. Completeness, smoothness, and any independent external audit are not established or required for the theorem. Older unindexed geometric stability literature may contain equivalent statements; bibliographic uniqueness cannot be guaranteed.

## References

1. Z. Fang, J. Qi and Q. Liu, *A Fermat–Torricelli convex-hull characterization of inner-product spaces via Birkhoff–James orthogonality*, arXiv:2611.09226v1, first posted 2026-11-06, https://arxiv.org/html/2611.09226v1 .
2. T. Kobos, *Spaces with the maximal projection constant revisited*, arXiv:2505.24526v1 (2025-05-30); revised v2 (2026-09-14), https://arxiv.org/html/2505.24526v2 .
