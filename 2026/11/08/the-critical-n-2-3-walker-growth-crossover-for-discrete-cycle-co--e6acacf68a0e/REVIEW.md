# Independent mathematical audit

## correctness

PASS

For synchronized nearest-neighbor walks starting at 0, the union of lifted visited sites is exactly the integer interval from the global negative minimum to the global positive maximum; cycle coverage is M_t^++M_t^-≥n−1. Reflection gives P(H_t≥a)=P(S_t≥a)+P(S_t≥a+1). Stirling with adjacent-binomial geometric-tail ratio proves the moderate-deviation factor sqrt(2/pi)/z exp(−t I(a/t)) under a/sqrt t→∞, a/t→0. The rate I(v)=v²/2+v⁴/12+O(v⁶) gives each extreme a shift δ=b_n^6/[3(n−1)^2]→8c³/3, while joint opposite crossings by one walker are exponentially negligible relative to k_n independent walkers. Hence two independently shifted Gumbel extremes yield Z_n⇒16c³/3−G1−G2. If n^(2/3)≪log k≪n, the quartic rate penalty diverges and a union bound forces Z_n→+∞, while exact large-deviation upper/lower bounds retain leading T_n~n²/[8 log k]. Independent brute-force reflection counts checked t=7,8,15 at levels a=1..4, agreeing with binomial tails, and symbolic expansion confirms coefficient 8c³/3 per direction. No finite test is used as an infinite limit proof.

## originality

PASS

Majumdar–Sabhapandit–Schehr already establish the two-Gumbel convolution for the large-number Brownian ring and the span-to-cover identity. Rivera–Sauerwald–Sylvester prove finite-cycle multirandom-walk bounds up to constants in polynomial walker regimes, not exponential joint n and k limits. Neither primary text inspected supplies the discrete Cramér quartic correction, the sharp n^(2/3) transition or loss of second-order tightness at larger k. Resultary searches identified only this result for the exact crossover.

## value

PASS

This is a sharply motivated lattice-versus-continuum universality boundary for cycle coverage with exponentially many searchers; it quantifies when Brownian cover-time approximations fail in the second-order window, identifies a universal correction 16c³/3, and proves a sharp transition. These are genuinely new asymptotic scale and constant questions, beyond routine applications of the existing Brownian law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
