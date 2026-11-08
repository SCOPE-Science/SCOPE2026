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

Run `python verify.py` with Python 3 and the standard library. The independent routine constructs a numerical transition matrix for each of 18 clique sizes \(n=3,\ldots,20\), seven reset probabilities per clique, and solves for its stationary probabilities by iteration. The observed row entropy is compared with the symbolic formula (126 combinations), the explicit stationary law, and a separately calculated unmerged-versus-merged entropy deficit. The test also checks normalization and a strict information upper bound. No output is used as an infinite-parameter proof.

The analytic proof depends on: (i) detailed balance; (ii) an exact symbolic row-entropy identity; (iii) the positivity and derivative identity for a Kullback--Leibler divergence; (iv) a quantified localization of entropy-maximizing reset rates; and (v) a uniform Taylor bound and strongly concave comparison function. The limiting optimizer is identified through \(W(m)e^{W(m)}=m\), not by fitting an observed numerical trend.

The source date 2022-08-11 is verified as the first public arXiv version. Independent audit has not been performed. Possible unseen priority is a scientific limitation, not a computational certificate.
