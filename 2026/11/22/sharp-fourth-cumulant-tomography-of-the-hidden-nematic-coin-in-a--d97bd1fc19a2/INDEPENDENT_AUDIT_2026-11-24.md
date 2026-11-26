# Independent mathematical audit

## correctness

PASS

Use the source’s column-as-initial-heading convention, as made explicit by CHECKER.py propagating column masses with C: the positive turn has weight l, so the first harmonic is λ=p+ic. Uniform stationarity and the independent turn increments give E[conj(U_i)U_{i+d}]=λ^d and E[U_iU_{i+d}]=0. Hence all second-order displacement statistics depend only on λ. The two projected variances agree exactly by quarter-turn invariance. With S_N=ΣU_i, the difference of the two fourth cumulants is therefore Re E[S_N^4]/4, as seen by expanding (e^{-iθ}S_N+e^{iθ}conj(S_N))^4/16 at θ=0 and π/4; mixed terms of angular order ±2 vanish. Independently sum this raw fourth moment over sorted times, including equal times. For block sizes m_1+…+m_b=4 each term has multinomial weight 4!/∏m_j!, and the gap following block j contributes the geometric factor of harmonic 4−(m_1+…+m_j). In the rate limit the number of placements divided by N tends to one for fixed gaps, and the sums are absolutely dominated since |λ|,|η|<1. Put R=λ/(1−λ) and E=η/(1−η). The compositions with one, two, three, and four blocks give respectively 1, 8Re R+6E, 12|R|²+24E Re R, and 24E|R|². Dividing by four and using |1+2R|²=W/h gives the exact contrast in the source. Each individual cumulant rate also exists: the strictly positive tilted matrix has a simple eigenvalue at 1, separated in modulus from the other eigenvalues; use its analytic spectral projector on a small complex disk and the nonzero initial overlap. The normalized moment generating function is that eigenvalue to the Nth power times a nonzero analytic multiplier plus exponentially small error; Cauchy estimates give bounded derivative remainders. The slope of Δ in η is strictly positive since h,W>0. Strict positivity of the four weights gives precisely 2|p|−1<η<1−2|c|, so the inverse and open endpoint formulas follow, including the c=0 infinite upper limit and the p=c=0 sign test.

## originality

PASS

Credit the prior chiral coin, covariance blindness, and broad fourth-moment forward machinery. Supported distinction is the exact strict inversion and full open realizability interval for one axial-versus-diagonal fourth-cumulant rate difference with a positive discrete coin, not higher-harmonic sensitivity in general. The comparisons are best-of-knowledge and the strongest unresolved risk is implicit exact specialization of a prior forward formula.

## value

PASS

The missing parameter is genuinely invisible to an entire class of natural second-order observations, not just a single selected statistic. One precisely defined extra fourth-order rate recovers it and gives a sharp admissibility test and unique positive reduced coin; this is quantitatively useful beyond demonstrating sensitivity. It does not recover redundant operation weights or promise reliable finite-data inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
