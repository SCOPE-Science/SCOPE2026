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

# Verification notes

Run `python verify.py` with Python 3 and no third-party packages. The checker enumerates labelled rooted binary extensions by canonical tree grafting, and independently computes the exact falling-factorial law, Markov transition and all inclusion moments over bounded integer ranges. Its recorded output is in `verification_output.txt`.

It performs 980 exact rational Markov/moment tests, 25 exhaustive small-tree comparisons (including balanced and caterpillar initial topologies), and the example \(n=4,c=2,r=2\). It should terminate with `ALL_MARKED_CHERRY_EXTENSION_CHECKS_OK`.

The proof of all-size claims is in `RESULT.md`, including reversible edge grafting, exact moment inversion, and root interlacing. Neither a finite sample nor a numerical root test is used to infer the infinite conclusion. The strong Rayleigh implication uses the established polarization theorem; no independent mathematical audit has been carried out.
