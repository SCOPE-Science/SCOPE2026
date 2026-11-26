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

Each predecessor of a word of length n is exactly a path of n edges labeled by that word, starting from any of the four input pairs, and its last vertex is the target pair. All such finite inputs extend bi-infinitely with the observation unchanged. Successor support is correctly computed by union over each current pair and either next input bit. Empty support is not a witness and stays empty. Shortest-path search in the closed graph of at most 15 reachable nonempty supports gives exact minima; absence of a singleton in the closure proves impossibility at all lengths. A separate set-based replay reproduced the counts (24,90,72,12,4,4,50), the four extremizers, their witnesses (100101 for 37 and 164; 010010 for 91 and 218), and all 256 rows including shortest-word multiplicities and reachable-support counts. The original --csv option writes a regenerated CSV rather than checking an already packaged file in place; the independent comparison checked the actual packaged rows. This is exact finite verification, not formal certification.

## originality

FAIL

The earlier dated Resultary record 218bfa54da8f explicitly defines exactly this right-boundary minimum and publishes both it and a witness for each of the 256 rules. The columns were compared rule by rule and match exactly. Consequently the headline sharp cutoff, extremizers, all length and witness classifications, and derived length histogram are already covered. This is a statement- and data-level match, not a conjecture from availability or a priority inference based on date alone. Two incidental statistics in the new CSV are not in those earlier columns; their presence does not make the headline finding original.

## value

FAIL

An exact endpoint-inference cutoff and all-rule census would be a useful gap if unknown, but here the cutoff, extremizers and all length/witness data come directly from the matched existing catalogue. The additional reachable-support sizes and counts of shortest words are correct catalog fields, but the frozen result does not motivate a separate precise question about either or show why either addition is mathematically useful beyond the already-known classification. The method and replay are useful verification, not a new valuable finding as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
