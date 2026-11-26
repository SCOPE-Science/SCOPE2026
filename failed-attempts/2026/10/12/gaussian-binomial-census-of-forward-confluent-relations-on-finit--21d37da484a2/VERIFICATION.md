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

On the fixed labeled chain, any element in row z forces every higher row to be nonempty, and applying the axiom to the maximum of row z forces the higher maximum to be at least as large. Conversely that higher maximum is a witness for every element in row z. For r nonempty rows their positions are fixed, and a row of maximum m has 2^m choices; reversing the sequence of maxima gives a partition in an r by (n−1) rectangle counted by size at q=2. The r=0 term is the empty relation, and n=1 gives two relations. Independent bounded computation found no mismatch in the axiom-versus-characterization check across all 66,066 relations for n=1 through 4, reproduced the first four totals 2, 11, 198, 13377, and separately recovered all eight displayed values by formula evaluation.

## originality

FAIL

A separately indexed earlier record states the same forward-only characterization and the same exact fixed-r and total counts up to an order-preserving shift of labels. It also gives an asymptotic. Two extra numerical evaluations of an identical formula do not make the later claim distinct.

## value

FAIL

A first exact census of this natural modal-frame class would be useful, including for calibrating exhaustive small-chain searches. The full normal form and census are already covered, however; neither evaluating the same expression twice more nor changing the labels supplies a scientifically motivated new invariant or cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
