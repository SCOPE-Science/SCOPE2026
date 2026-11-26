---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With vacancy i, the clockwise particle hop is i→i−1 at tilted rate pw_(i−1)e^s, and the other is i→i+1 at qw_(i+1)e^(−s), with p=(1+ε)/2, q=(1−ε)/2. Use the unweighted escape rates in the diagonal. The trace coefficient is a+b+c, since p+q=1. Principal minors do not depend on s because two-edge cycles have zero net count. Their sum is [(1−ε²)(a²+b²+c²)+2(1+ε²)(ab+bc+ca)]/4. The two directed 3-cycles are the only count-sensitive determinant terms, with weights abc p³e^(3s) and abc q³e^(−3s); the determinant vanishes at z=s=0, fixing the remaining constant. This gives the stated reversal-invariant cubic. For real s the tilted matrix is irreducible Metzler, giving a simple analytic dominant real eigenvalue and nonzero positive overlap for stationary initial data. A spectral gap near s=0 identifies its derivatives with long-time cumulant rates; the Legendre transform gives reflected rates (the finite differentiable SCGF permits the finite-state current LDP). At (a,b,c)=(1,2,4), implicit differentiation gives 24ε(ε²+3)/[7(ε²+7)], versus 12ε/7 in the one-particle sector. This asserts no finite-time equality. Independent symbolic replay /workspace/branches/7ce354f7-86bf-46f7-b877-2546f2dc20b8/replay_record3.py reproduced the full polynomial and example. The supplied script was inspected, not executed.

## originality

FAIL

The distinct earlier exact same-model record publishes not only odd mean current but the explicit even sum S of the three directed cofactors. That sum is exactly the coefficient of z of det(zI−L) and is unaffected by tilting. Its formula, the fixed trace and the elementary two 3-cycle tilt factors already fix the entire tilted cubic and directly imply the new reversal statement. The prior record need not use SCGF terminology for this coverage. The fixed-generator fluctuation theorem alone does not imply the result.

## value

FAIL

Full-law reversal is a motivated observable, but for this fixed three-state sector the only model-specific nontrivial coefficient is already explicitly known. The new presentation mechanically repackages it into the cubic and applies standard tilted-generator theory; the mean-current contrast is also already determined by the same exact prior currents. No independent nonroutine mathematical remainder in the frozen claim supports a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
