# Independent mathematical audit

## correctness

PASS

In the basis 1,x,x²,(x−k_ε)_+², the four-node evaluation determinant is εLR(3εL+4εR+2L²+3LR)/4, nonzero for the entire stated positive-length regime. For p_ε=ε I_ε y, use the first difference quotient in place of the second nodal equation; the resulting system is polynomial in ε with a nonzero determinant at zero. Its inverse yields coefficient error O_{L,R}(ε||y||_∞). At the moving knot the polynomials match and their derivatives are uniformly bounded; comparing on the O(ε)-length moving knot and endpoint regions gives the same uniform error for the norms. The limiting operator is (y_2−y_1) times the derivative-one Hermite profile in the frozen proof. Its left positive peak is L(2L+3R)/(4(3L+4R)), greater than the right positive endpoint at the knot; the right trough has absolute size R²/(4(2L+3R)). Their difference has sign −(2r+1)(r²−2r−2), switching once at r=1+sqrt(3). Multiplying by the exact data factor 2 and dividing by ε gives the stated coefficient and the symmetric 5/(14ε) case. At equality both positions maximize the limiting profile; it is not asserted that both are exact norming locations at positive ε. The estimate is for fixed L,R, and merely opposite signs without saturation need not attain the factor 2; the data (−1,1,0,0) do. Independently checked the determinant, confluent solve, peak balance and equal-length coefficient in the truncated-power basis (python /workspace/branches/independent_math_checks.py, section 5). Inspected but did not run the frozen checker.

## originality

FAIL

The distinct indexed 9e2adc916a5b finding covers the central four-node rank-one collision law, exact coefficient and localization transition in normalized coordinates. In those coordinates this record follows by allowing the outer endpoint to drift by O(ε) in exactly the already-used nonsingular divided-difference matrix. Its O(1) remainder is a direct local analyticity estimate in that same proof, not a distinct coefficient or new conditioning regime. The indexed comparison is later by its catalogue date than the date on the frozen record: this verdict records demonstrable equivalent coverage in the available corpus, not a finding that the compared record was published before the frozen work or has historical precedence. It does not rest on inaccessible spline papers.

## value

FAIL

A sharp arbitrary-noise coefficient and threshold in the smallest nontrivial midpoint-knot system are mathematically useful. The inspected indexed result already determines both across the full ratio range and gives the limiting operator profile. Varying the normalized outer endpoint by O(η) and obtaining a bounded additive error are immediate from that same finite linear system. The frozen record supplies no distinct unknown conditioning invariant or nonroutine new regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
