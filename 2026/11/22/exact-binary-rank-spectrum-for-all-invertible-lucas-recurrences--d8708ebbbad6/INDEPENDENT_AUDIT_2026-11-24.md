# Independent mathematical audit

## correctness

PASS

The recurrence is invertible because Q is a unit, so the reduced state returns to (0,1); its mod-two zeros are precisely the multiples of 2 for even P and of 3 for odd P. The polynomial identities U_{2k}=U_k V_k, V_{2k}=V_k^2-2Q^k and U_{km}=U_k U_m(V_k,Q^k) hold also for degenerate lifts, either by the companion identity or by polynomial continuation from distinct roots. For an even trace in the second recurrence and odd determinant, the last factor is odd for odd m. On the even-P branch V_2=2 mod 4, and this persists on doubling. Hence at indices 2^j times an odd multiplier, the valuation is v2(P)+j-1, with zero interpreted as infinite valuation. The fiber of valuation h<a has 2^{a-h-1} traces and every odd Q is allowed; P=0 mod 2^a alone has rank 2. For odd P the first candidate is U_3=A=P^2-Q and V_3=P B, B=P^2-3Q=3A-2P^2. Valuations t=v2(A), s=v2(B) are even-input valuations with exactly one equal to 1 and the other at least 2; v2(U_6)=t+s, and V_6=2 mod 4 supplies one per further doubling. Each fixed odd P gives uniform even A, and conditional on t=1 the variable 3(A/2)-P^2 is uniform even modulo 2^{a-1}. For a>=3 rank 3 has probability 2^{-(a-1)} within odd traces. Rank 6 comes from t=a-1 or from t=1 and s>=a-1, giving 3 times that mass. For rank 3*2^j with j>=2 the condition is t+s=a-j+1: the two mutually exclusive possibilities for the larger valuation give total mass 2^{-(a-j-1)} for 2<=j<=a-2. Counting all odd P multiplies these probabilities by 2^{2a-2}. The two smallest exponents give exactly the stated exceptions. Working with truncated or infinite valuations yields the same residue ranks; no restriction on a chosen lift is needed. An independent projective-row return enumeration reproduced all multiplicities for a=1..8 over 43,690 pairs. For C=[[P,-Q],[1,0]], the (1,2) entry of C^k is -Q U_k, and its vanishing is equivalent to C^k scalar. This is a projective order on the companion slice, not a full matrix period or a count over every matrix in the group. The frozen self-review suggestion that some residue pairs do not admit nondegenerate lifts is not used: one can take Q positive and P arbitrarily large positive in the required classes. The actual theorem is valid regardless of the lift.

## originality

PASS

The pointwise Lucas valuation and projective-order methods are not claimed as new. The identified additional content is the exact frequency of each first-zero rank over the full two-coefficient binary companion slice, including degenerate chosen lifts. No inspected evaluated distribution covers that slice. The finite-field and known pointwise results materially constrain novelty but do not give the residue-fiber counts.

## value

PASS

First-zero rank is a natural invariant of invertible second-order recurrences, and the dyadic modulus has an exceptional extra valuation stratum. Determining every frequency over the entire residue parameter space, not a selected finite modulus or a single recurrence, quantifies the disagreement between even and odd trace and supplies exact probabilities for generating recurrences of each projective order. The rank-six mass and the endpoint of the odd-trace branch are useful concrete invariants; the value is the evaluated aggregate law, not standard doubling identities or a full-period claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
