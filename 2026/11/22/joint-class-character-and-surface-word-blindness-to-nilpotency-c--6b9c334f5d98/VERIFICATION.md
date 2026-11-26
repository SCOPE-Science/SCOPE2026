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

For 0<j<p, T^j−I=N u_j(N) with u_j(0)=j, giving the same kernel and image W as N. The group commutator in the stated convention is ((I−T^k)v+(T^j−I)w,0). It gives G'=W and lower central terms gamma_(r+1)=N^r V, so the class is exactly the maximum block length. The geometric-sum polynomial in characteristic p is (X−I)^(p−1), giving exponent p since (T^j−I)^(p−1)=0 and there are nonidentity vectors. Inside V the C_p-orbits are singleton or size p; outside V the translation conjugations give whole W-cosets and generator conjugation stays in each coset. Thus no outside element is central for N≠0, and the every-size class counts and center follow. In the dual of V, exactly p^b characters annihilate W and extend in p ways across the split cyclic quotient. The other orbits have size p; induction yields inequivalent irreducibles of degree p using restriction to V, and the degree-square sum is the order. For the word law, all nonzero quotient pairs produce a surjective linear map onto W, so uniform inputs give p^(−2) delta_0+(1−p^(−2)) U_W. Uniform measure is convolution-idempotent and the commutators are independent. This yields the stated exact fibers, including zero outside W. The two partitions have p parts totaling 2p, maximum lengths p−1 and 2, including at p=5, and hence meet every assumption. For the rank-one boundary, p=3 and n=2 give class counts 3 at size 1 and 8 at size 3, character counts 9 at 1 and 2 at 3, and one-commutator identity probability 11/27, consistent with 11 classes. Frozen code and output were inspected only. Its dictionary at checker.py line 54 would overwrite rather than add a duplicate key in an untested rank-one case; all frozen test examples have rank at least two, and the theorem's polynomial correctly merges the terms.

## originality

PASS

The strong same-day cyclic-by-cyclic comparison gives exact surface-word twins of unbounded class gap, already at fixed prime. Moreover its construction also implies matching full class and character vectors, as checked below; that broad indistinguishability phenomenon should not be credited here as new. The distinct supported result is uniform collision under the stricter common exponent-p and elementary-abelian derived-group constraints, with the exact class and surface distribution parametrization for unipotent elementary-abelian-by-C_p groups. The cyclic-derived comparison cannot supply that regime, and no inspected broader theorem yields this constrained family of paired collisions.

## value

PASS

The exponent-p restriction is structural, not an arbitrary slice: it removes the cyclic prime-power mechanism and tests blindness without higher element orders or cyclic derived groups supplying class information. The example shows that rank alone controls all these distributions while the length of the Jordan filtration governs nilpotency class, even with a class-two comparator and class approaching p. This gives a usable obstruction for reconstructing class in a natural and narrower group family than the cyclic cousins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
