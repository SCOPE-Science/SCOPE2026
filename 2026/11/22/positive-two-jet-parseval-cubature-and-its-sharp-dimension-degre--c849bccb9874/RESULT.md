# Positive two-jet Parseval cubature and its sharp dimension-degree frontier for spherical harmonics

## Finding

For integers \(d\ge3\) and \(\ell\ge2\), let \(\mathcal H_\ell\) be the complex exact-degree-\(\ell\) spherical harmonic space on \(S^{d-1}\), normalized by probability surface measure \(\sigma\). Put
\[
D_\ell=(d+2\ell-4)(d+2\ell-2),\qquad
 a_{d,\ell}=\frac{\ell((\ell-2)^2-d)}{(\ell-1)D_\ell},\quad
 b_{d,\ell}=\frac{2(\ell-1)}{\ell D_\ell},\quad
 c_{d,\ell}=\frac{1}{\ell(\ell-1)D_\ell}.
\]
For any finite positive probability rule \(\nu=\sum_j w_j\delta_{x_j}\), and every \(f,g\in\mathcal H_\ell\), define
\[
B_\nu(f,g)=\sum_jw_j\big(a_{d,\ell}f(x_j)\overline{g(x_j)}+b_{d,\ell}\langle\nabla_S f(x_j),\nabla_S g(x_j)\rangle+c_{d,\ell}\langle\nabla_S^2f(x_j),\nabla_S^2g(x_j)\rangle_{\mathrm F}\big).
\]
Then \(B_\nu(f,g)=\int f\overline g\,d\sigma\) for every \(f,g\in\mathcal H_\ell\) **if and only if** the antipodal symmetrization \((\nu+(-\mathrm{id})_*\nu)/2\) integrates all spherical polynomials through degree \(2\ell-4\) exactly. The weights \(a_{d,\ell},b_{d,\ell},c_{d,\ell}\) are the unique scalar coefficients in the value/gradient/covariant-Hessian channel family that eliminate both highest harmonic components of every product \(f\overline g\) and normalize its constant component. All three are nonnegative exactly when
\[
\boxed{d\le(\ell-2)^2.}
\]
The gradient and Hessian coefficients are strictly positive. On the equality curve, the value coefficient vanishes and a **derivative-only Parseval identity** holds. No scalar combination of these three jet channels can additionally annihilate the next harmonic component while preserving constants, for \(\ell\ge3\).

## Assumptions and scope

The dimension \(d\) counts ambient real coordinates; \(S^{d-1}\) is the unit sphere. \(\nabla_S^2\) is the intrinsic covariant Hessian, viewed as a symmetric tangent \((0,2)\)-tensor, and its Frobenius product contracts both tangent indices. The node weights are positive and sum to one. The equivalence requires even moments only, so a nonsymmetric rule is allowed after antipodal symmetrization; odd moment conditions on the original rule are neither asserted nor needed. For \(\ell=2\), the required degree is zero, hence the identity holds for every probability rule but \(a_{d,2}\) is negative. The positive-frame conclusion applies when \(d\le(\ell-2)^2\).

## Proof

Write \(F=f\overline g\), \(G=\langle\nabla_Sf,\nabla_Sg\rangle\), \(H=\langle\nabla_S^2f,\nabla_S^2g\rangle_{\mathrm F}\), \(\lambda_k=k(k+d-2)\) and \(\Delta f=-\lambda_\ell f\). The product rule and the Bochner identity on the round sphere give
\[
G=\tfrac12(\Delta+2\lambda_\ell)F,\qquad
H=\tfrac14(\Delta+2(\lambda_\ell-d+2))(\Delta+2\lambda_\ell)F.
\]
Substituting the displayed coefficients and expanding gives the *pointwise* identity
\[
a_{d,\ell}F+b_{d,\ell}G+c_{d,\ell}H
=\frac{(\Delta+\lambda_{2\ell})(\Delta+\lambda_{2\ell-2})}{\lambda_{2\ell}\lambda_{2\ell-2}}F.
\]
Products of two exact-degree-\(\ell\) harmonics contain only even harmonic degrees \(0,2,\dots,2\ell\). The right-hand operator acts on degree \(k\) by
\[
 p_{d,\ell}(k)=\frac{(\lambda_{2\ell}-\lambda_k)(\lambda_{2\ell-2}-\lambda_k)}{\lambda_{2\ell}\lambda_{2\ell-2}}.
\]
It is \(1\) on constants, \(0\) at \(k=2\ell-2,2\ell\), and strictly positive on every even \(k\le2\ell-4\). Thus integration against any exact even-degree-\((2\ell-4)\) rule yields \(\int F\,d\sigma\).

For the converse, the linear span of products \(f\overline g\), with \(f,g\in\mathcal H_\ell\), contains every even harmonic sector through degree \(2\ell\). To verify this without assuming a spanning lemma, take the harmonic pure power \(f(x)=(x_1+\mathrm i x_2)^\ell\), whose squared modulus is \(t^\ell\) for \(t=x_1^2+x_2^2\). Under \(\sigma\), the variable \(t\) has beta weight proportional to \((1-t)^\gamma\) on \([0,1]\), with \(\gamma=(d-4)/2>-1\). The invariant degree-\(2r\) spherical harmonics under \(O(2)\times O(d-2)\) correspond to shifted Jacobi polynomials \(J_r(t)=P_r^{(\gamma,0)}(2t-1)\). Their coefficients in \(t^\ell\) do not vanish for any \(0\le r\le\ell\), since Rodrigues' formula and \(r\) integrations by parts give
\[
\int_0^1t^\ell J_r(t)(1-t)^\gamma dt=\binom\ell r\,\mathrm B(\ell+1,\gamma+r+1)>0.
\]
The rotation orbit of a nonzero component spans the irreducible real-sphere harmonic representation of that degree. Consequently, the Parseval identity for all products forces every even spherical moment of the rule through degree \(2\ell-4\) to match \(\sigma\). This is equivalent to the antipodal symmetrization being a weighted spherical \((2\ell-4)\)-design.

Any scalar combination of \(F,G,H\) acts on the harmonic-degree parameter \(\lambda_k\) by a polynomial of degree at most two. Eliminating the two distinct top degrees and normalizing constants determines this polynomial uniquely, hence also determines the three coefficients. Its constant-channel coefficient has the sign of \((\ell-2)^2-d\). Eliminating three distinct top degrees would require three roots of a nonzero quadratic, which is impossible for \(\ell\ge3\). This proves both sharp coefficient positivity and the four-degree lowering limit within the stated three-channel family.

## Verification

The standalone Python program `verify.py` reconstructs the factorization symbolically and checks the coefficient-sign threshold for integer dimensions and degrees. For an independent geometric test it constructs all nine quartic solid harmonics in three variables as a polynomial Laplacian nullspace; computes their exact Gram matrix from spherical monomial moments; and independently evaluates values, tangent gradients and intrinsic Hessians at the twelve normalized vertices of a regular icosahedron. With \(d=3\) and \(\ell=4\), the positive coefficients reduce to
\[
a_{3,4}=\frac4{189},\qquad b_{3,4}=\frac1{42},\qquad c_{3,4}=\frac1{756}.
\]
The computed mixed-node Gram matrix agrees with the exact sphere Gram matrix in every entry to maximum absolute error \(1.39\times10^{-16}\). A degree-eight monomial moment fails on the same twelve nodes, confirming that the observation identity is not merely ordinary degree-eight quadrature. At the 24 vertices of the regular 24-cell in \(S^3\), the separate 25-dimensional quartic-harmonic calculation gives a derivative-only Parseval identity with \(a_{4,4}=0\), \(b_{4,4}=3/160\), and \(c_{4,4}=1/960\); its maximum independent Gram error is \(5.56\times10^{-17}\). All polynomial moments through degree five (icosahedron) and degree four (24-cell) were checked numerically. These finite calculations check examples; the all-degree result is proved analytically above.

## Relationship to prior work

Xiao and Zhuang, *Spherical framelets from spherical designs* (first public arXiv version March 9, 2023), construct spherical tight framelets using polynomial-exact node rules; their Hessian calculations concern optimization of the design discrepancy, not covariant Hessians of the sampled input harmonics. The later open-access *Spherical designs for function approximation and beyond* likewise constructs value-based framelets and numerical designs. Jalolov and Isomiddinov's Hermite-type cubature work studies derivative-dependent cubature errors in Sobolev spaces, rather than the coefficient-sharp exact harmonic Gram identity derived here. The standard Laplace–Beltrami product and Bochner identities are used as established differential-geometric facts.

## Limitations

The claim is restricted to one exact-degree harmonic space and three isotropic energy channels, not heterogeneous degree bands, arbitrary derivative couplings, noisy-data optimality or arbitrary manifolds. The uniqueness and sharpness statements are relative to that stated channel family. This is an analytic identity, not an independently audited theorem. A historically equivalent formulation not found in the inspected sources may exist.

## References

1. Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365v1, March 9, 2023, https://arxiv.org/html/2303.05365v1 .
2. Y. Xiao and X. Zhuang, *Spherical designs for function approximation and beyond*, Sampling Theory, Signal Processing, and Data Analysis 23 (2025), https://doi.org/10.1007/s43670-025-00105-4 .
3. O. I. Jalolov and B. O. Isomiddinov, *On the construction of practically asymptotically optimal weighted cubature formulas of Hermite type in the Sobolev space*, Russian Mathematics 69 (2025), https://doi.org/10.3103/S1066369X25700288 .
