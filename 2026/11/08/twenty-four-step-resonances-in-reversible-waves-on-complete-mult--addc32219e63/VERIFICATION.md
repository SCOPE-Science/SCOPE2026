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

# Verification of the complete multipartite reversible-wave census

The theorem is proved for every labelled complete multipartite graph with at least two nonempty parts and over each characteristic-two finite field; no finite check substitutes for that proof.

Run `python verify_binary.py` using Python 3. The program uses elementary bit-matrix algebra to construct the graph adjacency and second-order reversible wave. It checks the predicted Jordan-derived adjacency ranks, all wave fixed-space dimensions through time \(24\), exact order divisibility by \(24\), nonnegative integral Möbius counts, and direct least-period enumeration of all binary states on small graphs. Expected output begins with `RANK_AND_FIXED_COUNT_OK 2891` and `STATE_ORBITS_OK 84`, and continues with eight reproducible example censuses. Actual recorded output is `binary_output.txt`.

Run `python verify_field4.py`. It independently iterates labelled two-row states using the additive representation of \(\mathbb F_4\), checking the complete fixed-space formula against primitive orbit enumeration on eleven small graphs. Its actual output in `field4_output.txt` is `GF4_DIRECT_ORBITS_OK 11`.

Critical all-parameter steps are the adjacency rank identities, the eigenvalue-one Jordan classification, and the transfer \(J_s(0)\mapsto J_{2s}(1)\), \(J_s(1)\mapsto C_{(z^2+z+1)^s}\); the proof in `RESULT.md` supplies them. The programs only test finite examples, not every graph or extension field. The verified source date is the MIT Press publication date, 22 April 1987, of the historical second-order construction; it is not a claim of publication priority for this finding.
