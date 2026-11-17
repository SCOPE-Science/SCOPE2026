# Scientific review: entropy rigidity for near-Euclidean central sections

## Correctness — PASS
The one-claim theorem consists of the explicit first-variation identity and its sharp-in-type global quadratic consequence for each fixed real dimension. The proof starts from the intrinsic polar section formula, differentiates uniformly in the exponent at 2, and computes coordinate marginals from the rotationally invariant sphere distribution. Strong convexity of \(x\log x\) provides a global first-order defect. A separate \(C^2\) argument near all signed diagonal normals controls the vanishing-defect regime; compactness handles the rest and yields a genuine \(\delta_n>0\). At the diagonal, the calculated spherical Hessian is \(-I/(n-1)\) and the direction-resolved ratio tends to \(n/[8(n-1)]\), safely above the claimed coefficient \(1/16\). The standalone `VERIFY.py` passed 2,066 deterministic numerical/identity checks. These tests check the formulas, not the uniform infinite-quantifier theorem; the proof supplies that.

## Originality — PASS (best-knowledge, provisional)
Koldobsky's subquadratic diagonal-minimality establishes only a *nonstrict* derivative inequality at exponent 2. König's open-access 2024 paper explicitly proposes that strictness could yield near-2 fixed-dimensional maximization. The new uniform, explicit entropy derivative proves that strictness and the new \(p>2\) global optimizer statement with a quadratic deficit. König's subsequent 2024/2025 paper treats large exponents with restrictions and conjectures diagonal maximality near 2 without proving it. Brazitikos and Eskenazis (2026) settle large-exponent optimizers and an asymptotic-in-dimension upper bound below the transition, which does not imply a fixed-dimensional exact maximizing section. Related indexed mathematical records address different bodies/exponents or pairwise comparisons near the high-exponent threshold, rather than the new theorem. The accessible full HTML texts and indexed search comparisons did not locate a prior claim that logically implies this one. This is not independent or exhaustive priority verification.

## Mathematical value — PASS
This resolves the fixed-dimension near-2 case of an explicitly motivated extremal-section conjecture, for arbitrary fixed ambient dimension, and supplies a quantitative stability gap in the geometric distance to the maximizer orbit. It relates cross-sectional volume variation to a strict entropy functional rather than merely obtaining another finite-dimensional evaluation. The method also identifies the obstacle in extending the statement to a dimension-free exponent neighborhood.

## Closest literature and limitations
- S. Brazitikos and A. Eskenazis, arXiv:2611.07619v1 (2026-11-05), theorem on the sharp large-exponent threshold and asymptotic-in-dimension comparison.
- H. König, DOI:10.1007/s43037-024-00375-5 (2024), introduction, theorem, derivative comparison and near-2 conjectural remark.
- H. König, DOI:10.1007/s43036-024-00404-y (online 2024-11-21), maximal-section results for other exponent regimes and a conjecture near 2.
- A. Koldobsky (1998), previously established minimizing diagonal for subquadratic exponents, consulted through the explicit 2024 discussion.

The result does not provide an effective numerical value for \(\delta_n\), cannot assert a dimension-independent interval, and does not address global optimality across the full subcritical exponent range. Equivalent unindexed literature remains a priority risk. Independent mathematical verification has not taken place.

Self-review: passed. Independent audit: not yet performed.
