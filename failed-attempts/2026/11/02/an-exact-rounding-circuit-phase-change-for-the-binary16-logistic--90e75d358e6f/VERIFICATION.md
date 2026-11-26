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

Independently exhausted all 15,361 encodings for both maps. The bounded reproduction /tmp/opencode/scope-independent-binary16.py decodes with struct, compares exact Fraction values against precomputed binary16 midpoints (including the midpoint above 1), finds the recurrent set as the image of F^16384 by pointer doubling, and reverse-BFS labels every state by cycle and entry depth. The staged overshoot is 509/1048576, below 1/2048; closure and representability of 4x were checked throughout. The independent census reproduced both hashes, every basin and period, maximum depths 83 and 109, and total depths 389795 and 712352. The five-cycle order is 11709,13625,15113,14026,15313 and the only shared recurrent codes are 0 and 14848. Each cycle gets its basin fraction under the uniform-code Cesàro limit, evenly spread over its vertices, so the overlap is (5092+2)/15361 and TV is 10267/15361. This is a finite exact-arithmetic check of the specified model, not of arbitrary compilers. The supplied checker was read, not executed.

## originality

FAIL

A distinct indexed package publishes the exact two reference graphs in its supporting certificate alongside a third (staged-expanded) graph. The reference code specifies identical successors, has both matching edge digests, and returns the ordered cycle encodings and basin sizes. The frozen comparison and exact Cesàro TV are covered or mechanically implied by those data. This compares available statements and artifacts, not the calendar order of catalog paths.

## value

FAIL

A full exact standardized-format orbit census is a useful diagnostic, but the outputs for both frozen maps are already supplied by matching graph certificates. Converting their basin weights to a Cesàro TV by a two-atom overlap calculation is not a separate substantial mathematical contribution. No other new exact invariant is proved here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
