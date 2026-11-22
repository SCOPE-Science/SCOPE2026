# Review of the endpoint-witness covering theorem

## Correctness
**PASS.** The exact Dirichlet exponential-spacing coupling gives \(R_n=\max(D_0,D_n,\max D_i/2)\), so the boundary event is \(W<2Z\) with independent \(Z\) and \(W\). The Beta integral is evaluated exactly, including \(n=1\). The transformed auxiliary density is normalized by that event probability and converges to a Gamma half-shape density with an integrable envelope. Conditional Chebyshev concentration of the spacing denominator establishes the claimed observable covering-radius limit. The exchange symmetry proves fair and independent endpoint marking. Reproducible rational checks support finite cases; they are not used as infinite proofs.

## Originality
**PASS, with historical priority risk.** The original 2015 Reznikov–Saff article includes the asymptotic expected covering radius for rectifiable curves (Corollary 3.6), but not the boundary-versus-interior maximizer indicator on a line segment; the 2021 Penrose treatment includes a polytope strong law applicable to intervals, but not the exact finite one-dimensional marked event. Search comparisons against uniform-spacings extrema and selected mathematical-record results located related maximum-gap dependence but no matching probability plus conditional Gamma law. This is a statement-level distinction, not a claim that absence from search proves priority. Classical exponential/Dirichlet and Gumbel laws are attributed as background. The possibility of an unindexed older formula remains material.

## Value
**PASS.** Worst-case coverage is a standard measure of point-set quality. The theorem gives a finite-sample probability that the bottleneck is an endpoint, proves the sharp \(n^{-1/2}\) localization rate, and identifies an explicitly different conditional error law. This provides location-sensitive reliability information absent from the unconditional covering-radius asymptotic and is not a simple marginal reparameterization.

## Closest literature and limits
Reznikov–Saff, arXiv:1504.03029, is the qualifying historical source (initial posting 2015-04-12; primary MSC includes 60D05). Penrose, arXiv:2101.06306, is a later relevant boundary-effects comparison. Hüsler (1988) was visible through bibliographic metadata and abstract only; undiscovered one-dimensional specializations remain an originality risk. The theorem is restricted to independent uniform sites and the ordinary Euclidean interval metric.

Self-review: passed. Independent audit: not yet performed.
