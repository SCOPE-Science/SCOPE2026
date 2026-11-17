# Scientific review: a rare-return paradox for the founding voter

## Correctness — PASS

The two disagreement probabilities satisfy the explicitly derived linear generator ODE. Integrating it gives the expected founder flip count, and the terminal-state identity gives the exact mean upward count. For the first-return probability, the total-mutant embedded symmetric birth-and-death chain has gambler’s-ruin probability \(1/k\) to reach \(k\) before extinction. Its quadratic stopped potential has generator bounded above by minus the current mutant count, controlling the integrated potential founder-return intensity. The resulting finite-size probability bound forces \(N_n\to1\) in probability, while the mean tends to two. Direct labelled generator calculations checked \(n=2\) through \(9\) and an independent return-event reduction checked \(n=3\) through \(17\). These checks support, but do not replace, the all-size proof. The theorem is not about attempted self-updates or arbitrary initial densities.

## Originality — PASS (qualified)

The priority comparison was statement-based. Ben-Naim, Frachebourg and Krapivsky’s historical paper develops voter-model opinion-change statistics, including a complete-graph mean-field calculation, but its asymptotics are for different population/time regimes. Pickering and Lim’s full complete-graph spectral calculation gives occupation times of total positive-population states, not the flips of a distinguished initial founder. Sood, Antal and Redner provide the classical martingale fixation result. The nearest recorded result, *Exact hub persistence on clique bouquets and its size-biased blade law*, **does** cover the zero-founder-flip probability even on the complete graph. That probability is acknowledged as existing work and is explicitly excluded from the originality claim. None of the inspected full texts states or implies directly both the exact tagged mean count and vanishing second-flip probability together with a large conditional return count. Possible older unindexed coverage remains a priority risk; database absence alone is not a novelty proof.

## Mathematical value — PASS

The phenomenon is a meaningful finite-system singular limit: almost every founder changes opinion once, yet rare founder-revival trajectories contribute an extra unit to the average, and the mean number of upward changes conditional on any revival grows at least on the order of \(\sqrt n\). The proof identifies an explicit finite-size stopped-potential mechanism that separates typical and mean behavior in an archetypal neutral interacting system. This contributes a natural path statistic not provided by standard fixation probability or consensus-time calculations. The proved probability bound is not claimed optimal, and the full flip-count distribution is not determined.

## Sources and remaining limits

Primary works and the closest overlapping mathematical record are cited in `RESULT.md` and indexed with inspected sections, direct relevance and residual risks in `AUDIT.json`. No publisher-restricted full text was used as a negative coverage claim. There has been no independent external audit.

Self-review: passed. Independent audit: not yet performed.
