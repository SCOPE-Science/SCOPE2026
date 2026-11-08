# Distinct analytic pinning responses of intrinsic and chordal circular Lloyd dynamics

## Finding

For each integer \(n\ge3\), the von Mises weight \(w_\kappa(\theta)=\exp(\kappa\cos\theta)\) selects two distinct, locally unique reflection-symmetric fixed-codebook branches for the intrinsic and chordal Lloyd maps near the regular \(n\)-gon. These branches are analytic for sufficiently small \(|\kappa|\), and each is locally attracting within the reflection-symmetric configuration space. With \(L=\pi/n\) and \(\alpha_j=2\pi j/n\), their angular coordinates obey

\[
q_j^{\mathrm I}(\kappa)=\alpha_j-\kappa\,B_{\mathrm I}(L)\sin\alpha_j+O_n(\kappa^2),\qquad
B_{\mathrm I}(L)=\frac{\sin L/L-\cos L}{\sin^2 L},
\]

\[
q_j^{\mathrm C}(\kappa)=\alpha_j-\kappa\,B_{\mathrm C}(L)\sin\alpha_j+O_n(\kappa^2),\qquad
B_{\mathrm C}(L)=\frac{L-\sin L\cos L}{2\sin^3 L}.
\]

The **strict inequality** \(B_{\mathrm C}(L)>B_{\mathrm I}(L)>0\) holds for every \(n\ge3\), so the intrinsic and chordal fixed-codebook branches are distinct for all sufficiently small positive \(\kappa\). Moreover, for **every** \(\kappa>0\), no regular \(n\)-gon, in any angular orientation, is fixed by either Lloyd map with this fixed von Mises density.

## Assumptions and scope

Angles are taken modulo \(2\pi\), with ordered lifts satisfying \(q_0<q_1<\cdots<q_{n-1}<q_0+2\pi\); near the reference configuration use lifts \(q_j^0=2\pi j/n\) and cyclic extensions \(q_{j+n}=q_j+2\pi\). The Voronoi cell for codepoint \(q_j\) is the circular interval
\[
R_j(Q)=\left[\frac{q_{j-1}+q_j}{2},\,\frac{q_j+q_{j+1}}2\right].
\]
Put its center and half-width equal to
\[
m_j=\frac{q_{j-1}+2q_j+q_{j+1}}4,\qquad s_j=\frac{q_{j+1}-q_{j-1}}4.
\]
The weight \(w_\kappa\) need not be normalized, since any positive normalizing factor cancels from Lloyd updates. Define the **intrinsic** map by the local arithmetic (Fréchet) centroid
\[
[T_{\mathrm I,\kappa}(Q)]_j=\frac{\int_{m_j-s_j}^{m_j+s_j}\theta\,w_\kappa(\theta)\,d\theta}{\int_{m_j-s_j}^{m_j+s_j}w_\kappa(\theta)\,d\theta},
\]
and the **chordal** map by the local circular first moment
\[
[T_{\mathrm C,\kappa}(Q)]_j=\operatorname{Arg}_{m_j}\left(\int_{m_j-s_j}^{m_j+s_j}e^{i\theta}w_\kappa(\theta)\,d\theta\right).
\]
Here \(\operatorname{Arg}_{m_j}\) is the continuous argument lift lying near \(m_j\); for configurations near the regular polygon, every cell has length strictly below \(\pi\), ensuring a nonzero moment and an unambiguous local branch. The two maps correspond to different squared-distance distortions: intrinsic geodesic distance and Euclidean chord distance. They must not be conflated.

Reflection symmetry means \(q_0=0\) and \(q_{n-j}=2\pi-q_j\) for \(1\le j<n\), including \(q_{n/2}=\pi\) when \(n\) is even. All existence, analyticity, uniqueness, and attraction assertions concern fixed points in a neighborhood of \(Q^0\) **inside this reflection-symmetric subspace**. We make no claim of transverse or global attraction.

## Proof

**1. Uniform-density linearization.** At \(\kappa=0\), symmetry of each interval makes both updates exactly equal to its midpoint \(m_j\). Thus every rotated regular polygon is fixed. The common Jacobian of either full map at \(Q^0\) is the periodic tridiagonal matrix
\[
J_0=\frac12 I+\frac14(S+S^{-1}),
\]
where \(S\) is the cyclic shift on \(n\) coordinates. Its Fourier eigenvalues are
\[
\lambda_k=\frac12+\frac12\cos\frac{2\pi k}{n}=\cos^2\frac{\pi k}{n}\qquad (k=0,\ldots,n-1).
\]
The sole eigenvalue one is the constant-vector rotation mode. Reflection-odd perturbations \(\delta q_{n-j}=-\delta q_j\), with \(\delta q_0=0\), have no constant mode. Therefore \(I-J_0\) is invertible on that subspace and the restriction of \(J_0\) has spectral radius strictly less than one.

**2. Local analytic fixed branches.** The density is analytic in angles and \(\kappa\); positivity of the centroid denominator and nonvanishing of the circular first moment hold in a fixed neighborhood of \((Q^0,0)\). Both maps preserve the reflection subspace because \(w_\kappa(-\theta)=w_\kappa(\theta)\), the Voronoi cells reflect, and either centroid transforms by reflection. The analytic implicit-function theorem applied to \(Q-T_{\bullet,\kappa}(Q)=0\), restricted to the reflection subspace, gives a unique analytic branch near \(Q^0\) for each convention. Continuity of the derivative and its strict spectral radius below one at \(\kappa=0\) give local attraction for small \(|\kappa|\) within this subspace. There is no assertion of a unique fixed point without the reflection constraint: the rotation mode makes the unrestricted implicit-function theorem inconclusive at \(\kappa=0\).

**3. First-order forcing of the regular polygon.** For \(Q^0\) the cell about \(\alpha_j\) is \(\alpha_j+[-L,L]\). Differentiating the intrinsic weighted mean at \(\kappa=0\) produces
\[
\left.\partial_\kappa T_{\mathrm I,\kappa}(Q^0)_j\right|_0
=\frac1{2L}\int_{-L}^{L}t\cos(\alpha_j+t)\,dt
=-\left(\frac{\sin L}{L}-\cos L\right)\sin\alpha_j.
\]
For the chordal map, write its moment as \(e^{i\alpha_j}\int_{-L}^{L}e^{it}e^{\kappa\cos(\alpha_j+t)}dt\). The real moment at zero concentration is \(2\sin L>0\). Its argument derivative is hence
\[
\left.\partial_\kappa T_{\mathrm C,\kappa}(Q^0)_j\right|_0
=\frac{\int_{-L}^{L}\sin t\cos(\alpha_j+t)\,dt}{2\sin L}
=-\frac{L-\sin L\cos L}{2\sin L}\sin\alpha_j.
\]
The vector \((\sin\alpha_j)_j\) is a \(k=1\) sine Fourier eigenvector of \(J_0\), with eigenvalue \(\cos^2 L\). Differentiating the fixed-point equations gives \((I-J_0)Q'(0)=\partial_\kappa T_{\bullet,\kappa}(Q^0)|_0\). Dividing by \(1-\cos^2L=\sin^2L\) yields exactly the two coefficients displayed in the finding, with componentwise \(O_n(\kappa^2)\) remainder.

**4. Strict separation of the two response coefficients.** On \(0<L\le\pi/3\), \(\sin L-L\cos L>0\), because its derivative is \(L\sin L>0\) and it vanishes at zero. Similarly \(L-\sin L\cos L>0\). A direct common-denominator subtraction gives
\[
B_{\mathrm C}-B_{\mathrm I}
=\frac{f(L)}{2L\sin^3 L},\qquad
f(L)=L^2+L\sin L\cos L-2\sin^2 L.
\]
Here \(f(0)=f'(0)=0\), while
\[
f''(L)=4\sin L\bigl(\sin L-L\cos L\bigr)>0\qquad(0<L\le\pi/3).
\]
Therefore \(B_{\mathrm C}>B_{\mathrm I}>0\). Since for \(n\ge3\) at least one \(\sin\alpha_j\) is nonzero, the two analytic branches genuinely separate at first order.

**5. No regular polygon is fixed at positive concentration.** Let a regular polygon be rotated arbitrarily so that one cell is centered at \(\alpha\). For \(0<t<L\), the exact identity
\[
w_\kappa(\alpha+t)-w_\kappa(\alpha-t)
=-2e^{\kappa\cos\alpha\cos t}\sinh(\kappa\sin\alpha\sin t)
\]
has strict sign \(-\operatorname{sgn}(\sin\alpha)\) for \(\kappa>0\) whenever \(\sin\alpha\ne0\). The intrinsic centroid displacement has numerator \(\int_0^L t[w_\kappa(\alpha+t)-w_\kappa(\alpha-t)]dt\). The imaginary part of the centered chordal moment has numerator \(\int_0^L\sin t[w_\kappa(\alpha+t)-w_\kappa(\alpha-t)]dt\), while its real part is strictly positive because \(\cos t>0\) on \([-L,L]\). Thus **both** centroids move strictly in direction \(-\operatorname{sgn}(\sin\alpha)\) for every such cell. No configuration of \(n\ge3\) equally spaced centers has \(\sin\alpha_j=0\) for all \(j\); consequently neither Lloyd map can fix any rotated regular polygon at \(\kappa>0\).

## Verification

The accompanying standalone standard-library program `verify.py` implements both cell-centroid formulas by Simpson quadrature and checks the strict drift sign on regular polygons, nearby fixed-codebook iterations and first-order response coefficients for \(n\in\{3,4,5,7,10\}\) at small concentrations. It also checks strict coefficient ordering for integers \(3\le n<100\). Expected terminal report:

```text
VERIFY_OK drift_sign_checks=132 analytic_branch_cases=20 strict_coefficient_cases=97
```

This finite numerical check is supplementary. The all-\(n\) and all-positive-concentration statements follow from the preceding analytic proof, not from sampling.

## Relationship to prior work

Saha, Jha and Roychowdhury (2026a, arXiv:2602.11926v1) derive general intrinsic centroid conditions and high-resolution density laws for nonuniform spherical-curve quantization; they also compare numerical geodesic and chordal von Mises codebooks, including a seven-point example. That work already demonstrates qualitative metric-dependent deformation; **this theorem does not claim to discover deformation or the two metrics**. Its new claim is the finite-\(n\), small-concentration **analytic fixed-branch** construction and exact, strictly ordered coefficient pair.

The same authors (2026b, arXiv:2605.29451v1) formulate the circle Lloyd iteration as a dynamical map and study linear stability and equally spaced configurations under von Mises weighting. Their Proposition 3.4 describes an equally spaced configuration as fixed at nonzero concentration; the exact positive-concentration drift identity here shows why the reflection of the cell about its own center is insufficient when the density mean direction remains fixed. Their rotational covariance theorem simultaneously rotates the density and codebook, whereas the present problem holds the density fixed. The formula for the uniform-density Jacobian is compatible with their Fourier approach, but the finite-density branch response is additional.

The earlier papers do not supply the displayed pair of finite-\(n\) first-order coefficients or their strict comparison in the inspected versions. No publication-level priority or independent completeness guarantee is asserted.

## Limitations

These are local fixed-point statements at small \(|\kappa|\), with attraction asserted only within the reflection-symmetric codebook subspace. No global minimizer classification, global convergence, unrestricted local stability, finite-\(\kappa\) branch continuation, or nonlinear higher-order response is established. The two centroid maps minimize different cell distortions and are not interchangeable. The regular-polygon nonfixed result, by contrast, is valid for every \(\kappa>0\) and every regular-polygon orientation. External priority review remains to be done.

## References

1. S. Saha, S. Jha, M. K. Roychowdhury, *Optimal Quantization for Nonuniform Densities on Spherical Curves*, arXiv:2602.11926v1 (first public 2026-02-12), https://arxiv.org/abs/2602.11926.
2. S. Saha, S. Jha, M. K. Roychowdhury, *Linear stability analysis of the Lloyd algorithm on a circle*, arXiv:2605.29451v1 (first public 2026-05-28), https://arxiv.org/abs/2605.29451.
3. M. K. Roychowdhury, *Optimal Quantization on Spherical Surfaces: Continuous and Discrete Models—A Beginner-Friendly Expository Study*, *Mathematics* **14** (2026), article 63, https://doi.org/10.3390/math14010063 (background on intrinsic and chordal quantization).
