# Independent mathematical audit

## correctness

PASS

For an independent k-subset of P_n, the incidence word padded by zeros has exactly 2k bit changes and r=n-2k+1 unchanged edges. Querying r+1 coordinates in an alternating transformed pattern forces >r unchanged edges; the all-one trace gives VC≤k. The explicit 3-spaced two-choice gadget realizes all 2^min(k,r) labels, proving VC=min(k,r). Counting shifted k-subsets gives |C|=binom(k+r,r), whence Ldim≤min(k,floor(log2|C|)). For r≥1 the balanced threshold-block construction of lengths 2b_i with zero separators gives Ldim≥sum floor(log2(b_i+1)), with exact r=1 and r≥k cases; r=0 is a single concept. Together these prove Ldim=r log2 k+O_r(1) at fixed r≥1. Independently enumerated 34 small (n,k) parameter cells and computed exact finite online ranks where feasible; finite checks corroborate the unrestricted proof.

## originality

FAIL

DECISIVE prior coverage in a published companion theorem on fixed-weight cyclic independent sets. Its full Step 6 separately reconstructs the same fixed-size PATH class on P_{2k+r_c}, states VC=min(k,r_c+1), and proves Ldim=(r_c+1)log2(k)+O_{r_c}(1) by precisely balanced threshold blocks and the class-count upper bound. Setting candidate r=r_c+1 gives the principal VC formula and every fixed-defect logarithmic coefficient. Its block and counting constructions also directly imply the candidate explicit finite lower and upper bounds, while r=0,1 are elementary boundary cases. The cyclic theorem supplies the path result as a proved component, not an unproved title analogy. Both records carry November 8 dating, so relative intra-day priority cannot be established here; the submitted claim nevertheless is covered as a mathematical statement by that existing public text.

## value

FAIL

The fixed-weight path class is a natural source of VC/Littlestone separation, and its precise logarithmic coefficient would have scientific value in isolation. In the submitted form, however, the theorem is already mathematically implied by the stronger published cyclic-versus-path theorem, whose proof contains the explicit path block and counting argument. The present work is a restatement of covered boundary and asymptotic facts, not a distinct new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
