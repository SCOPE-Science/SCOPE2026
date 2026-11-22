# Review: exact Szász–Kantorovich BV error and extremal jump retreat

**Correctness — PASS.** The operator, extension convention, BV domain and interval norm are explicit. Independent integration and a Gamma–Poisson computation agree. The exact identity \(\mathbb E|T-s|=2s p_m(ns)\), the Gamma overshoot recurrence, and strict cell concavity prove the finite sharp formula. Pairwise residual sign changes prove the entire norm-equality class. Stirling and two-sided Gamma moderate-deviation bounds establish the asymptotic constant and logarithmic displacement. The numerical checker is corroborative only.

**Originality — PASS (with historical-priority risk).** The full 2002 Walczak operator paper and 2009 Nowak–Sikorska-Nowak pointwise paper were inspected, as was the 2011 Acar–Gupta–Aral full text. Their actual claims treat different approximation questions and do not imply this exact BV-to-\(L^1\) finite-interval sharp constant, complete extremizer class or worst-jump displacement. Published comparison results about other positive approximation kernels, and Poisson smoothing on the circle, likewise have inapplicable hypotheses. The exhaustive historical literature is not searchable; unindexed equivalent formulas remain the principal originality risk.

**Value — PASS.** This is a canonical positive approximation operator, not a tailored example. The result computes a natural exact operator error, gives an efficient root-based finite evaluation algorithm, and explains the previously hidden \(\sqrt{\log n/n}\) scale at which worst discontinuities retreat from a hard observation boundary. These are substantive error-budget and boundary-rigidity facts, independent of a downstream theorem.

The claim excludes general kernels, arbitrary continuation conventions, and global uniqueness of the winning finite cell. The 1983 Totik article is historically relevant but its full body was not inspected. No independent priority certification is asserted.

Self-review: passed. Independent audit: not yet performed.
