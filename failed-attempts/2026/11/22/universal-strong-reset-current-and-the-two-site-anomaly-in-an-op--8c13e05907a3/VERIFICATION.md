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

Exactly the nonempty first-site-vacant states T have reset edges, and every such edge leaves T. Finite stationary tree polynomials have degree at most |T|. A degree-|T| in-tree rooted at the singleton e1 exists: choose one reset from each T, advance and remove the rightmost downstream particle from occupied-first-site states without disturbing site 1, and inject from empty. Each slow step in an occupied-first-site state strictly decreases the sum of downstream distances to removal. Roots in T lose one possible reset factor; with any other root, including empty, selecting all reset factors forces the disallowed e1 to z2 to e1 two-cycle. Normalization therefore gives pi(e1)=1+O(1/r) and other masses O(1/r). No reset enters T, and the only O(1) ordinary inflow from e1 is to z2, whose reset rate is r. Thus pi(z2)=1/r+O(1/r^2) and other T masses are O(1/r^2). The empty probability is beta/alpha times pi(z_L), contributing at order 1/r if and only if L=2. Stationary particle-count conservation gives both extraction and injection currents, including the stated coefficients and remainders. Independently `python /workspace/branches/audit_checks.py reset` solves the finite Poisson equation for the stationary extraction rate at symbolic L=2 and at L=3,4 with alpha=2,beta=3; it confirms both leading branches. The frozen diagnostic was inspected, not executed. No estimate uniform in growing L or vanishing boundary rates follows.

## originality

FAIL

The leading law is demonstrably covered at the exact same fixed-size and rate quantifiers by a distinct indexed same-day extraction-noise record, which proves the mean-current estimate from regeneration as part of a larger result. Its equations (2)–(3) and the reward-ratio formula even give the O(r^{-2}) remainder. Independently an earlier exact two-site law already implies that entire branch. This is a failure of scientific distinctness, not a conclusion that the frozen proof is wrong or that the same-day record has established calendar priority. No distinct surviving scientific claim within the frozen Finding was identified.

## value

FAIL

The exact fixed-size boundary effect is scientifically meaningful, and the tree argument is clear. But the audited claim is only the already-covered leading throughput and its automatic fixed-size remainder. No distinct order, uniform regime, or structural conclusion beyond the covered current law is claimed that could justify a surviving contribution in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
