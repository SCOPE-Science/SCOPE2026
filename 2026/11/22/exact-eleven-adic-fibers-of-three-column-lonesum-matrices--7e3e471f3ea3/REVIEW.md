# Independent mathematical audit

## correctness

PASS

All-depth proof checked. Binary lonesum row masks form a chain: crossed rows allow a 2-by-2 swap; for nested rows sorted by size, the first s rows attain the sum of the columnwise bounds min(s,column sum), forcing their entries. For j=0,1,2,3 distinct nonzero row masks the nested increments give 1,7,12,6 possible chains respectively, with an optional zero row and all nonzero masks required to occur. Inclusion-exclusion gives the stated three-base formula. On writing n=r+10t, the binomial term of degree j has ordinary coefficients with valuations at least j-v_11(j!), tending to infinity. Dividing each branch's first difference by 11 gives nine unit-slope restricted series modulo 11, hence nine bijective isometries after scaling. For r=5 the division is by 121; the normalized series reduces coefficientwise to 7t^2+10t with a unique derivative root t=4 modulo 11. Hensel lifting produces the unique center, and translation gives (t-tau)^2 times a unit series constant modulo 11. Its ratio to U has a restricted square root in 1+11 Z_11<t>; absorbing that root is a translation plus an 11-divisible Lipschitz correction, hence an isometry and surjection. This gives exactly eleven lifts per root, including modulus one, and the exceptional image is contained in the already-covered class 10. The class 1 occurs only at r=0, so any period is a multiple of ten; that branch's scaled isometry then forces 11^(k-1) in the remaining factor. Independently, python3 /workspace/replay_independent.py 3 recomputed the branch certificate by integer binomial coefficients, lifted the center by differentiating falling polynomials, checked every target and excluded smaller periods through k=5 (image sizes 7,77,847,9317,102487; maximum fibers 3,13,24,123,244). The finite replay supports the arithmetic only.

## originality

PASS

Pass for the evaluated prime-eleven image and complete multiplicity law, not for the classical sequence formula, the period as an admissible shift, or the generic Hensel/quadratic argument. A least-period proof is correct but elementary from the power sum and is not a separate originality basis. No compared primary or catalogue statement supplies the exceptional branch together with the nine regular multiplicities for this sequence.

## value

PASS

The three-column count is classical; eleven is a singular prime for its ten branches. The exact image and multiplicity law distinguish full coverage of the same seven target balls from unbounded concentration within one of them, with one translated square providing all excess counts. That is a reusable local invariant beyond the period and ordinary terms; no contribution for other widths or primes is needed for this value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
