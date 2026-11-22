---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The crown graph has 20 off-diagonal edges, a connected 9-edge gauge tree and 11 independent chord masks; the five diagonal frequency bits are inert. Every 11-bit signing has signed derangement permanent determined by 44 permutations. Exhaustively recomputed the 2048 exact integer signed sums: histogram 338 zeros and 1710 nonzero masks. An independent 2048-point integer Walsh-Hadamard transform of the nonzero-support indicator has |H| counts {6:960,10:360,14:44,18:70,22:360,26:240,46:12,338:1,1710:1}, sum |H|=27996, yielding ||P||_1=||P||_infty=27996/2048=6999/512 with the quotient kernel supported in the annihilator. Translation-averaging any projection onto the translation-invariant convolution range does not enlarge endpoint norms and is the unique commuting range projection. Thus the canonical projector is globally optimal, not merely among convolution projectors. The two independent integer derivations in packaged checker were inspected; separate calculations successfully reproduce the histogram.

## originality

PASS

Best-of-knowledge statement-and-implication comparison: A Fourier range projection onto the NONZERO signed-permanent support differs from the projection onto the 44 derangement characters: the latter multiplier is indicator of the original 44 codewords, not 1710 gauge classes. The earlier result gives 1269/256, whereas the present kernel yields 6999/512. General translation-averaging/invariant-projection theory proves global optimality once a multiplier support is known but does not compute this particular 2048-point support transform. Signed-permanent extremal theorems and unrestricted random-sign asymptotics do not determine its full hollow-matrix Walsh census. The read prior five-derangement census exhausts the SIGNED PERMANENT magnitude histogram and rank 28,016,640, not the transform of its 1710-class nonzero indicator. All 2048 mask values and |H| histogram were separately evaluated here; no matching earlier range projection table was located.

## value

PASS

The minimum endpoint projection constant onto the nonzero *convolution multiplier* range is a natural sharp recovery/projection-stability invariant; its full transform is a distinct finite exact fact from the formerly known derangement-character projector norm. It covers an entire 2048-class space, with a simple operator-theoretic global-optimality theorem; finiteness alone is not an objection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
