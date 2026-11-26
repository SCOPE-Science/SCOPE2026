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

The modulo-9 input holds for the whole exponent family. Here is an independent check despite lack of access to the exact cited corollary. Terms vanish if either binomial has a ternary carry. Otherwise each j digit w is 0 except possibly at n-digits equal to 1, and binom(n,j) is 1 modulo 3 by Lucas; thus both exponents may be replaced by 2 modulo 9. Remove factors of 3 recursively from (n+j)!/(j!²(n−j)!), which has valuation zero. For the 3-free product modulo 9 the full nine-block factors (−1) cancel by carry-freeness, leaving two-digit windows. With n-window 3x+y and j-window 3v+w, the local squared factor is 4^(w+1_{y=1}v+vw) modulo 9: this follows from the 3-free prefix products for residues 0 to 8, namely (1,1,2,2,8,4,4,1,8). Summing over the m freely chosen digits, 4^e≡1+3e mod 9; each adjacent pair of 1-digits contributes 3(2^(m−1)+2^(m−2)), hence zero mod 9, and the remaining sum is 2^m+3m·2^(m−1)≡5^m (the m=0 case is 1). With this digit input, enumerating carries yields the stated matrices using ω+conj(ω)=1 and a carry-one tail expectation 1/2. Each aligned block with length exceeding h differs from its infinite-digit mean sum only on at most h overflowing low digit strings, by at most 4h; at most two blocks per ternary level proves the ordinary cutoff rate. After the highest nonzero digit the column is (1/2,1/2); all three matrices preserve its bounding square, and a first loss of a coordinate can never restore both coordinates to 1/2. This proves the two exact rigidity families. All products are strictly positive in the output, and iterating the all-ones matrix gives the claimed unattained zero infimum. The independent residue-class recurrence C(3k)=C(k), C(3k+1)=C(3k+2)=(C(k)+C(k+1))/3 agrees with 19,682 exact shift classifications and 21 non-power cutoff checks (/workspace/branches/independent_replay.py, apery); sampling is supplementary.

## originality

PASS

Credit the mod-nine digit congruence and automatic description as prior input, not new arithmetic. The supported contribution is natural-average ternary sixth-root pair correlations, especially the sharp first and second levels and their exact digit-pattern equality sets; no inspected overlapping statement determines these.

## value

PASS

Sharp all-shift classification is a natural dependence invariant distinguishing these congruence sequences from their one-point residue counts. The positive arithmetic correlations, the gap between the top two levels, both complete equality classes, and the vanishing all-ones family encode concrete dependence not implied by residue frequencies or mere automaticity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
