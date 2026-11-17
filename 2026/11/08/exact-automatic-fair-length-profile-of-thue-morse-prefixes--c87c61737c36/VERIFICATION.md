---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For t_i equal to the parity of the binary digit sum and P_n=t_0...t_{n-1}, fairness is exactly D=number(01 scattered)-number(10 scattered)=0. Reconstruct D(uv)=D(u)+D(v)+(h(u)|v|-|u|h(v))/2, h=#0-#1. Both four-letter substitution blocks 0110,1001 have h=D=0; the four residue classes give (h,D)=(0,0),(epsilon,-2k epsilon),(0,epsilon),(-epsilon,2(k+1)epsilon). The equation 2D(P_n)=n h(P_j)-j h(P_n) for fair cuts forces exactly all claimed minimal 1/2/3-piece lengths and unique 2-piece cut positions; n=1,2,3 checked separately. t_k frequency one half yields densities 1/4,3/8,3/8, and nonperiodicity follows by decimation from Thue–Morse. Independently computed the actual fair-D DP and unique pair cuts for all n<=80, but the argument—not the finite test—covers all n>=1.

## originality

PASS

Best-of-knowledge original exact infinite prefix profile and forced split uniqueness. Richomme Proposition 6.2 establishes that every Thue–Morse FACTOR has fair length <=4, and an example sharp at 4, but not the exact minimum for each prefix, its automatic residue-4 refinement or unique cuts. Four-letter block fairness is prior. The classical substitutions alone do not imply these optimal-cut divisibility statements without additional proof.

## value

PASS

Fair length is a recently studied scattered-subsequence factorization invariant; exact infinite classification of the distinguished prefix origin explains why the global factor bound four is never reached at that origin, gives forced optimal cuts and a nonperiodic automatic profile with exact densities. This structural contrast is useful beyond merely tabulating finitely many prefixes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
