# Independent audit — 2026-09-29
- Source: `2026/09/12/032`
- Assigned/current tree SHA: `df7b629e9ffa84cf538b467423cd30b50e7f4718`
- Audited repository commit: `eff2c6312cec5b0dee5115e5f42211a853092dfb`
- Disposition: **failed**

## Three-axis assessment

### Correctness

**PASSED** — The displayed pair really violates the stated inequality. Both boxes are centered, have 8 facets, satisfy the ball bounds, and give normalized cone-volume mass 1/8 on each ±e_i, hence W2=0. Independent Euclidean computation gives directed Hausdorff distances sqrt(0.03) and 0.2, so the optimal-translation distance is 0.2 by the x1-projection lower bound. However, the committed verification script computes an L-infinity point-to-box distance (maximum coordinate excess) rather than Euclidean distance; its 0.1 first-direction value is wrong even though the final max remains 0.2.

### Originality

**FAILED** — The obstruction is not specific to the anisotropic box pair: normalized cone-volume measure is invariant under positive homothety because the cone-volume measure and total volume both scale by λ^n. Therefore any admissible class containing two distinct homothetic bodies already gives W2=0 but positive Hausdorff distance unless scale/volume is fixed. The record’s example is a concrete instance of this immediate scale-invariance obstruction.

### Scientific value

**FAILED** — The example usefully diagnoses a missing scale anchor in the proposed stability statement, but as a research claim it reduces to a formulation-level homothety invariance observation. Together with the metric bug in the committed verifier, this does not meet the threshold for a validated research finding.

## Independent checks

- current main record tree exactly equals the assigned source-tree SHA
- recomputed all eight normalized facet weights as 1/8
- recomputed Euclidean directed Hausdorff distances sqrt(0.03) and 0.2 from all box vertices
- proved the projection lower bound d_H(P,Q+t)>=0.2+|t1|
- checked normalized cone-volume measure is unchanged by K -> λK while Hausdorff scale changes

## Limitations

- The exact box counterexample remains valid despite the verifier’s wrong metric in one directed calculation.
- This audit rejects the record as original research; it does not reject stability theorems with a fixed volume/scale normalization or other additional hypotheses.
- No inaccessible paper was treated as read; open literature and the definition of cone-volume measure suffice for the scaling check.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/032
- https://real.mtak.hu/10063/
- https://doi.org/10.1090/S0894-0347-2012-00741-3
- https://real.mtak.hu/58172/
- https://doi.org/10.1016/j.aim.2016.10.005

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
