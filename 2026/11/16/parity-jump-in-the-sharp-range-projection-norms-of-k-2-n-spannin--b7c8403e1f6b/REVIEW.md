# Independent mathematical audit

## correctness

PASS

Each K2n spanning tree has one degree-two column and exactly one selected edge elsewhere, yielding W=sum_j sj tj product_{i != j}(si+ti). For disagreement count >=2 the multiplier vanishes; count one gives magnitude 2^(n-1), and count zero gives 2^(n-1)|sum si|. Thus the support is the radius-one disagreement mask minus a balanced binomial shell when n is even. The full mask Fourier kernel is 2^n 1_(u=v)(n+1-2|v|). The deleted shell Krawtchouk generating identity yields binom(n,2j)|B_2j|=binom(n,n/2)binom(n/2,j), and diagonal sign is unchanged by subtracting C because n+1-2|v| is odd and C<2^n. Summing absolute values proves the exact endpoint formulas and Stirling limits. Independent direct Walsh summations for n=2..8 gave norms 7/4,3/2,183/64,15/8,1095/256,35/16,106295/16384, matching formulas; finite checks do not establish all n.

## originality

PASS

The indexed prior same-K2n result gives the identical W spectrum/rank but computes the Fourier projection onto the TREE-VECTOR frequency set, with norm n/2+n*binom(n-1,floor((n-1)/2))/2^n. Here the projection is onto support(W), a different mask; the punctured radius-one Walsh absolute kernel sum and its exponential-even parity transition do not follow as an equality from the prior endpoint norm. Weighted matrix-tree enumerators count trees but do not give this projection norm in inspected sections.

## value

PASS

The exact sharp l1/linfty amplification of the range projection distinguishes identifiable spectral subspace from the tree incidence set and establishes an unexpected polynomial-versus-exponential parity instability across the entire natural K2n family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
