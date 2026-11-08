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

# Reproducible finite verification

Run `python3 verify.py` using Python 3.10 or newer with assertions enabled; no third-party dependencies or external source downloads are required. The verifier, which is bundled with these documents, reconstructs all faces of the open-neighborhood complex from the graph definition and does not consume precomputed homology data as input.

It independently constructs all 21 open neighborhoods, checks the exact equality of the larger unbalanced-bipartite face set with the neighborhood face set plus seven missing six-edge stars, generates the deterministic lexicographic toggle matching, verifies every one of 98,805 covering incidences and directed acyclicity, and computes the integer Morse boundary. The critical cells have counts one in dimension zero, 246 in dimension three and seven in dimension four. All entries of the integral \(246\times7\) Morse differential vanish. An independent mod-two boundary calculation reproduces the published ranks, but is not substituted for the integral proof.

`verification_output.txt` is the exact recorded output of executing `verify.py`; the final line is `ALL_CHECKS_PASS`. These exhaustive finite checks establish the critical combinatorial hypotheses in the mathematical proof. They do not, by themselves, certify publication priority, provide a uniform theorem for larger graphs, or constitute independent human mathematical validation.
