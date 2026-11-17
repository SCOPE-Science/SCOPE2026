---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS. Reconstructed transient generator Q=[[-2d,2d],[c,-(c+d)]] with d=2^gamma e. The exact survival Laplace transform (z+c+3d)/(z^2+(c+3d)z+2d^2) yields a two-exponential survival function; its hazard increases strictly from zero to the smaller decay root. This implies either strict all-horizon split advantage or one and only one positive crossing. Independently simplified the characteristic polynomial at root e and c_tail-c_mean=e exactly. Example delta=2,c=5e/2 gives E[T2]=17/(16e), despite inferior late survival. Proof handles c=0 and equality at the tail frontier.

## originality

FAIL

FAIL (decisive exact broader earlier published coverage). The published Oct18 fixed-area fragmentation theorem uses m=e,h=2^gamma e,c=c with the identical transient chain, the identical two-exponential survival function, all-deadline criterion c_tail, mean criterion c_mean, and the constant gap e, plus further crossover monotonicity and divergence. This is not just a similar title: direct parameter substitution makes the current main theorem a strict corollary. Novelty cannot survive by repackaging the same calculation.

## value

FAIL

FAIL as an independently useful contribution, because the identical fixed-area two-reserve all-deadline/mean classification and constant-width gap already appear as a stronger published theorem. The correct phase-type proof by itself is a recomputation of that table of exact results; no surviving new boundary or classification was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
