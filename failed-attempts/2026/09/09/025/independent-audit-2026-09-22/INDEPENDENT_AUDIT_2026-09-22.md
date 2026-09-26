# Independent audit — 2026-09-22

Record: SCOPE-20260909-025. Examined 2026-09-26.

## Correctness — PASS
Fetched the exact-rational certificate code and data. Its Pisot witness replay, Chebyshev identity check, and every full `--tally n 0 2^n` for n=2,…,12 returned `VERIFY_OK`; degree 12 classified 4,032 by Rouché disks and 64 by exact circle-root gcd/Sturm, with no fallback and exactly the all-negative-lower-coefficient mask 4095. A separate numerical root sweep over all 8,188 degree-2-through-12 monic patterns agreed on the unique candidate mask 2^n−1 at each degree (numerics serve as corroboration, not unit-circle proof). Exact witness enclosures put the degree-two golden ratio below the remaining houses. The n=13,14 records certify only their individual witnesses.

## Originality — FAIL
Mukunda, *Littlewood Pisot numbers* (2006), already characterizes all Pisot numbers whose minimal polynomial is Littlewood and proves that the sequence increases to two. Drungilas’s open 2008 paper states the classification explicitly: for the N=1 case proved by Mukunda, the sole degree-n minimal polynomial is `x^n−x^(n−1)−…−x−1`, and the roots increase to two; its N-generalization is Theorem 2. The candidate's allowance for reducible patterns does not create an exception: a monic integral factor containing only inside-disk roots would have nonzero integral constant of absolute value <1, impossible. Thus any monic ±1 pattern with exactly one outside root and none on the circle is irreducible and falls under the earlier theorem. The 2–12 census, minimal golden ratio, and 13–14 witnesses are finite cases of it. The candidate's claim that the relevant Pisot column was left unproved confuses Hare–Jankauskas's interior-column results with their explicit attribution of this column to Mukunda.

## Scientific value — FAIL
The exact certification is a careful finite replay, but it establishes no new root-location statement, bound, or extension beyond the all-degree classification. Certification of a finite prefix of an existing theorem alone does not support the stated scientific conclusion.

Sources: [Drungilas, *Unimodular roots of reciprocal Littlewood polynomials*](https://scispace.com/pdf/unimodular-roots-of-reciprocal-littlewood-polynomials-1adkq2231x.pdf), pages 2–3; [Hare–Jankauskas, arXiv:1910.13994](https://arxiv.org/html/1910.13994v1), Proposition 2.6 and Section 3; [Mukunda publisher abstract](https://www.sciencedirect.com/science/article/pii/S0022314X05001265). The Mukunda full text was not read: the available thesis PDF showed a human verification screen and Oxford Download reported `needs_human`; the open Drungilas text states the precise prior theorem. Repository evidence: `artifacts/verify.py`, `census_le12.json`, `pisot_13_14.json`.
