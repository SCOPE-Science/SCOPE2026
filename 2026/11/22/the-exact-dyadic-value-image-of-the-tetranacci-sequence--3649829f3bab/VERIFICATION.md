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

The companion matrix advances the specified state, and the independently recomputed A^10=I+4B and four coefficient triples agree with the frozen proof. The interpolation series converges uniformly on Z2 because the binomial polynomials there take integral values, and the nonnegative integer inputs reproduce u_(10t+j). Subtracting two binomial polynomials factors out s-t at the numerator and loses at most v2(m!) in the denominator. For j=1,4 the odd linear coefficient therefore gives exactly two additional valuation units: all terms m>=2 have at least three. For j=5,8 restrict to even inputs and divide out 16 after subtracting u_j. The divided difference from the first two terms is b_(j,1)/2+b_(j,2)(2(s+t)-1), odd, and the remaining terms lie in 4Z2 since 2m-3-v2(m!)>=2 for m>=3 (check m=3 directly and use v2(m!)<=m-1 for m>=4). Each normalized map thus permutes every finite residue ring by isometry and finiteness; nonnegative input representatives suffice for every finite precision. This gives the four entire balls at every precision rather than merely many enumerated outputs. A^40=I mod 16 by expanding (I+4B)^4; independent recurrence enumeration of that returning state gave exactly the ten stated classes, so no other dyadic cylinders can occur. Projecting gives V_1,V_2,V_3, and disjoint Haar masses sum to 5/8. The finite check can be replayed by shifting the state (a,b,c,d) to (b,c,d,a+b+c+d mod 16) from (0,0,0,1) for 40 steps and taking first coordinates; the matrix and coefficient checks use integral powers for j=1,4,5,8. The supplied CHECK.py was inspected but not executed; its reported deeper tests are finite and no equidistribution or frequency assertion follows.

## originality

PASS

The supported distinct result is exact four-ball support for the specific impulse Tetranacci sequence, equivalently ten mod-16 classes each saturated at every higher depth. Known periods and shifted initialization are credited, as are related Tribonacci results. The conclusion is qualified by bounded source access and is not a claim of historical priority.

## value

PASS

The support of a classical recurrence is the natural inverse question to orbit periodicity: one wants to know whether any term reaches a specified residue. A single bounded congruence test answers that question at every dyadic precision, and the exact p-adic closure and measure distinguish this recurrence from nearby generalized Fibonacci sequences. This is not an arbitrary initial-vector slice or merely a finite residue table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
