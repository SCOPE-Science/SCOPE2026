# Scientific review

## Correctness

**PASS (same-model).** The tested algorithms are precisely the source's DR and RD methods with its reported RSHK initialization. Independent componentwise substitution yields the exact rational expressions \(D_K(t)\) and \(R_K(t)\). After changing variables to \(Kt\) and \(K^3t\), uniform bounds on the discarded terms and both tails prove sharp maxima \(27/256\) and \(1/4\), not just pointwise limits. Positive maximizing parameters exist because the gain functions vanish at both boundaries. The embedded checker returned `VERIFY_OK 4430` (4,424 exact-rational assertions and six floating-point convergence checks). No numerical experiment was used as a substitute for the proof.

## Originality

**PASS (same-model, qualified).** Xu's source specifies the rules and acknowledges residual spikes, but the paper's two-mode analysis and experiments do not quantify sharp worst-startup conditioning exponents for the pair. Related asymptotic-rate papers study BB iteration over many steps, while published safety-frontier results analyze objective/gradient monotonicity and include a potentially overlapping repeated-long-step mechanism. The substantive contrast here is the joint, normalized DR versus RD amplification law with distinct optimizing initial scales; it is not an unmodified restatement of the algorithms or of one-step step-size ordering. A related published mathematical record and some contemporary BB full texts could not be inspected in full; independent priority judgment is necessary.

## Value

**PASS (same-model).** The source's principal numerical examples show pronounced spikes on ill-conditioned systems. This finding supplies sharp, dimension-minimal conditioning exponents for those early spikes, and distinguishes the two rules even when they share the same warm start and the shorter second step is always no larger than the longer one. The large difference matters for worst-case residual thresholds, finite-range arithmetic and safeguarding decisions. It is not a claim about typical data or ultimate convergence superiority.

## Closest literature and limitations

Most relevant: Xin Xu, arXiv:2611.02743v1, full publicly accessible primary text, especially definitions (8), (14), (16), (17), two-mode discussion and plotted spikes. Other references include Yang–Yuan arXiv:2608.07839 (asymptotic rates), arXiv:2607.21579 (BB quadratics), and published mathematical records on Cauchy repeated-step safety and BB-interval objective growth. The older general methods may imply parts of the long-step calculation; historical novelty depends on the two-rule asymptotic comparison, and full inspection of inaccessible related material remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
