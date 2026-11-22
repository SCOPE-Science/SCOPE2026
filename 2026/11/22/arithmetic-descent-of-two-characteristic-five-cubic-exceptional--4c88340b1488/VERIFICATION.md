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

# Verification of the cubic-descent computation

With Python 3 and SymPy installed, run `python verify_exceptional_cubics.py`. The program performs all finite-field operations exactly in \(\mathbb F_5[s]/(s^2-2)\), checks 18 graph automorphisms and 27 distinct lines for each cubic surface, computes every line pair incidence, and verifies the rank-seven/unimodular Picard bases. It checks Frobenius permutations, saturation of invariant lattices, their determinants and Smith diagonal invariants, and direct base-field point counts.

Expected output includes `split ... 15 ... Pic rank 6 ... -2 ... points 51`, and `nonsplit ... 3 ... Pic rank 4 ... -8 ... points 31`, followed by `All exact finite-field, line, Frobenius, and saturated-lattice checks passed.` The proof uses standard results about smooth cubic surfaces and cohomology for the infinite sequence of extension-field point counts; running a finite enumeration is not by itself a proof of those universal assertions.

The initiating paper's \(\mathbb F_{25}\)-point-count result is independently compatible with both zeta formulas. There is no external or independent certification.
