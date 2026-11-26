---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With b>0, mark a transition and record ordered pairs of alternating positive run lengths; a necklace corresponds to one orbit under simultaneous rotation of the b pairs. A rotation of order ell fixes precisely the ell-fold repetitions, giving the stated divisor sum by stars and bars. Its nonidentity terms total at most 2^(n/2) since the totients for all ell dividing b sum to b. Writing r=a+b, s=d+b gives the identity term as 2^n b p_r(b)p_s(b)/(rs). The entropy exponent is continuous on the closed feasible triangle, including zero-weight endpoints, and reaches one only at a=b=d=n/4. Thus a balanced lower witness excludes maximizers outside any fixed fractional neighborhood. Near the peak, Stirling at b-r/2=(b-a)/2 and b-s/2=(b-d)/2 gives the stated exponent and 4/pi prefactor uniformly, including odd r or s. For a global upper bound, fractional balance already suffices: use the maximum point masses of each fair binomial, without assuming that a maximizing triple lies in a square-root window. Constant necklaces contribute one to their separate fibers and do not compete asymptotically.

## originality

FAIL

A distinct November 2 catalogue statement gives precisely the indexed binary cyclic pair-count maximum asymptotic to (4/pi)2^n/n, and more strongly classifies its finite maximizing profiles. For each profile F/n differs from the necklace count by at most the total number of nonprimitive necklaces, at most n 2^(n/2), because each primitive necklace has n indexed representatives and each other necklace has a period at most n/2. This comparison is uniform and transfers the earlier sharp global limit with exactly the same constant. The local profile is not claimed to be verbatim in that entry: it is ordinary central Stirling applied to the two binomial factors of the exact indexed count F=(nb/(rs)) binom(r,b) binom(s,b), followed by the same uniform correction. That count follows by distinguishing one transition at one of n indices and dividing by b; it is the classical transition-total ingredient acknowledged in the record. Thus changing the equivalence relation does not establish a new sharp maximum, and the local display has no separate nonstandard limit or counting ingredient.

## value

FAIL

The ambiguity question is natural, but the headline sharp constant survives unchanged as a direct orbit-size conversion of the already quantified indexed ambiguity. The Gaussian profile is the central Stirling expansion of a product of fair binomial probabilities; it adds no nontrivial orbit phenomenon because the periodic correction is exponentially small. No distinct substantive invariant or threshold survives as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
