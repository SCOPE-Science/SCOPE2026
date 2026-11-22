# Mathematical review

## Correctness — PASS

For a uniformly random height ordering of \(K_{a,b}\), the minima count is the first monochromatic run length and the maxima count is the last. Gap moments and a two-dimensional beta integral give the exact mixed moment. The monotonicity claim is established by a rational difference identity and a symbolic positive-coefficient polynomial after the domain substitution \(a=u+3\), \(b=u+3+v\). The remaining case \(a=2\) has a seven-coefficient positive polynomial; \(a=1\), balance positivity, the negative tail and the square-root scaling are treated separately. Executing `python verify.py` checks 2,061 exact assertions and the positive-coefficient certificates. Tests alone are not the proof; the displayed identities give the all-parameter argument.

## Originality — PASS, with historical-priority risk

The full primary paper of Baldi, Rinott and Stein (1989) addresses marginal extrema statistics and a normal approximation, especially on regular graphs, rather than the mixed extrema-count transition of unbalanced complete bicliques. The full arXiv paper of Burdzy and Pal (2016) studies labelings with restricted peak configurations, rather than this mixed covariance law. Known general pairwise extrema formulas can imply the rational covariance expression by summation, but their statement does not supply the strict one-crossing result or the square-root imbalance boundary. The first/last homogeneous-run formulation was also searched. No explicit stronger theorem or tabulation settling this exact sign classification was identified; an overlooked older equivalent boundary-run analysis remains possible. The conclusion does not assert independent priority certification.

## Value — PASS

The balanced regular biclique has positive peak–valley covariance, but a sufficiently unbalanced biclique has negative covariance. The theorem resolves the complete integer phase diagram by an all-size monotonicity certificate and identifies the surprising \(\sqrt a\) rather than linear imbalance scale. This is a structural dependence boundary for a natural, classical random-labeling statistic; it is not a lone numerical case or an arbitrary derived invariant.

## Limitations and references

The result is restricted to iid continuous heights and complete bipartite host graphs. The first-order cutoff does not decide the sign in the microscopic \(b-a=\sqrt a+O(1)\) window; the exact covariance identity does. No independent validation or exhaustive historical-priority proof has been performed. Primary sources: P. Baldi, Y. Rinott and C. Stein (1989), *On the Distribution of the Number of Local Minima of a Random Function on a Graph*, and K. Burdzy and S. Pal (2016), *Twin peaks*, arXiv:1606.08025v1.

Self-review: passed. Independent audit: not yet performed.
