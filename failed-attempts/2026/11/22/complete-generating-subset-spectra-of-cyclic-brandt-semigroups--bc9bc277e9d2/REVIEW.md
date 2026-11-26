# Independent mathematical audit

## correctness

PASS

For n≥2 a product with nonzero result is a positive walk with accumulated gain, so producing every index pair requires strong support. At the root the positive closed-walk gains form a nonempty additive subsemigroup of a finite group and hence a subgroup, with zero gain attained by a positive power. For any ordered pair an insertion of root loops produces an entire coset, so a full root gain group suffices; a nonloop arc exists and its square produces zero. Containment of root gains in H_d is equivalent to the normalized potentials modulo H_d, by appending a return path to compare gains; a normalized potential is unique on a strong support. Each present ordered pair then has a nonempty choice from a d-label coset, giving the factor (1+z)^d−1; divisor inversion selects the full group. Strong connectivity is equivalent to avoiding every empty outgoing cut, giving the stated inclusion–exclusion including loops. With n arcs there must be one spanning directed cycle, so choosing n−1 labels freely and forcing the total gain to be primitive gives the claimed minimum coefficient, including m=1. Adding zero leaves generation unchanged. A bounded independent multiplication-table closure census (procedure and full vectors at /workspace/branches/9109661c-36a7-428c-b4d5-c2e9caffd0c9/independent-check.md) agreed coefficientwise with separately expanded formulas for (2,1), (2,2), (2,3), (2,4) and (3,2). It found totals 4, 136, 3124, 57312 and 189504. The uploaded checker was not run; these tests do not establish the general result.

## originality

FAIL

The decisive antecedent is Donoven–Mitchell–Wilson’s full-H-class subsemigroup classification, not merely their maximal-subsemigroup statement or the earlier rank result. For the Brandt identity sandwich matrix, its Graham–Houghton components are single diagonal edges and the component groups are trivial. Lemmas 2.3–2.5 therefore classify exactly the full-cell subsemigroups used in the frozen proof, with root subgroup H_d and one coset potential at each nonroot index; there are (m/d)^(n−1) and each cell is a d-label coset. The target polynomial follows directly by counting strongly supported subsets inside these subsemigroups and applying ordinary divisor inversion. This recovers all coefficients uniformly; the verdict is not based on a failure to fetch the older rank article or on the target’s own catalogue entry.

## value

FAIL

Generating-subset reliability is natural, and the formula is a useful way of presenting its cyclic Brandt evaluation. But this frozen claim is a direct weighted count on the previously classified coset cells, followed by textbook divisor inversion and cut inclusion–exclusion. The minimum count is the elementary single-cycle case, and no independent structural or enumerative contribution remains in the submitted scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
