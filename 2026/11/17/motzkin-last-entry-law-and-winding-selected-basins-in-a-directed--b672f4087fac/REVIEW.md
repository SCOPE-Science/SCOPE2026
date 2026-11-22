# Independent mathematical audit

## correctness

PASS

For n>=2 with one directed observed successor site and three colors, the edge differences obey p_i(new)=p_{i+1}(1-q_i), q_i(new)=q_i(1-p_{i+1}); a moving 1 and stationary 2 annihilate, preserving K=#1-#2 divisible by 3. A surviving 1 crosses every other edge by step n-1, forcing a single-species recurrent word by then. The unique collision at step n-1 gives a cyclicly marked (2, Motzkin-excursion length n-2, 1) edge word, with n possible marks and 3 vertex lifts: E_n=3n M_{n-2}. Central trinomial T_n counts K=0; reflection exchanging particles pairs K>0/K<0, so rotate/fix basin totals are (3^n-3T_n)/2 and (3^n+3T_n)/2. Motzkin asymptotic yields sqrt(3)/(2sqrt(pi*n)). Independently exhaustive labelled color state orbit detection for n=2..8 matched each histogram, n-1 boundary, winding sign and both exact formulas. The finite test is not the all-n argument; that comes from no-particle-creation and the outer pair Motzkin bijection.

## originality

PASS

The same annihilating-particle local rule and an infinite-line site-entry random-walk method are existing results of Kůrka, Formenti and Dennunzio. Their Definition 1 and Theorems 1–3 concern first *arrival at one site after a specified age* on the bi-infinite lattice, whereas here the statistic is *global first entry of a finite modulo-three lifted ring into its eventual periodic orbit*. Their results do not by direct implication specify the sharp n−1 cutoff, 3n M_{n−2} cyclic/lift correction or the exact winding sign basin census. Distinct two-neighbor cyclic automata and torus winding results also do not settle this model. Best-of-knowledge PASS, not priority certification.

## value

PASS

Sharp all-n transient bound and exact extreme-tail Motzkin law for a natural finite cyclic automaton, together with exact attractive basin split conditional on a conserved topological winding, are self-contained structural and enumerative invariants. The cyclic lift and last-collision constraint are not routine deductions from the infinite-line site arrival theorem; extremal entry-time population is mathematically meaningful rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
