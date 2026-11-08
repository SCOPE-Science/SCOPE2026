# Scientific review: one cross-approving voter and stochastic temporal representation

## Correctness — PASS

The single claim has a common precise domain: two constantly available candidates; \(a,b\ge1\), \(c\ge0\) static approval blocs; independent stationary Bernoulli choices for \(L\ge1\) rounds. Every cohesive group is either a pure exclusive bloc or contains an always-satisfied cross-approver. Hence the maximal demands of PJR, EJR and EJR+ are exactly the two pure-bloc integer quotas. The resulting interval count is binomial. The derivative telescopes to two boundary masses, giving a unique interior optimizer or an explicit endpoint case. Binomial Stirling estimates yield the disjoint-bloc square-root law, Cramér bounds yield the overlap-dependent exponential rate, and the central limit theorem yields the single-voter quadratic window. The proof handles finite horizons, floor effects and the zero and infinite Gaussian-window endpoints. Independent finite direct tests of all three axioms, not mere formula replay, passed 6,858 cases; the standalone verifier completed 7,758 finite checks plus four numerical boundary examples. No finite testing is used to assert an infinite theorem.

## Originality — PASS, qualified by publication-access limits

Phillips, Elkind, Teh and Wąs (2025) develop temporal proportionality axioms and implications, without giving an independent-stationary ex-post success distribution. Teh's IJCAI 2026 full text proves a general static EJR/EJR+ equivalence and explores deterministic welfare and fixed-candidate optimization, but not exact stationary lottery success, a randomization-vs-overlap transition, or the bridge-voter Gaussian horizon. Borodin and Lueger's 2026 arXiv text explicitly studies deterministic online rules and an additive asymptotic PJR relaxation, not this probability event. Public search and research-index comparisons against stochastic temporal voting, randomized quota mechanisms, binomial tails, and overlap/bridge-voter aliases retrieved no directly covering claim. Closest generic binomial statistics cannot imply the electoral coalition reduction without new modeling, although the probability machinery itself is standard. This is not a proof that the literature is exhaustive; related probabilistic studies could remain unindexed.

## Mathematical value — PASS

Deterministic temporal representation guarantees do not reveal how likely an unrestricted independent lottery is to satisfy proportionality once outcomes are realized. In a natural two-candidate election, a single cross-approver alters a zero-width quota corridor to a positive-width corridor. The theorem quantifies this in three complementary regimes: the exact optimal finite-horizon lottery, the fixed-electorate square-root versus exponential success laws, and the sharp crossover \(L\asymp n^2\) with explicit Gaussian profile. This clarifies when independent randomness suffices ex post and when quota-dependence is essential. The result does not claim a broader welfare theorem or new probability limit theorems.

## Closest primary sources and limitations

- B. Phillips, E. Elkind, N. Teh and T. Wąs, *Strengthening Proportionality in Temporal Voting* (first arXiv version 2025-05-28), https://arxiv.org/abs/2505.22513. The 37-page manuscript's model, axiom hierarchy and main contributions were examined.
- N. Teh, *The Price of Proportional Representation in Temporal Voting* (first arXiv version 2026-05-11), https://arxiv.org/abs/2605.11157, readable full conference text https://ijcai.org/proceedings/2026/394. Definitions 2.1–2.2, Lemmas 4.1–4.2, and Sections 3–6 were compared with the exact claim.
- A. Borodin and T. Lueger, *Online Temporal Voting: Strategyproofness, Proportionality and Asymptotic Analysis* (first arXiv version 2026-03-27), https://arxiv.org/abs/2603.26504. The introduction, model, related-work comparison and asymptotic deterministic rule analysis were examined.

Risk remains from unindexed material, alternate nomenclature, and treatments of random voting outside temporal-representation terminology. Dependence across rounds, nonstationary rules, more than two candidates and changing approvals are outside the theorem.

Self-review: passed. Independent audit: not yet performed.
