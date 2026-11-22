# Independent mathematical audit

## correctness

PASS

Connected-Laplacian conservation forces equal per-vertex firing count in any return after three steps; excluding 0/3 leaves one fire or two fires per vertex. The degree-bounded nontrivial periodic strip and involution x_v -> 2deg(v)-1-x_v exchange these classes, reflecting total mass about 7n+2. In the once-fire class, two hubs must have distinct phases. For ordered hub phases (0,1), k leaves firing at phase 1 carry one initial chip each and others zero; the phase-1 hub carries exactly n chips and the phase-0 hub has n+1,...,2n-k chips. Hence each chosen k-subset yields one state at every mass 2n+1+k,...,3n, and six distinct ordered hub phases give cumulative binomial coefficients. Summing (n-k)binom(n,k)=n2^(n-1), doubling by complement, and dividing into length-3 orbits yields 6n2^n states and 2n2^n orbits. K_{2,n} excludes period three by Jiang Theorem 3.10. Size bias gives K~Bin(n-1,1/2) and conditional uniform slack; their normalized limit, with complement, gives the mixture of uniforms. Independently implemented literal synchronous update with finite bounded boxes n=2,3,4,5 checked respectively 576,4096,25600,147456 initial configurations and each mass coefficient, agreeing with formula. These finite experiments are corroboration, not proof for all n. No mathematical counterexample found.

## originality

FAIL

The exact binomial cumulative mass polynomial, both reflection bands and every coefficient are explicitly given for the identical labelled book graph B_n and same synchronous degree-threshold dynamics in a published 2026-11-02 Resultary finding. The current mass polynomial is exactly three times its orbit polynomial. The current total is exactly three times the earlier book-graph orbit formula. The one-edge period activation follows by combining this known presence with Jiang 2010 Theorem 3.10 for K_{2,n}; alternatively the earlier arbitrary-graph divisible-by-three cycle criterion gives the same. The two-uniform mass limit follows by elementary binomial concentration and conditional discrete uniform scaling from that already published polynomial. None is an independent new theorem. This is affirmative implication, not inference from unsuccessful search.

## value

FAIL

The object and invariant are natural, but this exact book-graph mass polynomial and two disjoint bands were already fully evaluated in the 2026-11-02 published all-connected-graph theorem. The total and phase count were also published in the 2026-11-02 book-graph result. Edge activation merely juxtaposes that known positive count with Jiang 2010 exclusion on K_{2,n}; the conditional two-uniform limit is a short standard binomial concentration calculation from the already known polynomial. There is no unknown natural invariant, new structural lemma, nontrivial boundary, or meaningful independent contribution left once prior coverage is credited. Correctness and reproducibility do not rescue a covered original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
