# Gradient concentration of quadratic spherical harmonics on positive orthants

## Finding

On the unit sphere \(S^{d-1}\), let \(d\ge3\), let \(\sigma\) be probability surface measure, and let
\[\Omega_d=\{x\in S^{d-1}:x_1>0,\ldots,x_d>0\}.\]
For the complex exact-degree-two spherical-harmonic space \(\mathcal H_2(d)\), define the **Dirichlet-normalized gradient concentration operator** \(G_d\) by
\[
\langle G_df,g\rangle_D
=\int_{\Omega_d}\langle\nabla_Sf,\nabla_Sg\rangle\,d\sigma,
\qquad
\langle f,g\rangle_D=\int_{S^{d-1}}\langle\nabla_Sf,\nabla_Sg\rangle\,d\sigma.
\]
Here all gradients are tangential and the inner product is sesquilinear (linear in its first argument). Set
\[
a=\frac2\pi,\quad
\alpha_d=(1-a)\left(1+\frac{2a}{d}\right),\quad
\beta_d=\frac{a(d-2+4a)}{2d},\quad
\gamma_d=-\frac{2a^2}{d},
\]
\[
L_d=\alpha_d+2(d-1)\beta_d+\binom d2\gamma_d,\qquad
M_d=\begin{pmatrix}1&a\sqrt{(d-2)/2}\\a\sqrt{(d-2)/2}&\alpha_d+(d-2)\beta_d\end{pmatrix},
\]
and let \(\mu_-(d)<\mu_+(d)\) be the eigenvalues of \(M_d\). The complete spectrum of \(G_d\) is

| Eigenvalue | Multiplicity |
|---|---:|
| \(2^{-d}\mu_+(d)\) | \(d-1\) |
| \(2^{-d}L_d\) | \(1\) |
| \(2^{-d}\alpha_d\) | \(d(d-3)/2\) |
| \(2^{-d}\mu_-(d)\) | \(d-1\) |

The \(\alpha_d\) row is absent when \(d=3\). For every \(d\ge3\),
\[
0<\mu_-(d)<\alpha_d<L_d<\mu_+(d)<2^d.
\]
Consequently the largest and smallest concentration eigenspaces **both** have dimension \(d-1\), and the sharp concentration-eigenvalue condition number is
\[
\boxed{\displaystyle \kappa(G_d)=\frac{\mu_+(d)}{\mu_-(d)}
=\frac{d}{\pi-2}+O(1)\quad(d\to\infty).}
\]
Thus tangential-gradient energy observation on the positive orthant has linearly, not quadratically, growing spectral condition number in ambient dimension. By contrast, the previously computed *scalar-value* quadratic concentration on exactly the same orthant has a simple maximal sector and a dimension-squared condition-number law. This is a comparison of two **different** observation norms, not an equivalence of their operators.

## Assumptions and scope

The theorem holds for all integers \(d\ge3\), with real or complex quadratic spherical harmonics \(f(x)=x^{\mathsf T}Qx\), \(Q^{\mathsf T}=Q\), \(\operatorname{tr}Q=0\); complexification uses the Hermitian form. This is a pure harmonic degree, not a low-pass band. The open orthant has \(\sigma\)-mass \(2^{-d}\); its boundary is null. Every operator eigenvalue is a fraction of full-sphere Dirichlet energy. \(\kappa(G_d)\) is the ratio of largest to smallest concentration eigenvalues, whereas the corresponding gradient restriction operator has singular-value condition number \(\sqrt{\kappa(G_d)}\). There are no discrete measurement sites, weights to optimize, or noise assumptions.

## Proof

**1. Normalized gradient identity and absolute moments.** Write the coefficient coordinates
\[
f(x)=\frac1{\sqrt2}\sum_{i=1}^d u_ix_i^2+\sum_{i<j}v_{ij}x_ix_j,
\qquad \sum_i u_i=0.
\]
Equivalently \(f(x)=x^{\mathsf T}Qx\) with \(Q_{ii}=u_i/\sqrt2\) and \(Q_{ij}=v_{ij}/2\) for \(i\ne j\). Full-sphere moments and the harmonic Laplace eigenvalue \(2d\) yield
\[
\int_{S^{d-1}}|f|^2d\sigma=\frac{\|u\|^2+\|v\|^2}{d(d+2)},\qquad
\int_{S^{d-1}}|\nabla_Sf|^2d\sigma=\frac{2(\|u\|^2+\|v\|^2)}{d+2}.
\]
Pointwise,
\[
\nabla_Sf(x)=2(Qx-f(x)x),\qquad
|\nabla_Sf(x)|^2=4(x^{\mathsf T}Q^*Qx-|f(x)|^2),
\]
where \(Q^*Q\) is the Hermitian matrix product (for real matrices, \(Q^2\)). Given the positive orthant, \(X\) has the same law as \((|Z_1|,\ldots,|Z_d|)/\|Z\|\) for independent standard real Gaussians. Therefore, for total degree \(k\) and nonnegative integer exponents,
\[
\mathbb E_{\Omega_d}\prod_i X_i^{k_i}
=\frac{\Gamma(d/2)}{\Gamma((d+k)/2)}
\prod_i\frac{\Gamma((k_i+1)/2)}{\Gamma(1/2)}.
\]
In particular \(d\mathbb E_{\Omega_d}X_iX_j=1\) for \(i=j\) and \(=a=2/\pi\) otherwise.

**2. The complete regional quadratic form.** Let \(B\) be the unsigned vertex-edge incidence matrix of the complete graph on \(d\) vertices, namely \((Bv)_i=\sum_{j\ne i}v_{\min(i,j),\max(i,j)}\); let \(S(v)=\sum_{i<j}v_{ij}\). The fourth moments give the scalar quadratic form
\[
d(d+2)\,\mathbb E_{\Omega_d}|f(X)|^2
=\|u\|^2+(1-a)^2\|v\|^2+a(1-a)\|Bv\|^2+a^2|S(v)|^2
+2\operatorname{Re}\left(\frac{a}{\sqrt2}\langle u,Bv\rangle\right).
\]
For the other term in the gradient identity, \(\operatorname{tr}(Q^*Q)=(\|u\|^2+\|v\|^2)/2\) and \(\|Q\mathbf1\|^2=\frac12\|u\|^2+\frac14\|Bv\|^2+\frac1{\sqrt2}\operatorname{Re}\langle u,Bv\rangle\). The second moments consequently yield
\[
d\,\mathbb E_{\Omega_d}\|QX\|^2
=(1-a)\operatorname{tr}(Q^*Q)+a\|Q\mathbf1\|^2.
\]
Insert these expressions into the pointwise gradient identity and divide by the global Dirichlet norm. The resulting scaled Hermitian form for \(2^dG_d\), relative to \(\|u\|^2+\|v\|^2\), is exactly
\[
\boxed{\|u\|^2+\alpha_d\|v\|^2+\beta_d\|Bv\|^2+
\gamma_d|S(v)|^2+
2\operatorname{Re}\left(\frac a{\sqrt2}\langle u,Bv\rangle\right).}
\]
This formula is also a finite-dimensional characterization independent of the subsequent diagonalization.

**3. Symmetry decomposition.** The identity \(BB^{\mathsf T}=(d-2)I+J\) splits edge coordinates orthogonally into: the constant-edge line; \(B^{\mathsf T}(\mathbf1^\perp)\), of dimension \(d-1\); and \(\ker B\), of dimension \(d(d-3)/2\), the last absent when \(d=3\). On the constant-edge line, the values \(\|Bv\|^2=2(d-1)\|v\|^2\) and \(|S(v)|^2=\binom d2\|v\|^2\) give \(L_d\). On \(\ker B\) the eigenvalue is \(\alpha_d\). For each unit \(w\in\mathbf1^\perp\), the orthonormal pair \(u=w\) and \(v=B^{\mathsf T}w/\sqrt{d-2}\) has precisely the matrix \(M_d\). Therefore \(\mu_\pm(d)\) each occur with multiplicity \(d-1\), and all \((d-1)(d+2)/2\) dimensions are accounted for. The extremal harmonic subspaces are those two standard-representation eigenspaces.

**4. Rigorous eigenvalue ordering.** Set \(p(t)=\det(M_d-tI)\). Since \(1/2<a=2/\pi<2/3\), direct factorization gives
\[
p(\alpha_d)=\frac{a^2(d-2)}{d^2}\bigl[d(3a-2)+4a^2-6a+2\bigr]<0.
\]
Moreover
\[
L_d-\alpha_d=\frac{a(d-1)}{d}\bigl[d(1-a)+4a-2\bigr]>0,
\]
\[
p(L_d)=\frac{a^2(d-2)}{2d}
\bigl[d(a-1)-3a+1\bigr]
\bigl[d(2a-1)-6a+4\bigr]<0.
\]
The last first bracket is negative and the second is at least one (equality at \(d=3\)). Each negative polynomial value places its argument strictly between the two eigenvalues of \(M_d\). It follows that \(\mu_-<\alpha_d<L_d<\mu_+\). Nonzero pure quadratics cannot have identically zero tangential gradient on the open orthant, so every concentration eigenvalue is strictly positive; the nonempty open complement similarly gives the strict upper bound one for the actual eigenvalues. The \(\alpha_d\) expression is a useful comparison number even when that spectral row is absent at \(d=3\).

**5. Sharp large-dimensional law and contrast.** As \(d\to\infty\), the lower right entry of \(M_d\) is \(ad/2+O(1)\), its off-diagonal squared is \(a^2d/2+O(1)\), and thus
\[
\mu_+(d)=ad/2+O(1),\qquad \mu_-(d)=1-a+O(d^{-1}).
\]
The quotient is \(a/[2(1-a)]\,d+O(1)=d/(\pi-2)+O(1)\). For comparison, the known scalar-value orthant concentration operator on the same \(\mathcal H_2(d)\) has \(\kappa(C_d)\sim 2(\pi-2)d^2/[\pi^2(\pi-3)]\). In dimension three, the three distinct gradient eigenvalues (multiplicities respectively two, one, two) reduce to
\[
\frac{6\pi-1+\sqrt{73}}{48\pi},\qquad
\frac{3\pi+2}{24\pi},\qquad
\frac{6\pi-1-\sqrt{73}}{48\pi}.
\]
They sum with multiplicities to \(5/8\), as required by the rotationally invariant trace density and orthant area.

## Verification

Execute `python verify_orthant_gradient.py` with NumPy installed. It constructs each *full* quadratic gradient Gram matrix independently from Gaussian absolute moments, diagonalizes matrices in dimensions \(3\) through \(10\), checks every predicted eigenvalue and multiplicity, strict ordering, and trace, and checks the asymptotic constant at three larger dimensions. The tested code emitted `ORTHANT_GRADIENT_SPECTRUM_CHECKS_PASS 243`. The optional `python verify_factors.py` (SymPy) independently checks the displayed factorization identities, and emitted `ORTHANT_GRADIENT_SYMBOLIC_IDENTITIES_PASS 6`. These finite checks are independent numerical corroboration; the proof of every dimension is the moment identity and symmetry decomposition above.

## Relationship to prior work

Michel, Plattner and Seibert (first posted 2021-03-26; arXiv:2103.14650) develop a unified spin-weighted spherical Slepian framework, giving general regional concentration matrices and special commuting constructions for spherical caps. Their general formulation motivates exact study of nonspherical observation regions, but it does not evaluate the all-dimensional orthant tangential-gradient spectrum or its sharp linear conditioning law. Earlier vector Slepian research also supplies general regional machinery, not this evaluated operator. *Exact quadratic spherical-orthant concentration and a sharp dimension-squared stability law* (2026) evaluates the **scalar-value** orthant operator and, in its derivation, the needed fourth-moment form; the present different Dirichlet observation requires an additional second-moment term and changes both the maximizing representation and conditioning order. Existing exact gradient-concentration results for spherical lunes and paired caps use different observation regions and do not determine the positive-orthant matrix. This relationship is a genuine close overlap in methods, not evidence of historical uniqueness.

## Limitations

Only exact-degree-two gradient fields are treated; the result does not classify full tangent-vector spaces, higher harmonic degrees, arbitrary simplicial regions, or discrete sampling. The numerical checks are finite; they do not certify all dimensions. The all-dimensional asymptotics concern concentration-eigenvalue conditioning, not noise-optimal reconstruction under a specified measurement scheme. Priority remains provisional because the scalar orthant moment method is available in prior work, and an unindexed explicit gradient evaluation could exist. No independent mathematical validation has been performed.

## References

1. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first posted 2021-03-26), https://arxiv.org/abs/2103.14650.
2. A. Plattner and F. J. Simons, *Spatiospectral concentration of vector fields on a sphere*, arXiv:1306.3201 (first posted 2013-06-13), https://arxiv.org/abs/1306.3201.
3. *Exact quadratic spherical-orthant concentration and a sharp dimension-squared stability law*, publicly indexed mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-quadratic-spherical-orthant-concentration-and-a-sharp-dime--043aca2fd738.
