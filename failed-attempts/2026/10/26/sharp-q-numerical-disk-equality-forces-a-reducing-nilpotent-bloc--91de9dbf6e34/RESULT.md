# Sharp \(q\)-numerical disk equality forces a reducing nilpotent block

## Finding
Fix \(4/5<q<1\) and set
\[
\rho_q=\frac{2q}{1+\sqrt{1-q^2}}>1.
\]
Let \(H\) be a complex Hilbert space of dimension at least two. For \(A\in\mathcal B(H)\), let
\[
W_q(A)=\{\langle Au,v\rangle:\ \|u\|=\|v\|=1,\ \langle u,v\rangle=q\},\qquad \Omega_q(A)=q^{-1}W_q(A),
\]
using the inner-product convention linear in the first variable. Suppose \(\Omega_q(A)\subseteq\overline{\mathbb D}\) and \(A\) attains its norm. Then the following are equivalent:

1. \(\|A\|=\rho_q\).
2. There is an orthonormal pair \(x,y\in H\) spanning a **reducing** subspace for \(A\), with \(Ax=\rho_q y\) and \(Ay=0\).

Thus every finite-dimensional sharp operator-norm extremizer has a reducing, square-zero \(2\times2\) summand; no hypothesis on the rank of \(A\) is needed. The remaining reducing summand is unconstrained except for the assumed scaled-range containment.

## Assumptions and scope
The parameter is real \(4/5<q<1\). The Hilbert space may be infinite dimensional, but the operator must attain its norm. The range containment uses **all** unit pairs with inner product exactly \(q\). A two-dimensional subspace is reducing when both it and its orthogonal complement are invariant under the operator. The endpoint \(q=4/5\) and the ordinary numerical-radius endpoint \(q=1\) are excluded; the strict inequality \(\rho_q>1\) matters in the proof.

## Proof
Put \(h=q/(1+\sqrt{1-q^2})\), so that \(\rho_q=2h\) and \(q=2h/(1+h^2)\). We use the already established general upper bound \(\|A\|\le\rho_q\) from Kaunisto--O'Loughlin--Virtanen, Theorem 2.2, and the following overlap estimate from their Lemma 2.1. Whenever \(a,b\) are unit vectors and \(s=|\langle a,b\rangle|\), disk containment implies
\[
|\langle Aa,b\rangle|\le
\begin{cases}
 h\bigl(1+\sqrt{1-s^2}\bigr),&0\le s\le q,\\
 s,&q\le s\le1.
\end{cases}
\tag{1}
\]
Only its strictness for \(s>0\) when the left side equals \(\rho_q>1\) is needed.

Assume \(\|A\|=\rho_q\), and choose a unit norming vector \(x\). Write \(Ax=\rho_q y\), where \(\|y\|=1\). Apply (1) to \(x,y\). For \(0<s\le q\), its right side is strictly less than \(2h\). For \(s\ge q\), its right side is at most \(1<2h\). Therefore \(s=0\), so \(x\perp y\).

**Exact two-dimensional compression.** For a complex \(z\), consider the polynomial
\[
F(z)=\frac12\langle A(x+zy),\ y+\overline z x\rangle.
\]
For \(|z|=h\), the normalized vectors \((x+zy)/\sqrt{1+h^2}\) and \((y+\overline z x)/\sqrt{1+h^2}\) have overlap of modulus \(2h/(1+h^2)=q\). A unimodular adjustment gives overlap exactly \(q\) without changing the absolute matrix coefficient. Consequently \(|F(z)|\le q(1+h^2)/2=h\) on that circle. Yet \(F(0)=\langle Ax,y\rangle/2=h\). The maximum-modulus principle yields \(F\equiv h\). Expanding it gives
\[
F(z)=h+\frac z2\left(\langle Ax,x\rangle+\langle Ay,y\rangle\right)
+\frac{z^2}2\langle Ay,x\rangle.
\]
Since \(Ax=\rho_qy\) and \(x\perp y\), both \(\langle Ay,y\rangle=0\) and \(\langle Ay,x\rangle=0\). Thus the compression of \(A\) to \(E=\operatorname{span}\{x,y\}\) is exactly the scaled square-zero Jordan block.

**Eliminating cross-block couplings.** Put \(t=\sqrt{1-q^2}\), and choose positive \(c,s\) satisfying \(c^2=(1+t)/2\), \(s^2=(1-t)/2\); hence \(2cs=q\). For \(\beta=0,\pi\), define
\[
X_\beta=cx+s e^{i\beta}y,\qquad
Y_\beta=sx+c e^{i\beta}y.
\]
These vectors are unit, \(\langle X_\beta,Y_\beta\rangle=q\), and the compression just obtained gives
\[
\bigl|\langle AX_\beta,Y_\beta\rangle\bigr|=\rho_qc^2=q.
\tag{2}
\]
For each unit \(z\in E^\perp\), write \(V_\beta=(X_\beta-qY_\beta)/t\), a unit vector orthogonal to \(Y_\beta\). Every vector
\[
X_\beta(\varepsilon)=qY_\beta+
 t\frac{V_\beta+\varepsilon z}{\sqrt{1+|\varepsilon|^2}}
\]
is unit and satisfies \(\langle X_\beta(\varepsilon),Y_\beta\rangle=q\). Expanding the saturated bound in (2) at \(\varepsilon=0\), and varying the complex phase of \(\varepsilon\), forces \(\langle Az,Y_\beta\rangle=0\). Since \(Y_0,Y_\pi\) span \(E\), this proves \(A(E^\perp)\subseteq E^\perp\).

Similarly, put \(U_\beta=(Y_\beta-qX_\beta)/t\) and perturb the second test vector by
\[
Y_\beta(\varepsilon)=qX_\beta+
 t\frac{U_\beta+\varepsilon z}{\sqrt{1+|\varepsilon|^2}}.
\]
It remains unit and satisfies \(\langle X_\beta,Y_\beta(\varepsilon)\rangle=q\). Saturation of (2), with arbitrary complex perturbation phase, forces \(\langle AX_\beta,z\rangle=0\). Since \(X_0,X_\pi\) span \(E\), \(AE\subseteq E\). We already have the compression \(Ax=\rho_qy\) and \(Ay\perp E\); invariance now gives \(Ay=0\). Both \(E\) and \(E^\perp\) are invariant, as asserted.

Conversely, a reducing \(\rho_q\)-scaled square-zero summand gives \(\|A\|\ge\rho_q\). The published general upper bound for the assumed disk containment gives \(\|A\|\le\rho_q\), hence equality. This proves both implications.

## Verification
All computations above are finite-dimensional calculations within the span of an extremizing singular-vector pair, regardless of the dimension of \(H\). The normalization \(q=2h/(1+h^2)\), equality \(\rho_qc^2=q\), and the exact polynomial coefficients can be verified by direct substitution. For the perturbation arguments, the leading term of a saturated complex-valued coefficient has a freely chosen phase and is linear in \(\varepsilon\) (or \(\overline\varepsilon\)); a nonzero coefficient would increase the modulus for one phase. Quadratic normalization terms cannot cancel this linear increase.

The sole imported non-elementary statements are Lemma 2.1 and Theorem 2.2 of the cited source. The equality and reducing-subspace arguments are supplied in full. Numerical experiments are not used as proof.

## Relationship to prior work
Kaunisto--O'Loughlin--Virtanen determine the universal dilation/norm coefficient and display a \(2\times2\) square-zero sharpness example, without classifying higher-rank equality operators. Aouichaoui--O'Loughlin obtain the same optimal polynomial spectral-set coefficient by a similarity representation, but the inspected text does not classify reducing summands of arbitrary sharp norm extremizers. Denčić--Stanković--Krstić--Damnjanović treat exact \(q\)-numerical radii of rank-one operators. The present rigidity statement is for arbitrary rank, including matrices that may have additional nontrivial reducing blocks.

## Limitations
Norm attainment is an explicit hypothesis, automatic in finite dimension but not for arbitrary bounded operators. The theorem makes no claim of a reducing sharp block for a non-norm-attaining operator, no classification at \(q=4/5\) or \(q=1\), and no classification of all possible complementary reducing summands. Historical-priority searches and source comparisons cannot prove global novelty; analogous rigidity under a different characterization of constrained numerical ranges remains a residual possibility. Independent validation has not been performed.

## References
1. M. Kaunisto, R. O'Loughlin and J. Virtanen, *Dilation Theory for Scaled \(q\)-Numerical Ranges*, arXiv:2610.00443v1 (first public 2026-09-30), especially Lemma 2.1 and Theorem 2.2; expanded v2 October 2026.
2. M. A. Aouichaoui and R. O'Loughlin, *Sharp spectral constants for scaled \(q\)-numerical ranges*, arXiv:2608.09866v1 (2026), particularly Theorem 4.1.
3. D. Denčić, H. Stanković, M. Krstić and I. Damnjanović, *\(q\)-numerical radius of rank-one operators and the generalized Buzano inequality*, arXiv:2503.05036v1 (2025).
