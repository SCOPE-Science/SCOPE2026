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

# Reproduction instructions

The main result is proved for every integer \(n\ge4\) in `RESULT.md`, including its integral homotopy statement. The two independent finite programs provide corroborating trace checks, not infinite proofs.

With Python 3 standard library: `python3 verify.py`. This generates all \(n+\binom n3\) star/triangle concepts, enumerates every support of cardinality at most four at each order from four to eight, and verifies the necessary-and-sufficient shattering criterion and face polynomial. It also computes mod-two simplicial boundary ranks of the complete two-dimensional support complex.

With a C++17 compiler: `g++ -std=c++17 -O2 verify.cpp -o verify_bin && ./verify_bin`. This independently assembles bit-mask concepts, exhaustively tests all requested supports and checks expected cardinalities. The expected final line in each program is `VERIFY_OK`. Recorded outputs are supplied in `verify_python_output.txt` and `verify_cpp_output.txt`.

The complete online dimension is justified by the positive-branch structural bound in the proof, not by an exhaustive recurrence. The integral homotopy type relies on the graph-of-spaces version of van Kampen, triangle generation of the graph cycle group, and the Hurewicz/Whitehead wedge criterion; finite boundary calculations over \(\mathbb F_2\) alone would not prove it. Arithmetic is integer exact in both programs and no random samples are used.
