# Mathematical review

## Correctness — PASS

The stated deterministic pressure reduction is obtained directly by solving the susceptibility transport equation and integrating recovery. For strictly positive infection seed, the final pressure is the unique positive zero of a strictly concave scalar function. The lognormal Stieltjes perturbations have the same nonnegative integer moments by the exact complex-Gaussian identity; smooth time jets then agree by ODE differentiation. Holomorphic uniqueness of the Laplace transform, isolated zeros on the positive axis and strict monotonicity of the unperturbed terminal pressure prove the generic-seed difference. The nonanalyticity statement follows from growth of lognormal moments and the analytic inverse-function theorem. The finite 18-interval lower estimate and Mills upper estimate prove the strict \(0.16056\) attack-fraction gap; the standalone `checker.py` independently verifies its conservative elementary arithmetic margins. All infinite quantifiers are proved analytically, not inferred from samples.

The result assumes unbounded positive susceptibility, the deterministic closed SIR fluid system, strictly positive initial prevalence, and constant transmission and recovery parameters. Approximate numerical final sizes are illustrations only. At the edge \(r=0\), at compactly supported moment-determinate laws, and for changed infection mechanisms the conclusions are not asserted.

## Originality — PASS (literature-bounded)

The closest same-model article, Izyumtseva et al. (arXiv:2608.22122v1), supplies the Laplace-transform model but its full text could not be read; its abstract does not state an all-order-moment alias, identical initial time jets or a quantitative separation. Miller (2012, PMCID PMC3506030), whose full-text Section 3.2 was inspected, gives a generic heterogeneous-susceptibility final-size relation but not these joint identifiability and lower-bound conclusions. Classical lognormal Stieltjes moment-indeterminacy is acknowledged rather than claimed as new. Muslim (arXiv:2608.04943v1) establishes finite-moment sufficiency for a different group-size transmission kernel, not failure despite equality of all susceptibility moments. Mohammed et al. (arXiv:2606.08693v1) consider mean-and-variance matched gamma/lognormal distributions, rather than same-all-moment laws.

Known finite-support moment-cutoff and incidence-timing results do not imply this unbounded-support, all-order nonidentifiability theorem. Searches of published research records and primary literature for lognormal/Stieltjes aliases, Laplace equivalence and all-jet/terminal-size reversals did not produce a logically covering statement. Neither retrieval failure nor this comparison proves universal novelty; the inaccessible main full text, older unindexed work and possible synthesis from classical results remain genuine risks.

## Value — PASS

Moment-based susceptibility models are natural tools for epidemic risk estimation. Here even the **complete** moment sequence and all local temporal derivatives fail to determine terminal epidemic burden, while an explicit, common-parameter construction guarantees a separation exceeding 16 percentage points. This establishes a meaningful boundary for moment/Taylor-based prediction that is absent on compactly supported, moment-determinate laws. It is more than a numerical alias or a reparametrization: the proof gives a robust generic-seed theorem, nonanalyticity mechanism and quantitative macroscopic witness. It does not imply that a complete measured time trajectory is nonidentifying.

## Closest literature, evidence and remaining limits

Relevant full text: Miller (2012), Section 3.2 and its final-size Laplace integral, https://pmc.ncbi.nlm.nih.gov/articles/PMC3506030/. Relevant public abstracts: Izyumtseva et al. (2026), https://arxiv.org/abs/2608.22122; Muslim (2026), https://arxiv.org/abs/2608.04943; Mohammed et al. (2026), https://arxiv.org/abs/2606.08693; Kleiber (2013), https://arxiv.org/abs/1301.1277. The full 2026 initiating preprint was unavailable for inspection, so possible appendices or same-model variants remain a priority risk. Independent scientific validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
