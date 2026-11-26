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

For exact masses the diagonal Gram entries equal γ and the off-diagonal modulus is |Z|/(2π); the cross term is 2 Re(conj(a)b Z)/(2π). Trimming surplus mass by nonatomicity lowers the integral strictly for nonzero coefficients if positive mass was removed. For the moment problem use independent upper level sets of cos(t−φ); cosine level sets have measure zero, giving uniqueness at fixed phase. Complementation negates Z. For l≤L/2 reduce by grid symmetry to 0≤φ≤L/2. The last cell is optimized at its right endpoint; in the second cell the two endpoint caps for φ≤l/2 have lengths l/2+φ and l/2−φ because their interior boundaries have equal cosine, and the first cell then takes [0,l]. For φ≥l/2 only the left cap survives and the first interval is centered. The sine boundary terms give 2sin(L+l/2)+2(sin l−sin L)cos φ in the first branch, and 2sin(l/2)[1+2cos((L+l)/2)cos(φ−L/2)] in the second. These increase strictly toward L/2 below half occupancy and are identically 1 at half occupancy. In the flat case each phase realizes the global modulus bound with that exact phase, so the masks are distinct up to null sets; their intervals vary continuously in measure. The explicit maximizer gives attainment; its Gram matrix is positive definite because a nonzero two-mode polynomial cannot vanish on positive measure. The eigenvector in the Finding has the correct phase. A separate cosine-sorting midpoint grid reproduced 427 bounded support tests (`python3 /workspace/frozen_review_replay.py 5`); this is numerical corroboration only. The frozen checker was read, not run.

## originality

PASS

The supported distinction is the exact three-fixed-cell first-moment envelope and the full change in its maximizing masks at half occupancy, together with the equivalent sharp two-frequency lower bound. The Gram reduction, one-phase bathtub principle and total-mass concentration are established tools, not claimed original. The strongest inspected related statements change the constraints or the modes and do not give the three-cell support computation or equality set.

## value

PASS

Independent local occupancy rather than just total occupancy is a natural observation constraint. The exact worst conditioning and the nontrivial transition from three masks to a full circle of optimal masks are useful features of the smallest odd three-cell case, not just a numerical example or a qualitative rearrangement bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
