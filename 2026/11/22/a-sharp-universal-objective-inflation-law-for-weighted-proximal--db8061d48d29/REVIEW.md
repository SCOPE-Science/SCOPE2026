# Self-review

## Correctness — PASS

The central assertion is the exact all-data, all-gauge bound \(f_b(x_\kappa)/f_b(x_*)\le(1+r)/(r+\kappa(2-\kappa))\), for \(0<\kappa<1\), \(r>0\), nonzero finite nonnegative convex positively homogeneous \(H\), and \(b\ne0\). Every quantifier and exceptional case is explicit. The support-function dual \(H=\sigma_C\) gives the exact minimizer and dual objective. Projection gives \(p\cdot q\ge0\); the factorization \((r+\kappa)^2-[r+\kappa(2-\kappa)](r+\kappa^2)=\kappa^2(1-\kappa)^2\) proves the nonnegative gap. A farthest dual-set point proves sharpness for each nonzero gauge, not merely for a single example. The iteration is contractive for the stated steps. `verify.py` passed exact rational checks on independently evaluated weighted-box cases. The numerical tests are not substituted for the proof.

## Originality — PASS, with historical limitations

The October 2026 motivating work [1] explicitly distinguishes the optimized weighted objective from the comparison objective and derives distance-to-minimizer estimates, but does not state a sharp unweighted *objective ratio* or an all-gauge geometric equality theorem. Its quadratic bias examples do not imply a universal worst-case value comparison with exact saturation for every gauge. Zou and Hastie [2] derive orthogonal-design elastic-net shrinkage, which handles the box dual set but neither arbitrary convex dual geometry nor the universal worst-case ratio. Balcan et al. [3] characterize elastic-net validation loss as piecewise rational in tuning parameters; that is a different risk quantity and a narrower model class. Related thresholding and duality findings do not establish the comparison. Search incompleteness and potentially unnoticed formulations remain historical-priority risks.

## Value — PASS

Weighting the data-fit gradient is an explicit mechanism in [1]; it changes the objective being optimized. A sharp loss inflation factor assesses whether proximity to a weighted critical point translates into good value for the intended unweighted objective. Here the result is uniform over all ambient dimensions and all nonzero convex gauges, yet attainable for every individual gauge. This geometry-independence and complete sharpness are more than a scalar threshold calculation. The formula quantifies how ridge curvature buffers the mismatch; for vanishing ridge it tends to \(1/[\kappa(2-\kappa)]\). It is an exact optimization-quality benchmark, not a result about general nonconvex penalties or stochastic estimates.

## Closest literature and limits

[1] Brito, Lara and Yuan, *A Proximal Gradient Method for Nonconvex Nonsmooth Optimization with Applications*, arXiv:2610.32750 (first public 2026-10-23), especially Algorithm 1, Theorem 3.15, Examples 3.16–3.17 and Section 4. [2] Zou and Hastie, *Regularization and Variable Selection via the Elastic Net*, JRSS B (2005), Sections 2–3. [3] Balcan et al., *Provably Tuning the ElasticNet across Instances*, NeurIPS 2022; the available abstract was consulted, not its full paper. The theorem assumes isotropic quadratic fidelity, an exact proximal update, positive ridge and a finite convex one-homogeneous penalty. No independent mathematical audit or exhaustive historical-priority determination has been completed.

Self-review: passed. Independent audit: not yet performed.
