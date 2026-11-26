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

The periodic closure appends the least number of zeros making the sum of the two exterior runs divisible by m. When that sum is 1 modulo m, a cyclic period n+j with 0<=j<=m-2 would have total zeros congruent to 1+j-t for t appended ones, a nonzero residue. A shorter-than-word period entails a border. In the special residue case a zero-ended word with zero at both ends can delete its last zero and close cyclically. If endpoints differ, the shortest border v is unbordered, contains a one, and has length at most n/2 (an overlapping border of shortest length k would force a shorter one of length 2k-n). Deleting the final v gives a cyclic closure: the junction gap is the one in the original word that reaches the final copy of v, since its first one is in the same position as in the prefix copy. The zero word has period one. Hence precisely the asserted unbordered words are maximal, including the witness 1^(n-1)0. Reversal exchanges the two orientations. In the 1-to-0 orientation, all words have generating function z^2/(1-z-z^m). A bordered word has unique decomposition vsv with unbordered oriented v; s must run from modular state 1 to 0, first traversing m-1 zeros and then concatenating the loops 1 and 0^m. Conversely such concatenation has shortest border v since a shorter border would border v. This gives the Mahler equation. The whole-language series follows by arbitrary initial/final zero runs and arbitrary intervening 0^(jm)1 blocks. Its dominant root r is simple and unique on its modulus circle by equality in the triangle inequality. U<=A coefficientwise, so its equation continues it into a disk larger than r (chosen smaller than sqrt(r)); its pole at r does not cancel since r^(m-1)U(r^2)<=r^2/2. Taking the ratio of pole coefficients and substituting the equation at r^2 gives the two stated density forms. For the variable modulus, t=m delta satisfies t exp(t)<=m, hence t<=W(m); expanding log(t)+t=log m+O(t^2/m) and using monotonicity gives t~W(m). At r^4 the leading denominator is 4delta+O(delta^2) and the U(r^8) term is bounded after division by O(delta^2) via A(r^8), giving the stated relative correction. Replay: RESULT.md steps 1–5. The frozen checks/verify.py was located and inspected, not executed. An independent bounded enumeration tested all 1,684 admissible words of lengths 2–11 at m=3,4,5,6 by trial of each cyclic completion up to n+m-1, and checked the border criterion and resulting count recurrence there. These finite cases are corroboration only.

## originality

PASS

Credit the established entropy root, shortest-border method, nearby finite-state closing laws and all modulus-two overlap. In particular a general primitive Markov closing-offset limit transports to this language, so mere existence of a fixed-modulus limit is not credited. Supported distinct content is the exact sharp extremizer characterization and all-length enumeration for the variable-modulus family m>=3, its explicit fixed-modulus density and its quantified large-modulus asymptotic. The strongest indexed cases and source-access limits are specified below.

## value

PASS

For a natural strictly sofic family the maximum additive delay grows with modulus, whereas the limiting fraction of words attaining it vanishes at a squared-logarithmic scale divided by m^2. An all-length extremizer count and explicit asymptotic quantify this separation, which neither a generic bounded-offset law for fixed input graph nor entropy alone measures. The result does not extrapolate uniform word proportions from the measure of maximal entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
