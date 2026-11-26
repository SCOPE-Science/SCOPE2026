# Independent mathematical audit

## correctness

PASS

For a selected a_i, self-privacy is J contained in {i}; an external witness b_j must satisfy j not in J, j different from i, and I minus {i} contained in {j}. The symmetric test is exact. Index overlap rules out every extension of a deleted pair. With disjoint nonempty indices there is no self-privacy, hence each side has size at most two. In a mixed triple the singleton needs an unused fourth index; in a disjoint (2,2) the other vertex on the same side supplies the index of an external witness. This proves the types, including the n=3 exception. Irredundance is hereditary. At n>=4 every disjoint mixed pair and triple extends to a (2,2) set, and none of the full sides, deleted pairs or disjoint (2,2) sets extends. At n=3 the full sides and all nine mixed pairs are maximal. The coefficients follow from counting these types; for example the quartic coefficient is binom(n,2)binom(n-2,2) plus the one-sided contribution when applicable. Both scalar invariants and the K_{n,n} comparison follow. Read VERIFICATION.md and verify_irredundance.py without running the frozen code; a separate direct closed-neighborhood enumeration over 3<=n<=7 corroborated both tables and maximality. At n=3 it obtained all-set coefficients 1,6,15,2 and maximal coefficients 9,2 in sizes 2,3; at n=4, (1,8,28,32,8) and 4x^2+8x^4. These bounded checks do not replace the local proof.

## originality

FAIL

OEIS A290710 already states the entire all-set classification for n>=4 by the same types and their counts, including sizes of every mixed family, and separately lists the all-set total 24 at n=3. The graded enumerator is the size-weighted form of this classification. The n>=4 maximal families follow by one-vertex containment tests directly on those known types and A289121 lists their total. A289121 incorrectly lists 5 instead of 11 at crown order 3, but the correct count and the exact boundary polynomial 9x^2+2x^3 are already published under the equivalent cycle graph in A286954 and A291044. A narrow repair around the discrepancy would therefore be a reconciliation of known tables, not a distinct mathematical finding.

## value

FAIL

The structural description is useful as an exposition, but the size marking is a direct readout of known classes, and maximality is an immediate extension test on those classes. The alternative C6 tables already supply the correct exceptional count and maximal enumerator, leaving no independently useful unknown exact invariant or substantive correction suitable for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
