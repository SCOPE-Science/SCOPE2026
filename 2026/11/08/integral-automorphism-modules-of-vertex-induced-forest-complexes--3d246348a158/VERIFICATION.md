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

# Verification

The mathematical argument uses an arbitrary finite complete multipartite graph. The exact pairwise relative-chain splitting, two contractible-cover Mayer–Vietoris sequence, augmentation-kernel identification, and incidence boundary map jointly establish the module isomorphisms over \(\mathbb Z\) for all permitted parameters. The sign under exchanging two parts was checked separately through both cover-order and oriented-edge reversal.

The included `verify.py` computes actual signed facewise reduced Lefschetz traces and independent predicted character traces for each automorphism in eight examples. It tests 1,848 automorphisms. Its second, logically separate test enumerates simplicial boundary matrices and reduces them over \(\mathbb F_2\) in seven cases. These finite tests support the formulas and catch common orientation errors but are not substitutes for the integral infinite-family proof. The precise expected output is embedded as `verification_output.txt` and is reproducible by executing `python3 verify.py`.

Independent mathematical audit has not been conducted. No equivariant homotopy equivalence, individual characteristic-\(p\) irreducible decomposition or result outside complete multipartite graphs is asserted.
