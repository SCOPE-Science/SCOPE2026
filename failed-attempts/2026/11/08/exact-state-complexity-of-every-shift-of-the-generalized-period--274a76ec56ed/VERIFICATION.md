---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: The morphism mu_m(a)=0(a+1 mod m) gives P_m(n)=nu_2(n+1) mod m. After reading e least-significant bits, every residual is either constant or the unique nonconstant G_(ceil((c+1)/2^e), e mod m). Strictly decreasing transient shifts for e<ceil(log2(c+1)), then m cyclic phases plus m constants, give exactly ceil(log2(c+1))+2m reachable pairwise distinct states. Padding zeros and empty input are accounted for; arithmetic distinguishability by arguments n=2^H-q is valid. Independent Moore minimization and value checks for 2<=m<=10, 0<=c<=255 corroborated the infinite structural proof.

## originality

FAIL

FAIL decisive: Resultary published October 25, 2026 a theorem giving N_{b,m}(c)=min{ell:b^ell>=c+1}+2m for the valuation word nu_b(n+c+1) mod m in every base b>=2 with the same LSD-first complete DFA convention, including the same transient chain, m-cycle and m constants. Specializing b=2 gives *all* submitted formulas and automaton residuals. Generalized period-doubling morphism is the elementary valuation representation, not a separate novel result.

## value

FAIL

FAIL: The exact entire shifted 2-kernel and minimal DFAO law and matching state graph were already proved within a strictly more general base-b theorem. Rebranding as a substitution sequence and running further finite checks are not a motivated independent contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
