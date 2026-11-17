# Independent mathematical audit

## correctness

PASS

For a unit row, exact conditional expected squared-error decrease is zᵀS(w)z; optimum is max λmin(S). Diagonal values are a p_i+b p_{i−1} and offdiagonals proportional to w_{i,+}−w_{i,−}. For a≤b the nonnegative dual vector y=(1/a,0,1−(−a/b)^1,…,1−(−a/b)^(n−2)) satisfies a y_i+b y_{i+1}=1, yielding 1≥Qλmin with Q=Σy. Primal equally split signed edge masses q_i/Q have all required diagonal entries ≥1/Q and offdiagonals zero; Σq=Q. Equality forces offdiagonals zero and recurrence unique when a<b; at a=b the positive q_i form a minimum edge cover. Reversal handles a>b, uniform gives c/(n−1), and ratio tends n−1 as c→0. Independent 48 rational primal–dual cases match, not the all-parameter proof.

## originality

PASS

Exact E-optimal sample weights and saturated primal–dual certificates for the mirrored ± adjacent-coordinate frame, unique away from equal weights and sparse at the balanced phase boundary, are not supplied by the general Kaczmarz sampling SDP or earlier endpoint-anchored difference-path theorem.

## value

PASS

A complete exact E-optimal design for the natural signed edge-measurement frame quantifies worst-direction convergence improvement, a unique all-row phase off balance, and a sharp sparse optimum at balance. Its exact primal-dual profile is a motivated nontrivial optimization fact beyond a generic SDP existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
