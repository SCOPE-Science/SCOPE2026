# Scientific review: Parity-selective covariance transitions in uniform occupancy and hypercube walks

## Correctness — PASS

Equation \(1\) follows from conditioning on a marked \(r\)-hit box; strict negativity for every even \(r\) follows from \(v=[1+(m-1)u]/m\) and Jensen. The odd-frequency first differences are \(2(u^{n-r}-v^n)\), whose signs change at most once, while the sequence tends to one and begins negative when odd \(r\ge3\). The fixed-frequency large-dimension limit has root \(e^{2c}+2c=2r-1\). These arguments cover all declared integer parameters. Exact enumeration and rational tests verify 25,210 bounded parameter cases but are not used as infinite proofs.

## Originality — PASS, with historical-priority qualification

The raw multinomial covariance is derivable from classical indicator moments and is explicitly not asserted as novel. The searched full published richness-frequency result, classical occupancy frequency-count sources and modern pairwise covariance asymptotics do not state the parity-dependent finite sign classification or its unique time threshold and asymptotic root; residual implicit coverage remains possible.

The closest source inspected is the published richness-versus-frequency one-switch theorem (https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813), which treats a different covariate and sign parameter. Barbour–Gnedin (arXiv:0809.4387) and Sagitov (arXiv:2604.15152) provide wider frequency-moment and approximation frameworks, not the finite parity-conditioned sign theorem found here. The unavailable full text of Voit's hypercube-walk paper and possible implicit classical equivalents remain historical-priority risks.

## Value — PASS

\(H\) is the exact Hamming distance in an \(m\)-dimensional coordinate-flip walk, while \(F_r\) describes its coordinate-use spectrum. The theorem answers a natural signed dependence question in every finite uniform occupancy model, separates even frequencies from odd ones, proves one and only one sign transition for odd \(r\ge3\), and determines the precise linear-in-\(m\) transition constant. This is a structural boundary, not just a numerical case or recomputation of known moment tables.

## Scientific limitations

Nonuniform allocations, exact arithmetic exclusion of the possible odd-frequency transition zero, and finite-dimension cutoff error bounds remain outside the result. Recovery of the raw covariance from established multinomial moments is not claimed as original; the analytical proof concerns the sign classification and threshold. Finite exact computations are supplementary.

Self-review: passed. Independent audit: not yet performed.
