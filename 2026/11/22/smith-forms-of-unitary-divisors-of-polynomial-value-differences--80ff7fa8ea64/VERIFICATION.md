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

The maximal prime-power unitary selectors multiply in CRT coordinates, since an integer polynomial respects each residue projection. Subtracting representative rows and then representative columns for each local value fiber is unimodular and leaves (q-1)I_s+J_s and q-s zero positions. For t=q-1 and j<s, the difference of any two rows inside a j-minor has entries in tZ, giving divisibility by t^(j-1); rows 1..j and columns 2..j+1 attain that divisor (subtract the first row, then use its remaining ones). The full determinant is t^(s-1)(t+s), with the singleton block equal to q. Tensoring the integral transformations yields a diagonal over Z with the stated products. The minimum valuation of any product of j diagonal entries is the sum of the j smallest valuations, establishing primewise sorting and the torsion-order formula. At N=q rank recovers s, proving the converse; the empty CRT case is (1). Distinct nonzero square values separate by even valuation, and the unit group has half its elements squares for odd primes and the stated counts for powers of 2. Independent exact Smith reductions of directly constructed full matrices verified all displayed examples, plus mixed-prime nonsquarefree and constant cases: python3 /workspace/reproductions/four_direct_smith.py. Evidence discrepancy: CHECKER.py:144–147 explicitly checks N=15 and N=9, not the claimed N=4 example (VERIFICATION.md:21); the new replay verifies both N=4 matrices. The frozen checker was inspected, not executed, and the finite checks are not the all-modulus proof.

## originality

PASS

The supported distinction is the full unitary polynomial-value classification, including arbitrary fibers at prime powers, recombination of integral invariants, and the converse in terms of value-image cardinalities. The rank-one local matrix formula, standard Smith and CRT facts, and the squarefree ordinary gcd-difference boundary are not credited as new. No inspected evidence establishes broader coverage of the full classification.

## value

PASS

This is a natural complete arithmetic classification, not a small matrix exercise: it replaces an integral lattice calculation of size N by prime-power image cardinalities, characterizes when all Smith forms agree, and determines torsion even away from primes dividing N. The noted standard local matrix calculation is not on its own the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
