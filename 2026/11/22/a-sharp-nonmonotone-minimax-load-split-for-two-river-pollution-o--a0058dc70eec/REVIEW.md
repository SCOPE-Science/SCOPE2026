# Scientific review

**Correctness — PASS.** The proof reconstructs the initial boundary condition, two BOD jumps, rate normalization and full infinite downstream domain. It maximizes each exact positive quadratic and supplies a global lower bound with strict uniqueness in both intervals \(0<q<1/3\) and \(1/3\le q<1\), including the switching equality. The standard-library checker passed 16,432 exact-rational assertions; these finite checks do not substitute for the proof.

**Originality — PASS, provisional.** The same-kernel published double-sag theorem proves the number of local maxima at fixed load ratios, but not which are globally worst or the fixed-total allocation minimizer. Jamal's 1986 thesis optimizes permitted wastewater loadings with a different tidal river objective, and the accessible 2014 multi-outfall paper predicts rather than optimizes sag. The classic general convexity and linear-programming literature is relevant but the inspected text does not explicitly give the two closed-form minimax branches. Full-text gaps remain for Liebman and Lynn (1966), Arbabi et al. (1974), and Bhargava (2007), so historical priority is **not certified**.

**Value — PASS.** River oxygen-deficit peaks are a meaningful water-quality invariant. The theorem supplies a complete unique-optimizer classification with two exact regimes, a sharp geometric separation threshold, two globally active worst-deficit locations in one regime, and a nonmonotone optimal load fraction. This is more informative than a single numerical load split or the known one-source sag formula. It remains an idealized model benchmark.

**Limitations.** Rates are restricted by \(k_r=2k_d\); no settling, nonuniform flow, background oxygen deficit, dilution or direct oxygen shock is modeled. The full source archive and historical priority require independent review. No experimental or field validation was undertaken.

Self-review: passed. Independent audit: not yet performed.
