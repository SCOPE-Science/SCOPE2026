# Flat-facet subconvolution: a dimension-sharp lattice threshold and universal logarithmic residue

## Finding

**Theorem.** Let \(d\ge2\) be an integer, \(a>0\), \(p\ge0\), and put
\[
\rho(k)=\|k\|_\infty=\max_{1\le i\le d}|k_i|,\qquad
w_{a,p}(k)=\frac{e^{-a\rho(k)}}{(1+\rho(k))^p}\quad(k\in\mathbb Z^d).
\]
Define the positive, finite convolution quotient, with unnormalized counting measure,
\[
Q_{a,p}(n)=\frac{\sum_{k\in\mathbb Z^d}w_{a,p}(k)w_{a,p}(n-k)}{w_{a,p}(n)}.
\]
Then
\[
\sup_{n\in\mathbb Z^d}Q_{a,p}(n)<\infty\quad\Longleftrightarrow\quad p>d.
\]
For the first coordinate vector \(e_1\), as integers \(N\to\infty\), there is the stronger sharp law
\[
Q_{a,p}(Ne_1)=
\begin{cases}
C_{d,p}N^{d-p}+o(N^{d-p}),&0\le p<d,\\
2^d\log N+O_{a,d}(1),&p=d,
\end{cases}
\]
where
\[
C_{d,p}=2^{d-1}\int_0^1\frac{\min(t,1-t)^{d-1}}{t^p(1-t)^p}\,dt
\]
is finite and strictly positive whenever \(0\le p<d\). The leading constants do not depend on \(a\).

## Assumptions and scope

All coordinates and convolution sums are over the integer lattice. Parameters \(a\) and \(p\) are fixed when \(N\) tends to infinity; this theorem does not give uniformity in \(a\downarrow0\), \(p\to d\), or growing dimension. The norm is the cubical \(\ell^\infty\) norm, not Euclidean length. The quotient uses no \((2\pi)^{-d}\) Fourier normalization. All lattice sums are absolutely convergent because \(a>0\).

## Proof

**Step 1: a uniform bound when \(p>d\).** Fix \(n\), write \(R=\rho(n)\), \(r=\rho(k)\), and \(s=\rho(n-k)\). The norm triangle inequality gives \(R\le r+s\), so the exponential factor in the quotient is at most \(1\). As \(p>d\ge2\), convexity and \(1+R\le(1+r)+(1+s)\) give
\[
\frac{(1+R)^p}{(1+r)^p(1+s)^p}
\le2^{p-1}\big((1+r)^{-p}+(1+s)^{-p}\big).
\]
Summing the last expression over \(k\) yields the uniform bound
\[
Q_{a,p}(n)\le2^p\sum_{k\in\mathbb Z^d}(1+\rho(k))^{-p}<\infty.
\]
The last sum converges because the cubical shell of radius \(j\) has cardinality \((2j+1)^d-(2j-1)^d=O_d(j^{d-1})\).

**Step 2: isolate precisely the norm-equality region on an axis.** Take \(n=Ne_1\) with \(N\) a positive integer. Write \(k=(j,z)\), \(j\in\mathbb Z\), \(z\in\mathbb Z^{d-1}\), and \(\ell=\rho(z)\). Then
\[
r=\max(|j|,\ell),\qquad s=\max(|N-j|,\ell).
\]
Equality \(r+s=N\) holds if and only if \(0\le j\le N\) and \(\ell\le m_j:=\min(j,N-j)\). (Outside this range, \(|j|+|N-j|>N\); within it, either exceeding constraint increases a maximum.) There are exactly \((2m_j+1)^{d-1}\) transverse integer points in this equality region at coordinate \(j\). Its contribution is therefore the exact finite sum
\[
B_{d,p}(N)=(N+1)^p\sum_{j=0}^N
\frac{(2\min(j,N-j)+1)^{d-1}}{(j+1)^p(N-j+1)^p}.
\tag{1}
\]
The factors \(e^{-a(r+s-N)}\) equal one on this entire region.

**Step 3: bound everything outside the equality region.** Set \(m=d-1\). For transverse radius \(\ell\ge1\), the shell count
\[
A_m(\ell)=(2\ell+1)^m-(2\ell-1)^m\le C_d(1+\ell)^{d-2}.
\]
By reflection \(j\leftrightarrow N-j\), it suffices first to consider integers \(0\le j\le N/2\). Off the equality region, \(\ell>j\), hence \(r=\ell\), \(s\ge N-j\), and \(r+s-N\ge\ell-j\). Moreover \((N+1)/(1+s)\le2\). Thus, for fixed \(d,a,p\), that part is bounded by
\[
C_{d,p}\sum_{0\le j\le N/2}\sum_{h=1}^\infty
 e^{-ah}(1+j+h)^{d-2-p}
\le C_{d,a,p}\sum_{0\le j\le N/2}(1+j)^{d-2-p}.
\tag{2}
\]
The last inequality follows from exponential summability in \(h\), valid for either sign of \(d-2-p\). For \(j<0\), write \(j=-h\) with \(h\ge1\). If \(\ell\le h\) then \(r=h\), \(s=N+h\), and \(r+s-N=2h\); its total contribution is at most
\[
\sum_{h=1}^\infty e^{-2ah}(2h+1)^{d-1}(1+h)^{-p}<\infty.
\]
If \(\ell>h\), then \(r=\ell\), \(s\ge N+h\), and \(r+s-N\ge\ell+h\), so its contribution is bounded by
\[
C_d\sum_{h=1}^\infty\sum_{\ell>h}
 e^{-a(\ell+h)}(1+\ell)^{d-2-p}<\infty.
\]
We used \((N+1)/(s+1)\le1\) in both cases. The half-line \(j>N\) contributes the same bound. Hence
\[
0\le Q_{a,p}(Ne_1)-B_{d,p}(N)
\le C_{d,a,p}\left(1+\sum_{0\le j\le N/2}(1+j)^{d-2-p}\right).
\tag{3}
\]
This is \(O_{d,a}(1)\) when \(p=d\). For every \(0\le p<d\), it is \(o(N^{d-p})\): the finite sum is \(O(N^{d-1-p})\) if \(p<d-1\), \(O(\log N)\) if \(p=d-1\), and \(O(1)\) if \(p>d-1\).

**Step 4: the subcritical Riemann sum.** For \(0\le p<d\), split (1) at \(N/2\). At a macroscopic index \(j/N\to t\in(0,1)\), the normalized summand has the Riemann density
\[
2^{d-1}\frac{\min(t,1-t)^{d-1}}{t^p(1-t)^p}.
\]
Endpoint control is essential: for \(0\le j\le N/2\), the unnormalized summand in (1) is bounded by \(C_{d,p}(1+j)^{d-1-p}\); therefore, after division by \(N^{d-p}\), the part \(0\le j\le\varepsilon N\) is at most \(C_{d,p}\varepsilon^{d-p}+o(1)\), and similarly at the other endpoint. Since \(d-p>0\), both endpoint contributions vanish after taking \(\varepsilon\downarrow0\). The interior Riemann sum then proves
\[
\lim_{N\to\infty}\frac{B_{d,p}(N)}{N^{d-p}}=C_{d,p}.
\]
Equation (3) transfers the same limit to \(Q_{a,p}(Ne_1)\).

**Step 5: the critical logarithmic coefficient.** Put \(p=d\). For \(1\le j\le N/2\), the corresponding summand in (1) equals
\[
\frac{(2j+1)^{d-1}}{(j+1)^d}
\left(\frac{N+1}{N-j+1}\right)^d
=\frac{2^{d-1}}j+O_d(j^{-2})+O_d(N^{-1}).
\]
The two symmetric endpoint halves therefore sum to \(2^d\log N+O_d(1)\); a possible central index is counted only once and contributes \(O_d(N^{-1})\). By the \(O_{d,a}(1)\) off-region estimate (3),
\[
Q_{a,d}(Ne_1)=2^d\log N+O_{d,a}(1).
\]
The divergent critical law and the positive subcritical power law prove the converse of Step 1. This completes the proof.

## Verification

The standalone `checker.py` recomputes the exact equality-region cardinality for several small integer boxes and evaluates absolutely convergent convolution ratios after cubical truncation. It checks the finite ridge identity, positivity of the off-ridge contribution, and numerical approach toward the critical coefficient; these finite checks do **not** certify an infinite limit or a global supremum. Those are proved above by Steps 1–5. For reproducing an axis bound with custom parameters, evaluate formula (1); its error is bounded by formula (3), with constants depending on the indicated parameters. The checker uses only Python's standard library.

## Relationship to prior work

Das and Giannakis (arXiv:1912.11664, first submitted 25 December 2019) develop harmonic Hilbert spaces under the subconvolutive weight condition and treat subexponential spectral weights. Montgomery and Giannakis (2024) give the abstract equivalence between this condition and bounded comultiplication in the weighted Hilbert setting. Neither identified inspected result evaluates the cubical exponential-polynomial family's sharp threshold or its critical residue. Kaleta and Ponikowski (arXiv:2109.06336, Section 3, Proposition 3.5) obtain the different threshold \((d+1)/2\) for continuous, essentially Euclidean-radial exponentially tempered densities; a cubical exponential is not uniformly comparable with an Euclidean-radial exponential in dimension at least two. The present lattice proof exploits the cube's exact norm-equality region rather than spherical angular concentration.

## Limitations

The threshold concerns the convolution quotient and its associated Hilbert-algebra coproduct, not a claim that ordinary pointwise multiplication is unbounded whenever the quotient diverges. The asymptotic formulas are along coordinate axes; no all-direction asymptotic profile is asserted. The results are pointwise in fixed \(d,a,p\), and no convergence rate uniform in those parameters is proved. Comparison with indexed publications supports a best-knowledge originality assessment, not a proof of historical priority; independent validation remains outstanding.

## References

1. S. Das and D. Giannakis, *On Harmonic Hilbert Spaces on Compact Abelian Groups*, arXiv:1912.11664 (submitted 25 December 2019), https://arxiv.org/abs/1912.11664 ; Journal of Fourier Analysis and Applications 29, 12 (2023), https://doi.org/10.1007/s00041-023-09992-4 .
2. K. Kaleta and D. Ponikowski, *On Directional Convolution Equivalent Densities*, arXiv:2109.06336 (submitted 13 September 2021), https://arxiv.org/abs/2109.06336 .
3. M. Montgomery and D. Giannakis, *An Algebra Structure for Reproducing Kernel Hilbert Spaces*, first published 12 December 2024, https://doi.org/10.1007/s43037-024-00398-y .
