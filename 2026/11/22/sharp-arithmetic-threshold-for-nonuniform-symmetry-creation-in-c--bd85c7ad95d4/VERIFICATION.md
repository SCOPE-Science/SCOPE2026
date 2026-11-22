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

# Reproducible finite checks

Run `python3 checker.py` under Python 3.8+; it uses only standard-library integer arithmetic.

The checker directly constructs the two \(4\times4\) integer transition matrices from the majority truth table and performs a complete enumeration of all \(52\) nonconstant binary target words of lengths \(2,3,4,5\). For each word it verifies (i) no diagonal entry of the period transfer exceeds one and (ii) no distinct pair of input-pair states is mutually reachable. The exact four-row results are (length, blocks, blocks with diagonal loop, maximum trace, exceptions):

```
2; 2; 2; 1; 0
3; 6; 0; 0; 0
4; 14; 6; 1; 0
5; 30; 20; 1; 0
```

The checker also verifies the explicit output and the two primitive periods for each pair \(6\le d\le30\), \(2\le m\le6\), for \(125\) total witness pairs. Finally, it tests all ring sizes \(3\le n\le16\) by enumerating asymmetric inputs until it finds a valid witness (or exhausting them to establish nonexistence). The output should end with:

```
ALL WITNESSES PASS for 6<=d<=30, 2<=m<=6
EXHAUSTIVE n=3..16 confirms sharp arithmetic criterion
```

The finite checks alone do not prove the theorem for arbitrary large ring lengths. That conclusion follows from the universally quantified graph-walk deduction and explicit family of constructive witnesses in `RESULT.md`. The present scientific review is a self-review only; independent audit remains unperformed.
