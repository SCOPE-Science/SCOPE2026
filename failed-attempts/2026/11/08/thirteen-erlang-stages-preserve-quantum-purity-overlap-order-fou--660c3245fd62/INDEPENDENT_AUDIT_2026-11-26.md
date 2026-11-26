# Independent mathematical audit

## correctness

PASS

Integrating the Erlang survival function against exp(iωt) and dividing by the mean waiting time gives F_n=((1-iz)^(-n)-1)/(inz), with F_n(0)=1. The energy basis makes P−O a sum over unordered pairs weighted by 2|rho_0,jk|². With y=z², W=(1+y)^n, and A+i z B=(1+i z)^n, the direct numerator of |F_n|²−Re F_n over n²yW² is yB²+(W−A)²−nyBW. Exact division by y²W reproduces Q_n. An independent rational Sturm check gave matched sign variations at 0 and +infinity for n=2,…,13 (0,0,1,1,2,2,3,3,3,4,4,4 on each end) and Q_n(0)>0 for every one, so none has a nonnegative zero. It also checks Q_1=0 and reproduces the exact n=14 balanced-qubit value −40308117/105226698752. Only nonzero-gap coherences can contribute for shapes 2–13, so the equality condition is precisely [H,rho_0]=0 including degeneracies.

## originality

FAIL

A distinct Resultary record states the sharp threshold and the same qubit witness for pure resets, with stronger results for n≥14. The mixed-state statement is a direct pairwise consequence: the earlier all-gap balanced-qubit inequalities give the strict sign of the scalar kernel at each nonzero gap; in any mixed reset state exactly the same kernel is summed with nonnegative weights 2|rho_0,jk|². No purity or rank assumption survives in that step. The exact rational witness is just evaluation of the earlier specified kernel at the earlier specified gap.

## value

FAIL

The sharp change in order between purity and overlap is a meaningful resetting phenomenon. As submitted, however, the threshold and witness reproduce that phenomenon in an already stronger characterization; replacing pure-state gap weights by mixed-state gap weights gives no additional sign question or nontrivial threshold. The rational evaluation of the same witness and replay of a sign proof do not give a distinct scientific result in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
