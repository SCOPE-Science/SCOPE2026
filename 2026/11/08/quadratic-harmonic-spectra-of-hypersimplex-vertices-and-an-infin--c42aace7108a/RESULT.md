# Quadratic harmonic spectra of hypersimplex vertices and an infinite Pell family of exact designs

## Finding
Let \(n\geq5\) and \(2\leq k\leq\lfloor n/2\rfloor\). Normalize the centered \(k\)-subset indicator vectors to unit length in the \((n-1)\)-dimensional zero-sum subspace. On real homogeneous harmonic quadratics, the equal-weight evaluation frame has *exactly two* squared singular values:
\[
\begin{aligned}
\Lambda_1(n,k)&=\frac{n(n-2k)^2}{(n-2)k^2(n-k)^2}\binom{n-2}{k-1},&&\text{multiplicity }n-1,\\
\Lambda_2(n,k)&=\frac{2n^2}{k^2(n-k)^2}\binom{n-4}{k-2},&&\text{multiplicity }\frac{n(n-3)}2.
\end{aligned}
\]
The kernel is zero exactly when \(n\ne2k\). In that case, the optimal Euclidean sampling condition number is \(\sqrt{\max(\Lambda_1,\Lambda_2)/\min(\Lambda_1,\Lambda_2)}\).

The frame is tight (both squared singular values equal) **if and only if**
\[
 k(n-k)=\frac{n(n+1)}6.
\]
Every admissible tight pair is uniquely parametrized by
\[
 (n-1)+(n-2k)\sqrt3=(2+\sqrt3)^r,\qquad r=2,3,\ldots.
\]
The first pairs are \((8,2)\), \((27,6)\), \((98,21)\), and \((363,77)\). Thus these normalized hypersimplex vertex configurations form an infinite explicit family of equal-weight **real projective \(2\)-designs** (equivalently real spherical \((2,2)\)-designs) and exactly conditioned quadratic-harmonic sampling frames. The smallest case \((8,2)\), identified with the classical \(28\) equiangular lines in \(\mathbb R^7\), is previously known; the claim is the full two-sector spectrum and the Pell classification across all parameters.

## Assumptions and scope
Use the real Hilbert space
\[
 V=\{v\in\mathbb R^n:\sum_{i=1}^n v_i=0\},\qquad d=n-1,
\]
with the standard inner product and orthogonal projector \(P=I-\mathbf1\mathbf1^\top/n\). For each \(k\)-subset \(I\subseteq[n]\), let
\[
 u_I=\sqrt{\frac{n}{k(n-k)}}\left(\mathbf1_I-\frac kn\mathbf1\right)\in V.
\]
Every \(u_I\) has norm one. The real Hilbert space of degree-two spherical harmonics is represented by
\[
 \mathcal H=\{Q\in\mathbb R^{n\times n}:Q=Q^\top,\ Q\mathbf1=0,\ \operatorname{tr}Q=0\},
\]
with Frobenius inner product \(\langle Q,R\rangle=\operatorname{tr}(QR)\); its dimension is \(h=(n-2)(n+1)/2\). Define \(\mathsf S_{n,k}:\mathcal H\to\mathbb R^{\binom nk}\) by \((\mathsf S_{n,k}Q)_I=u_I^\top Q u_I\). Singular values and frame bounds use *unweighted counting measure* on the sample coordinates. Statements also hold for the complexification of this real frame, but not for arbitrary complex Hermitian quadratic data.

## Proof
**1. Two orthogonal sectors.** There is an orthogonal direct sum \(\mathcal H=\mathcal U\oplus\mathcal W\), where
\[
 \mathcal U=\{P\operatorname{diag}(x)P: x\in V\},\qquad
 \mathcal W=\{W=W^\top:W\mathbf1=0,\ W_{ii}=0\ \text{for every }i\}.
\]
The map \(x\mapsto P\operatorname{diag}(x)P\) is injective for \(n\ge5\), with squared norm \((n-2)\|x\|^2/n\), so \(\dim\mathcal U=n-1\). The zero-row-sum conditions on symmetric off-diagonal matrices have rank \(n\) for \(n\ge3\), giving \(\dim\mathcal W=\binom n2-n=n(n-3)/2\). Each \(W\) is orthogonal to each \(P\operatorname{diag}(x)P\), since \(PWP=W\) and \(W\) has zero diagonal. Dimensions sum to \(h\).

**2. Diagonal sector.** Write \(Q_x=P\operatorname{diag}(x)P\), with \(\sum_i x_i=0\). A direct coordinate calculation gives
\[
 u_I^\top Q_xu_I=\frac{n-2k}{k(n-k)}\sum_{i\in I}x_i,
\qquad\|Q_x\|_F^2=\frac{n-2}{n}\sum_i x_i^2.
\]
Counting each singleton and ordered pair among all \(k\)-subsets yields
\[
 \sum_{|I|=k}\left(\sum_{i\in I}x_i\right)^2=\binom{n-2}{k-1}\sum_i x_i^2.
\]
Thus \(\|\mathsf S_{n,k}Q_x\|^2=\Lambda_1\|Q_x\|_F^2\).

**3. Zero-diagonal sector.** For \(W\in\mathcal W\), using \(W\mathbf1=0\) gives
\[
 u_I^\top Wu_I=\frac{2n}{k(n-k)}\sum_{\{i,j\}\subseteq I,\ i<j}W_{ij}.
\]
Write \(w_{ij}=W_{ij}\). Because every row sum and hence the total edge sum vanish, sums of \(w_ew_f\) over distinct edges meeting at one vertex and over disjoint edge pairs are respectively \(-\sum_e w_e^2\) and \(\tfrac12\sum_e w_e^2\). Grouping subset-incidence pairs by these three intersection types yields
\[
 \sum_{|I|=k}\left(\sum_{\{i,j\}\subseteq I}w_{ij}\right)^2
 =\left[\binom{n-2}{k-2}-2\binom{n-3}{k-3}+\binom{n-4}{k-4}\right]\sum_e w_e^2
 =\binom{n-4}{k-2}\sum_e w_e^2.
\]
Binomial coefficients with out-of-range lower entries are zero. Since \(\|W\|_F^2=2\sum_e w_e^2\), this proves \(\|\mathsf S_{n,k}W\|^2=\Lambda_2\|W\|_F^2\).

**4. No mixed block.** The cross inner product of the two sample vectors reduces to a multiple of
\[
 \sum_{i<j}W_{ij}(x_i+x_j)=\sum_i x_i\sum_{j\ne i}W_{ij}=0.
\]
Hence the two mutually orthogonal sectors remain orthogonal after sampling. Their dimensions exhaust \(\mathcal H\), completing the full spectral proof, including the zero eigenvalue for \(n=2k\).

**5. Tightness and classification.** Comparing the two explicit positive eigenvalues and simplifying the ratio of binomial coefficients gives
\[
 \frac{\Lambda_1}{\Lambda_2}
 =\frac{(n-2k)^2(n-3)}{2n(k-1)(n-k-1)}.
\]
Equality is equivalent, after multiplying out, to \(6k(n-k)=n(n+1)\). With \(x=n-1\) and \(m=n-2k\), this becomes \(x^2-3m^2=1\). Under the stated ranges, \(x>0\), \(m\ge0\), and \(r\ge2\). The standard positive integer solutions of this Pell equation are \(x+m\sqrt3=(2+\sqrt3)^r\). Conversely, the recurrence \(x'=2x+3m\), \(m'=x+2m\) preserves integrality and parity, and starting at \(r=2\) produces admissible \(k=(x+1-m)/2\ge2\), proving both necessity and sufficiency.

**6. Projective design and reconstruction.** Permutation symmetry gives \(\tfrac1M\sum_{|I|=k}u_Iu_I^\top=P/d\), where \(M=\binom nk\). At tight parameters, taking the trace of \(\mathsf S_{n,k}^*\mathsf S_{n,k}\) gives the common eigenvalue \(\lambda=2M/[d(d+2)]\). Consequently every traceless symmetric \(Q\) satisfies
\[
 \frac1M\sum_{|I|=k}(u_I^\top Q u_I)^2=\frac{2}{d(d+2)}\|Q\|_F^2.
\]
Together with the second-moment identity and polarization, this is the uniform-sphere fourth-moment identity \(\mathbb E(v^\top Bv)^2=[2\operatorname{tr}(B^2)+(\operatorname{tr}B)^2]/[d(d+2)]\) for all real symmetric \(B\) on \(V\). This is precisely the real projective \(2\)-design property. The sharp reconstruction formula is
\[
 Q=\frac{d(d+2)}{2M}\sum_{|I|=k}(u_I^\top Q u_I)\left(u_Iu_I^\top-\frac Pd\right),\qquad Q\in\mathcal H.
\]

## Verification
The independent, standard-library-only script `checker.py` represents the projective sample Gram matrix over exact rational numbers:
\[
 G_{I,J}=\left(\frac{n|I\cap J|-k^2}{k(n-k)}\right)^2-\frac1{n-1}.
\]
It verifies the cubic matrix identity \(G^3-(\Lambda_1+\Lambda_2)G^2+\Lambda_1\Lambda_2G=0\), the two predicted spectral power sums, and the zero row-sums for five small parameter pairs. It also verifies the Pell recurrence through eight steps and enumerates all potential tight parameters with \(5\le n\le200\) for comparison. Executing `python checker.py` returned `EXACT_FRAME_CHECKS_PASS 14764`. Finite exact computation supports but does not replace the universal proof above.

## Relationship to prior work
The classical framework of spherical harmonic sampling and spherical tight framelets appears in Xiao and Zhuang, *Spherical framelets from spherical designs* (arXiv:2303.05365, first posted 2023-03-09), which addresses spherical design computation and framelet reconstruction rather than the present complete Johnson-orbit quadratic spectrum or Pell classification. Hughes and Waldron, *Spherical (t,t)-designs with a small number of vectors* (2018), give the general projective design framework and list the known \(28\)-line configuration in \(\mathbb R^7\); that instance of the present family is not claimed as new. Bachoc and Vallentin (arXiv:0708.3947) analyze the ten-point Petersen hypersimplex configuration and its optimal spherical-code property, not the all-parameter quadratic evaluation frame. These comparisons distinguish the exact statements, not just titles. An undiscovered general association-scheme result could imply the spectrum; historical priority is not independently certified.

## Limitations
Only normalized equal-weight full orbits of all \(k\)-subsets are covered. The squared singular values depend on unweighted counting measure, real traceless symmetric quadratic forms, and the stated range \(n\ge5\), \(2\le k\le\lfloor n/2\rfloor\). Tight projective \(2\)-design does not imply an un-antipodalized ordinary spherical \(4\)-design. The method neither yields optimality among arbitrary non-orbit point configurations nor noise-robust statistical guarantees. At the antipodal-complement case \(n=2k\), a nontrivial kernel remains.

## References
1. Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365 (first posted March 9, 2023); *SIAM Journal on Imaging Sciences* 16 (2023), 2072–2104, DOI:10.1137/22M1542362.
2. D. Hughes and S. Waldron, *Spherical (t,t)-designs with a small number of vectors* (2018), https://www.math.auckland.ac.nz/~waldron/Preprints/Numerical-t-designs/numerical-t-designs.pdf.
3. C. Bachoc and F. Vallentin, *Optimality and uniqueness of the (4,10,1/6) spherical code*, arXiv:0708.3947 (2007).
4. A. Elzenaar and S. Waldron, *Putatively optimal projective spherical designs with little apparent symmetry*, *Journal of Combinatorial Designs* 33 (2025), 222–234, DOI:10.1002/jcd.21979 (broader comparative context).
