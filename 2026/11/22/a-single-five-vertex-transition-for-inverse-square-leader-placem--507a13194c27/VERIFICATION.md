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

# Mathematical verification and scope

Use Python 3 with the SymPy version in `requirements.txt` and execute:

```sh
python3 verify.py
```

The accompanying `verification_output.txt` records the independently observed execution output. This verifier reconstructs the entire undirected Laplacian using unit hub edges and conductance \(t\) around each triangle, deletes both selected leader rows and columns, and obtains exact rational matrix inverses. For each \(m\in\{2,3,4,5,6,7\}\) and \(t\in\{1/5,1/3,1/2,3/5,1,3,5\}\), it enumerates **all** unordered two-leader pairs and checks their exact squared-inverse traces and exhaustive optimizer classification. The executed output reports 4,354 matrix/orbit assertions and eight symbolic/formula checks (4,362 total).

Separately, SymPy checks the nontrivial polynomial simplification
\[
J_2(D)-J_2(H)=\frac{(4m^2+4m-39)t^2+(8m^2-46)t+4m^2+4m-11}{4(1+2t)^2},
\]
and the positivity comparison for same-triangle leaders, as well as the exact root of \(13-14t-15t^2\). The proof in `RESULT.md` independently gives the block inverse identity, all hypotheses and orbit coverage, coefficient positivity for every \(m\ge3\), monotone root for \(m=2\), all ties and the application to damped second-order noisy consensus.

**Limits:** The seven-point finite conductance grid and bounded-vertex enumeration are not an infinite proof; the analytical derivation establishes all \(t>0\) and all integer \(m\ge2\). A specialist windmill article was accessible only through its abstract; originality therefore remains qualified by possible prior equivalent results. There has been no independent mathematical audit.
