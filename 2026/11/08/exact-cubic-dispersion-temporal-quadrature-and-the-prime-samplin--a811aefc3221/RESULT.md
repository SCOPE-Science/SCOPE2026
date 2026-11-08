# Exact cubic-dispersion temporal quadrature and the prime sampling threshold

## Finding

For integers \(K\ge1\), \(N\ge1\), and arbitrary \(a=(a_0,\ldots,a_{K-1})\in\mathbb C^K\), define the periodic cubic Fourier flow
\[
U_a(x,t)=\sum_{n=0}^{K-1}a_n e^{2\pi i(nx+n^3t)},\qquad x,t\in\mathbb R/\mathbb Z.
\]
Define the uniform temporal sample of the spatial fourth moment and its continuous counterpart by
\[
Q_{K,N}(a)=\frac1N\sum_{j=0}^{N-1}\int_0^1|U_a(x,j/N)|^4\,dx,
\quad Q_{K,\infty}(a)=\int_0^1\int_0^1|U_a(x,t)|^4\,dx\,dt.
\]
Put \(S=\sum_n|a_n|^2\). Then
\[
Q_{K,\infty}(a)=2S^2-\sum_n|a_n|^4,
\]
and the exact, generally signed sampling defect is
\[
\boxed{Q_{K,N}(a)-Q_{K,\infty}(a)=
4\!\!\sum_{\substack{h,r\ge1,\ h+r\le K-1\\0\le m\le K-1-h-r\\N\mid 3hr(2m+h+r)}}
\operatorname{Re}\!\left(a_{m+h}\overline{a_m}\,\overline{a_{m+h+r}}a_{m+r}\right).}
\]
There is an exact arithmetic decision rule for whether these quantities agree **for every** complex vector \(a\). Set \(M=N/\gcd(N,3)\). For each ordered pair of positive integers \((h,r)\) with \(h+r\le K-1\), define
\[
t_{h,r}=\frac{M}{\gcd(M,hr)},\quad g_{h,r}=\gcd(2,t_{h,r}),\quad L_{h,r}=K-1-h-r.
\]
If \(g_{h,r}\nmid(h+r)\), this pair produces no alias. Otherwise let \(m_{h,r}\) be the least nonnegative solution of
\[
\frac2{g_{h,r}}m\equiv-\frac{h+r}{g_{h,r}}
\pmod{t_{h,r}/g_{h,r}}.
\]
When the modulus is one, the least solution is zero. **Universal exact quadrature occurs if and only if \(m_{h,r}>L_{h,r}\) for every admissible pair whose congruence is solvable.** The criterion takes \(O(K^2)\) gcds and modular inversions, independent of any floating-point integration.

The sharp squared-energy fourth-power norm
\[
C_{K,N}=\sup_{a\ne0}\frac{Q_{K,N}(a)}{(\sum_n|a_n|^2)^2}
\]
satisfies
\[
\boxed{C_{K,N}=2-\frac1K\quad\Longleftrightarrow\quad
\text{universal exact temporal quadrature holds}.}
\]
When equality holds, every nonzero extremizer has constant coefficient magnitude and arbitrary phases. Otherwise the sharp norm strictly exceeds \(2-1/K\).

**Prime-grid threshold.** For every \(K\ge4\) and prime \(p\), universal exact quadrature holds precisely when
\[
\boxed{p\ge2K-3.}
\]
Thus the smallest *prime* number of equally spaced time samples is the smallest prime at least \(2K-3\). This is not asserted to be the smallest sample count over all composite moduli. For \(K=3\), the smallest sample count among all positive integers is \(4\), while the smallest prime sample count is \(5\). For \(K=1,2\), every positive number of time samples works.

## Assumptions and scope

The spatial integral and time integral are normalized Lebesgue measures on \(\mathbb R/\mathbb Z\). The frequency band consists of consecutive **nonnegative** integer modes \(0,\ldots,K-1\), with exact dispersion \(n\mapsto n^3\). The uniform time grid is \(\{j/N:0\le j<N\}\). Coefficients can be arbitrary complex numbers and may vanish. The results concern the fourth power of the spatial \(L^4\) norm and are not claims for arbitrary shifted frequency bands: unlike quadratic dispersion, cubic dispersion has a translation-dependent time frequency difference.

## Proof

**Spatial Parseval identity.** At each time, the positive spatial Fourier coefficient of \(|U_a|^2\) at lag \(h\) is
\[
B_h(t)=\sum_{m=0}^{K-1-h}a_{m+h}\overline{a_m}
 e^{2\pi i((m+h)^3-m^3)t}.
\]
The zero Fourier coefficient is \(S\), and the negative-lag coefficient is \(\overline{B_h(t)}\). Therefore
\[
\int_0^1|U_a(x,t)|^4\,dx=S^2+2\sum_{h=1}^{K-1}|B_h(t)|^2.
\]

**Continuous orthogonality and exact sampling defect.** For distinct \(m,m+r\) in a fixed positive-lag block, \(h,r\ge1\), the difference of cubic time frequencies equals
\[
((m+h+r)^3-(m+r)^3)-((m+h)^3-m^3)
=3hr(2m+h+r)>0.
\]
Hence no off-diagonal term survives continuous temporal integration. Summing diagonal terms of \(|B_h|^2\) gives \(Q_{K,\infty}=S^2+2\sum_{h,m}|a_{m+h}|^2|a_m|^2=2S^2-\sum_n|a_n|^4\). The uniform \(N\)-point time average of an integer-frequency exponential is one when its frequency is divisible by \(N\), and zero otherwise. Pairing each off-diagonal block term with its conjugate supplies the factor four and exactly the displayed signed defect, with its full index bounds.

**Necessary and sufficient arithmetic rule.** The alias condition \(N\mid3hr(2m+h+r)\) is equivalent to \(M\mid hr(2m+h+r)\), and hence to \(t_{h,r}\mid 2m+h+r\). The linear congruence is solvable precisely when \(g_{h,r}\mid h+r\); when solvable, all nonnegative solutions are congruent to the stated \(m_{h,r}\) modulo \(t_{h,r}/g_{h,r}\). There is a solution with \(0\le m\le L_{h,r}\) exactly when the least solution lies in that range. If there is no alias, the defect is identically zero for all \(a\). If an alias exists, choose \(a_n=1\) for every \(n\): all defect summands are nonnegative and at least one strictly positive, ruling out universal equality. The criterion follows.

**Sharp norm transition.** In the alias-free case, \(Q_{K,N}=2S^2-\sum|a_n|^4\). Cauchy--Schwarz gives \(\sum|a_n|^4\ge S^2/K\), with equality if and only if the \(K\) magnitudes are equal (for nonzero \(a\)). In an aliasing case the all-ones vector simultaneously saturates this Cauchy--Schwarz inequality for the continuous moment and makes the defect strictly positive. Thus the sampled sharp constant is strictly larger, as claimed.

**Sharp classification for prime time grids.** Let \(K\ge4\). If \(p\ge2K-3\) is prime, it is at least five. Every possible alias has \(h,r\le K-2<p\), while
\[
2\le 2m+h+r\le 2(K-1)-(h+r)\le2K-4<p.
\]
Also \(p\nmid3\), so \(p\nmid3hr(2m+h+r)\): no alias exists. Conversely, for prime \(p=2\) or \(3\), the indices \((h,r,m)=(1,1,0)\) are admissible and produce time frequency \(6\), divisible by \(p\). For prime \(5\le p<2K-3\), necessarily \(p\le2K-5\); choose \(h=1\), \(r=2\), \(m=(p-3)/2\). These satisfy \(m+h+r=(p+3)/2\le K-1\), and \(2m+h+r=p\), giving time-frequency alias \(6p\). This covers every smaller prime. At \(K=3\), the only off-diagonal frequency is \(6\), so \(N=4\) works but \(N=1,2,3\) do not. At \(K=1,2\) no off-diagonal pairs exist.

## Verification

The independent-to-the-derivation standalone integer checker `verify.py` enumerates exact alias triples and independently evaluates the modular inverse rule in \(1344\) cases \((1\le K\le16,\ 1\le N\le84)\). It computes the whole quartic moment directly from spatial-momentum and cubic-time congruences and checks the signed defect for \(756\) real coefficient tests plus \(88\) Gaussian-complex tests; it verifies the prime threshold for \(4\le K\le35\), checks the \(K=3,N=4\) boundary, and exhibits a negative signed defect at \(K=3,N=2\) with coefficients \((1,1,-1)\). Reproduce by running `python3 verify.py` with Python 3 standard library. The general theorem is proved symbolically above; finite enumeration does not certify an infinite range.

## Relationship to prior work

Classical periodic KdV/Airy Fourier restriction and its momentum-resonance identities motivate the dispersion \(n^3\). Bourgain's KdV restriction argument and Li's bilinear dispersive estimate treat continuously observed or otherwise different norms, not this exact uniform temporal sampling law. Hughes and Wooley analyze the cubic curve and continuous discrete restriction rather than all-grid exact temporal fourth-moment quadrature. A related published quadratic-dispersion theorem, *Exact arithmetic aliasing and prime-optimal time quadrature for quadratic Fourier flows*, has a position-independent alias frequency \(2hr\) and a divisor-sum criterion; cubic dispersion instead produces \(3hr(2m+h+r)\) and a different sharp prime-grid threshold. Fourier orthogonality and geometric-series sampling are classical tools, not claimed as new.

## Limitations

Only consecutive nonnegative cubic modes, normalized continuous spatial integration, fourth moments and uniform time samples are covered. The theorem gives a sharp fourth-power norm constant in the no-alias regime but **not** its exact numerical value when aliases occur. It classifies the smallest **prime** sampling cardinality, not the globally smallest cardinality over composite grids. The defect is signed; the sampled moment need not dominate the continuous one for every complex coefficient choice. The proof does not extend unchanged to arbitrary shifted intervals, other dispersions, mixed-sign bands or higher moments. Historical priority against every possible broad polynomial-phase sampling theorem is not certified.

## References

1. J. Bourgain, *Fourier transform restriction phenomena for certain lattice subsets and applications to nonlinear evolution equations, Part II: The KdV equation*, Geometric and Functional Analysis **3** (1993), 209–262. Earlier publicly cataloged 1992 IHES manuscript: https://archives.ihes.fr/document/M_92_62.pdf (catalog does not verify a precise day).
2. Q. Li, *A Bourgain type bilinear estimate for a class of water-wave models*, arXiv:1009.4442v1, first submitted 2010-09-22: https://arxiv.org/abs/1009.4442.
3. K. Hughes and T. D. Wooley, *Discrete Restriction for (x,x³) and Related Topics*, International Mathematics Research Notices (online 2021), freely accessible manuscript: https://www.math.purdue.edu/~twooley/publ/20210304kdv.pdf.
4. *Exact arithmetic aliasing and prime-optimal time quadrature for quadratic Fourier flows*, published research record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-arithmetic-aliasing-and-prime-optimal-time-quadrature-for--0049864e4447.
