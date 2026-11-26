# Independent mathematical audit

## correctness

PASS

The binomial interpolation converges uniformly, and the squared-binomial generating-function identity at z=2 gives F(−x−1)=−F(x). In the first-shift calculation, grouping the symmetric single-positive Vandermonde terms gives an extra factor 2; the two double-positive exceptions at shift valuation 2 have equal residues 16 modulo 32 and cancel. This gives valuation shift +2 in the regular branches. The resulting period is 2^(k−2); k=4 has four distinct values, and for k≥5 its half fails at n=1. At the singular branch the formal dilogarithm relation at z=2 is legitimate by 2-adic convergence and log(−1)=0, and removes the quadratic term exactly. I independently checked the bounded coefficient exceptions by multiplying the factors of P_j with exact rational arithmetic: exactly the two odd nonconstant contributions at (j,m)=(4,2),(8,2) cancel in parity, and the constant term is odd. Above the finite range the stated B(j) is bounded below by (j−3)/2−2 floor(log2 j), giving uniform convergence. An integral restricted power series with nonconstant coefficients even gives the required Lipschitz bound. For indices of valuation r≥2 the leading cubic difference has valuation 2r+ν₂(x−y), strictly smaller than the error, giving bijections on the normalized odd-unit quotients. Reflection gives the other center. Counting one period then yields the stated regular, shell, center and unattained fibers; the two real Haar shell measures sum with 1/8 to 1/7 (the 2-adic convergence convention concerns the interpolation series, not this real measure sum). Independent lattice-path dynamic programming checks every target and the period witnesses at k=4 through 11. Replay: python3 /workspace/branches/independent_checks_2_5.py. The frozen checker was inspected, not run; the bounded checks are not the infinite proof.

## originality

FAIL

A separate indexed record with the same displayed date states the identical complete 2-adic image, image cardinalities and Haar measure, and proves the very same regular and normalized critical-shell isometries and reflection. Its proof, together with the independently prior least period, mechanically implies every extra finite multiplicity here. Thus a materially distinct original contribution beyond the overlapping result is not established. The evidence establishes equivalent mathematical coverage, not which same-day record was first; it neither proves the frozen theorem false nor establishes historical preemption by one of the pair.

## value

PASS

The all-level image and index distribution of this standard combinatorial sequence are natural exact invariants. The proof identifies a genuine cubic degeneration and contrasting regular branches, explaining both the fractal pattern of missing targets and the measure 1/7. This is scientific value for the underlying theorem, not a claim that re-counting the quotient fibers from the companion isometries would be a valuable standalone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
