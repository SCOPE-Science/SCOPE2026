# Review of the neutral-feedback sine-map theorem

## Correctness

**PASS.** The claim is an exact reduction on the parameter surface \(\mu=1\), \(\delta=\beta+\gamma\), and its global quantifiers are checked without a numerical infinite-time inference. Direct substitution proves the translation \(W\circ F=W+\alpha\). The nonnegative two-coordinate Lipschitz matrix has two-step sup-norm \(s=\beta+\delta<1\), giving a unique continuous invariant phase graph and the stated uniform attraction. Since the first two coordinates are bounded after two steps, nonzero drift implies linear escape and precludes finite invariant probabilities. Irrational rotation gives the common projected time-average law, while Taylor's theorem bounds the statistical-mean remainder by \(3s^2/2\). At zero drift the leafwise scalar fixed-point equation is a strict contraction when \(s<1\); at \(w=\pi\), the equation \(r=\sin(sr)\) gives the sharp threshold and the supercritical leafwise pitchfork. The eigenvalue calculation explicitly retains the neutral full-space direction. The supplementary Python checker passed 400 drift instances, 100 contraction cases and six near-critical stability cases; none is used as a proof of a universal claim.

## Originality

**PASS within inspected evidence.** The 2023 defining article (DOI 10.3390/sym15040780, Equation (1) and Sections 2–6) treats numerical parameter transitions and network synchrony, but not the special neutral-feedback cancellation, exactly translating coordinate, globally attracting forced graph, invariant-measure obstruction, sharp scalar pitchfork or uniform phase-bias coefficient. The 2017 precursor by Mammeri (Equation (1), Theorems 1–4, Sections 2–3) has no linear feedback in its third coordinate and accordingly states boundedness and fixed-point stability of a different recurrence, not a translating invariant. General skew-product invariant-graph results are methodologically relevant but do not by themselves identify the source-specific cancellation or model-specific constants and stability boundary. The nearest indexed comparison about resonant rank collapse concerns a reciprocal-sine map, not the present recurrence. The statement is a conjunction of coupled claims for this particular parameter surface, not a claimed general invention of graph transforms. Equivalent or unindexed exact formulas remain a priority risk; independent publication-priority review has not occurred.

## Value

**PASS.** The source emphasizes feedback-driven transition among periodic, quasiperiodic and chaotic regimes without an analytic global classification at neutral linear feedback. The theorem identifies an exact nongeneric mechanism separating an unbounded physical phase direction from bounded driven coordinates, gives a globally uniform relaxation rate and a quantitative bias in time averages, and proves a sharp transition from leafwise uniqueness to multistability. The distinction between absence of a stationary probability in \(\mathbb R^3\) and existence of a projected quasiperiodic law is structurally useful for interpreting bounded numerical projections of an escaping map. This is not a generic parameter substitution or solely a numerical sample. Its relevance is restricted to the stated cancellation surface; no security claim is made.

## Closest literature and limitations

- K. Rajagopal, S. Kanagaraj, C. Volos and A. Karthikeyan, *Symmetry* **15** (2023), 780, DOI 10.3390/sym15040780: original model and numerical dynamics; exact special-surface results not stated.
- M. Mammeri, *Bulletin of Mathematical Analysis and Applications* **9** (2017), no. 1, 1–8: non-feedback precursor, boundedness and fixed-point analysis.
- T. Withers, *Invariant Graphs of Skew Product Dynamical Systems*, thesis (2017): general skew-product theory, different base and fiber class; contraction methodology is standard.

The result is conditional on \(\mu=1\), \(\delta=\beta+\gamma\), \(\beta>0\), \(\gamma\ge0\). Only the \(s<1\) region has an all-phase uniform graph theorem, and at \(s>1\) the pitchfork claim is leafwise at zero drift. The full 2017 PDF was available in extracted text; page-image preview was unavailable. Other equivalent literature may exist.

Self-review: passed. Independent audit: not yet performed.
