# Scientific review

## Correctness — PASS
The four-window central spacing has a continuous piecewise-affine rank representation. On each strict chamber, changing a single input-edge step alters at most three consecutive output windows by coefficients in \(\{-1,0,1\}\). The exact finite-length maximum variations are 0, 2, 4, 5, 6, with explicit distinct-integer input witnesses. Integrating chamber derivatives yields the global two-input inequality. The independent one-input proof uses exact level-set coarea and a complete 16-state, 32-transition potential certificate to prove universal factor 2, a single-replacement bound for five sites, and binary signals establishing sharpness. The stored checker uses exact fractions and independent exhaustive/random tests; the analytical argument covers arbitrary sample length.

## Originality — PASS, qualified
The principal comparisons were with Celebi et al. (2009), Little–Jones (2010/2011), and earlier patent quantile-filter disclosures, plus published indexed findings on median perturbations, trimmed means, and moving three-point median absolute deviation. The 2009 vector order-statistic work concerns computational approximations; the Little–Jones proof concerns one-input variation for a moving median; moving MAD uses a distinct three-window statistic. None of the inspected statements implies both exact sharp constants for the four-sample middle-two spacing or the separate dimension thresholds. General order-statistic results do not automatically identify the sharp norm of a *difference* between two ranks. Unindexed and inaccessible literature still presents a historical priority risk.

## Mathematical value — PASS
The middle-two gap is a natural four-observation local dispersion statistic resistant to extreme order values. Characterizing both within-signal variation and input-perturbation sensitivity identifies a genuine robustness distinction: the one-input coefficient saturates at 2 while the two-input coefficient saturates at 6. The sharp onset dimensions and explicit finite attaining witnesses make the fact useful when specifying stability budgets for local rank-based contrast detectors.

## Scientific limits
Only full, nonperiodic, unweighted windows of exactly four observations are addressed. The result is not an independent audit, a general moving-quantile theorem, or an exhaustive historical priority search.

Self-review: passed. Independent audit: not yet performed.
