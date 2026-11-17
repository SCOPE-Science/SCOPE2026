# Independent mathematical audit

## correctness

PASS

For N>=3, Gamma>0, 1<=m<N and 0<b<1, the diagonal one-channel Dicke ladder is a pure-death chain with independent Exp(Gamma*k*(N-k+1)) holding times. Since lambda_1=lambda_N=Gamma*N while all 2<=k<N are faster, T_m has log-concave density and increasing positive hazard; E[S_m(t-V)/S_m(t)] with V=sum_{k=m+1}^N E_k is strictly increasing by the hazard difference and P(V>t)>0. S_N(0)/S_m(0)=1 and its ratio diverges, giving exactly one positive trace-distance crossing. The exponential moment product C_m=prod_{k=2}^m lambda_k/(lambda_k-Gamma*N)=m*(N-1)/(N-m) telescopes; the two equal endpoint slow exponentials give S_N(t)~Gamma*N*(N-1)^2*t*exp(-Gamma*N*t), S_m(t)~C_m*exp(-Gamma*N*t). Thus S_m/(b*S_N)~Q_m/(b*Q_N)~m/[b*Gamma*N*(N-1)*(N-m)]/t. Initial Q_m(0)>b*Q_N(0) implies at least one energy crossing, not uniqueness. The proof applies for fixed N in t->infinity; SciPy generator checks and exact rational telescopes are only finite corroboration.

## originality

PASS

Best-of-knowledge distinct exact result after comparing named equivalent, broader and database formulations; known subclaims explicitly credited, with residual priority risks.

## value

PASS

An all-size, uniquely timed trace-distance reversal in the ideal collective-emission Dicke cascade, together with the exact double-slowest-mode late-time coefficient, closes a meaningful gap between observed finite-size Mpemba crossings and unrestricted prediction, while correctly separating the weaker energy-crossing conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
