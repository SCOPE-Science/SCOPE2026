---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python3 verify.py` from the extracted directory. The program enumerates all 46,230 permutations of sizes three through eight and checks 230 exact assertions: the expected signed adjacency counts, every specified common-triplet probability, six equal internal block-order counts, conditional signed means, and pairwise triplet overlaps for all six-, seven-, and eight-label cases. Expected final output: `PASS: 46230 exhaustively enumerated permutations; 230 exact assertions`.

The all-size result follows from the exact block-counting and mixed-factorial-moment proof in `RESULT.md`; finite checks are not treated as an infinite certificate. No specialized theorem prover, external proof certificate, stochastic simulation, or independent audit was used. The source papers provide earlier unconditional laws and rare-block enumerations; the conditional marked limit is the newly assessed statement.
