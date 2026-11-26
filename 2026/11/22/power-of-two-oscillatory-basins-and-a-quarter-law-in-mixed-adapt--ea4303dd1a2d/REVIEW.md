# Independent mathematical audit

## correctness

PASS

Subtract the old opinion from its threshold: h=k-x is conserved, and the closed-neighborhood test then becomes an open-neighbor threshold test. Admissibility forces the opinion at h=0 or h=degree+1; intermediate h allows both. Leaves are therefore fixed at one, fixed at zero, or copy the old hub. With a fixed-one leaves and c copying leaves, from time 1 onward the hub follows a two-step recurrence with single-bit map g. The map is constant outside a<h<=a+c, and the state is then fixed by time 2; when c=0 even time 1 suffices. Inside the interval g is the identity and the state has period dividing two already at time 1. For each of the c central h values and each type assignment there is one primitive alternating orbit. Every word on the c copying leaves determines the new hub, hence selects exactly one of the two old hub opinions that enters this orbit. Thus the full basin has 2^c states, including both recurrent phases. There are binom(m,c)2^(m-c) assignments, giving every basin bin and the total oscillation mass by binomial differentiation. Fixed hub zero admits m+1-a thresholds and fixed hub one admits a+c+1, yielding the fixed-state census. Entry at time 2 requires c>=1 and a wrong initial hub in a constant regime, with a+b admissible interior choices; summation gives the stated N_2, with N_0 from the recurrent census and N_1 by subtraction. For m=1 N_2=0; for m>=2 a fixed-one leaf, copying leaf, h=1 and inactive initial hub give a sharp witness. The probability normalizations use all 2(m+1)4^m legal extended states, not just opinions. Independent direct closed-neighborhood replay classified all 72,816 states for m=1 through 6: every individual primitive basin bin, entry layers and the identity F^4=F^2 agreed (python3 /workspace/branches/independent-replay.py 1).

## originality

PASS

The update and the general period restriction are known; the tree fixed-state recursion can specialize to stars. The supported distinct claim is the per-orbit primitive basin spectrum and sharp full entry census for the mixed adaptive star, with the quarter-law as a consequence. Similar results for majority dynamics do not cover this state space or theorem.

## value

PASS

A star is the canonical hub-and-leaf test of feedback. The exact per-orbit basin sizes, recurrence census and sharp transient law separate two quantitatively different effects: a uniformly sampled extended state has exponentially small probability of lying on an oscillatory orbit initially but approaches oscillation with probability tending to one quarter. Neither simple period classification nor fixed-state counts provide that distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
