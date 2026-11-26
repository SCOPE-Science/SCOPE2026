# Independent mathematical audit

## correctness

PASS

For the unnormalized XOR operator on labelled supports of all permutations, the two restricted-cycle EGFs give the bivariate signed EGF (1+s+t)/sqrt((1-(s+t)^2)(1-(s-t)^2)), where s marks ordinary labels and t marks labels in the Walsh character. In its even part put u=s^2,v=t^2; expansion of ((1-u-v)^2-4uv)^(-1/2) gives the binomial-square coefficient by Vandermonde. The odd part gives the stated two-term recursion with exactly one nonzero term. Restoring labelled factorials proves the multiplier, signs, and parity of the nullspace. On odd orders the even-weight sequence is strictly decreasing, and complement symmetry gives the (n-1)! minimum; n=1 has both multipliers one. On even orders the sign of the successive positive-eigenvalue ratio minus one is the sign of 2r+1-m. Stirling at r=m/2+O(1) yields sqrt(pi*m)/2 for the nonzero-spectrum condition number, not a full inverse. Moore–Penrose and projection conclusions follow by orthonormal Walsh diagonalization. The supplied verifier was inspected, not executed. A separately written direct character-sum replay passed 1,234 exact checks (permutations through n=8, formula/extrema through n=200) at /workspace/branches/70be3bda-ef13-496d-974e-9dd364114f51/independent_replay.py; the finite replay does not establish the all-order result.

## originality

PASS

The best matched statements cover the restricted-count inputs and a different cycle statistic, not the full labelled-support transform and parity-sharp inversion. The binomial and Fourier tools themselves are classical; this judgment is on the exact all-order spectral and conditioning results for the specified kernel.

## value

PASS

The statistic is naturally induced by cycle parity and the exact law answers a useful inversion question: even sizes lose precisely the odd Walsh modes, whereas invertible odd sizes have a condition number growing faster than the restricted even-size inverse. Exact smallest eigenvalues locate the most poorly recovered modes; the singular-versus-invertible parity transition and the distinct stability scales are not just a computation of total cycle counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
