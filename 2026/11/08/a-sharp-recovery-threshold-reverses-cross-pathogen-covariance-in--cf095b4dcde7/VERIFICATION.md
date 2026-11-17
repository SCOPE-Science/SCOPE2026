---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

At round one, the initial co-infected source survives independently for each pathogen with Bernoulli(s); all other pathogen-specific acquisitions are independent Bernoulli(p_j) fields because only one initial source makes r=2 group hazards inactive. At round two, present pathogens independently survive with probability s; absent pathogen acquisition averages U or V depending on presence of the other pathogen at round start. Enumerating four C1,C2 possibilities yields M=s²+(1-s)[(1-s)U+sV], J=s^4+2s²(1-s)V+(1-s)²U², and covariance J-M²=s(1-s)²(U-V)[2U-s(2+U-V)]. If the source has a positive-transmission neighbor then 0<U,V<1, U!=V exactly when alpha!=1; the bracket decreases across zero at unique s*=2U/(2+U-V) in (0,1). alpha=1 independence follows from identical independent pathogen-specific dynamics and deterministic initially independent configuration. An independently worked overlapping-triangle case gives U=319/512, V=25215/32768 and s*=40832/60737; checked verify.py independent exact enumerator. Scope is exactly source time 2, not global prevalence.

## originality

PASS

Best-of-knowledge PASS: Liu–Schaposnik provide the synchronous higher-order co-infection model and hazard mechanisms, but in inspected material the two-step seeded-source joint covariance factorization and sharp survival crossing were not already established. Prior mean-field reinforcement/priority publications address different aggregate settings. Full Liu–Schaposnik original article could not be inspected, so a hidden equivalent theorem remains a clear priority risk, not an automatic fail.

## value

PASS

The sign of two-pathogen covariance can be opposite to the within-host susceptibility interaction, an important identifiability boundary. A universal exact finite-hypergraph two-round threshold including activated overlapping triangles gives a sharp, motivated dynamical counterexample with practical interpretive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
