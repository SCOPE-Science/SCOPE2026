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

# Verification instructions and limits

Run `python3 verify.py` beside this file, using Python 3.10 or newer. The checker uses only the Python standard library. Its deterministic expected output appears in `verify_output.txt`.

The checker builds every graph and clique independently from the group-table operation. It enumerates intercalates and checks that their rainbow triangular faces occur in no other intercalate. It computes the exact signed alternating trace over all setwise fixed simplices and compares this with the closed character formula for every tested autotopism. Cyclic orders four, five and six, the Klein four-group, and a nongroup Latin square of order five are covered. For the nongroup example, the checker also computes mod-two boundary ranks and its second Betti number directly. The order-four tests validate a local combinatorial mechanism but are outside the theorem's stated order-at-least-five domain.

These finite tests cannot establish the all-order theorem or the full integral lattice presentation. The written proof relies instead on the equivariant line-cover nerve, attaching-map identification, and a primitive integral boundary retraction. An independent mathematical audit has not been performed. No external validation is implied.
