# Independent mathematical audit

## correctness

PASS

For the unnormalized 16-DFT the squared lower gain on each fixed C is the least Gram eigenvalue. An odd multiplier on rows permutes supports, and translation changes only unit phases on columns, so the minimum over C is affine-invariant. Repeated row classes modulo four duplicate rows on C={0,4,8,12}; the converse is the prime-power full-spark theorem (balanced residues at each divisor of 16, implied here by one representative of each class modulo 4). The independently written exact reproduction at /workspace/branches/c64e8ab6-aba3-4c76-900e-19f789cfd1a9/reproduce.py exhausts all 1,820 row sets and verifies the 256 balanced sets decompose into disjoint affine orbits of sizes 64,128,64. Its reproduction.log lines 2–3 give negative determinants of 1000G−I on one support for each competing orbit, implying a strictly subthreshold eigenvalue. Line 4 records strict positive signs for every one of 7,280 leading principal minors for the last orbit representative: exhaustive enumeration of 1,820 supports, recursive determinants in Z[x]/(x^8+1) and integer radical enclosures. Sylvester's criterion gives a strictly superthreshold least eigenvalue at every support, hence also for the finite minimum. The determinant digest matches the frozen exact certificate; its supplied code and optional floating-point diagnostic were inspected but not executed. This proves the affine optimizer class and the 64/192/1564 split. Neither the spectral condition-number ratio nor blind unknown-support identifiability with four samples follows; the result compares the gain conditional on each frequency support.

## originality

PASS

Pass for the exact minimax spectral comparison on the order-16 four-row problem. The full-spark criterion and rank census, including the qualitative split and universal orbit structure, are not credited as new. Available evidence does not show distinct prior coverage of the winner or strict separator.

## value

PASS

The finite case compares a motivated stability invariant in a cyclic Fourier inverse problem, not a convenient isolated minor. It distinguishes all fixed-size designs by a strict uniform bound and shows that, among universally invertible four-sample designs, the consecutive baseline is not optimal. The quantitative comparison is useful for this order even without an exact expression for the optimal eigenvalue or an all-orders theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
