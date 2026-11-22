# Scientific review: a rare binomial bridge in complete bipartite sandpiles

## Correctness — PASS

For each integer \(n\ge2\), the exact burning criterion for a stable state with \(k\) occupied nonsink leaves is the union of the two boundary strips \(a=n-1,\ b\ge n-1-k\) and \(b=n-1,\ a\ge n-1-k\), containing \(2k+1\) pairs. A legal-wave case split for hub and leaf drives gives the full stated polynomial identities. For the leaf, the driven vertex fires twice exactly in the maximum event; for the hub all vertices fire at most once. Both polynomials sum to \(n2^{n-1}\) recurrent states, and the intermediate coefficients are exact binomial expansions. The vanishing intermediate probability \(1/n\) proves the two-atom weak limit without extrapolating finite numerics.

The provided `verify.py` independently implements Dhar burning and legal topplings for all stable configurations with \(2\le n\le10\), and checks polynomial identities, normalization, exact means and extreme coefficients for \(2\le n\le512\). Actual output: `SANDPILE_TWO_HUB_CHECKS_PASSED finite_n=2..10 formulas_n=2..512`.

## Originality — PASS on examined evidence, with residual risk

The primary-source analyses of Dukes–Le Borgne (arXiv:1208.0024), Aval et al. (arXiv:1307.7740), and Selig–Zhu (arXiv:2409.11811) cover recurrence and operators. Austin et al. (arXiv:1605.02713) give the general adjacent-sink one-toppling bound and avalanche polynomials on other families. The published *Full-system Abelian sandpile avalanches on complete bipartite graphs* record already gives the extremal coefficient for the **hub** drive; that coefficient is explicitly credited, rather than claimed as new. Its full statement and limitations do not give the intermediate binomial spectrum or the nonadjacent leaf-drive law. The published three-hub \(K_{3,n}\) avalanche record has a different family and source class and does not imply the two-hub formulas.

Actual published-record queries compared complete polynomial laws, both source types, binomial bridges, and possible equivalences. No stronger theorem was identified in examined material. Residual risk: unindexed older graph-specific avalanche polynomials, or an implicit coefficient extraction from general decorated-polyomino statistics, may cover the claim. Search failure alone is not taken as proof of uniqueness.

## Mathematical value — PASS

The exact polynomials describe the entire stationary response, not just a known maximum avalanche. The striking separation into two order-one extreme probabilities and a rare \(1/n\) binomially concentrated half-system bridge is a natural finite-size burst phenomenon. It exposes a structural difference between a hub drive and a nonsink leaf drive, including a unique double-toppling source in the leaf maximum event. The law is an interpretable full classification of the simplest two-hub complete bipartite family and supplies a tractable baseline for larger hub sets and perturbations.

## Limitations

All claims are restricted to the uniform recurrent measure, one sink from the \(n\)-part, a single chip, ordinary unweighted legal topplings, and integers \(n\ge2\). Finite checking is not an infinite proof, historical originality is not independently certified, and no broader universality or power-law claim is made.

Self-review: passed. Independent audit: not yet performed.
