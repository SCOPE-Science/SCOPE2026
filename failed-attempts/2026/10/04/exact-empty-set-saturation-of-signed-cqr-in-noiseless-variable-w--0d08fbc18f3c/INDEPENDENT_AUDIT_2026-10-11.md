# Independent mathematical audit

## correctness

PASS

For noiseless Y=c(X) and endpoints c±W, signed conformal scores satisfy E_i=max(-W_i,-W_i)=-W_i. The empirical quantile index k=ceil((1-alpha)(m+1))=m+1-r yields correction -W_(r) with r=floor(alpha(m+1)). Then the displayed lower endpoint exceeds the upper exactly when test W<W_(r), whereas otherwise the true center is covered. For iid continuous widths the rank of the test among m+1 is uniform, hence empty probability r/(m+1). Conditional on F(W)=u, the number of calibration widths below W is Bin(m,u), producing coverage P(Bin(m,u)>=r); LLN gives the 0/1 threshold for u≠alpha. Checked the actual verifier and reconstructed exact rank identity for m=99, alpha=.1. There is no finite-to-infinite inference gap in these standard calculations.

## originality

FAIL

The final formulas are a direct specialization of the original CQR construction (Romano, Patterson, Candès, arXiv:1905.03222 equations (14)-(16) and Appendix A) and its standard distinct-score exchangeability/rank argument. Inserting exact noiseless center and fitted positive symmetric widths gives E=-W in one line; reversing order yields -W_(r), and event 'empty' equals event 'not covered', so Appendix A's exact uniform-rank law already fixes r/(m+1). Conditional-binomial tail is the elementary order-statistic conditional rank distribution and its step limit is the ordinary binomial law of large numbers. Although the paper does not use an 'empty CQR output' label, the required implication-based originality bar rejects renaming a direct specialized rank corollary as a new result. A full inspection of source's CQR definitions and rank lemma supplies decisive prior coverage.

## value

PASS

The concrete construction motivates a practical warning: signed CQR may return an empty interval even with an exact noiseless center, while globally attaining its advertised nominal miscoverage concentrated on low-width test points. An explicit conditional profile offers a clear stress test. This motivation makes the example pedagogically and methodologically useful, although it is already implied by the foundational source, so it fails originality rather than correctness or potential relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
