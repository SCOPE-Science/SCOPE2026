---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS applies to repairs/5/RESULT.md, not the original shortcut. The frozen Finding and proof omit a≡4 (mod 7) from the cases with F=P_a(a−2). At a=11 the verified PF set is {72,111,112}, so the frozen shortcut gives 111 instead of 112. The original PF table itself is correct. Re-audit of the repair: the 1,3 minimum H increases by 1 or 3 on adding 7, which proves greedy optimality with seven-coins and the periodic λ. For a residue −m the offset m suffices and all larger congruent offsets cost more than the unit-coin bound, hence W_a(m) is the exact Apéry representative. Earlier indices cannot dominate later ones because any possible backward gain is at most 2, below the multiplicity. A later index dominates an earlier one exactly when the coin count is additive at their offset difference, which is equivalent to the existence of a first coin step staying below a and raising λ by one. The seven-step restricts the last seven positions, and the unit and three-step residue increments give precisely J_r. For the separate numerical maximum, W(m+7)−W(m)=8a−7, and any suffix to a−1 containing a positive step has positive total increment because each negative run has length at most two. Hence j_F is the length of the terminal negative run, giving offsets (1,2,0,0,1,0,0). Each non-a generator is the Apéry member of its own coin offset and has only its one-coin presentation at minimum value, so the four are minimal. Independent exact residue-graph and generator-membership checks for all 493 parameters 8≤a≤500 confirmed the PF table and corrected Frobenius offsets; replay: branches/f1a4b85c-c28d-40ff-b434-61b3481dc1cc/record5_independent_check.py and record5_independent_8_500.txt. Frozen verification artifacts were inspected, not executed. Their checker takes the maximum of the full predicted set, and never tests the false separate shortcut; the repair makes this limitation explicit. The original files are unchanged.

## originality

PASS

For the corrected finding, only the complete maximal-Apéry/PF classification uniformly in a≥8 is credited as distinct. The underlying semigroup family and the exact greedy Apéry formula already occur in a stronger theorem, and one exact PF spectrum is covered by the generalized repunit literature. The inspected statements do not give the all-parameter negative-shift classification. The corrected Frobenius shortcut is a consequence, not a separate priority claim.

## value

PASS

The negative shift is a natural boundary of the monotonic Frobenius method for the known repunit-length-three offset system. The repaired table provides the full PF set, including type and exactly which parameters are symmetric, without computing an Apéry set of growing size. The distinct information is the uniform classification of semigroup-order maximality, not another computation of known Apéry values or the isolated correction to a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
