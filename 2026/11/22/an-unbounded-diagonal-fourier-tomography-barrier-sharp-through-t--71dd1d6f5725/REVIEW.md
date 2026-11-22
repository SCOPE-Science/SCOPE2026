# Scientific assessment

## Correctness

**PASS.** The lower bound follows for every \(n\ge4\) from an explicit \(\lfloor(n-2)/2\rfloor\)-dimensional cube of commuting triangulation flips; the alternating signed sum annihilates every lower-degree diagonal monomial. The two parity classes give actual positive probability distributions, not merely a formal linear dependence. The exact upper bounds for \(4\le n\le10\) are proved by explicit exhaustive finite matrices: two independent enumeration paths and two independently organized mod-two elimination routines give full row rank. Full rank modulo two certifies a nonzero integer determinant and therefore full rank over the reals. The Boolean monomial and Walsh evaluation spans agree over the reals. Both packaged Python verifiers were executed successfully. The all-size upper bound is not proved and not claimed.

## Originality

**PASS under bounded comparison.** The most directly relevant prior full texts are Devadoss et al. (arXiv:0903.2848) for the associahedral structure, Dochtermann (arXiv:1503.06243) for its face ring and face enumerations, and de Loera et al. (DOI 10.4171/DM/4) for the affine span of a different triangulation-incidence embedding. Their inspected theorems do not state or imply the minimum degree needed to identify arbitrary probability distributions from *joint diagonal observations*: the face counts are not ranks of the face/facet incidence matrix, and affine-span results do not determine its higher interaction-degree saturation. Searches also considered equivalent phrases such as face–facet incidence rank and Boolean Fourier interpolation. The remaining risk is an unindexed historical description of the same higher-incidence ranks or a general theorem from which the finite cutoffs follow.

## Mathematical value

**PASS.** The first cases of a natural, nonparametric inverse problem are resolved, including a growing all-size information-theoretic lower bound and exact sharpness in dimensions reaching 1,430 triangulations. The obstruction is structurally motivated by independent local flips and provides explicit observationally identical probability measures. The upper bound requires a substantive full-rank verification, not just Catalan counting or one-feature discrimination. These values calibrate the number of simultaneous diagonal questions required for arbitrary-mixture recovery on associahedra; the open larger-polygon upper bound is a meaningful next question.

## Limitations and comparison risk

Only \(4\le n\le10\) have proved matching upper bounds; conditioning and all intermediate real ranks are not calculated. The closest full texts were compared by the actual mathematical objects and conclusions, but indexing and historical-priority searches cannot prove global uniqueness. No independent human or external mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
