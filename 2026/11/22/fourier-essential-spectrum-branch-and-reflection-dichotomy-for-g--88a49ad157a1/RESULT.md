# Fourier essential-spectrum branch and reflection dichotomy for generalized Hilbert matrices

## Finding

Let \(\mu\) be a nonzero finite positive Borel measure on \((0,1)\) with
\[
M_\mu=\int_0^1\frac{d\mu(t)}{\sqrt{t(1-t)}}<\infty.
\]
Define the bounded generalized Hilbert matrix \(\Gamma_\mu\) on the coefficient realization of \(H^2(\mathbb D)\) by
\[
(\Gamma_\mu)_{n,k}=\binom{n+k}{k}\int_0^1 t^k(1-t)^n\,d\mu(t),\qquad n,k\ge0.
\]
For each \(\xi\in\mathbb R\), define its weighted-logit Fourier curve
\[
\Lambda_\mu(\xi)=\int_0^1\frac{\exp\!\left(i\xi\log\frac{1-t}{t}\right)}{\sqrt{t(1-t)}}\,d\mu(t).
\]
Then every \(\Lambda_\mu(\xi)\) belongs to the *left essential approximate-point spectrum*: there exist unit vectors \(f_j\rightharpoonup0\) such that \(\|(\Gamma_\mu-\Lambda_\mu(\xi)I)f_j\|\to0\). In particular,
\[
\Lambda_\mu(\mathbb R)\subseteq\sigma_{\mathrm{ess},F}(\Gamma_\mu),
\]
where the latter denotes the Fredholm essential spectrum. The following reflection dichotomy holds **for every such measure**:
\[
\sigma_{\mathrm{ess},F}(\Gamma_\mu)\subseteq\mathbb R
\quad\Longleftrightarrow\quad
\mu(E)=\mu(1-E)\text{ for every Borel }E\subset(0,1).
\]
Thus every *asymmetric* positive measure produces a nonreal Fredholm essential spectral point. Moreover, for every integer \(m\ge1\),
\[
\|\Gamma_\mu^m\|_{\mathrm{ess}}=\|\Gamma_\mu^m\|=M_\mu^m,
\]
so its ordinary and essential spectral radii are \(M_\mu\). No nonzero vector attains the operator norm of \(\Gamma_\mu\).

## Assumptions and scope

The measure is nonzero, positive and finite, is concentrated on the open interval, and satisfies the finite reciprocal-square-root moment above. The matrix uses the \(t^k(1-t)^n\) convention of Bellavita–Chalmoukis–Daskalogiannis–Stylogiannis (2023). Reflection means the pushforward under \(t\mapsto1-t\). The assertion **does not** identify the complete Fredholm essential spectrum for arbitrary measures; it identifies a parameterized subset and a complete *reality-versus-nonreality* criterion. For the zero measure, the spectral and norm identities hold for the zero operator, but norm nonattainment does not.

## Proof

**1. Exact weighted-composition representation.** For \(0<t<1\), set
\[
(T_tf)(z)=\frac{1}{1-(1-t)z}\,f\!\left(\frac{t}{1-(1-t)z}\right).
\]
The binomial identity \((1-z)^{-k-1}=\sum_{n\ge0}\binom{n+k}{k}z^n\) shows on polynomials that \(\Gamma_\mu=\int T_t\,d\mu(t)\); the extension to \(H^2\) follows from the integrable norm bound below.

**2. Unitary logarithmic-coordinate model.** The Cayley unitary from disk \(H^2\) to right-half-plane \(H^2\) is
\[
(Uf)(w)=\frac{\sqrt2}{w+1}f\!\left(\frac{w-1}{w+1}\right).
\]
It conjugates \(T_t\) to
\[
(UT_tU^{-1}F)(w)=\frac{1}{1-t}F\!\left(\frac{t}{1-t}w+\frac{1}{1-t}\right).
\]
Use the Paley–Wiener Laplace isometry (with a consistent Fourier normalization) to identify half-plane \(H^2\) with \(L^2(0,\infty)\), followed by the logarithmic unitary \(h(x)=e^{x/2}g(e^x)\) to \(L^2(\mathbb R)\). Direct substitution gives
\[
(A_th)(x)=\frac{e^{-e^x/t}}{\sqrt{t(1-t)}}\,
 h\!\left(x+\ell_t\right),\qquad
\ell_t=\log\frac{1-t}{t}.
\]
The shift is unitary and the damping multiplier has supremum one; hence \(\|A_t\|=[t(1-t)]^{-1/2}\). For each fixed \(h\), the map \(t\mapsto A_t h\) is continuous in \(L^2\) on \((0,1)\): translations are strongly continuous, and the multipliers converge strongly by dominated convergence on compact subintervals of \((0,1)\). Thus \(Ah=\int_0^1 A_t h\,d\mu(t)\) is a vector-valued Bochner integral with \(\|A\|\le M_\mu\); no Bochner integral in operator norm is needed. The polynomial matrix identities then show that \(\Gamma_\mu\) is unitarily equivalent to \(A\).

**3. Explicit weakly null Fourier packets.** Fix \(\xi\in\mathbb R\). Let \(L_j=j\), \(R_j=j^2\), and set
\[
h_j(x)=(2L_j)^{-1/2}e^{i\xi x}\mathbf1_{[-R_j-L_j,-R_j+L_j]}(x).
\]
These unit vectors converge weakly to zero because their supports escape to \(-\infty\). For each fixed \(t\), the normalized measure of the symmetric difference between this interval and its translate by \(\ell_t\) tends to zero; more precisely, the squared \(L^2\)-translation error in the pure plane-wave packet is at most \(\min(2,|\ell_t|/L_j)\). On both relevant supports \(e^x/t\to0\) uniformly, so the damping multiplier tends uniformly to one. Therefore
\[
\|A_t h_j-[t(1-t)]^{-1/2}e^{i\xi\ell_t}h_j\|_2\longrightarrow0.
\]
The left side is bounded by \(2[t(1-t)]^{-1/2}\). Dominated convergence in \(t\), with respect to \(\mu\), yields
\[
\|(A-\Lambda_\mu(\xi)I)h_j\|_2\to0.
\]
Unitary conjugacy transfers the packets to disk \(H^2\). If \(A-\lambda I\) were Fredholm, an inverse modulo compacts on the left would force these weakly null unit packets to tend to zero in norm, an impossibility. This proves the essential approximate-point and Fredholm claims. Since \(\Lambda_\mu(0)=M_\mu\), every compact \(K\) satisfies \(\|A-K\|\ge M_\mu\); hence \(\|\Gamma_\mu\|_{\mathrm{ess}}=\|\Gamma_\mu\|=M_\mu\). The packet for \(\xi=0\) is also a Weyl packet for every power, by telescoping the difference of powers and uniform boundedness; this proves all \(m\)-power norm formulas and both radius identities.

**4. The reflection dichotomy.** Let \(\nu\) be the finite measure on \(\mathbb R\) obtained by pushing \(d\mu(t)/\sqrt{t(1-t)}\) forward under \(\ell_t=\log((1-t)/t)\). Then \(\Lambda_\mu\) is its Fourier–Stieltjes transform. If the imaginary part vanishes identically, the Fourier transforms of \(\nu\) and its reflection agree; uniqueness of Fourier transforms of finite measures implies that \(\nu\) is symmetric. Since the weight is strictly positive and unchanged by \(t\mapsto1-t\), the original \(\mu\) is symmetric too. Contrapositively, asymmetric \(\mu\) has some \(\xi\) with \(\operatorname{Im}\Lambda_\mu(\xi)\ne0\), so the Fredholm essential spectrum is not real. Conversely, for symmetric \(\mu\), the matrix entries satisfy \((\Gamma_\mu)_{n,k}=(\Gamma_\mu)_{k,n}\) by reflection and are real; hence the bounded matrix operator is self-adjoint, and its entire spectrum is real.

**5. Failure of norm attainment.** For every nonzero \(h\in L^2(\mathbb R)\) and every \(t\in(0,1)\), the multiplier \(e^{-e^x/t}\) is strictly less than one for every finite \(x\). Hence \(\|A_t h\|_2<[t(1-t)]^{-1/2}\|h\|_2\). Integrating the strict positive deficit against the nonzero positive measure yields \(\|Ah\|_2<M_\mu\|h\|_2\). This excludes norm-attaining nonzero vectors.

## Verification

The standalone `check.py` checks the Cayley transform and logarithmic scalar multiplier algebra symbolically, compares 192 rational coefficients against a formal power series recurrence, and illustrates packet boundary and damping errors for a two-atom measure. These finite calculations are auxiliary: the proofs for all indices, all finite positive measures and the essential spectral inclusion are analytical and are given above. The power formulas and Fourier uniqueness require no numerical approximation.

## Relationship to prior work

Bellavita–Chalmoukis–Daskalogiannis–Stylogiannis (2023, Theorems 2–3 and proof in Section 3) established the exact norm and noncompactness of this same family on Hardy spaces. Their weakly null near-extremizers already imply the equality between operator and essential norms at the Hilbert endpoint; **that equality alone is not claimed as original**. The substantive additional statement here is the entire complex Fourier spectral branch and its *if-and-only-if* reflection criterion for the reality of Fredholm essential spectrum, yielding explicit nonreal Fredholm points for every asymmetric measure. Lindström–Miihkinen–Norrbo (2022) treats other generalized Hilbert integral kernels, not this whole positive Hausdorff-derived family. Existing two-atom symmetric spectral classifications cover a specialized self-adjoint case; neither their exact interval nor its norm formula is newly claimed. The 2026 Hausdorff spectral theory on BMOA and Bloch uses different spaces and operator conventions. Relevant abstract general operator-limit methods may independently imply parts of the Fourier-branch statement; this is a residual priority risk, not an independently certified uniqueness claim.

## Limitations

No complete description of \(\sigma_{\mathrm{ess},F}(\Gamma_\mu)\) for arbitrary \(\mu\) is asserted. The Fourier curve can be a proper subset: for a unit atom at \(t=1/2\), the operator is unitarily equivalent to multiplication by \(2e^{-2e^x}\), whose essential spectrum is \([0,2]\), whereas the Fourier curve consists only of \(2\). The result assumes positivity and the finite critical moment; it does not cover arbitrary signed/complex measures or higher Hardy exponents. The coefficient normalization, support conditions, and Fredholm definition are essential to the statement.

## References

1. C. Bellavita, N. Chalmoukis, V. Daskalogiannis, G. Stylogiannis, *Generalized Hilbert operators arising from Hausdorff matrices*, 2023, arXiv:2307.15334, https://arxiv.org/abs/2307.15334 (first public version 28 July 2023).
2. M. Lindström, S. Miihkinen, D. Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, 2022, arXiv:2201.09591, https://arxiv.org/abs/2201.09591.
3. P. Galanopoulos, A. Mahillo, J. Oliva-Maza, A. G. Siskakis, *Hausdorff Matrices on the BMOA and Bloch spaces*, 2026, arXiv:2610.22554, https://arxiv.org/abs/2610.22554 (different function-space setting).
