# Independent mathematical audit

## correctness

PASS

Theorem 1.1, Eq. (1.2) of arXiv:2611.04339v1 has floor(i/a)+1, not floor((i−1)/a)+1, in the relevant prefix, and asserts expected-total-score optimality only for sufficiently large n at fixed k. The standard a-packet word with independent uniform marks has the correct conditional interleaving law. For t≤floor(n/2), with r=floor(t/a), later packets cannot match any prefix guess on N₀>r; the complementary event has probability at most exp(−n/(8a)). The first negative value of i−aS_i requires a zero mark and count exactly floor(i/a)+1, so the survival comparison preserves the correct strict hitting rule. Prepending +1 and counting positive rotations with multiplicity gives (t−aj+1)/(t+1) times binomial(t+1,j), even for periodic words. At p=1/a the weighted sum is the difference of the two given binomial CDFs divided by 1−p. A one-step Bernoulli coupling leaves precisely the binomial atom at r, including t=0. A first hit is impossible at a positive multiple of a because the preceding nonnegative height is at least a−1 modulo a. Stirling and the exponentially small error give the uniform relative tail for fixed a; summing the tail up to H_n−1 gives the exact leading coefficient of the truncated mean. The law concerns the specified canonical sequence, not arbitrary tie choices or early-hit optimization. Read RESULT.md, VERIFICATION.md and verify.py; script inspected, not run; the finite exact checks are not a proof of the all-horizon law.

## originality

PASS

The prior optimal sequence, score distributions and ballot count are credited. The distinct result is the fixed-depth first-hit comparison between the finite GSR deck and a classical critical walk, including an explicit error through the midpoint and a sharp truncated mean. No inspected source covers that connection and quantitative conclusion.

## value

PASS

Waiting time is a natural observable distinct from total score and an explicitly identified gap in the one-shuffle literature. The quantitative coupling makes an exact random-walk identity useful for an actual finite policy. The limiting law is tight while even its half-deck-truncated mean grows like a computable constant times √n, a distinction not visible in expected total score.

The dated certificate retains the supplied scientific assessment, sources and limitations.
