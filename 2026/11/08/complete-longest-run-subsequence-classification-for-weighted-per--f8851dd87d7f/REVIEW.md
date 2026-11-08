# Research review: weighted permutation powers and longest run subsequences

## Correctness — PASS
The displayed period-span inequality is derived from source-copy intervals for every output run. Descent transitions must advance by at least one additional source copy. This gives a sharp global upper bound, while a constructive selection attains it. Equality forces every letter to appear, natural index order, all used physical letter-runs to be complete, and extra occupied copies to be assigned only to maximum-weight letters. Consequently the stars-and-bars count is exact for distinct output strings. A separate subset-state dynamic program and a different exhaustive language-enumeration routine check 1,440 and 84 finite parameter configurations, respectively. The proof, not the finite check, carries the unbounded statement.

## Originality — PASS (with bibliographic limits)
The key closest sources are Schrinner et al. (2020, DOI: 10.4230/LIPIcs.WABI.2020.6), Dondi–Sikora (2020/2021, arXiv:2011.08119), and Asahiro et al. (2023 and 2025). Inspected source sections address the general NP-hard LRS problem, exact general-purpose algorithms, parameterized complexity, and approximation. They do not present the closed-form optimal value and *entire optimal-label set* for powers of positive weighted permutation templates. General exact optimization programs can solve each input but do not state or trivially subsume the universal equality rigidity and enumerator. Targeted bibliographic and published-result queries found no direct equivalent; absence from such searches is not proof of novelty. Unindexed equivalent work remains a risk.

## Value — PASS
A natural full-dimensional family of arbitrary alphabet size, period run weights and repeat count within a generally NP-hard problem admits an exact optimum and a classification of all optimal output strings. The count depends only on the number of tied heaviest template runs, not on other multiplicities. This supplies a structural explanation and a constant-formula alternative to expanded-instance optimization, rather than a numerical instance or cosmetic specialization. The result addresses length and distinct-optimal-output enumeration; it does not solve general LRS or count embeddings.

Self-review: passed. Independent audit: not yet performed.
