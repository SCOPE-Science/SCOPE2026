# Independent mathematical audit

## correctness

PASS

Original proof gap (not a false entropy formula): at frozen RESULT.md line 59 the fixed limiting tilt does not in general give a Theta(N^(-1/2)) probability at the required integer V. For I=2, rho=2/3 and N=floor(2L/3+L^(3/4)), the target is a deviation of order L^(3/4) from the mean of Binomial(N,1/2); a Chernoff bound is exponentially smaller in sqrt(L). The replacement uses the actual mean V/N, monotonicity of the tilted mean by positive variance, and exact-sum multinomial counts rounded with entries 0 and 1 adjusting the two constraints. All probabilities remain uniformly positive and Stirling gives a subexponential lower bound; coefficient extraction proves the claimed limit for every specified sequence. The strict entropy gap follows from positive relative entropy against the unbounded geometric law with the same mean, not from assuming independent geometric finite-ring gaps. Other claims survive unchanged: neighboring transfers connect all compositions, and one circuit of a vacancy token returns the gaps and moves the mark by I, exhausting each gcd phase. Incoming and outgoing weights match in the cyclic donor sum, giving product balance, including on the marked cover. A one-unit removal in the donor sum gives the partition-function ratio; each jump crosses I physical bonds and stationarity gives equal signed flux on each bond. Frozen configurations correspond to the bounded compositions after dividing marked counts by N, including exactly I translations when L=IN. Independent occupancy-based replay (python3 /workspace/branches/audit_exact_124.py 1) checked 68 small rings, all tested class sizes and keys, exact balance, individual physical-bond currents and frozen counts. The repair corrects the scope note for the packaged script and retains strictly positive baselines as the assumed setting, not a necessary condition for irreducibility. The repaired RESULT.md and verification notes were reassessed; no change to the frozen evidence was made.

## originality

PASS

Credit the same fixed-hop Arrhenius generator, Gibbs invariance, zero-range methods, and even exact unrestricted finite-ring current as prior, as well as the elementary static frozen-gap criterion in earlier traffic dynamics. The supported distinct contribution is the exhaustive marked residue/root-phase decomposition and transport conditioned on a specific communicating class, with the frozen physical census and entropy. The repaired prior-work account gives the finite-current overlap explicitly. No global priority is asserted.

## value

PASS

This resolves a real ergodicity issue for using Gibbs transport in a finite long-hop ring. At the same particle count one may have frozen states and an active steady current of 8/27 in the stated example, and the class formula says which current an initial preparation selects. The census and its entropy distinguish exponentially many traps from an exponentially small uniform probability of preparation in a trap. The repaired proof retains these scientific conclusions and does not claim new hydrodynamics or mixing rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
