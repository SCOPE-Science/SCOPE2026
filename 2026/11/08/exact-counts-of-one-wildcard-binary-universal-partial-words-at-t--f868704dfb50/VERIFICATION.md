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

# Reproducible checks and scope

Run `python3 verify.py` from this folder using only the Python standard library. Its successful final line is `VERIFY_OK`. The direct checker enumerates all words in the specified two position classes for \(n=2,3,4\) and checks exact one-time coverage of all binary windows. The exact Bareiss matrix-tree checker computes the second-position count after prefix-edge deletion for \(4\le n\le7\). The rational three-by-three Green determinant check independently recomputes \(4\le n\le12\). None of those finite checks proves an infinite claim; the proof is the finite-step de Bruijn inverse plus explicit symbolic alternating-geometric overlap evaluation in `RESULT.md`.

The proof uses the published forced-prefix lemma for binary linear universal partial words (Chen et al., arXiv:1601.06456, Lemma 4), including its normalization and final complement constraint; independent rediscovery of that lemma is not claimed. No outside certificate, publisher evaluation or independent mathematical audit has been performed.
