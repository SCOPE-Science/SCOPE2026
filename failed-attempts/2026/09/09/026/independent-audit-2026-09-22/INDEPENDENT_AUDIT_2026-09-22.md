# Independent audit — 2026-09-22

Record: SCOPE-20260909-026. Examined 2026-09-26.

## Correctness — PASS for the diversity witnesses
I independently enumerated all 64 words from each committed 6×18 generator and all 4,096 from each 12×18 parity matrix. Generator rank is six, G H-transpose is zero, and the direct spectra are 1+45z^8+18z^12 and 1+46z^8+16z^12+z^16. The independently calculated Krawtchouk/MacWilliams transforms agree with direct dual spectra term by term. Both have minimum distance eight. The ancillary 134,596-shortening and 13-vector feasibility censuses were not independently replayed; the two witnesses alone prove diversity. The standard Griesmer bound gives optimal distance eight.

## Originality — FAIL
Bouyukliev, Bouyuklieva, Gulliver and Östergård (2006), page 14, explicitly list two inequivalent self-orthogonal [18,6,8] codes with **exactly these two weight enumerators** and state that both come from the extended Golay code. All their weights are divisible by four, so these witnesses are in the self-orthogonal class. This directly preempts the candidate's diversity theorem, spectra and Golay lineage. The candidate compared only Grassl's single construction and unrelated work, missing the exact prior classification.

## Scientific value — FAIL
The diversity and both spectra were published within a stronger classification. Matrix and dual recomputation can validate existing results but adds no substantive coding-theoretic conclusion; the candidate makes no full classification of all [18,6,8] codes.

Source read in full: [Bouyukliev et al., 2006, author-hosted PDF](https://www.researchgate.net/profile/Stefka-Bouyuklieva/publication/265974028_Classification_of_optimal_binary_self-orthognal_codes/links/5cdf9e84a6fdccc9ddb950ba/Classification-of-optimal-binary-self-orthognal-codes.pdf), p.14; [publisher record](https://combinatorialpress.com/jcmcc-articles/volume-059/classification-of-optimal-binary-self-orthogonal-codes/). Repository evidence: artifacts/G_C1.txt, G_C2.txt, H_C1.txt, H_C2.txt, RESULT.md.
