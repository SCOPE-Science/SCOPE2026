# Scientific review

## Correctness — PASS

The proof reconstructs SIS Poisson equations for all nonempty infected subsets and shows that the expected accumulated infection burden has the state-size reward rather than the constant reward for extinction time. An attractive graphical coupling yields edge monotonicity, and the classification of all at-most-three-vertex residual graphs establishes the exact lower-order optimum. The explicit five-vertex residuals reduce the decision to a path versus a triangle plus isolated vertex. The self-contained script symbolically checks both 15-state rational solutions, their factorization, the sole positive root, residual graph isomorphisms and five independent rational-parameter optimum tests. The finite rational tests do not replace either the coupling proof or the all-parameter polynomial sign argument.

## Originality — PASS (best-knowledge assessment)

The closest primary works are Ball–Britton–Neal (2014), on total life-time reward for homogeneous-mixing birth–death and SIS processes; van de Bovenkamp–Van Mieghem (2015), on exact SIS extinction time; Holme (2017), on exact SIR size-based node deletion; and Holme–Tupikina (2018), on finite-graph SIS extinction time rankings. The new statement is a sharp, transmission-rate-dependent optimal vaccination threshold for *SIS cumulative infected person-time*, with a different Markov-reward right-hand side and different quantifiers. No inspected paper or screened prior claim provided this theorem or implied it via a stronger coverage theorem. The remaining risk is unlocated small-graph SIS reward or optimization work under equivalent terminology; the searches do not establish definitive historical uniqueness.

## Value — PASS

Unlike an arbitrary small-graph numerical comparison, the result proves a natural first possible network size, a unique positive rate transition, the full optimizer sets for every rate, and an exact algebraic threshold. This is an interpretable theoretical benchmark for reinfecting epidemic-control objectives and illustrates how clustering versus connectivity changes prevention priorities. It does not claim empirical policy value.

## Evidence and limitations

The primary proof is in `RESULT.md`; executable exact symbolic checks are in `verify_sis.py`. Independent confirmation beyond this review has not been performed. All assumptions are finite homogeneous SIS, one uniformly seeded initial case and one fully protected vertex. Related SIR final-size and SIS extinction-time results do not automatically transfer to this cost.

Self-review: passed. Independent audit: not yet performed.
