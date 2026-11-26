# Independent mathematical audit

## correctness

PASS

Checked RESULT.md lines 4–52. A maximal commuting subset contains zero and is product-closed since products of commuting elements commute with every member. Two off-diagonal triples can commute only by both products being zero: if both are nonzero they occupy different diagonal fibers. Therefore sources and targets are disjoint; each index used by an off-diagonal triple excludes its entire diagonal fiber. Completing the rectangular block adds no conflicts, and the remaining fibers must be maximal pairwise commuting subsets of G, hence subgroups (products and inverses commute with all members). Conversely the diagonal identities block off-diagonal incidence at unused indices and the full rectangle blocks a source in T or a target in S; all remaining elements are included or forbidden by maximality in the pertinent group. This proves uniqueness and all scope cases, including G trivial and U empty. Independent choices give one factor z for zero, z^(|G|st) for the rectangle and H_G(z) for each unused index. Inclusion–exclusion leaves (a+2)^n−2(a+1)^n+a^n for the rectangular family; adding the diagonal family gives the stated total. The full formula uses |G| explicitly, in addition to the subgroup-size data. A separate finite check (python3 /workspace/review_checks.py 2) enumerated commuting cliques and tested product closure and size multiplicities including zero for 12 small cases over five groups: S3 gives totals 18 and 94 at n=2 and 3; the n=4 total 558 follows from the proved expression. The finite check is not a proof in arbitrary n or G; the frozen scripts were inspected, not run.

## originality

FAIL

The distinct indexed Resultary record 4fb43e2cf90b directly covers the entire frozen classification, order polynomial and total for all finite G, with n≥1 rather than n≥2. Its extra extremal and asymptotic results do not leave a distinct remainder in the frozen record. This is a failure of distinct mathematical coverage, not a finding about chronological priority or derivation; the comparator's displayed catalogue date is later than the frozen item's directory date.

## value

PASS

As a mathematical result, the full inclusion-maximal size distribution for arbitrary finite Brandt semigroups is structurally useful: it reduces a semigroup clique census to a finite-group subgroup spectrum and a rectangle count, and distinguishes subgroup choices of different orders in nonabelian examples. A clique number alone would not supply this information. This assessment of the theorem's mathematical content does not supply a new contribution beyond the exact comparator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
