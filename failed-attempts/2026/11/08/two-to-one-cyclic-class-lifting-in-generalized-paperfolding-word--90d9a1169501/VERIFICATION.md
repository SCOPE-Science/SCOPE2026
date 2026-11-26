---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In each source factor with 4|n and n≥8 exactly one relative parity track is alternating, because the other track is a factor of the next instruction tail and no such word has an alternating four-letter factor. The alternating track has even length, so it determines parity and phase modulo four and that phase moves by the rotation offset, even across the cut. The even-start lift is independent of the occurrence. Any rotation between two even-start lifts is even, since their alternating tracks have the same parity and the other tracks are nonalternating; decimation then recovers a source rotation. Odd-start factors are precisely the one-place left rotations of even-start factors, by equality of the two marker bits n steps apart, including the one-sided boundary at index zero. The lift and one-place rotate are injective with disjoint images, proving exact doubling. Independent complete residue enumeration (branches/paperfolding_independent.py) gave c(4)=3, c(8)=4 and at length 12 eight size-2 and eight size-4 classes, doubled at 24. The uploaded verifier was inspected and not run; it schedules 18 input instances but duplicates the all-zero instructions, so those are 17 distinct sequences. That does not affect the universal proof.

## originality

FAIL

The regular count/bijection is already covered in an earlier indexed finding. More importantly, the published arbitrary-paperfolding interleaving argument in the proof of Proposition 20 already performs the forward lift of each occurring conjugate with the phase chosen by parity, and obtains the odd-start mate by rotating one place. The induction on power-of-two lengths is used to know how many rotations occur, not to construct the transfer for an individual occurring rotation. Reading the nonalternating track of an even-start lift gives the immediate reverse, leaving no substantive independent transfer theorem at general admissible lengths.

## value

FAIL

A full class spectrum would be useful if it required a new structural step. Here the stronger-looking formulation isolates the existing per-conjugate lift and reads off its elementary inverse; the finite mixed-spectrum examples are checks, not a separate classification. No distinct valuable narrower result is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
