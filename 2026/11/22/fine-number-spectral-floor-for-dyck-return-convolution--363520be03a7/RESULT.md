# Fine-number spectral floor for Dyck-return convolution

## Finding

For each integer \(n\ge1\), let \(\mathcal D_n\) be all Dyck paths of semilength \(n\). Associate to a path \(P\) its interior return vector \(r(P)\in\mathbb F_2^{n-1}\), with coordinate \(j\) equal to one exactly when the path returns to height zero after step \(2j\), for \(1\le j<n\). Define the counting kernel \(\mu_n(v)=|\{P\in\mathcal D_n:r(P)=v\}|\), and convolution \(T_nf=\mu_n*f\) on the Boolean group.

Let \(C_n=\binom{2n}{n}/(n+1)\), and let \(f_j\) be the Fine numbers \(f_0,f_1,f_2,\ldots=1,0,1,2,6,18,57,\ldots\). Then the exact smallest and largest unnormalized Walsh multipliers are
\[
\min_{\xi\in\mathbb F_2^{n-1}}\widehat\mu_n(\xi)=f_{n-1},\qquad
\max_{\xi\in\mathbb F_2^{n-1}}\widehat\mu_n(\xi)=C_n.
\]
The minimum is attained at the character selecting every interior return coordinate; there may be other minimizers. Consequently \(T_n\) is singular **only** for \(n=2\), when its rank and nullity are both one. It is strictly positive definite for every \(n\ge3\) (and for the zero-dimensional case \(n=1\)). For \(n\ge3\), its sharp \(\ell^2\) condition number equals \(C_n/f_{n-1}\), and
\[
\lim_{n\to\infty}\frac{C_n}{f_{n-1}}=9.
\]
For probability-normalized convolution \(T_n/C_n\), the smallest eigenvalue is \(f_{n-1}/C_n\), tending to \(1/9\).

## Assumptions and scope

A Dyck path consists of \(n\) upward and \(n\) downward unit steps, has nonnegative partial height and finishes at zero. The final return at time \(2n\) and the initial point are **not** coordinates. The push-forward \(\mu_n\) counts paths with multiplicities; it is not the indicator of distinct return vectors. The Walsh transform is unnormalized: \(\widehat\mu_n(\xi)=\sum_v\mu_n(v)(-1)^{\langle\xi,v\rangle}\). The operator acts on all real or complex functions on \(\mathbb F_2^{n-1}\), with counting-measure \(\ell^2\). For \(n=1\), this group is trivial and the sole eigenvalue is one.

## Proof

**Primitive excursion decomposition.** Every Dyck path is uniquely a concatenation of primitive (positive except at endpoints) Dyck excursions. A primitive excursion of semilength \(r\ge1\) is a Dyck path of semilength \(r-1\) enclosed by one up-step and one down-step, so there are \(w_r=C_{r-1}\) of them. Therefore the return vector of a path with component lengths \(r_1,\ldots,r_q\), summing to \(n\), has ones exactly at their proper partial sums. For independent signs \(\varepsilon_j\in\{-1,1\}\) we obtain the exact character polynomial
\[
Z_n(\varepsilon_1,\ldots,\varepsilon_{n-1})
 =\sum_{r_1+\cdots+r_q=n\atop r_i\ge1}
 \left(\prod_{i=1}^q C_{r_i-1}\right)
 \left(\prod_{i=1}^{q-1}\varepsilon_{r_1+\cdots+r_i}\right).
\]
Taking \(\varepsilon_j=(-1)^{\xi_j}\) gives precisely \(\widehat\mu_n(\xi)\).

**A monotonicity identity.** The polynomial \(Z_n\) is affine in each \(\varepsilon_j\). The contribution containing the boundary return at \(j\) splits uniquely into a left and a right Dyck path, so
\[
\frac{\partial Z_n}{\partial\varepsilon_j}
=Z_j(\varepsilon_1,\ldots,\varepsilon_{j-1})
 Z_{n-j}(\varepsilon_{j+1},\ldots,\varepsilon_{n-1}).
\]
The right factor uses signs relabelled by translation of the component. This derivative is a formal coefficient derivative, or equivalently half the difference when \(\varepsilon_j\) changes from negative to positive.

**Positive bottom eigenvalue.** Write \(W(z)=\sum_{r\ge1}w_rz^r=z\sum_{r\ge0}C_rz^r=(1-\sqrt{1-4z})/2\). With all interior signs negative, the generating function of the minima candidates is
\[
H(z)=\sum_{n\ge1}Z_n(-1,\ldots,-1)z^n
=\sum_{q\ge1}(-1)^{q-1}W(z)^q
=\frac{W(z)}{1+W(z)}
=\frac{1-\sqrt{1-4z}}{3-\sqrt{1-4z}}.
\]
This is \(zF(z)\), where \(F(z)=\sum_{j\ge0}f_jz^j\) is the classical Fine-number generating function. Hence the all-negative value is \(m_n=f_{n-1}\). The equation \(z=W(1-W)\) and substitution \(W=H/(1-H)\) yield
\[
H=z+\frac{zH^2}{1-2H}.
\]
This identity recursively gives nonnegative integer coefficients: \(m_1=1\), \(m_2=0\), and \(m_n\ge2^{n-3}>0\) for every \(n\ge3\), since the summand \(z2^{n-3}H^{n-1}\) contributes \(2^{n-3}\) at degree \(n\).

We now induct on \(n\) to show \(Z_n(\varepsilon)\ge m_n\) for every sign vector. It is immediate for \(n=1\), and for \(n=2\) the polynomial is \(1+\varepsilon_1\ge0\). Assuming all smaller signed polynomials nonnegative, the derivative factorization shows that increasing any sign from negative to positive cannot decrease \(Z_n\). Thus its minimum occurs at the all-negative vector and equals \(m_n\). Since all weights in the defining sum are positive, the zero-frequency value \(C_n\) is a maximum. For \(n=2\) the two multipliers are \(2,0\); for \(n\ge3\) all are strictly positive, proving the classification and condition numbers by Walsh diagonalization.

**Asymptotic conditioning.** Expanding the algebraic function at its dominant singularity gives, with \(s=\sqrt{1-4z}\),
\[
H(z)=\frac13-\frac29s+O(s^2),\qquad
m_n\sim\frac{4^n}{9\sqrt\pi\,n^{3/2}}.
\]
The classical Catalan asymptotic is \(C_n\sim4^n/(\sqrt\pi\,n^{3/2})\). Therefore \(C_n/m_n\to9\). The algebraic identity above also yields this limit directly by standard coefficient extraction; finite enumeration is not used for the asymptotic or any all-order claim.

## Verification

Run `python3 verify.py` with standard Python 3. It independently enumerates Dyck step words through semilength ten, constructs return incidence vectors directly from height traces, compares them with the primitive-composition count, checks complete integer Walsh transforms, tests the flip factorization across every frequency through semilength nine, and checks the exact spectral minimum and positivity through semilength sixteen. The proof above establishes the infinite claims; the code is a finite consistency check.

## Relationship to prior work

Classical Catalan decomposition and the Fine-number generating function are not new. Deutsch–Shapiro survey the Fine numbers, and Cameron–McLeod describe returns, hills and their generating functions. The added statement is **simultaneous positivity for every choice of individually signed interior return times**, together with the sharp lowest Walsh multiplier and the exact deconvolution condition number. Total-return count distributions do not by themselves determine the joint position-resolved Walsh spectrum. Existing results on Dyck step-incidence Fourier transforms and noncrossing-matching incidence vectors act on different coordinate embeddings and do not imply this theorem.

## Limitations

The theorem concerns only unrestricted Dyck paths and their interior ground-level return locations; it does not assert analogous inequalities for height-restricted paths, elevated paths with marked hills, or more general lattice walks. Some properties of Fine numbers, including the algebraic generating function and their asymptotic relationship to Catalan numbers, are classical. Historical-priority comparison is necessarily bounded, and an earlier unindexed return-position Fourier inequality is a residual risk. There has been no independent mathematical audit.

## References

1. E. Deutsch and L. W. Shapiro, *A survey of the Fine numbers*, Discrete Mathematics 241 (2001), 241–265, https://doi.org/10.1016/S0012-365X(01)00121-2 . Public date verified as 2001-10-28 in an accessible bibliographic record.
2. N. T. Cameron and J. E. McLeod, *Returns and Hills on Generalized Dyck Paths*, Journal of Integer Sequences 19 (2016), Article 16.6.1, https://cs.uwaterloo.ca/journals/JIS/VOL19/McLeod/mcleod3.pdf . Public date 2016-06-15.
3. OEIS A000957, Fine numbers, https://oeis.org/A000957 .
