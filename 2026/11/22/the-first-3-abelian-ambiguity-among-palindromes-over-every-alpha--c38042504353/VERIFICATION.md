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

For lengths 1 and 2 the full observed word is an available factor. For n>=3, subtracting the trigram prefix-marginal from the bigram counts yields the indicator of the final bigram. For a palindrome this determines its initial bigram, and conversely the trigram counts and initial bigram recover the bigram and unigram counts using the reversed final bigram. Independent replay `python /workspace/replay/combinatorial.py palindromes` generates each equality pattern of an initial half in first-occurrence order, then exhausts all directed de Bruijn trails with the fixed starting bigram and prescribed multiset of triples, retaining only palindromes. Choosing each possible unused labeled transition and tracking its multiplicity enumerates the entire fiber of the representative; reversing the equality-pattern relabeling covers every alphabet and does not merge distinct words. This gives only singletons at 3..9 and exactly the two normalized doubletons {0001001000,0010000100} and {0012002100,0021001200} at 10, with no larger fiber. An additional direct exact five-symbol replay corroborates 3025 singletons and 50 doubletons accounting for 3125 words at length ten (all 7810 words at lengths 1..10 enumerated); there is no extrapolation beyond length ten. Each half has at most five symbols and equivalent words have the same symbol support. The ordered majority/marker pair gives q(q-1) repeated-marker fibers, while the second form fixes a majority and an unordered pair, giving q*binom(q-1,2), disjoint by support size. This proves the uniform counts, including q=2, the distinct-profile and singleton formulas, and the absence of longer fibers at length ten only.

## originality

PASS

Pass for the complete length-ten fiber classification over every alphabet: in particular the interchanged-marker doubletons, absence of any other types or higher multiplicities, and the exact counts for all q. Do not credit isolated novelty for the cutoff in light of the materially overlapping same-day general-threshold summary, or for the repeated-marker pair once restricted from the earlier sparse-shell theorem. No priority ordering is inferred for the same-day threshold work.

## value

PASS

A natural inverse problem on a standard word equivalence asks not just when symmetric words are ambiguous but how that information first fails. Exact order-ten fiber sizes and symbolic descriptions distinguish relocation of a repeated marker from interchange of genuinely different labels, and the no-triple-fiber result gives a sharp bound on ambiguity for every alphabet. The first complete ambiguity census, rather than the known partial example or a chosen small shell, is the substantive finite result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
