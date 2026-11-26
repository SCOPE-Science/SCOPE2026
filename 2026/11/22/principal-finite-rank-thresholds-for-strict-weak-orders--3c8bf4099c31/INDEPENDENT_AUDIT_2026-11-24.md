# Independent mathematical audit

## correctness

PASS

Induct on the target rank simultaneously for all marked hosts. A one-point type either joins a marked level (decrementing exactly its unused capacity) or creates a level at one of the cuts (selecting a gap pivot of width u_j, leaving capacity u_j−1, and splitting the gap). For threshold t+1 each join thus needs capacity at least t+1, and each cut needs a pivot of width at least t+1 with both subgaps of rank at least t. These conditions suffice as all unchanged resources already meet threshold t. This proves the marked min and the max–min gap recurrence, including empty gaps, depleted levels and the unmarked empty host. The root pivot criterion recursively forces and is forced by an ordered width-dominating copy of B_t, which is exactly an induced copy. Its length and sum satisfy the displayed recurrences; size equality excludes all unused vertices and extra levels, giving uniqueness. Increasing an eligible host's level size realizes the threshold on every larger size, and the constant-width formula follows from the pattern's length and maximum. Greedy matching keeps the earliest eligible position and preserves any possible suffix. The final proof is unbounded; weakorder_rank_verify.py and verification_output.txt were inspected, not rerun. They record 2,047 positive compositions through size 11, 627,231 marked count states and 1,200 additional comparisons, not a formal certificate.

## originality

PASS

The supported distinction is the exact marked rank and principal induced threshold for ordered antichain levels, with its specific unique extremizer. Neither the finite-list existence theorem nor the closest same-day component-rank finding supplies that result; the latter does share the exact extremal size law for a different class. No priority or newness is attributed to the bare numerical sequence or to the general rank.

## value

PASS

Computes a class-relative extension rank for every finite host and marked subset in a natural ordered class with genuinely different cut and same-level challenges. Knowing there is a finite witness list cannot tell whether it is principal or identify the smallest host. The exact induced witness, its unique equality case, and a direct greedy decision procedure answer those structural and algorithmic questions even though the size sequence itself is shared by a different class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
