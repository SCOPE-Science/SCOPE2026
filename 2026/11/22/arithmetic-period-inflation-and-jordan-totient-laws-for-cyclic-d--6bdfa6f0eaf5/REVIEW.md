# Self-review

## Correctness — PASS
The cyclic translation by the stride on a ring of length \(nt\) has precisely \(g\gcd(t,b)\) components. A cyclic difference equation is soluble if and only if its input sums to zero over each component, and each soluble component has \(\kappa\) free starting values. This proves the fixed-point count, the prime-adic minimal multiplier, and the universal maximum multiplier. Möbius inversion is restricted to targets with *least* period \(n\). For uniformly random output words, the mutually independent residue-class sums produce the exact Jordan-totient law. The standalone checker matches 81,090 direct fibers and all-output distributions for 95 further parameter choices. Finite checks do not certify the infinite statement; the proof does.

## Originality — PASS within inspected evidence
Kang–Jäger (arXiv:2609.01140v1) develops the permutative lift framework and minimality/ergodicity criteria, not this periodic-target census. Mariot–Leporati–Dennunzio–Formenti (2017) gives a general algorithm for preimage periods and multiplicities and finite-ring linear decompositions, which *does* cover computational determination of any particular instance. The present restricted claim instead supplies a simultaneous closed gcd-and-vector-order formula for all parameters, with an exact Jordan-totient random-target distribution. Nearby indexed work on period-doubling components, elementary-rule lifting, and Rule 150 inversion does not imply that distribution. A related difference-lift reflection-complexity theorem computes a different statistic; an additive cellular-automaton temporal-symmetry census likewise does not imply inverse-fiber period counts. A historical equivalent under cocycle or linear-module terminology remains possible; neither indexed absence nor this partition proves priority.

## Mathematical value — PASS
The full cyclic preimage-period spectrum and first allowable lifting period are canonical dynamical invariants for a finite-to-one sliding-block code. The new arithmetic expression resolves them uniformly, and the Jordan-totient law measures precisely how often a random target permits an uninflated spatial period. The explicit dependence only on \(\gcd(n,d)\) for that law is a structural simplification, not an arbitrary finite computation. General linear cellular automata and primitive-target-conditioned probability distributions are outside the claim.

## Closest literature and residual limitations
- Z. Kang and T. Jäger, *Lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1 (2026).
- L. Mariot, A. Leporati, A. Dennunzio and E. Formenti, *Computing the periods of preimages in surjective cellular automata*, Natural Computing 16 (2017), 367–381, DOI:10.1007/s11047-016-9586-x.

The earlier general algorithm applies to individual instances; its existence is not a new result. An overlooked explicit specialization remains the main novelty risk. Random-target probabilities must not be interpreted as probabilities conditioned on primitive output period.

Self-review: passed. Independent audit: not yet performed.
