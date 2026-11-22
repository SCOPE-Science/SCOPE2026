# Complete essential Fourier calculus for an affine Hardy composition semigroup

## Finding
Let \(H=H^2(\mathbb D)\), put \(\varphi_s(z)=1-e^{-s}+e^{-s}z\) for \(s\ge0\), and let \(V_s=e^{-s/2}C_{\varphi_s}\). For a finite complex Borel measure \(\mu\) on \([0,\infty)\), define \(T_\mu=\int_{[0,\infty)}V_s\,d\mu(s)\) as a strong operator integral, and set
\[
\widehat\mu(\xi)=\int_{[0,\infty)}e^{-i\xi s}\,d\mu(s),\qquad\xi\in\mathbb R.
\]
Then the exact operator and essential norms, and the numerical radius, agree:
\[
\boxed{\|T_\mu\|=\|T_\mu\|_{\mathrm{ess}}=w(T_\mu)=\sup_{\xi\in\mathbb R}|\widehat\mu(\xi)|.}
\]
The assertion is **completely isometric**: for every integer \(m\ge1\) and every \(m\times m\) matrix \(\boldsymbol\mu=(\mu_{ij})\) of finite complex Borel measures, the block operator \(\mathcal T_{\boldsymbol\mu}=(T_{\mu_{ij}})\) on \(H^{\oplus m}\) obeys
\[
\boxed{\|\mathcal T_{\boldsymbol\mu}\|=\|\mathcal T_{\boldsymbol\mu}\|_{\mathrm{ess}}=\sup_{\xi\in\mathbb R}\|(\widehat\mu_{ij}(\xi))_{i,j=1}^m\|_{\mathbb C^{m\times m}}.}
\]
In particular \(\mu\mapsto T_\mu\), and its image in the Calkin algebra, are faithful homomorphisms of the convolution algebra of finite measures, equipped on the image with the uniform Fourier-transform norm. No nonzero \(T_\mu\) is compact; its entire sequence of approximation numbers is constant and equal to \(\|T_\mu\|\).

For example, if \(0<a<1\), then
\[
\left\|I+\sqrt a\, C_{1-a+az}-a\,C_{1-a^2+a^2z}\right\|
=\left\|I+\sqrt a\, C_{1-a+az}-a\,C_{1-a^2+a^2z}\right\|_{\mathrm{ess}}=\sqrt5.
\]
Here \(C_{1-a+az}\) means composition by the displayed affine map, not multiplication by it.

## Assumptions and scope
The Hardy norm is the standard boundary \(L^2\) norm. A *finite complex Borel measure* means finite total variation; atoms at zero, singular-continuous measures and unbounded support are allowed. All integrals are defined by \(T_\mu f=\int V_sf\,d\mu(s)\). The essential norm is distance to compact operators. The matrix-level essential norm uses compact operators on \(H^{\oplus m}\), and the matrix norm on the right is the Euclidean spectral norm. No analyticity, positivity or absolute-continuity assumption is placed on the measures.

## Proof
**1. A unitary translation model and contractivity.** Under the Cayley map \(z=(w-1)/(w+1)\), the standard unitary Hardy-space transformation \((Uf)(w)=\sqrt2 f((w-1)/(w+1))/(w+1)\), the Paley--Wiener Laplace transform, and the logarithmic coordinate unitary \((Jg)(u)=e^{u/2}g(e^u)\), the operator \(V_s\) is unitarily equivalent to
\[
(\Sigma_sh)(u)=\exp\bigl(-(1-e^{-s})e^u\bigr)h(u-s),\qquad h\in L^2(\mathbb R).
\]
Indeed, the half-plane symbol is \((w+1-e^{-s})/e^{-s}\), and the Cayley Jacobian supplies the factor \(e^{s}\). In Laplace coordinates, \(C_{\varphi_s}\) becomes \(g(x)\mapsto e^{-(1-e^{-s})x}g(e^{-s}x)\); multiplication by \(e^{-s/2}\) and the logarithmic unitary give the formula above. This also proves \(\|\Sigma_s\|\le1\). The maps \(\Sigma_s\) form a strongly continuous contraction semigroup, since the underlying affine maps compose by addition of the parameter and translations and bounded multipliers vary strongly continuously.

**2. Universal matrix upper bound.** By the continuous Sz.-Nagy unitary-dilation theorem for contraction semigroups, there exist a larger Hilbert space \(K\), an isometry \(E:H\to K\) and a strongly continuous unitary group \((U_s)_{s\in\mathbb R}\) such that \(V_s=E^*U_sE\) for every \(s\ge0\). Strong integration gives \(T_{\mu_{ij}}=E^*(\int U_s\,d\mu_{ij}(s))E\). The spectral theorem for the common unitary group, followed by amplification to \(m\) coordinates, yields
\[
\|\mathcal T_{\boldsymbol\mu}\|\le\sup_{\xi\in\mathbb R}\|(\widehat\mu_{ij}(\xi))\|.
\]
The sign convention for the generator of \(U_s\) may replace \(\xi\) by \(-\xi\); this does not change the supremum. Finite total variation justifies the strong integrals and extension from finite sums.

**3. Weakly null simultaneous approximate eigenvectors.** Fix \(\xi\in\mathbb R\), and on \(L^2(\mathbb R)\) put
\[
h_n(u)=n^{-1/2}e^{i\xi u}\mathbf1_{[-2n,-n]}(u),\qquad n\ge1.
\]
These are unit vectors tending weakly to zero, since their supports escape to the left. For any fixed \(S>0\), all \(0\le s\le S\), and all sufficiently large \(n\), translation of the interval contributes at most \(\sqrt{2S/n}\) in norm, while the damping multiplier differs from one by at most \(e^{-n+S}\) on the translated support. Consequently
\[
\sup_{0\le s\le S}\|\Sigma_s h_n-e^{-i\xi s}h_n\|\le\sqrt{2S/n}+e^{-n+S}\longrightarrow0.
\]
For any finite measure \(\mu\), the contribution of \(s>S\) to the difference is at most \(2|\mu|((S,\infty))\). First taking \(n\to\infty\), then \(S\to\infty\), proves
\[
\|T_\mu h_n-\widehat\mu(\xi)h_n\|\longrightarrow0,
\]
where the vectors are transported through the unitary model. For the matrix case, fix a unit \(v\in\mathbb C^m\); the same componentwise argument gives
\[
\|\mathcal T_{\boldsymbol\mu}(v\otimes h_n)-(\widehat\mu_{ij}(\xi))v\otimes h_n\|\longrightarrow0.
\]
Each \(v\otimes h_n\) is weakly null, so every compact operator sends it to a norm-null sequence. Taking a unit \(v\) maximizing the finite matrix norm gives \(\|\mathcal T_{\boldsymbol\mu}\|_{\mathrm{ess}}\ge\|(\widehat\mu_{ij}(\xi))\|\) for every \(\xi\). Together with the upper bound and \(\|\cdot\|_{\mathrm{ess}}\le\|\cdot\|\), this proves the two matrix equalities.

**4. Consequences.** In the scalar case, the approximate-eigenvector identity also yields \(w(T_\mu)\ge|\widehat\mu(\xi)|\) for every \(\xi\), while \(w(T_\mu)\le\|T_\mu\|\), proving the numerical-radius equality. The uniqueness theorem for Fourier transforms of finite Borel measures implies \(T_\mu=0\Rightarrow\mu=0\); since \(V_sV_t=V_{s+t}\), Fubini proves \(T_\mu T_\nu=T_{\mu*\nu}\). Every finite-rank operator is compact, so all approximation numbers equal the operator norm. Finally the measure \(\delta_0+\delta_h-\delta_{2h}\), where \(h=-\log a>0\), has transform \(1+e^{-i\xi h}-e^{-2i\xi h}\), whose squared modulus on the unit circle is \(3-2\cos(2\xi h)\); its supremum is \(5\), proving the displayed example.

## Verification
The Cayley--Laplace--logarithm conjugacy was independently recomputed from the transformations given in the proof, including the normalization \(e^{-s/2}\). The contraction estimate is pointwise in the model. The essential-norm lower bound uses genuinely weakly null unit vectors and finite-variation tail bounds; no finite sample replaces the limit proof. The matrix extension uses a common unitary dilation, not separate dilations. The equality \(|1+z-z^2|^2=3-z^2-z^{-2}\) for \(|z|=1\) verifies the exact \(\sqrt5\) example.

## Relationship to prior work
Chalendar--Partington (2022) survey composition semigroups and their generator/compactness theory. Gallardo-Gutiérrez--Partington (2022 preprint; 2023 publication), Section 2.1 and Proposition 2.4, explicitly identify the same affine composition semigroup with weighted translations and give the single-operator norm \(\|C_{\varphi_s}\|=e^{s/2}\). These crucial antecedents are credited; the present statement instead addresses *all* finite complex-measure combinations, proves equality after quotienting by compact operators, and includes every finite matrix amplification. Their Proposition 2.4 supplies a model, not a stated exact Fourier-Stieltjes norm identity. Wang--Pang (2016), Theorem 3.7, give an essential-norm lower estimate for finite sums on a different upper-half-plane weighted Bergman space, not a complete equality here. Gallardo-Gutiérrez--González-Doña (2025) study spectral properties of subordinated operators but do not state the same complete essential-norm formula. Cowen (1984) studied the Cesàro operator and a related composition semigroup and is an important historical priority risk; only the abstract was inspected.

## Limitations
The statement is confined to this particular affine boundary-fixed composition semigroup on the classical Hilbert Hardy space; it does not claim analogous identities for arbitrary composition semigroups, weighted Hardy variants, or \(H^p\) with \(p\ne2\). The theorem relies on the standard unitary-dilation theorem for contraction semigroups. Historical priority cannot be exhaustively ruled out, particularly in older semigroup literature where full text could not be obtained. Spectra, Fredholm indices and norm-attaining vectors are not classified here.

## References
1. I. Chalendar and J. R. Partington, *Semigroups of weighted composition operators on spaces of holomorphic functions*, arXiv:2201.09249 (first posted 2022-01-23), https://arxiv.org/abs/2201.09249.
2. E. A. Gallardo-Gutiérrez and J. R. Partington, *Insights on the Cesàro operator: shift semigroups and invariant subspaces*, arXiv:2206.11882 (first posted 2022-06-23), especially Section 2.1, Proposition 2.4, https://arxiv.org/abs/2206.11882.
3. M. Wang and C. Pang, *Difference of composition operators on weighted Bergman spaces over the half-plane*, J. Inequal. Appl. 2016, Article 206, https://doi.org/10.1186/s13660-016-1149-2.
4. E. A. Gallardo-Gutiérrez and F. J. González-Doña, *Local spectral theory for subordinated operators: The Cesàro operator and beyond*, J. London Math. Soc. 112 (2025), e70273, https://doi.org/10.1112/jlms.70273.
5. C. C. Cowen, *Subnormality of the Cesàro operator and a semigroup of composition operators*, Indiana Univ. Math. J. 33 (1984), 305--318 (abstract only checked), https://iumj.s3-us-west-2.amazonaws.com/abstracts/33017_abs.pdf.
