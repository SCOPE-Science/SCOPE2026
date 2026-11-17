---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For D=diag(a,b), D_prime=JDJ, M(p)=[[1-p,hp],[hp,1-p]], monodromy equals (JMD)^2. The nonnegative matrix JMD gives Perron multiplier G(p)=[hp(a+b)+sqrt(h^2p^2(a-b)^2+4ab(1-p)^2)]/2. Its second derivative equals AB/[2Q^(3/2)]>0 for A=h^2(a-b)^2 and B=4ab. Thus only endpoint maximizers, switch h=sqrt(b/a), and derivative-at-zero threshold 2sqrt(ab)/(a+b), with a unique interior minimum below the local boundary. At the rational rescue witness G(0)<1<G(1), unique root follows from strict convexity and the explicit characteristic equation. Exact symbolic and rational independent checks agree; these do not replace the analytic proof.

## originality

FAIL

FAIL: an October 18 2026 earlier theorem gives precisely the same model, closed Perron/Floquet growth multiplier and global endpoint-only optimum incl exact tie, with an additional uniform strict interior penalty. A November 2 2026 earlier theorem gives the SAME closed multiplier, strict convexity, BOTH global and local thresholds, unique interior minimum and extinction-rescue paradox. The current rescue numbers merely reparameterize a previously established mechanism.

## value

FAIL

FAIL: there is no non-implied structural theorem left after the two full earlier same-model results. Varying the rational extinction-rescue witness is a routine example, not a independently useful new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
