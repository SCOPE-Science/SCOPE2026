# Independent mathematical audit

## correctness

PASS

The fixed source a and sink lie on the same shore of K_{3,n}, hence are nonadjacent. The burning test first activates height-two leaves and requires the taller hub to reach n; after it topples the height-one leaves activate, so the shorter hub needs initial height at least z0. This gives max(A,B)≥z0+z1 and min(A,B)≥z0, with n²·3^(n−1) recurrent states after summing (n−z0)²−z1² over ordered leaf heights. Adding at a does nothing unless A=n−1, when recurrence ensures z2≥1. After a's first toppling only the height-two leaves topple. If B<n−z2, there are z1 admissible B heights and size 1+z2. Otherwise there are z2 choices for B and b topples, releasing the height-one leaves. When z0>0, the source gets back fewer than n grains and size is n−z0+2. When z0=0 all leaves return one grain to a, which legally topples twice, and the odometer (2,1,1,…,1) sums to n+3. The stated binomial sums reproduce H_n, including replacing the last exponent n+2 of the second binomial branch by n+3. Dividing the two positive branch masses and maximum coefficient by the recurrent count gives the stated probabilities. Conditioned on positivity, the branches have asymptotically equal weights; their binomial parameters 1/3 and 2/3 and a vanishing conditioning/exception correction give the two-atom weak limit. The fresh finite replay matched all coefficients for n=2,…,7.

## originality

PASS

In the actual comparisons the exact fixed same-shore source polynomial counting repeated topplings, its exceptional exponent and its two-component conditional limit remain distinct. An earlier complete-bipartite avalanche paper has a plausibly relevant abstract but inaccessible decisive details; the verdict is bounded to the evidence available, not a claim of priority over that paper.

## value

PASS

A hub on the sink's shore is the natural nonadjacent drive, and K_{3,n} is the first fixed-shore size along this hub family with a second nonsink hub available. Its activation controls a different macroscopic size band. A full source-specific law including the repeated-toppling tail is a useful benchmark for distinguishing wave mechanisms and conditional size scaling, not just a known recurrent-state count or a finite numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
