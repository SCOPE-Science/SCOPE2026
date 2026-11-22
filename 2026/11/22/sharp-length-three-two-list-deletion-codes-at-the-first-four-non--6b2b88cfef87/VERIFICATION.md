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

The verifier is `verify.py` (Python 3 standard library). Execute `python3 verify.py` in the directory holding the complete package. Its reproduced output is `verify_output.txt`.

The checker builds \(D(w)=\{w_2w_3,w_1w_3,w_1w_2\}\) as a **set** of distinct deleted-position outputs for each codeword, then counts, independently for each \(y\in X_q^2\), the number of codewords whose set contains \(y\). It checks all receiver outputs, the complete codebooks and their sizes, nonrepetition of words, symbol-range validity, the exact one/two/three-output stratification, and the complete receiver-list histograms.

The calculated capacities and incidences are \((q,|C|,E)=(4,14,30),(5,21,48),(6,30,72),(8,50,126)\). Each output is produced by one or two codewords; all thirty-six outputs at \(q=6\) are produced by exactly two. The cyclic translation symmetry and both proposed conflict triangles are directly tested.

The upper-bound proof is mathematical, not computational: with \(A\) one-output words, \(B\) two-output words, and \(C_3\) three-output words, use \(A\le q\), \(A+B\le2q\), and \(A+2B+3C_3\le2q^2\) to derive \(3(A+B+C_3)\le2q^2+3q\). This certifies global optimality of the checked codebooks without enumerating all candidate codebooks. No finite check is claimed to establish an infinite-family construction.

The two conflict triangles show that the **presented** optimal codes at \(q=5\) and \(q=8\) are not unions of two uniquely-decodable subcodes. They do not prove that all optimum codes at those alphabet sizes are similarly nondecomposable. No independent audit has been performed.
