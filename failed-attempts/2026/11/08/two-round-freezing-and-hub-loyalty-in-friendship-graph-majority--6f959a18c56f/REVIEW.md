# Independent mathematical audit

## correctness

PASS

Condition on initial hub 0 by complement symmetry. A uniform peripheral pair persists regardless of the hub; a mixed pair takes the old hub's bit at both endpoints after the first update. So the periphery is frozen at time 1. With u initially opposite pairs and m mixed pairs the hub flips first exactly when 2u+m>k, and flips twice exactly when 2u<k<2u+m. It cannot flip for the first time at update two. Thus the second state is fixed; double flips give entry two. The sharp examples are u=(k-1)/2,m=2 for odd k>=3 and u=k/2-1,m=3 for even k>=4, with no double flips for k=1,2 and nonfixed initial states in each. Permanent flips are precisely u>k/2, or u=k/2 with m>0, giving the Bin(k,1/4) tail minus its even all-uniform tie count. Subtract permanent flips from the strict first-flip probability based on Bin(2k,1/2). Fixed states require m=0 and u<=k/2; unanimous final states require u=0 or u=k. These establish all the counts. At the respective even and odd binomial upper-tail starts, successive ratios decrease and are bounded by 1/3, tending to 1/3 at any fixed offset, so the tail is asymptotic to 3/2 of its first term. Stirling gives the stated parity constants and the omitted tie event is exponentially smaller. The exact entry-two fraction tends to 1/2. Independent exhaustive tuple-state dynamics for k=1..7 checked the fixed-state bound and all counts; at k=3 the entry counts are (8,96,24), with 20 hub reversals and 56 consensus cases.

## originality

FAIL

Two earlier Resultary findings jointly cover the theorem. 6882fd08f78e gives the same sharp rapid freezing, fixed/entry and consensus census, and entry-two limit. Full-text inspection of 035eb4d8b16a establishes the exact permanent hub-flip tail and parity constants as well, despite its emphasis on global-majority reversal and biased initialization. The two probabilities are distinguished explicitly in that source: its P_n equals the audited R_k at n=k. This is demonstrable prior coverage, not an access limitation.

## value

FAIL

The exact hub and basin statistics are meaningful for a natural highly centralized graph, but the same cutoff, census, exponential rate and sharp constants are already available. Combining their earlier expressions or restating them in separate even and odd variables yields no independently useful new exact fact or surviving repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
