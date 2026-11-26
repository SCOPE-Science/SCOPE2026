---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For prime p>m>=2, p is not divisible by m, so T is the next admissible multiple p+s, 1<=s<m. All selected k obey s<k<p, and T<p^2. Kummer gives exactly one borrow at p and none at greater powers; earlier rows are strictly below p. The arbitrary-row upper bound also checks independently: if q=lambda*p^t+b and b>0, choose k=mb; k has high block X=floor(mb/p^t)<m and N-k has zero low block, so after separating low digits the total X+lambda*m<pm<p^2 has at most one carry. If b=0 and lambda>=2 choose k=mp^t: the shifted sum is lambda*m<p^2. If q=p^t then q>=2 forces t>=1; choose k=mp^(t-1): the shifted sum m+(p-1)m=pm has exactly one carry, since m<p and no higher digit is needed. Every witness has 0<k<N. Inspected frozen verifier (target and lower rows, no arbitrary-row empirical bound), not executed. Independent replay: python3 /workspace/branches/independent_probes.py 2; 36553 admissible rows up to p^3 with p prime 3..19 and 2<=m<p, exact residue comparisons for the upper bound and direct binomial divisibility at target rows. The proof, not the finite replay, supplies the global bound.

## originality

FAIL

Demonstrated coverage of the full mathematical conclusion via the broader Lucas/minimal-zero-sum criterion in Resultary 339a752cfdc3 and the prior global maximum theorem of Fairfax-Ball. For p<N=p+s with s the least positive residue of -p mod m, W(N) is s copies of 1 and one residue -s. A subset without -s must be empty to sum to zero, and one containing it must use all s ones. Below p any admissible N>=2m has at least m ones as a proper zero-sum subset. Hence the first positive row is T. Moreover T<p^2 and Kummer or the Legendre valuation formula bounds every coefficient by 1 there: the broad criterion therefore implies coefficientwise exactness, not just a gcd-level assertion. The November catalog date establishes neither priority nor dependence; mathematical coverage is the reason for FAIL, not an assertion that the exact formula was published first in that text.

## value

FAIL

The first extremal row is a naturally motivated invariant, but in the stated regime its exact value and coefficientwise refinement are an immediate two-digit application of the known rowwise flag and maximum. No independently nonmechanical remainder of the asserted result was identified. A condition beyond p>m would be new work, not a repair of this proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
