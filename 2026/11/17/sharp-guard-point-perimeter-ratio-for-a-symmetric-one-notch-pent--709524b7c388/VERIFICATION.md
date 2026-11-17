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

# Verification record

The analytical proof, not sampling, establishes the theorem for every positive \(b,h\) and every \(0<t<1\). It explicitly checks the active halfplanes, both area branches and their common boundary, the perimeter identities, the strictness at finite height, the unique shape optimizer and the cubic root's uniqueness. Its derived critical factors can also be checked by elementary polynomial expansion.

The included `verify.py` uses only Python standard-library exact rational arithmetic. It intersects all five oriented inward halfplanes with a sufficiently large rational square and calculates the exact shoelace area. Testing 42 rational parameter pairs spans both halfplane combinatorial regimes and their common boundary. The finite rational inequality \(G/P>41/40\) is verified by a strict radical enclosure and exact fractional comparisons. A high-precision bisection independently brackets the algebraic optimizer and resulting constant. These are finite regression tests, not an infinite search, formal proof, or independent audit.

The exact upper bound is an unattained class supremum; it is not a general sharp polygon inequality. The earlier Sibley paper's complete text could not be inspected; priority remains subject to historical review. No independent validation has been performed.
