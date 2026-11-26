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

Reassessed the complete replacement RESULT.md in repairs/4. It retains the constant-free signature, the exact Ma–Yue tables and arbitrary positive finite rank for rigidity. The frozen assertions were mathematically supported; the repair is to the novelty scope. Setting one variable to 2 and all others to 3 detects exactly whether that variable occurs, since word values are 2 and 3 and addition absorbs 3 into 2. Hence content is a nonempty union invariant under both operations. A generating r-tuple must supply every singleton content and has no extra entries. The tables give x^k=x² for k≥2 and x+x²=x²; x² is constant under further unary generation from itself in the sense that both x²+x² and x²·x² equal x², and differs from x at input 1. This forces projection generators, and freeness extends every permutation uniquely to an automorphism. For the counts, normalize multiplicative words by Ma–Yue's Lemma 4.1 and distinguish contents, order and terminal flag by the specified assignments. Pointwise join closure over all 5^r assignments exhausts terms by distributivity and induction on the set of processed word vectors. Independently replayed from the tables, checking the semiring laws and product closure of the word vectors and recovering content directly from values. Results: 2, 8, 30 word functions; 2, 21, 778 full closures; support profiles {1:2}, {1:4,2:17}, {1:6,2:51,3:721}. Replay: /workspace/branches/2b1795e9-93f4-4c2c-9484-97a2189922b1/independent_replay.py and full-replay.txt (rank three approximately 0.026 seconds). The frozen checker and masks were inspected, not executed as code; the new replay does not depend on their result or any sampling. The repaired text retains the witness method and has been inspected against the unchanged support files. There is no total-order formula for r≥4 or assertion of formal verification.

## originality

PASS

PASS for the replacement's exact low-rank free-spectrum/content census and all-rank generating-tuple rigidity. The frozen first Finding item is not accepted as a distinct originality claim: Ma–Yue already give the same two types of word normal forms in Lemma 4.1, and their product rule immediately separates the representatives and yields the word count by counting ordered lists. This is known coverage, not a defect in the formula. The replacement removes that item from the asserted contributions and uses the normal forms and immediate count solely as attributed input. The exact additive closure and rigidity remain distinct from the inspected claims.

## value

PASS

For the repaired scope the semiring is motivated by its least-order limit-variety property, and its three-generator free algebra is already a concrete object used in the primary subvariety proof. Its exact cardinality and support distribution clarify that object and supply a finite benchmark for future identity and subvariety computations. Independently the all-rank result determines automorphisms and rules out nonlinear replacements of a size-r generating basis in the full free algebra. Neither reason relies on presenting the preparatory word census as a new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
