# Independent mathematical audit

## correctness

PASS

After normalization by the throughflow, the column deficits of the loss-and-transport matrix are a, b and 1+c. Its positive diagonal, nonpositive off-diagonal and strict column dominance give stability and a nonnegative inverse. Expansion along the end rows gives the quadratic P and the three stated cofactors; mass balance is a z₁+b z₂+(1+c)z₃=1. For N=n₀+n₁m+m² the derivative numerator in ascending order is n₁P₀−n₀P₁, 2(P₀−n₀P₂), P₁−n₁P₂. Substituting the middle-source cofactor gives the three sign factors b−T_C, b−a/c and b−T_A. In the open band the first and last coefficients have opposite signs, so the two real roots have opposite signs and the one positive root crosses strictly. Outside the band the coefficients have a common weak sign, with at least one strict unless a=c and b=1. This includes T_A≤0, equality at either threshold and the constant case. The same substitution gives strictly positive derivative for the upstream cofactor and strictly negative for the downstream cofactor. For two boxes the derivative numerators are ab and −a(a+1), and one box has no interbox exchange. For (3,3,1) the middle derivative numerator is 24−6m², with E₂(2)=3/22 and both endpoint exports 1/8. For (20,20,1) it is 380(21−m²); the positive root raises export relative to the common endpoint by about 40.9%. The supplied checker.py was inspected, not executed; its rational linear solves and finite sign/identity checks supplement, rather than prove, the all-parameter classification.

## originality

PASS

Standard box mass balances and backmixing operators are not new. The supported distinct claim is the exact steady-state max/min and source-position phase diagram for common symmetric exchange in the specified directed three-cell chain, including the minimal cell number within that class. Neither close primary transport modeling nor the inspected transient and stationary catalogue analogues establishes the same optimization theorem. This conclusion does not certify historical priority.

## value

PASS

The internal loading position gives a demonstrable mechanism for a sign reversal in mixing sensitivity in a natural open transport model. It is not just an example of a rational curve: the two distinct endpoint-derivative thresholds give a complete decision rule for the first chain size that can admit either an interior maximum or minimum. The equal-endpoint examples show why comparing only weak and strong mixing can miss appreciably greater export. These are theoretical model diagnostics, not a recommendation to tune real dispersion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
