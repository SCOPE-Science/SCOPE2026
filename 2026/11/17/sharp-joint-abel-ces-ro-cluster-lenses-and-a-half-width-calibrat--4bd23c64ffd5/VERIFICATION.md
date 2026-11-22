---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The RESULT.md proves finite attained bounds q^(n-k)-q^n and 1-q^k+q^n from descending geometric weights plus tail mass q^n, then passes k/n→u to the exponential lens. Balanced rounding of a convex combination of the earliest/latest block controls bounds prefix discrepancy by 1; summation-by-parts and finite exponential tail control give arbitrary late approximation after any fixed prefix. Rational (lambda,u,theta) Baire intersections plus uniform parameter estimate 2|lambda-mu|/min(lambda,mu) extend the SAME G_delta simultaneously to all real lambda>0. The maximum vertical width reduces to 1/2+2(exp(-lambda/2)-1/2)^2, uniquely minimized at 2log2. Conditions n>lambda and endpoints u=0,1 checked. Independent fresh rational prefix tests covered 504 combinations n=2..7,p=1/4,1/2; full bounded code also inspected (check_abel_lens.py); these do not prove Baire universality.

## originality

PASS

A near-identical Baire template is known for first/second Cesaro averaging, and general bounded-alphabet generic approximation is classical. However the Abel observable includes a geometric tail beyond n and its conditional extrema are exponential rather than the harmonic/entropy Cesaro lens. Neither the inspected prior statements implies the precise all-lambda geometric-tail compatibility nor unique lambda=2log2 calibration. Best-of-knowledge priority, qualified for older Abel/Cesaro Tauberian terminology.

## value

PASS

The simultaneous two-observable cluster set under finite-prefix information is a natural exact summability invariant. Its sharp conditional 1/2 ambiguity quantifies a concrete obstruction to recovering an exponential forecast from a prefix mean, and an optimal calibration scale. The infinity-level genericity is substantive beyond the easy rearrangement lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
