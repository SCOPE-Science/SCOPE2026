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

Run in a directory containing `oct3.py`, `oct3_sym.py`, `oct3_abrams.py` and `oct3_irreps.py` with Python 3.11 or newer (standard library only):

```
python oct3.py > oct3.log
python oct3_sym.py > oct3_sym.log
python oct3_abrams.py > oct3_abrams.log
python oct3_irreps.py > oct3_irreps.log
```

The symmetry script generates `oct3_chars.json`, and the other subsequent scripts read it. The supplied logs and generated JSON permit exact record comparison. The graph and all boundary matrices are generated internally from the antipodal-pair graph definition. No downloaded databases, prior-run certificates or unavailable libraries are required.

The weight-three reduced Świątkowski complex has chain dimensions \((364,1404,1620,540)\); integer-echelon boundary ranks are \((363,1033,540)\) and every nonzero new leading coefficient is a unit. The program checks \(\partial^2=0\). Distinct primes \(2,3,5,1009\) independently recover the Betti vector \((1,8,47,0)\), but these modular checks alone would not prove integral torsion-freeness. The exact-unit minor argument is the integral certificate.

The rational characters are tested on all \(48\) automorphisms; all chain maps commute with boundaries. The independently enumerated Abrams cubical model has dimensions \((816,2880,3192,1088)\), and all signed Lefschetz numbers agree with the Świątkowski character values. The wreath-group irreducible module decompositions have integral nonnegative multiplicities and the expected dimensions.

The computation is finite and complete for the specified graph and particle number. It proves no uniform result for all graphs; it does not determine the fundamental group or integral equivariant homotopy type. The checks have not undergone an independent mathematical audit.
