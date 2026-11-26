# Independent mathematical audit

## correctness

PASS

On precisely the stated interval and for real α>1/2, the triangular kernel has squared Hilbert–Schmidt norm 1/[2α(2α−1)Γ(α)^2]; both products therefore have that same finite trace. Endpoint reflection interchanges the two products and pairs all nonzero eigenvalues. At m∈ℕ the weak 2m-th derivatives of both products equal (−1)^m times the input, so their difference maps into P_{2m−1}. If an input polynomial in that space is killed by the difference, the common output is of degree ≤4m−1; the complementary left/right primitive conditions give zeros of order 2m at both endpoints, forcing it and then the input to vanish. For noninteger α, on a rectangle with x near zero and y uniformly separated from zero the right-product kernel is analytic in x, while the left-product kernel is x^α times an analytic series with all beta-binomial factors nonzero. A linear relation forces both series to vanish; its first N fractional coefficients give a Vandermonde system in 1/y_j. A finite-rank compression would contain every such section, by approximating it by normalized averages near y_j on the separated rectangle, and so is impossible. Reflection converts infinite rank to infinite inertia of both signs. The companion code checks finite rational grids and sampled coefficients only; it was inspected, not executed, and is not needed for the rank argument.

## originality

FAIL

A distinct published catalogue entry gives the identical rank and inertia for the same self-commutator on the strictly larger interval of orders α>0, including reflection symmetry, and adds an integer spectral determinant. The trace-class and trace-zero statements in the frozen range are direct Hilbert–Schmidt consequences and do not constitute an uncovered main result. The catalogue dates do not establish who first obtained the theorem; this is a finding of mathematical coverage, not of historical priority.

## value

PASS

The mathematical phenomenon is structural, not a sampled rank computation: noninteger endpoint powers force independent kernel sections of arbitrarily large cardinality, so infinitesimal order changes turn a polynomial-range defect into one with infinitely many eigenvalues of each sign. This is useful in distinguishing endpoint regularity and spectral behavior of fractional integration. It does not supply a distinct contribution beyond the stronger published theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
