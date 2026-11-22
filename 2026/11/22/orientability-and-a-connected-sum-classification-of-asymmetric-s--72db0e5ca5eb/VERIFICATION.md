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

# Verification instructions

The exact regular polytopal cells are pairs of **nonempty disjoint** simplex faces \((A,B)\) on \(p+q+3\) vertices, with \(|A|\le p+1\), \(|B|\le q+1\). Their product-cell dimension is \(|A|+|B|-2\). The signed cellular boundary is
\[
\partial([A]\times[B])=(\partial[A])\times[B]+(-1)^{|A|-1}[A]\times(\partial[B]).
\]

Use Python 3.8 or later and run:

```
python3 check_cells.py
```

No third-party packages or external files are needed. The expected console transcript is included as `check_output.txt`.

**Actual finite checks.** The program enumerates all top facets and all codimension-one incidences for the 25 choices \(1\le p,q\le5\); verifies every ridge has two cofacets; and verifies the cancellation of the explicit integral orientation coefficients along every ridge. In the case \((p,q)=(1,2)\), it independently constructs all cells, determines the cellular boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\), and checks cell numbers \((30,120,150,60)\), boundary ranks \((29,81,59)\), and Betti numbers \((1,10,10,1)\) over those two fields.

**Proof obligations not discharged by the experiment.** The integral orientation in all dimensions follows from the two possible ridge-filling signs given in `RESULT.md`. The full fundamental-group formula follows from the exact graph-of-spaces decomposition, its simply connected vertex and edge spaces, and van Kampen. The three-manifold homeomorphism relies on the published closed-PL-manifold result and the classical prime-decomposition/Poincaré theorems. Neither modular ranks nor this finite enumeration alone establish these global claims. No independent audit has been performed.
