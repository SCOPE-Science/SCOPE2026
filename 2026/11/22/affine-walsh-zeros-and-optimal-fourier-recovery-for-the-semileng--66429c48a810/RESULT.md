# Affine Walsh zeros and optimal Fourier recovery for the semilength-five Catalan matroid

## Finding

Let \(\mathcal D_5\subseteq\mathbb F_2^{10}\) be the 42 incidence vectors of up-step positions of Dyck paths of semilength five (ten steps), with positions numbered \(1,\ldots,10\). Define the unnormalized Walsh multiplier
\[
\Lambda(s)=\sum_{u\in\mathcal D_5}(-1)^{\langle s,u\rangle},\qquad s\in\mathbb F_2^{10}.
\]
The **complete zero locus** is the affine codimension-three space
\[
\boxed{\Lambda(s)=0\quad\Longleftrightarrow\quad
s_2+s_3=s_8+s_9=s_4+s_5+s_6+s_7=1\pmod2.}
\]
Consequently counting convolution \(Tf=\mathbf1_{\mathcal D_5}*f\) has exactly 128 zero Walsh eigenvalues, rank 896 on the 1024-dimensional function space, sharp least nonzero singular value 2, and surviving \(\ell^2\) condition number 21. Every vanishing Walsh character selects at least three step coordinates; exactly 16 characters of weight three vanish. Among odd positive semilengths, five is the first for which the Catalan-matroid basis convolution is singular.

Set \(a=e_2+e_3\), \(b=e_8+e_9\), \(c=e_4+e_5+e_6+e_7\), and \(U=\operatorname{span}_{\mathbb F_2}\{a,b,c\}\). The unique translation-invariant projection \(Q\) onto \(\operatorname{ran}T\) has convolution kernel supported exactly on the eight points of \(U\):
\[
q(0)=\frac78,\qquad
q(ua+vb+wc)=-\frac18(-1)^{u+v+w}
\quad\text{for }(u,v,w)\in\mathbb F_2^3\setminus\{0\},
\]
and \(q(x)=0\) outside \(U\). This projection is **globally optimal**, even among real or complex linear projections without translation symmetry:
\[
\boxed{\min_{P^2=P,\,\operatorname{ran}P=\operatorname{ran}T}\|P\|_{\ell^1\to\ell^1}
=\min_{P^2=P,\,\operatorname{ran}P=\operatorname{ran}T}\|P\|_{\ell^\infty\to\ell^\infty}=\frac74.}
\]

## Assumptions and scope

The group is \(G=\mathbb F_2^{10}\), with coordinatewise XOR and standard dot-product pairing. A Dyck path has five upward and five downward steps, all prefix heights nonnegative, and endpoint height zero. The incidence vector has coordinate one precisely for an upward step. Convolution and Walsh multipliers are unnormalized; the \(\ell^p\) norms use counting measure on \(G\). The claims are exact for the Catalan matroid of semilength five; no all-order singularity classification is asserted. The basis family is the classical Catalan matroid family established by Ardila [1].

## Proof

**1. Exact signed-ballot recurrence.** For a fixed frequency \(s\), let \(\varepsilon_i=(-1)^{s_i}\). Put \(F_0(0,0)=1\), all other entries zero, with \(F_j(h,r)\) counting signed admissible prefixes of length \(j\), height \(h\), and \(r\) up-steps. From each nonzero state \((h,r)\), an up-step is allowed if \(r<5\), contributing \(\varepsilon_{j+1}F_j(h,r)\) to \(F_{j+1}(h+1,r+1)\), and a down-step is allowed if \(h>0\), contributing \(F_j(h,r)\) to \(F_{j+1}(h-1,r)\). Then \(\Lambda(s)=F_{10}(0,5)\), by a direct partition of all legal paths by their last step. This recurrence is an exact exhaustive calculation, not a numerical approximation.

Every such path begins upward and ends downward. Consequently \(s_1\) changes only the overall sign, and \(s_{10}\) has no effect. For the 256 normalized frequencies with \(s_1=s_{10}=0\), put \(\alpha=s_2+s_3\), \(\beta=s_8+s_9\), and \(\gamma=s_4+s_5+s_6+s_7\), all modulo two. The exact recurrence yields the following complete table; each row represents 32 normalized frequencies, and each entry is an eigenvalue followed by its multiplicity.

| \((\alpha,\beta,\gamma)\) | Signed multipliers and multiplicities |
|---|---|
| \((0,0,0)\) | \(-14:8,\ -6:8,\ 2:8,\ 10:6,\ 42:2\) |
| \((0,0,1)\) | \(-12:4,\ -4:12,\ 4:12,\ 12:4\) |
| \((0,1,0)\) | \(-2:28,\ 14:4\) |
| \((0,1,1)\) | \(-4:16,\ 4:16\) |
| \((1,0,0)\) | \(-14:4,\ 2:28\) |
| \((1,0,1)\) | \(-4:16,\ 4:16\) |
| \((1,1,0)\) | \(-6:8,\ 2:24\) |
| \((1,1,1)\) | \(0:32\) |

The table is reproducible from the recurrence just stated, requiring only ten updates for each of 256 finite sign vectors. Its last row and the absence of other zero entries prove the **if and only if** zero characterization. The two free endpoint frequency bits multiply the 32 zeros by four, so there are 128 zeros. A Walsh character basis diagonalizes \(T\), proving rank 896. The table proves the sharp nonzero gap 2 and largest magnitude 42. The affine parity equations force at least one selected position from each of three disjoint groups; choosing one from each gives \(2\cdot2\cdot4=16\) weight-three zeros. For semilength one, there is one Dyck path; for semilength three, there are five. Their odd base counts force all signed sums to be odd and nonzero, proving the first-odd-semilength assertion.

**2. Projection and its optimality.** Write \(Z\) for the affine zero set. Its direction space is \(U^\perp\), and a representative is \(s_0=e_2+e_4+e_8\). Fourier inversion gives
\[
q(x)=\delta_0(x)-2^{-10}\sum_{s\in Z}(-1)^{\langle s,x\rangle}.
\]
Character orthogonality on \(U^\perp\) makes the sum vanish unless \(x\in U\), in which case it equals \(128(-1)^{\langle s_0,x\rangle}\). This is exactly the displayed eight-point kernel, whose absolute mass is \(7/8+7/8=7/4\). A convolution operator on a finite group has both \(\ell^1\)- and \(\ell^\infty\)-norm equal to the absolute mass of its kernel (equality follows from a delta input, or from a sign-chosen test input).

For **any** bounded real or complex linear projection \(P\) onto \(\operatorname{ran}T\), average its conjugates under all translations of \(G\). Since the range is translation invariant and each conjugate is the identity on that range, the average still fixes the range pointwise and has image contained in it; hence it is again a projection. Its norm does not exceed \(\|P\|\). It is translation invariant and therefore diagonal in the one-dimensional Walsh character spaces; the only possible projection with this range is the multiplier \(\mathbf1_{G\setminus Z}\), namely \(Q\). Hence every competing projection has endpoint norm at least \(7/4\), and \(Q\) attains it.

## Verification

Run `python3 verify_catalan5_recovery.py` with standard Python 3. It independently enumerates all 42 bases by selecting five of ten positions and testing ballot prefixes, and by a separate recursion. It evaluates all 1024 multipliers three ways: direct signed sums, signed height-state dynamic programming, and an integer Walsh--Hadamard transform. It verifies the full signed histogram, the exact eight-row parity-class table, all 128 zero-frequency masks, Parseval's identity, the spectral gap, the eight-point projection kernel, its Fourier multiplier, and its exact \(7/4\) norm. Success marker: `CATALAN5_AFFINE_WALSH_ZERO_LOCUS_AND_SHARP_PROJECTION_PASS`. The finite enumerations are exhaustive for semilength five and establish no claim for larger semilengths.

## Relationship to prior work

Ardila [1] defines precisely the up-step base set and proves its matroid structure and self-duality, but not this Boolean convolution spectrum. Cohen, Tetali and Yeliussizov [2] study negative correlation and the basis-exchange random walk on these paths, rather than ambient XOR convolution. A published position-by-position Catalan-matroid theorem [3] derives the complete signed Walsh transform **modulo four**, explicitly leaving the real zeros and exact rank undetermined. A separate study of semilength-four degree-bounded Walsh **sampling Gram matrices** [4] addresses recovery from a different operator, and a study of height-at-most-three Dyck paths [5] uses a strict subset of the 42 paths at semilength five (34 paths), so its all-order theorem does not imply this zero set. Defant et al. [6] derive a general projection constant formula for Fourier subspaces, and that general averaging principle is credited; the new specific input here is the exact affine Fourier-zero locus of the full semilength-five Catalan matroid. Neither the general projection theorem nor the modulo-four residues identify these 128 specific exact zeros. The zero-locus formula and resulting eight-shift recovery kernel are the assessed contribution, not the existence of the Catalan matroid or the general projection principle.

## Limitations

This is a complete theorem for the semilength-five finite object, not an infinite family classification. The exact zero-locus step is certified by a fully specified integer recurrence over 256 normalized cases and independently exhaustive implementations, rather than a closed-form all-semilength factorization. The endpoint constant is a consequence of the new affine zero-locus formula and a general projection principle. The comparison cannot exclude unindexed historical calculations of the same 42-path signed enumerator. No independent mathematical audit has been performed.

## References

1. Federico Ardila, *The Catalan matroid*, arXiv:math/0209354, first public submission 2002-09-25, https://arxiv.org/abs/math/0209354.
2. Emma Cohen, Prasad Tetali and Damir Yeliussizov, *Lattice Path Matroids: Negative Correlation and Fast Mixing*, manuscript dated 2015-06-10, https://tetali.math.gatech.edu/PUBLIS/Catalan_CTY.pdf.
3. *A binary-digit parity law and the mod-four Walsh spectrum of Catalan matroid bases*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-binary-digit-parity-law-and-the-mod-four-walsh-spectrum-of-cat--84ddf083bb47.
4. *Sharp quadratic and cubic Walsh sampling spectra at the first Catalan-matroid tomography obstruction*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-quadratic-and-cubic-walsh-sampling-spectra-at-the-first-ca--bd8b6ff286b5.
5. *Fourier recovery and a cubic minimum-zero threshold for height-three Dyck paths*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-fourier-recovery-and-a-cubic-minimum-zero-threshold-for-height-t--51de04f7e6b4.
6. Andreas Defant, Daniel Galicer, Martín Mansilla, Mieczysław Mastyło and Santiago Muro, *Asymptotic insights for projection, Gordon--Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233, first public submission 2023-02-01, https://arxiv.org/abs/2302.00233.
