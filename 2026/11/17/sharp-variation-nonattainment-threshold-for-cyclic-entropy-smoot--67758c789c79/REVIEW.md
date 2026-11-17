# Review of the cyclic entropy-smoothed maximum variation theorem

## Correctness — PASS

The derivative of a shared-site-weight sliding log-sum-exp is a conditional probability average. For each pair of consecutive windows the cumulative-probability difference factors the first-difference operator through a strictly positive, column-stochastic matrix whose columns each occupy a circular arc of length equal to the window size. Telescoping proves the precise column sums. Integration proves global contraction. When the window exceeds half the cycle, all pairs of such columns overlap, forcing cancellation between positive and negative portions of every nonzero cyclic gradient; integration yields strictness for all finite input pairs. Two disjoint complete windows give equality when the cycle contains at least two window lengths, while a concentrating one-site pair yields the sharp supremum otherwise. The full-window case is constant. The independently reconstructed algebra was checked using exact rational Jacobian factorization and numerical secants from the standalone program.

## Originality — PASS, qualified

The smooth-maximum formula and its derivative are established in Nesterov's 10 January 2003 preprint (Section 4.1, Lemma 4). The accessible published finite-window morphology result treats truncated path min/max filters, not entropy-smoothed cyclic windows and not the strict nonattainment phase. Its max-filter contraction can imply the coarse nonexpansive bound after a standard randomized-maximum identity, so that bound alone is **not** presented as the novel contribution. The specific equality-versus-nonattainment classification, uniformly in positive site weights and temperature, was not implied by the inspected statements. The continuum one-input maximal-function BV theory and available morphological-pyramid abstract also do not state this equality problem. Search and access limitations prevent any claim of definitive historical priority.

## Mathematical value — PASS

The half-cycle geometric threshold is a complete natural classification for a smooth local maximum regularly used as an entropy-regularized surrogate of dilation: for shorter windows equality can occur with finite data, while for long-but-not-global windows each individual pair is strictly damped despite sharp global Lipschitz constant one. This distinction matters when inferring strong stability from nonexpansive estimates and is explained by a reusable positive-column-overlap mechanism rather than arbitrary small cases. It contrasts with instability results for nonlinear median-based filters and is not a renaming of the standard smooth-maximum derivative.

## Limits and source risk

The theorem is one-dimensional, cyclic, uses contiguous windows and globally shared positive site weights, and concerns a single pass. The derivative overlap argument does not yield a uniform strict contraction over unbounded data. The original Nesterov open preprint and the available full text of the relevant finite-window morphology result were examined in the material needed for comparison; older morphological-pyramid work was available here only through its abstract. A broader historical theorem about stochastic-order kernels could contain an equivalent statement; historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
