# Independent mathematical audit

## correctness

PASS

For s=x_4, direct quadratic recursion is 2s_{n+1}−1=(2s_n−1)², giving s_n=[1+(2s_0−1)^(2^n)]/2; 0<s_0<1 ensures 1−s_n>0 at each finite step. Dividing other coordinates by 1−s_n gives pair-average matrix (I+P_{ij})/2 on p. On E={sum z_i=0}, it equals the orthogonal projector v_ij v_ij^T with three unit vectors v_12=(1,1,−2)/√6, v_23=(−2,1,1)/√6, v_13=(1,−2,1)/√6, all pairwise dot −1/2. Multiplying gives exact p_n−u=(z·v_{I1})(−1/2)^K v_{In}. Every pattern of change bits has 2^K ordered pair continuations, so K~Bin(n−1,2/3) independent of initial pair, and conditional endpoint comes from powers of (J−I)/2. q-th moments average |dot|^q and [(1+2^{1−q})/3]^(n−1); mean-square 2^(−n)||z||² via tight frame. For all three projections nonzero, log error is fixed first-pair term −K log2, so Bernoulli SLLN/CLT prove infinite limits. Independently enumerated 1,092 random words through n=6 with exact fractions and compared stated path squared norms; source checker reaches n=8, 9,840 words. Finite tests corroborate only.

## originality

PASS

Jamilov 2022/2023 full primary theorem studies fixed permutation and parameter α autonomous QSO, thus provides exact nonlinear update but not iid randomly changing pair words. Boyd et al. 2006 full original randomized gossip paper includes asynchronous pair-average matrices, a second-moment convergence criterion and averaging time bounds; the q=2 decay is a known type of conclusion. Bajović et al. random stochastic-matrix paper supplies general rate theory, but accessible claims do not give the discrete triangle orientation-conditioned binomial path law or all q moments. Equivalent three-agent projection and random matrix product perspective was explicitly searched; novelty accepted only for exact joint finite-horizon law, positive-moment spectrum and log-fluctuation specialization, with possible broader hidden gossip formulas retained.

## value

PASS

Exact q-order fluctuation spectrum and quenched–annealed separation in the smallest nontrivial iid switched population operator illuminate why second-moment consensus rates do not represent typical individual paths. The complete path orientation law and CLT are natural mathematical invariants of the original four-species nonlinear model, not a routine restatement of one known mean-square inequality; the α=1/2 and uniform-transposition hypotheses are motivated precisely by geometric projection simplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
