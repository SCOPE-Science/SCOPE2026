# Independent mathematical audit

## correctness

PASS

An influence from t at time 0 reaching 0 at time t has exactly one nearest-neighbor path, moving one step left each update. No other input to a path update can depend on the flipped bit. Thus the output indicator is the product of the local right differences δ at the successive unperturbed center bits. Left-edge permutivity of (F^s X)_i follows by induction: the left input to the last update uniquely contains X_(i−s), once and with XOR coefficient one, and the other inputs exclude it. The center at step s therefore has unique fresh pivot X_(t−1−2s), XORed with a function of bits strictly to its right. Conditional on all nonpivot initial bits used by the centers, the center-word map from pivots is triangular and bijective. Hence the centers are jointly fair, turning the product into 0, 2^(−t), or 1 exactly. Each ordered derivative pair leaves two independent table entries, yielding the 4/8/4 census. Rule 30 corresponds to h(b,c)=b OR c, so its right derivative is nonconstant; leftmost influence is always one. An independent direct iteration using Wolfram rule numbers and full finite cone truth tables checked both edges for all 16 rules at t=1..5.

## originality

PASS

Same-observable Monte Carlo profiles and the exact left-edge influence are antecedents; the left edge is explicitly not credited. The inspected statements do not cover the exact rightmost product expectation for Rule 30 or the all-rule derivative census. Distinct Resultary analogues have different observables or dynamics. The decision concerns the exact right-edge claim, not historical priority for qualitative right-side decay.

## value

PASS

The extreme edge is a natural, observable boundary of the empirical Rule 30 sensitivity profile. Its exact all-time formula gives an analytic reference, distinguishes qualitative irrelevance from exponential survival and full transmission, and explains the distinction uniformly across the whole naturally defined left-permutive elementary class. The fresh-pivot argument matters: local marginal fairness on its own would not determine survival along the path.

The dated certificate retains the supplied scientific assessment, sources and limitations.
