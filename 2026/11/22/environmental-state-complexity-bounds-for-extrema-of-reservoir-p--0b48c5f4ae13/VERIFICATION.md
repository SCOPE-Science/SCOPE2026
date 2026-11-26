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

The exponentially damped integral over a two-sided stationary finite-state chain converges boundedly and is the unique stationary solution by contraction (and a factor of the ergodic stationary chain). Applying the joint generator to C times each state indicator gives (D−κGᵀ)m=Πu for unnormalized conditional first moments. Detail balance makes −Π^(−1/2)GᵀΠ^(1/2) symmetric positive semidefinite of rank n−1, and congruence by D^(−1/2) preserves this rank. The resolvent expression for M has a constant zero-mode term plus at most n−1 distinct positive-mode terms c_j/(1+κλ_j). The derivative is a sum of shifted inverse squares. For the general exponent p>0 in the proof, divide the linear combination by (x+a_1)^(−p); differentiation followed by division by p(x+a_1)^(p−1) deletes the first term and multiplies each other coefficient by a_i−a_1 while raising its inverse exponent to p+1. Dropping zero coefficients and using Rolle closes the induction, including exclusion of identically zero combinations. Thus M is constant or has at most n−2 distinct critical points on the stated open domain. Independent symbolic elimination in the three-state moment system gave determinant (κ+10)(111κ+100), with summed Cramer numerator (273κ²+9040κ+5500)/3. Differentiation gives −30(7479κ²+7500κ−26500)/[(κ+10)²(111κ+100)²]. The numerator polynomial inside parentheses has one positive root (−1250+80√3685)/2493≈1.446584864600 and changes sign from negative to positive, proving the unique strict maximum. Its mean is approximately 2.139979258105 versus endpoint limits 11/6 and 91/111, a peak about 16.7261% above the larger limit. Neither the proof nor example covers nonreversibility or sample-path peaks; sharpness is shown only for the first possible case n=3. RESULT.md lines 23–57, VERIFICATION.md, and checker.py lines 28–76 were inspected. The uploaded checker was not run; the example was independently reproduced by symbolic balance, not by treating a finite test as proof of the bound.

## originality

PASS

The known stationary mean formula and known inverse-square kernel theorem jointly supply the machinery for the upper bound: after the reversible spectral reduction, that zero count is an immediate corollary of strict total positivity. No independent novelty is credited to the resolvent, reciprocal kernel lemma, or zero-count method. The distinct supported finding is the reservoir-specific regime-count threshold with a matching, explicit three-regime interior maximum despite strictly increasing flushing and loading. The prior bounds and resolvent do not assert existence under these sign and monotonicity constraints; related switching reversals and the deterministic three-box optimum do not entail it.

## value

PASS

Environmental-state count limits the complexity of a natural control response, the stationary concentration versus switching intensity. The minimal three-regime example provides a specific counterexample to monotonicity even with concordantly increasing inputs and flushing; it is structurally motivated by the exclusion of two-regime extrema, not a search for a small gain. This is an interpretable exact design benchmark, without claiming field calibration or any conclusion about peak exposure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
