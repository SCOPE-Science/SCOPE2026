---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For all r,mu>0 and nonnegative starting states at theta=1/2, direct transformation z=x+y-1,d=x-y gives z’=-z(3d²+z²-1)/4 and d’=-d(d²+8u+3z²-1)/4, u=mu/r. Factorization exhausts the 3,5,9 equilibria, with off-divider saddles only for u<1/12, extra divider attracting states precisely below 1/12, and their collision at u=1/8. At u=1/12, the center manifold d²=1/3-3z²+O(z⁴) yields z’=2z³+O(z⁵), excluding convergence from either off-divider half-plane. Invariance, bounded gradient potential, finite equilibria, and sign(z) preservation yield global initial-sum basins for u>=1/12. This proves the critical equality as well as both strict regions; numerical checks alone do not.

## originality

PASS

Best-of-knowledge original under actual inspected statements; significant access or historical-priority risks are explicitly retained.

## value

PASS

The precise ecological two-patch cubic model has a mathematically nontrivial sharp transition for multistability and global basins at u=1/12, different from equilibrium merger at 1/8. A parameter-specific structural classification and nonhyperbolic boundary are independently useful, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
