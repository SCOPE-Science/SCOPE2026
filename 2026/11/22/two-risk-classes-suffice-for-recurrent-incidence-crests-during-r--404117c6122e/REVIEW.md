# Scientific assessment

## Correctness — PASS

The state equations preserve nonnegativity, and the cumulative-pressure coordinate \(x=\beta\int I\) is strictly increasing wherever \(I>0\). The exact formula \(I(x)=I(0)+\sum S_j(0)(1-e^{-\lambda_jx})-(\gamma/\beta)x\) yields \(I'=A-c\) and \(J'_x=\beta[A(A-c)-IB]\). Four strict signs at \(x=0,\log(9/8),\log(5/4),\log(3/2)\) are checked with rational bounds on logarithms in `check_incidence.py`. The susceptible class with risk one alone guarantees \(I'>0\) at the last landmark and hence throughout the witnessed interval. Real analyticity gives two strict incidence maxima separated by a minimum. A separate monotonicity argument proves at most one incidence maximum with one susceptibility value. The proof is exact; numerical labels in the result are only orientation.

## Originality — PASS (literature-bounded)

The originating 2026 model provides the finite-class closure and selection identity, not a second aggregate-incidence crest during strictly rising prevalence. Bootsma et al. report double incidence peaks associated with latent-period heterogeneity and weak coupling, mechanisms absent here. Alutto et al. prove unimodality of a weighted *infectious-prevalence* aggregate and study individual class prevalence; these are mathematically distinct observables from total new-case incidence. The related multilayer-network literature requires heterogeneous contact structure or propagation delay. Searches for static susceptibility-only incidence multimodality and semantic searches of indexed mathematical findings did not reveal an implication covering the exact two-class witness. Search failure alone is not a novelty proof; older generalized incidence theorems may remain undiscovered.

## Value — PASS

The result isolates a minimal, entirely static source of more than one new-case incidence crest: only two persistent susceptibility values are needed, while transmission, recovery and mixing stay fixed and total infectious prevalence remains increasing during the two crests. This matters mathematically because a monotone effective susceptibility and unimodal total prevalence do not imply unimodal new-case incidence. The sharp one-class obstruction and the nonempty open example class make the boundary structural rather than a single arbitrary simulation.

## Closest sources and limitations

- Izyumtseva et al., arXiv:2608.22122, Sections 3 and 4: model, susceptibility selection, and exact finite-support closure; not total-incidence multimodality.
- Bootsma et al., arXiv:2308.06593, Section 10.1: multiple incidence peaks through heterogeneous latent periods and weak contacts; does not imply the current no-latency, homogeneous-mixing witness.
- Alutto et al., arXiv:2309.14583, Theorem 3.8 and Section 4: one peak for the weighted infectious aggregate, possible multiple extrema in individual classes, not the total incidence formula here.
- Zheng et al., arXiv:1706.05780: multiple peaks on weakly coupled multilayer networks, not the same single-pool mechanism.

This is a mathematical model result, not a fit to observed data. The proof gives **at least** two incidence maxima, and it does not certify the absence of additional extrema. General historical-priority review is incomplete.

Self-review: passed. Independent audit: not yet performed.
