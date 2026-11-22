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

# Verification notes

The included `checker.py` was executed as a standalone program under exact arithmetic, not floating point. For every enumerated pair \((X,Y)\), the checker computes the full matrix \(XAY-YAX\) and increments the corresponding fixed-target counter. It independently generates the predicted count for each target using ordinary rank and the two distinguished-axis predicates. It then compares every predicted count with the observed count and checks that their sum is \(q^{2mn}\).

The tested \((m,n,q)\) triples were \((2,2,2)\), \((2,3,2)\), \((3,2,2)\), \((3,3,2)\), \((2,4,2)\), \((2,2,3)\), \((2,3,3)\), and \((2,2,4)\). The last case uses an explicit polynomial-basis realization of \(\mathbb F_4\). Totals of ordered pairs were respectively \(256\), \(4096\), \(4096\), \(262144\), \(65536\), \(6561\), \(531441\), and \(65536\). All exact comparisons passed with final marker `SANDWICH_PRESCRIBED_COMMUTATOR_FIBERS_VERIFIED`.

The infinite-family claim is established by the complete factorization argument in `RESULT.md`; the finite cases are independent consistency checks, not an exhaustive proof over all fields and dimensions. The zero-target count was already established by prior work and was included for reproducibility, not claimed as new. Independent mathematical audit has not been performed.
