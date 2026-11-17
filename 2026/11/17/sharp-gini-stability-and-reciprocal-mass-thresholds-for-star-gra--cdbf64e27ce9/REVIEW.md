# Scientific review of sharp Gini stability for star-graph fusion

## Correctness
**PASS.** The global fit is continuous piecewise affine because the hub equation is strictly increasing and each leaf is scalar soft-thresholded about the hub. Every open-cell Jacobian is a single weighted block average plus unchanged coordinates, and every block size is locally realized with strict sign margins. The induced Gini norm is exactly a maximum over binary cuts by level-set decomposition. The cut ratio reduces to two endpoints in the number of selected untouched leaves by concavity of the proposed norm inequality, and the remaining cases yield the two explicit candidate factors. Algebra establishes the reciprocal nonexpansivity interval and the supremal envelope. Exact-rational tests and actual proximal witnesses support, but do not replace, these unrestricted arguments.

## Originality
**PASS, qualified.** The 2004 fused-lasso article, generalized-lasso paper arXiv:1005.1971, and graph-guided regularization paper arXiv:1005.4717 describe algorithms, sparsity/fusion geometry and generalized graph penalties. Their examined statements do not give the two-input complete-pair Gini constant, the edge-penalty invariance, or the reciprocal star mass interval. The closest accessible earlier quantitative claim is an exact Gini stability formula for weighted isotonic regression on chains. Weighted block averaging is shared, but that theorem is about a different nonlinear fitting map; the present star fusion result requires deriving all actual local proximal slopes and showing that each is attainable under arbitrarily unequal positive edge penalties. The possibility of an unindexed equivalent theorem or a straightforward transfer from isotonic methods remains a substantive priority caveat.

## Mathematical value
**PASS.** In a classic graph denoising model, stronger quadratic fidelity at a hub can create *more* pairwise-dispersion instability even though the fit remains well defined and nonexpansive in its objective's Hilbert geometry. The result gives a complete sharp mass tolerance interval for any star size, proves the independence of all positive edge-fusion weights, identifies concrete extremal perturbations, and discovers the five-leaf crossover of two competing high-contrast mechanisms. These are structural stability boundaries for a natural class of graph regularizers, rather than a single arbitrary numerical constant.

## Limits
Unweighted complete-pair Gini variation is not graph-edge variation. The leaf observation masses must be equal; the graph must be a star; strict positivity of fidelity and fusion parameters is essential for the stated open-cell realization argument. No claim is made about all trees or nonlinear loss models. No independent verification has been performed.

Self-review: passed. Independent audit: not yet performed.
