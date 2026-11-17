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

The monadic k-round Ehrenfeucht–Fraïssé theorem reduces logical equivalence precisely to equality of k-truncated counts of each of M=2^r unary Boolean types. Summing two independent multinomial assignments gives the exact coefficient C=(n!)^2 M^-2n [x^n y^n]F_k(x,y)^M, F_k=sum_{j<k}(xy)^j/(j!)^2+(e^x-tail_{<k})(e^y-tail_{<k}). A two-dimensional exponential tilt at a unique diagonal saddle has positive definite covariance (support includes (k,k),(k+1,k),(k,k+1)) and full Z^2 difference lattice. Fourier local CLT yields 1/(2pi M sqrt(detSigma)); Stirling gives the prefactor alpha_M/sqrt(detSigma). At k=1, alpha=log2 the saddle equals the Poissonizing parameter, detSigma=t^2(1-t^2), and first derivative of rate vanishes, controlling floor(n). Independent exact rational type-assignment/EGF comparisons passed 24 cases M=2,4, n<=3, k<=3. No numerical test is treated as the asymptotic proof.

## originality

PASS

Best-of-knowledge PASS for the sharp fixed-size two-structure collision probability, all fixed k two-dimensional LLT prefactor and rank-one log(2) contact point. Carreiro–Facchini–Venema–Zanasi (arxiv:1809.03262) already prove the k-truncated count logical criterion; this prerequisite is not original. Dupuis–Nuzman–Whiting (J. Appl. Prob. 44 (2007), pp.115–141) establish colored occupancy sample-path large deviations and rate principles, not the event-specific exact coefficient, sharp polynomial prefactor, or rank-one Poissonization contact in their full examined source. A general LDP may dominate a qualitative rate under reductions but does not alone yield this local-limit constant. Historical occupancy-collision literature retains residual risk.

## value

PASS

PASS. Bounded quantifier rank is the natural logical indistinguishability invariant; quantifying collisions of two random interpretations is a genuine all-parameter finite-model probability problem. The fixed-size-vs-Poissonized comparison detects a critical density where exponential rates touch and a nonunit prefactor; this is not implicit in a generic LDP. The exact coefficient gives finite-n probabilities, the 2D saddle gives sharp behavior for every fixed k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
