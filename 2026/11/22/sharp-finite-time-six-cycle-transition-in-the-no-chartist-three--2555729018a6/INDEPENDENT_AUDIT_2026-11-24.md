# Independent mathematical audit

## correctness

PASS

Each update replaces the first coordinate by one of three symbols, so the second iterate is in the exact nine-state grid for any real starting point. In previous/current order, with r=h/d, the only non-neutral pairs for 1<=r<2 are opposites: each goes to an equal nonzero pair, then to a trailing zero and then (0,0). For r>=2 all differences are neutral, including at r=2; the grid then extinguishes within two steps. For 0<r<1, six distinct states close in the given cyclic order while the two opposite pairs enter in one step and (0,0) is fixed. Swapping to current/previous coordinates gives the stated word. For a concrete worst transient at h<2d use (x_0,y_0)=(-d-h-1,0), which enters the grid as (d,-d) in current/previous order; five steps are attained for d<=h<2d and three for h<d. When h>=2d the bound is actually four and is attained, for example from (d+h+1,d+3h+1). The invariant set is Borel and the complement has empty sufficiently high preimage, so invariance forces full mass on the finite periodic set; the cycle weights are uniform. Independent rational grid and off-grid checks confirmed the transitions and time witnesses.

## originality

PASS

The distinct contribution is the complete global classification of the two-step memory-collapse boundary, including its closed endpoint, finite-time capture and invariant measures. No novelty is attributed to the market model or the finite-state method itself.

## value

PASS

Zero trend following and exact fundamental-price correction are a motivated boundary, not fitted constants chosen to get a particular period. The finite-state graph characterizes every real starting point and resolves what happens at both switching equality and strict threshold, separating exact extinction from coexistence with one repeating orbit. The uniform capture bound and measure classification give a concrete baseline before chartist memory is restored. The proof is elementary but the complete boundary result is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
