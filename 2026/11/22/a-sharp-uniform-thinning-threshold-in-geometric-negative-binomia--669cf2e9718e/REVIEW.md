# Independent mathematical audit

## correctness

PASS

Factoring the pgf numerator gives a complex-conjugate pair w,w̄ with |w|<q, where w=q/(1+i√s ε), s=(1−p)/p and ε=1−q. Log expansion normalized by G(1)=1 gives b_n=3q^n−2 Re(w^n)>q^n and summable jump intensities b_n/n. For the thinning quotient the first-order coefficient at retention t→1 is (1−t)(b_n−b_(n+1)), proving necessity. Nonnegative consecutive differences give sufficiency by integrating (1−u)(log G)'(u) along u=1−v+vz from v=t to v=1, yielding nonnegative compound-Poisson jump intensities. After division by q^nε the difference is at least 3−2√(1+s)/(1+sε²)^((n+1)/2), positive even at s=5/4 for fixed q<1. For s>5/4, choose n=floor(arctan(√s)/(√s ε)). Then nε tends to arctan(√s)/√s, nε²→0, and the complex phase approaches the direction maximizing the real part of (1+i√s) times a unit complex number. The normalized difference tends to 3−2√(1+s)<0 as ε→0, so failure holds for every sufficiently large q, not only along a subsequence. The pure negative-binomial endpoints are separately self-decomposable, and s≤5/4 is p≥4/9, or α³≥4/5 in the convex model. Independently checked the finite witness with integer operations: write A_n+iB_n=(2500+50i)^n; the sign after normalization by q^n at p=1/5, q=99/100 is the sign of 3·2501^(n+1)−100(52A_n+99B_n). This is positive for n=1,…,12 and negative at n=13, with normalized difference approximately −0.00018947412013575. The infinite classification is analytic, not inferred from this witness.

## originality

PASS

The named mixed-Poisson model and the general thinning criterion are known. The strongest distinct indexed comparison gives an exact thinning and continuous self-decomposability classification for adjacent gamma shapes. It does not cover gap two, where conjugate zeros produce an oscillatory obstruction. The gap-two uniform discrete law is equivalent to a continuous mixture classification, so an exact prior threshold in that formulation would be equivalent coverage; no such classification was located in the actual comparisons. The direct proof also specifies the growing index that witnesses failure near q=1.

## value

PASS

This is a motivated count mixture and a sharp uniform closure question about its possible innovation representation. All laws are infinitely divisible, yet positive weights below the sharp thinning cut fail near one extreme of rate, even arbitrarily close to the admissible pure shape-three endpoint. The conjugate-root regime produces a genuine difference from neighboring-shape mixtures, and the explicit moving-index obstruction explains why fixed finite tests can miss the failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
