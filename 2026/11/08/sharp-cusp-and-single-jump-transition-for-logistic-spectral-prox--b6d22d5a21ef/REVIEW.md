# Scientific review: logistic spectral proximal transition

## Correctness — PASS

The theorem is quantified over every positive hardness and threshold and every positive scaled penalty multiplier. Its proof derives the unique maximum of the shrinker derivative by an explicitly strictly increasing tanh equation; the inverse-function formula then gives the unique minimum of penalty curvature. For subcritical scaling, strong convexity proves uniqueness; at equality, the stationarity map is strictly increasing despite a single zero derivative, and its nonzero cubic coefficient yields the sharp one-third Hölder cusp. Beyond the threshold, precisely two folds produce two outer stationary minima; strict descent of their objective-value difference yields exactly one tie input and excludes all other global ties. A quartic rescaling gives the one-half minimizer-jump exponent and three-halves fold-window exponent with leading constants. Singular-vector alignment transfers the failure of unique minimization to rank-one spectral problems. `verify.py` checks the fold, tie, and critical scales at finite precision. The infinite-parameter claims rely on the analytic proof, not sampling or enumeration.

## Originality — PASS, with residual priority risk

Yang, Wang and Yang (arXiv:2610.21664v1, §§3–5) construct the exact penalty and sharp weak-convexity constant, and prove scaled proximal uniqueness for the sufficient strict inequality \(\beta\rho<1\). Their Theorems 5.2–5.3 leave the equality and postcritical regimes open: they do not claim a unique tie input, one-third critical cusp, one-half jump or three-halves fold width. Chartrand (ICASSP 2014) supplies the general inverse-designed shrinkage-penalty principle without this family-specific scaled bifurcation. Lu et al. (arXiv:1412.2231, §§2–3) provide generalized singular-value thresholding and generic set-valued proximal arguments without these exact logistic constants. Published published-finding corpus claims on other proximal or fold phenomena do not imply this quantitative classification. Structural similarities to universal quartic catastrophe theory create a historical-priority risk; the claim is the complete, explicitly normalized logistic family-specific result, not the generic existence of such bifurcations.

## Mathematical value — PASS

The source's weak-convexity inequality is a usable uniqueness safeguard but leaves an important practical scaling boundary unresolved. The result establishes that the boundary is an attained but non-Lipschitz single-valued regime and that every larger scale necessarily has a unique input with two distinct global solutions, already in rank one. Leading-order constants predict the onset of multivaluedness and the shrinking region of three competing stationary points, clarifying uniqueness, numerical conditioning, and the limits of scalar root-finding used in spectral recovery. This gives a motivated, nonroutine boundary classification, without asserting algorithmic failure outside the source's proven range.

## Closest literature and limits

- G. Yang, Z. Wang, G. Yang, *Data-Driven Smooth-to-Hard Spectral Regularization for General Linear Inverse Problems*, arXiv:2610.21664v1 (first public 2026-10-15), especially §4, Thms 5.1–5.3: https://arxiv.org/html/2610.21664v1
- R. Chartrand, *Shrinkage mappings and their induced penalty functions*, ICASSP 2014: https://www.researchgate.net/publication/272790166_Shrinkage_mappings_and_their_induced_penalty_functions
- C. Lu et al., *Generalized Singular Value Thresholding*, arXiv:1412.2231: https://arxiv.org/abs/1412.2231

The proof does not cover general penalties, practical iterative algorithms, hard-threshold limits uniform in the hardness parameter, or independent mathematical validation. A broader classical catastrophe-theory formulation may subsume some local asymptotics, but the global all-scale one-tie classification is separately established for the precise family here.

Self-review: passed. Independent audit: not yet performed.
