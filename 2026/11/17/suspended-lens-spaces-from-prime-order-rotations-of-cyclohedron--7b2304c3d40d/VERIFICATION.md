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

The exact symbolic proof is in `RESULT.md`, Steps 1–4. The finite verifier uses only Python's standard library and can be rerun with:

```
python3 verify_cyclohedron.py
```

The actual output is recorded in `verification_output.txt`. The script enumerates all cyclic tubes, all compatible-tube simplices for two small cycle sizes, the full prime-rotation quotient cellular boundaries for the five-vertex case, and finite-field ranks for four characteristics. It also checks the fixed and moving representation dimensions for eight arithmetic parameter pairs.

For the five-vertex dual boundary, it finds \((20,90,140,70)\) nonempty simplices in dimensions zero through three; the order-five quotient has \((4,18,28,14)\) simplices. All consecutive quotient boundary compositions are zero. The mod-five quotient Betti vector is \((1,1,1,1)\); the mod-two, mod-three and mod-seven Betti vectors are each \((1,0,0,1)\). The seven-vertex dual boundary face counts are \((42,420,1680,3150,2772,924)\).

Finite checks do **not** establish the homeomorphism or the infinite parameter range. Those require the invariant-Minkowski-sum radial homeomorphism, Fourier decomposition of the coordinate permutation module, the free weighted action and the lens-space cellular calculation; each is supplied and justified in the proof. These checks do not establish novelty or independent certification.
