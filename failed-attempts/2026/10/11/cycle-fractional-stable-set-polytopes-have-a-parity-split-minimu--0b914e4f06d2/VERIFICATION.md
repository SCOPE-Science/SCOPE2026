---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For n≥3, Hamano–Hibi–Ohsugi Lemma 2.2 gives the exact cycle vertices: stable-set 0–1 incidence vectors for even cycles, and these plus h=(1/2)1 for odd cycles. For each stable set S of size k and uniform center s1, squared distance is ns²+k(1−2s). When n is even, the two complementary alternating stable-set vectors have distance sqrt(n) and midpoint (1/2)1; their diameter forces radius at least sqrt(n)/2, while every 0–1 vertex lies exactly that far from the midpoint. When n is odd, alpha=(n−1)/2 and the n maximum stable sets average to c=(alpha/n)1. Their common squared distance alpha−alpha²/n=(n²−1)/(4n) is a universal lower bound by the variance identity, and all smaller stable sets have squared distance (alpha²+k)/n strictly less. The extra h lies at squared distance 1/(4n), strictly below the squared radius. The barycentric variance identity gives uniqueness over all R^n centers, not just symmetric centers. All n≥3 boundaries were checked, including C3. Independent halfspace-intersection computations reproduced all vertices for 3≤n≤8; independent exact rational stable-set/radius checks were run for 3≤n≤10. These are corroborations, not infinite proofs.

## originality

FAIL

FAIL due to decisive coverage by another published mathematical record, not merely search ambiguity. The full proof of the published graph-cone stable-set circumradius theorem SCOPE-20261011-a4388ee8bd83 already establishes the minimum-ball formula for STAB(H) for every vertex-transitive graph H with an edge: c=(a/N)1 and R²=a−a²/N; the contact criterion follows from distance²=a²/N+k(1−2a/N). Specializing H=C_n and adding the known Hamano–Hibi–Ohsugi cycle vertex classification yields every assertion of the submitted FRAC(C_n) theorem, with only the elementary inequality dist²(h,c)=1/(4n)<(n²−1)/(4n) needed in odd order. This is stronger mathematical prior coverage, even though the published theorem is presented in terms of graph cones rather than a same-title fractional-cycle result. The identical current record returned by Resultary was not counted as independent priority evidence.

## value

FAIL

The fractional stable-set relaxation and its even/odd cycle integrality difference are mathematically natural, and the exact sphere/contact classification is correct and clear. However, after accounting for the established general vertex-transitive stable-set minimum-ball lemma and the existing half-integral vertex theorem, the claimed new exact invariant reduces to a one-line addition of an interior half-vector. No independent unknown non-implied invariant, motivated new boundary, or structural step remains; this is a routine specialization and recomputation rather than a separately valuable mathematical finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
