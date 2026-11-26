# Independent mathematical audit

## correctness

PASS

On bin i write qX=i+u, where u is uniform on [0,1). The future label runs through b^n consecutive residues, with exactly the excess residues and multiplicities in (1), including the lag-zero diagonal. The same residues are the endpoints of n successive digit updates, which proves the stated power identity independently of an assumption about the observation process. For the spectrum let Df(i)=f(i+1)-f(i) and Mf(i)=f(bi mod q). The identity b Q^T D=DM follows by telescoping. D identifies functions modulo constants with the mean-zero subspace, so the restriction is conjugate to the action of M modulo constants divided by b. On characters M permutes each coprime additive-order class in cycles of length ord_d(b), while all transient characters contribute zero on the resulting diagonal blocks. Removing the fixed constant gives exactly (2). The two relative deviations from uniform are (q-r_n)/b^n and -r_n/b^n. Counting their multiplicities gives (3) and (4); the linear terms cancel and the quadratic term in (3) is chi-square/2, with O_q(b^(-3n)) error. The zero residue occurs iff q divides b^n; otherwise the eventual nonzero residue cycle yields the claimed rate and the checked coefficients 5,6,3 at b=2,q=7. The supplied exact finite checker check_arithmetic_binning.py and VERIFICATION.md were inspected; no uploaded code was run. This verifies the stated equal-bin, two-time result, not arbitrary partitions or higher-order information.

## originality

FAIL

The claimed all-resolution arithmetic classification materially overlaps the older spectrum of exactly the generalized de Bruijn digraph, not merely the classical q=b^k case. The ordinary graph parameter range suffices for the nonconstant spectrum at all b: write b=Lq+r, then b Q_{b,q}=L J+r Q_{r,q} for 2<=r<q, where J is the all-ones matrix; at r=0 or 1 the residual summand is respectively zero or the identity. On mean-zero vectors the uniform part vanishes. The cell law and exact cutoff follow by counting digit-path endpoints in the graph. Exact divergences, the quadratic information prefactor and its eventual arithmetic oscillation then follow directly from the two distinct cell counts. No separate prior statement of the Shannon formulas is claimed. The failed decision is grounded in the older spectrum coverage and the mathematical reductions, not in inability to read the full 1991 article or in treating a later indexed record as earlier.

## value

FAIL

The bridge from bins to a digit walk and the oscillating information example are useful exposition. The proposed new classification, however, recomputes the invariant of an established graph, extends it by a uniform matrix term, and applies elementary divergence formulas to its two cell counts. The surviving changes do not supply an independently substantive new invariant as claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
