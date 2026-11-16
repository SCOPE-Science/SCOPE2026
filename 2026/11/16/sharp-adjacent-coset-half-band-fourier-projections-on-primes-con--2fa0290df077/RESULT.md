# Sharp adjacent-coset half-band Fourier projections on primes congruent to five modulo eight

## Finding

Let \(p\equiv5\pmod8\) be prime. Split the nonzero frequencies into the four multiplicative quartic classes \(C_j=g^j\langle g^4\rangle\) for a primitive root \(g\), indexed modulo four. Among the six two-class spectra, the Fourier projection onto **adjacent** quartic classes always has minimum \(\ell^\infty\)-operator norm. The two pairs of opposite classes have weakly larger norm, and equality occurs exactly when the even coordinate in the sum-of-two-squares representation \(p=a^2+b^2\) has \(|b|=2\).

Precisely, let the order-four character \(\chi\) satisfy \(\chi(g)=i\), and write its Jacobi sum \(J(\chi,\chi)=a+ib\). The two sharp norms are
\[
L_{\mathrm{adj}}=\frac{p-1}{4p}\left(2+\sqrt{p+1-b\sqrt p}+\sqrt{p+1+b\sqrt p}\right),
\qquad L_{\mathrm{opp}}=\frac{p-1}{2p}(1+\sqrt p).
\]
Therefore \(L_{\mathrm{adj}}\le L_{\mathrm{opp}}\), with equality if and only if \(|b|=2\). Equivalently, all six candidate spectra tie only when \(p=a^2+4\) with the odd coordinate \(a\). For primes \(p=37,61,101\), the adjacent choice is strictly better; for \(p=5,13,29,53\), the choices tie.

## Assumptions and scope

The finite group is \(G=\mathbb Z/p\mathbb Z\) with counting \(\ell^\infty\) norm. Define Fourier projection by \(P_E f=\mathcal F^{-1}(\mathbf1_E\mathcal Ff)\) for either unnormalized Fourier transform followed by inverse normalization \(1/p\), or equivalent unitary normalization. The six candidate sets are precisely unions of two distinct quartic classes, all having cardinality \((p-1)/2\), with zero excluded. The result does not compare arbitrary half-cardinality sets or other residue characteristics. Its primary subject is endpoint norm optimization of finite-group Fourier multipliers.

## Proof

Write \(m=(p-1)/4\), \(\zeta=e^{2\pi i/p}\), \(\eta_j=\sum_{x\in C_j}\zeta^x\). Since \(m\) is odd and \(-1\in C_2\), \(\eta_2=\overline{\eta_0}\) and \(\eta_3=\overline{\eta_1}\). Put \(y_0=\operatorname{Im}\eta_0\), \(y_1=\operatorname{Im}\eta_1\). For a multiplicative character satisfying \(\chi(g)=i\), its Gauss sum is
\[
\tau(\chi)=\eta_0+i\eta_1-\eta_2-i\eta_3=-2y_1+2iy_0.
\]
The standard finite-field Gauss–Jacobi identity \(\tau(\chi)^2=\tau(\chi^2)J(\chi,\chi)\) and the positive quadratic Gauss-sum evaluation \(\tau(\chi^2)=\sqrt p\) apply because \(p\equiv1\pmod4\). Writing \(J(\chi,\chi)=a+ib\), we obtain \(y_0^2+y_1^2=p/4\), \(y_0y_1=-b\sqrt p/8\), and \(a^2+b^2=p\) because the Jacobi sum has modulus \(\sqrt p\). The Jacobi sum is a Gaussian integer. The elementary quadratic-character identity \(\sum_x\bigl(\frac{x(1-x)}p\bigr)=-1\) counts the imaginary and real summands. For \(p\equiv5\pmod8\), \(b\) is even and nonzero: the number of imaginary summands in \(J\) is \((p-1)/2\), which is even, while the number of real summands is \((p-3)/2\), which is odd. Thus \(|b|\ge2\).

For a spectrum \(E\), the projection is convolution by \(K_E(t)/p\), where \(K_E(t)=\sum_{e\in E}\zeta^{et}\). Hence \(\|P_E\|_{\infty\to\infty}=p^{-1}\sum_{t\in G}|K_E(t)|\), with equality attained by a suitable choice of signs of the input function.

If \(E=C_0\cup C_1\), the four nonzero-frequency kernel values are \(\eta_j+\eta_{j+1}\). Each of the two absolute values appears twice. Because \(\operatorname{Re}(\eta_0+\eta_1)=-1/2\), the two squared magnitudes are
\[
|\eta_0+\eta_1|^2=\frac{p+1-b\sqrt p}4,\qquad
|\eta_1+\eta_2|^2=\frac{p+1+b\sqrt p}4.
\]
The value at zero is \(2m\), and each nonzero class occurs \(m\) times. This proves the adjacent formula, and multiplication of the entire frequency set by powers of \(g\) shows that all four adjacent pairs have identical norm.

For \(E=C_0\cup C_2\), the kernel values on nonzero frequencies are \((-1\pm\sqrt p)/2\), each appearing on two classes, by the quadratic Gauss sum. Together with \(K_E(0)=2m\), this gives the opposite formula, shared by the two opposite pairs.

Finally, \(p-1>0\) and
\[
\left(\sqrt{p+1-b\sqrt p}+\sqrt{p+1+b\sqrt p}\right)^2
=2(p+1)+2\sqrt{(p+1)^2-pb^2}.
\]
This is at most \(4p\) precisely when \(b^2\ge4\), and is strictly smaller if \(|b|>2\). The nonzero even integer \(b\) satisfies this universally. The tie occurs precisely at \(|b|=2\). Any representative of the two-square decomposition has the same absolute even coordinate. This completes the classification.

## Verification

The accompanying independent reconstruction script computes quartic classes, the Jacobi sum and both actual finite convolution norms by direct complex sums for all \(43\) primes \(p\equiv5\pmod8\) below \(1000\). It checks both radical formulas, norm ordering, tie conditions and the integer identity \(a^2+b^2=p\). Floating computations are consistency checks, not the universal proof above.

## Relationship to prior work

Quartic Gauss and Jacobi sums and the explicit evaluation of Gaussian periods are classical background. The sharp norm is a Fourier-algebra norm, related to the contemporary Fourier-ratio framework of Burstein, Iosevich and Nathan (2026). Unlike the cubic-residue single-subgroup projection studied in a related published mathematical record, this claim selects the norm-minimizing union among the six equal-cardinality **quartic** two-coset spectra and characterizes a sparse arithmetic tie family. Neither the general Fourier-ratio formulation nor the classical Gauss–Jacobi identity itself states that half-band optimization. The result follows by a specific comparison of the adjacent versus opposite additive character kernels and does not assert that the underlying character-sum evaluations are new.

## Limitations

This is an algebraic endpoint-norm theorem for a restricted, highly symmetric design family, not an unrestricted minimizer among all frequency sets. The parameterized equality condition \(p=a^2+4\) does not prove infinitely many such primes. Originality remains subject to checking older cyclotomic-number and idempotent-norm treatments that might encode the same adjacent-versus-opposite comparison. The calculations use complex floating point only as supplementary tests.

## References

1. W. Burstein, A. Iosevich, H. S. Nathan, *The Fourier Ratio: A Unifying Measure of Complexity for Recovery, Localization, and Learning*, 2026, arXiv:2601.16345, first public January 22, 2026. https://arxiv.org/abs/2601.16345
2. Classical Gauss–Jacobi identity and quartic character-sum theory; see *Jacobi sum*, https://en.wikipedia.org/wiki/Jacobi_sum, for definitions and the Gauss-sum product relation.
3. Z. Rudnick and E. Waxman, *Angles of Gaussian primes*, 2017, arXiv:1705.07498, for arithmetic context (not needed for the proof). https://arxiv.org/abs/1705.07498
4. Related research record, *Exact cubic-residue Lebesgue constants from Gaussian period arithmetic*, 2026/10/11/SCOPE-exact-cubic-residue-lebesgue-constants-from-gaussian-period-arit--36f40db19f8d
