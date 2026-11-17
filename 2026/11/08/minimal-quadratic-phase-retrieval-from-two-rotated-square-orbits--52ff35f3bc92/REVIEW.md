# Independent mathematical audit

## correctness

PASS

For complex P_2 and two rotated 4-point circles, four-point Fourier decomposition isolates diagonal mean D, complex first-harmonic C and aliased Nyquist O. With u=r1^2,v=r2^2, the Hermitian lifted kernel is span{diag(uv,-(u+v),1)} iff r1,r2 positive unequal and sin(2alpha)!=0. Its generator has rank 3, so no nonzero rank<=2 difference xx*-yy* lies in the kernel, proving phase injectivity, with explicit ambiguities on zero/same radius or aligned angles. The odd homogeneous Hermitian determinant argument proves a seven-measurement global impossibility. Frobenius-orthogonal Fourier blocks yield two singular values of 2[[1,u,u²],[1,v,v²]], twice those of 2[[r1,r1³],[r2,r2³]], and those of 2sqrt(2)[[u,0],[v cos(2alpha),-v sin(2alpha)]]. Their squared-product equals 2^18 (uv)^4 (u-v)^6((uv)^2+(u+v)^2+1)sin²(2alpha), maximized in angle at alpha=pi/4 modulo pi/2. The rank-two distance-to-full-rank-kernel bound establishes the stated nonsharp stability inequality. Independently reconstructed the raw 8x9 Hermitian sampling matrix in orthonormal coordinates and compared spectrum, kernel, product determinant for 27 distinct parameter triples; all passed.

## originality

PASS

A decisive comparison identifies full PRIOR coverage of injectivity, sharp sample count, excluded angles/radii, and even the one-dimensional Hermitian kernel: these must not be credited as original. The narrower surviving claim is the complete Frobenius-normalized eight-value lifted singular spectrum, explicit determinant/squared-volume objective for arbitrary positive radii, and global rank-two difference lower bound. Inspected earlier exact two-polygon and balanced-square proofs do not give those quantitative invariants; different Gaussian-bin spectral results do not specialize to this arbitrary radial polynomial evaluation family without changing weights. Best-of-knowledge O is qualified for this quantitative remainder only.

## value

PASS

With injectivity and its eight-sample minimum already known, the exact individual measurement singular values, Gram determinant, and explicit global rank-two stability factor are still motivated exact design invariants. They distinguish phase-retrievable configurations with widely different conditioning, give a sharp angular optimum for a specified volume objective, and can guide finite sampling design. The formulas contain nontrivial radial factors and the full orthogonal block decomposition, not a mere restatement of known injectivity. No global condition-number optimum or novel general uniqueness theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
