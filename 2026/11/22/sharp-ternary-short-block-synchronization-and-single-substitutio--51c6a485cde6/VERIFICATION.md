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

# Finite verification instructions

Run `python3 verify.py` and `g++ -std=c++17 -O2 alternate.cpp -o alternate && ./alternate` in one directory containing the four accompanying TSV files. The Python checker requires only the Python standard library and reports `VERIFY_OK`; the C++ checker uses no third-party libraries and reports `ALTERNATE_OK`.

Both programs generate every ternary word at lengths two through six. They apply the self-bifix and pairwise tests specified in the finding. The first uses an exhaustive Bron–Kerbosch maximal-clique recursion and checks all listed optimal codes and symmetry orbits. The other enumerates every clique in increasing vertex order rather than relying on a maximal-clique pivot rule. Their maximum and multiplicity outputs agree.

The checked graph and optimum statistics are: at lengths \(2,3,4,5,6\), vertex counts \(6,18,48,144,414\), compatibility edges \(0,0,108,2070,24156\), maximum code sizes \(1,1,2,4,8\), and number of labeled maxima \(6,18,108,300,528\). The length-six maximal-clique size histogram is \(3:48,4:4752,5:289464,6:507546,7:56568,8:528\). No larger clique was found by the exhaustive recursions; the theoretical recursion invariants justify using this as a finite impossibility result, not a heuristic search failure.

The enumeration is finite; nothing in it settles longer blocklengths or historical novelty. Mathematical verification was performed on these supplied source files and data only. Independent mathematical audit has not been performed.
