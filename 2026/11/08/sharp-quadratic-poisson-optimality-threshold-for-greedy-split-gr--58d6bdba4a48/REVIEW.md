# Scientific review

## Correctness — PASS

The feasible-edge probabilities follow from exact edge counts in \(K_a\vee\overline K_b\). Internal clique choices contribute one lost matching edge each. Conditioning on no internal choice gives a uniform labeled cross-part injection. A coupling of the remaining clique-size process with independent Bernoulli choices proves the explicit Poisson total-variation bound, and a logarithmic expansion of the exact zero-deficit product gives all three sharp limit regimes. The standalone Python checker passed 11,717 assertions covering independent labeled enumeration, exact rational recursion, critical inequalities and finite total-variation estimates. The infinite statements rely on the proof rather than those finite tests.

## Originality — PASS (qualified)

The greedy edge-choice algorithm and independent Bernoulli Poisson approximation are established tools. Arnosti (2021), *Greedy Matching in Bipartite Random Graphs*, https://doi.org/10.1287/stsy.2021.0082, studies random bipartite input instances, not this nonbipartite split-graph family. Dyer–Frieze–Pittel (1993), https://doi.org/10.1214/aoap/1177005436, analyze sparse random graphs and random labeled trees. Neither inspected source directly implies the fixed-family exact optimality product, whole-matching-law total variation or quadratic Poisson deficit window. The abstract of Dyer–Frieze (1991), https://doi.org/10.1002/rsa.3240020104, was available but its full text was not, so historical priority remains qualified. An absence in searches is not treated as proof of global novelty.

## Value — PASS

For the natural random-edge greedy maximal-matching algorithm, the theorem identifies a sharp \(b\asymp a^2\) scale for achieving the true maximum rather than simply a good multiplicative approximation. It supplies a finite error estimate, a Poisson additive-deficit law and an exact whole-output comparison with uniform optimal matchings. This is a mathematically motivated algorithmic reliability question on an infinite canonical graph family.

## Limitations

The explicit Poisson bound assumes \(b\ge4a\), while the exact optimality formula assumes \(b\ge a\). No statement is made about unequal edge weights, vertex-first greedy matching, or sharpness of the numerical error constant. Full historical-priority verification and independent scientific audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
