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

# Direct verification of minimal total domination

The standalone `verify.py` constructs the direct product using the adjacency rule that both cell coordinates differ. It checks total domination of every candidate subset by intersecting it with every vertex's open neighborhood. A successful candidate is inclusion-minimal precisely when deleting any selected vertex destroys total domination, since total domination is monotone under supersets. The program separately generates the three structural families and checks exact equality of families and coefficients.

Executed with Python 3:

```
case 2x2: candidate_subsets=15 minimal={4: 1}
case 2x3: candidate_subsets=63 minimal={4: 9}
case 2x4: candidate_subsets=255 minimal={4: 36}
case 2x5: candidate_subsets=1023 minimal={4: 100}
case 3x3: candidate_subsets=511 minimal={4: 45, 3: 6}
case 3x4: candidate_subsets=4095 minimal={4: 144, 3: 24}
case 3x5: candidate_subsets=32767 minimal={4: 360, 3: 60}
case 4x4: candidate_subsets=65535 minimal={3: 96, 4: 396}
case 4x5: candidate_subsets=1048575 minimal={4: 900, 3: 240}
VERIFY_OK instances=9 examined_subsets=1152839 minimal_sets=2417 exact_families=PASS all_coefficients=PASS
```

The program and log validate only the nine finite instances. The general theorem requires, and is supported by, the symbolic matching–cover proof given in RESULT.md. No independent mathematical audit was performed.
