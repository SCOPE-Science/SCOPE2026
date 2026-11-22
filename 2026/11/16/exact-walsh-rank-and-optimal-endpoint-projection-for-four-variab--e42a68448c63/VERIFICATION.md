---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

At frozen tree 51d0d573 reconstructed the antichain incidence embedding of all subsets of the sixteen-element Boolean lattice B4 (the ambient group is 2^16, not the four-bit truth-table input cube). There are exactly 65 distinct unordered comparable-element pairs; a 16-bit family is an antichain iff no comparable pair is jointly selected, giving 168 families. A separate exact enumeration over all 65,536 incidence vectors and 16-bit Walsh transform verified 6,611 zero multipliers, rank 58,925 and complete signed frequencies, with absolute minimum 2, maximum 168; inverse Walsh of support has total abs numerator 3,052,046, so the sharp projection constant is 1,526,023/32,768. Source checkers verify_antichain.py, verify_direct.cpp and verify_orbits.py and their certificates (signed_walsh.csv, projection_kernel.csv and orbit_census.csv) were inspected at the assigned Git tree; independent direct character sums and 48-action S4 x order reversal establish 2,104 frequency orbits, 199 zero ones. For any real/complex projection, translation averaging preserves the range, reduces norm and forces the unique Fourier support projection. This is a finite exact census, not an infinite claim.

## originality

PASS

The Dedekind number 168 and antichain/monotone-function theory are old, but the transform of the complete 168-point ensemble as a subset of the sixteen-coordinate Boolean group is distinct from the Fourier spectrum of each individual monotone Boolean function on four input bits. Earlier sources do not state the full ensemble zeros or 1,526,023/32,768 range projection constant.

## value

PASS

The complete antichain family of B4 is the canonical Dedekind ensemble at the first nontrivial manageable order for a high-dimensional incidence Walsh transform. Its signed-frequency histogram, 199 zero-orbit types, exact rank defect 6,611 and sharp endpoint projection norm furnish precise basis-invariant recovery information not provided by the ordinary antichain count. Those exact natural invariants can serve as a finite benchmark for incidence-code, order-ideal and monotone-function ensemble harmonic studies. The result is narrower than an all-n theorem but materially richer than a routine small count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
