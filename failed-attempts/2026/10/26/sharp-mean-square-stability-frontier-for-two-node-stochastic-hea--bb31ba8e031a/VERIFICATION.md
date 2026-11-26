---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With t=e^(−2ah), q=e^(−2bh), and E=e^(σ²h), the even second-moment block is t[[AE,B],[BE,A]] and the difference mode has multiplier tEq. The larger even eigenvalue is the full spectral radius since A≥q, and positive initial data excite it. Strict monotonicity in E makes det(I−K)=1−tA−tE(A−tq²)=0 the unique crossing. The numerator of the logarithmic ratio exceeds the denominator by B(1−t)>0, and the ratio tends to 2 as h→∞. Thus the all-step condition includes σ²=2a; equality at the fixed-h crossing gives nondecay, not exponential stability. The continuous even generator has negative lower diagonal and loses negativity at determinant zero, giving 2a(a+2b)/(a+b); the odd eigenvalue cannot be larger. Lumped masses and stiffness give a=b=9; the two disjoint spatial hats each have squared norm (45/2)·2/45=1 and yield nodal variance 45/2. An independent basis-matrix construction and power iteration reproduced 0.903844803656 and 1.368745544567. Interpret ‘one-step amplification factor’ as the spectral amplification of the moment update, as defined by the proof, not the worst immediate ratio of expected squared norms from deterministic vectors (the latter is t(AE+B), generally larger).

## originality

FAIL

A distinct same-day Resultary record gives the exact same a=b moment block and closed eigenvalues, the continuous and discrete stability separation, and the same nodal stochastic witness. The general a,b formula is not stated there, but follows by a commuting scalar drift shift from that already known full block, not merely by analogizing its stability conclusion. This shows coverage by direct reduction; it does not establish which record came first.

## value

FAIL

The distinction between positivity, finite-time moment bounds, and long-time stability is worth knowing. The known record already demonstrates it on the same nodal problem with an exact threshold. The extra scalar damping parameter rescales the known block, while the FE example recasts the same finite system. There is no separate, nonmechanical exact fact established here after that comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
