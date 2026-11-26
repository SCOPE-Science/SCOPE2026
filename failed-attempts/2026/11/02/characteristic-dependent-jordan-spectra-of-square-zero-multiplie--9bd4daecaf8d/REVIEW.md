# Independent mathematical audit

## correctness

PASS

For R=k[y]/(y^n), write f=a+xb and let u,v be the valuations with zero assigned n. Then f²=a²+2xab, so square-zero means 2u≥n and, outside characteristic two, u+v≥n. The R-linear matrix of multiplication has equal diagonal a and sole off-diagonal b. If v≥u, eliminate b with a, leaving two factors of valuation u; if v<u, pivot on b and the other factor has valuation 2u−v capped at n. Zero factors give the same formula. The k-rank is therefore max(2(n−u),n−v), and m_f²=0 makes rank the number of Jordan blocks of size two. Every rank r is witnessed by xy^(n−r), including zero at r=0. Bounding rank gives u≥n−s and v≥n−r for s=floor(r/2), and 2u≥n is then automatic. In characteristic two these bounds give one linear space of dimension s+r. Outside characteristic two the spaces L_h in the proof exhaust all points: take h=n−u; conversely their defining inequalities imply square-zero and the rank bound. When s≤n−r they are nested. Otherwise the maximal ones are L_{n−r},…,L_s, of dimension n with intersection for i<j of dimension n−(j−i). The intersection with the previously added union is the intersection with the immediately preceding component, yielding q^n−q^(n−1) new points per step. This gives all cumulative counts including r=n. For e=r+s−n>0 these counts differ from q^(n+e) since q^e>1+e(1−1/q); the first such r is ceil(2(n+1)/3). The coefficient conditions and intersections apply over the algebraic closure and describe reduced support only. The supplied checker was inspected, not executed: it constructs finite multiplication matrices and compares Gaussian-elimination histograms with an equivalent valuation sum; it does not certify the universal geometric statement.

## originality

FAIL

The distinct indexed all-element census for the exact same algebra gives the first and second power ranks on every valuation cell in positive characteristic and the corresponding finite-field weights. Selecting the cells with second power rank zero and first power rank at most r gives this census; taking their maximal closures yields exactly the reduced components. Equivalently, after the rank cutoffs the odd-characteristic region is a split-node jet locus with free tail coefficients, with an elementary coordinate-linear component rule. The extension to characteristic zero uses the same two formulas with 2 nonzero. Thus a distinct result beyond specializing the stronger valuation stratification and evaluating its cells is not established. The two indexed records carry the same date, so the comparison demonstrates mathematical coverage, not who obtained it first. The failure is not based on inaccessibility of monomial-jet literature.

## value

FAIL

The square-zero slice is mathematically natural, and the component transition gives an interpretable description. But the stronger exact-algebra valuation stratification already identifies the relevant cells via ranks of powers one and two. The remaining closed counts and component data come from elementary closures and a single valuation inequality, equivalent to a truncated product equation in two variables with free tails. At this scope the record has not established an independently valuable unknown invariant beyond that specialization; no separate surviving claim is being delivered as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
