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

Writing n=q m, m is even and prime to p, and the complementary factor takes value −m at X=−1; coprimality mod p lifts over Z/p². Thus the complementary rank n−q factor is a permutation and the q-dimensional factor is nilpotent. With Y=1+X the monic relation has no constant, has every coefficient below d divisible by p², and has degree-d coefficient of valuation one. The binomial identity follows from binom(q,j)=(q/j)binom(q−1,j−1) and the last factor being nonzero mod p, by the expansion of (1+Z)^(q−1) mod p. For 1<=t<=q, reduce the relation mod Y^t to −pY^d W; W is a unit in that truncated quotient, leaving independent coefficients modulo p² below d and modulo p thereafter. Kernel and cokernel cardinalities coincide for this finite endomorphism. At t=0 the nilpotent-factor kernel is trivial. For t=q+r the image is pY^(d+r)A and pA has one mod-p basis vector per degree 0,...,q−1; image size is p^max(q−d−r,0). The expressions coincide at q, saturate at 2q−d, and differ by one exponent from the preceding step. Independent indegree peeling of the full functional graph at p=3,n=6 (531441 states) returned shells [729,5832,13122,39366,118098,354294], without assuming the periodicity criterion. Replay: python3 /workspace/branches/independent_reproduction.py 1.

## originality

PASS

The distinct result is the depth-by-depth population, not the maximum, polynomial representation, or first prime-square relation. The older maximum proof contains the key algebraic input but does not compute intermediate cokernel cardinalities. The repaired text credits that input explicitly.

## value

PASS

The previously studied worst-case clock does not indicate a typical transient or how many points populate each layer. The exact invariant for every p, n in the repeated-primary prime-square regime exposes a transition from two independent p-adic coefficient layers to one. It gives, in particular, the exact mass of the extremal shell and a benchmark for higher prime-power work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
