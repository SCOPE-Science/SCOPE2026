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

The 16 length-15 linear-function codewords are affinely independent at squared separation 8. The centered Gram identity 4(I-J/16) reduces the nearest-polytope distance to a Euclidean probability-simplex projection of 16 barycentric coordinates b_a/16. KKT threshold t with sum_a(b_a-t)_+=16 determines a unique nearest point and an exact rational squared-distance formula. Independent complete integer enumeration over all 2^15=32768 cube corners reproduces exactly 13 levels, their count/support triples, 16 maximizers 49/15 (precisely complements of codewords) and 240 next-level neighbors 18/7. This is exhaustive for the explicitly finite domain, not an inference about arbitrary code sizes or continuous interior cube points.

## originality

PASS

The assigned punctured linear simplex-code regular simplex and its complete 13-shell corner/nearest-face spectrum were compared at the statement and implication level with the unpunctured affine first-order Reed–Muller cross-polytope projection theorem, dual Hamming-code polytope results and coding LP/facet literature. The Reed–Muller result covers 16 coordinates and 32 affine codewords and gives Walsh projection and bent deep holes; removing the zero coordinate and all affine complements changes the codeword polytope and does not supply the 13 discrete shells, multiplicities and nearest-face supports. No known exact table was found; this is best-of-knowledge, not a priority certificate.

## value

PASS

The [15,4,8] binary simplex is a natural 15-coordinate projective code and the Euclidean convex codeword-polytope distances quantify the discrepancy between binary words and convex decoding relaxation. The complete discrete distance spectrum and nearest-face support distribution, including a sharp outer-shell stability gap, are independently useful structured geometric data and benchmark a canonical coding polytope, beyond the easy regular-simplex formula or one covering-radius number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
