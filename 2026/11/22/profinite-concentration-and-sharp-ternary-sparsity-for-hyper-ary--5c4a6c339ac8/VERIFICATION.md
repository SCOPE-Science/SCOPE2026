---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The occupancy of the units place is uniquely d when the last base-b digit d is nonzero, and is 0 or b when d=0, yielding the stated recursions with h_b(−1)=0. Tracking (h_b(n),h_b(n−1)) gives the three stated digit maps, including the leading-zero initial state (1,0). For b≥3 the word 2 0^(q−1) 2 sends (x,y) to (qx,qx). This absorbing congruence state forces all counted indices to avoid that word in the disjoint length-(q+1) blocks; counting available blocks gives exactly the bound. Bracketing any cutoff by two successive powers transfers the fixed-modulus density, and residue cylinders give weak profinite convergence. Modulo three the opposite-pair classes A,B,C,D have complete live transitions A→A,C; B→B,C; C→C,D; D→A,B,C, with row weights (1,b−1), (1,1), (b−2,2), (1,1,b−2). The missing b−2 weight at B goes to zero. The accepting classes are A,C,D. Solving the continuation series first gives C=(1+z)/[1−(b−1)z−(b−2)z²−4z³]; then A=[1+(b−1)zC]/(1−z), giving the displayed numerator and denominator, including b=2 and r=0. For b≥3 the live transfer is irreducible with a self-loop; a positive left Perron vector and the strict deficit at B force λ<b. The characteristic cubic has one positive root, larger than 1 by its value at 1. Positivity of both Perron pairings yields N_b(r)∼c_b λ^r with c_b>0, and neighboring base powers give the all-cutoff sharp exponent. These deductions and the independent finite replay agree.

## originality

PASS

The parity-density special case for b≥3 is already covered by the earlier parity theorem, and Reznick's exact dyadic recurrence recovers the entire binary specialization of the ternary generating function. The supported additions are the cap-b family-wide all-modulus concentration with an explicit block bound, and the evaluated ternary generating function and sharp exponent in the higher bases; these are not implications of the inspected parity, binary, or pointwise partition results alone.

## value

PASS

The absorbing-word argument quantifies simultaneous fixed-modulus divisibility in a natural integer sequence and identifies the full profinite limit, not just isolated progressions. The exact ternary transfer measures how sparse the exceptional set is, including a nontrivial sharp exponent for each higher base rather than just a small coefficient sample or the already known binary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
