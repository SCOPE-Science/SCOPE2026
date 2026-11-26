---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The odd-parity chart is affine and the seven-bit characters with index omitting 7 are exactly the 64 chart characters. Subtracting the line character sum from the Krawtchouk sum over all 35 triples gives the recorded table: at sizes 0,1,2 the line sums are 7,1,−1; at a line triple each of the seven intersections is odd, giving −7; at a nonline triple the intersection counts 0,1,2,3 occur 1,3,3,0 times, giving +1. Complements reverse all signs. Thus the trivial coefficient is 28 and nontrivial magnitudes are 4. Since b(0)=0 the coefficients sum to zero, forcing 28 positive and 35 negative nontrivial values. Fourier inversion of the squared magnitudes gives (28²−16)/64=12 for all nonzero shifts. The sign transform is 64 at zero minus twice the indicator transform, interpreted with a zero-frequency delta, so all sign-transform magnitudes are 8. Counting convolution has singular values 28 and 4 and condition number 7. Independently, the coefficient for a monomial on S of size k is the parity of binom(k,2)+binom(k,3) minus the number of pairs of S summing to 7 and the number of Fano lines in S. On the six remaining points the three pairs are the nonzero cosets modulo 7’s span. Lines avoiding 7 are exactly four transversals of even orientation parity after choosing representatives with XOR zero. At k=2 all but three pairs survive. At k=3 twelve subsets with occupancy profile (2,1,0) and four line transversals survive. The contributions of pairs and lines together have even parity for k=4,5 and odd parity for k=6, matching the parities of the binomial sum; k=0,1 vanish. This proves the exact ANF inventory, not just degree≤3. A separate bounded replay builds the support via binary linear independence, checks every direct chart Walsh sum, counts all ordered XOR pairs, and computes each ANF coefficient by direct subset parity. Replay: python3 -B /workspace/reproductions/check.py 4; output /workspace/reproductions/4.log. The supplied script was inspected, not executed. Its advertised Python 3.8 compatibility is inaccurate because int.bit_count requires 3.10 or later; this does not affect the mathematical statement or reproduction on 3.12.

## originality

FAIL

The decisive earlier indexed source is the stronger Steiner-matroid Walsh theorem, SCOPE-20261116-1a9938b7ebb8, read in the local mirror. Its congruence on exactly the same basis support at v=7 forces the exact spectrum by Parseval saturation, not just nonvanishing. Its exact subset-count identity also yields the seven-bit signed-character table. Thus the signed spectrum, (64,28,12) difference set, bentness and exact convolution conditioning are mechanically implied. The residual chart-specific monomial counts are a small parity inventory on the already identified support; they do not rescue the main claim. The classical quadratic odd-theta-characteristic support is not the reason for rejection; it has different affine degree.

## value

FAIL

The Fano basis set is a natural host for a finite harmonic invariant. Here the earlier general theorem and one exact Parseval equality already force the main invariant and every asserted spectral and conditioning consequence. What remains is an elementary count of ANF monomials in this one chart, with no separate motivated use for those monomial counts or new bent-class result. A fresh computation or different character-sum proof does not supply an independently valuable finding in this case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
