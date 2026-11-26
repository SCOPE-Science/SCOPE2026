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

Every aa forces two occurrences, hence length at least 2q. At equality, for each pair of letters both orders occur just when their occurrence intervals overlap; the strict common intersection of all intervals separates all first from all second occurrences. Thus successful starts are exactly two permutation blocks P,Q. A shift by t within the first block is successful iff the removed prefix of P and inserted prefix of Q have the same letters, giving exactly the direct-sum boundaries of the relative permutation, with t=0 included and t=q excluded. A shortest balanced word of smaller rotation orbit must be repeated exactly twice, hence is PP, and these have b=q. Thus for b<q the q! a_(q,b) ordered splits count each qualifying orbit 2b times; in the periodic bin each permutation is counted once as a word and q times per orbit. The formal component decomposition yields F=1/(1-C); summing the primitive formula and correcting the doubled bin gives q!/2 times [z^q] log(F/(1-z)). A proper direct-sum prefix of length j occurs in j!(q-j)! permutations; the union bound relative to q! is O(1/q), using the two endpoint summands and binomial(q,2) for the interior. This gives single-cut concentration and the stated counts, and Stirling applied to binomial(2q,q) gives the rarity constant. My direct two-subsequence check for every individual rotation and both b-spectra at q=2,3,4 reproduced the finite results.

## originality

FAIL

A distinct all-depth phase-intersection and period census, Resultary 640a099a3a6b, gives at depth two the complete b-spectrum and asymptotics by elementary extraction. With F=1+sum m! z^m, its total size of t-fold phase intersections is S_t=(q!q/t)[z^q](F-1)^t. This also equals sum_(b>=t) binomial(b,t)L_(q,b). Binomial inversion and binomial(t,b)/t=binomial(t-1,b-1)/b give L_(q,b)=(q!q/b)[z^q]((F-1)/F)^b, exactly the frozen formula. The catalogued period census gives orbit lengths 2q except PP, so all necklace bins and the logarithmic sum follow. Moreover S_1=q(q!)² and S_2/S_1=(1/2)sum 1/binomial(q,j)=O(1/q); the excess of S_1 over the labeled union and the number of multiply witnessed words are both bounded by S_2. With the period correction and Stirling this recovers the frozen large-q bounds. The direct-sum proof is a concise alternate derivation, not a separate new spectrum. This is substantive coverage, not a conclusion about historical priority or who obtained it first.

## value

FAIL

The shortest word length and the phase multiplicity statistic are naturally motivated. However, the claimed counts, periodic correction and leading asymptotic already follow from the indexed all-depth intersection census by binomial inversion and its second intersection bound. The proof using direct-sum boundaries elucidates the formula but is an elementary rewriting of the same prefix-set phase conditions, not a new independently useful theorem on the submitted scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
