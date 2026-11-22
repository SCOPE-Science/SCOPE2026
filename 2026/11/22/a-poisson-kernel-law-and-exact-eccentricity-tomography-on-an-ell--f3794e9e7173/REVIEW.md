# Scientific review

## Correctness — PASS

The sampled object is precisely the ordered pair of supporting tangents with outward normals \(\Theta\) and \(\Theta+\pi/2\). Both supporting-line equations, the circle radius, inverse normal-to-position Jacobian, Fourier coefficients, exact total variation, and singular weak and local limits follow from explicit identities given in RESULT.md. The strict positivity of the angular Jacobian excludes fold multiplicities. The Cauchy total-variation limit uses normalized pointwise density convergence and Scheffé's lemma. An executable verifier checked 327,728 deterministic statements; these checks supplement rather than replace the proof.

## Originality — PASS, with historical qualification

The nearest classical sources establish the director circle, conic isoptics, and general support-function parametrizations. Odehnal's 2010 paper treats the locus and equations of equioptics; Csima–Szirmai's 2013 paper treats conic isoptics in constant-curvature geometries; Cieślak–Mozgawa's 2021 support-function theorem describes circular orthoptics without choosing a tangent-angle probability measure. The 2008 ellipse isoptic demonstration gives an explicit curve-generation method but not a probability pushforward. A comparison with published related results on ellipse boundary normals, normal multiplicity and isoptic area did not identify a statement implying the *specific probability law plus inversion and total-variation limit*. The general parametrization is acknowledged and only the sampling-induced consequences are claimed. Historical uncatalogued treatments remain possible; no independent priority determination has occurred.

## Mathematical value — PASS

A classical locus alone gives only the radius and does not distinguish ellipses with the same sum of squared semiaxes. The new observable is a natural invariant of sampling uniformly in tangent-normal angle. Its exact half-uniform/half-Poisson decomposition gives the complete law, one complex moment recovers anisotropy and axis orientation, an exact total-variation distance measures deviation from circularity, and a striking half-diffuse/half-atomic limit quantifies the collapse of highly eccentric ellipses. These features make this a fully resolved inverse-geometric measurement problem, not merely another equation for the director circle.

## Closest literature and residual qualifications

Primary geometric sources: B. Odehnal (2010), https://www.geometrie.tuwien.ac.at/odehnal/tr200.pdf ; G. Csima and J. Szirmai (2013), https://arxiv.org/abs/1301.6991 ; W. Cieślak and W. Mozgawa (2021), https://doi.org/10.1007/s00010-021-00828-4 ; Csima–Szirmai–Tóth (2008), https://demonstrations.wolfram.com/IsoOpticCurveOfTheEllipse/ . One 2008 online resource exposes only a year, not an independently verified date to the day. The precisely dated primary 2010 report gives the recorded source date. The theorem is restricted to ellipses and normal-angle uniformity; it does not claim a rigidity characterization among all ovals.

Self-review: passed. Independent audit: not yet performed.
