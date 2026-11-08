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

Run `python3 verify.py` from the directory containing the embedded research files. It uses Python 3 standard-library mathematics and pseudorandom sampling, with a fixed explicit seed.

The verifier passes: (1) five independent angular-integral quadratures compared to the CDF formula; (2) 240 independent Plücker determinant and trace comparisons from Haar Gaussian frames; (3) eight direct direction-grid maximizations of the true bidisc section radius against the compressed-spectrum formula; and (4) 18,000 Haar-plane samples for the predicted \(\pi/4\) endpoint atom and five CDF values. The grid approximation tolerances are intentionally finite; none certifies an infinite geometric statement. The exact theorem follows from the written Grassmannian, polynomial and integration proofs.

The full motivating preprint HTML and two closely related published mathematical result proofs were read and compared by objects, hypotheses, and implications. Bibliographic equivalence under other terminology remains a residual risk. Independent audit has not been performed.
