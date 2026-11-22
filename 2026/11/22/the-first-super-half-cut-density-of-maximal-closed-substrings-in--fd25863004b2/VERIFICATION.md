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

# Reproduction and scope

This package supplies a self-contained finite exhaustive certificate for the exact first-super-half cut-density theorem. For each length \(2\le n\le14\), both programs enumerate all \(2^n\) binary words and all \(n-1\) internal cuts. A candidate interval crosses the cut only if it is closed and neither available one-character extension is closed. A nonempty proper border is a witness of closedness only when it occurs at exactly two starting positions, even if the occurrences overlap.

Run, from the extracted directory:

```
python3 verify_direct.py
c++ -O2 -std=c++17 verify_bits.cpp -o verify_bits
./verify_bits
```

The Python and C++ standard libraries suffice. The programs' full output should exactly match `direct_output.txt` and `bits_output.txt`; each terminates with `DIRECT_PASS` or `BITS_PASS` after its assertions. The Python implementation uses substring comparisons; the C++ implementation uses bit-level masks and precomputed closedness tables. Both independently produce the maximum crossing sequence and the four length-fourteen extremal word–cut pairs.

One witness is `00101110100011`, with its cut after position eight and the eight MCS intervals listed in `RESULT.md`. Reversal and complementation generate all other optimal pairs. The exact loops, not the saved output logs, establish finite completeness.

**Unproved limits:** no theorem is claimed for maximum cut density beyond length fourteen; there is no assertion of an asymptotic leading constant, independent validation, or prior-art absence over all publications. The source PDF arXiv:2611.11552v1, Section 7, supplies the motivating density bounds and definitions.
