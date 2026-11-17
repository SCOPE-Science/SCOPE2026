# Independent mathematical audit

## correctness

PASS

For Q=P_n-I and Gauss-Legendre r(z)=(12+6z+z²)/(12-6z+z²), the inverse denominator has right-half-plane roots, so r(hQ) is well-defined and row-sum preserving for h>=0. Exact symbolic inversion of n=2..7 recovers unconditional positivity for 2,3 and neighbor numerator -c_n h F_n(h)/D_n(h) for n=4..7, positive denominator. Each F_n has one sign variation and a unique positive root (H4~6.1357203, H5~4.3143227, H6~3.8080105, H7~3.6119199); positive-coefficient/interval-transformed certificates keep other entries positive through each root. The Padé seventh coefficient is -1/1728, giving (0,7) negative for sufficiently small h for any n>=8; the cyclic group inverse yields adjacent coefficient -6(n-3)/(nh) for n>=4 at large h. Independently reproduced the exact symbolic n<=7 signs and small/large asymptotics from the frozen formula/artifacts/verify.py.

## originality

PASS

General finite-Markov [2/2] Padé result covers n<=7 local positivity and n=8 obstruction, and other published two-stage heat-cycle results concern undirected Laplacians. Neither derives the global sharp thresholds for each directed n=4..7. Exact directed eight-cycle re-entry findings concern n=8, not these four positive windows. PASS on best-of-knowledge; earlier unindexed directed-cycle threshold algebra remains a risk.

## value

PASS

Sharp, fully algebraic positivity windows for an A-stable fourth-order conservative integrator on canonical nonreversible Markov cycles are a meaningful numerical-analysis benchmark; they discriminate unconditional, bounded-window and small-step failure regimes and provide exact endpoints beyond general local theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
