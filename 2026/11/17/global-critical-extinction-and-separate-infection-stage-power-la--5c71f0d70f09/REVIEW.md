# Scientific assessment

## Correctness — PASS

The proof is global over every initially infected state in the closed simplex, not just a local center-manifold expansion. The simplex is invariant for \(0<b\le1/3\), the eventual sign \(q_n=y_n-u_n-v_n\le0\) forces monotone \(z_n=u_n+2v_n\), and an explicit contradiction excludes a positive limit. The stable-response lemma yields \(v_n/z_n^2\to2\) and \(q_n/z_n^2\to-4\), hence \(z_{n+1}^{-2}-z_n^{-2}\to16b\). Symbolic checks reproduce the exact update identities; numerical trajectories only supplement the analytic proof. The infection-free face is handled separately.

## Originality — PASS within inspected evidence

The 2020 Shoyimardonov article (Eq. (6) and Conjecture 2) gives the map and conjectures disease-free convergence in the relevant double-equality regime, but does not supply this slice's global proof or quantitative stage-dependent powers. The 2021 follow-up provides fixed-point threshold analyses and conditional convergence statements without the derived \(n^{-1/2}\) versus \(n^{-1}\) hierarchy. Searches comparing parameter aliases, quadratic stochastic representations, and stronger global results did not find the same four-compartment theorem. Closest indexed epidemic critical-decay results concern different multiple-exposure or SIS network maps, so they do not logically cover this recurrence. Absence from indexed results does not prove publication priority; unindexed equivalent derivations remain a residual risk.

## Value — PASS

This resolves a mathematically motivated, conjectured global-convergence boundary on a natural probability-admissible symmetric slice of a six-parameter epidemiological map. The cancellation of the ordinary quadratic slow drift produces a cubic critical mechanism and **two distinct measured powers** for first infections and reinfections. These are not determined by the previously known local multiplier or fixed-point census; the explicit amplitudes give concrete, initial-condition-independent predictions.

## Scope and scientific limitations

The slice does not resolve the full SISI convergence conjecture and does not describe neighboring parameter unfolding or stochastic finite-population processes. Priority risk from possible unindexed equivalent results remains. Self-review is mathematical and computational only, not independent peer review.

Self-review: passed. Independent audit: not yet performed.
