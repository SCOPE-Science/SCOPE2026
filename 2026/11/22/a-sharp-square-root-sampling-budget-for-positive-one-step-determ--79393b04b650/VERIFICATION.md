---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Re-audited final statement and complete corrected RESULT.md in /workspace/repairs/4. The frozen summary called the endpoints smallest/largest even at s=n, contrary to its own proof; they are infimum/supremum and at s=n the actual range is (1,K). Its description of a minimal-dimension rational witness also conflated the first failure dimension 35 with the displayed sharp witness at 37. The repair distinguishes them and supplies a rational example at 35. Proof replay: v,w are orthonormal and the off-axis coefficient of Aφv is nonzero exactly under the stated nondegeneracy condition. All ordinary basis rows coincide; row 1 has leverage 1 versus 1/(n−1), so Q-DEIM and every full-rank selector must sample it. The sampled w-to-v coefficient is −d=−(n−s)/(s√(n−1)). The reduced scalar's sinusoid cos 2φ−d sin 2φ has amplitude √(1+d²); for d>0 both extremizers are nondegenerate, and for d=0 they are limits. The strict sign criterion d<2√K/(K−1) yields the stated sharp row count and its fixed-K growth, with an attained zero or negative when the strict inequality fails. At K=2,s=2 the sign test changes from (n−2)²−32(n−1)=−32 at 34 to +1 at 35; the quadratic roots exclude all n=3,…,34. For z=(−35,6,…,6) in dimension 35, ||z||²=2449 and the entry sum is 169; z has both required nonzero components, and A=I+zzᵀ/2449 gives row sums −3466/2449 and 3463/2449, hence the exact −3/4898. In dimension 37 the two row sums −3/2 and 17/12 give −1/24, exactly its lower endpoint (√(1+d²)=37/12); the full and three-row quotients are 99/74 and 4/9. This checks the repair by exact algebra, not by a new certificate. Original verify.py and its descriptions were inspected, not executed; the script checks the 37-dimensional witness and finite QR/quotient diagnostics, not the new dimension-35 example or the general proof. The scope is one retained vector, distinct unweighted rows, and the specified exact-arithmetic family only.

## originality

PASS

For the corrected finding, the supported distinct contribution is the exact uniformly sign-safe coordinate row count and its attainable directional envelope for a Q-DEIM-compatible family, not qualitative spectral pollution, the quotient formula, or the mere existence of a small rational example. The strongest general norm-distortion result is sharp on a larger class but yields a strictly looser bound on this family for 2<s<n. The two rational witnesses corroborate the family classification and are not separate priority claims.

## value

PASS

The repaired finding quantifies an actual sampling-budget limitation of a deterministic algorithm: every full-rank selection is equivalent, yet fixed-size samples can give increasingly negative Ritz values on uniformly well-conditioned SPD inputs. The exact directional law changes the sufficient scaling predicted by a distortion-only argument from linear to square-root within a natural one-outlier symmetry class. A precise within-family sharp row budget and rational failure at its first negative dimension are useful test cases, without implying any all-SPD sufficient budget or finite-precision behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
