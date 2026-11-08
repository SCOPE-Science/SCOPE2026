# Scientific review: optimal two-offer tree hitting laws

## Correctness

**PASS.** The state space consists of vertices in a finite complete rooted \(b\)-ary tree with independent, with-replacement uniform neighbor offers. For each deadline the full-history optimal hitting probability is weakly decreasing in depth: any successful path from deeper level must first visit the preceding level, after which the remaining-time optimal probability is at most the shallower level's full-horizon probability. Finite-horizon Bellman induction therefore proves that choosing an offered parent is optimal for *every* deadline. Under this policy the depth chain is a reflected homogeneous birth-death chain. Its difference recurrence gives the exact expectation and its one-step first-passage recursion gives the finite rational probability-generating function.

For \(b=2\), a pathwise upper coupling by an unreflected inward-biased walk and an exact bounded expectation difference reduce the Gaussian theorem to an i.i.d. first-passage central limit theorem, with explicitly computed variance \(720\). For fixed \(b\ge3\), regeneration at the reflecting leaf gives a rare-success cycle whose second moments are uniformly bounded by an outward-biased one-level hitting time. The gambler's ruin success probability and renewal Laplace transform yield the exponential limit and exact leading constant. Numerical labeled-state and exact-rational Bellman/PGF checks are reproducible in `verify.py`; they support but do not substitute for the mathematical limits.

## Originality

**PASS, with priority limitations.** The closest primary source, *The Power of Two Choices for Random Walks* (arXiv:1911.05170), proves a bound using the inward probability \(5/9\) on maximum-degree-three graphs and remarks on outward bias on the infinite degree-four regular tree. These statements contain the qualitative drift boundary. They do not directly state the exact all-deadline optimal finite-tree law, the Gaussian binary-tree fluctuations, or the exponential higher-branching normalized law. The reported novelty is the combined precise controlled-walk distributional classification, not the pre-existing drift observation. Zhang's 2019 general birth-death hitting-moment theorem supplies applicable general first-passage machinery and reduces the novelty attributable to the exact mean alone. Full-text examination did not identify a matching law in those two sources; targeted record and literature searches also did not locate a matching published result. An implicit specialization of more general one-dimensional metastability or birth-death results remains a real priority risk.

## Value

**PASS.** This is a natural, complete, infinite-family classification for the optimal root-hitting distribution under a standard two-choice random-walk control rule. The change from a law of large numbers with Gaussian fluctuations and linear mean to an exponential law with exponential mean occurs between binary and ternary branching, at the graph's smallest integer branching threshold. The theorem quantifies the shape of uncertainty under optimal control, not simply expected speed. The exact finite distribution, through a rational continued fraction, provides a benchmark for general hitting-time control methods and makes precise the gap between the original paper's qualitative drift argument and finite-height stochastic behavior.

## Closest prior results and limits

- Georgakopoulos, Haslegrave, Sauerwald and Sylvester, arXiv:1911.05170, first public 2019-11-12, especially Proposition 3.4, Section 5, and Section 7. The \(5/9\) drift and degree-four outward-bias warning are pre-existing; no claim of novelty is made for them.
- Zhang, *Moments of first hitting times for birth-death processes on trees*, DOI 10.1007/s11464-019-0784-6, particularly its general first-moment identities. The exact mean is an explicit specialization after identifying the optimal control law.
- The conclusion requires fixed integer branching, with replacement offers, a perfect regular rooted finite tree and a leaf initial state. Nothing is asserted about general irregular trees, growing branching, or optimal cover-time control. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
