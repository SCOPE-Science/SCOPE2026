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

The morphism is prolongable on 0, yielding a one-sided fixed point w. Every adjacent binary source pair occurs already inside φ(0)=010011. The true φ³ images have lengths 150 and 100, so each factor of length n≤25 in w=φ³(w) lies within two consecutive φ³-blocks. Conversely every such concatenation φ³(ab) occurs because ab occurs. This proves equality of all length-n factor sets, not sample-based inference. An independent standard-library program enumerated all 23,800 windows of lengths 1..25 in the four words of lengths 300,250,250,200 and recovered the explicit 37 palindromes, their exact lengthwise counts, and absence at lengths 24 and 25. Centered subpalindromes exclude every longer even/odd palindrome. Exactly six catalogue elements lack both 0p0 and 1p1 in the complete language, establishing global center-maximality. A separately constructed six-iterate 18,750-letter prefix gave all the same palindromes (468,450 windows) as a diagnostic, not as the infinite proof.

## originality

PASS

The exact same binary fixed point was checked against its founding 2023 paper and 2024 extension; these determine automaticity and abelian complexity, not the 37-entry palindrome language, length-23 bound, or six maximal factors. A 2024 primary classification treats critical exponents of words with at most 25 palindromes (including empty), whereas this word has 38 including empty. The 2021 conditional PPL theorem applies only after a finite-palindrome property is supplied. Two recently published Resultary palindrome classifications involve demonstrably different morphisms/words. Specific published coverage was not located. This is a best-of-knowledge judgment, not proof of global bibliographic nonexistence.

## value

PASS

The fixed point was independently introduced as a notable aperiodic 5-automatic Parikh-collinear example in Rigo–Stipulanti–Whiteland 2023. Palindromic complexity, sharp maximum-palindrome length and global center-maximal factors are natural structural invariants of that particular studied word, distinct from its previously known abelian-complexity function. The exact 37-word global classification is not an arbitrary finite slice: an all-factor cover and two forbidden central lengths establish a complete infinite-language invariant. This supplies the nontrivial finite-palindrome hypothesis required to apply the Frid–Laborde–Peltomäki PPL regularity theorem to this instance. Even without computing the full PPL function or a universal classification, the exact independently useful data pass the standard for a motivated natural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
