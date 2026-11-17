---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Constant-term identity CT(3+X+2/X)^n produces D_n and digit multiplicativity excludes 2 mod3. Sparse powers yield D_{a+2*3^r}=D_a*c_k mod3^k for sufficiently separated blocks. c_k=D_{2*3^(k-1)}=7 mod9 for k>=2 generates principal units by lifting exponent. Low-degree Legendre coefficients at odd n=3^(a-1) and even n=3^a+1 produce valuation a with both leading unit signs. These seeds, principal-unit powers, and arbitrarily spaced blocks prove all allowed residues infinitely. Independent integer recurrence computation through n=16002 observed precisely 2*3^(k-1) classes for k=1..4; finite check is corroboration only.

## originality

PASS

Deutsch–Sagan gives digit restriction modulo 3; Krattenthaler–Müller 2013 gives computational schemes and concrete Delannoy congruences mod powers, but no inspected theorem asserts the complete all-k residue image and infinite hit property. Resultary search found no stronger same-object published theorem. Literature access remains bounded.

## value

PASS

The image of a familiar central lattice-path sequence in Z_3 is a natural exact distribution invariant; identifying complete excluded 3-adic balls and realizing every allowed residue by infinite explicit indices is mathematically motivated and stronger than digit exclusion alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
