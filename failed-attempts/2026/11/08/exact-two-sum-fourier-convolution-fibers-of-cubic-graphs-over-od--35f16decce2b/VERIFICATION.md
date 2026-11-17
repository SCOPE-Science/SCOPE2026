---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Correct over all odd prime powers p^k including singular p=3: u=x-y bijects centered pairs and 4(x^3+y^3)=s^3+3su^2; valuation h of 3s reduces all fibers to square roots modulo p^(k-h). Hensel root counts give target multiplicity classes; (u-u′)(u+u′)=0 counts additive energy; CRT handles odd composite N. Independently enumerated every target for (p,k)=(3,1),(3,2),(5,1),(5,2),(7,2), matching formula exactly. Fourth moment normalization E/q^2 verified by character orthogonality, not a sharp weighted norm.

## originality

FAIL

FAIL: An already published independent mathematical record gives the same cubic graph ordered pair-sum function r_q(s,t) for every odd modulus, the identical p-adic root conditions, support |C+C|, full additive energy and Fourier fourth moment. The displayed energy p^(2k)[1+k(1-1/p)+k(k+1)(1-1/p)^2/2] equals p^(2k)+(p-1)p^(2k-2)[kp+(p-1)k(k+1)/2]. Both cover exceptional p=3 and CRT. This is claim-level domination, not matching titles. Both published date 2026-11-08: within-day priority unresolved but submitted contribution is duplicated as of audit.

## value

FAIL

FAIL: Exact local p-adic convolution data would otherwise be a useful arithmetic classification, but the same complete invariant and all stated consequences already occur in published mathematical record; no distinct precise unknown fact remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
