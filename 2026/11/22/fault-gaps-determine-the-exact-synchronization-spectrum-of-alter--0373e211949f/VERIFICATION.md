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
# Reproducible checks

From the directory containing the two standalone scripts, run `python3 verify_graph.py` and `python3 verify_transport.py` using the Python 3 standard library. The first implements the graph update directly, covering all \(119\) nonempty fault patterns at \(m=2,\ldots,6\) and \(294128\) initial states; also all fault-free orbit counts at those lengths. The second independently propagates Boolean source positions, checking \(4697\) random/structured fault layouts at sizes \(m=2,\ldots,60\). Both finished without assertion failures in the reported check. This finite verification is supplementary to the all-size proof in RESULT.md. The Bernoulli law is established by explicit probability inequalities and not by simulation.
