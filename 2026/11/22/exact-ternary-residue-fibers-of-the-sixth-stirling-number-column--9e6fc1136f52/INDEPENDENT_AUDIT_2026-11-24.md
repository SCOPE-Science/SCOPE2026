# Independent mathematical audit

## correctness

PASS

The two discarded multiples of 3 in inclusion–exclusion are zero mod 3^(k+2) from the stated starting index, compensating exactly for v_3(720)=2. Every length-2·3^k late block gives one full t-block on each parity. For A=log25, B=log16, C=log4, the reductions mod 27 are (24,15,21), obtained by truncating the logarithm after its cubic term. The even branch's coefficient of t is 1 mod 3 and all nonlinear coefficients vanish mod 3, by m−1−v_3(m!)≥1 for m≥2. For g=f_1/3, the linear numerator is −5A+10B+5C=0 mod 27, the t² coefficient is 2 mod 3, and the t³ numerator after removing 3³ cancels mod 3 by the cube congruence. For m≥4, m−2−v_3(m!)≥1 by Legendre's bound. These estimates also ensure restricted convergence. Thus g' is an isometry with a unique zero α in 3Z_3; translating the restricted series and factoring s² leaves U(s)=u mod 3 coefficientwise, where u=g''(α)/2 is 2 mod 3. The unit square root in 1+3Z_3⟨s⟩ follows by convergent binomial expansion, so s√(U(s)/u) is an isometry (identity plus 3 times a restricted integral series), not just a local approximation. Also g(α)=1/40 mod 9, giving δ=21 mod 27. The even branch contributes one per target; the odd branch has three lifts per lower-depth square root, including k=1. Even-valuation square classes, scaled Haar measure and the modulo-three count (four out of six) give the other claims. Fresh recurrence-only checks at nonaligned blocks n=7..60 (k=3) and n=8..493 (k=5) matched all finite branch profiles; these tests do not determine the high digits of u, which is defined canonically by the derivative. Replay /workspace/branches/79519d69-e82a-41b5-9545-32753b2a0f87/record4_finite_check.py. No supplied checker was executed.

## originality

PASS

Credit only the evaluated all-target fiber law and odd-branch image for the sixth Stirling column modulo all powers of three, with the stated arbitrary-block start condition. The period itself is baseline information. Kwong's Corollary 3.4 gives the period upper bound; the extracted inequalities in Theorem 3.5 are typography-sensitive at b=2, so direct invocation of that statement was not needed: his general generating-function criterion already gives the matching least-period obstruction on specialization. Other inspected Stirling congruence and p-adic results do not give this square-folded branch distribution. The exact binomial-polynomial analogues concern different maps.

## value

PASS

The parity split exposes a genuine distinction between permutation behavior and critical concentration in a standard Stirling sequence. The global analytic coordinate gives the exact output counts for every target at every ternary depth and the exact exceptional support, which are not supplied by the period or divisibility data alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
