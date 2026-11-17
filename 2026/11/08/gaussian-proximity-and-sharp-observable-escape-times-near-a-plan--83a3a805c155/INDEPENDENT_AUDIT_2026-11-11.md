# Independent mathematical audit

## correctness

PASS

Conserved H=x-log x+y^2/2 and xdot=-xy, ydot=x-1 imply a unique initial small-x exit on negative-y branch for sufficiently small epsilon. At exit y=-z, x=s/z, energy equation z^2/2+log z+s/z=L+eta^2/2+log s+epsilon. Exact physical time integral of 1/(1-X(y)) has boundary layer s/z^2+O(z^-3), which cancels -s/R^2 from endpoint expansion, leaving time eta+sqrt(2L)+(eta^2+2log s-log(2L))/(2sqrt(2L))+O((log L)^2/L^(3/2)). Independent mpmath high-precision Lambert W quadrature at eta=0,s=1,L=100 yields 13.95456467198 against 13.95481181679 asymptotic and reconstructs Gaussian inverse. Fixed positive s, bounded eta only.

## originality

PASS

Prior transient-center theory defines finite-time exit concepts and studies the same flow but inspected abstracts do not establish this explicit threshold speed first-exit asymptotic and Gaussian inverse proximity. Resultary search found different systems with logarithmic escape laws, none equivalent by smooth conjugacy or parameter substitution. 2022 SIAM full text unavailable; best-of-knowledge PASS with explicit unresolved priority risk, not a whole-text NOT_COVERING declaration.

## value

PASS

A sharp residence-time versus distance law for a documented nonequilibrium transient-center example is a natural quantitative diagnostic, with nontrivial cancellation of the physical-time layer. The Gaussian-in-time precision is relevant to distinguishing slow observable dynamics from simple logarithmic hyperbolic escape.

The dated certificate retains the supplied scientific assessment, sources and limitations.
