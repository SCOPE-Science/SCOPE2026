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

For p time steps the directed graph on ordered pairs of p-bit histories has edge (a,b)→(b,c) exactly when the next temporal bit of b agrees with the local rule in every row. An indexed ring fixed by the p-th iterate gives a based closed walk, and the time-zero row of a based walk reconstructs that walk by deterministic updating. Neither construction divides by spatial rotations, including for words with smaller spatial period. Primitivity in time follows by subtracting fixed points when p=5 is prime; exactly five temporal states are counted per such orbit. Independently reconstructed history-pair graphs had single cyclic components with (vertices,edges)=(4,5),(19,32),(49,70) for p=1,3,5. Newton identities checked all coefficients of det(I−zA_5)=A²B and det(I−zA_1)=1−z³−z⁴. Transient blocks do not contribute to traces or determinants. Logarithmic differentiation thus gives the claimed all-length generating function. The independent direct simulation exhausted all 262136 words over n=3..17 and agrees with exact trace counts, including the zeros at 3..10 and 13 and counts 11,12,14 at n=11,12,14. It verifies both seeds' constant-history (1,0) pair and the two stationary closed paths of lengths 3 and 4. Inserting these paths preserves a genuinely time-varying column, and the two seeds plus the two insertion lengths generate all n≥14 as well as 11 and 12. At temporal heights 3 and 5 the constant-history walks are in the unique cyclic component, so coprime lengths 3 and 4 give primitivity and a single leading eigenvalue in each trace; fixed points are negligible (the root of x⁴−x−1 is below 1.3). Exact recomputation gives ρ_3≥2718457310/1758827257>3/2, and ρ_5≤57236574384761/41508028722101<7/5; the frozen transfer log also encloses ρ_5 between 1.37890 and 1.37893, so it exceeds the fixed-point rate. The positive root calculated from the reciprocal of B in that interval is 1.378913380008526. The trace asymptotic therefore proves c_n∼λ_5^n/5 and the asserted population comparison, not a basin comparison. Replay: independent rule73_independent_check.py and full_check.txt under /workspace/branches/abf8112a-4119-4a12-999c-d79b18417e05/; no frozen code was executed.

## originality

PASS

Earlier work exhibits finite Rule-73 period-five behavior, and the older finite atlas calculation would recover the early presence/absence and counts on its covered window. The supported distinct claim is the exact all-length fifth-return determinant and census, constructive proof of the full support, and its exact exponential growth comparison with temporal three. Standard transfer constructions or another period's enumerator do not supply these data. This is not a historical-priority certification.

## value

PASS

Exact primitive return periods on indexed rings are natural invariants. The length-13 gap followed by guaranteed existence at every larger length is structurally explained by insertion, rather than merely read off a short table. The factorized generating function makes later counts and exact growth available without enumerating the full ring phase space, and the smaller growth rate than period three shows that the population growth is not ordered by temporal period.

The dated certificate retains the supplied scientific assessment, sources and limitations.
