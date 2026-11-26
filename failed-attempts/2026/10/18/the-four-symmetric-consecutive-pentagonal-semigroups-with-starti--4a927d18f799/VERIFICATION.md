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

Writing A,B,C for the three successive generators gives differences B−A=3n+1, C−B=3n+4, C−A=6n+5. Reducing 2A and 2B modulo the adjacent differences proves both adjacent gcds divide 2; the outer gcd divides 35 because it divides odd 6n+5 and n(3n−1), whose individual common divisors with 6n+5 divide 5 and 7. Therefore the triple has gcd one. For n≥6 one has A<B<C<2A, hence minimality; direct check handles n=3,4 and the redundant C at n=2,5. A symmetric minimally three-generated semigroup must have a two-generated gluing across a pair with gcd d>1. For n≥71, the adjacent-pair candidates 2C=xA+yB and 2A=xB+yC are excluded by comparing x+y with 2 and using 3A>2C and C<2A. For the outer pair the two strict inequalities in the frozen proof hold at 71 and increase thereafter. They force x+y=d in dB=xA+yC, so (2y−d)(6n+5)=−3d while 6n+5>105≥3d. Exact independent modular-inverse enumeration in 3≤n≤70 excluding 5 gave precisely (n,d,x,y)=(3,2,4,1),(40,35,7,27). For normalized coprime (u,v) and target w, take the least j≥0 with vj≡w mod u; this j minimizes vj among all permitted coefficients, so membership is equivalent to vj≤w. A second independent test marked members k by the recurrence k−A or k−B or k−C in S, starting with 0 and stopping after A consecutive marked integers; adding A then proves that no later gaps exist. Through n=70 it yielded symmetric indices 2,3,5,40, with F=43,133,1699,258529. The standard three-generator symmetry/CI equivalence and the two-generator hypersurface presentation give the CI claim over any field.

## originality

FAIL

The earlier-dated distinct indexed result e2d53bad3bc7 states the exact same all-n symmetry classification for the same ordinary pentagonal triples, with the same n=40 triple and exceptional Frobenius numbers. The complete-intersection wording follows by the standard equivalence; the two dimension-two cases and the witnesses at 3 and 40 follow by direct integer membership/gluing in the already identified exceptions. This is exact statement-level coverage, not an inference from similar titles or a newer date, and the review makes no attribution of derivation or authorship.

## value

FAIL

The isolated gluing at 40 and the complete symmetry set are natural and useful results for a long-tabulated family. The frozen finding, however, covers no new index, adds no unknown invariant, and gives only mechanical corollaries of the already stated exact classification. The separate finite reconstruction does not supply distinct scientific value on the evidence inspected.

The dated certificate retains the supplied scientific assessment, sources and limitations.
