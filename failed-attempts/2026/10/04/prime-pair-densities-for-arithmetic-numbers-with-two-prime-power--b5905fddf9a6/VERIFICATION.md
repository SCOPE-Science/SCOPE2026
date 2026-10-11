---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Oller-Marcén's Proposition 6 specializes to \(\ell\mid P-1\) and \(m\mid Q-1\) or \(\operatorname{ord}_m(P)=\ell\). If \(\ell\mid m-1\), the cyclic group modulo \(m\) has exactly \(\ell-1\) classes of order \(\ell\); CRT with \(P\equiv1\pmod\ell\) gives \(\ell-1\) reduced classes modulo \(\ell m\). Fixed-modulus PNT in arithmetic progressions then yields density \(1/(m-1)\) for the cross-supplying P's and the displayed pair constants. The finite checker matches the structural criterion on its bounded test set.

## originality

FAIL

The final constant is a routine density corollary of Oller-Marcén's exact two-block congruence/order criterion plus the standard prime number theorem in fixed arithmetic progressions. Under the required implication test, specializing a broader theorem and counting its finitely many residue classes is covered even if the source does not print the resulting constant.

## value

FAIL

The cross-compensation interpretation is pleasant, but after the published exact criterion the derivation is a standard count of fixed residue classes followed by PNT in arithmetic progressions. Under the common bar this is a routine corollary rather than a substantive new structural or classification result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
