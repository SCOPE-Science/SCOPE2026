# Independent audit — 2026-09-22

Record: SCOPE-20260909-024. Examined 2026-09-26.

## Correctness — PASS
The committed CSV verifier returns `VERIFY_OK`: 60 S7 and 110 S8 triples are integral, nonnegative and satisfy symmetric plus alternating equals the square coefficient, with maximum absolute gap two and the stated lexicographic witnesses. I checked the explicit class-square formulas against the decomposition statements in the open prior paper: for λ=(5,2) at n=7, its Proposition 5.4 has symmetric multiplicity two of ν=(5,2) and alternating multiplicity zero, exactly the candidate's S7 maximal-gap witness. Its Theorem 5.5 similarly gives symmetric multiplicity two for the S8 pair λ=(5,3), ν=(4,2,2). The census arithmetic is consistent with prior exact formulas.

## Originality — FAIL
The candidate says its λ=(5,2) and (6,2) rows lie outside Bessenrodt–Bowman’s closed forms by focusing on Section 7. Their Proposition 5.4 explicitly gives the **complete symmetric and alternating decompositions of [n−2,2] for all n≥4**, which directly covers both supposedly uncovered rows. The same paper gives [n−1,1] (Proposition 5.4), [n−3,3] (Theorem 5.5, covering S8 [5,3]), and the near-square cases (Theorems 7.8, 7.11, 7.13); trivial representations are immediate. Thus every two-row source partition in this 170-entry table is already covered by formulas published in 2023. Its two highlighted gap witnesses are direct entries in those formulas, not a new finite classification.

## Scientific value — FAIL
A small exact replay table can be a useful teaching or software regression check, but the main decomposition data and maximum-gap-two claim here are direct finite substitutions into existing complete formulas. The record states no independent conjecture resolution or result beyond that recomputation. It does not clear the campaign's scientific-value threshold.

Primary source read in full: [Bessenrodt–Bowman, arXiv:2202.03066v3](https://arxiv.org/html/2202.03066v3), especially Proposition 5.4, Theorem 5.5 and Section 7. Repository evidence: `artifacts/splitting_tworow_S7.csv`, `splitting_tworow_S8.csv`, `verify.py`, `RESULT.md`.
