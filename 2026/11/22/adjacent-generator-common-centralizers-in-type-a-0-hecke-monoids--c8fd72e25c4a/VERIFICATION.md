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

For one generator, two descents leave both products unchanged; exactly one descent forces unequal lengths. With no descents, equal products imply symmetric-group commutation, which preserves the adjacent pair as a set. Its swap would be a double descent, leaving only pointwise fixation. In the two-generator double-descent case with B the three consecutive labels and T its complement, fix the partial bijection T→T. If it leaves t rows and t columns unmatched in T, the unmatched T columns must appear among B rows in decreasing order, and their locations there are forced because every external label is less than all of B or greater than all of B. Inverse descents similarly force the unmatched T rows among B columns. Match the remaining B rows to the remaining B columns in reverse order. This is the unique double-descending completion, giving the sum of binomial squares times (m−t)! for t≤min(3,m). In either mixed case the two fixed positions and the two separately chosen outside matrix entries leave (n−4)! completions. The all-fixed case gives m!; in S_3 the mixed cases cannot occur, leaving identity and longest element. With a=i−1 the position term is a²+(m−a)², giving the stated size multiplicities and gap. The t=3 summand divided by n! tends to 1/36 with O(1/n) error, lower t contribute O(1/n), and the uniform mixed contribution is O(1/n²). In S_n the ordinary simultaneous centralizer fixes the triple pointwise and permutes its complement.

## originality

PASS

The supported distinct claim is the complete position-sensitive count for an adjacent generator pair. Neither the standard longest-parabolic-representative count for the absorbing stratum nor the presentation and permutation indexing is new. The sources inspected do not supply the combined count, in particular the two mixed corrections responsible for its positional dependence.

## value

PASS

Adjacent generators are the smallest interacting parabolic block, and their monoid centralizer tests the effect of the noninvertible length-increasing action under a natural commutation constraint. The exact four-stratum count isolates the source of genuine position dependence even though all these blocks have the same S_3 type and ordinary group centralizer size. It gives the full positional spectrum and a uniform comparison to the group case, not just one sample number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
