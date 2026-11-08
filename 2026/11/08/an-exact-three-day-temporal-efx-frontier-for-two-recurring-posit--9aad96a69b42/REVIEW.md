# Self-review

## Correctness — PASS

The claimed quantifiers and boundary cases have been checked independently of the finite verifier. The compulsory first-day split follows from positive values. Conditioning on that split, precisely four day-2 assignments exist. The cross branch caps all day-3 outcomes by \(C=(H+2L)/(2H)\), including the both-to-one subcase. Repeating day-1 assignments gives a cap \(2L/H\le C\) for \(H\ge2L\); assigning both to the day-1 high-value holder gives a cap \(L/(2H)\le C\); assigning both to the other holder gives a cap \(D=H/(H+L)\). Explicit schedules attain each branch without a later prefix violation. Algebra gives the unique crossover \((3+\sqrt{17})/2\) and minimum \((\sqrt{17}-1)/4\). Separately, alternating high/low recipients gives exact EFX at every prefix if \(H\le2L\). Three-day failure therefore excludes all later exact solutions for \(H>2L\). The standard-library checker exhaustively evaluates 64 three-day schedules at each of 21 rational ratios (1344 paths), and checks nine-day exact reachability; finite tests are not substituted for the real-parameter proof.

## Originality — PASS, qualified

The closest source is Choi and Li (arXiv:2601.12835), which *already* proves a three-day identical-round TEFX impossibility for values \(\{0,1,3\}\), with an argument reducing to \(\{1,3\}\). The present theorem does **not** claim novelty for that counterexample. Its precise contribution is the *whole positive continuous two-value* feasibility threshold, the *optimal three-day approximation* including two competing strategies, the crossover and the sharp worst-case uniform guarantee. Their later paper arXiv:2607.17224 includes a general \(1/2\)-TEFX identical-day construction and value-dependent lower bounds for other broad domains, but no exact three-day frontier in the inspected full text and appendix. Elkind et al. (arXiv:2410.14593) and Cookson et al. (arXiv:2410.23416) study broader temporal guarantees and distinct per-day versus cumulative criteria. Semantic research-record and earlier work comparisons did not reveal a directly implying statement; that absence is evidence of noncoverage, not a mathematical uniqueness certificate. Residual risk: unindexed equivalent two-good three-day analysis.

## Mathematical value — PASS

This is the smallest natural repeated two-good schedule in which exact TEFX can fail, and the problem is explicitly motivated by the 2026 identical-day approximation gap. The exact boundary \(H/L=2\) and the sharp factor \((\sqrt{17}-1)/4>1/2\) are motivated invariants, not arbitrary finite enumeration. The switch between balanced daily splitting and deliberately bundling one day's goods explains a substantive tradeoff in maintaining cumulative fairness. The all-horizon exact-feasibility classification and sharp worst-case three-day performance improve the understanding of a canonical structured market, without claiming a general fair-division algorithm for arbitrary goods or horizons.

## Sources and limitations

Primary full texts and relevant proofs/appendices examined: https://arxiv.org/abs/2601.12835, https://arxiv.org/abs/2607.17224, https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p676.pdf, https://ebadian.org/preprint/temporal.pdf, and https://olinarr.github.io/files/publications/pdf/IgarashiEtAlAAAI2024.pdf. The exact approximation formula is for three days; beyond that, only the exact feasibility criterion is established. Equivalently phrased unindexed results may exist. Independent external validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
