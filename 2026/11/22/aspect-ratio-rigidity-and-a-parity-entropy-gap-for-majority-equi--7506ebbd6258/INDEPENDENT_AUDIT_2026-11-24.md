# Independent mathematical audit

## correctness

PASS

The open degree m+n-2 and neighbor count r_i+c_j-2x yield exactly the two fixed-state inequalities including tie retention; an alternating rectangle would force two opposite column-sum differences both >=2. The row multiset then determines the Ferrers representative uniquely. On its boundary, each occupied row-length block has its minimum r+c at the southeast occupied corner, and each unoccupied block its maximum at the northwest unoccupied corner, giving precisely the two turn barriers including full and empty edge blocks. In the width inverse the starting altitude s=(n+2-m)/2>=1. A leading D-run that ends in a valley has length >=s+1; any interior D-run connects an allowed peak to an allowed valley, and the end is symmetric. If there is only one D-run it contains all n+2>=3 D's. Thus removing the first and last D leaves all relevant runs nonempty. A first peak before any D was at height >=s+1 and a final valley below the last D was at height <=-s-1, so they survive their unit shifts. No interior extremum changes altitude. For odd endpoints, reaching a peak directly gives x^(1+a), with a first valley adding z^(2+b), while leaving it directly gives y^(2+a), with a terminal valley adding z^(1+b); internal two-run transitions have z^(3+b)y^a x^a'. The even case has endpoint valley factors z^(1+b) and internal exponent 2+b. These geometric series and the no-peak cases give the stated rank-one sums. The cubic has one real root >1 (its two stationary values are negative) and the conjugate pair has modulus rho^(-1/2), so the growth comparison follows from the simple positive pole. Read RESULT.md, VERIFICATION.md and verify.py; the frozen script was not executed. A separate bounded reproduction in branches/8260f815-b315-49f7-ac49-a009a2c8d7a9/rectangular_count_check.py with output expanded.out corroborated small Ferrers, path and labelled counts. The proof, not the finite reproduction, covers all rectangles.

## originality

PASS

Pass applies to the width-two invariance and complete parity distinction for rectangles, not to Ferrers nesting, the exact square enumeration or the opposite-parity sequence as a numerical sequence. The strongest distinct Resultary match exactly covers the square specialization, but not the rectangular extension. Source coverage and historical priority are separate, and the displayed same day does not order the square and rectangular records.

## value

PASS

On a natural graph family the theorem determines every symmetry-reduced fixed-state count, with a structural bijection explaining why arbitrarily large aspect-ratio changes preserve the count within one parity. The opposite-parity change alters exponential growth rather than just a boundary term. This is useful new rectangular structure beyond the square count, the known recurrence in another setting, and finite enumeration. It does not quantify labelled populations or primitive two-cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
