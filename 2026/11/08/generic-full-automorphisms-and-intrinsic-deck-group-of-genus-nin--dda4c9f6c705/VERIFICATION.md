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

The standalone `verify.py` uses exact integer and modular arithmetic only. It lists the 20 branch roots of the specialization \(a=(2,3,4,5,6)\) in characteristic \(719\), computes every projectivity from the 6,840 triples of prescribed images of three distinct roots, and tests the full branch set. The output is `CERTIFICATE_OK` with four surviving projectivities. All PGL\(_2\)-automorphisms are found because any projectivity is determined by images of three distinct points and these images must lie in the branch set, all of whose points lie in \(\mathbb F_{719}\).

The full geometric claim additionally uses the established mathematical facts that every hyperelliptic automorphism acts on the base projective line, that smooth genus-nine characteristic-zero automorphism groups have order at most \(672\), and that good-reduction specialization has only pro-\(719\) kernel. The generic extrapolation follows from the finite unramified automorphism functor and upper semicontinuity. The finite certificate itself does not establish those geometric theorems, nor classify exceptional parameters. No independent audit has been performed.
