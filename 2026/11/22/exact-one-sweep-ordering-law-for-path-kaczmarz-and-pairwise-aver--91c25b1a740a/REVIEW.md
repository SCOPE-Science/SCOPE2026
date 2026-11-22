# Scientific review: exact one-sweep path Kaczmarz ordering

## Correctness
PASS. Every quantifier is restricted to \(n\ge2\), a permutation of all adjacent-difference projections, and isotropic covariance on the mean-zero subspace. The proof expands the tested row of each projection along two monotone predecessor chains, uses the tridiagonal edge Gram identity and telescopes the exact Frobenius-energy loss. The resulting run sum yields both bounds and their equality classes by strict monotonicity and strict superadditivity. There is no inference from finite data to arbitrary size. The embedded exact-rational checker was executed and passed 8200 cases.

## Originality
PASS on the inspected record, with publication-priority uncertainty. The closest inspected foundational paper, Oswald and Zhou (arXiv:1510.04727), treats error bounds for shuffled/preshuffled SOR and Kaczmarz, not a complete exact one-pass order-to-isotropic-error map for path incidence projections. Boyd et al. (2006) treat iid randomized gossip and long-run rate design, a different scheduling class. Dai et al. (2014) optimize iid row selection rather than a without-replacement permutation. Publicly indexed descriptions of Kazantsev–Matej–Lewitt (2005) and Herman–Meyer (1993) concern projection view orders in tomography; full text of these older comparisons was not available for direct inspection. Distinct titles or failed search alone do not prove novelty; the conclusion rests on the compared statements and the explicit residual access risk.

## Value
PASS. In one full pass with exactly \(n-1\) pair contacts and an isotropic initial error, scheduling changes the exact squared disagreement by an asymptotically sharp factor of \(4/3\). Equation (1) evaluates every schedule solely from a binary precedence word; it identifies all optimal and worst ordering classes and quantifies penalties of monotone runs. This is a complete natural finite-budget scheduling classification, not a minor numerical improvement or merely one example.

## Scientific limitations
The theorem does not optimize worst-case fixed-error contraction, multi-epoch schedules, nonpath graphs, heterogeneous averaging coefficients, or adaptive policies. Closely relevant older tomography-ordering papers were available only in abstract/metadata form and remain a bibliographic uncertainty. No independent audit was conducted.

Self-review: passed. Independent audit: not yet performed.
