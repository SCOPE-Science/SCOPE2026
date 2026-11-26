---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the stated wiring and gauge, the pair Schur term is 2(E+c)/(E²−1), so the hub diagonal resolvent is (E²−1)/F_m. Matching left and right plane waves across the wire contact gives transmission (4−E²)/(4−E²+V²) with V this resolvent. F_m(−1,c)>0>F_m(1,c) at generic flux; the two outer roots are separated from the central root by ±1. The signs at ±2 and at infinity then give the three, threshold two/one, and uniform one-notch regimes; an edge root at equality is excluded. Square summability inside the band forces both lead tails, then the contact and hub, to vanish. The sole freedom is in the dimer ±1 eigenspaces, with one linear constraint proportional to 1±e^{iφ}, giving dimensions m−1 (the record's eigenfunction counts are multiplicities) and the stated rank drops. At c=±1 the common factor cancels and the remaining quadratic poles are outside the open band for m≥3. With E=−1+sε the leading cubic term is 2ε[m−(m−1)s] and E²−1=−2sε+O(ε²); this gives the stated reflection profile. The two transverse half-level roots have denominators m−1±1/√3, and the conversion ε=φ²/2+O(φ⁴) gives the claimed full width and ratio. These expansions hold at fixed m, not uniformly in m. The frozen verification and full-system numerical checker were inspected; the reported 345 assertions are supporting samples, not an independently replayed proof.

## originality

PASS

Pass for the exact open-system classification, particularly its full propagating-band census, endpoint threshold and asymmetric weak-flux scaling. The Schur method, Fano/BIC mechanisms, and even the corresponding closed-device spectral determinant are not distinct claims. No temporal priority is inferred from catalog dates.

## value

PASS

The natural finite magnetic side device provides an exact benchmark for how compact dark-state multiplicity and propagating reflection can coexist without tracking each other. The smallest bouquet with one notch at every generic flux and the explicit asymmetric collapse toward exact transparency are useful parameter boundaries not supplied by a generic Fano ansatz. The contribution is these quantitative distinctions, not the elementary reduction alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
