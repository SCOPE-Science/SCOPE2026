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

The invertible odd-characteristic change (u,v)=(2(x+y),2(x-y)) gives H(u,v)=(u²+v,u), with inverse (b,a-b²) and exactly one fixed point. A two-step return forces u²=0 from the second coordinate, then v²=0. For H³, eliminating the return's second coordinate gives v²+v+u²-u=0 and (u²+v)²+u-v=0. Using the first in the second gives 2(u²-1)v+u⁴-u²+2u=0. In odd characteristic u=±1 is impossible; substitution into the first then gives numerator u²(u⁶-3u²+6), so the converse holds as well. At u=0 only the origin results; in characteristic three the sextic is U⁶. For p≥5, g(0)=6, g(±1)=4, and g'=6U(U⁴-1), which gives separability and discriminant -2^17·3^7 (g(i)=g(-i)=8). Independently, the splitting-field step can be verified dynamically: any root a gives a primitive orbit with first coordinates (a,b,c) all in Q(a) and all distinct because the first coordinate determines the whole point. Its equations are b-c=a², c-a=b², a-b=c². The signed reversal (-a,-c,-b) satisfies the same equations. It gives a disjoint orbit, because any overlap of the first-coordinate sets would make the two orbits identical, and a set of three nonzero elements cannot be invariant under negation. Thus Q(a) contains all six roots. Eisenstein at 3 gives degree six; their squares are precisely the roots of Z³-3Z+6, an Eisenstein cubic of discriminant -864=-6·12². Its S_3 splitting field also has degree six, so it is the same field. The sextic is therefore a regular S_3-set, and its discriminant excludes ramification outside 2,3. Over F_(p^m) the Frobenius power fixes six or no roots according to d_p|m; each primitive orbit uses three points. Chebotarev applied to the three class sizes gives the stated prime densities. For p≥5, a cubic root and square discriminant force the Frobenius to be an even permutation with a fixed point, hence the identity. The proof covers all extensions. A separate bounded enumeration of F itself over odd primes ≤139 agreed with the cubic-splitting test, including two primitive three-cycles at p=29,59,79,103; it is not used for the densities.

## originality

PASS

The original map, its membership in the standard quadratic Hénon family, and generic short-period algebra/Galois density machinery are not new. The distinct supported claim is the specific regular S_3 splitting law and resulting all-extensions period-three trichotomy for this parameter. Inspected sources on the same map or broader family do not reach that conclusion; historical short-period literature remains a disclosed risk.

## value

PASS

The exact minimal extension degree is a useful invariant of a published quadratic permutation, not a free choice of a toy polynomial. The calculation distinguishes two complete primitive cycles from no cycles for each odd prime and extension and explains the prime-density trichotomy by a concrete regular Galois action. It does not merely apply Chebotarev to an unconnected field, give a prime sample, or assert a longer-cycle classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
