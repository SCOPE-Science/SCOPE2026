# Review of the eight-one prefix-normal palindrome enumeration

## Correctness — PASS

The gap-span equivalence converts every prefix-normal constraint into inequalities for sums of consecutive zero runs. Palindromic symmetry reduces seven inter-one gaps to four, and the full list of window lengths leaves exactly \(a\le b,c,d\) plus \(a+b\le c+d\). The substitution \((a,b,c,d)=(t,t+x,t+y,t+v)\) converts admissibility into \(x\le y+v\); subtracting its complement yields the exact rational series. Leading-pole extraction gives \(5n^3/1008\) and the conditional \(40/(21n)\) law. Direct brute force up to length 24 and a separate all-gap/series checker pass. This is an all-length mathematical proof, not an extrapolation from finite experiments.

## Originality — PASS, qualified

The earliest prefix-normal generation paper (arXiv:1401.6346) develops the class but not fixed-eight-one palindromic enumeration. The fixed-density treatment (arXiv:1611.09017) establishes general rationality for prefix-normal words and explicitly computes some small weights, but its stated results do not give the mirrored eight-one subset. The dedicated pnPal treatment (arXiv:1905.11847) and OEIS A308465 enumerate the entire palindromic class by length rather than weight. The new formula, sharp coupled gap condition and conditional density are not implied by those aggregate numerical counts. Historical priority can still be affected by an older unindexed or equivalent enumeration; public literature search is not an exhaustive novelty proof.

## Value — PASS

The fixed-composition refinement addresses the explicitly studied yet not generally enumerated prefix-normal palindrome class. Eight ones are the first even positive weight whose palindromic gap restrictions require a genuine two-gap coupled inequality beyond individual minimum-gap conditions; the resulting subtracted partition generating function is informative rather than a mere unconstrained binomial count. The all-length formula and sharp \(n^{-1}\) probability quantify a natural rare-event regime and provide a reproducible benchmark for string algorithms operating on palindrome-constrained jumbled-factor profiles. The theorem does not solve unrestricted enumeration.

Self-review: passed. Independent audit: not yet performed.
