# Scientific assessment: three-regime two-arm colonization layout

## Correctness — PASS

The model assumes six permanently available habitat sites on two positive-length independent outward-only chains and independent rate-\(\lambda\) exponential stage clocks. For every \(T>0\) and \(R\ge0\), the exact objective is equation (1) in RESULT.md. The proof exhausts all three unordered arm splits, reconstructs exact Poisson occupancy counts and at-least-one-terminal reliability, and derives adjacent objective differences from unnormalized finite sums. Each of the four polynomial identities is verified by independent rational-polynomial checker arithmetic; the strict threshold ordering is an all-positive coefficient certificate. Tie cases, positive-parameter boundaries and first feasible interior layout are explicitly resolved. The checker passed 124 assertions. This does not certify applications beyond the model.

## Originality — PASS, with residual historical-priority risk

Searches of published mathematical statements by sequential Poisson colonization, two-arm Erlang stages, endpoint reachability, weighted occupancy and exact six-site allocation found no statement or stronger implication covering the two critical thresholds or the strict intermediate optimal layout. The closest Hock–Mumby paper formulates path reliability, whereas Seymour–Altermatt measure network topology and colonization. The closest indexed published mathematical comparisons address either extinction-time optimization of colonization **rates**, static habitat survival/connectivity, or stochastic terminal reachability without this two-objective finite-time site allocation. Those hypotheses and decision variables are not interchangeable with the present claim. Residual risk: classical redundancy-allocation and network-reliability literature could contain an equivalent finite-design result; searches and full-text comparisons cannot prove global novelty.

## Value — PASS

The count of colonized sites and probability of reaching a critical refuge are conflicting ecological-network objectives. This theorem is the complete smallest nontrivial two-arm allocation in which a third layout exists, and proves—not merely numerically suggests—that all three layout classes each become uniquely optimal for a nonempty range of a meaningful refuge-credit weight at **every** positive deadline. The exact thresholds describe precisely when a marginal change in conservation emphasis alters integer network geometry. It is a small idealized structural benchmark, not an empirical claim or a generic consequence of merely counting the feasible layouts.

## Limits and closest comparisons

Seymour and Altermatt (2014, DOI 10.1002/ece3.1020): full-text article sections, environmental relevance of dendritic colonization; no equivalent reward threshold. Hock and Mumby (2015, DOI 10.1098/rsif.2015.0013): full-text article sections, stochastic path reliability and route ranking; no finite-horizon occupancy-versus-endpoint layout optimum. Related published exact results on three-patch directional extinction and static refuge connectivity use different processes and rewards. A close historical analogue is El-Neweihi, Proschan and Sethuraman (1986), *Optimal allocation of components in parallel–series and series–parallel systems*, DOI 10.2307/3214014. Its abstract describes component-allocation reliability optimization but complete text was inaccessible. No inference of whole-document noncoverage is made. General reliability allocation literature remains the primary unresolved historical-priority risk. The result does not infer real-world corridor superiority under competition, extinction, changing rates or dispersal distance.

Self-review: passed. Independent audit: not yet performed.
