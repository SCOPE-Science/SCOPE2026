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

The per-spin energy change is 2Jσ_i(x−sum of neighboring spins), so the only nonnegative positive-field sign breakpoints are 1 and 3, with no ties at zero. Below 1, stability requires the aligned edges to be a matching. Each of 12 pentagons has an odd number of aligned edges, and a matching fits at most two per pentagon, so there is precisely one per face and exchange energy −18J. Conversely equality in the face lower bound forces that matching in the cubic planar embedding. The aligned edges correspond to perfect matchings on the dual and face-parity consistency determines spins up to global reversal. For a down-spin set A of size k, the energy in units of J is 30−20x+2(x−3)k+4e(A). For k≤8 and 0<x<3 this is minimized only by independent eight-sets; for k>8 the exchange bound −18 and magnetization <4 exclude a tie. At x=1 strict flips require independence and at least two down neighbors for each up vertex, forcing 3k≥2(20−k). An independent eight-set reaches the zero-field exchange bound and thus every up vertex has at most one up neighbor; all five such sets are strict. Weak flips at x=1 instead permit each down vertex at most one down neighbor and require each up vertex at least one. For 1<x<3 the strict and weak conditions both say independent and dominating, exactly maximal independent. At 3, the weak and ground sets are the independent sets and none is strict; above 3 only all-up survives. Independent exact reproduction: python3 /workspace/evidence/dodecahedron.py uses two ten-bit rings, rotated neighbor masks, and all 1,048,576 labelled assignments. At doubled fields 0,1,2,4,6,8 the strict/weak/ground counts are 250/250/250, 250/250/5, 5/6710/5, 295/295/5, 0/5828/5828, 1/1/1; it checks identity of the plateau ground sets and the relevant magnetization distributions. The analytic energy and flip inequalities, not field sampling, extend these counts to the indicated real intervals. In particular 6710 is the inclusive weak count at x=1, and 6705 are weak but non-strict (admit a neutral flip); the frozen informal use of marginally stable refers to the inclusive weak count. Absorbing means under the stated positive-rate allowance for zero-energy flips, not collective or multispin dynamics.

## originality

PASS

The supported distinction is the labelled all-field strict/weak one-spin stability census, especially the degree-one dominating-set condition and 6710 weak states at x=1. The equilibrium benchmark and independent-set totals are credited, and the generic local flip formula or equivalence with independent domination is not a standalone originality claim.

## value

PASS

An exactly specified canonical frustrated Ising cage separates thermodynamic equilibrium from the zero-temperature single-spin landscape: the same five ground states persist while strict excited traps change from 245 to 290, and the intervening field has 6705 additional neutral-move weak states. The structural descriptions make the exact finite census interpretable and useful as a dynamics benchmark rather than a recomputation of equilibrium counts. It does not predict basins, escape barriers, or absorption times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
