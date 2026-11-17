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

Run `python3 verify.py` using Python 3.8 or newer; only the Python standard library is used. The script generates four de Bruijn subgraphs (4, 16, 64, and 256 states), verifies that their only cyclic strongly connected components are primitive, checks the 50-step positive-vector Collatz–Wielandt inequalities exactly in integers, and compares transfer traces with direct bitwise fixed-point enumeration for sixteen finite ring cases. Recorded output: `verification_output.txt`.

The integer inequalities certify exponential growth rates, not exact polynomial minimal equations, transient basin distributions, or behavior for radii beyond four. The direct finite enumerations alone are not a proof of the infinite-ring statement; the transfer-matrix bijection and Perron argument provide that proof. No independent audit has been conducted.
