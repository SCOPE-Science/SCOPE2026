---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With positive allowed flip rates and n≥3, a frozen set contains no pair with a common neighbor, whether or not either site can itself flip. The distinct endpoints of non-returning two-step walks are T^{±1}v and T^{±2}v for T(r,i)=(1−r,i+1); repeated edges cause no change, including at n=4. T closes after lcm(2,n) steps, so the relevant graph is one squared 2n-cycle or two squared n-cycles. Marking a selected position counts each labeled k-set k times and yields (m/k) binom(m−2k−1,k−1) for 1≤k≤floor(m/3). This also proves the stated degree deficit. The weighted transition 1→2 forces 2→3→1 before another selection; the all-zero cyclic word has exactly the constant path at 1. Thus the trace is the cycle polynomial, and the primitive matrix gives the stated limit at z>0. Independent Bernoulli weights give the exact tilt and the inequality ρ(z)<1+z makes the log rate strictly negative. The supplied verifier was inspected as text and its recorded finite calculations are corroboration only; the all-size proof does not depend on them.

## originality

FAIL

Two distinct indexed circular-ladder open-packing findings give exactly the frozen finding's coefficient-by-coefficient polynomial after the equivalence in its own proof. The entropy and Bernoulli formulas are routine consequences of that covered census. This is positive equivalent coverage, not a priority inference from catalogue dates.

## value

FAIL

The full density-resolved frozen census is naturally motivated, but the distinct remainder beyond the covered census consists of reweighting under the independent initial law and the standard growth rate of the spacing polynomial. Neither supplies another nontrivial invariant, kinetic statement or independently valuable new claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
