# Independent Audit — 2026/09/10/019

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `cb9460ec1d724a6858e32d9b22755bdcc4ce3dd5`  
**Disposition:** **FAILED**

## Correctness

The finite computation is correct: the stored census has positive classwise preimage counts for all nine A_7 classes, so e_2(A_7)=A_7, and therefore width two follows trivially. The character-table/Frobenius calculation is consistent with E=G and yields N(g)=2520. The exact per-element counts form a valid computational invariant.

## Originality

The central theorem is prior art. Martínez Carracedo's work on Engel words in alternating groups proves width bounds, and the 2019 computational paper 'A Computational Approach to Verbal Width for Engel Words in Alternating Groups' states that for 5<=n<=14 every element of A_n is an Engel word of arbitrary length. Taking n=7 and Engel length 2 already gives e_2(A_7)=A_7. The record's claim that no such surjectivity/width theorem was recorded beyond A_5/A_6 is therefore false. The detailed fiber-count table may be a new numerical refinement, but it does not rescue the originality of the packaged headline.

## Scientific value

Because the main mathematical conclusion is already known in a stronger uniform finite range and for arbitrary Engel length, the remaining exact census is chiefly verification data. The record does not demonstrate an independent conceptual consequence of those counts sufficient to support the current research claim.

## Limitations

- The exhaustive census itself can be retained as computational data, but should be contextualized against the existing surjectivity theorem.
- The rejection is for originality/value, not for computational correctness.

## Evidence

- [Martínez Carracedo, Engel Words in Alternating Groups](https://doi.org/10.1142/S0219498817500219): Establishes Engel-word width results in alternating groups.
- [A Computational Approach to Verbal Width for Engel Words in Alternating Groups](https://www.mdpi.com/2073-8994/11/7/877): States that every element of A_n for 5<=n<=14 is an Engel word of arbitrary length; this includes e_2-surjectivity on A_7.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `cb9460ec1d724a6858e32d9b22755bdcc4ce3dd5`; no repository writes were made by this audit.
