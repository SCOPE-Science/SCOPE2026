# Independent mathematical audit

## correctness

PASS

For two agents with independent item utility realizations and exponential means w_j, nonenvy probability of one agent is p(S)=P(X(S)>X(S^c)), so global P_EF=p(1−p) and 1/4 is the absolute maximum. For 2 goods equal-mean split attains 1/4; for 3 goods a balanced singleton a=b+c has p=a²/((a+b)(a+c))<1/2, dominating other singleton splits by exponential stochastic ordering. For (1,2,t,t+3), t≥2, the unique ex-ante equal-mean split A={t+3}|{1,2,t}; all pair partitions are optimized by B={1,t+3}|{2,t} via stochastic dominance (prior pairing result). Direct Laplace probability calculation yields p_A and p_B as stated, and rational difference factorization with unique positive cubic zero t*=3.937292225...; equality at t* and global optimizer switch are exact. Independently checked the difference factorization using SymPy, derived p values and the t=4 rational improvement 11081/141134400. Verified the general large-t advantage leading a(b−a)/(2t²) from the source analytic expansion. Finite checks do not substitute for all-real-t proof.

## originality

PASS

Igarashi and Oh 2026 establish common-convolution-family ex-ante optimality and a broader log-concave approximation/counterexample but do not, in accessible material, furnish this all-exponential first-failure boundary or the exact cubic t family. Distinct published 2026 'Extremal pairing' theorem explicitly solves the 2+2 subset by stochastic dominance; that part is credited and not claimed new. The surviving result is the global comparison of best 2+2 versus the ex-ante EF 1+3 allocation, its transition and robust unequal-exponential neighborhood. Complete Igarashi–Oh arXiv HTML and lawful OA failed; authorized Oxford request returned vpn_disconnected without full text. This is a material priority risk, not proof of coverage. Best of knowledge PASS.

## value

PASS

Whether equality of ex-ante expected utility maximizes the probability of no ex-post envy is a natural lottery allocation problem. The result identifies the minimal size where heterogeneous exponentials violate a would-be common-family fairness guarantee, determines an exact optimizer phase transition on a nontrivial continuous 4-good family, and proves robustness under balanced perturbation, giving usable quantitative boundary rather than an arbitrary isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
