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

# Verification details

The primary standalone script `verify.py` (Python standard library only) enumerates canonical commuting-idempotent components and their multisets at every order 1–9. It validates every transition table against the two idempotence and commutation laws, refines the complete five-flag binary atomic types with a common global color palette, and asserts the exact isomorphism and logical counts at each order. It also verifies independently computed labeled structure totals by automorphism stabilizers and tests all 362,880 relabelings of the two nine-point witnesses.

Run `python3 verify.py`; the actual stdout is provided as `verify_output.txt`, ending in `VERIFY_OK first_collision=9 unique_doubleton_at_9=1`.

The independent script `check_labeled.py` generates labeled idempotent maps directly through order six, filters all commuting pairs and confirms their exact labeled counts; through order five it also checks simultaneous-conjugacy orbits. Run `python3 check_labeled.py`; the captured stdout `brute_output.txt` ends in `BRUTE_OK`.

Key numerical results are: 2,432 isomorphism and 2,432 logical classes at order eight; 6,752 isomorphism and 6,751 logical classes at order nine; at order nine precisely one nonsingleton class of size two. These are exhaustive **finite** checks. Exhaustiveness rests on the proved component-matrix canonical normal form. The standard relational counting-refinement theorem gives the \(C^2\) connection.

The computations do not classify higher orders, independently certify mathematical truth, or certify historical priority. All input data and scripts used for the finite proof are embedded alongside these notes.
