---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The referenced general finite-graph circulation/activity theorem reduces CCA rate to max_C |T_C|/|C| with winding T_C divisible by 3; the GHM cycle form equals one third by conservation of three color-transition currents. Cactus cycles use disjoint edges, and root color plus independent edge increments constrained by sum divisible by 3 yield exactly 3^(b+1) prod A_ell(t_ell) colorings. This proves cumulative distribution 3^(b+1)prod B_ell(a), and 3x CCA/GHM rate ratio. For a length-n petal, maximal winding m=n-(n mod 3) occurs with p_n=2A_n(m)/3^(n-1) ~6 n^s/(s!3^n); next winding m-3 occurs at scale n^3 times more, giving Poisson(6c/s!) and a sharp two-rate limit on r_n~c 3^n/n^s. Independent from source code, exhaustively enumerated 243 assignments on two triangles for both update rules and reproduced rate histogram 147 at zero and 96 at maximal. Finite state verification is corroboration only.

## originality

PASS

Gravner–Lyu–Sivakoff 2018 Theorem 3 and Doba 2018 give the pointwise long-run excitation rate from cycle integrals, duly credited. Their actual text does not enumerate all labelled initial states on arbitrary cacti or derive the Poisson arithmetic saturation of exponentially many petals. Close 2026-11-08 Resultary results count time-zero primitive three-cycles, which is a different observable from the eventual rate of every initial state. Current best knowledge supports originality of the new rate-population and two-rate threshold claims.

## value

PASS

The full uniform-initial-state distribution is a natural exact statistic on all cactus geometries, not a restatement of one-trajectory rate. The dimension-residue-dependent 3^n,3^n/n,3^n/n^2 sharp thresholds and two-rate Poisson profile give a nontrivial structural effect of many loop blocks and can be reused for excitable network design and probabilistic initial-data questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
