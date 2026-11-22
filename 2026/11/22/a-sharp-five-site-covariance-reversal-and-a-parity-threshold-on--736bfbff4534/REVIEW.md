# Scientific review: fan hard-core covariance reversals

## Correctness — PASS

The hard-core partition polynomial on \(F_n=K_1\vee P_n\) equals \(I_n(z)+z\). Conditioning at each endpoint produces unnormalised weights \(zI_{n-2}\) and \(z^2I_{n-4}\). Multiplying the standard path recurrence gives the continuant determinant \(I_{n-4}I_n-I_{n-2}^2=(-1)^{n-1}z^{n-2}\), yielding the displayed covariance identity. For even \(n\), the sign polynomial \(I_{n-4}(z)-z^{n-3}\) has precisely one positive root by Descartes' rule and the endpoint signs. The recurrence's positive characteristic root establishes monotonic thresholds and the expansion about \(z=2\).

The minimum is not inferred from a sample: the included Python-stdlib `verify.py` enumerates all 1,099 labelled simple graphs on one through five vertices and all 10,650 unordered vertex pairs, computing the entire signed covariance numerator in integers. Exactly 60 labelled graph/pair combinations have coefficients of both signs, all are the five-site fan with marked path endpoints, and each has numerator \(z^3-z^4\). All other pairs have numerators whose coefficients share one weak sign. The checker separately verifies the fan identity for path lengths four through eleven, but these finite comparisons are not used as proof of the infinite statement.

## Originality — PASS on examined evidence

The standard hard-core partition and path recurrence are credited to classical literature, including Scott and Sokal (arXiv:cond-mat/0309352, first posted 2003-09-15). The new claim concerns sign reversals of unconditioned *marked endpoint* covariance under variable common fugacity, the all-even-length threshold asymptotic, and a sharp uniqueness result among all graphs with at most five vertices. The published research summaries on fan dissociation polynomials and canonical independent-set path correlations use different admissibility rules and ensembles. A published summary on inverse covariance for hard-core crown graphs addresses a different statistic. These differences mean those particular statements do not imply the present theorem, but absence of a matching indexed result does not prove priority. The primary preprint was materially examined in its partition-function and vertex-deletion sections; the comparison is bounded and not a full reading of all potentially relevant works.

## Mathematical value — PASS

The five-vertex fan is the smallest graph where ordinary pairwise exclusion-gas dependence can reverse sign when one common activity is varied. This makes the result a sharp motivated boundary, rather than a table of isolated small-graph computations. The exact all-length parity law and the convergence of the unique even-length threshold to activity two give an explanatory infinite family: the universal hub contributes a competing exclusion mechanism, and path parity determines the high-density sign. Neither a general correlation-inequality proof for all graphs nor a phase transition is claimed.

## Closest literature and remaining risks

Scott–Sokal (2003) covers the graph-independent hard-core partition formalism, but the examined text does not derive this joint endpoint result. Brown–Hickman–Nowakowski (2004) studies the locations of zeros of independence polynomials, not the specific two-point sign reversal. Public research summaries for fan dissociation polynomials, canonical hard-core path/cycle correlations and hard-core crown-graph precision entries concern distinct statistics or ensembles. The GitHub full-text pages for those summaries were unavailable through the attempted access route; no claim is made to have read them. A stronger unindexed theorem or a result in an uninspected appendix could subsume the finding. Independent scientific audit and complete historical-priority certification are not performed.

Self-review: passed. Independent audit: not yet performed.
