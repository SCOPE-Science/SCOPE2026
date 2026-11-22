# Self-review

## Correctness — PASS

The result is a complete finite/infinite one-step fiber classification on the specified half-open cube and integer-gain domain. The critical monotone cubic has exactly the enumerated sheets; the middle modular equation has exactly \(m\) residues; the first equation becomes a half-open interval count of integers. The strict lower endpoint and closed upper endpoint account for every boundary, including \(u=0\) versus the excluded \(u=1\). The only free-coordinate case occurs when \(v=0\), yielding exactly the explicitly stated exceptional image set. The determinant identity independently identifies this rank-collapse locus on smooth cells. Surjectivity for \(m\ge2\) and non-surjectivity for \(m=1\) follow directly from the proved count, not simulations. The exact-rational checks and numerical reconstruction tests in `verify.py` corroborate the derivation; they are not treated as infinite proofs.

## Originality — PASS, conditional on accessible evidence

The full originating published paper defines the 3D map and assesses numerical chaos and pseudorandom output, not the number of real one-step ancestors. The original intertwining map has a sine nonlinear term and is not algebraically the same map. A previously available result for the identical map counts fixed points on the invariant face; such points are solutions of a different, far more constrained equation and the face result does not entail the all-target, full-dimensional inverse counts, global onto threshold, or critical continuum. Related indexed results on coupled Gumowski–Mira maps and polynomial modular skew maps have different defining equations and cannot be substituted into the present cubic-sheet calculation. Actual searches for the source, modular inverse-fiber aliases, and numerical values did not find a direct dominating claim; lack of indexed results is not itself proof of novelty. Risks remain from unindexed comparable analyses and the full text of the earlier sine-map source, which was only checked via an accurate quotation in the originating article.

## Value — PASS

One-step invertibility is a natural state-reconstruction invariant for noninvertible modular dynamics, especially a system proposed as a deterministic output generator. The theorem settles it on the **full state cube** for the natural integer gains, including the published gain \(m=64\). The combination of the sharp onto/non-onto distinction, a complete exact formula, a rank-collapse continuum-fiber locus, and a universal six-figure inverse multiplicity is not a trivial renaming or a mere low-precision simulation. No cryptographic security conclusion is inferred from the inverse count, and no higher-iterate classifications are claimed.

## Closest literature and scientific limits

- W. Zhao and C. Ma, *Symmetry* **16** (2024), 169, https://doi.org/10.3390/sym16020169, full HTML scientific sections inspected.
- G. Ye and X. Huang, *Neurocomputing* **251** (2017), 45–53, original sine formula quoted by Zhao and Ma. Its complete text was not inspected.
- Published inverse-sheet results for coupled Gumowski–Mira maps and modular skew maps use distinct equations. Their indexed statements address different objects; fetching two of those complete articles was unsuccessful, so their unseen sections are not certified as noncovering. Indexed comparison does not exhaust all potential equivalent literature.

The theorem concerns exact real arithmetic for integer \(64\mu\), not physical finite-precision implementations or long-time dynamics. The displayed six-figure bounds are certified bounds, not asserted optimal.

Self-review: passed. Independent audit: not yet performed.
