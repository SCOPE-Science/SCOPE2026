---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

From the preprint exact optimized C_*(A), substitute x=1/A and expand −log(1−x). The linear coefficient is 7/3+log3−2log2−2=1/3+log(3/4); n≥2 coefficient is (4n−7)/(3n(n−1))>0 with maximum 5/18 at n=3. Independently evaluated the original logarithmic expression against truncated series at A=3,7,32,1000 to 10^(−35) or better. Strict decrease + dense odd-rational squares and B-continuity yields lim ε A_adm(ε)=c* via lower/upper thresholds. B_min=12/(π−4 arcsin A^(−1/2))² expands to 12/π²+96/π³ A^(−1/2)+O(A^(−1)). The asymptotic proof is real, no numeric approximation substitutes for it.

## originality

FAIL

Strong implication coverage: Gariboldi–Gigante Theorem 7 and the proof of Theorem 2 already give the fully explicit optimized coefficient C_*(A), its strict decrease to L, continuous B_min(A), and density of admissible odd-rational squares. Substituting x=1/A into their explicit logarithmic formula and taking the first Taylor coefficient gives c_*=1/3+log(3/4) immediately; monotonicity and density then invert the same limit to ε A_adm(ε)→c_*. The coefficient series and B_min expansion are elementary expansions of the prior closed forms. An explicitly written number is not needed for implication coverage. This is a correct but directly covered corollary, similar to other formula-differentiation claims rejected on the same bar.

## value

FAIL

The motivating Pearl energy construction is worthwhile, but these proposed quantitative statements are an elementary Taylor expansion/inversion of the originating source’s fully explicit optimized formula and its already proved density argument. Neither the constant c* nor the √ε optimizer correction resolves an independent structural or unknown exact invariant that is not mechanically determined by the prior formula; the all-order coefficients are direct algebraic consequences. An unmotivated extra precision on a source formula does not clear the same scientific-value threshold applied to derivative-only formula restatements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
