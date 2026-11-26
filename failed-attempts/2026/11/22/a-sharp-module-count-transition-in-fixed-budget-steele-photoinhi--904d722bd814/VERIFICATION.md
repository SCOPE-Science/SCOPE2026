---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the forced-sum mathematical model the classification is correct. Given an occupied coordinate, moving a little load from it to any zero coordinate strictly increases the value because f'(0)=1>f'(x) for x>0. At an interior unequal optimizer the common derivative allows only the two levels a in (1,2), b>2; two high coordinates have a positive tangent second variation, so exactly one is high. Stationarity gives a-1=d/(exp(d)-1) for d=b-a. The Finding defines this as u but then writes Greek nu without a separate definition; these denote the same function, unambiguously fixed by the stationarity equation in Proof §2. Its strict convexity follows from (d-2)exp(d)+d+2 having zero value and slope at zero and positive second derivative for d>0. The budget has a strictly increasing branch from 4 for n=2, and one fold for n>=3. A fixed-budget variation in the high-versus-low directions excludes the decreasing branch since the second variation has sign T_n'/u'; differentiating the stationarity identity twice gives a nonzero third derivative at the fold, excluding it too. For n>=3 the value gap is strictly negative at the fold and strictly positive at 2n, where the cubic variation in direction (n-1,-1,...,-1) excludes equality. On the upper branch before 2n the gap derivative is f'(a)-f'(S/n)>0 since both arguments are between one and two and a<S/n. Compactness, the candidate list and the strict root then give all global optima including threshold equalities. For n=2 the sole unequal branch merges continuously into equal at S=4; for n>=3 the tie has d_c>d_f>0. This also yields the stated high-load limit. Independent decimal calculations give n=3: S_f=5.7456435767327244, S_c=5.7743134717251248, d_c=1.3974995195938845, and optimum F_3 at S=7 of 0.7718350579247905.

## originality

FAIL

The complete mathematical claim is equivalent to the theorem in distinct record 7678a45b7053, including the exhaustive all-load optimizer classification, the exact transition equations and the jump. Record d6c7f813eac2 gives the same mathematical optimization with a stronger lower bound for the transition and also gives the high-load limit. This is demonstrable same-model coverage, not inferred chronological priority: the entries share a date, which does not establish order. The photosynthetic interpretation does not change the optimization or add a tested biological consequence.

## value

FAIL

The exact transition is useful within the model but the frozen finding adds no distinct scientific result to the fully equivalent allocation theorem. It translates the same normalized objective, constraint and root into a new application name. It introduces neither a photoinhibition-specific constraint or theorem nor empirical calibration/validation, and a numerical evaluation of the known branch does not supply a meaningful remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
