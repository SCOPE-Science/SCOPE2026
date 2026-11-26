# Independent mathematical audit

## correctness

PASS

The last-column decomposition yields P_j=a_j P_(j-1)+b_j P_(j-2). Gauging by the product of the rung signs gives u_0=u_1=1 and u_j=u_(j-1)+epsilon_j u_(j-2), where epsilon_j=b_j a_(j-1) a_j. The gauge preserves magnitudes and each normalized string has 2^n rung choices and 2^(n-1) horizontal-pair sign lifts, giving the exact kernel multiplicity. All-plus gives the Fibonacci maximum; all signed sums have Fibonacci parity. The all-minus orbit (1,1,0,-1,-1,0) proves both singularity in the even-Fibonacci residue and attainment of absolute value one elsewhere. Flipping its last sign at a resonant width gives magnitude two. At n=1 the two frequencies have magnitude one. Starting at a zero at width 2, each subsequent three-step block can freely assign its first two signs and take its last sign minus, returning to zero; this proves Z_(3k-1)>=4^(k-1) and the stated fraction bound. The independent Python replay at branches/2af68975-471d-4be0-856f-c5ca19a59e03/signed_recurrence_check.py checked all width-1 through width-15 normalized strings and checked the physical-edge fibers directly through width 4, with the five listed zero counts reproduced. The frozen scripts were read, not executed. These bounded data corroborate, not prove, the all-width reasoning.

## originality

FAIL

Material coverage of the headline spectral recovery theorem is demonstrable, not merely a similarity of recurrences. The earlier indexed height-three Dyck result gives the same invertibility law and sharp signed multiplier gaps for an affine copy of precisely the same Fibonacci cube at every even ladder width n=2m-2, where m is Dyck semilength. Its reported 7032 zeros at m=8 also give the exact normalized zero count 879 at ladder width 14, not a different spectral statistic. The extension to odd widths uses the same cube and elementary parity and sign witnesses. The frozen record's claim of a distinct sharp recovery invariant as framed therefore does not pass originality. This comparison does not establish that the quantitative lower bound at all resonant widths was previously proved, and is not a rejection for unavailable full text. No substantively narrowed replacement is submitted.

## value

PASS

Perfect-matching edge incidence is a natural signal, and the sharp nonzero gap and the dimension of its lost Fourier space directly quantify recovery. In particular, constructing a quantitative family of cancelling frequencies at every resonant width is informative beyond the existence of one zero. This scientific usefulness does not restore originality to the previously covered sharp recovery classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
