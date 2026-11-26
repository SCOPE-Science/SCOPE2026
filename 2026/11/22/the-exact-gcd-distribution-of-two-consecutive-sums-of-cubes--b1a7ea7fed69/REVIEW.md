# Independent mathematical audit

## correctness

PASS

Factoring in (x,s=x+y) separates odd primes p>=5 into s=0,-2,-1 with discriminant square class -3 and nonzero common Jacobian determinants; each of the six roots at a split prime lifts uniquely, and p=3 is excluded by the two different linear sum conditions. At 2 exactly one of the two same-parity pairs is odd-odd, so its sum is the necessary and sufficient zero condition through modulus 8 (the even-even cubes vanish there). A root mod 16 would force the even-even sum to have valuation 1 and its quadratic factor valuation 2, a contradiction. CRT gives the finite laws; the three branches bound p by 2X+2 and their box counts by 6(2X/p+1)(X/p+1). After summation the limiting large-prime error is at most 12/M, so finite-prime exact-valuation limits give actual exact-value densities and full convergence. The split-prime moment factors are summable in excess over one for 0<t<1 and equal 1+6/p at t=1, where the reciprocal-prime sum diverges. Independent full residue enumeration matched 22 moduli (2^1..2^5, 3^1..3^3, and p,p^2 for p=5,7,11,13,17,19,23); replay by precomputing cubes mod each modulus and testing every ordered pair for both shifts. An independent product through 10^7 was 0.4059864631292707, with absolute omitted tail less than 3/10^7, confirming 0.406.

## originality

PASS

Credit the known general limiting-GCD framework and the Ekedahl–Poonen Euler-factor formula. The supported distinct claim is the evaluated all-depth local law for these two diagonal cubic sums, its exact positive-density support and its limiting moment threshold. The closest indexed translated-polynomial analogue uses a different pair with different reductions. No checked prior statement supplies this explicit local law or computes its moment threshold.

## value

PASS

Simultaneous unit translation is a natural first dependence test for the diagonal two-cube form. All-depth local counts distinguish a sharp dyadic obstruction from unbounded split-prime exponents and give the exact support of an almost-surely finite but infinite-mean law. The prime-by-prime law and exact-value densities are usable in a way that an unevaluated general density product is not.

The dated certificate retains the supplied scientific assessment, sources and limitations.
