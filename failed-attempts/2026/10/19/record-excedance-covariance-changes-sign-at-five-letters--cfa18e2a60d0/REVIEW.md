# Independent mathematical audit

## correctness

PASS

Conditioning on a record at i fixes the maximum of a uniform i-subset at i but leaves the subset uniform. The expected indicator at i differs from its unconditional mean by delta=t/n-binomial(t,i)/binomial(n,i); for earlier positions the expected number of threshold exceeders is unchanged over the entire subset, so each of the i-1 other positions has the opposite difference divided by i-1. The relative order giving R_i remains uniform even when later entries are fixed. Multiply by 1/i, with R_1 deterministic, to get the kernel. At t=0,n the threshold is constant; for 1<=t<n and i>=2 the binomial ratio is strictly less than t/n. Substituting t=j and telescoping sum_{i>j} 1/[i(i-1)] gives the column formula including j=1; at j=n the indicator is constantly zero. For interior columns j binomial(n,j)=n binomial(n-1,j-1)>=n(n-1) and j(n-1)>n, establishing their positive signs. Summation gives C_n=1/2+(1/2-B_{n-1})/n. Symmetrizing the factorial ratio for successive B_m gives the stated recurrence; it gives B_1=2, B_2=5/2, B_3=B_4=8/3 and preserves the upper bound 8/3 for m>=3. This proves all signs and the four displayed small values. Substitution gives C_{n+1}-C_n=[(n+1)B_{n-1}-2n-1]/[2n(n+1)]>0. The index pairs at 1,m-1 contribute 2/m to B_m; those at 2,m-2 contribute O(m^-2), and all deeper indices together are bounded by m/binomial(m,3). Thus C_n tends to 1/2, and the stated correlation follows from the rank-record and Eulerian marginal variances. Fresh exact enumeration of S_5 corroborated all 150 kernel entries and totals sum R=274, sum E=240, sum RE=556, giving 1/15. This is finite corroboration; the uploaded checker was read, not run.

## originality

FAIL

Distinct indexed record 8032d5fd55d9 states the same full ordinary-excedance matrix, the identical aggregate formula and sign reversal, and the same correlation asymptotic. The arbitrary-threshold version is not separately stated there, but the inspected proof supplies the conditional law of the subset and of each selected position, and the generalization only changes the count of all-below-threshold subsets from 1 to binomial(t,i). The column sums and monotonicity are direct summation and reciprocal-binomial algebra on the same exact covariance. The comparison shows material equivalent coverage, not historical priority or derivation between archive entries.

## value

PASS

The sign reversal is a substantive structural fact about two natural statistics on the same permutation. The matrix explains why replacing the aggregate with an assumption of uniformly positive or negative dependence would fail. That scientific interest is separate from the indexed overlap, and the mechanically implied threshold extension does not support a stand-alone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
