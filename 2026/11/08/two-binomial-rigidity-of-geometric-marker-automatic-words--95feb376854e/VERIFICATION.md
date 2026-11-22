---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For every integer B>=2, n>=1 and every starting index, the stated 2-binomial fingerprint is precisely (n,r,T), where r is the number of markers and T their total relative offset, since scattered 01=T-r(r-1)/2 and the other two-letter counts follow at fixed length and weight. For r=0 or 1 the factor is immediate. For r>=2 the markers are consecutive powers B^a,...,B^(a+r-1); their sum gives T=A_r B^a-rs with A_r=(B^r-1)/(B-1). Exclusion of the immediately preceding marker confines a>=1 to half-open T intervals [(A_r-r)B^a,(A_r-r/B)B^a). Adjacent levels cannot overlap because B^r-1>=r(B-1/B) for B,r>=2, with equality only at B=r=2 and the upper endpoint open. The a=0 starts are only s=0,1 and give T=A_r,A_r-r; these lie below the positive levels except B=r=2, when they equal 3,1, the only level-one T equals 2, and higher levels start at 4. Thus T and r uniquely determine a,s and every factor. Explicit integer start windows L_{a,r}=max(B^(a-1)+1,B^(a+r-1)-n+1) for a>=1 and max(0,B^(r-1)-n+1) for a=0, with U_{a,r}=min(B^a,B^(a+r)-n), exhaust the factors with >=2 ones and neither double-count nor omit intervals; the n+1 zero/singleton words all occur at sufficiently isolated large powers. The resulting finite double sum counts all factors. At n=2, distinct 01 and 10 have the same first-order fingerprint, proving sharp order two. The geometric support is B-automatic (regular 10* base-B representations) and not eventually periodic (unbounded gaps and infinitely many ones). Checked the exact B=2,r=2 and end-exclusive boundary cases. A fresh separate exact-integer factor/sum/formula implementation compared 2,400,960 windows across bases 2..9 and n=1..120 with 960 formula comparisons; zero mismatches. These finite diagnostics are supplementary, not proof of the universal quantifiers.

## originality

PASS

Best-of-knowledge originality for the all-base 2-binomial factor-reconstruction theorem, qualified by the preexisting general identity scattered-01 = positional moment minus binomial(weight,2), classical factor-complexity methods, and an extensive same-object reflection-complexity classification. The published same-object theorem enumerates and pairs powers-of-B factors under reversal but does not assert or imply injectivity of the scattered-subsequence fingerprint. Known binomial-faithfulness theorems apply to Sturmian, Tribonacci, and selected balanced/billiard language classes with hypotheses the geometric-power-support word does not satisfy. The closest Rigo–Stipulanti–Whiteland sparse nonrecurrent example requires order 3, not 2. Other published automatic words have distinct languages. The first-level arithmetic separation and exact all-base window formula remain unlocated as prior claims. This is an incremental, not foundational, new classification; unindexed equivalent formulations and stronger theorems are residual priority risks.

## value

PASS

Order-two scattered-subsequence reconstruction of an entire natural aperiodic automatic language is a motivated exact combinatorics-on-words invariant. The proof gives the optimal reconstruction order for every B and factor length and an exact arithmetic factor-complexity census, not an arbitrary finite slice. In contrast, the Rigo et al. sparse nonrecurrent morphic word has order-two collisions and needs order three; the Tribonacci/Sturmian examples are recurrent and structurally different. The uniform nonrecurrent sparse power-marker family therefore provides a natural sharp positive case. Its exact formula is useful for complexity and algorithmic factor fingerprinting, though the counting apparatus overlaps a published same-object reflection census; no broad classification of all sparse words or downstream theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
