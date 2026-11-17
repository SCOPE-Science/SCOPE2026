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

# Verification

Both scripts use only the Python standard library. From the artifact root, execute `python3 verification/finite_quotient.py` and then `python3 verification/direct_graph.py`. The first script regenerates the exactly 17576-row `certificates/all_signatures.csv` finite-factor proof and compares every row; its asserted 21-case histogram, exact period-four profiles, seven-step witness and stabilization conditions are checked. The second script independently updates individual vertices of 56 labelled graphs and compares their actual least-return classes with the certificate over exactly 179604 initial states. The actual successful outputs are recorded in `verification/finite_quotient_output.txt` and `verification/direct_graph_output.txt`.

The scripts and the certificate are embedded at the paths given. The first calculation is exhaustive only because the proof reduces **every** arbitrary-size graph state to one of those tagged capped-initial-color class signatures; a direct finite experiment alone would not prove the all-size result. The source code is transparent but has not been audited by an independent mathematician. The literature comparison remains subject to unindexed priority risk.
