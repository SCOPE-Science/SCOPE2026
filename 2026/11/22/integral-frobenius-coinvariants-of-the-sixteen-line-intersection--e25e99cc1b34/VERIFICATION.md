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

Computing with marked Picard classes independently identifies intersection one with distance four on the odd five-bit words. The even translation subgroup acts regularly. On its character basis, indexed by coordinate subsets modulo complement, the distance-four translations give eigenvalues 5, −3 and 1 for representatives of sizes 0, 1 and 2. The character matrix is invertible over Z[1/2]; the determinant is odd, so it gives the full geometric 3- and 5-primary structure: five elementary 3 factors and one elementary 5 factor, or Smith diagonal 1^11,3^4,15. The 3-primary representation is the signed action on the five singleton characters and the 5-primary action is trivial on constants. Each signed cycle has a one-dimensional coinvariant over F3 exactly when positive, including cycles of length divisible by 3. Thus C_F is (Z/3)^p plus Z/5 with p the number of positive signed cycles. Independently, orbit matrices constructed from Picard pairings for all 1920 elements give these ranks, all eighteen class sizes, and the sets p={0,1,2} and p={1,2,3} at the equal line-orbit profiles (4^4) and (2^8), respectively. This is a conditional classification on abstract Weyl actions; no fieldwise realization is inferred. The support scripts use int.bit_count, so the claimed Python 3.9 compatibility should read 3.10 or newer; the independent exact calculation used Python 3.12.

## originality

PASS

The line geometry, the group of automorphisms, the spectrum and, consequently by elementary Fourier calculation, the unactioned Smith form do not supply a distinct novelty claim. The supported contribution is the Weyl-equivariant arithmetic adjacency quotient and its exact dependence on signed cycles, including the failure of the line-orbit spectrum to determine it. No inspected source gives the relevant modular signed cokernel or its equivalent coinvariant classification.

## value

PASS

The unsigned adjacency operator is intrinsic to the geometric intersection configuration. The arithmetic quotient measures how Frobenius acts on that finite relation module beyond the splitting spectrum of the sixteen lines. The classification produces concrete coincident orbit profiles with three distinct groups each and separates the arithmetic signed-cycle dependence from the known geometric eigenvalues. This is a natural finite invariant with explicit witnesses, not merely a new table of the sphere sizes or adjacency spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
