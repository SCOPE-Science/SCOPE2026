# Sharp negative-set volume and angular stability for quartic Gaussian Fourier eigenfunctions

## Finding

Let \(d\ge2\), let \(Q\colon\mathbb R^d\to\mathbb R\) be a homogeneous quartic polynomial that is **strictly positive** on the unit sphere, and use the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R^d} f(x)e^{-2\pi i x\cdot\xi}\,dx.
\]
Define
\[
 f_Q(x)=e^{-\pi|x|^2}\left(Q(x)-\frac{\Delta Q(x)}{8\pi}\right),
 \quad A(\omega)=Q(\omega),\quad
 \mathcal I(A)=\int_{\mathbb S^{d-1}}|\nabla_{\!S}\log A|^2\,d\sigma,
\]
where \(\sigma\) is **probability** surface measure and \(\omega_d=\pi^{d/2}/\Gamma(1+d/2)\) denotes the Euclidean unit-ball volume. Then \(f_Q\) is a real Schwartz Fourier \(+1\)-eigenfunction satisfying \(f_Q(0)=0\), and its negative set obeys the *sharp dimension-dependent bound*
\[
 \boxed{\quad
 |\{x\in\mathbb R^d:f_Q(x)<0\}|\ge
 \omega_d\left(\frac{d+2}{2\pi}\right)^{d/2}
 \left(1+\frac{\mathcal I(A)}{4(d+2)}\right)^{d/2}.
 \quad}
\]
In particular the minimum over this entire strictly positive quartic-leading class is
\[
 \boxed{\omega_d\left(\frac{d+2}{2\pi}\right)^{d/2}},
\]
attained exactly for positive scalar multiples of \(Q(x)=|x|^4\). These, and only these, give radial minimizers. The inequality is sharp in every dimension; the additional angular term is an exact, dimensionless stability penalty. In dimension \(d=2\), the bound becomes \(|\{f_Q<0\}|\ge 2+\mathcal I(A)/8\).

## Assumptions and scope

The variable \(d\) is any integer at least two. The polynomial \(Q\) is real, homogeneous of degree four, and \(Q(\omega)>0\) at every unit direction. No convexity of \(Q\) is assumed. All norms and measures are Lebesgue unless otherwise stated. The set \(\{f_Q<0\}\) is bounded because \(Q\) has a positive lower bound on the compact sphere. The same volume is obtained with \(\{f_Q\le0\}\), since the zero set of the nonzero polynomial factor has Lebesgue measure zero. An arbitrary real Fourier \(+1\)-eigenfunction of the form polynomial-of-degree-at-most-four times the Gaussian, with zero value at the origin and strictly positive top-degree homogeneous term, has **exactly** the displayed form; this is the first nontrivial finite Hermite band (orders zero and four) for the \(+1\) eigenvalue. The theorem does not address higher bands, noncoercive leading quartics, or the unrestricted global definite-set uncertainty problem.

## Proof

**1. Fourier eigenfunction classification.** The Gaussian \(g(x)=e^{-\pi|x|^2}\) is Fourier self-dual. Differentiating its transform shows that for a homogeneous quartic \(Q\),
\[
 \widehat{Qg}=g\left(Q-\frac{\Delta Q}{4\pi}+\frac{\Delta^2Q}{32\pi^2}\right).
\]
For any homogeneous quadratic \(R\),
\[
 \widehat{Rg}=g\left(-R+\frac{\Delta R}{4\pi}\right).
\]
Substituting \(R=-\Delta Q/(8\pi)\) cancels the fourth-derivative constant term and proves \(\widehat{f_Q}=f_Q\). Since \(\Delta Q\) is quadratic, \(f_Q(0)=0\). Conversely, the Fourier eigenvalue equation fixes the quadratic part from the homogeneous quartic leading part, while the freely adjustable constant part is forced by the condition at the origin. Hence there are no omitted polynomial eigenfunctions under the stated degree and leading-term hypotheses.

**2. An exact polar volume formula.** Write \(x=r\omega\) with \(r>0\) and \(\omega\in\mathbb S^{d-1}\). The Euclidean and spherical Laplacians satisfy the homogeneous identity
\[
 \Delta Q(r\omega)=r^2\bigl(4(d+2)A(\omega)+\Delta_S A(\omega)\bigr).
\]
Define
\[
 \rho_0^2=\frac{d+2}{2\pi},\qquad
 h(\omega)=\rho_0^2+\frac{\Delta_S A(\omega)}{8\pi A(\omega)}.
\]
Then the **exact factorization** is
\[
 f_Q(r\omega)=e^{-\pi r^2}\,r^2 A(\omega)\bigl(r^2-h(\omega)\bigr).
\]
The ray is negative exactly at \(0<r<\sqrt{h(\omega)}\) when \(h(\omega)>0\), and nowhere on that ray when \(h(\omega)\le0\). Consequently, with \(s_+=\max(s,0)\),
\[
 |\{f_Q<0\}|=\omega_d\int_{\mathbb S^{d-1}}h(\omega)_+^{d/2}\,d\sigma(\omega). \tag{1}
\]
This identity is finite, because \(A\) is positive and smooth on the compact sphere.

**3. Spherical integration by parts and Jensen.** As the sphere has no boundary,
\[
 \int_{\mathbb S^{d-1}}\frac{\Delta_S A}{A}\,d\sigma
 =-\int\nabla_S A\cdot\nabla_S(A^{-1})\,d\sigma
 =\int|\nabla_S\log A|^2\,d\sigma
 =\mathcal I(A).
\]
Therefore
\[
 \int h\,d\sigma=\rho_0^2+\frac{\mathcal I(A)}{8\pi}
 =\rho_0^2\left(1+\frac{\mathcal I(A)}{4(d+2)}\right)>0.
\]
For \(d\ge2\), the map \(s\mapsto s_+^{d/2}\) is convex. Applying Jensen to (1) gives
\[
 |\{f_Q<0\}|\ge\omega_d\left(\int h\,d\sigma\right)^{d/2}
 =\omega_d\rho_0^d\left(1+\frac{\mathcal I(A)}{4(d+2)}\right)^{d/2}.
\]
Since \(\mathcal I(A)\ge0\) and the sphere is connected, \(\mathcal I(A)=0\) if and only if \(A\) is constant. By quartic homogeneity, this means \(Q(x)=c|x|^4\) with \(c>0\). For these \(Q\), \(h\equiv\rho_0^2\), so both inequalities are equalities. Conversely, any nonconstant \(A\) makes the right-hand stability factor strictly greater than one and hence cannot attain the minimum.

**4. Exact planar excess formula.** When \(d=2\), the positive-part identity \(h_+=h+(-h)_+\) and (1) give, without assuming \(h\ge0\),
\[
 \boxed{|\{f_Q<0\}|=2+\frac{\mathcal I(A)}8+
 \pi\int_{\mathbb S^1}(-h(\omega))_+\,d\sigma(\omega).}
\]
The last term quantifies the additional excess when some directions have no negative radii. This establishes a complete exact angular decomposition in the plane.

## Verification

The accompanying `checker.py` independently replays Gaussian Fourier differentiation on every monomial of total degree four in dimensions two, three and four; checks Euler homogeneity; and tests the polar identity and Fisher-information formula by a high-resolution periodic angular quadrature on a nonradial strictly positive quartic. It has 173 successful assertions. These finite checks **do not prove** the all-dimensional statement: the analytic proof above does. To replay, install NumPy and SymPy and run `python checker.py` alongside this file. The radial equality value is \(2\) in dimension two and \(9/2\) in dimension four.

## Relationship to prior work

Roni Edwin, *Fourier inequalities and sign uncertainty II* (first publicly posted November 5, 2026, arXiv:2611.08224), formulates the definite-set uncertainty principle: minimize the measure of a Fourier eigenfunction's nonpositive set subject to vanishing at the origin. That source establishes global dimension-dependent lower bounds; the present theorem instead solves **exactly** the first nontrivial quartic Gaussian Fourier eigenspace with positive leading form, including uniqueness and a spherical Fisher-information stability term. It does **not** purport to solve the unrestricted Edwin problem. The 2023 Dicke–Seelmann–Veselić Hermite spectral inequalities estimate \(L^2\) observability on externally prescribed sets and do not imply the sharp *sign-defined* volume formula here. The classical Hermite and Gaussian Fourier identities are used as ingredients, not claimed as novel.

## Limitations

Coercivity of the quartic leading form is assumed; we do not claim an exact optimizer for all Fourier eigenfunctions, for higher Hermite orders, or for noncoercive leading forms. The angular penalty is sharp at radial equality and becomes an equality throughout a larger class of planar examples; it is not claimed pointwise optimal for every prescribed positive angular Fisher information in higher dimension. The novelty comparison is limited to the inspected primary sources, published-record searches and recoverable prior claims; priority under unrelated terminology remains subject to independent literature review. No independent mathematical audit has been performed.

## References

1. R. Edwin, *Fourier inequalities and sign uncertainty II*, arXiv:2611.08224v1 (first public posting 2026-11-05), https://arxiv.org/abs/2611.08224.
2. R. Edwin, *Fourier inequalities and sign uncertainty*, arXiv:2505.15994 (2025), https://arxiv.org/abs/2505.15994.
3. A. Dicke, A. Seelmann, and I. Veselić, *Uncertainty Principle for Hermite Functions and Null-Controllability with Sensor Sets of Decaying Density*, J. Fourier Anal. Appl. 29, article 11 (2023), https://doi.org/10.1007/s00041-022-09989-5.
4. A. Bonami, B. Demange, and P. Jaming, *Hermite functions and uncertainty principles for the Fourier and the windowed Fourier transforms*, Rev. Mat. Iberoam. 19 (2003), 23–55, https://doi.org/10.4171/RMI/337.
