# Self-review

## Correctness — PASS

The assertion is for all positive four-run parameters and all factor lengths of an infinite periodic word. Every circular maximum-weight binary factor can be shifted without losing ones to the beginning of one of the two one-runs; comparing the two closed prefix-count expressions proves the exact defect. The longest one-run necessity restricts candidate phases. The run-pair symmetry of necklaces gives the two rational series. The proof explicitly handles ties, nonprimitive words, and all lengths by division with remainder. The included independent brute-force circular-window verifier confirms the theorem over 2,401 small parameter quadruples, 650 seeded larger quadruples, and all 32 length-specific coefficients from lengths 4 through 35. Finite checks are supporting evidence, not the proof.

## Originality — PASS, qualified

Burcsi et al. (arXiv:1611.09017) define prefix-normal forms and study pre-necklace enumeration; Cicalese–Lipták–Rossi (arXiv:1811.06273) treat infinite prefix-normal forms; Cunha et al. (arXiv:1702.01280) supply a general run-start factor-search principle. An accessible earlier rearrangement theorem establishes that sorting one-runs descending and zero-runs ascending yields a prefix-normal periodic word; this supplies a sufficiency construction but not the strict failure criterion, the exact deficit of an incorrect order, or the complete successful/unsuccessful necklace census. OEIS A006918 already lists the successful coefficient sequence up to index shift, which is expressly acknowledged. Targeted equivalent-form and implication searches did not find direct coverage of the whole claim. Unindexed or implicit coverage remains possible.

## Mathematical value — PASS

A periodic prefix-normal form need not be a cyclic rotation of the observed host. This is the smallest alternating-run family with a genuine run-order obstruction: an exact parameter condition, a finite-size gap when it fails, and an all-length count of all cyclic instances that realize their extremal jumbled-factor profile. Its univariate census is natural because four-run cycles form a well-defined unrestricted class. The result does not claim a new generic prefix-normality algorithm or a previously unknown numeric sequence.

## Boundaries and reproducibility

The theorem concerns exactly four positive cyclic runs over a binary alphabet. Rotation equivalence does not identify reversal or complement. The exact defect is for the phase beginning at the longer one-run, not the minimum across all phases. Run `python verify.py` to replay finite independent checks; the symbolic arguments in RESULT.md prove the infinite claim. No external independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
