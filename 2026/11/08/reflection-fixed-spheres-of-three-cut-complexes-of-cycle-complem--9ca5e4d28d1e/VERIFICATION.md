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
# Reproduction and limits

Execute `python3 verify.py` in the same directory. No downloads or third-party packages are required. The accompanying `verification_output.txt` records the actual run. The checker reconstructs every disconnected triple directly from graph adjacency (rather than assuming which triples are arcs), constructs quotient orbit graphs, checks their linear order, minimizes the projected hyperedges, verifies the exact two-vertex suspension intersection, and computes reduced homology by independent mod-two boundary matrices for quotients up to fifteen vertices.

The signed integral homotopy statement is established by the proof's union of two contractible CW subcomplexes and induction; the finite mod-two computations are not an integral proof and do not certify the theorem for untested values. Independent validation has not been performed.
