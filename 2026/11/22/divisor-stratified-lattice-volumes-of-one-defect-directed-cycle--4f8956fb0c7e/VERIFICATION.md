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
Run `python3 verify.py` from the directory containing these files. This standalone Python 3 program uses only the standard library and checks the vertex-matrix determinants and lattice-index maximal minors independently for 264 triples with \(3\le n\le8\), \(2\le w\le5\), \(1\le u\le11\). The signed minors' gcd is computed from the edge-difference matrix, without using the cofactor-normal argument of the proof. The checker reports 181 unimodular cases among the test triples. No sampled or finite computation is treated as an all-parameter proof; that proof is in RESULT.md. The affine-lattice normalization, positivity and dimensional hypotheses are essential. Independent mathematical audit has not been performed.
