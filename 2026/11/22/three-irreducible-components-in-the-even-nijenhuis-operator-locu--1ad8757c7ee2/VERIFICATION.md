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

The full algebraic proof in `RESULT.md` gives the exact sixteen-pair torsion expansion; in particular, the \((f_2,f_2)\) pair forces \(r^2=0\), hence \(r=0\) over a field. With that reduction, splitting into \(c=0\) and \(c\ne0\) yields precisely the stated three reduced irreducible components. The proof of geometric irreducibility uses that \(bc+t^2\) remains a primitive linear polynomial in \(b\) over every extension field. This is the infinite/all-field justification.

Reproduce the arithmetic checks with `python3 verify.py` in the directory containing this document. The checker implements the original two-product algebra, performs each of the sixteen basis-pair identities, independently compares the formula-defined components, and tests determinants. Its expected console output is:

```
GF(2): 256 tuples checked; 32 Nijenhuis; 8 invertible; components [16, 16, 16]; PASS
GF(3): 6561 tuples checked; 189 Nijenhuis; 90 invertible; components [81, 81, 81]; PASS
GF(5): 78125 tuples checked; 1625 Nijenhuis; 1100 invertible; components [625, 625, 625]; PASS
FOUR_DIMENSIONAL_PERM_SUPER_NIJENHUIS_OK
```

For the third case, only the \(r=0\) slice is enumerated; this restriction is justified by the proved identity and is not claimed to be exhaustive over all even endomorphisms without that proof. These experiments do not certify general-field geometry, historical originality or external independent audit.
