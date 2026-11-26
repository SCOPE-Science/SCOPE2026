---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The anticanonical-sum triples give the 27-by-45 incidence matrix B, with line and plane degrees 5 and 3. For the line-intersection graph A, BBᵗ=5I+A and the eigenvalues of BBᵗ are 15, 6, 0 with multiplicities 1, 20, 6. The nonzero Laplacian eigenvalue product is 8·9^20·5^6·3^24; division by 72 gives the reduced determinant 3^62·5^6. In the degree-zero divisor basis the reduced Laplacian presents the critical group, and adjoining columns of G_r−I presents coinvariants. The inverse reduced Laplacian gives a perfect pairing modulo integers; its intrinsic description via degree-zero divisors and potentials shows automorphism invariance. Thus the fixed group is dual to the computed coinvariant group. Independent exact reconstruction enumerated 51,840 Weyl elements in 25 conjugacy classes, compared all 25 lines/planes cycle rows and invariant-factor decompositions with two roots, and found exactly the collisions 12/16 and 23/24. The determinant restricts possible primes to 3 and 5, and the local reductions exclude saturation at either modulus cutoff; determinant size alone would not prove the valuation bounds. Rows 6 and 8 both have line cycles 3^9 but 5-primary fixed ranks 0 and 2. The classification is of all abstract Weyl classes, not a realization theorem over each field. The reference to 135 as an elementary divisor should be read as an invariant factor, as the group table correctly uses it.

## originality

PASS

The supported distinct contribution is the full fixed-critical-group classification and the line-cycle counterexample for this invariant, not the ordinary group, the 25 Weyl classes, the conjugacy-class detection problem, or the monodromy pairing. The strongest related indexed statements were compared with the actual graph and integral action, not excluded by date or title.

## value

PASS

The abstract graph and its Frobenius action arise canonically from a classical incidence configuration. A researcher comparing integral equivariant invariants needs the group structures, not just the order, a cycle table, or ordinary Smith factors. The exhaustive natural parameter set and concrete distinction invisible in the line splitting supply a reusable exact classification and a clear limit of the simpler datum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
