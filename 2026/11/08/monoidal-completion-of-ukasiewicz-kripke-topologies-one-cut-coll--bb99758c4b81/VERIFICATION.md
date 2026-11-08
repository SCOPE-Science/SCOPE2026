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

# Reproducibility and scope

Run `python verify_monoidal_completion.py` using Python 3.9 or later, without external dependencies. It enumerates exact integer-grid fuzzy relations, tests reflexivity and Łukasiewicz transitivity, identifies every induced open fuzzy set, generates its closure under the required finite operations, and checks that the result equals the degree-one-upward family. It also exhausts grid-valued valuations to check exact necessity-operator displacement.

The successful run produced these counts (worlds, denominator, transitive frames, proper enlargements): (1,1,1,0), (2,1,4,0), (2,2,9,5), (2,3,16,12), (2,4,25,21), (3,2,281,252), and (3,3,1490,1461). Power cutoffs were checked for denominators 2 through 19. This finite computation checks the implementation and examples, not arbitrary real degrees or infinite worlds.

For the unrestricted theorem, reproduce the row identity \(r_x^{\odot n}(y)=\max\{0,1-n(1-R(x,y))\}\), take its infimum to obtain the principal degree-one upset, and reconstruct an upward fuzzy function from joins of its weighted principal upsets. For the modal displacement, use one-off-point valuations as extremizers. For the countable obstruction, verify preservation of \(\liminf f(v_n)\ge f(o)\) under joins, finite meets, and pointwise strong conjunction.

Self-review was performed; independent audit has not been performed.
