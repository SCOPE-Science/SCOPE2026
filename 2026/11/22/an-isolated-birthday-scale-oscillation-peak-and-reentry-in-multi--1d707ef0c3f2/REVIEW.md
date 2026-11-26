# Independent mathematical audit

## correctness

PASS

The same opposite-shore word is seen by every vertex on a shore, so it is either overwritten by one color or left unchanged. Both ties give an initial fixed point; with two winners the first step is monochromatic on each shore, and their winners agree exactly in the fixed case. Among these states only the q constant and q(q-1) differently colored monochromatic pairs are periodic from the start. With exactly one winner the first step changes the tied shore to that winner's color, and the second step finishes consensus unless the winning shore was already monochromatic. Counts by winner are U_r/q by permutation symmetry, proving the five census rows and exact oscillation probability, also when either shore has one vertex. For (m,n,q)=(2,3,3), direct counts give U_2=3, U_3=21 and the five populations 39,6,54,36,108. The generating coefficient chooses the winning color of occupancy h and caps all others at h-1. For growing r and q of order r², one doubleton with all remaining singleton colors has probability binom(r,2)/q times product_{j=1}^{r-2}(1-j/q), and the possibility of any triple changes the unique-maximum event by at most binom(r,3)/q². Expanding the product yields (r²/(2q)) exp(-r²/(2q)) to leading order in the critical regime. Independent uniform winner colors on the two shores give the factor 1-1/q. With n/m→ρ, the product yields H_ρ; its log derivative has its only zero at (1+ρ²)/4, and 4ρ²/(1+ρ²)²≤1 proves the balanced peak. In the valley the collision count has diverging mean and variance at most its mean (even overlapping pair indicators are uncorrelated), whereas triples vanish; at least two doubletons tie. Above the birthday scale collisions vanish by the union bound. At fixed q, conditioning on a prescribed pair's total count bounds the equality probability for those two counts by O_q(r^-1/2); a finite union bound makes a unique winner overwhelmingly likely. The limiting entry classes follow from the normalized census. This covers only the specified valley and each fixed-q regime, not all intervening growing palettes or a global maximum over q. The supplied occupancy verifier and logs were inspected as corroboration, not executed.

## originality

PASS

Standard sparse occupancy already gives the single-doubleton law used here, and period-two convergence is classical in binary majority. The supported distinct contribution is the five-class entry census under the particular two-shore update and the resulting unbalanced birthday profile with valley and fixed-palette reentry. The closest same-day clique study uses the same palette scale and another event with a different limit and constant; no priority ordering follows from the date.

## value

PASS

The analytically solvable two-shore model converts collisions into an oscillation event. The exact entry-time baseline and explicit unequal-shore peak show quantitatively how a larger palette can both create and suppress oscillation, with a genuine gap before fixed-palette reentry. That parameter-dependent boundary is substantive beyond the textbook birthday law or a binary eventual-period bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
