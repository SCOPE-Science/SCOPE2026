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

# Reproduction and proof checks

Run `python3 verify.py` from the extracted package directory. No third-party packages, internet, or databases are needed. The program generates endomorphisms from their generator images, explicitly builds their full action on the Lie algebra, tests \(P^2=P\) by composition on every basis vector and computes the actual linear rank. It does not use the proposed rank-count formula to select successful candidates.

The exhaustive field/dimension cases are \((n,q)=(2,2),(2,3),(3,2)\). In increasing image-rank order the confirmed histograms are \([1,12,1]\), \([1,36,1]\), and \([1,224,896,1]\), respectively. The listed image-rank indices are \(r+\binom r2\) for \(0\le r\le n\); all unlisted ranks have count zero. Independently computed exact Gaussian-binomial values agree. An exhaustive central-shear reconstruction for every admissible central component in \((n,q)=(3,2)\) also confirms the one-orbit normal form.

Additional large-\(n\) arithmetic checks compute exact coefficients and probabilities for \(q=2,3\) and \(n=3,4,5,6,8,10,20,50,100\). These verify decreasing tail mass outside the two adjacent predicted ranks. The checks terminate with the literal line `VERIFY_OK`.

The all-field, all-dimension classification rests on the explicit homomorphism/idempotency decomposition and central-shear argument. The exponential error bound follows from the cubic exponent and a bounded product correction, not from regression on the finite tables. There is no claim that exhaustive finite tests certify all dimensions or all fields. The scientific review is not an independent audit.
