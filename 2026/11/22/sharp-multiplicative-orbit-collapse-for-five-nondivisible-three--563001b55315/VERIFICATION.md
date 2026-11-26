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

The starting alternating digit criterion follows from Straub–Amdeberhan–Moll Theorem 3.2 with p=5 and k=3; independently, the 5-adic binomial upper parameter −1/3 has all base-25 digits 8, since 8/(1−25)=−1/3. By continuity from nonnegative integer upper parameters and the Frobenius/Lucas coefficient identity over F_5, (1−9z)^(−1/3) reduces to the product over j≥0 of (1+z^(25^j))³(1+z^(5·25^j)). The binomial coefficients in those factors are units, so E uses precisely the base-25 alphabet D={0,1,2,3,5,6,7,8}. As max(D)·3=24, there are no carries at all between base-25 blocks for the first multiplication by 2 or 3. The sets D ∩ {a:ma∈D} are {0,1,3} and {0,1,2}. For a nonzero five-adic or ordinary integer in either pair set, the least nonzero block yields m²a=4 or 12 for m=2, and 9 or 18 for m=3, all outside D even after reduction modulo 25. This excludes every nonzero triple. The pair-prefix counts are 3^r including r=0. The 3^r balls of radius 25^(−r) give the Hausdorff upper bound; the uniform digit measure gives each such cylinder mass 3^(−r), and for intervening ball radii gives the same power-law bound up to a constant. This proves the matching lower bound and uncountability. The triple is a singleton, and 2,8,32 have only blocks in D (32=1·25+7), so ratio four admits a positive triple.

## originality

PASS

Best of current knowledge: the unit-index language itself is prior work. The distinct supported claim is the evaluated two- and three-position orbit classification for this prime-five alphabet, including the pair dimensions and the change at ratio four. Related indexed and cited work develops multiplicative digit intersections but the available statements do not already evaluate this case.

## value

PASS

This natural set of binomial coefficient unit indices has a sharp small-multiplier boundary: two independent restrictions preserve a positive-dimensional set with an exact growth rate, but the third position collapses both to zero, and ratio four disproves a generic collapse. The exact pair languages and the sharp witness make the small classification usable even without an all-multiplier result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
