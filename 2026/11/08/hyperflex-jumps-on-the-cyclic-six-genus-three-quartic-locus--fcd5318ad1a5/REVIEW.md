# Scientific review: hyperflex jumps in the cyclic-six quartic family

## Correctness (C): PASS

The claim is over \(\mathbb C\), for every smooth parameter \(r\ne\pm2\), and distinguishes three mutually exclusive cases. The Jacobian calculation excludes singular parameters; the only point at infinity has tangent contact four; every point with \(X=0\) has contact exactly three; and all remaining possible hyperflexes are determined by two explicit contact equations. The polynomial resultant and Gröbner-basis identities are checked by an executable symbolic verifier. The exceptional polynomial is squarefree, its roots avoid all degenerate cases, and each gives exactly six additional hyperflexes. The unique \(r=0\) case gives exactly three additional hyperflexes. The classical inflection-weight total of \(24\) determines ordinary-flex counts. There is no numerical extrapolation or unproved infinite case. The isomorphism and full automorphism-group criteria are taken from the cited primary literature.

## Originality (O): PASS with residual priority risk

Closest published work is Ohashi–Kudo–Harashita, arXiv:2111.09777 (first posted November 18, 2021), which fixes the same quartic family and determines its smoothness, automorphism groups, isomorphism parameter, and Hasse–Witt properties. The relevant preprint sections (§§1–2, theorem statements, and abstract) were examined; its scanned text had no hyperflex/inflection result. This work is not a new quartic family or a new classification of automorphism groups.

Girard–Kohel, arXiv:math/0603555 (2006), gives a general classification of the high-hyperflex strata of genus-three moduli, explicitly including the one-dimensional stratum \(Z_4\) with seven hyperflexes. Its relevant §§2 and 4–6, Table 1 and the \(Z_4\) model were inspected. That broader modular classification is a serious prior comparison but does not print the two cyclic-six parameter values or the \(1,4,7\) flex-count trichotomy. The new polynomial intersection calculation is needed to extract the statement. Lercier–Ritzenthaler–Rovetta–Sijsling, arXiv:1403.0562 (2014), supplies the automorphism-type families and \(r^2\) parameter equivalence but not the flex counts. Targeted literature searches did not identify the same statement under common aliases. Absence of a search match is not proof of priority: unlocated older intersections of Vermeulen's strata with automorphism strata remain a risk.

## Mathematical value (V): PASS

The family is a canonical, one-dimensional automorphism stratum in genus-three moduli, not a parameter subset chosen to produce a numerical curiosity. Hyperflex counts are intrinsic Weierstrass-weight data and define meaningful high-contact moduli strata. The theorem locates **exactly two isolated isomorphism classes** at the natural intersection of the cyclic-six stratum with the seven-hyperflex stratum, while simultaneously classifying every other fiber and its complete ordinary/hyperflex profile. This supplies a usable explicit equation for an otherwise implicit intersection of previously studied moduli loci. No general theorem for arbitrary quartics is required for the local classification to be meaningful.

## Limits and independent status

Over positive-characteristic fields the same elimination need not control flex weights, and no such extension is asserted. Broader modular invariant algorithms may recover these values by nontrivial specialization, so historical novelty is not guaranteed. This review confirms the mathematical statement with reproducible symbolic checks, but is not an independent external assessment.

Self-review: passed. Independent audit: not yet performed.
