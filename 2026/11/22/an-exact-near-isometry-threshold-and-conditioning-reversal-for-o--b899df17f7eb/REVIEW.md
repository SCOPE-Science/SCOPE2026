# Review of the one-collision unicyclic sketch-spectrum finding

## Correctness — PASS
For any unit-weight connected unicyclic incidence space, the circulation vector gives the projector \(P=I-cc^{\mathsf T}/\ell\). One collision changes the ambient sketch Gram by a difference of two orthogonal rank-one projectors; compression yields an exact two-root characteristic equation, with each of four sign/support cases checked. The kernel-intersection dimension argument excludes all multiple-collision events at distortion below one. Counting collision-free maps and unique cycle–bridge collisions proves the probability. The singular-value calculation establishes the strict reversal. The embedded verifier confirms 1,260 exact rational polynomial cases and exhaustive small signed-hash cases. Risks: incorrect whitening or extrapolation beyond distortion one would invalidate the claim; neither is done here.

## Originality — PASS (qualified)
The closest published item, *Exact signed CountSketch rank survival for weighted unicyclic incidence matrices* (2026), gives the rank-survival law and the circulation-hyperplane reduction for the same setting. Rank survival is expressly excluded from new contributions. Its complete inspected result and proof did not state the one-collision Gram spectral atoms, the exact squared-norm distortion distribution below one, or the conditioning-vs-distortion reversal. Clarkson–Woodruff (2012) and Hu et al. (2021) supply more general sparse embedding frameworks; neither inspected full-text treatment makes these exact finite unicyclic statements. A codimension-one sketch-frame result not found in the searches may still subsume them.

## Value — PASS
The dimension-critical one-collision regime separates three commonly conflated diagnostics: full algebraic rank, subunit subspace norm distortion, and singular-value conditioning. The exact near-isometry success probability provides a closed benchmark at any \(n,\ell,m\); the strictly reversed rankings of two genuinely rank-preserving collision classes explain why maximizing one diagnostic can worsen another. This is structurally sharper than an isolated small example, while confined to a meaningful restricted graph family and not a general embedding theorem.

Self-review: passed. Independent audit: not yet performed.
