---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof dependencies

Run `python3 verify_commuting.py` with a standard Python 3 interpreter. The script is self-contained and uses exact integer arithmetic, with no downloaded files or third-party packages. It rederives the count by (1) summing the bivariate rank polynomial over integer partitions and (2) evaluating an independent weighted exponential-formula recurrence. It checks degrees one through eight and verifies the rank symmetry. In the standard-form family, it directly evaluates every ordered parameter pair on representatives of odd/even permutations and nonpermutations for degrees one through four, and 12,500 pseudo-random ordered pairs at degree five; the finite random sample uses a fixed seed solely for reproducibility.

Expected degree-five joint-rank matrix: `[[196,2160,1140],[2160,67755,56595],[1140,56595,53925]]`. Expected total ordered-commuting counts for degrees five through eight: `241666, 15801247, 1248611442, 118745065537`. Expected final output marker: `COMMUTING_SINGULAR_ENDOMORPHISM_CENSUS_CHECKS_PASSED`.

These checks do not inspect the exceptional nonstandard maps at degree four; no complete assertion for that degree is made. The general proof depends on the published Schein--Teclezghi classification and Gould--Grau--Johnson composition table plus elementary finite counting and the exponential formula. The finite tests do not independently establish historical originality or prove the all-degree claim.
