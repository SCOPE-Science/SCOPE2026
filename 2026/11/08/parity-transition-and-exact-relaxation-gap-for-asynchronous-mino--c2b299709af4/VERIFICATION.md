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

The all-size arguments are in `RESULT.md`; the finite programs serve as independent numerical cross-checks and are not themselves certificates for unbounded parameters.

Run `python3 check_recurrent.py` with a standard Python 3 interpreter. For \(m=2\) through \(7\), this constructs the full transition graph by examining the actual closed neighborhood of each chosen vertex, computes its strongly connected components, checks closure, and compares the closed recurrent set against independently counted maximum cuts. The six state-space sizes total \(21{,}840\) and the recorded output is `recurrent_output.txt`.

Run `python3 check_spectrum.py` with Python 3 and NumPy. For odd \(m=3,5,7\), this constructs independent Markov matrices, checks their symmetry and stochasticity, reconstructs the middle-level inclusion graph, confirms its eigenvalue multiplicities numerically, and compares the second Markov eigenvalue to the closed spectral formula. The actual results are in `spectrum_output.txt`.

The proof does not rely on floating-point eigenvalues to establish any infinite-family assertion. Source originality and historical priority are not settled by these tests.
