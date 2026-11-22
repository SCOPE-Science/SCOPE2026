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

# Reproducible verification

Run the attached Python 3 standard-library checker from the extracted artifact directory:

```sh
python3 checks/verify_tree_types.py
```

It checks the exact four-way equality/ancestor/descendant/incomparable signature of each vertex against every choice of distinct parameters in every labelled rooted tree of orders two through six (enumerated via Prüfer words), including the external bound \(3m\) and global bound \(4m\). It also generates binary and path witnesses for each \(m=1,\ldots,12\), testing their counts and the binary outdegree restriction. The expected terminal line starts with `VERIFY_OK`.

The proof for arbitrary sizes is in `RESULT.md`; the finite checks neither verify all infinite parameter values nor establish novelty. No independent audit has been performed.
