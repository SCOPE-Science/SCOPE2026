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

# Reproducibility and verification

The result is proved for all positive run lengths \(a,b\) and all moduli \(m\ge2\). The independent finite programs test the actual recurrence and the claimed reachability/minimality mechanism; they are not exhaustive over unbounded parameters.

Run `python3 checker_modular.py` to test the modular phase-period formula, all compressed-state orbits and separating-suffix signatures for 201 parameter triples, comprising 93,596 states, plus 4,236 candidate periods and 49,056 literal positional-embedding comparisons. The recorded stdout is `verification_modular.txt`.

Run `python3 checker_bitwise.py` for a separately encoded parity-case reachability calculation and output-signature tests on 54 run pairs and 13,196 states, together with 24,042 directly generated binary words. The recorded stdout is `verification_bitwise.txt`.

The key infinite-proof ingredients are the binomial-period prime-power criterion, a return-loop construction of both affine maps \(Y\mapsto(1+X)Y\) and \(Y\mapsto(1+X)Y+X\), the unitriangular basis \(X(1+X)^j\), and suffix distinguishability of the full prefix-counter vector. Finite state enumeration checks these mechanisms only in the stated ranges. No external independent mathematical audit was performed.
