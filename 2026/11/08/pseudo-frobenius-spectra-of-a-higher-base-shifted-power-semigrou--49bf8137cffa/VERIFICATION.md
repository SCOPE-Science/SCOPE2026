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

# Verification protocol

The standalone integer program `verify_semigroup.py` implements the proposed closed pseudo-Frobenius and genus formulas and a separate residue-graph Dijkstra method for the exact Apéry set. The latter constructs every smallest reachable residue-class representative without using the weighted-coin formulas, and then enumerates pseudo-Frobenius candidates by checking whether adding each generator yields a semigroup element. Every integer equality is exact.

The tested box is \(3\le h\le12\), \(1\le m\le4\), \(1\le d\le12\), restricted to \(\gcd(m(h^3-h+1),d)=1\). It contains 300 admissible triples, and all pass. The script output is included as `verification_output.txt`. These checks are finite and do not by themselves prove the all-parameter theorem; the symbolic proof in `RESULT.md` does.

No independent human or external mathematical audit has been conducted.
