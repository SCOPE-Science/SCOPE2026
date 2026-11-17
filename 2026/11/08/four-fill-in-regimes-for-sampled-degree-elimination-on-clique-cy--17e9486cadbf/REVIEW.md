# Independent mathematical audit

## correctness

PASS

Before any hub pivot, each rim elimination inserts one chord and retains a cycle. At k>=4 rim vertices hub degree h+k-1 exceeds rim degree h+2; a hub is chosen only if all q distinct sampled vertices are hubs, probability binom(h,q)/binom(h+k,q), zero for q>h. The first hub pivot inserts k(k-3)/2 rim edges, giving total m-3+(k-2)(k-3)/2 and the exact stopping distribution. For q=1, first-hub beta-binomial factorial moments yield the stated exact mean; p_k~(h)_q k^-q and survival products yield q=2 linear, q=3 log, q>=4 finite limits, tail exponent (q-1)/2 and exact moment criterion. I reconstructed the hazard, telescoping mass and tail asymptotic. An independently written exact graph-pivot enumerator confirmed 5 small (h,m,q) configurations from actual graph edges; source verify.py was read but its ALL_PASS log is not taken as proof. Covers h>=1,m>=3,q>=1 with fixed h,q limits and distinct-without-replacement sampling.

## originality

PASS

Best-of-knowledge original for the specified refreshed q-candidate current-degree rule on clique–cycle joins; general minimum-degree and randomized Schur complement methods do not imply its exact stopping law or sharp heavy-tail regimes.

## value

PASS

The clique–cycle family is a natural exact symbolic-factorization benchmark. The theorem quantifies dramatic q-candidate risk transitions, including finite-sample expected fill with heavy-tailed limiting excess and an infinite-mean threshold for q=2,3; this is a motivated structural distribution, not a generic elimination identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
