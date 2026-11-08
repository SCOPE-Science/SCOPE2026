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
Run with the standard Python 3 interpreter in a directory containing the two attached scripts:

```sh
python3 verify_k2_6.py
python3 character_k2_6.py
```

`check.txt` records their exact output. The first script builds all \(1417\) augmented faces of \(X(\overleftrightarrow K_{2,6})\), uses the strict arc-order matching, checks \(624\) face pairs, verifies the acyclicity of all \(4608\) oriented Hasse incidences, checks the expected matching SHA-256, and finds \(169\) critical three-cells and no other unmatched cells. It independently computes boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\), which cannot by themselves prove the integral homotopy result. The second script computes signed fixed-face traces for all eleven classes of \(\mathfrak S_6\), determines Specht multiplicities using the rim-hook rule, checks orthogonality of the full character table, and verifies reconstruction of the character. Neither script uses external libraries or network data. All reported results concern this exact finite graph; no arbitrary-width or equivariant-homotopy statement is certified.
