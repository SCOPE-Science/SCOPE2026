# Scientific review of the two-step Rule 50 checkerboard law

## Correctness — PASS

The final statement covers every even indexed ring and exactly its four spatial-period-at-most-two output words. The all-zero and all-one two-step counts follow directly from the local rule. For checkerboards, the 16-state transfer construction counts all cyclic predecessors, including lengths two and four. Its fully enumerated nonzero rows reduce to a four-class graph with uniquely lifted closed walks; the displayed four-state matrix has characteristic polynomial \(t^4-t^3-2t^2-2t-1\). The logarithmic determinant identity then proves the rational generating function, recurrence, and exponential asymptotic. The included standalone checks rebuild the matrices, verify the determinant, and exhaustively compare all four output classes on rings through length 18. The general proof is algebraic; those finite checks are not substituted for a proof.

## Originality — PASS, with documented limitations

Wolfram (1983) defines and studies elementary rules. Jen (1989, especially pp. 426–427 and 433) explicitly treats Rule 50's **one-step** preimages of finite blocks, exhibiting Fibonacci-type formulas. Fukś (2003; publicly accessible arXiv copy dated May 28, 2013) studies **time-depth** preimage counts for fixed short blocks of the infinite shift, including Rule 50. Neither inspected statement gives the two-update inverse-fiber spectrum of period-dividing-two outputs on all indexed even rings, nor the corresponding quartic recurrence in spatial half-length. The present claim is a particular evaluated transfer-graph reduction, not a claim of inventing transfer methods. Searches for equivalent two-step/checkerboard terms, recurrence coefficients, and initial numerical sequence found no direct covering statement. The relevant 1989 and 2003 works remain important conceptual antecedents; an older table or implicit special-case calculation cannot be ruled out. A direct sequence-database query failed to load and therefore provides no negative evidence.

## Value — PASS

The complete set of two-periodic targets is a natural fixed-spatial-period benchmark for inverse branching of a cellular automaton. Exact two-step counts are not determined by one-step target counts alone. The checkerboard's fourth-order recurrence and Perron rate determine a nontrivial probability of recovering the output after two updates at every even circumference, while the constant outputs have radically different inverse behavior. This supplies a reusable finite-state model and a sharp asymptotic for a standard periodic test configuration, beyond a finite census or an arbitrary parameter slice.

## Scientific limitations

No claim is made about a global maximum over arbitrary output configurations, about odd circumference, about longer time depths, or about historical uniqueness. The direct sequence-database lookup was inaccessible and there is no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
