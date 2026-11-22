# Scientific review: finite-spacing persistence benchmark

## Correctness — PASS

The result uses the two-state transient block of the explicitly stated discrete-time catastrophe-then-colonization model. The crucial identity is \(\det((1-r/2)I-M)=r\{rq-c[2-r-(4-3r)q]\}/4\). Its sign can be compared to the Perron eigenvalue because the other eigenvalue is strictly below \(1-r/2\) at every positive finite distance. Reduction to \(q^{k-1}(2-r-(4-3r)q)\) gives a complete one-maximum/one-crossing classification, including tangency, strict inequalities, and the limit at infinite separation. The exact-rational and numerical diagnostics in `verify.py` pass 12,532 checks; the proof, rather than bounded enumeration, supplies the universal quantifiers. The model parameters and boundary cases are explicit.

## Originality — PASS relative to inspected evidence, with residual priority risk

Wagner, Ross and Possingham's accessible complete preprint (arXiv:math/0309255) supplies the model and quasi-stationary eigenvalue objective, not the complete finite-versus-infinite parameter threshold, unique critical decay ratio, exact intermediate bounded improvement window, or tangency classification proved here. A separate published mathematical result on *mean-persistence reserve spacing* uses a continuous-time common-fatal-catastrophe generator and compares mean versus tail optima; its statements do not imply this theorem for the discrete-time single-or-double catastrophe matrix. Shanks, Grantham and Carr (2003) discuss dispersal-distance-based siting empirically, not this eigenvalue classification. Blowes and Connolly (2012) describe reserve-spacing transitions for a different stochastic population growth/covariance model, but inaccessible full text prevents a complete exclusion of broader mathematical coverage. Searches and implication comparisons are specified in the accompanying structured audit. No claim of exhaustive historical priority or independent certification is made.

## Value — PASS

The source model's illustrative persistence-versus-distance curves can appear almost flat at large distance. The new exact inequality distinguishes a genuine finite-spacing benefit from an unattainable limiting supremum, proves that the beneficial region can be an isolated bounded distance window, and locates a sharp critical parameter for the onset/disappearance of that window. These are operationally interpretable structural boundaries of a named metapopulation model, not an arbitrary parameter-table entry or merely an eigenvalue recalculation. They make precise when optimizing over finite spacing is mathematically well-posed. The idealized baseline remains unsuitable for direct reserve placement without calibration, finite-horizon analysis, and model validation.

## Evidence limits

One highly relevant 2012 article was inspected only at abstract and bibliographic level after open-access routes failed; a full-text institutional attempt was unavailable. This is recorded as residual priority risk. Related general matrix inequalities explain proof tools, not the particular sharp ecological phase boundary. No external scientific validation was performed.

Self-review: passed. Independent audit: not yet performed.
