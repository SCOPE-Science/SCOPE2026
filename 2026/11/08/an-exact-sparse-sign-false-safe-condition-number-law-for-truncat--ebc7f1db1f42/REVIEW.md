# Independent mathematical audit

## correctness

PASS

For s>=zeta>=2, N>=max(s+1,5), sketch columns uniform over M=2^zeta*C(s,zeta) unit signed-support vectors, build normalized b1=(e1-e2+epsilon e3)/sqrt(2+epsilon²), b2=(e1-e2+epsilon e4)/sqrt(2+epsilon²). Gram off-diagonal c=2/(2+epsilon²) gives kappa(B)=sqrt(4+epsilon²)/epsilon. In orthonormal span q1,q2,q3=e5, the displayed symmetric near-I matrix sends b1 to b2 and has nonzero q3 component in A b2, hence genuine nonterminated t=0 Krylov prefix; ||A-I||<1 makes A SPD. For S columns s1..s4, v=s1-s2; if v!=0, ||v||>=sqrt(2/zeta), and epsilon<sqrt(2/zeta)/(tau+1) ensures sketch condition>tau. Thus accepted event requires s1=s2 (prob 1/M). Conditional collision, SB is a common multiple of [s3,s4], and condition<=sqrt(2zeta-1)<=tau iff s3,s4 are nonparallel, occurring with probability 1-2/M. The exact full-rank false-safe probability is (M-2)/M² for all admissible epsilon. Independently enumerated full-support signed patterns zeta=2..5 and exact count; finite enumeration only corroborates all-s,zeta proof.

## originality

PASS

Compared same independent-column sparse signed sketch and monitor in Güttel–Liu–Nyman primary article, collision-based lower bounds on OSE and same-day Gaussian continuous-angle acceptance theorem. Neither states this discrete full-rank accepted collision atom with (M-2)/M² or near-identity SPD realization. Unlike Gaussian theorem, the signed sketch distribution has a discrete collision atom. Originality best-of-knowledge with unindexed CountSketch risk.

## value

PASS

A condition-number-only check for a sketch of an unorthogonalized Krylov basis can falsely accept arbitrarily ill-conditioned true bases even when the generating SPD matrix tends to I. The exact positive atomic probability, nonterminated genuine SPD Krylov realization and quantification across sketch sparsities isolate a concrete numerical diagnostic failure mode. Its rarity and detectability by separate norm guards are stated; this is meaningful as a caution about this statistic, not a claim of common practical failure or full restarted-algorithm breakdown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
