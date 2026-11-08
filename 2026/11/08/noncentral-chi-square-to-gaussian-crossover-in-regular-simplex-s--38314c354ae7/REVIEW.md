# Self-review: noncentral regular-simplex section fluctuations

## Correctness

PASS. For generic affine sections of the regular simplex, exact mixed-subset counting gives every face count as a polynomial in the number of vertices on one side of the section. A Haar normal is exactly a centered Gaussian vector divided by its Euclidean norm, so the count has an exact studentized moving-threshold representation. The empirical threshold expansion, including the sample standard deviation term, yields the influence function and corrected variance \(v(c)\). Taylor expansions of the face-count polynomial yield all three claimed joint weak limits. The \(t=h/n\) coefficient is \(1/(2^j j!)\), checked both algebraically and by the standalone program. No finite test is used in place of the Gaussian central limit theorem or empirical-process control.

## Originality

PASS under the inspected sources, with historical priority provisional. The two closest published central-section notes already establish the \(t=0\) chi-square face-vector law; the new claim explicitly excludes priority for that case. König's 2023 article treats maximal noncentral section **volume** rather than invariant-random **face counts**. Brandenburg–De Loera–Meroni's slicing-chamber theorem and De Loera–Lopez-Campos–Torres' attainable-count results do not give fixed-offset random fluctuations. Their statements, including the general edge-crossing principle, do not imply the corrected Gaussian variance or the noncentral \(t=h/n\) transition without additional analysis. Broad and parameter-specific published-finding corpus searches returned central-section notes but no positive-offset statement. A differently indexed statistical functional limit, or older unpublished geometry calculation, remains a genuine risk; absence of a search hit alone is not a uniqueness proof.

## Mathematical value

PASS. This is a natural fluctuation question for the full combinatorial complexity of sections of one of the canonical convex polytopes. The result identifies the sharp geometric distance \(1/n\) at which the symmetric central chi-square law becomes noncentral and then Gaussian. The three regimes require an exact normalization that depends on the sample standard deviation and produce a common factor simultaneously across all fixed face ranks. The work extends the baseline theory beyond a mere special parameter value, rather than recomputing a finite known table.

## Closest literature and limitations

The strongest existing overlap is *Joint chi-square face-vector fluctuations of random central regular-simplex sections* (public research note, 2026). Its hypotheses expressly fix the section through the centroid, so its limit is the \(h=0\) member of the critical family and does not determine the positive-offset or Gaussian regimes. König, arXiv:2312.01325, studies extremal section volumes at fixed distances, not Haar-random combinatorial laws. *The Best Ways to Slice a Polytope*, arXiv:2304.14239, supplies deterministic slice-combinatorics theory. *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, concerns maxima and attainable counts. The theorem covers fixed ranks only, does not give rates or total-variation convergence, and has no independent review.

Self-review: passed. Independent audit: not yet performed.
