# Universal phase frustration at the first resonance of four geometric Fourier tones

## Finding

Let \(b\ge 2\) be an integer, put \(p=b+1\), and equip \(\mathbb T=\{e^{it}:0\le t<2\pi\}\) with normalized Haar probability measure. For unit complex numbers \(a_0,a_1,a_2,a_3\), consider the geometric-frequency four-tone polynomial
\[
P_a(z)=\sum_{j=0}^{3}a_jz^{b^j},\qquad |a_j|=1.
\]
For \(r\ge1\), define the collision-free four-tone diagonal count
\[
B_r=\sum_{\substack{\alpha\in\mathbb Z_{\ge0}^4\\\alpha_0+\alpha_1+\alpha_2+\alpha_3=r}}
\left(\frac{r!}{\alpha_0!\alpha_1!\alpha_2!\alpha_3!}\right)^2.
\]
All even moments through half-order \(b\) are independent of the phases:
\[
\int_{\mathbb T}|P_a(z)|^{2r}\,dm(z)=B_r\quad (1\le r\le b).
\]
At the first possible resonant half-order \(p=b+1\), write \(\eta_j=a_j^b\overline{a_{j+1}}\) for \(j=0,1,2\). The exact identity is
\[
\boxed{\ \int_{\mathbb T}|P_a|^{2p}\,dm
=B_p+2p\operatorname{Re}(\eta_0\overline{\eta_1}+\eta_1\overline{\eta_2})
+2p^2\operatorname{Re}(\eta_0\overline{\eta_2})\ }.
\]
Consequently its **sharp full phase range** is
\[
\boxed{\quad B_p-2p^2-1\ \le\ \int_{\mathbb T}|P_a|^{2p}\,dm\ \le\ B_p+2p^2+4p.\quad}
\]
Every triple \((\eta_0,\eta_1,\eta_2)\in\mathbb T^3\) is realizable by such a coefficient vector. The lower endpoint holds exactly when
\[
|\eta_0+\eta_2|=\frac1p,
\qquad \eta_1=-p(\eta_0+\eta_2).
\]
The upper endpoint holds exactly when \(\eta_0=\eta_1=\eta_2\). The lower endpoint cannot be achieved by a coefficient vector whose entries are all roots of unity, including any finite root-of-unity phase alphabet. In contrast, restricting the coefficients to binary signs \(\{\pm1\}\) gives the exact minimum \(B_p-2p^2\), precisely one unit above the unrestricted optimum, for every \(b\ge2\).

For example, the unrestricted minima for bases \(b=2,3,4\) are respectively \(237,2683,31453\), whereas binary phases give \(238,2684,31454\). This is an unnormalized even-power moment: the numbers are not roots of \(L^{2p}\) norms.

## Assumptions and scope

The polynomial is on the continuous circle, not on a finite cyclic grid. Frequencies are the four distinct *positive* integers \(1,b,b^2,b^3\). Every coefficient has modulus one; no coefficient amplitudes are optimized. The exponent is the first phase-sensitive even order and depends on the integer base, namely \(2(b+1)\). The statements do not describe higher moments, where further carrying configurations occur. The diagonal value \(B_r\) counts the squared multinomial coefficients, not the distinct character sums. All equality classifications above are necessary and sufficient.

## Proof

**1. The first nontrivial additive relations.** A monomial in \(P_a^r\) is represented by a nonnegative multiplicity vector \(\alpha\in\mathbb Z_{\ge0}^4\) with total mass \(r\), character frequency \(\sum_j\alpha_jb^j\), and coefficient \(r!\prod_j a_j^{\alpha_j}/\alpha_j!\). Two different vectors \(\alpha,\beta\) can interfere in Parseval precisely when their character frequencies agree.

Cancel their common coordinatewise minimum, obtaining two disjoint multiplicity vectors, of the same residual mass \(s\le r\), with the same geometric sum. Let \(j\) be the smallest index in their combined support and orient the pair so that the first vector has a positive count at \(j\). The second vector has no mass at indices at most \(j\). Reduction modulo \(b^{j+1}\) forces the first count at \(j\) to be a positive multiple of \(b\), hence \(s\ge b\). At \(s=b\), the first vector must consist of exactly \(b\) atoms at \(j\), whereas the other \(b\) atoms are all at indices at least \(j+1\), making its sum strictly larger. Thus **no collisions occur for \(r\le b\)**.

When \(r=b+1\), cancellation and the preceding argument force \(s=b+1\) and exactly \(b\) copies of the \(j\)-th frequency on the first side. The one remaining atom has some index \(k\ge j+2\); the case \(k=j+1\) is too small to equal any sum of \(b+1\) atoms of frequencies at least \(b^{j+1}\). The resulting equality is
\[
b\,b^j+b^k=b^{j+1}+b\,b^{k-1},\qquad k\ge j+2. \tag{1}
\]
To see that the right side is *forced*, reduce the other side's number of atoms at index \(j+1\) modulo \(b\); it is either \(1\) or \(b+1\). In the latter case equality requires \(k=j+2\), and the stated right side is all \(b+1\) atoms at \(j+1\). In the former case the remaining \(b\) atoms sum to \(b^k\). Each must have index at most \(k-1\), so each contributes at most \(b^{k-1}\), and equality forces all \(b\) to equal \(b^{k-1}\). Hence (1) exhausts every nontrivial collision at the first resonant order. Because there are only four frequency indices \(0,1,2,3\), exactly the three pairs \((j,k)=(0,2),(1,3),(0,3)\) occur, with disjoint two-element fibers.

**2. Exact Fourier moment.** Parseval for \(P_a^p\) says that its squared \(L^2\) norm is the sum over Fourier frequencies of squared sums of multinomial-weighted monomials. The diagonal contributions total \(B_p\). In (1), the two sides have multinomial coefficients \(p\) and \(1\) when \(k=j+2\), and \(p\) and \(p\) when \(k=j+3\). Their phases differ by \(\eta_j\overline{\eta_{k-1}}\). The three disjoint collision fibers therefore contribute precisely
\[
2p\operatorname{Re}(\eta_0\overline{\eta_1}+\eta_1\overline{\eta_2})+2p^2\operatorname{Re}(\eta_0\overline{\eta_2}).
\]
This establishes the formula. For \(r\le b\), all fibers are singleton and the moment equals \(B_r\).

**3. Complete phase optimization.** The phases \(\eta_j\) are unconstrained: start with any \(a_0\in\mathbb T\) and recursively choose \(a_{j+1}=a_j^b/\eta_j\). Put \(R=|\eta_0+\eta_2|\), where \(0\le R\le2\). The correction to \(B_p\) is
\[
p^2(R^2-2)+2p\operatorname{Re}((\eta_0+\eta_2)\overline{\eta_1}).
\]
Its smallest possible value at fixed \(R\) is \(p^2R^2-2pR-2p^2\), attained for \(R>0\) exactly when \(\eta_1=-(\eta_0+\eta_2)/R\). Completing the square shows the unique optimal radius \(R=1/p\), with correction \(-2p^2-1\). Its largest value at fixed \(R\) is \(p^2R^2+2pR-2p^2\); this strictly increases for \(R\ge0\) and reaches \(2p^2+4p\) only at \(R=2\), when all three phases coincide. Continuous interpolation and compact connectedness yield the full interval of intermediate moments.

**4. Binary bound and root-of-unity obstruction.** If every \(a_j\in\{\pm1\}\), then every \(\eta_j\in\{\pm1\}\), so \(R\in\{0,2\}\). For \(R=0\) the moment is always \(B_p-2p^2\); for \(R=2\), even optimizing \(\eta_1\) gives \(B_p+2p^2-4p\), which is larger because \(p=b+1\ge3\). Recursion realizes \(R=0\) by binary coefficients, proving its exact optimum.

At any unrestricted minimum, \(R=1/p\), hence the unit complex number \(\zeta=\eta_0\overline{\eta_2}\) obeys
\[
\zeta+\overline\zeta=\frac1{p^2}-2.
\]
If all coefficients were roots of unity then \(\zeta\) would be a root of unity, so its sum with its reciprocal would be an algebraic integer. A rational algebraic integer must be an integer, but \(1/p^2-2\) is nonintegral for every integer \(p\ge3\). This contradiction proves the finite-root-of-unity obstruction. No unproved continuity-to-infinity step is used.

## Verification

The standalone standard-library script `verify_geometric_first_resonance.py` independently builds Fourier coefficients of powers by enumerating four-part compositions and summing exact multinomial contributions. It checks phase independence below the predicted threshold and the full resonant formula on all \(256\) four-tone Gaussian-unit phase assignments for bases two through five; it checks all sixteen binary assignments and the character-phase upper bound through base six. The exact integer-based tests return `EXACT_FIRST_RESONANCE_CHECKS_PASS 1129`. The theorem for every integer base and the prohibition on all finite root-of-unity alphabets follow from the proof, not from extrapolating the finite tests.

## Relationship to prior work

Prochno and Strzelecka (arXiv:2312.09137v1, first public December 14, 2023) analyze moderate deviations and cumulant estimates for lacunary trigonometric sums; their large-length probabilistic bounds do not imply this exact finite four-tone phase range. Aistleitner, Berkes and Tichy (arXiv:2301.05561v1, January 13, 2023) survey lacunary trigonometric sums and additive Diophantine relations; they do not present the three-collision minimum with continuous-phase cancellation. Ciccone and Gonçalves (arXiv:2208.09441v1, August 19, 2022) study Fourier extension from the geometric circle into a different ambient norm, not this exact continuous-circle moment minimization.

The published all-length dyadic fourth-moment rigidity result has a different moment order; its collision-free fourth-moment result for bases at least three does not cover the first later resonance. An exact general three-tone first-resonance formula lacks the third coupling phase and hence cannot yield the four-tone frustrated optimum. A four-consecutive-tone sixth-moment classification has a different support, and the one-defect four-character sixth-moment result requires exactly one triple-sum collision, unlike the three simultaneous collisions here. These are comparisons of hypotheses and implications, not claims that a missing title proves priority.

## Limitations

The statement concerns exactly four geometric frequencies, normalized Haar measure on the continuous circle, unit-modulus coefficients and the first phase-sensitive even moment. It does not optimize higher moments, unrestricted magnitudes, other frequency sets, or finite cyclic grids (where aliasing changes the collision structure). The exact baseline \(B_p\) grows rapidly; the universal one-unit improvement is mathematically exact, not a claim of substantial applied signal gain. Historical priority in older thin-set or lacunary moment literature is not independently established.

## References

1. Joscha Prochno and Marta Strzelecka, *Moderate deviation principles and Mod-Gaussian convergence for lacunary trigonometric sums*, arXiv:2312.09137v1, first public 2023-12-14. https://arxiv.org/abs/2312.09137 .
2. Christoph Aistleitner, Istvan Berkes and Robert Tichy, *Lacunary sequences in analysis, probability and number theory*, arXiv:2301.05561v1, first public 2023-01-13. https://arxiv.org/abs/2301.05561 .
3. Valentina Ciccone and Felipe Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1, first public 2022-08-19. https://arxiv.org/abs/2208.09441 .
4. *Resonance-chain phase rigidity in lacunary fourth-moment extremizers*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-resonance-chain-phase-rigidity-in-lacunary-fourth-moment-extremi--2b706c80a337 .
5. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79 .
6. *Exact sixth-moment flatness of four unimodular Fourier taps*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-sixth-moment-flatness-of-four-unimodular-fourier-taps--cd075328c111 .
7. *Sharp sixth-moment norm for one balanced triple-sum defect*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-norm-for-one-balanced-triple-sum-defect--927de11a37e9 .
