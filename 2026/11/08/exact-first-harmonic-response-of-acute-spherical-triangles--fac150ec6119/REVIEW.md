# Scientific review

## Correctness — PASS

The claim is an exact two-dimensional spherical integral. Normalized pair-distance density is \(\sin d/2\); both base angles are acute only within a longitude wedge, and the third-angle inequality yields an explicitly integrated latitude cutoff. The second term in that integral is reduced to two elementary fixed-range integrals, giving both the known unweighted baseline and the new weighted moment \((\pi-2)/64\). The dipole identity follows exactly (not perturbatively) by antipodal cancellation and rotational tensor averaging. The pinned and three-iid von Mises–Fisher coefficients follow from properly normalized likelihood expansions. The supplied standard-library verifier independently checks both moments, nonzero-dipole probability, and pinned derivative. Numerical tests do not substitute for the analytic steps.

## Originality — PASS, provisional

Uniform angle-type probabilities are classical, including Maeda's 2008 classification: the uniform acute probability is **not** a novel assertion. The 2013 Li–Cooper–Eum paper was inspected in its relevant full sections: §§2.7–2.8 give an unweighted acute-triangle integral and approximate the uniform probability, while §§3.1–3.5 numerically analyze a von Mises–Fisher distribution with one vertex pinned at the mean. They do not evaluate the cosine-weighted uniform moment, the full dipole family, or the exact pinned concentration derivative. The closest retrieved mathematical database findings concern Euclidean planar triangle moments or projections of polyhedra and do not imply the claimed spherical weighted moment. Maeda's complete article and Le's earlier cap-density article were not accessible in full; historical priority remains provisional, and the relationship to these sources warrants human examination.

## Mathematical value — PASS

There is a concrete, independently motivated nonuniform probability question in the 2013 spherical-triangle study, where the onset of the pinned probability curve was only estimated numerically. One exact weighted spherical moment supplies the onset coefficient and, by a genuine symmetry cancellation, determines the *entire* (not merely leading-order) acute probability under a natural first-harmonic family of nonuniform densities. The unconditional uniform probability already being known makes the weighted response the substantive point. This exact, parameter-uniform probability law is a structural bridge between classical geometric probability and directional statistics, not a gratuitous parameter substitution.

## Limitations and historical risk

The Fisher expansions are local at zero and do not prove global monotonicity. The exact dipole law is specific to the first-harmonic family with \(|\varepsilon|\le1\). Historic shape-density literature and Maeda's complete primary source were not retrieved; no claim of established worldwide priority or independent validation is made. The relevant 2013 paper's text was inspected in full, while only abstracts and metadata were available for the earlier Maeda and Le papers.

Self-review: passed. Independent audit: not yet performed.
