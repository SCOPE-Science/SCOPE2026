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

In a nonnesting source, second occurrences follow the permutation of first occurrences, so a Dyck path plus that permutation determines the word. A mountain excursion spells BB and interlaces exactly the letters within B. In a primitive nonmountain excursion, the first U after the initial U^p D^q with 1≤q<p opens c. The first and p-th opened letters a and b give edges ab and bc but no ac. The two returns a→b in this configuration differ because c occurs between a2 and b2 but not between a1 and b1; exchanging the two returns preserves all counts and gives a different unrestricted competitor. Conversely, the directed spectrum of a concatenation of BB blocks determines the endpoint letters (distinct unless n=1), its bridges cannot be crossed prematurely, and the unique internal loop/cycle traversal forces BB at each block. The n=1 case is immediate. The composition and permutation count, Catalan denominator and Catalan asymptotic then follow.

## originality

FAIL

The relevant prior result is not just the definition of k-Abelian equivalence. Karhumäki, Puzynina, Rao and Whiteland (arXiv:1605.03319, 2016) give the exact switch-generation theorem and a general singleton characterization by uniqueness of (k−1)-factor returns. The frozen ambiguity switch is exactly their switch at k=2. In the double-occurrence setting every possible switch is of the form a1<b1<a2<b2: a shared middle index would require a third occurrence, and equality of the two endpoint labels is likewise impossible. In a FIFO mountain encoding the only such pairs are within BB, and both returns are identical. In a nonmountain excursion the first and last letters of the initial ascent have distinct returns because a new letter is opened between their respective second occurrences. Thus the frozen singleton classification is a direct specialization of the prior singleton criterion plus the elementary FIFO/Dyck characterization; the resulting composition count is already indexed under the equivalent block representation. No publication-priority inference is made from a different same-day record.

## value

FAIL

The reconstruction question is natural and the mountain description is a useful concise explanation. But as a separate exact finding, the boundary here is a routine application of the general singleton theorem to two occurrences with FIFO order. Once the two returns are compared, the induced path, mountain blocks and enumerated compositions follow from the same first-descent case, and the count is a known block count. No further nontrivial reconstruction invariant or quantitative fiber theorem is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
