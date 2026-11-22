# Mathematical review

## Correctness — PASS

The full claim was checked from the normalized analytic Bergman basis rather than inferred from a finite computation. The Jacobi entries follow from the exact normalized shift and radial Toeplitz diagonal, and the all-index polynomial inequality proves the no-outlier side at \(s=1/2\) and above. For smaller \(s\), the exact quadratic form and fixed-parameter \(1/n\) coefficient yield the Coulomb comparison. A geometric-block min–max argument computes the counting constant, and recurrence simplicity yields the individual eigenvalue asymptotic. The included Python checker passed 4,631 supplementary assertions. Potential risks: constant conventions in the free Jacobi edge and boundary cut must be followed; these are explicitly fixed in the proof.

## Originality — PASS, qualified

Simanek's 2018 work already gives the necessary coefficient bound and sufficiency for \(s\ge2\); Simanek 2020 and Le–Simanek 2020 already give the general **implicit** Jacobi norm criterion. The first \(1/n\) bond coefficient is directly accessible by expansion of the published Jacobi formula and is not separately claimed as new. The new reviewed statement is the exact all-parameter closed phase classification and paired exterior Coulomb eigenvalue-counting law, not the background criterion or tail expansion. Luef–Teschl gives general qualitative oscillation criteria. No inspected source or searched record states this combined exact spectral classification. Unindexed equivalents and derivations from more general spectral laws remain residual priority risks.

## Mathematical value — PASS

The motivating classification asks when adding a radial nonharmonic term preserves hyponormality. An exact half-power cut-off substantially extends the old explicit sufficient range. The sharp eigenvalue count measures the entire accumulation of spectral outliers on its failure side and supplies explicit constants; no unmotivated parameter slice or finite computational census is required.

## Scope and limits

Only classical normalized Bergman space and fixed \(s>0\) are treated. The small-exponent coefficient boundary remains the already-known implicit norm expression. The edge-counting constant is not claimed uniformly in \(s\), and no independent mathematical validation has occurred.

Self-review: passed. Independent audit: not yet performed.
