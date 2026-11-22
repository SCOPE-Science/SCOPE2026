# Scientific review

## Correctness
**PASS.** The proof specifies the exact circular gap model, a tagged Dirichlet identity, the explicit one-dependent overlap probability and an independent-block Poisson construction. The normalization and random starting phase are handled explicitly. A local-dependence Chen–Stein bound plus concentration of the exponential total yields the fixed-threshold total-variation rate. Checks in `check.py` concern independently computed finite identities and simulations, not an infinite certificate.

## Originality
**PASS, qualified historical priority.** A previously established exact full vector law for circular Voronoi cell lengths gives finite-n coverage and, for odd sample sizes, recovers all original gaps and finite shape marks; it must be credited as substantial prior mathematical coverage. However, this does not itself provide the spatial/height/left-right-marked extreme process, its asymptotic independence or the explicit total-variation bound; those require the new extremal analysis. The closest verified classical \(m\)-spacing paper treats unmarked exceedance counts; the inspected maximal-empty-spacing result concerns a different geometric functional, and the inspected Voronoi paper concerns typical cells. None of the inspected scientific text supplies the product-intensity spatial/height/left-right-skew point process or the maximizing-cell mark independence. The 1993 full paper was not accessible for a conclusive whole-document comparison; an inaccessible older source remains a priority risk, not positive evidence of novelty. Standard gamma-Dirichlet splitting and Poisson-approximation ingredients are acknowledged.

## Value
**PASS.** The maximal cell is an intrinsic worst-case load/coverage descriptor of one-dimensional Voronoi sampling. Its *shape* matters: a long cell can be almost entirely due to one neighboring gap or split relatively evenly. A uniform extreme-cell skew and its independence of the extreme score and spatial location determine this geometric imbalance for the full cloud of unusually large cells, beyond the unmarked largest-size law. The rate for exceedance counts gives a usable finite-sample calibration.

## Closest literature and limitations
Roos (1993), *Compound Poisson approximations for the numbers of extreme spacings*, DOI 10.2307/1427795; Aaron–Cholaquidis–Fraiman (2014), arXiv:1411.2482; Devroye–Györfi–Lugosi–Walk (2015), arXiv:1512.04267; Barbour–Holst–Janson (1992), *Poisson Approximation*, Chapter 7. Old full-text access remains incomplete. The result is limited to the uniform circular model; no stronger optimality or density universality is claimed.

Self-review: passed. Independent audit: not yet performed.
