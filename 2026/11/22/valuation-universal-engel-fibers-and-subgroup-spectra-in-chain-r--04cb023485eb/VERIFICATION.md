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

# Verification of right-Engel word fibers

The accompanying `verify.py` contains a dependency-free implementation of finite chain rings, including \(\mathbb Z/p^m\mathbb Z\), \(\mathbb F_p[t]/(t^m)\), and \(\mathbb F_4[t]/(t^m)\). It constructs all affine group elements and all commutators directly from multiplication and inverses, without using the theoretical formula to evaluate the word. For each specified depth it then tests every ordered pair and compares each target count with the theorem's ideal-image sum; it also checks every right-argument Engelizer order separately.

The tested sixteen cases cover residue orders \(2,3,4,5\), ideal lengths up to four, and both mixed/equal characteristic; the largest full test has 500 group elements and 250,000 ordered pairs. Reproduction: run `python3 verify.py`; expected output is exactly the supplied `verification_output.txt` ending in `VERIFY_OK`. No random sampling is used.

The proof, not these finite tests, establishes the unrestricted quantifiers. The subgroup assertion is independently justified by a crossed-homomorphism kernel. The exact stationary transition and exceptional boundary \(m=1\) were checked symbolically as well as in the finite enumeration. This verification does not represent an independent expert audit or a machine-formal proof.
