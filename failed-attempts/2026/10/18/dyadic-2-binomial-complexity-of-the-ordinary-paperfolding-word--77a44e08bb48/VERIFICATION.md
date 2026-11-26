---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At fixed length the profile is exactly (W,S): the 01 count is S minus binom(W,2), and the other pair counts follow from W and that count. The explicit starts at length four realize all four adjacent-bit choices for either parent parity, giving the stated complete base profiles. For either lift of a start i, the alternating lane contributes L/2 ones and the stated positional offset; every start is lifted, so the recurrence is exact for all factors. At each side weight, an overlap of the two images within one child parity would require the parent sums to differ by the even number L/2, impossible by their opposite parities. The child even and odd output sums in a side layer have opposite parity and therefore the layer has 2L classes at length 2L. In the central layer the two images are step-L progressions with starting values one step apart, and their union agrees in the two child parities. This proves the theorem from k=2. An independent bounded odd-part check counted pairs directly in eight windows; for example length 32 at start 31 gives W=16, S=288 and 168 scattered 01s. The frozen verifier was inspected but not executed; the windows are illustrations, not an exhaustion of the factor set.

## originality

FAIL

A distinct inspected catalog record states the same theorem, including the three layer counts and the central progression. Its complemented one-based normalization and use of scattered 01 rather than positional sum do not change the claim. It gives a different proof, not a different invariant or result. Its later catalog date does not settle priority; this verdict concerns demonstrated overlap in the statements, not provenance.

## value

PASS

The theorem resolves how a natural refinement of abelian equivalence splits each of the three dyadic weight layers. The distinction between the two linear-size layers and the logarithmic central layer, with exact spacing there, is not recovered from the usual abelian counts or a routine statistic conversion. This is a structural result on an infinite family even though its statement is covered in the catalog.

The dated certificate retains the supplied scientific assessment, sources and limitations.
