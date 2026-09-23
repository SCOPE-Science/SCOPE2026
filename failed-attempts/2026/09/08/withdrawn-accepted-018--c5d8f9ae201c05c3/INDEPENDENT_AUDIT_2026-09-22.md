# Independent audit — 2026-09-22

**Disposition: FAILED ATTEMPT.** Recovery verification performed 2026-09-23 UTC against public `main` head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`. The assigned source directory still has exact tree SHA `1de203618e80d999bdc5c2c2384166f9cd9232e0`, matching the assignment guard. RESULT.md blob: `4bd2fcc625ce4e99ed614f191ceaa4d08bbdea2d`.

## Claim reviewed
Discrete Willmore gap extremal among a selected 20-mesh family. This audit preserves reproducible finite computations where supported while evaluating correctness, originality, and scientific value separately.

## Correctness
PASS. The recovered audit independently replayed the stated 20-mesh finite survey, checked closedness/Euler characteristic, reproduced the stored Bobenko-energy values and the reported separation of the selected 8×8 mesh from the other 19 surveyed competitors. The current source tree is unchanged from the audited snapshot.

## Originality
NARROW. Bobenko's Möbius-invariant discrete Willmore functional and subsequent convergence/minimization questions are established prior literature. The exact 20 sampled meshes may be an unreported finite table, but no broad extremal theorem, convergence result, or mesh-independent classification survives as a novel claim.

## Scientific value
FAIL. The headline extremum is only the minimum of a hand-selected 20-mesh grid. It is not an extremum over all triangulations or even a systematic resolution/aspect class, and the supporting refinement values themselves show strong discretization dependence. Prior literature also documents that minimizing PL/discrete Willmore energies can fail to converge to the smooth variational problem, so a coarse selected-grid minimum has weak transferable significance.

## Literature checked
- A. I. Bobenko, A conformal energy for simplicial surfaces: https://arxiv.org/abs/math/0406128
- X. Chen et al., The Willmore flow of triangulated surfaces: https://arxiv.org/abs/1901.09990

The decisive disposition does not rely on an inaccessible source; the cited open/DOI literature was sufficient to assess the relevant coverage and value.

## Bounded repair assessment
Narrowing the statement to 'minimum among these 20 explicitly listed meshes' makes the finite claim accurate but is already the effective limitation of RESULT.md. It does not repair the value deficit; a substantive repair would need a systematic theorem, convergence result, or reusable extremal principle.

## Final disposition
The record fails the independent three-axis gate because at least one of originality/scientific value does not pass after established results and the record's finite scope are accounted for. The complete package should be preserved and archived as a failed attempt rather than represented as a validated finding. This does not erase reproducible finite computations.

## Reproducibility / provenance
Inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`; current checked head `dcdc9e9b990eef6d712e3a1e18d83b7f50e21bfb`; source tree `1de203618e80d999bdc5c2c2384166f9cd9232e0`. Existing historical AUDIT/REVIEW evidence is preserved. Lean verification and expert attestation are not changed by this audit.
