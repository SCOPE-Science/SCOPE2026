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

# Reproducibility and limitations

The machine-checked portion is finite complete enumeration, not random simulation or an infinite-family extrapolation. Execute `python3 verify.py --certificate` and `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify` in a directory containing the extracted files. Both programs have no data inputs; the Python program uses only the standard library, and the C++ program uses only the C++17 standard library. They independently reconstruct the two named graphs on 16 vertices, every 16-bit subset, the code-validity predicate, the minimum-size layers, every token-jump/token-slide adjacency, and all component and degree profiles. Both run breadth-first searches from **all 2,208 rook code states** in each move model, checking every eccentricity.

`states.txt` is the complete ascending hexadecimal list of all minimum code masks, preceded by S or R. `edges.txt` lists every unordered pair of adjacent masks under the four graph/move models, prefixed ST, SJ, RT, RJ. A missing ST line is expected: all 96 Shrikhande optimum codes have no slides. `verify_python_output.txt` and `verify_cpp_output.txt` are recorded execution results, not independently performed scholarly audits.

Targeted assertions from both programs: rook slide state count 2,208, edge count 14,976, connected component size 2,208, degree spectrum (12:1,344; 16:864), eccentricity six at every state. The independently known rook jump count 28,800 and diameter six are checked but not claimed new. Shrikhande comparison (96 frozen optimum codes, jump graph 16 six-cycles) is background and not a separate originality claim.

Scientific limits: the exhaustive finite proof covers only the fixed named 16-vertex host graph and specified closed-neighborhood identifying-code and single-swap rules. Independent scholarly review has not been performed; absence of an earlier equivalent unindexed exact slide census has not been proven.
