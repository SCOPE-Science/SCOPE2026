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

# Reproducibility

Run `python checker.py` followed by `python rank_check.py` in the directory containing both scripts. Only Python 3's standard library is required. The expected deterministic output is preserved in `checks.txt`.

The first program creates the ordinary derivations from arbitrary generator endomorphisms and central shears, then tests linear witness solvability against paired inputs. It exhausts all 729 ordered pairs when the generator rank is two and the field is \(\mathbb F_3\), checks 2,500 pairs when the rank is three over \(\mathbb F_3\), 600 in rank three over \(\mathbb F_5\), and 350 in rank four over \(\mathbb F_3\). It also produces explicit pairs for which a merely local projection has no simultaneous witness.

The second program forms, by independent left-kernel elimination, linear constraints on the full matrix space of putative two-local maps. Its constraint ranks are 2, 17, 17, and 59 in the four tested cases, leaving precisely the predicted dimensions 7, 19, 19, and 41. The linear-space rank conclusion is exact for these finite-field cases because the proved family constructs the matching lower bound; the finite witness samples do not alone establish the theorem for all fields.

Proof dependencies: the alternating normal form of bivectors, the explicitly proved distinguished-vector projection lemma, derivations of the free class-two Lie algebra, and elementary linear algebra. No unverified external computational certificate or machine formalization is invoked. Independent audit has not been performed.
