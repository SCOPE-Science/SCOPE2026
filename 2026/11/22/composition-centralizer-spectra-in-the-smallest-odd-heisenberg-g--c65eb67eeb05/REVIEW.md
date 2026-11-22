# Scientific review: composition-centralizer spectrum for an odd Heisenberg group

## Correctness — PASS

The claim specifies an odd prime \(p\), the exponent-\(p\) Heisenberg group of order \(p^3\), and *all* group endomorphisms under composition. The established normal form \(f_{A,u}(w,z)=(Aw,(\det A)z+uw)\), with column \(w\) and row \(u\), gives \(|M_p|=p^6\). Direct substitution establishes the composition and two simultaneous commutation conditions. A complete case partition separates the two special scalar matrices, the other \(p-2\) scalars, nonscalars with invertible \(A-\det(A)I\), and rank-one singular matrices of semisimple or Jordan form. The crucial rank-one quotient argument yields exactly the two root counts \(2p-1\) and \(2p\). Thus the seven terms cover every endomorphism disjointly.

Two checksum identities were verified algebraically: coefficient sum \(p^6\) and weighted centralizer sum \(p^8+5p^7-8p^5+3p^3\). The standalone computational checker independently enumerates matrix commutation and linear-fiber conditions for \(p=3,5,7\); separate actual group-operation tests exhaust all endomorphism homomorphism laws and composition-on-generators at \(p=3\). These finite checks support, but do not replace, the universal algebraic proof. No characteristic-two claim is made.

## Originality — PASS relative to inspected literature

The closest direct paper is Kumar and Pradhan, *On the Endomorphism Semigroups of Extra-special p-groups and Automorphism Orbits* (arXiv:1908.00331, first posted 2019-08-01). Its Theorem \(\Omega\) gives the general endomorphism normal form, and its subsequent sections calculate the total endomorphism population, semigroup images of **group elements**, and automorphism orbits of group elements. These findings are credited, not rebranded. The present centralizer-size **distribution in the endomorphism composition monoid** is not one of those stated formulas; deriving it requires the new rank-one solvability and affine-line cases. Szabó, *Finite Class 2 Nilpotent and Heisenberg Groups* (arXiv:2301.01863, first posted 2023-01-05), studies structural decompositions/embeddings rather than this invariant.

Related indexed mathematical findings on automorphism Reidemeister numbers, Heisenberg Lie-algebra endomorphism ranks, commuting rank-one group retractions, and centralizers of a different prime-kernel Frobenius endomorphism monoid do not imply the complete seven-stratum census. Historical claims in the accessible algebra archive were compared by mathematical objects, restrictions and logical implications, not matching titles alone. A non-exhaustive search is not proof of absolute novelty; earlier unindexed or differently worded semigroup-centralizer enumerations remain a possible priority risk.

## Value — PASS

The centralizer-size histogram of a finite monoid is a natural invariant: it refines the global number of commuting ordered pairs, records degrees of its commuting graph, and detects the center. The exact seven-value spectrum gives a complete nonabelian infinite-prime family and a sharp probabilistic statement, not an arbitrary finite count. Its nontrivial semisimple-versus-Jordan split explains why two different intermediate centralizer degrees arise, beyond the previously known total endomorphism count.

## Scientific limitations and closest sources

The result applies only to the smallest exponent-\(p\) extraspecial group for odd \(p\). It does not assert statements for exponent-\(p^2\) groups, characteristic two, or higher Heisenberg rank. The checker is exhaustive only for \(p=3,5,7\), and group-operation testing is exhaustive for \(p=3\). The 2019 general-parametrization paper makes eventual rediscovery by simpler methods plausible; the seven centralizer coefficients require the separately documented calculation. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
