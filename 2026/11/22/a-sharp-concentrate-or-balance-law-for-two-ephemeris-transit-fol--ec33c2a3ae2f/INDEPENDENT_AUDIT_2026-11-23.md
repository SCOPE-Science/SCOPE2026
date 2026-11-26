# Independent mathematical audit

## correctness

PASS

The objective is the equally weighted sum of conditional two-success tails; the factor 1/2 is immaterial. For q=1−p, K=n−1, the increment of F_p(k) is k p²q^(k−1) for k≥1 and is zero at k=0. Hence the first increment of the symmetric objective H is strictly negative, and for 0<j<K/2 the sign is that of log(j/(K−j))+(2j−K)log q. An independent sign argument divides by K−2j: with t=(K−2j)/K, the result is −log q−2 arctanh(t)/(Kt), strictly increasing with j by the positive series for arctanh(t)/t. Thus the half-range can only decrease and then increase, with at most one zero step inside; the initial strict decrease rules out an interior tie for the maximum. The odd central reflected pair agrees by symmetry. Rechecked the even factorization and the odd incremental polynomial: dividing respectively by p q^(m−1) after removing the even positive factor, or by p² q^(m−1) in the odd case, yields a strictly increasing expression in q, negative near zero and positive near one. Thus the roots and all endpoint ties are as stated, including p₄=2/3. For p=z/n the exact endpoint difference tends to (1−e^(−z/2))[(1+z)e^(−z/2)−1], with one positive sign change, so two fixed brackets and the finite-n uniqueness imply convergence of np_n. Independently evaluated the positive root by 55-digit decimal bisection as 2.512862417252339353965475… . Inspected the finite supporting checker without executing it; it is not the proof of the all-n result. The strict claim excludes p=0 and 1 and assumes static, equal-prior design.

## originality

PASS

The complete finite-binomial classification is not covered by the inspected sources. The optimizer pattern has a close continuous Poisson analogue and the limiting equation is known in another exact optimization; these are not independently new features taken alone. The scope of this pass is the finite-n law, including its strict ties and the link from the finite roots to that limit.

## value

PASS

For a fixed budget and independent per-visit reliability, two confirmations create a real choice between fully exploiting one ephemeris and protecting both. A unique finite-n boundary with exact tie information gives a complete decision rule without scanning possible allocations, and shows why a partially concentrated compromise is never optimal within this model. This is a useful exact stylized design result, not evidence for real-weather independence or adaptive telescope scheduling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
