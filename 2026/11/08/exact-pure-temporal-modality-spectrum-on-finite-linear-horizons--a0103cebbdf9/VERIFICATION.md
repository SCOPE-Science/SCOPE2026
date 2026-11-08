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

The accompanying `finite_tense_check.py` computes, for each 2<=n<=12, the closure of the strict-past and strict-future Boolean relation matrices under composition and separately generates the proposed canonical normal-form relations. All eleven classifications agree with the stated formula and have cardinalities 6,20,42,72,110,156,210,272,342,420,506. For n<=6 the code additionally exhausts all Boolean valuations and shows that the meet operators of distinct relation normal forms are distinct. The general result is established by the explicit five-step proof in RESULT.md, not by the finite checks. Inputs at each time are unrestricted in a common nontrivial complete lattice; the paper's actual models with restricted local lattices can produce fewer realizable distinctions. The independent audit has not been performed.
