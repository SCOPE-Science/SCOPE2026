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

After the intervention, the difference from the untreated adult cohort is exactly qA(s) exp[-μ(t-s)]; recruitment is unchanged. Thus the unique optimum is sought by maximizing A(s)H(T-s), with positive q an overall factor, and the derivative has the sign of H(T-s)-D(s), where D=A(s)/(βL_0 exp(-αs)). The explicit D in the result satisfies D'=exp[(α-μ)s][1+(α-μ)a]. In the delayed regime this is positive, including α<μ because a<H(T)<1/μ. The difference starts positive and ends negative, so the unique crossing is the strictly optimal interior time. If a≥H(T) and α≥μ, then D≥a. If α<μ, then D is a convex combination of a and 1/(μ-α)>H(T); in both cases the derivative is negative for s>0, also at threshold equality. At s=T/2 the integral term in D strictly exceeds H(s) for α>0, giving the strict half-horizon bound directly. The sign of the same crossing equation gives the stated strict a, α and T comparisons while interior. At α=0 the equation reduces to exp(2μs)=exp(μT)(1-μa); this is a formal constant-source limit, not the positive-loss cohort theorem. Solving a<H(T) gives all three horizon cases. An independent numerical evaluation of the equal-rate example gave s=0.5624831767 and a benefit ratio of 1.9155763157. VERIFICATION.md and impulse_benchmark.py were inspected; python3 impulse_benchmark.py is the optional frozen calculation path.

## originality

PASS

The finite declining cohort, sharp initial-cohort and horizon boundary, strict uniqueness and α-dependence are not covered by the inspected simulation, numerical impulse-control, or constant-source timing results. Linear dependence on a fixed fractional impulse is standard linear superposition; it is not new in isolation. Historical priority for the joint classification remains provisional.

## value

PASS

The theorem identifies when protecting a recruiting cohort actually changes the timing choice and gives a strict bound and comparative statics across the entire idealized finite-horizon problem. It is a useful exact benchmark for more complex control models; it neither recommends a field schedule nor identifies an epidemic or operational optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
