# Sharp fixed-fidelity logarithmic tilting inequality and its alignment cusp

## Finding
For \(1/2<\alpha<1\), put \(s=(1-\alpha)/\alpha\). If \(A=aP\) and \(B=bQ\) are nonzero positive rank-one matrices, write \(t=\operatorname{Tr}(PQ)\in(0,1]\). Then the optimal constant at this fixed squared fidelity in
\[
\operatorname{Tr}\!\left[A\,D\log[A^\alpha+B^\alpha](B^\alpha)\right]
\le C_s(t)\,\operatorname{Tr}(A^\alpha B^{1-\alpha})
\]
is
\[
C_s(t)=\max_{\xi>0}\xi^{1-s}
\int_0^\infty\frac{z^2\,dz}{[z^2+(1+\xi)z+\xi(1-t)]^2}.
\]
The maximum is attained for some finite positive \(\xi\). The function \(t\mapsto C_s(t)\) is strictly increasing on \((0,1]\), and
\[
0<C_s(t)<C_s(1)=s^s(1-s)^{1-s}\qquad(0<t<1).
\]
The optimal strictness defect has the exact logarithmic alignment law
\[
\lim_{t\uparrow1}\frac{C_s(1)-C_s(t)}{(1-t)\log(1/(1-t))}
=2s(1-s)\,s^s(1-s)^{1-s}.
\]
These statements hold in every finite Hilbert-space dimension at least two; indeed, the matrices act on the span of the two rank-one ranges. At complete alignment, the one-dimensional formula gives the same value \(C_s(1)\).

## Assumptions and scope
Here \(D\log[X](H)\) is the Fréchet derivative of the principal matrix logarithm at \(X>0\) in Hermitian direction \(H\). For singular \(X\), it is evaluated on its support, where \(X\) is invertible, and extended by zero. Matrices are complex Hermitian positive semidefinite, \(P,Q\) are rank-one orthogonal projections, and \(a,b>0\). The squared transition probability \(t\) is strictly positive. At \(t=0\), both quantities in the inequality are zero, so no ratio-based optimal constant is defined. The exponent endpoints \(\alpha=1/2,1\) are not part of this theorem. The rank-one eigenvalue weights are arbitrary and need not sum to one.

## Proof
**Reduction to one positive integral.** Write \(u=a^\alpha\), \(v=b^\alpha\), and \(X=uP+vQ\). For \(0<t<1\), the operator is positive definite on \(\operatorname{span}\{\operatorname{ran}P,\operatorname{ran}Q\}\). For \(w>0\), the two-dimensional resolvent has determinant
\[
\det(X+wI)=w^2+(u+v)w+uv(1-t),
\]
and, for unit spanning vectors \(p,q\) of the two ranges,
\[
\big|\langle p,(X+wI)^{-1}q\rangle\big|^2
=\frac{t\,w^2}{[w^2+(u+v)w+uv(1-t)]^2}.
\]
The standard resolvent representation
\[
D\log[X](H)=\int_0^\infty(X+wI)^{-1}H(X+wI)^{-1}\,dw
\]
then gives the exact numerator
\[
\operatorname{Tr}[A D\log[X](B^\alpha)]
=avt\int_0^\infty\frac{w^2\,dw}{[w^2+(u+v)w+uv(1-t)]^2}.
\]
The denominator without a constant is \(\operatorname{Tr}(A^\alpha B^{1-\alpha})=uv^st\), since \(b^{1-\alpha}=v^s\). Substituting \(w=uz\) and \(\xi=v/u\) yields exactly \(R_s(\xi,t)=\xi^{1-s}\int_0^\infty z^2/[z^2+(1+\xi)z+\xi(1-t)]^2\,dz\). Every \(\xi>0\) is achieved by choosing positive weights, so taking its supremum is exactly the optimal coefficient, not merely an upper bound. The collinear case \(t=1\) follows directly from the scalar logarithmic derivative and yields \(R_s(\xi,1)=\xi^{1-s}/(1+\xi)\).

**Existence, strictness and monotonicity.** Since \(1-t\ge0\),
\[
0<R_s(\xi,t)\le f_s(\xi):=\frac{\xi^{1-s}}{1+\xi},
\]
with strict inequality whenever \(0<t<1\). As \(0<s<1\), \(f_s\) tends to zero at both ends of the positive line. Continuity gives a positive maximizer for \(R_s(\cdot,t)\). The scalar function \(f_s\) has the unique maximum at \(\xi_0=(1-s)/s\), of height \(C_s(1)=s^s(1-s)^{1-s}\). Strict pointwise comparison at the maximizing \(\xi\) proves \(C_s(t)<C_s(1)\) for \(t<1\). If \(0<t_1<t_2\le1\), every integrand at \(t_2\) is strictly larger; testing the maximizer for \(t_1\) proves \(C_s(t_2)>C_s(t_1)\).

**Uniform singular integral estimate.** Fix a compact interval \(K\subset(0,\infty)\) for \(\xi\), set \(A_0=1+\xi\), \(e=\xi\delta\), and
\[
I_e(A_0)=\int_0^\infty\frac{z^2\,dz}{[z^2+A_0z+e]^2},\qquad I_0(A_0)=1/A_0.
\]
Subtracting integrands exactly gives
\[
I_0-I_e=\int_0^\infty\frac{1}{(z+A_0)^2}
\left\{\frac{2e}{z(z+A_0)+e}-\frac{e^2}{[z(z+A_0)+e]^2}\right\}\,dz.
\]
Uniformly for \(\xi\in K\) and \(e\downarrow0\), the contribution from \(0<z<e/A_0\) is \(O_K(e)\). On \(e/A_0<z<1\), the first term is \(2e/(A_0^3 z)\) plus an error whose integral is \(O_K(e)\); the squared-denominator second term also has integral \(O_K(e)\). The contribution for \(z>1\) is \(O_K(e)\). Thus, uniformly on \(K\),
\[
I_0-I_e=\frac{2e}{A_0^3}\log(1/e)+O_K(e).
\]
Inserting \(e=\xi\delta\) yields
\[
R_s(\xi,1-\delta)=f_s(\xi)-h_s(\xi)\delta\log(1/\delta)+O_K(\delta),
\qquad h_s(\xi)=\frac{2\xi^{2-s}}{(1+\xi)^3}.
\]

**Maximizing and taking the cusp limit.** Let \(\xi_\delta\) maximize \(R_s(\cdot,1-\delta)\). As \(R_s(\xi_0,1-\delta)\to C_s(1)\) and \(R_s\le f_s\) with \(f_s\to0\) at both ends, all sufficiently small \(\delta\) have maximizers in a fixed compact subset of \((0,\infty)\). Any limit point of \(\xi_\delta\) maximizes \(f_s\), so \(\xi_\delta\to\xi_0\). Bounding the difference from above by \(f_s(\xi_0)-R_s(\xi_0,1-\delta)\) and below by \(f_s(\xi_\delta)-R_s(\xi_\delta,1-\delta)\), then applying the uniform expansion, gives
\[
\lim_{\delta\downarrow0}\frac{C_s(1)-C_s(1-\delta)}{\delta\log(1/\delta)}
=h_s(\xi_0)=2s(1-s)C_s(1).
\]
This proves the theorem.

## Verification
The determinant, overlap-resolvent identity, and Fréchet-logarithm coefficient were checked independently in finite two-dimensional matrices using an eigenbasis divided-difference formula. Numerical quadrature of the exact integral agrees with that independent matrix evaluation for several distinct exponents, weights, and fidelities. Further scalar optimization tests show the predicted logarithmic normalization approaching its analytic coefficient for several fixed exponents. These numerical tests do not replace the proof, in particular its uniform singular-integral estimate. Run the included `verify_tilting.py` with Python, NumPy, and SciPy for reproducibility.

## Relationship to prior work
Cheng and Liu, *Sharp Tilting Inequalities* (2026, arXiv:2610.39598v1), Theorem 4, proved the sharp **unrestricted** coefficient \(s^s(1-s)^{1-s}\) and treated aligned rank-one matrices as scalar sharpness witnesses. Their theorem does not imply the present fixed-**nonparallel**-overlap optimum; even strictness below the global constant leaves both its exact profile and logarithmic approach undetermined. The resolvent representation of the logarithmic Fréchet derivative is classical and is explicitly used in their paper. Here the additional information comes from the rank-two resolvent and a uniform boundary-layer calculation. No publication-priority claim is made beyond the inspected literature.

## Limitations
Only nonzero rank-one positive inputs with positive overlap and interior exponent \(1/2<\alpha<1\) are considered. The sharp coefficient is given by a one-dimensional integral optimization, not an elementary closed form for every nonunit fidelity. The theorem gives no universal improvement for arbitrary higher-rank matrices, no statement at orthogonality where the trace normalization is zero, and no fixed-fidelity claim for the symmetric-quotient variant. An equivalent formulation in previously uninspected literature remains possible. An independent mathematical audit has not been performed.

## References
1. Hao-Chung Cheng and Po-Chieh Liu, *Sharp Tilting Inequalities*, arXiv:2610.39598v1, first posted 2026-10-29; especially Theorem 4 and its proof, https://arxiv.org/abs/2610.39598.
2. Standard matrix-function Fréchet derivative and resolvent formula, used as equation (7) in reference 1; no novelty claimed for this identity.
