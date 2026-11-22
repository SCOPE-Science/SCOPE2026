# A critical Schatten boundary layer for differences of affine Fock composition semigroups

## Finding

Let \(\mathcal F^2\) be the normalized Gaussian Bargmann–Fock space with orthonormal basis \(e_n(z)=z^n/\sqrt{n!}\). For distinct fixed \(u,v\in\mathbb C\), put \(\Delta=u-v\) and, for \(0<q<1\), define \(C_{q,u}f(z)=f(qz+(1-q)u)\), \(D_q=C_{q,u}-C_{q,v}\), and \(h=1-q\). Every \(D_q\) is trace class. Writing \(a=h/(1+q)\), its Hilbert–Schmidt norm satisfies the **exact** identity

\[
\|D_q\|_{\mathcal S_2}^2=\frac{e^{a|u|^2}+e^{a|v|^2}-2\operatorname{Re}(e^{a u\overline v})}{1-q^2},
\qquad \lim_{q\uparrow1}\|D_q\|_{\mathcal S_2}=\frac{|\Delta|}{2}.
\]

For every real \(1\le p<\infty\),

\[
\lim_{q\uparrow1}h^{1/p-1/2}\|D_q\|_{\mathcal S_p}
=\frac{|\Delta|\Gamma(1+p/2)^{1/p}}{p^{1/2+1/p}},
\quad
\lim_{q\uparrow1}\frac{\|D_q\|}{\sqrt h}=\frac{|\Delta|}{\sqrt{2e}}.
\]

The full singular-value boundary layer has an explicit counting law. For \(0<\lambda<|\Delta|/\sqrt{2e}\), let \(0<x_-(\lambda)<1/2<x_+(\lambda)\) be the two roots of \(|\Delta|\sqrt{x}e^{-x}=\lambda\), and let \(N_q(\lambda)\) count the singular values of \(D_q\) strictly larger than \(\lambda\sqrt h\). Then

\[
\lim_{q\uparrow1}hN_q(\lambda)=x_+(\lambda)-x_-(\lambda).
\]

In particular, despite \(\|D_q\|\to0\), its Schatten \(p\)-norm diverges when \(1\le p<2\), converges to a nonzero limit when \(p=2\), and vanishes when \(p>2\).

## Assumptions and scope

The Hilbert-space inner product is that for which \(e_n(z)=z^n/\sqrt{n!}\) is orthonormal; equivalently the measure is \(\pi^{-1}e^{-|z|^2}\,dA(z)\). The parameters \(u,v\in\mathbb C\) are fixed and distinct, \(q\in(0,1)\), and \(p\) is fixed in \([1,\infty)\). The asymptotics are for \(q\uparrow1\), not simultaneous variation of \(u,v\). Singular values are counted with multiplicity. The counting formula holds at each fixed threshold strictly between zero and the profile maximum, not at either endpoint.

## Proof

Put \(T_{k,q}e_{m+k}=q^m h^k(u^k-v^k)\sqrt{(m+k)!/m!}\,e_m/k!\), and \(T_{k,q}e_n=0\) for \(n<k\). The binomial theorem on the orthonormal basis gives the exact decomposition \(D_q=\sum_{k\ge1}T_{k,q}\). Every \(T_{k,q}\) is a weighted backward shift of step \(k\). For \(0<q<1\), its trace norm is the sum of the moduli of its nonzero weights. By Cauchy–Schwarz and \(\sum_{m\ge0}(m+k)!q^m/m!=k!/(1-q)^{k+1}\),

\[
\|T_{k,q}\|_1
\le \frac{|u^k-v^k|}{\sqrt{k!}}h^{k/2-1}.
\]

The series on the right converges for every fixed \(q>0\), so the expansion converges absolutely in trace norm. In particular \(D_q\in\mathcal S_1\). For \(1/2\le q<1\), let \(\delta=-\log q\ge h\). Since \((m+k)!/m!\le(m+k)^k\), maximizing \(y^{k/2}e^{-\delta y}\) over positive \(y\) yields

\[
\|T_{k,q}\|\le
\frac{|u^k-v^k|}{k!}h^{k/2}2^k\left(\frac{k}{2e}\right)^{k/2}.
\]

Both coefficient series converge uniformly for \(0<h\le1/2\). Thus, with \(A_q=T_{1,q}\) and \(R_q=\sum_{k\ge2}T_{k,q}\),

\[
\|R_q\|_1=O_{u,v}(1),\quad
\|R_q\|=O_{u,v}(h),\quad
\|R_q\|_{\mathcal S_p}=O_{u,v,p}(h^{1-1/p})
=o(h^{1/2-1/p})
\]

for every fixed \(1\le p<\infty\), by Schatten interpolation; the operator-norm error is \(o(\sqrt h)\). The leading operator \(A_q\) is one weighted backward shift with singular-value multiset

\[
\{h|\Delta|\sqrt n\,q^{n-1}:n\ge1\}.
\]

Writing \(x=hn\), the rescaled weights converge uniformly on compact positive \(x\)-intervals to \(F(x)=|\Delta|\sqrt{x}e^{-x}\), and exponential estimates bound both tails. Riemann sums imply

\[
\lim_{h\downarrow0}h^{1-p/2}\|A_q\|_p^p
=|\Delta|^p\int_0^\infty x^{p/2}e^{-px}\,dx
=\frac{|\Delta|^p\Gamma(1+p/2)}{p^{1+p/2}}.
\]

Maximizing \(F\) gives its maximum at \(x=1/2\) and the operator-norm constant. The remainder estimates transfer these norm limits to \(D_q\). Since each singular value changes by at most \(\|R_q\|=o(\sqrt h)\), upper and lower threshold sandwiches transfer the Riemann counting law for \(A_q\) to \(D_q\). The set \(\{x:F(x)>\lambda\}\) is exactly \((x_-(\lambda),x_+(\lambda))\), proving its claimed length.

Finally, the subdiagonals of distinct \(T_{k,q}\) are Hilbert–Schmidt orthogonal. Directly summing their squared entries and using \(\sum_{m\ge0}(m+k)!q^{2m}/m!=k!/(1-q^2)^{k+1}\) gives

\[
\|D_q\|_2^2=\frac{1}{1-q^2}\sum_{k\ge1}\frac{a^k}{k!}|u^k-v^k|^2
=\frac{e^{a|u|^2}+e^{a|v|^2}-2\operatorname{Re}e^{a u\bar v}}{1-q^2}.
\]

Expanding the exponentials at \(a=0\) yields \(\|D_q\|_2^2\to|\Delta|^2/4\). This finishes the proof.

## Verification

The standalone `checker.py` computes the exact lower-triangular coefficient matrices from the binomial identity, compares finite Hilbert–Schmidt sums to the closed form at three values of \(q\) and three complex parameter pairs, tests the leading weighted-shift constants for four Schatten exponents, and compares the full matrix to its leading shift. It passed 33 test groups with worst relative errors below \(1.2\times10^{-14}\) on Hilbert–Schmidt comparisons. The code uses Python 3 with NumPy and is supplementary: the infinite-dimensional assertions follow from the proof above.

## Relationship to prior work

Tien and Khoi (2017) establish boundedness, compactness and essential-norm descriptions for differences of weighted Fock composition operators, but not this moving near-identity singular-value boundary layer. Chalendar and Partington (2021) establish iteration and semigroup properties for affine Fock composition, not sharp Schatten asymptotics for the **difference of two coalescing semigroups**. Peng, Jiang et al. (2024) study order-bounded differences. Lin, Lu, Yang and Zu (2026) give fixed-symbol Schatten membership for finite sums; their comparison constants need not be uniform in a coalescing-symbol limit. Existing polynomially weighted Fock dilation singular-value laws also describe the leading weighted shift but do not independently imply the trace-norm remainder estimate or the exact Hilbert–Schmidt expression for this non-diagonal difference.

## Limitations

The result assumes a one-complex-dimensional Gaussian Fock norm, equal real contraction factors \(q\), and fixed distinct centers. It does not address general entire weights, different contraction factors, exponents \(0<p<1\), or simultaneous parameter drift. The literature assessment is not a formal proof of historical novelty; unindexed equivalent results may exist. No independent mathematical validation has been performed.

## References

- P. T. Tien and L. H. Khoi, *Differences of weighted composition operators between the Fock spaces* (first posted 23 August 2017), https://arxiv.org/abs/1708.06924 .
- I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups* (first posted 1 June 2021), https://arxiv.org/abs/2106.00427 .
- *Order-Bounded Difference in Weighted Composition Operators Between Fock Spaces* (2024), https://doi.org/10.3390/math12213360 .
- Z. Lin, Y. Lu, R. Yang and C. Zu, *Finite sums of weighted composition operators on the Fock space* (first posted 15 November 2026), https://arxiv.org/abs/2611.19948 .
