# Review of the graphical-discotope width theorem

## Correctness — PASS

The radius-normalized Gaussian support representation is exact and uses the ambient \(n\)-dimensional Euclidean sphere. Rayleigh moments, conditional independence of overlapping edge disks, and incidence-pair counting establish both finite moments without approximation. Tree degree excess gives strict path–star uniqueness. The one-dependent multivariate central limit theorem, covariance with the Gaussian radial norm, and delta method give the path limit; a conditional strong law gives the star law. Direct asymptotic integration of the common-coordinate conditional mean yields the logarithmic lower edge and its constant. The attached `verify.py` reproduces numerical moments for twenty graphs and exhaustive finite tree degree bounds for 18,247 labeled trees; tests are supplemental rather than the infinite proof.

## Originality — PASS, with priority risk

The discotope definitions and boundary geometry of Gesmundo–Meroni and the related fiber-body analysis of Mathis–Meroni were inspected at the relevant complete public sources; neither evaluates graph-indexed spherical width moments or the star boundary law. The closest published disk-sum record, *Degree-ellipsoid rigidity and complete contact graphs of bipartite graphical discotopes*, characterizes John–Löwner ellipsoids and contacts, not directional width fluctuations. The closest published variance record, *Sharp width-variance extremizers among tree graphical zonotopes*, concerns line-segment graphical zonotopes, with a different support kernel; no transfer of its absolute-Gaussian results determines the Rayleigh kernel or the nonanalytic logarithmic edge here. The accessible prior research ledger was checked for overlapping claims, and targeted semantic searches returned no identified covering claim. An unindexed generic zonoid correlation theorem or earlier discotope-width work remains a possible historical-priority risk. Literature search is not a proof of uniqueness.

## Mathematical value — PASS

The theorem gives a complete exact second-moment graph invariant for a curved zonoid family, sharply classifies all trees at fixed order, and proves a qualitative bifurcation between Gaussian constant-order path fluctuations and non-Gaussian square-root-order star fluctuations. Its logarithmically suppressed lower-edge law is a substantive boundary feature absent from the line-segment analogue and motivates studying disk-generated random widths rather than restating a generic Gaussian-moment identity. No wider graph-sequence universality or full finite distribution is claimed.

Self-review: passed. Independent audit: not yet performed.
