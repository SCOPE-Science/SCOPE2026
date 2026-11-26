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

After choosing a basis adapted to the induced projection, lift retained generators by F(u) and discarded generators by w-F(w). The lifts give an automorphism because they are the identity on degree one and hence on the associated graded, and they conjugate F to the standard generator projection in all characteristics. The retained generators freely generate the image; D_c(r) is strictly increasing by the Hall dimensions (the degree-one part already strictly increases). For each r-plane U there are q^{r S_c(d)} choices of lifts of a basis, each generating an eligible image. A given image is counted q^{r S_c(r)} times: all lifts in that image generate it and differ by its higher-degree part. With that choice of free generators, a retraction fixes the first r and maps the other d-r arbitrarily into the image, giving q^{(d-r)D_c(r)} maps per image; this gives the stated polynomial, including zero and identity. With c and q fixed the log of the coefficient equals d^{c+1} f_c(r/d)/c + O(d^c) uniformly. The derivative first increases and then decreases, is positive at 1/2 and negative at 1; the unique maximizer gives a uniform positive gap on every nonempty excluded compact set, while the nearest lattice rank attains the leading exponent. This proves the concentration bound, the rank fraction, and the entropy limit.

## originality

PASS

No inspected distinct finding gives or directly implies the class-c Lie census together with the class-dependent concentration law. The class-two and anti-associative cases are substantive antecedents for the method and are credited; neither counts these idempotents or supplies their class-dependent entropy law.

## value

PASS

The enumeration separates embedded images from maps to a prescribed image and includes all nonlinear generator corrections and finite characteristics. It yields a class-dependent quantitative rank law for a natural random retraction, not simply an automorphism count or a by-hand extension to a particular small class. The shared class-three saddle is not claimed as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
