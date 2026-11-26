---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

By A³=A+I, B=A+A² over the integers and C=B+B² reduces to A² modulo two. Modulo two the irreducible cubic makes A multiplication by a generator of the seven nonzero elements of F_8. For each nonzero v, the three vectors v,Bv,Cv are independent since the field elements 1, α+α², α² are a basis. The first-coordinate row and its A-iterates exhaust the nonzero dual rows, so exactly one r gives (0,1,1). With H=A⁷, H²=I+4C and successive squaring imply H^(2^j)−I≡2^(j+1)C mod 2^(j+2) for j≥1; j=0 uses 2B. Since H acts trivially modulo two, adding 2^j to any index toggles the required bit without changing lower bits. Pairing the two halves of the index interval lifts the bijection from one modulus to the next, starting with the singleton modulo 2. Normalization and multiplication by 2^s give the remaining cases, with the zero triple immediate. The supplied finite checker was inspected, not run. An independent finite implementation independently_check.py checked all 28,672 primitive triples modulo 32 and all 32,767 nonzero triples there including normalized valuation strata; this corroborates the proof, not the infinite quantifier.

## originality

FAIL

The indexed odd-fibers result is stronger than its headline full-period surjectivity: its Proof Steps 2–3 explicitly select the same (a_j,b_j,d_j)=(0,1,1) branch among all seven triples and prove the identical step-seven bijection to even residues for every primitive seed. Small moduli and scaling do not leave an independent claim. This is equivalent coverage by a distinct indexed record, not a determination of historical priority from directory dates.

## value

PASS

As a mathematical statement independently of coverage, the uniform parity selector and exact step-seven permutation give useful projected-orbit information for a natural recurrence. They resolve zero avoidance and give much more control than a state period or aggregate mean count, uniformly across seeds and precisions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
