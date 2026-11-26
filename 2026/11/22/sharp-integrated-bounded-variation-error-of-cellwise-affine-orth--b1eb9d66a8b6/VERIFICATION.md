---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A one-dimensional BV function is an additive constant plus the integral of unit steps against its distributional derivative. The residual kills constants and commutes with that integral by the cellwise moment formula and Fubini. Its norm is bounded by the integrated single-jump residual, and a longest-cell jump realizes the maximum. Interior nodes make zero contribution; there are no outer endpoint masses. Independently, on the unit cell let a=(1-t)(1-3t), b=6t(1-t), and g=a+bx. On 0<t<=1/2, g(t) lies strictly between 0 and 1, and g(1)>1. Since g-H_t has zero mean, the L1 error is twice its positive area. The areas before and after the jump give E(t)=[g(t)^2+(g(1)-1)^2-max(a,0)^2]/b. This yields both stated rational branches and their derivatives. The first derivative changes from positive to negative at the unique root of the cubic on (0,1/3), since that cubic is strictly increasing there and the quadratic factor is positive. On (1/3,1/2), the shifted sextic satisfies 4Q(1/2-u)=288u^6-96u^4-6u^2-1<0 for 0<u<1/6, giving E'<0. Reflection handles the other half, with zero endpoint residual. Therefore there are precisely two maximizing relative coordinates, and a jump attains the global normalized bound exactly at one of those coordinates in a longest cell.

## originality

PASS

The most similar catalogue results share the step method or the projection kernel, but not the sharp integrated L1 residual norm. The closest traditional projection literature supplies Sobolev or smooth-function estimates in other norms. The supported distinct claim is the exact BV-to-L1 residual constant and off-centre optimizer pair for this projector, not its local moment formula or the reduction to steps.

## value

PASS

For a standard local projector applied to BV data with discontinuities, the L1 residual is distinct from output variation and is sensitive to the jump's position within a cell. A sharp, attained bound independent of grading after scaling by the longest cell makes this dependence precise. In particular, midpoint jumps are not worst, and even the rational test at t=1/4 exceeds the tempting bound 1/4. This exact normalized constant is a useful endpoint error benchmark, not an arbitrarily selected instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
