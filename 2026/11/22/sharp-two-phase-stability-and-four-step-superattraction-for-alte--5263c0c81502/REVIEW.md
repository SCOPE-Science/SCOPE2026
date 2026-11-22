# Self-review

## Correctness — PASS
The two-phase product \(T=(I-bvv^\top)(I-auu^\top)\) has trace \(2-a-b+ab(1-s)\) and determinant \((1-a)(1-b)\). The complete quadratic Schur criterion gives both claimed inequalities, with \(abs>0\) automatic. On \(b=1\), the spectrum is \(\{0,1-as\}\), so the zero-trace choice \(a=1/s\) is unique. Cayley–Hamilton and the nonzero-matrix calculation prove the four-step quadratic cancellation; the \(C^2\) Taylor expansion of the four-step nonlinear map with zero derivative proves local quadratic attraction. Boundary eigenvalues are explicitly excluded from nonlinear stability claims. Exact-rational checks reproduce the identities and a concrete example. The numerical quartic perturbation check is illustrative, not an infinite proof.

## Originality — PASS within checked evidence
Ridenhour's full accessible article introduces the modified-gradient framework, gives conservative sufficient conditions, and identifies sharper anisotropic bounds as a direction; it does not supply the joint two-phase rank-one criterion or nonlinear four-step superattractor. Borgard et al.'s accessible paper covers strong over-relaxation in a **distributed pooled** Kaczmarz framework, not this fixed alternating two-direction modified-gradient system. The available abstract of Cegielski–Suchocka and the accessible material on oblique Kaczmarz do not state the particular nonlinear superattraction theorem. published-finding corpus queries for algebraic equivalences, alternating projections, common- versus heterogeneous-gain Kaczmarz, and nilpotent products found nearby but non-dominating results. Historical priority remains uncertain for the elementary linear product criterion; the coupled nonlinear conclusion and exact two-parameter boundary are the central claimed contribution.

## Mathematical value — PASS
This resolves a concrete stability question explicitly motivated by a recent analysis: a complete, sharp, angle-dependent two-gain region, a unique superattracting tuning and an arbitrarily large individually over-relaxed phase. The nilpotent derivative is a structural cancellation that survives as a higher-order nonlinear local attraction, whereas stepwise sufficient criteria do not explain it. The result is not a claim that over-relaxation is generally beneficial, nor a universal higher-dimensional theorem.

## Related sources and risks
The main comparisons are arXiv:2611.14756v1 (full accessible HTML), arXiv:2006.01739 (abstract and first main sections of the complete PDF), doi:10.1137/070698750 (abstract), doi:10.1016/j.rinam.2022.100342 (accessible source excerpts), and published-finding corpus indexed summaries of pertinent Kaczmarz studies. Full text unavailable for the plausible Cegielski–Suchocka article; inaccessible specialized earlier results could imply some of the elementary two-by-two algebra. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
