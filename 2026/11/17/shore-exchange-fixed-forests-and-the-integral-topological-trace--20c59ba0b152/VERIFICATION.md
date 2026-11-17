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
# Reproducible mathematical checks
Run `python3 verify.py` with standard Python 3, without installing dependencies. The program recomputes all edge-orbit forests and the corresponding simple-complete-graph forests for \(n=2,3,4,5\), checking every subset of the \(n(n+1)/2\) orbit vertices. The expected face-count vectors, including the empty face, are respectively \((1,3,3)\), \((1,6,15,16)\), \((1,10,45,110,125)\), and \((1,15,105,435,1080,1296)\). Their signed Euler characteristics give exact top Betti numbers \((1,6,51,560)\).

Separately, for \(n=2,3,4\), the program enumerates every original forest of \(K_{n,n}\), and for each invariant oriented simplex computes its permutation sign \((-1)^{q}\), where \(q\) counts exchanged off-diagonal edge pairs. Its augmented signed Lefschetz trace is \(-1,6,-51\), respectively, and the ambient reduced top-homology ranks from the alternating face counts are \(1,20,1071\). The independent computation of the fixed complex agrees with the trace identity.

`verify_output.txt` is the recorded output from execution of the included `verify.py`. The exact computations terminate on the enumerated finite cases; they are not offered as an exhaustive argument for unbounded \(n\). The universal proof is the covering-forest equivalence plus established matroid shellability and Lefschetz theory.
