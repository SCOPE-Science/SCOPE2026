# Review of the opinion-connectivity threshold and subcritical symmetry breaking

## Correctness — PASS

The claimed model is an admissible specialization of Samadi et al. (2026), equations (3)–(4), using one undirected opinion edge, off-diagonal pairwise infection, and within-community quadratic exposure. The examined endemic equilibrium has original opinions \(-1/6\), away from the model's sign-switching surfaces. Direct calculation gives synchronous and antisynchronous Jacobian blocks with respectively \((\operatorname{tr},\det)=(-11/30,11/30)\) and \((-(1/2+2w),1/2-w)\), proving the full local exponential-stability cutoff. At \(w=1/2\), the exact center cubic \((164/11)v^3\) proves nonlinear instability. An analytic implicit-function argument gives the two unequal equilibria with branch slope \(-246/11\), and the center normal form shows each is unstable. The checker reconstructs all principal identities in exact symbolic arithmetic. No numerical experiment is used as an infinite proof.

## Originality — PASS, with residual literature risk

The primary source was inspected in its full-text HTML representation, including its model, full Jacobian, synchronous theorem, and numerical-example sections. Its Theorem 2 establishes endemic coexistence and stability *relative to a synchronous invariant set*, and its full Jacobian is general, but it does not report a two-community transverse threshold or a subcritical branch. The new result establishes that full-state stability changes with opinion-edge weight even as the synchronous dynamics remain unchanged. Search comparisons included local and published research records, related SIS-opinion literature, higher-order SIS literature, and general symmetry-breaking bifurcation theory. The latter supplies a method, not the specialized coefficient and threshold. Some related texts were accessible only by abstract or overview; an unindexed equivalent calculation remains possible.

## Value — PASS

The motivating paper specifically restricts its positive endemic stability statement to synchronous data and cautions that heterogeneous initial data need not synchronize. This finding supplies a sharp obstruction to inferring full-state stability, and identifies a counterintuitive design consequence: larger opinion connectivity can *remove* local endemic stability. The exact nonzero cubic resolves the bifurcation's direction and shows that the emergent unequal equilibria do not immediately become stable. This is a dynamical boundary in an admissible epidemiological model, not a normalization check or arbitrary parameter recomputation. A natural next research problem is the fate of nonsynchronous solutions beyond the local loss of stability; that is not proved here.

## Closest literature and limits

Samadi et al., arXiv:2608.31032 (2026), full text https://arxiv.org/html/2608.31032: model, Jacobian, synchronous-only coexistence theorem. She et al., arXiv:2102.12834 (2021), abstract inspected: pairwise-network SIS–opinion model without the present quadratic exposure. Kiss et al., doi:10.1093/comnet/cnad044 (2023), public abstract inspected: higher-order contagion without the present opinion coupling. Golubitsky, Stewart, and Schaeffer, doi:10.1007/978-1-4612-4574-2 (1988), publisher overview inspected: general symmetry-breaking methods. The conclusion is local to one two-community parameter choice with opinions strictly below the sign-switching surface; there is no statement of global attraction or a generic threshold for all network configurations.

Self-review: passed. Independent audit: not yet performed.
