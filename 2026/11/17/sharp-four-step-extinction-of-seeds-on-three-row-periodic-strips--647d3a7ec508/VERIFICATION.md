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

# Reproducibility and scope

Execute `python3 verify_weight_cones.py` to check both exact finite local lemmas. Five initial column counts determine a two-step output at one column, yielding the complete distribution \((963,18,0,43)\) for possible outputs \((0,1,2,3)\). Six initial column counts determine adjacent outputs after two steps: none of the \(4096\) words yields \((1,1)\). A separate direct three-step check of \(16384\) seven-column words gives \((16375,0,0,9)\), confirming that all nonempty third-step columns have weight three.

Execute `g++ -O2 -std=c++17 -Wall -Wextra verify_binary.cpp -o verify_binary` followed by `./verify_binary`. This checker implements the original 8-neighbor rule directly on labelled binary cells, not via the column-weight reduction. It visits all \(512,4096,32768,262144\) states for circumferences three through six and checks their extinction times. The two exact recorded standard outputs are supplied separately.

The universal theorem is established by exhaustive **local** neighborhoods and a subsequent mathematical argument; it does not infer a general theorem from short-ring simulations. The full infinite-plane cellular automaton, vertical-open cylinders and larger vertical heights are not addressed. Independent external audit is not part of these certificates.
