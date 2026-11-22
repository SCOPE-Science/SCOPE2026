# Independent mathematical audit

## correctness

PASS

At the assigned RESULT.md blob 7686756fddaba06d56a28b3e4ae1e20f41d0580c, the Boolean-lattice Möbius coefficient factors over maximal selected coordinate runs. The exact one-run generating function (1-z^k)/(1-z^(k+1)) gives q_l=0 or ±1 on the stated residues. The degree bound D=n-r for 1<=r<=k-1 follows from the run count and gap congruence, attained by the length n-r prefix; D=n for residues 0,k. The unnormalized monomial-to-Walsh formula then forces divisibility by 2^(n-D) and yields a frequency supported on a maximal-degree monomial attaining that magnitude, establishing both gcd and least nonzero multiplier. The n<k boundary has only the zero-frequency nonzero multiplier 2^n; k>=2, n>=1 and linear, not cyclic, avoidance are explicit. Counting-convolution characters give the pseudoinverse norm; zero-free is asserted only for residues 0,k. The actual two verification scripts verify integer Möbius transforms and full Walsh spectra, independently cross-checked in bounded k,n cases; finite checks are supporting diagnostics, not the all-n proof.

## originality

PASS

The theorem's specific integer Möbius support on selected runs and the sharp all-frequency least Walsh multiplier for the highly bordered pattern 1^k are not implied by the compared unbordered-pattern theorem, generalized Fibonacci Gray codes or ordinary generating-function counts. Best-of-knowledge PASS for this motivated natural pattern class, with priority and general signed-pattern results still possible in unindexed literature.

## value

PASS

For the standard k-consecutive-one avoidance language (generalized Fibonacci strings), the exact integral Möbius support gives reusable coefficient-level structure, while the sharp minimum character multiplier directly quantifies stability of counting convolution on every binary cube size. This is a nontrivial uniform structural theorem, not just counting or an arbitrary small enumeration; no broader result is required for the exact gap to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
