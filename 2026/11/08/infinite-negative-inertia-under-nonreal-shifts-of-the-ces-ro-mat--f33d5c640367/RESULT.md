# Infinite negative inertia under nonreal shifts of the Cesàro matrix

## Finding

For each complex parameter \(\alpha=u+iv\) with \(u>-1\), define on \(\ell^2(\mathbb N_0)\) the bounded generalized Cesàro operator
\[
 (C_\alpha x)_n=\frac{1}{n+1+\alpha}\sum_{j=0}^n x_j.
\]
Write \(Q_\alpha=C_\alpha^*C_\alpha-C_\alpha C_\alpha^*\). The operator \(Q_\alpha\) is compact, self-adjoint, and Hilbert–Schmidt. Its **negative index**, the supremum of dimensions of subspaces on which its quadratic form is strictly negative, obeys the exact trichotomy
\[
 \operatorname{ind}_{-}(Q_\alpha)=
 \begin{cases}
 0,& v=0,\ u\ge0,\\
 1,& v=0,\ -1<u<0,\\
 \infty,& v\ne0.
 \end{cases}
\]
In particular, a negative real shift has exactly one strictly negative eigenvalue, whereas **every nonreal shift**, no matter how small its imaginary part, has infinitely many strictly negative eigenvalues accumulating only at zero. The real nonnegative case has no strictly negative eigenvalues. Multiplicities are counted.

For each fixed real \(u>-1\), these nonreal examples approach the real-shift operator even in Hilbert–Schmidt perturbation norm:
\[
 \|C_{u+iv}-C_u\|_{\mathcal S_2}^2\le |v|^2\sum_{n=0}^\infty\frac{n+1}{(n+1+u)^4}\longrightarrow0\quad(v\to0).
\]

## Assumptions and scope

All operators act on the complex Hilbert space \(\ell^2(\mathbb N_0)\), with inner product linear in the second variable. The parameter domain is the open half-plane \(\operatorname{Re}\alpha>-1\); no assertion is made for the boundary or the opposite half-plane. The negative index is a quadratic-form invariant; compactness then identifies it with the total multiplicity of strictly negative eigenvalues. The theorem concerns generalized Cesàro operators of **order one only**, not higher integer orders.

## Proof

**Step 1: boundedness and a dense finite-support right inverse.** Since \(n+1+u\ge c(n+1)\), with \(c=\min(1,1+u)>0\), the absolute value of every nonzero matrix entry of \(C_\alpha\) is at most \(1/[c(n+1)]\). The classical discrete Hardy averaging operator is bounded on \(\ell^2\), so \(C_\alpha\) is bounded. On finitely supported sequences define the difference operator
\[
 Le_j=(j+1+\alpha)(e_j-e_{j+1}).
\]
Direct telescoping shows \(C_\alpha Le_j=e_j\). If a square-summable vector is orthogonal to \(L(c_{00})\), its coordinates are constant (the conjugate nonzero factors can be cancelled); it must therefore vanish. Hence \(L(c_{00})\) is dense. Also \(\operatorname{ran}C_\alpha\) contains \(c_{00}\), and is dense.

**Step 2: an explicit bounded intertwiner.** Let \(B_0=C_\alpha^*L\) on \(c_{00}\). Its matrix entries are
\[
 (B_0)_{ij}=
 \begin{cases}
 \displaystyle\frac{j+1+\alpha}{(j+1+\overline\alpha)(j+2+\overline\alpha)},& i\le j,\\[4pt]
 \displaystyle-\frac{j+1+\alpha}{j+2+\overline\alpha},&i=j+1,\\[4pt]
 0,&i>j+1.
 \end{cases}
\]
The part above and on the diagonal has entries of modulus \(1/|j+2+\alpha|\le C/(j+1)\). It is bounded by the Copson inequality (the adjoint of discrete Hardy averaging). The remaining one-step weighted shift has bounded weights. Consequently \(B_0\) extends to a bounded operator \(B\). The identity \(BC_\alpha=C_\alpha^*\) holds on the dense set \(L(c_{00})\) and hence everywhere. Therefore
\[
 Q_\alpha=C_\alpha^*(I-B^*B)C_\alpha.
\]

**Step 3: exact phase-normalized Gram matrix.** Define \(A=I-B^*B\), and set
\[
 d_j=\frac1{|j+2+\alpha|},\qquad
 \phi_j=\frac{j+1+\alpha}{j+1+\overline\alpha}\frac{j+2+\alpha}{|j+2+\alpha|}.
\]
Then \(|\phi_j|=1\), and direct multiplication of the two columns of \(B\) gives
\[
 A_{ij}=\overline{\phi_i}\phi_jd_id_j
 \begin{cases}
 i+2+2u,&i=j,\\
 \alpha,&i<j,\\
 \overline\alpha,&i>j.
 \end{cases}
\]
For example, the sole overlapping entries at \(i<j\) yield the stated upper-triangular coefficient after the common phase is factored out. The diagonal is \((i+2+2u)/|i+2+\alpha|^2\). The off-diagonal entries are dominated in modulus by \(|\alpha|/[|i+2+\alpha|\,|j+2+\alpha|]\). Hence the sum of their squared moduli is finite, as is the sum of the squared diagonal entries. Thus \(A\) is Hilbert–Schmidt. Because \(Q_\alpha=C_\alpha^*AC_\alpha\), the self-commutator is Hilbert–Schmidt and compact.

The diagonal change of variables \(c_j=d_j\phi_jx_j\) maps \(c_{00}\) bijectively to itself. By the displayed Gram identity, on finite sequences
\[
 \langle Ax,x\rangle=\mathfrak q_\alpha(c),\qquad
 \mathfrak q_\alpha(c)=
 \sum_{j\ge0}(j+2+u)|c_j|^2
 +u\left|\sum_{j\ge0}c_j\right|^2
 -2v\,\operatorname{Im}\!\sum_{i<j}\overline c_i c_j.
\]
The bounded change of variables is not asserted to have a bounded inverse on all of \(\ell^2\): only its bijectivity on finite-support vectors is needed. Since finite-support vectors are dense, \(A\) and this form have the same negative index. Since \(\operatorname{ran}C_\alpha\) is dense and \(Q_\alpha=C_\alpha^*AC_\alpha\), the negative indices of \(A\) and \(Q_\alpha\) agree. Indeed, any finite-dimensional negative-definite subspace of either quadratic form can be approximated within the relevant dense range while preserving strict negativity; the reverse index inequality follows by pullback.

**Step 4: the real-axis cases.** For \(v=0\), the form reduces to a strictly positive diagonal form plus the real rank-one term \(u|\sum c_j|^2\). When \(u\ge0\), it is positive. When \(-1<u<0\), its negative index is at most one. To produce a negative vector, choose, for \(0\le j\le N\),
\[
 c_j=\frac{1}{H_N(j+2+u)},\quad
 H_N=\sum_{j=0}^{N}\frac1{j+2+u},
\]
with all later coordinates zero. Then \(\sum c_j=1\) and \(\mathfrak q_\alpha(c)=H_N^{-1}+u\), which is negative for sufficiently large \(N\), since \(H_N\to\infty\). Hence the negative index is exactly one.

**Step 5: every nonreal shift has infinite negative index.** Let \(v\ne0\) and \(\sigma=\operatorname{sgn}v\). Take four successive disjoint finite intervals \(I_1<I_2<I_3<I_4\) and define \(H_t=\sum_{j\in I_t}(j+2+u)^{-1}\). Since the harmonic tail diverges, these intervals can be chosen with every \(H_t\) arbitrarily large. On \(I_t\) put
\[
 c_j=\frac{m_t}{H_t(j+2+u)},\qquad
 (m_1,m_2,m_3,m_4)=(1,i\sigma,-1,-i\sigma),
\]
with zero elsewhere. The four block sums are exactly \(m_t\), so \(\sum_j c_j=0\). Within each block, the imaginary cross term vanishes because all entries have the same phase; between blocks,
\[
 \operatorname{Im}\sum_{i<j}\overline c_i c_j
 =\operatorname{Im}\sum_{s<t}\overline m_s m_t=2\sigma.
\]
Consequently
\[
 \mathfrak q_\alpha(c)=\sum_{t=1}^4H_t^{-1}-4|v|<0
\]
when the four harmonic masses are chosen sufficiently large. Construct as many of these witnesses as desired, one after another on entirely disjoint sets of four ordered intervals. Every such witness has total sum zero. Mixed diagonal terms vanish because the supports are disjoint, and the mixed off-diagonal terms vanish because each witness has zero total sum. The resulting vectors therefore span negative-definite subspaces of every finite dimension. Thus the negative index is infinite. Compact self-adjoint spectral theory gives infinitely many negative eigenvalues, with zero as their only possible accumulation point.

**Step 6: perturbative smallness.** Subtract the two lower triangular matrices entry by entry. The squared Hilbert–Schmidt norm is the sum over rows of \(n+1\) identical squared differences; the bound in the finding follows by factoring \(|v|\) and using \(|n+1+u+iv|\ge n+1+u\). The indicated inverse-fourth-power series converges for every \(u>-1\). Thus the infinite-negative-index phenomenon persists under arbitrarily small Hilbert–Schmidt perturbations of any real member of the family.

## Verification

The standalone script `checks/check_complex_cesaro.py` compares, for six real and nonreal parameters and matrix sizes up to twenty, every entry of the explicitly computed finite Gram matrix \(I-B^*B\) with its phase-normalized formula. It also checks concrete four-block negative witnesses for both signs of the imaginary shift and real-negative harmonic witnesses. Run `python3 checks/check_complex_cesaro.py` from the directory containing this document. It requires Python 3 standard library only. These tests check algebra and examples; the all-parameter and infinite-dimensional statements follow from the five proof steps above.

## Relationship to prior work

Ma's 2026 theorem establishes the hyponormality classification for **real** shifts and arbitrary positive integer Cesàro orders. The real-axis portion of the order-one result is known in its positivity content; the **new asserted contribution** is the complete **negative-index trichotomy**, most notably the infinite negative inertia for every nonreal complex shift, which the real-parameter theorem does not address. Ma's general finite-difference intertwining method motivates the bounded-intertwiner reduction but its restriction to real parameters neither implies nor treats the imaginary cross-term mechanism in Step 5.

Gallardo-Gutiérrez and Partington consider Rhaly matrices with arbitrary complex coefficient sequences, but their 2025 study concerns spectra, invariant subspaces, and related structure rather than a nonreal-shift negative-index classification. Rhaly's older generalized Cesàro hyponormality work is likewise concerned with real shifts and the first few integer orders. This result concerns a specific new spectral-inertia property rather than a broad classification for arbitrary complex Rhaly coefficients.

## Limitations

The theorem is restricted to \(\operatorname{Re}\alpha>-1\), to the order-one family, and to the total negative index; it gives neither individual negative eigenvalue magnitudes nor optimal Schatten indices below Hilbert–Schmidt. Independent mathematical validation has not been performed. A general theorem about complex terraced matrices or compact commutator inertia under an alternative name could imply some part of the result; mathematical publication priority remains subject to further specialist checking.

## References

1. Yicen Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1 (first public 2026-09-18), https://arxiv.org/html/2610.00193v1.
2. Eva A. Gallardo-Gutiérrez and Jonathan R. Partington, *Rhaly operators: more on generalized Cesàro operators*, Annali di Matematica Pura ed Applicata 204 (2025), 2049–2063, https://doi.org/10.1007/s10231-025-01560-5.
3. H. C. Rhaly Jr., *Supraposinormality and hyponormality for the generalized Cesàro matrices of order two*, arXiv:1602.01408 (2016), https://arxiv.org/abs/1602.01408.
