# Independent mathematical audit

## correctness

PASS

The language permits integer linear comparisons and negation. For each n≥1 one depth-one child has X~Bin(n,1/2), and B is 2X=n or 2X=n+1; exactly one equality is feasible for any parity, giving q_n=2^(−n)binom(n,ceil(n/2)). The n child leaf blocks are independent, so root Ψ=(#B=0) has exact probability (1−q_n)^n. Stirling gives q_n=sqrt(2/(πn))(1+O(1/n)); nq_n→∞, proving μ_n→0, and n log(1−q_n)=−sqrt(2n/π)−1/π+O(n^(−1/2)) via n q_n^2/2→1/π and n q_n^3=O(n^(−1/2)). Under the original paper’s recursive Definition 6.3, the depth-one B limit is 0, so #B=0 has substituted probability 1 for every outer n and μ′_∞=1. Depth-one probabilities coincide by original definition, and without propositional letters fixed-depth comparisons of eventually 0/n successor counts stabilize as the sign of integer affine expressions, proving zero-letter impossibility. The maximal gap is bounded by probabilities in [0,1]. Independently enumerated all 2^(n²) leaf valuations for n=1,2,3,4, obtaining 1/2,1/4,125/512,625/4096 exactly. Numeric residuals log μ_n + sqrt(2n/π) at n=100,1000,10000 were −0.314677,−0.317297,−0.318003, tending toward −1/π≈−0.318310. Enumeration and numerics are corroboration only, not infinite proofs.

## originality

FAIL

The advertised refutation of Ghosh–Schwarzentruber’s adherence conjecture with maximal unit discrepancy is already established by the published 2026-11-02 Poisson-amplification theorem: its (k,t)=(1,1) depth-two formula has ordinary probability tending to one and recursive-limit probability zero, and its negation reverses those endpoints. The published 2026-11-08 one-letter parity-spectrum theorem is stronger at the crucial alphabet restriction: writing θ_0=(#p-#¬p=0), θ_1=(#p-#¬p=1), C_a=#θ_a, the assigned B is θ_0∨θ_1 and Ψ is ¬[(C_0≥1)∨(C_1≥1)]. That Boolean formula belongs to the prior one-letter fragment. The earlier paper’s exact π_{n,a} law and nπ_{n,a}~sqrt(2n/π) show the ordinary limit is zero on BOTH parities; the original arXiv Definition 6.3 supplies surrogate one. Its exact finite expression is immediate from those same per-category probabilities. The remaining -1/π logarithmic term is routine Stirling-plus-log expansion, while the zero-letter and depth-one lower bounds follow directly from the semantics. The exact expression may not appear verbatim in either older RESULT, but novelty is assessed by mathematical implication; no independently substantive claim survives.

## value

FAIL

The purported resolution of an open conjecture with maximal discrepancy is already the main finding of the 2026-11-02 theorem. The one-proposition depth-two instance is contained in the 2026-11-08 parity-spectrum theorem, which already motivated and classified far more general one-proposition formulas in this exact model. The displayed central-binomial identity and −1/π correction follow immediately from its exact category mass and standard Stirling/log expansions; depth-one and zero-letter minimality are elementary semantic lower bounds. After the decisive coverage, there is no independent motivated unknown exact invariant, structural lemma, or counterexample left that could justify the original claim as a new valuable mathematical result. This is not rejection because the computation is finite or because historical searches are incomplete: it is rejection of a correctly proved but covered and mechanically specialized finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
