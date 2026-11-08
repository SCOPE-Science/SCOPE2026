# Parity-controlled negative type of even-capped Boolean Hamming metrics

## Finding

For integers \(n\ge r\ge2\), let \(V_n=\mathbb F_2^n\) and let
\[d_{n,r}(x,y)=\min\{\operatorname{wt}(x-y),r\}.\]
For \(p>0\), a kernel \(d_{n,r}^{p}\) has **negative type** when
\[\sum_{x,y\in V_n}c_xc_y d_{n,r}(x,y)^p\le0\quad\text{whenever}\quad\sum_x c_x=0\]
for all real coefficient families. Let \(\beta_{n,r}\) be the supremum of its admissible exponents.

**General even-cap asymptotic.** For every fixed even integer \(r\ge2\),
\[\boxed{\lim_{n\to\infty} n^{r-1}\beta_{n,r}=\frac{(r-1)!}{\log(r/(r-1))}.}\]
The full-parity Walsh character supplies the sharp upper obstruction on this scale. The assertion does not identify the uniquely critical frequency in every finite dimension for caps \(r\ge6\).

**Exact four-cap threshold.** For every \(n\ge8\), let \(m=n-1\) and define \(\beta_n\) as the unique root in \((0,1)\) of
\[1-m(2^{\beta_n}-1)+\binom m2(3^{\beta_n}-2^{\beta_n})-\binom m3(4^{\beta_n}-3^{\beta_n})=0.\]
Then \(d_{n,4}^p\) has negative type **if and only if** \(0<p\le\beta_n\). It has strict negative type for \(0<p<\beta_n\). At \(p=\beta_n\), the only nonconstant Walsh character in its nullspace is the full-parity character, whose degree is \(n\). Consequently the least Euclidean dimension for an isometric embedding of \((V_n,d_{n,4}^{p/2})\) is \(2^n-1\) for \(0<p<\beta_n\), and \(2^n-2\) at \(p=\beta_n\). Equivalently, \(\exp(-t d_{n,4}^{p})\) is positive semidefinite for every \(t>0\) exactly for \(0<p\le\beta_n\); for \(p>\beta_n\) it is not positive semidefinite for every sufficiently small positive \(t\). In particular,
\[\beta_n\sim\frac{6}{n^3\log(4/3)}.\]

## Assumptions and scope

The group is Boolean, the Hamming weight is the number of nonzero coordinates, and the Fourier transform is **unnormalized**, \(\widehat f(\xi)=\sum_{x\in V_n}f(x)(-1)^{\xi\cdot x}\). The cap \(r\) is held fixed for the asymptotic theorem and is an **even integer**. The exact endpoint classification is for cap four and \(n\ge8\). No assertion is made about cap four in dimensions below eight, or about exact finite-dimensional critical degrees at other even caps. The capped distance is a genuine metric because truncation by a positive constant preserves the triangle inequality.

## Proof

**1. Walsh reduction.** Write \(K_j^{(n)}(s)\) for the binary Krawtchouk polynomial,
\[K_j^{(n)}(s)=\sum_{i=0}^j(-1)^i\binom si\binom{n-s}{j-i},\qquad \sum_jK_j^{(n)}(s)u^j=(1-u)^s(1+u)^{n-s}.\]
The convention is that binomial coefficients outside their natural range vanish. Set \(\Delta_1(p)=1\) and \(\Delta_t(p)=t^p-(t-1)^p\) for \(2\le t\le r\). Since \(\min(w,r)^p=\sum_{t=1}^r\Delta_t(p)\mathbf1_{w\ge t}\), and \(\sum_{j=0}^{t-1}K_j^{(n)}(s)=K_{t-1}^{(n-1)}(s-1)\) for \(1\le s\le n\), every nontrivial Walsh eigenvalue of the powered-distance matrix is
\[\widehat{d_{n,r}^{p}}(s)=-Q_{n,r,p}(s),\quad Q_{n,r,p}(s)=1+\sum_{t=2}^{r}\Delta_t(p)K_{t-1}^{(n-1)}(s-1).\tag{1}\]
Walsh diagonalization implies negative type precisely when \(Q_{n,r,p}(s)\ge0\) for each \(s=1,\dots,n\); strict negative type means all these inequalities are strict. The multiplicity of degree \(s\) is \(\binom ns\).

**2. Exact four-cap minimizing frequency.** Put \(m=n-1\), \(z=n+1-2s\), and
\[a=2^p-1,\quad b=3^p-2^p,\quad c=4^p-3^p.\]
Using \(K_1^{(m)}=z\), \(K_2^{(m)}=(z^2-m)/2\), and \(K_3^{(m)}=(z^3-(3m-2)z)/6\), equation (1) becomes
\[Q_{n,4,p}(s)=1+az+\frac b2(z^2-m)+\frac c6\bigl(z^3-(3m-2)z\bigr).\tag{2}\]
For \(0<p\le1\), concavity gives \(a\ge c>0\). Furthermore \(b/c\le\log(3/2)/\log(4/3)<3/2\): write the increments as integrals of \(p u^{p-1}\) over consecutive unit intervals; the ratio decreases with \(p\), since the logarithm of the integrand ratio has strictly ordered means of \(\log u\) on the two intervals.

At the parity degree \(s=n\), we have \(z=-m\). Subtraction of the values of (2) gives
\[Q_{n,4,p}(s)-Q_{n,4,p}(n)=(z+m)R(z),\]
where
\[R(z)=a+\frac b2(z-m)+\frac c6\bigl(z^2-mz+m^2-3m+2\bigr).\]
The minimum of this upward-opening quadratic over all real \(z\) is
\[\min R=\frac{24ac-9b^2-6bcm+3c^2m^2-12c^2m+8c^2}{24c}\ge\frac{c}{24}\left(3m^2-21m+\frac{47}{4}\right)>0\]
for \(m\ge7\). Thus for \(n\ge8\) and \(0<p\le1\), degree \(n\) is the **unique** minimizing nonconstant Walsh frequency.

**3. Existence and uniqueness of the four-cap root.** Define
\[q_m(p)=Q_{n,4,p}(n)=1-ma+\binom m2b-\binom m3c.\]
Then \(q_m(0)=1\) and \(q_m(1)=-(m-1)(m-2)(m-3)/6<0\). Also \(q_m\) strictly decreases for \(p\ge0\). To see this, note that
\[b'(p)=\int_2^3u^{p-1}(1+p\log u)\,du,\quad c'(p)=\int_3^4u^{p-1}(1+p\log u)\,du.\]
The factor \(u^p(1+p\log u)\) is increasing in \(u\) for \(p\ge0\). Therefore
\[\frac{c'(p)}{b'(p)}\ge\frac{\log(4/3)}{\log(3/2)}>\frac23.\]
Because \(\binom m3/\binom m2=(m-2)/3\ge5/3\), one gets \(\binom m3c'(p)>\binom m2b'(p)\), and hence \(q_m'(p)=-ma'(p)+\binom m2b'(p)-\binom m3c'(p)<0\). Thus there is exactly one positive root, in \((0,1)\). By step 2, all other Walsh inequalities are strictly positive at this root. After the root the parity coefficient violates negative type, proving the exact range.

**4. Kernel and embedding dimensions.** The centered Euclidean Gram matrix for squared distances \(d_{n,4}^{p}\) is minus one-half the distance matrix compressed to the orthogonal complement of constants. Its positive eigenvalues correspond exactly to negative nonconstant Fourier coefficients, by (1). Below the root all \(2^n-1\) nontrivial character directions survive; at the root precisely the unique parity direction vanishes. Schoenberg's criterion equates conditional negative definiteness with positive definiteness of \(\exp(-t d^p)\) for all \(t>0\). If some powered-distance Fourier coefficient is positive, the same nontrivial coefficient of \(\exp(-t d^p)\) is negative for sufficiently small \(t\), by Taylor expansion.

**5. All fixed even caps.** Let \(r\) be even, \(j=r-1\), and take \(p=c_0n^{-j}\) for any fixed \(c_0>0\). Uniformly in \(s\) one has \(|K_h^{(n-1)}(s-1)|\le\binom{n-1}{h}\). Moreover \(\Delta_t(p)=p\log(t/(t-1))+O_r(p^2)\). Substituting in (1) shows
\[Q_{n,r,p}(s)\ge1-\frac{c_0\log(r/(r-1))}{(r-1)!}+O_{r,c_0}(n^{-1})\quad\text{uniformly in }s.\tag{3}\]
At the full-parity frequency \(s=n\), \(K_j^{(n-1)}(n-1)=(-1)^j\binom{n-1}{j}\), with \(j\) odd, so
\[Q_{n,r,p}(n)=1-\frac{c_0\log(r/(r-1))}{(r-1)!}+O_{r,c_0}(n^{-1}).\tag{4}\]
For \(c_0\) below the asserted constant (3) proves negative type for all sufficiently large \(n\); for \(c_0\) above it (4) gives a violating character. These two bounds prove the limit. The four-cap asymptotic follows as its special case.

## Verification

`check_capped_even.py` is a standalone Python 3 checker. It compares the direct Walsh transform of the literal truncated-distance table against (1) for every nonconstant frequency and multiple exponents in dimensions eight through thirteen. It finds the four-cap root by bisection and checks parity minimization and the unique endpoint zero. It also tests both sides of the asymptotic leading-scale bound for even caps two, four, six, and eight at dimensions 250 and 500. These are finite numerical consistency checks; the infinite and exact claims follow from steps 1–5 above. Reproduce with `python3 check_capped_even.py`. The successful execution ends with `EVEN_CAPPED_HAMMING_WALSH_CHECKS_OK`.

## Relationship to prior work

Schoenberg established the classical equivalence between negative type, Hilbert embeddings, and positive-definite exponential kernels. Sánchez (2011) gave a general finite-metric supremal-negative-type method and documented the interval property; neither reference supplies the specialized Fourier minimization or the all-even-cap asymptotic. Feinsilver and Schott (2018) provide general Krawtchouk transforms and convolution theory, without a determination of powered capped-Hamming negative-type thresholds. The older Deza–Maehara work (1990) treats metric transforms and, as described in Sánchez (2011), truncated **two-distance** graph metrics; it was investigated as a possible stronger antecedent, but its primary full text was not available for examination. The exact three-cap Boolean result in the related research record uses a different quadratic Walsh polynomial, and does not imply the cubic four-cap minimizer or the fixed-even-cap asymptotic hierarchy.

## Limitations

The exact endpoint classification is restricted to \(n\ge8\) for cap four. The uniform asymptotic limit fixes an even cap before dimension tends to infinity; no joint growing-cap regime is claimed. The finite checker's floating-point calculations are illustrative, not a substitute for the displayed inequalities. No complete priority claim is made with respect to inaccessible historical sources, especially Deza–Maehara (1990), Maehara (1986), or other unlocated specialized metric-transform theorems. No independent mathematical audit has been performed.

## References

1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, publicly posted 2011-08-02, https://arxiv.org/abs/1108.0451 .
2. I. J. Schoenberg, *Metric Spaces and Positive Definite Functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, https://doi.org/10.2307/1989894 .
3. M. Deza and H. Maehara, *Metric Transforms and Euclidean Embeddings*, Transactions of the American Mathematical Society 317 (1990), 661–671, https://doi.org/10.1090/S0002-9947-1990-0974513-6 .
4. H. Maehara, *Metric transforms of finite spaces and connected graphs*, Discrete Mathematics 61 (1986), 235–246.
5. P. Feinsilver and R. Schott, *Krawtchouk transforms and convolutions*, Bulletin of Mathematical Sciences (2018), https://doi.org/10.1007/s13373-018-0132-2 .
