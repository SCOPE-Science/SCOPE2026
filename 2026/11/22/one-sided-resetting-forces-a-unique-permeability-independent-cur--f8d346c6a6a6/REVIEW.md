# Scientific review: One-sided resetting forces a unique permeability-independent current reversal at a biased membrane

## Correctness — PASS

The unique normalized solution follows from a positive Neumann source resolvent plus one explicitly derived homogeneous flux corrector. The directed interface algebra yields the exact current formula and strictly positive boundary traces. The monotonicity argument compares two hyperbolic-cosine weighted averages with the midpoint and is strict for **every** Borel law wholly supported in the open left/right semicircle. Endpoint limits establish precisely one transverse threshold in the competing-bias regimes, and no root otherwise. The uniform-source formulas integrate exactly. The standalone checker ran successfully with 877 diagnostic checks including independently discretized finite-volume boundary problems. Infinite-parameter statements rest on the analytic proof rather than finite experiments.

## Originality — PASS, qualified

Bressloff (2024, arXiv:2402.16403) already provides asymmetric membrane transmission and separately the unbiased resetting ring; Bressloff (2022/2023, arXiv:2211.12460) provides an asymmetric interval first-passage treatment. Previously published unbiased ring membrane-current tomography and entropy optimization results were compared at their theorem and proof levels: each has membrane bias \(eta=1\), where a one-sided source gives a **fixed current sign** rather than the phase transition proved here. Tucci et al. (2020, DOI:10.1103/PhysRevResearch.2.043138) treat transport/resetting gauge choices without this biased membrane. The checked exact statements do not imply the claimed all-source, bias-dependent unique inversion with permeability-independent threshold. The antecedent Green and interface techniques are credited and not claimed as discoveries. Residual publication-priority risk remains from broader implicit comparison theorems and one incompletely inspected screened-reset paper.

## Mathematical value — PASS

There are two naturally competing sources of directed transport: the membrane preference and frequent relocation to one semicircle. Their competition leads to a complete and sharp regime classification that is robust under arbitrary source singularity, with an exactly identified threshold independent of crossing conductance. This provides a usable boundary in experimental current-direction control and a clean counterpoint to symmetric-interface fixed-sign behavior. The contribution is a structural one-crossing theorem, not merely a computation for a special reset point.

## Closest literature and limitations

The primary models are Bressloff (2024), arXiv:2402.16403, and Bressloff (2022), arXiv:2211.12460. The result applies to the **continuous physical membrane flux only**, not jumps assigned winding during resetting, and requires fixed positive bias/permeability, fixed homogeneous diffusivity and a reset law fully supported in an open semicircle. It does not establish current-reversal bounds for sources spanning both sides. Some claims may follow from a broader, as-yet-unlocated transport comparison. Independent scientific audit is not complete.

Self-review: passed. Independent audit: not yet performed.
