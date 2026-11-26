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

Reconstructed rank-wise Burnside under the full action of Araújo et al., Theorem 5.5. A rotation with gcd g has invariant subsets periodic modulo g; choosing ℓ residue classes makes its shift in either subset (s/g)ℓ modulo rank, so every cyclic shift between the two subsets commutes. A reflection on an invariant rank-k subset acts in cyclic coordinates by i↦α−i, including k=1,2. A shift v from one subset to another commutes precisely if 2v≡β−α modulo k. Solvability is equivalent to equal numbers of restricted fixed points (one at odd rank; at even rank this distinguishes α even from α odd), and there are gcd(2,k) solutions. This verifies both fixed-map polynomials, including the separately counted empty map. At z=1 Vandermonde gives R=1+(n/2)binom(2g,g) and H=(2+f²+2 binom(f,2)²)binom(2m,m)−1, yielding the divisor sum with both reflection parities. Rank one and full rank classify respectively by unsigned displacement and inverse-paired rotations; rank n−1 gets (n−1)n² identity fixes and 2n total reflection fixes. Each nonidentity rotation has g≤n/2; the fixed-set union bound then proves the claimed exponential rarity and Stirling gives the total asymptotic. This is an all-n argument, not extrapolation from the supplied test vectors.

## originality

PASS

Credit the previously known full action and the labeled rank enumeration in full. The distinct result is the all-rank orbit enumerator with nonidentity stabilizer corrections and its explicit consequences. The closest actual statements inspected do not provide it. The assessment is best-knowledge, not a priority guarantee.

## value

PASS

This is the complete natural rank stratification after quotienting a standard inverse monoid by its actual full automorphism group. The parity-dependent reflection contributions, exact next-to-unit orbit law, and generic-freeness bound resolve concrete consequences of stabilizers missed by labeled counts. The calculation is elementary but supplies an all-size explicit answer with no monoid generation needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
