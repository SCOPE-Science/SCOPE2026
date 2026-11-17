---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Uniformly naming the n chords yields exchangeable double-occurrence words, whose restrictions to any k marked chords are uniform among (2k)!/2^k words. The 90 three-label words give probabilities (1/3,2/5,1/5,1/15). For two triple sets sharing r=1,2,3 labels, exactly enumerating all words on 6-r labels yields Q1 of denominator 2835, Q2 of denominator 315 and Q3 of denominator 15; disjoint supports are independent. Summing covariance of triple indicators gives comb(n,3)*sum_{r=1}^3 comb(3,r)comb(n-3,3-r)*(Q_r-qq^T), equivalent to displayed quadratic matrix expression. Independent enumeration of all 113400,2520,90 double-occurrence words reproduced all 48 table entries. A separately coded symbolic interpolation checked every matrix component at n=3,4,5,6,17,118,119 and recovered the exact N1,N2 numerator n^2-115n-420. Its root lies strictly between 118 and 119 (n=118 -> -66, n=119 -> 56), establishing sharp sign via monotonic quadratic for all n>=3. Finite verification is exhaustive for the finite Q_r tables needed for the infinite-n overlap identity, not an extrapolation in n.

## originality

PASS

PASS, best of knowledge: Flajolet–Noy 2000 gives crossing-count generating functions/moments and random chord diagram asymptotics; Acan 2015 studies vertex degree, cores, independent-set EXPECTATIONS and connected structure, not the joint four induced three-chord motif covariance. Earlier October 13 2026 Resultary proves exact triangle variance and crossing-edge/triangle covariance (a proper subset of the joint information) but does not determine the entire 4x4 matrix or the sharp one-edge/path crossover. No stronger or equivalent exact 3-motif covariance result was identified in actual semantic searches and accessible primary full-text inspections.

## value

PASS

PASS: Full joint second-moment classification of all four induced three-vertex graph types in a canonical random circle graph is a natural complete finite-motif invariant. The highly nonobvious negative-to-positive covariance transition at exactly 119 chords demonstrates a structural dependence reversal not predicted by fixed-triple exclusion, and the finite-overlap derivation is useful for further random chord motif studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
