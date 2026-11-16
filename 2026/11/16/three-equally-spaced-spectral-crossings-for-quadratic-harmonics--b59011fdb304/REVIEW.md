# Scientific review

## Correctness

**PASS.** The four symmetry sectors exhaust the trace-free quadratic harmonics; conditional independent uniform angular directions and \(\operatorname{Beta}(p/2,q/2)\) radial mass yield the normalized eigenvalues. Direct differentiation of \(t^a(1-t)^b(A+Bt)\) proves each of five exact spectral-gap factorizations for arbitrary positive shape parameters, hence three and only three crossings. Positivity of the angular and radial moments, all multiplicities, endpoints, and the thin-cap asymptotic are accounted for. A standalone symbolic checker and an independently assembled numerical generalized Gram eigensystem support the algebra. Main limitations: the theorem does not apply to full harmonic bands or to boundary-only restriction, and its finite numerical examples do not themselves prove the general theorem.

## Originality

**PASS, provisional historical priority.** Full relevant published comparisons distinguish (i) general Slepian construction on \(\mathbb S^2\), (ii) a balanced single-hypersurface four-branch trace theorem, and (iii) one-coordinate antipodal-cap concentration. The present claim deliberately excludes equal-dimensional blocks, treats distinct dimensions at least three, integrates over positive ambient cap volume, and supplies three exact rational crossings, a four-phase global ordering, and a sharp divergence constant. Accessible earlier findings involving real Grassmannians, signed orthants, and coordinate-axis caps have different domains and do not imply these conclusions. Possible broader historical Jacobi-decomposition results remain a residual priority risk; absence of a match is not a proof of global novelty.

## Mathematical value

**PASS.** A block cap is the natural spherical tubular neighborhood of a totally geodesic lower-dimensional sphere. The four-branch spectrum gives sharp stability of all quadrupolar components, while the equally spaced three-transition law identifies the exact geometry where radial modes pass consecutively through each angular sector. The result supplies exact loss-of-observability scaling even as the observed region shrinks. This is a complete classification over an infinite, independently motivated two-parameter family, not merely an isolated numerical invariant.

## Scope and residual limits

Prior intrinsic hypersurface spectra do not become new simply by renaming or rescaling; equal blocks are excluded. Old general methods could conceivably imply the formula via additional work, so priority remains provisional. The complete quantified claim and bibliography are in `RESULT.md`; the checker is `check_exact.py`.

Self-review: passed. Independent audit: not yet performed.
