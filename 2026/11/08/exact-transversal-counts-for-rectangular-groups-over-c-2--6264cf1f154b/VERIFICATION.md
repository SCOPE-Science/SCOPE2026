---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For every r,s>=1 the nonzero Rees rectangular group has product (i,a,lambda)(j,b,mu)=(i,a+b,mu), with labeled 2rs-point permutations. Indexing each distinct output (i,t,mu) fixes g=t+b. The 2r target middle bits in each mu-slice must be balanced; each such slice admits (r!)^2 independent target-first-coordinate assignments. The source exponent balance assigns each input suffix lambda in (s!)^(2r) ways. Four possibilities for a pair of target bits give exactly (1+z^2)x_i0*x_i1+z(x_i0^2+x_i1^2); extracting z^r and then each x_i,g^s gives a bijective count, no overcount. Inversion of alpha in the opposite semigroup and exchanging the row/column index sets yields N_rs=N_sr. The r=1 and r=2 expansions and n=2 group boundary are correct. Independently reimplemented the coefficient DP and exhausted every 8!-or-smaller permutation: (1,1)=0,(1,2)=8,(1,3)=0,(1,4)=3456,(2,1)=8,(2,2)=2048,(3,1)=0,(4,1)=3456; also N_2,3=2,654,208 by independent coefficient DP. Generality follows from the bijective proof, not finite checks.

## originality

PASS

The all-size complete-mapping enumerator for Rees rectangular groups with nontrivial middle C2 is a specific, natural exact count, not mechanically determined by the known parity-existence theorem or enumeration of zero-containing Brandt semigroups. Resultary semantic searches for rectangular groups, C2 transversals, Rees matrices and complete mappings did not surface a prior formula. Priority remains best-of-knowledge.

## value

PASS

Complete mappings/transversals are canonical semigroup combinatorial objects. The precise labeled count extends a nontrivial all-dimensions existence boundary to a computable coefficient enumerator, with one- and two-row closed forms and row-column duality; this is more than a normalization or a tiny case count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
