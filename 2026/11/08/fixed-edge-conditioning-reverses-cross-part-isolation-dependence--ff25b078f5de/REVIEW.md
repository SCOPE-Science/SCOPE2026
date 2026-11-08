# Scientific review

## Correctness — PASS

The proof defines all finite edge ranges and the out-of-range binomial convention. Exact hypergeometric event counts establish the mixed covariance. The factor identity \((C-t)(N-t)-(A-t)(B-t)=-t\) controls signs including all endpoint cases, and uniform logarithmic expansions give both asymptotic covariance rates and the variances required for correlation normalization. The packaged Python verifier passed 17,150 checks, including exhaustive exact enumeration of all binary matrices up to \(4\times4\). The all-size claims are proved symbolically, not inferred from finite experiments.

## Originality — PASS, qualified

The closest available full text is McKay–Skerman (arXiv:1302.2446), which defines these fixed-edge and independent-edge bipartite models and approximates degree laws in an acceptable density regime. Its key assumption excludes the present sparse \(p\asymp1/n\) scaling; no exact two-sided isolation covariance classification is stated in the inspected material. Strona et al. (2014) instead preserve both row and column totals, which fixes the isolation counts. Results involving degree-one vertices do not imply this different mixed statistic or the opposite-sign and scale comparison. Searches for zero rows, zero columns, two-sided isolated vertices, model equivalences, published research records and tables yielded no decisive matching formula. Historical sources of Eicker et al. (1972) and Holst (1980) could not be read in full: implicit priority remains unresolved and no claim of exhaustive novelty certification is made.

## Mathematical value — PASS

The exact all-size sign law explains a natural conditioning effect on two-sided network isolation. The independent-edge model gives positive covariance of order \(n\) in the sparse regime; a fixed edge count reverses the sign and reduces covariance to order one. Balanced correlations have explicit distinct limits, making the effect a structural feature of random bipartite network null models, not a local numeric improvement.

## Limitations

No joint central-limit theorem, stochastic-order comparison or negative-association property for arbitrary statistics is asserted. The covariance could be implicit in unexamined historical occupancy results. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
