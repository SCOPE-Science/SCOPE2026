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

# Reproduction of finite checks

The two independent enumeration programs use only the standard Python 3 or C++17 libraries.

Run `python3 verify.py` and `g++ -std=c++17 -O2 verify.cpp -o verify_cpp && ./verify_cpp`.

Both programs enumerate the actual parity-filtered order ideals, compute all Boolean traces of every eligible query support, and compare the complete finite face-count vector to the stated formula for every \(k\in\{1,2,3\}\), \(L\in\{2,3,4,5\}\), and \(p\in\{0,1\}\). This gives 24 exact finite cases for each implementation. The programs are independent implementations: Python uses explicit tuples and set-valued traces, while C++ uses base-\((L+1)\) integer states and sorted traces.

Python also constructs all simplicial boundary maps over the binary field and performs a direct sparse column-rank computation for the 18 cases with \(k\in\{1,2,3\}\), \(L\in\{2,3,4\}\), \(p\in\{0,1\}\); these agree with the integral-homology rank prediction. The standard reduced-homology convention is used for the empty-vertex complex at \(k=1,L=2,p=1\). The finite checks are not substitutes for the arbitrary-parameter proof or a check of integral torsion; the join-cycle and long-exact-sequence arguments in `RESULT.md` establish those statements.

The file `verification_output.txt` contains the successful captured output of both programs. No outside datasets, solver, network, or unavailable dependencies are required.
