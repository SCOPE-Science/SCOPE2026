# Independent mathematical audit

## correctness

PASS

Balance of prefix/suffix pairs at the four de Bruijn vertices with c111=0 forces c001=c100=x, c011=c110=y and c101=c010+y-x. Setting c010=a and c000=b gives the stated vector and t=a+y=w-y. At positive weight any balanced connected profile has t>=1; x<=t, and x=0 disallows b>0 (the 000 loop would be disconnected). All these vectors have connected support, so an Euler circuit realizes them, including n=1,2 under the specified wrap convention. Summing b and x gives the rational series. For w>=2 the y=0 summand remains strictly deficient below 3w even at the singleton boundary n=2w, and all others are bounded by their plateau values. Scaling y by n gives the integral of the positive part of min(alpha-beta,1-2alpha+beta) over [0,alpha/2], with intersection (3alpha-1)/2, yielding the three claimed quadratic pieces with O(n) error including the floors. The univariate series has an order-four pole with leading term 1/[12(1-z)^4] at 1 and genuine primitive third- and fourth-root poles. Its polynomial part is constant, so positive indices obey a quasipolynomial of exact period 12. Independent enumeration of balanced connected arc-multiplicity vectors at every n<=16 gives 394 profiles and matches every weight group (node /workspace/independent_checks.js, section 2). The finite test is not the proof. The frozen verifier was inspected, not executed.

## originality

FAIL

The October 26 composition-refined result explicitly supplies a complete connected-flow parametrization of the same eight oriented cyclic trigram coordinates at fixed composition. The new constraint is exactly deletion of the self-loop 111, a coordinate-zero face of that parametrization. It changes neither the balance equations nor the connectivity test for any nonconstant profile visiting 11. Setting that coordinate to zero therefore gives the claimed four-coordinate count directly, not merely a broader asymptotic or a count over an unrelated observation model. The generating series is also a routine specialization of the full fixed-composition count with a lower-support correction: if U counts all mixed profiles, H0 counts those not visiting 11 and Hplus counts the 111-free ones visiting 11, then U=H0+Hplus/(1-uz), since one can restore any number of 111 loops. Thus the desired mixed series is (1-uz)U+uz H0. H0 is the connected-flow slice with y=0. Constants, capacity, saturation, integral and pole statements follow from evaluating these elementary sums; no separate obstruction or structural claim survives this restriction. This is positive coverage through the prior stated parametrization, not a claim that the earlier text prints the forbidden-word formulas verbatim.

## value

FAIL

The noiseless binary profile-code model is natural, but this submission restricts an already exact four-vertex flow classification by setting a single freely repeatable loop coordinate to zero. The resulting interval sum and its elementary asymptotic and pole analyses do not supply a separate scientific gap, a new obstruction, or a nonroutine exact invariant beyond that specialization. The representative construction is an alternative description of the same realizable flows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
