# The sharp two-neighbor filter for Gaussian shift-invariant Riesz conditioning

## Finding
Fix an inverse-variance shape parameter \(s>0\). Among all nondegenerate real two-neighbor generators
\[
\psi_{s,t}(x)=e^{-\pi s x^2}-t e^{-\pi s(x-1)^2},\qquad t\in\mathbb R\setminus\{-1,1\},
\]
for the same Gaussian integer-translate space, the squared Riesz-condition number \(\kappa_s(t)=B_s(t)/A_s(t)\) has exactly two global minimizers, which are reciprocal. Put
\[
q=e^{-\pi s/2},\quad H=\vartheta_3(0,q),\quad J=\vartheta_4(0,q),\quad
 t_s=\frac{\sqrt H-\sqrt J}{\sqrt H+\sqrt J}\in(0,1).
\]
The minimizing coefficients are exactly \(t=t_s\) and \(t=t_s^{-1}\). Here \(\vartheta_3(z,q)=\sum_{k\in\mathbb Z}q^{k^2}e^{2ikz}\) and \(\vartheta_4(0,q)=\vartheta_3(\pi/2,q)\).

Let \(\Theta_q(u)=\vartheta_3(\tfrac12\arccos u,q)\) for \(-1\le u\le1\). The two spectral endpoints are **simultaneous, strict minima** at either optimal coefficient, and the unique interior spectral maximizer \(u_s\in(-1,1)\) is characterized by
\[
\sum_{n=1}^{\infty}\frac{2q^{2n-1}}{1+2q^{2n-1}u_s+q^{4n-2}}
 =\frac{2t_s}{1+t_s^2-2t_su_s}.
\]
Consequently the exact optimal condition number is
\[
\boxed{\ \kappa_s^{\mathrm{opt}}
=\frac{\Theta_q(u_s)(1+t_s^2-2t_su_s)}{J(1+t_s)^2}
=\frac{\Theta_q(u_s)(1+t_s^2-2t_su_s)}{H(1-t_s)^2}.\ }
\]
For weakly overlapping (narrow) Gaussian translates (\(s\to\infty\), or \(q\downarrow0\)),
\[
t_s=q+q^3+O(q^5),\qquad
\kappa_s^{\mathrm{opt}}=1+4q^2+O(q^4),\qquad
\kappa_s(0)=1+4q+O(q^2).
\]
Thus the optimal two-neighbor filter changes the leading condition-number excess from order \(e^{-\pi s/2}\) to order \(e^{-\pi s}\), without changing the generated closed subspace.

## Assumptions and scope
Use the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx\). For any finite complex coefficient sequence \(c\), the *sharp squared Riesz bounds* of the integer translates of \(\psi_{s,t}\) are the best numbers \(0<A_s(t)\le B_s(t)<\infty\) satisfying
\[
A_s(t)\sum_{k\in\mathbb Z}|c_k|^2\le
\left\|\sum_{k\in\mathbb Z}c_k\psi_{s,t}(\cdot-k)\right\|_{L^2(\mathbb R)}^2
\le B_s(t)\sum_{k\in\mathbb Z}|c_k|^2.
\]
The case \(t=\pm1\) is excluded because its translate system has no positive lower Riesz bound. All real \(t\ne\pm1\) are included, including \(t=0\) and negative parameters. The condition number is for the *squared* synthesis norm (not its square root). No assertion is made about general complex, longer, or non-consecutive filters, nor about frame bounds of a Gabor time-frequency lattice.

## Proof
**Step 1: Exact multiplier and preservation of the space.** Direct Gaussian integration gives
\[
\langle e^{-\pi s(\cdot-j)^2},e^{-\pi s(\cdot-k)^2}\rangle
=(2s)^{-1/2}e^{-\pi s(j-k)^2/2}.
\]
Thus Parseval on the coefficient torus diagonalizes the Gaussian-translate Gram form with multiplier \((2s)^{-1/2}\vartheta_3(\pi\xi,q)\). Filtering the generator by \(1-t e^{-2\pi i\xi}\) gives
\[
G_{s,t}(\xi)=\frac1{\sqrt{2s}}\vartheta_3(\pi\xi,q)
(1+t^2-2t\cos(2\pi\xi)).
\]
Its essential infimum and supremum are exactly \(A_s(t)\) and \(B_s(t)\); continuity turns these into ordinary minima and maxima. The Jacobi product below proves strict positivity of \(\vartheta_3\), so \(A_s(t)>0\) exactly when \(t\ne\pm1\). For those parameters the scalar filter and its reciprocal are bounded on the coefficient circle, hence the filtered and original translated families span the same closed Gaussian shift-invariant subspace.

**Step 2: One-dimensional strict logarithmic concavity.** Jacobi's absolutely locally uniformly convergent triple product gives, for \(-1\le u\le1\),
\[
\Theta_q(u)=\prod_{n=1}^{\infty}(1-q^{2n})
(1+2q^{2n-1}u+q^{4n-2}).
\]
Each affine factor is positive on this interval. Therefore \(\log\Theta_q(u)\) is strictly increasing and strictly concave, as its derivative is a strictly positive convergent series and its second derivative is strictly negative. For \(0\le t<1\), \(u\mapsto\log(1+t^2-2tu)\) is concave (strict for \(t>0\)). Hence
\[
F_t(u)=\Theta_q(u)(1+t^2-2tu)
\]
has strictly concave logarithm. Its minimum over \([-1,1]\) must occur at an endpoint, and its maximum is unique. The endpoint values are
\[
F_t(-1)=J(1+t)^2,\qquad F_t(1)=H(1-t)^2.
\]
Since \(0<J<H\), these endpoint values cross exactly once on \([0,1)\), at \(t=t_s\) as displayed. Before this crossing the minimum is at \(-1\); after, at \(1\). At the crossing both endpoints equal and, by strict log concavity, the unique maximum lies in \((-1,1)\), with both endpoints strictly below it. Differentiating the product and the filter yields exactly the displayed scalar equation for \(u_s\), which consequently has one solution in \((-1,1)\).

**Step 3: Strict global minimax comparison.** For \(0\le t<t_s\), normalize the multiplier by its minimizing endpoint:
\[
\frac{F_t(u)}{F_t(-1)}
=\frac{\Theta_q(u)}{J}\left(1-\frac{2t}{(1+t)^2}(1+u)\right).
\]
The scalar \(t/(1+t)^2\) increases strictly for \(0\le t<1\). Therefore the normalized value decreases strictly in \(t\) for every \(u>-1\). Since the normalized maximum is strictly greater than one, \(\kappa_s(t)\) decreases strictly on \([0,t_s]\). For \(t_s<t<1\), normalization at the other endpoint yields
\[
\frac{F_t(u)}{F_t(1)}
=\frac{\Theta_q(u)}H\left(1+\frac{2t}{(1-t)^2}(1-u)\right).
\]
This increases strictly for every \(u<1\), and the maximum lies away from the minimizing endpoint. Hence \(\kappa_s(t)\) increases strictly on \([t_s,1)\).

If \(-1<t<0\), both \(\Theta_q(u)\) and \(1+t^2-2tu\) increase strictly in \(u\), so the condition number strictly exceeds its value at \(t=0\). For any \(|t|>1\), \(F_t=t^2F_{1/t}\), giving \(\kappa_s(t)=\kappa_s(1/t)\). These observations and the vanishing lower bound at \(t=\pm1\) give precisely the two claimed global real minimizers.

**Step 4: Sharp high-separation asymptotics.** By the Jacobi series, uniformly for \(|u|\le1\) as \(q\downarrow0\),
\[
\Theta_q(u)=1+2qu+2q^4(2u^2-1)+O(q^9),
\]
while analytic expansion of the theta constants gives \(t_s=q+q^3+O(q^5)\). Consequently, uniformly on the full interval,
\[
F_{t_s}(u)=1+q^2-4q^2u^2+O(q^4).
\]
Its unique maximum is \(1+q^2+O(q^4)\), since the value at \(u=0\) matches that upper envelope, whereas its common endpoint minimum is \(1-3q^2+O(q^4)\). Division gives the optimal expansion. Finally \(\kappa_s(0)=H/J=1+4q+O(q^2)\).

## Verification
The accompanying `verify.py` independently evaluates \(\Theta_q\) by its defining Jacobi series (not its product), checks the Gaussian Gram Poisson duality, solves the interior maximum numerically, tests the minimizing filter against alternatives on both sides, and verifies the small-\(q\) coefficient at high precision. It passed **145 numerical assertions** over positive widths and parameter perturbations. These are consistency checks; the all-parameter theorem and the strictness of its inequalities come from the preceding analytic argument, not from finite sampling.

For example, at \(s=1\), the optimal two-neighbor coefficient is approximately \(0.216845335437\), and the sharp squared Riesz-condition number falls from approximately \(2.414213562373\) (unfiltered) to \(1.198140924365\).

## Relationship to prior work
Romero–Ulanovskii–Zlotnikov (first public 2023-06-23, arXiv:2306.13619) study sampling of Gaussian shift-invariant spaces; their setting motivates well-conditioned Gaussian translate representations but their results do not optimize a two-neighbor generator. Grohs–Liehr (published online 2023-10-04, DOI:10.1007/s00365-023-09629-1), Sections 2.1–2.2, explicitly supply the general periodized-Fourier criterion for Riesz bounds and the Gaussian theta multiplier. Those ingredients are used here, and **are not claimed as new**. The contribution is the sharp *global* minimax filter coefficient among all real two-neighbor filters, its unique interior extremal-frequency equation, and the exact second-order decay of the optimal conditioning excess. Kiselev–Minin–Novikov–Sitnik (2014), Section 2 and Table 1, calculates exact Riesz constants for unfiltered Gaussian translates and their infinite-coefficient nodal interpolation generator; these results are prior and do not optimize the adjacent two-term filter. Faulhuber's 2017 theta/Gabor frame optimization concerns a different problem: optimizing Gabor lattice geometry for fixed Gaussian windows rather than adjacent-translate generator filters.

## Limitations
The optimizer is only asserted among real-valued **two-neighbor** filters of a single fixed Gaussian shift-invariant space. Neither optimality among complex filters of the same length nor among longer filters is established. The explicit best condition number requires one unique scalar implicit root; no elementary closed form is asserted. The small-\(q\) expansions apply only as \(s\to\infty\). Independent mathematical validation and exhaustive historical-priority verification have not been performed. Published shift-invariant-space theory and classical theta identities are prior ingredients, not discoveries of this result.

## References
1. J. L. Romero, A. Ulanovskii and I. Zlotnikov, *Sampling in the shift-invariant space generated by the bivariate Gaussian function*, arXiv:2306.13619 (first version 2023-06-23), https://arxiv.org/abs/2306.13619.
2. P. Grohs and L. Liehr, *Stable Gabor Phase Retrieval in Gaussian Shift-Invariant Spaces via Biorthogonality*, *Constructive Approximation* 59 (2024), 61–111 (published online 2023-10-04), https://doi.org/10.1007/s00365-023-09629-1.
3. E. A. Kiselev, L. A. Minin, I. Ya. Novikov and S. M. Sitnik, *On the Riesz Constants for Systems of Integer Translates*, *Mathematical Notes* 96 (2014), 228–238, https://doi.org/10.1134/S0001434614070244; official author-hosted Russian full text https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=eng&paperid=10386&what=fullt.
4. M. Faulhuber, *Minimal Frame Operator Norms Via Minimal Theta Functions*, *Journal of Fourier Analysis and Applications* 24 (2018), 545–559 (published online 2017-02-11), https://doi.org/10.1007/s00041-017-9526-x.
5. Classical Jacobi triple-product identity and Poisson summation for Gaussians (standard identities; used only with absolutely convergent series and products).
