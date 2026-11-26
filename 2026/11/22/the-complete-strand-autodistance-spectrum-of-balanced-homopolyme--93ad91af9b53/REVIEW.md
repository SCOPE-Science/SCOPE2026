# Independent mathematical audit

## correctness

PASS

The inverse of (a_i,b_i)=(x_i,bar x_{2m+1-i}) reconstructs the original linear word. Each track is proper, and the middle constraint is a_m different from bar b_m; that terminal indicator is not the mismatch indicator. Complementation preserves GC. Unequal paired states cause exactly two discrepancies, so the powers of v count half-distance. For even m alternating classes along both tracks keeps total GC m, permits every subset of mismatches before the center, and requires the center matched. For odd m, matching everywhere would give even GC. Changing the second track's last class while forcing the penultimate letter to be the other second-track letter from that same class keeps the track proper, gives the missing one GC occurrence and makes one forced mismatch. Free choices among the first m−2 positions give the other intermediate ranks, with m=1 checked directly. Alternating opposed mixed-class pairs gives full half-distance m for either parity. Independent enumeration over nonzero xor increments of a four-color alphabet, using global color-translation symmetries to count all initial colors, exactly reproduces all six spectra. For the limit, the normalized paired transition is P tensor P with P=(J−I)/3; centered G is in the sum of single-track eigenspaces (eigenvalue −1/3), while centered H has zero conditional mean on either track and lies in the tensor of mean-zero eigenspaces (eigenvalue 1/9). They are orthogonal with variances 1/2,3/16 before summing correlations, hence joint long-run diagonal 1/4,15/64. The three recorded same-length closed walks are valid and their additive-total differences are (1,0),(0,1), excluding any nontrivial unit spectral phase by the phase equality on closed walks. The conditioning is justified by Fourier inversion in GC: the primitive tilted matrix has an analytic simple dominant eigenvalue near zero, exponential decay away from the unique GC saddle, and a nonzero boundary prefactor since a positive fraction of stationary states pass the center test. Scale the GC integral and half-distance test frequency by m^(-1/2); the mixed quadratic term is zero, so dividing by the GC coefficient leaves the normal with variance 15/64 per paired site. The terminal factor cancels in the leading ratio. For r=0 the middle letters are complementary and therefore distinct, so the numerator is the proper halfword count at weight m/2. In a single track the GC type chain switches with probability 2/3 and has variance rate 1/8; its span is one (compare equal-length two-step returns with and without switching). The local limit contribution at even length k is 2/sqrt(pi k), and the total proper count is 4·3^(k−1). Substituting k=m and 2m in the ratio gives sqrt(2)·3^(−m) along even m and exactly zero along odd m.

## originality

PASS

The supported distinct claim is the joint finite-length enumeration including positive aligned half-distances, its exact support, and the balance-conditioned Gaussian law. The balanced proper-word marginal and zero-distance slice, and hence the component estimates underlying the zero-distance frequency, substantially overlap verified earlier formulas and should be treated as predecessor consequences, not independent novelty.

## value

PASS

The centered, aligned distance is a natural statistic of balanced proper words rather than a selected handful of lengths. The complete counts answer both which aligned distances are possible and how often each occurs in the mathematical model. The support distinguishes a parity-forbidden endpoint from all achievable ones, and the conditional variance tells a researcher the fluctuation scale among balanced words, neither of which follows from simply counting the total family or its fixed points. This is useful as a symbolic enumeration benchmark without any claims about physical sequence behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
