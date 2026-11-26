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

The symmetric-design Gram identities give A squared, and rank(A)=2 rho. In the even-even case A is square-zero with 2 rho size-two blocks. In the odd-even case B is invertible with inverse B^T, so a change of coordinates on one shore makes A a direct sum of swaps. For odd lambda, v is odd and the constant and zero-sum summands split on both shores. On the latter, even k again gives swaps and odd k gives a square-zero operator of rank 2(rho-1). The constant summand is respectively zero or one swap. In the odd-odd case rho cannot be one: all nonzero binary rows would coincide, contrary to the column sums 0<k<v. For any cyclic adjacency block with generator z, (z,0) generates both temporal rows, since T inverse sends it to (0,z) and T+T inverse acts as A on both rows. A block killed by (A-aI)^s thus transfers to the cyclic module killed by (X^2+aX+1)^s of full dimension 2s. This verifies all three temporal transfers over any finite characteristic-two field, whether or not X^2+X+1 splits. The fixed dimensions are gcd degrees; the latter polynomial has the two primitive third roots and is square-free. Taking the available primary components gives the asserted sharp orders and exactly the listed periods, including no least period two in the odd-even case. Mobius inversion counts orbits, and a fixed state is precisely (u,u) with Au=0, giving rank recovery independently of the four formulas.

## originality

PASS

The projective-plane clock and the temporal transfer are prior, not distinct contributions of this record. The identifiable extension is the complete classification for symmetric designs with lambda>1, including even lambda; the checked partial-geometry and strongly-regular cases do not cover that extension. This is a bounded comparison, not a publication-priority certificate.

## value

PASS

The useful result is the explicit complete time census across the symmetric-design family, not reversibility or the elementary module transfer. It states exactly when a global order of six lacks any state of least period two and when design information beyond the parameters is needed. Even the plane and its complement give sharply different orders. The theorem turns a large state-space enumeration into four parity cases and one incidence invariant on a natural class of incidence graphs outside the plane case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
