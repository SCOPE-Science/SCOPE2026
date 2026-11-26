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

An independent run argument recovers the entire claim. Constant circles fail, including n<4 under the periodic-extension convention. In a nonconstant circle 0000/1111 excludes runs of length ≥4, and 1001/0110 excludes maximal runs of length 2. Thus every zero or one run has length 1 or 3, and each circle has equally many zero and one runs, say r of each. Mark a zero-run start: at position zero the circle is a unique ordered list of r zero/one run pairs, with pair enumerator H=(z+z³)(uz+u³z³). For given n,r, counting all marked starts among indexed words multiplies by r, while counting by fixed start and rotation multiplies that coefficient of H^r by n. Thus the log of the indexed zeta is sum_r H^r/r, giving the stated reciprocal. This also checks the evaluated trace normalization, independently of cycle cancellation. The run pairs all have even length. Every allowed four-window has between one and three ones (two is possible); summing gives the necessary weight bounds, and using a pairs of lengths (3,1) or a pairs of (1,3), filled out by (1,1) pairs, realizes every weight n/2±a with 0≤a≤floor(n/4). A single length-3 zero run with all other runs singleton realizes every even primitive n≥4, since a shorter period would repeat that run; n=2 is alternating. Grouping by least period gives the weighted Möbius inversion, and Burnside terms for rotations with gcd n/d require u→u^d. At u=1 the pole gives root ρ=2.147899035704787…; growth is sqrt(ρ) in the limsup sense, or the rate along even lengths, not a limit of nth roots over odd and even together. Independent replay: python3 /workspace/branches/independent_replay.py 4 (SymPy 1.14.0), using an exact Berkowitz determinant and direct rotation classes for primitive and total necklace weights to n=12. The run argument, not this finite check, proves the all-n statement.

## originality

PASS

There is prior work on the exact same four factors and circular graph (Arnoux), plus comparable zeta computations for materially different local exclusions. The supported finding is the evaluated weight-marked periodic census together with exact weight support and existence of all even primitive periods for the ordinary binary four-palindrome constraint. It is equivalently the binary circle with all maximal equal-symbol runs of length 1 or 3. No inspected prior theorem evaluated or supplied this exact language's invariant by specialization; the graph, renewal calculation, and orbit transforms are standard methods.

## value

PASS

Among circular finite-factor constraints, forbidding ordinary palindromes of the first nontrivial even length is natural. A composition-aware zeta is useful where a plain entropy or a finite-word count does not answer whether a given density or primitive circumference is possible. Here the exact rational function gives every fixed-point and necklace composition, and the run structure explains both the sharp support and nonempty primitive spectrum. This is a narrow exact invariant with natural parameters, not a claim of a new general counting method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
