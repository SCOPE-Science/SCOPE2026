# Laguerre-controlled sign reversals in near-lumped finite-element heat propagation

## Finding

For the uniform continuous linear finite-element discretization of the one-dimensional homogeneous Dirichlet heat equation, an arbitrarily small consistent-mass component can create repeated sign reversals in the **exact semidiscrete propagator**, even though fully mass-lumped propagation is positivity-preserving.

For every fixed integer \(n\ge3\), when the consistent-mass fraction \(p>0\) is sufficiently small, the influence of the rightmost interior node on the leftmost node reverses sign exactly \(n-2\) times at positive times. These crossing times satisfy
\[
\frac{t_j(p)}{h^2}=\frac{p}{6}\xi_j+O_n(p^2),\qquad
0<\xi_1<\cdots<\xi_{n-2},\qquad L_{n-2}^{(1)}(\xi_j)=0.
\]
For example, the \(n=4\) far-end influence has precisely two positive zero crossings for small \(p\), at the respective leading dimensionless times \(p(3-\sqrt3)/6\) and \(p(3+\sqrt3)/6\). The crossings are simple. The \(n=3\) case is solved exactly for every mixing fraction, not merely asymptotically.

## Assumptions and scope

Take \(n+2\) equally spaced mesh nodes on a finite interval, with \(n\) interior unknowns and mesh spacing \(h>0\). Impose homogeneous Dirichlet boundary conditions and zero forcing; diffusion is one. Let \(C_n\) denote the symmetric tridiagonal matrix with diagonal entries \(2\) and neighboring entries \(-1\). The stiffness matrix is \(K=C_n/h\). The consistent mass is \(M_c=(h/6)(6I-C_n)\), while the fully lumped mass is \(M_\ell=hI\). Blend them as
\[
M_p=pM_c+(1-p)M_\ell=\frac h6(6I-pC_n),\qquad 0\le p\le1.
\]
The semidiscrete coefficient vector satisfies \(M_p\dot u+Ku=0\). Its exact propagator is
\[
E_p(t)=\exp\!\left(-\frac{t}{h^2}C_n(I-pC_n/6)^{-1}\right).
\]
For fixed \(n\), every \(p\in[0,1]\) gives a positive definite mass matrix. Times are physical positive times, and signs refer to the entries in the nodal basis; no assumption of positivity of all entries is made in advance.

## Proof

**1. An exact Laguerre matrix generating function.** Put \(X=pC_n/6\) and \(z=6t/(ph^2)\) for \(p>0\). All eigenvalues of \(C_n\) lie strictly between \(0\) and \(4\), hence \(\|X\|_2<2/3\). Therefore the matrix identity
\[
E_p(h^2pz/6)=\exp[-zX(I-X)^{-1}]
=\sum_{k=0}^\infty L_k^{(-1)}(z)X^k
\]
follows by absolute convergence from the generalized Laguerre generating function \(\sum_{k\ge0}L_k^{(-1)}(z)w^k=\exp[-zw/(1-w)]\). The latter is an algebraic identity and requires no stochastic approximation.

**2. Distance-filtered leading term.** For nodes \(i\) and \(i+d\), \(1\le d\le n-1\), matrix bandwidth gives \((C_n^k)_{i,i+d}=0\) for \(k<d\). The only path of length \(d\) that reaches the second node yields \((C_n^d)_{i,i+d}=(-1)^d\). Consequently
\[
(E_p(h^2pz/6))_{i,i+d}
=(-1)^d\left(\frac p6\right)^d L_d^{(-1)}(z)+O_{n,K}(p^{d+1})
\]
uniformly for \(z\) in any fixed compact set \(K\subset[0,\infty)\). This is a power-series remainder estimate for fixed dimension, not an empirical approximation. For every \(d\ge1\), the exact polynomial identity
\[
L_d^{(-1)}(z)=-\frac zd L_{d-1}^{(1)}(z)
\]
holds. The ordinary orthogonality of \(L_{d-1}^{(1)}\) with weight \(ze^{-z}\) shows that its \(d-1\) zeros are real, simple and strictly positive. For each one, the leading coefficient changes sign; continuity, uniform convergence and the analytic implicit-function theorem produce a corresponding simple positive zero for all sufficiently small \(p>0\), with \(z_j(p)=\xi_j+O_n(p)\). This proves all the stated local sign switches and first-order crossing times.

**3. Exact count for the farthest pair.** With \(\lambda_k=2-2\cos(k\pi/(n+1))\), the sine eigenvectors give
\[
(E_p(t))_{1n}=\frac2{n+1}\sum_{k=1}^n(-1)^{k+1}
\sin^2\!\left(\frac{k\pi}{n+1}\right)
\exp\!\left[-\frac t{h^2}\frac{\lambda_k}{1-p\lambda_k/6}\right].
\]
The \(n\) decay rates in this sum are strictly increasing and distinct, and all coefficients are nonzero. A nonzero linear combination of \(n\) real exponentials with distinct real exponents has at most \(n-1\) real zeros counted with multiplicity, by the standard inductive Rolle argument after factoring out one exponential. At \(t=0\), the far-end entry is zero. It is a **simple** zero for every \(p>0\): indeed \(6I-pC_n\) has positive off-diagonals and its inverse has strictly alternating nonzero signs: conjugation by the diagonal sign matrix makes \(6I-pC_n\) an irreducible symmetric positive definite matrix with negative nearest-neighbor entries, whose inverse is strictly positive. Because \(G_p=-C_n(I-pC_n/6)^{-1}=(6/p)I-(36/p)(6I-pC_n)^{-1}\), the off-diagonal generator entry at distance \(n-1\) is nonzero. Part 2 supplies \(n-2\) additional simple positive zeros for sufficiently small \(p>0\). Together with the zero at the origin, these exhaust the exponential-polynomial bound. There can be no further real positive zeros or tangencies. Since the lowest sine eigenvector is strictly positive, the far-end entry is positive for large times, establishing the stated full sign-reversal count.

**4. The exact minimal three-interior-node transition.** When \(n=3\), define \(s_1<s_2<s_3\) by
\[
(s_1,s_2,s_3)=\left(\frac{6(2-\sqrt2)}{6-p(2-\sqrt2)},\frac{12}{6-2p},\frac{6(2+\sqrt2)}{6-p(2+\sqrt2)}\right).
\]
Putting \(\tau=t/h^2\), the only offdiagonal entry that may be negative is
\[
(E_p(h^2\tau))_{13}=\frac14\left(e^{-s_1\tau}+e^{-s_3\tau}-2e^{-s_2\tau}\right).
\]
The nearest-neighbor entries equal \((e^{-s_1\tau}-e^{-s_3\tau})/(2\sqrt2)>0\) whenever \(\tau>0\), and all diagonal entries are positive. Write \(x=p/(6-2p)\), so \(0<x\le1/4\); direct common-denominator algebra gives
\[
 s_1+s_3-2s_2=\frac{24}{6-2p}\frac{x+2x^2}{1-2x^2}>0.
\]
Thus for every \(p>0\), with \(\alpha=s_2-s_1>0\) and \(\beta=s_3-s_2>\alpha\), the function \(F(\tau)=e^{\alpha\tau}+e^{-\beta\tau}-2\) has \(F(0)=0\), \(F'(0)<0\), \(F''>0\) and \(F(\tau)\to\infty\). Hence it has precisely one positive zero \(\rho(p)\), and \(E_p(t)\) is entrywise nonnegative exactly when \(t=0\) or \(t\ge h^2\rho(p)\). From the Laguerre root \(\xi_1=2\), \(\rho(p)=p/3+O(p^2)\). For \(p=1\), numerical evaluation gives \(\rho(1)\approx0.2128117769214\). For \(p=0\) every entry is nonnegative for all times since the generator is Metzler.

## Verification

The standalone \(\texttt{verify.py}\) checks the Laguerre identities symbolically, positivity of their roots, inverse-mass signs and matrix exponential formulas over several mesh dimensions and mass mixtures, high-precision leading-term signs, and the exact three-node spectral expression. The embedded checker reports **431 passing finite consistency assertions**. The proof for arbitrary dimensions and the exact zero count rests on the generating-function, orthogonal-polynomial and exponential-Chebyshev arguments above, not on the finite checks.

## Relationship to prior work

Chatzipantelidis, Horváth and Thomée (2015), and Jin, Lazarov, Thomée and Zhou (2015), already establish fundamental nonnegativity failures of Galerkin-type semidiscretizations at small positive times, and recovery mechanisms at large time. Those qualitative facts are **prior art**, not a novel part of this result. Omle, Askar and Kovács (published May 31, 2022) motivate the continuing numerical importance of positive heat propagation; their inspected full text addresses explicit positivity-preserving time algorithms on two-dimensional discretizations, not the blended-mass exact semigroup or Laguerre endpoint crossing hierarchy. The added statement is the specific uniform one-dimensional blended-mass Laguerre scaling and the exact \(n-2\) positive-zero count, including the all-parameter three-node classification.

## Limitations

The arbitrary-dimensional exact crossing count requires sufficiently small positive consistent-mass fraction for each fixed \(n\); no dimension-uniform allowed fraction or all-parameter crossing count is proved. The Laguerre boundary-layer expansion holds with fixed dimension and bounded rescaled time; it does not by itself establish global positivity-restoration times for all \(n\). The exact all-parameter restoration classification is only for \(n=3\). Positivity refers to the nodal coefficient semigroup and exact exponential propagation, not an individual finite-timestep integrator. Potential overlap with older specialized finite-element positivity studies, in particular the inaccessible full 2015 Chatzipantelidis–Horváth–Thomée article, remains a publication-priority uncertainty; its available abstract was reviewed but cannot support a whole-document exclusion.

## References

1. I. Omle, A. H. Askar, E. Kovács, *Systematic testing of explicit positivity preserving algorithms for the heat-equation*, J. Math. Comput. Sci. **12** (2022), article 162, published 2022-05-31, https://doi.org/10.28919/jmcs/7407.
2. P. Chatzipantelidis, Z. Horváth, V. Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, Comput. Methods Appl. Math. **15** (2015), 417–437, https://doi.org/10.1515/cmam-2015-0018. Abstract inspected; full text unavailable during this comparison.
3. B. Jin, R. Lazarov, V. Thomée, Z. Zhou, *On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations*, arXiv:1510.02825 (first public 2015-10-09), https://arxiv.org/abs/1510.02825. Open-access manuscript sections 3–4 and numerical examples consulted.
4. Generalized Laguerre generating function and orthogonality: classical polynomial identities, also verifiable directly by series expansion and integration against the positive weight \(ze^{-z}\).
