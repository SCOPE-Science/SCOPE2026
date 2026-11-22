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

# Verification of the finite dual cut-complex claim

Run `python3 verify.py` with Python 3 from this folder. It builds the canonical Petersen graph and its line graph, all forbidden disconnected four- and five-subsets, all faces of each Alexander dual, the deterministic element-by-element matching, and the complete directed Hasse diagram. It checks distinct pairs, complete critical-cell counts, every cover relation, and global acyclicity by full topological sort, together with independent mod-two boundary reductions on the same dual faces.

A replay of `python3 verify.py` matched `verification-output.json` byte-for-byte: dual face counts 767 and 2,457; matching pairs 285 and 916; Hasse covers 2,355 and 9,690; sorted vertices 767 and 2,457; critical cell vectors \(1+196\) in dimensions zero/two and \(1+624\) in dimensions zero/three.

Run `python3 independent_crosscheck.py` to enumerate *original cut-side* faces and compute their mod-two boundary ranks: it reads the shared graph-construction function but independently enumerates cut faces and their chain complexes. Observed stdout is in `independent-output.txt`; exact counts are 31,999 and 30,309 faces and unique positive-degree reduced mod-two Betti numbers 196 in dimension ten and 624 in dimension nine.

The integral sphere-wedge theorem follows from the complete acyclic discrete-Morse matching and CW reduction, not from mod-two Betti numbers. Neither source inspection nor software execution constitutes an independent mathematical audit. No claim is made for thresholds other than four and five.
