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

# Verification notes
The accompanying `verify_split_bosons.py` implements two hard-core-particle adjacency directly from core and peripheral graph edges, rather than building the representation-theoretic blocks. It checks exact characteristic polynomial identities on five independent small integer instances and checks all numeric eigenvalues against the full factorization for all sixteen pairs \(3\le r,m\le6\). It computes the kernel of the unsigned peripheral incidence matrix, verifies those vectors lie in the actual full-Hamiltonian zero eigenspace, and checks the dimension is exhaustive. It also verifies the exact zero-projector diagonal on peripheral pairs and directly propagates selected localized pairs by spectral diagonalization at five times to test the protected-sector lower bound.

The program requires Python 3, SymPy and NumPy; run `python3 verify_split_bosons.py`. It prints `PASS: 16 independent matrix vs factorization cases, 5 exact charpolys, full dark eigenspaces.` on success. All checks completed on the packaged source before review acceptance. Mathematical generality rests on the proof in RESULT.md, not on bounded enumeration. No independent scientific validation, historical priority certificate, or formal proof assistant certificate is claimed.
