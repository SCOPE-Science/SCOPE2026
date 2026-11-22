# Scientific review

## Correctness — PASS

The exact normalized pulse equations reduce to a two-mode positive exponential response whose three invariant combinations are \(A_\theta=a+\theta d\), \(D=b+e\) and \(B=ab\). Positive rates force distinct modes with positive weights, so the positive variance \(y_2-y_1^2\) guarantees non-singular three-sample Prony reconstruction. For fixed \(D,B\), the identity \(\partial_A W(t)=-(W*W)(t)<0\) proves that one selectively altered reading identifies the remaining combination without local-only assumptions. Explicit algebra recovers all four original rates. The complete one-condition positive fiber is an open interval; invariance of domain proves that any three fixed scalar measurements are insufficient. These are analytic arguments for all positive parameters, not extrapolations from finite tests. The included high-precision executable checks 150 parameter sets and 2,250 assertions; its numerical precision does not replace the proof.

## Originality — PASS, with priority risk

Pont (2024), McKnight et al. (2024), and Sakata et al. (2020) motivate water–sediment exchange and condition-dependent eDNA loss but do not prove this two-condition finite-measurement identifiability result. Meshkat et al. (2014) already establish identifiability combinations for one-output linear two-compartment systems, and Prony's two-exponential recovery is classical (Cuyt and Lee 2018). Those are acknowledged ingredients; the precise four-reading selective perturbation theorem is not claimed in their inspected materials. Broader linear-compartment identifiability theory and the older extra-input literature (Godfrey, Jones and Brown 1980, abstract accessible) could imply or contain a specialized analogous result; absence of a match is not a proof of priority. The statement and implications were also compared to relevant research records and accessible prior findings. No directly covering result was found in those comparisons.

## Value — PASS

The biological motivation is the otherwise confounded interpretation of aqueous eDNA persistence as degradation versus temporary sediment storage. The theorem gives a *complete minimal intervention/measurement rule* rather than an arbitrary isolated numerical parameter: it proves exactly why one condition fails, describes every indistinguishable positive parameter set, gives a positive-parameter global reconstruction with three-plus-one readings, and proves that no fixed design with fewer total scalar measurements can succeed. It is useful as an identifiability benchmark for deciding whether a selective biochemical microcosm intervention could resolve exchange from degradation. Its idealized selectivity and noise-free assumptions limit any direct field prescription.

## Closest literature and limitations

The most direct antecedent is Meshkat et al. (2014) on identifiable combinations of linear two-compartment models. Prony reconstruction predates this result; an exact finite design is its application. Pont (2024) discusses physical transport with water–sediment exchanges; Kelleher et al. (2013) and Dallan et al. (2023) discuss different river-transient-storage inverse problems. The intervention must genuinely affect *only* aqueous degradation; realistic biological treatments may violate this. Other risks include nearly merged modes and nearly identical intervention levels, unknown gain and initial storage, and unresolved historical equivalence to some general compartment design theorem.

Self-review: passed. Independent audit: not yet performed.
