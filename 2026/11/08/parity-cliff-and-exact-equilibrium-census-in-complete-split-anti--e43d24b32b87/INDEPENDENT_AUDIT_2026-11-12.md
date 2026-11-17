# Independent mathematical audit

## correctness

PASS

For K_c∨independent_m, let k core ones and ℓ peripheral ones. Core 1 best-responds iff 2(k+ℓ)≤c+m+1; core 0 iff 2(k+ℓ)≥c+m−1, where relevant; peripheral 1 requires 2k≤c and peripheral 0 requires 2k≥c. For k<c/2 all peripheral ones, with k=0 permitted iff m≥c−1 and k>0 exactly when c−1≤2k+m≤c+1; action reversal gives the opposite occupancies. For even c the k=c/2 mixed peripheral layer satisfies |2ℓ−m|≤1. Counting labelled choices gives E_{c,m} as stated. Cut is C(k,ℓ)=k(c−k)+k(m−ℓ)+(c−k)ℓ. Global optimization reduces to concave F(k)=cm+k(c−m−k), yielding cm+floor(max(c−m,0)^2/4). Noncentral equilibria are F local (hence global) maxima, while central equilibria cut c²/4+cm/2. This yields the precise c parity price-of-anarchy law, including c=1 and m=1. Independent labeled enumeration c,m≤7 confirmed census and extremal cuts; proof handles all integers.

## originality

PASS

The general max-cut/anti-coordination equivalence and tractability/hardness are prior mathematics. The most similar Resultary published complete multipartite equilibrium census treats equal size parts K_{n,...,n}; the graph here K_{m,1,...,1} is not balanced unless m=1. Earlier general stable-cut and game-complexity theorems do not imply a full exact labelled split-graph census and odd/even efficiency cliff. Same graph under distinct synchronous/dynamic models was not confused with Nash equilibria.

## value

PASS

The labelled equilibrium polynomial and exact price-of-anarchy parity cliff reveal a sharp qualitative difference: for odd clique size every stable cut is globally optimal, but for even clique size weak-tie central profiles persist and approach a factor-two welfare loss. Complete split graphs are a canonical threshold/split network family, and the full weak-tie census is a nontrivial exact local-vs-global optimization classification, not generic hardness restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
