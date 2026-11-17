# Mathematical review: empirical-quantile Winsorization

## Correctness (PASS)
The complete proof uses an exact coordinate-replication lemma with an independently checked multiplicity/cut argument; the coarea extension covers all real increments. The strict-order-chamber computation is exhaustive over all rank orders, line-segment integration covers two-input global stability, and rank-pivot perturbations attain the bound. No finite enumeration is substituted for the unrestricted proof. Exact rational diagnostics cover 2,352 complete multiplicity cases, 165 rank-pair cells and sharp witnesses, and 10,800 pairs.

## Originality (PASS, qualified)
The primary full text of Dey et al. (2012, arXiv:1211.4262v1) treats robust control charts and Winsorized variance, not a two-input Gini seminorm of the entire vector map. Bieniek (2014) proves trimean bias bounds via projection; Bieniek's 2016 Winsorized-mean bias paper was available only through an abstract and publication record, and this access limitation remains a risk. Relevant previously published statements about sorting, sample Gini dispersion and Gini–Greenwood dependence address different maps or statistical functionals; the source comparisons found no implication of this exact deterministic constant. Database searches and comparisons are not a proof of priority.

## Value (PASS)
Rank-capped Winsorization is natural in robust statistics. The result supplies exact perturbation sensitivity, complete nonexpansivity thresholds, attaining inputs, a structural multiplicity formula valid for arbitrary replication maps, and a striking dimension-linear amplification law for a fixed trimming fraction. It distinguishes one-input dispersion control from two-input robustness and provides a sharp stability baseline for pairwise-dispersion preprocessing.

## Residual scientific limitations
The result is only for complete-graph unweighted Gini variation and strict integer empirical quantile thresholds. No multivariate or general weighted-graph claim is made. Unindexed historical equivalents, notably in older statistical functional and deterministic resampling literature, remain possible; the 2016 Winsorized-bias paper's full text was inaccessible.

Self-review: passed. Independent audit: not yet performed.
