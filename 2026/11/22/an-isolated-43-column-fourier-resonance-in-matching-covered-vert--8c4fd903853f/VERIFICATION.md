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

For chosen k-element endpoint sets there are k! bijections with the same character value, so the transform is the stated product sum of elementary sign polynomials. Simultaneous sign negation preserves all phases and reduces the zero test to a=0 and a=1. The Newton identities for right sign sum x=n−2b give the two cubics, including at n=1,2 where out-of-range symmetric sums vanish. For a=0 the variable y=x+1 must divide 2 at a zero, with y=0 excluded by the value −2; none of the four candidates gives integral n. For a=1, put t=3x+1: the exact identity 27(x³+x²+x−1)=t³+6t−34 gives t|34 and t≡1 mod 3. The only admissible (x,n) are (−1,1) and (11,43); (0,−1) fails the size constraint and (−6,11) fails parity. The resulting classes and their complements give nullities 6 and 6·C(43,16)=1,591,092,895,308, with rank 2^46 minus the latter. At n=43 every multiplier is even and a=0,b=22 realizes −2; the trivial character attains the total matching mass 79,594, an upper bound in absolute value for any character. Walsh diagonalization in counting ℓ² then gives the norms without a factor of |G_n|. Direct finite enumeration over endpoint subsets and bijections, summing each character for n=1–5, corroborated the transform and those small zero sets; the divisor candidates and the n=43 witness and counts were also checked separately. The supplied verify.py was inspected, not run. The divisor proof, not finite search, establishes the all-size conclusion.

## originality

PASS

The vertex-activity transform is classical and is also the rank-one sign restriction of a known edge-incidence transform. The compared results do not give the complete zero set on that restriction. The distinguishing claim is the exact exceptional positive sizes and zero classes for the multiplicity-weighted covered-vertex operator, not the parity bound, matching-polynomial definition, or Fourier diagonalization.

## value

PASS

The operator naturally models the matching measure when only covered vertices are observed. The change from arbitrary edge signs to rank-one signs has a substantive effect: instead of all odd sizes, only two sizes give singularity, and the only nontrivial one is isolated at 43. The infinite exclusion, exact loss of recoverable dimensions, and sharp condition number give a useful classification rather than a small-board calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
