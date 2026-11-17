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

# Verification scope

The original complex is the clique complex on 49 points of \((\mathbb Z/7)^2\) with inclusive circular-Manhattan distance at most three. The provided certificate refers to the integer vertex index \(7a+b\) and records every removal in chronological order. No original face list is trusted: `VERIFY.py` rebuilds it from pairwise metric tests.

Execute `python3 VERIFY.py CERTIFICATE.json` with Python 3.9 or newer. Successful execution must give the complete face vector \((49,588,2646,5488,5733,3136,896,98)\), \(9{,}309\) verified free-face pairs, sixteen critical cells of dimensions zero, three and four with multiplicities one, one and fourteen, and fourteen integer Morse boundary coefficients all zero. It also checks that each critical cell is maximal at its removal and that no face remains. The saved output is `VERIFY_OUTPUT.txt`.

The proof uses standard discrete Morse theory to convert the acyclic matching into a CW complex. The signed recursion in `VERIFY.py` computes attaching degrees from actual matching events and integral incidence signs; reduced Betti numbers by themselves would not establish this homotopy type. All checks are finite exhaustive checks on the 49-vertex case only. This package does not constitute an independent external audit.
