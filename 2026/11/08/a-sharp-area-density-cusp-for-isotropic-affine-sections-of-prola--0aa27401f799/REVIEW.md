# Independent mathematical audit

## correctness

PASS

Rebuilt the invariant-plane disintegration: s=|u_z| is uniform before conditioning; hit interval length 2b h(s) makes p(s)=h/H and normalized signed offset v independent uniform [-1,1]. For Q=b^{-2}diag(1,1,r^{-2}), det(Q|u⊥)=h²/(b⁴r²), and slice reduction 1-v² gives X=r(1-v²)/h. Thus P(X>x)=H^{-1}∫h√(1-xh/r)_+ and E[X]=2r/(3H). Differentiating the survival (integrable endpoint) and substituting h=√(1+(r²-1)s²) yields exact density (1). At x=1 the upper endpoint weight W(r)=r²/[2H(r²-1)]; replacing y=r-h shows Δf=-2rW(r)√ε+O(ε) from below; moving-upper-limit sin² reparameterization from above gives analytic behavior; away from x=1 changes are analytic. Support [0,r], b=√(A_cusp/π), r=A_max/A_cusp. Independent SciPy quadratures at r=1.3,2,4,12 recovered left coefficients to within 0.0051 relative at ε=10^-5, with finite right slopes; independent 80,000-plane simulations for r=1.3,2,4 matched means and survival. Finite checks corroborate, not prove, exact asymptotics. Boundary ball r=1 explicitly excluded.

## originality

PASS

Qualified best-of-knowledge: a 1986 primary paper already numerically plotted section-area distributions for prolate ellipsoids, and 1976 general stereological joint-size/shape theory is a serious potential predecessor. Neither accessible primary full result establishes the exact Crofton-invariant density cusp, unique singular point, sharp nonzero one-sided coefficient and area-only endpoint/cusp inversion. This judgment credits all known special/implicit laws and does not mistake a failed search for proof of worldwide priority.

## value

PASS

Natural Crofton invariant-plane sampling of a fixed spheroid induces a sharp, analytically nontrivial change in the range of allowed normal angles when raw area crosses the minor-axis disk area. The resulting universal fractional density coefficient and two-feature area-only reconstruction are structural and usable exact population invariants, distinct from classical section-ellipse size/shape inference. The 1986 numerical area histograms are credited, and no finite-observation/noise guarantee is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
