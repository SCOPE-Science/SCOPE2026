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

With exactly t copies of the two consecutive generators in total, all integers from (pk+1)t through (pk+2)t are represented. Selecting the multiples of p gives I_t=[kt+ceil(t/p),kt+floor(2t/p)] as integer intervals. Between t=0 and h=ceil(p/2) all other I_t are empty; I_h starts at hk+1 and I_t is nonempty thence by writing t=qp+r, 0≤r<p. Both endpoints strictly increase because k≥1. The gap after I_t has length max(0,k-q-[r≥h]), using ceil((t+1)/p)=floor(t/p)+1. For each j=1,...,k-1 this is k-j at exactly the p consecutive indices (j-1)p+h through jp+h-1; all later intervals meet or overlap without a gap. With the initial run of length hk this proves the exact run polynomial, including k=1. The last missing integer is one below the left endpoint of I_((k-1)p+h); this yields the claimed F both at k=1 and later. The genus is the sum of all lengths. Summing the polynomial in k gives uz^h/(1-uz^h) plus p u²z/((1-u)(1-uz)), by summing k≥ℓ+1 for each ℓ≥1. Independently reproduced all 975 finite comparisons and counted 246675 runs by marking representable original sums, not by the frozen modular criterion. This check is finite corroboration; the interval argument establishes the quantifiers.

## originality

FAIL

The complete all-modulus run spectrum is a mechanical consequence of an earlier explicit description of all gaps for consecutive generators, Feihu Liu, arXiv:2607.23076v1, Proposition 2.3. This is not merely a general computability observation or a prior on aggregate invariants: imposing one congruence on the published two-index gap formula yields the entire run partition by a single division into residue blocks. The prior does not need to print the same polynomial. The frozen record credits odd and modulus-three overlap only in more limited ways and does not account for this all-modulus prior implication.

## value

FAIL

The lengths of maximal gaps are a natural finer invariant than genus and Frobenius number, and the formula is a useful explicit restatement. As a contribution of the frozen scope, however, it is obtained from the earlier complete gap formula by taking one arithmetic progression, then grouping adjacent intervals and reading their lengths. The global invariants and rational generating function add routine sums to that same consequence. No distinct independently valuable theorem remains in the record after crediting the mechanical coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
