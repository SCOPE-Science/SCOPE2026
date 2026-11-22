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

The only code dependency is Python 3 standard library. From the directory containing the accompanying files, run:

```sh
python verify_rule150_hardcore.py
```

Expected final line:

```text
VERIFY_OK all indexed cyclic inputs n=1..21; kernel-pair counts and fiber spectra
```

The checker enumerates every admissible circular source configuration at each size from one through twenty-one, applies literal synchronous three-neighbor XOR, groups output fibers, independently counts nonzero difference compatibility, and verifies every announced multiplicity, total source count and image count. The enumeration is genuinely exhaustive for the listed sizes; its finite range is not an infinite proof.

The all-length proof independently establishes the kernel recurrence, the two independent options per triple under each of the three kernel differences, the exceptional triple-fiber intersection, and the edge-count identities. The source restriction is enforced around the end-to-start boundary. Sizes one and two are explicitly included in the code and the proof.

No external mathematical audit has occurred; the output probability assumes a uniform distribution over the admissible indexed input words.
