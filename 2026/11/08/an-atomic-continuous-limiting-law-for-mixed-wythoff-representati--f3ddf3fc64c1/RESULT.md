# An atomic-continuous limiting law for mixed Wythoff representation counts

## Finding

Let \(\varphi=(1+\sqrt5)/2\), \(\alpha=\varphi^{-1}\), and \(\beta=\varphi^{-2}=1-\alpha\). For each integer \(n\ge1\), let
\[
r(n)=\#\{(h,k)\in\mathbb Z_{\ge1}^{2}:\lfloor h\varphi\rfloor+\lfloor k\varphi^{2}\rfloor=n\}.
\]
This is the mixed lower/upper Wythoff representation function (OEIS A259598). Define the continuous circular piecewise-linear profile \(L:[0,1]\to[0,\beta]\) by
\[
L(t)=\begin{cases}
\beta-t,&0\le t\le\beta,\\
t-\beta,&\beta\le t\le2\beta,\\
\beta,&2\beta\le t\le1.
\end{cases}
\]
The endpoints \(L(0)=L(1)=\beta\) agree. There is an absolute constant \(C\) such that, for every \(n\ge1\),
\[
\left|r(n)-(n-1)L(\{n\alpha\})\right|\le C\log(n+1).\tag{1}
\]
The empirical probability measures of the numbers \(r(n)/n\) converge weakly to
\[
\boxed{\ \mu=2\,\mathbf1_{(0,\beta)}(s)\,ds+(1-2\beta)\,\delta_{\beta}.\ }\tag{2}
\]
In particular, the limiting distribution has a uniform continuous component of total mass \(2\beta\) and an atom of mass \(1-2\beta=\varphi^{-3}\) at its upper endpoint \(\beta\). Moreover, every real-valued function \(f\) on \([0,1]\) with Lipschitz constant at most one satisfies
\[
\left|\frac1N\sum_{n=1}^{N}f(r(n)/n)-\int f\,d\mu\right|
\le C'\frac{\log^2(N+1)}{N}\qquad(N\ge2),\tag{3}
\]
with an absolute \(C'\). Thus for each fixed integer \(j\ge1\),
\[
\frac1N\sum_{n=1}^{N}\left(\frac{r(n)}n\right)^j
=\beta^j\left(1-2\beta+\frac{2\beta}{j+1}\right)
+O_j\left(\frac{\log^2(N+1)}N\right).\tag{4}
\]
The convergence claims concern the sequence of indices \(n\), not random independent summands and not prime-number statistics.

## Assumptions and scope

The representation pairs \((h,k)\) are ordered by their distinct lower- and upper-sequence roles, both indices are strictly positive, and \(n\) runs over all positive integers. For \(n\le2\), there are no representations. The phase \(\{x\}=x-\lfloor x\rfloor\) lies in \([0,1)\). Only the golden-ratio Wythoff pair is asserted; no statement is made for arbitrary complementary Beatty slopes or arbitrary higher-fold sums. Equations (1)--(4) are unconditional. The constant in (3) is uniform in the one-Lipschitz test function, including additive constants.

## Proof

**1. Beatty membership as a circle rotation.** Put \(a(m)=\mathbf1_{\{m=\lfloor h\varphi\rfloor\text{ for some }h\ge1\}}\) for \(m\ge1\). The inequality \(m\le h\varphi<m+1\) shows that \(a(m)\) counts integers in \([m\alpha,(m+1)\alpha)\), hence
\[
a(m)=\lfloor(m+1)\alpha\rfloor-\lfloor m\alpha\rfloor
=\mathbf1_{[\beta,1)}(\{m\alpha\}).\tag{5}
\]
Because the two Wythoff Beatty sequences are complementary, the upper-sequence indicator is
\(b(m)=1-a(m)=\mathbf1_{[0,\beta)}(\{m\alpha\})\). This also follows directly by replacing the lower-sequence reciprocal slope by \(\beta\) and using \(\alpha+\beta=1\).

**2. Exact geometric reduction.** Summing over the lower summand \(m\) gives the exact convolution
\[
r(n)=\sum_{m=1}^{n-1}a(m)b(n-m).
\]
Write \(\theta=\{n\alpha\}\) and \(x=\{m\alpha\}\). Both indicators equal one precisely when \(x\in[\beta,1)\) and \(\{\theta-x\}\in[0,\beta)\). Up to endpoints, the admissible circle arc \(I_\theta\) is
\[
I_\theta=\begin{cases}
[\theta+\alpha,1),&0\le\theta<\beta,\\
[\beta,\theta),&\beta\le\theta<2\beta,\\
[\theta-\beta,\theta),&2\beta\le\theta<1.
\end{cases}
\]
Its Lebesgue length is exactly \(L(\theta)\). All relevant possible endpoint coincidences are absent for \(1\le m<n\) by irrationality of \(\alpha\), except harmless empty-arc conventions. Consequently,
\[
r(n)=\#\{1\le m<n:\{m\alpha\}\in I_{\{n\alpha\}}\}.\tag{6}
\]

**3. A uniform Fibonacci-block discrepancy bound.** For every half-open circular arc \(I\), every integer starting index \(s\ge0\), and every integer \(H\ge1\),
\[
\left|\#\{s\le m<s+H:\{m\alpha\}\in I\}-H|I|\right|\ll\log(H+1),\tag{7}
\]
with an absolute, arc-independent constant. To verify (7) without a black-box distribution theorem, let \(p/q\) be a continued-fraction convergent to \(\alpha=[0;1,1,1,\ldots]\). The denominator \(q\) is a Fibonacci number and \(|\alpha-p/q|<q^{-2}\). In a block of \(q\) consecutive iterates starting at any \(s\), the \(q\) points \(\{(s+j)\alpha\}\) (\(0\le j<q\)) lie at circular distance less than \(1/q\) from the uniformly spaced grid \(\{s\alpha+jp/q\}\). The grid count in any arc differs from \(q|I|\) by at most two, and modifying the grid within distance \(1/q\) affects only the points within \(1/q\) of its two endpoints: at most six grid points. Thus each convergent-denominator block has absolute discrepancy at most eight. Every positive \(H\) is a sum of distinct, nonconsecutive Fibonacci denominators (with the initial \(1\) handled separately); this yields \(O(\log(H+1))\) blocks. The bound applies uniformly to their shifted starting indices and to the arc. Apply it with \(H=n-1\) and the arc in (6) to obtain (1).

**4. Limiting distribution.** Irrational rotations are equidistributed: for each nonzero integer \(\ell\), the geometric sum \(\sum_{n\le N}e^{2\pi i\ell n\alpha}\) is bounded independently of \(N\), giving equidistribution by the usual trigonometric approximation. Since \(L\) is continuous on the circle, \(L(\{n\alpha\})\) has limiting law \(L(U)\) for a uniform \(U\in[0,1)\). On each of \((0,\beta)\) and \((\beta,2\beta)\), the map \(L\) has slope of absolute value one and covers \((0,\beta)\), contributing density one twice. On \([2\beta,1)\), it is constant equal to \(\beta\), contributing an atom of size \(1-2\beta\). Formula (1) implies \(|r(n)/n-L(\{n\alpha\})|\ll\log(n+1)/n\to0\). This proves (2).

**5. Quantitative Lipschitz comparison.** If \(f\) is one-Lipschitz, then \(g=f\circ L\) has circular total variation at most the total variation of \(L\), namely \(2\beta\). The standard one-dimensional integration-by-parts discrepancy inequality, obtained by applying the interval-count bound (7) to a Stieltjes decomposition of \(g\), gives
\[
\left|\sum_{n=1}^{N}g(\{n\alpha\})-N\int_0^1g(t)\,dt\right|\ll\log(N+1).
\]
Also the Lipschitz property and (1) show
\[
\sum_{n=1}^{N}|f(r(n)/n)-f(L(\{n\alpha\}))|
\ll\sum_{n=1}^{N}\frac{\log(n+1)}n\ll\log^2(N+1).
\]
Here \(r(n)/n\in[0,1]\) and \(L\in[0,\beta]\). Divide by \(N\) to obtain (3). For (4), use the test \(f(t)=t^j/j\), which is one-Lipschitz on \([0,1]\), and integrate \(s^j\) against (2): the atom contributes \((1-2\beta)\beta^j\) and the continuous part contributes \(2\beta^{j+1}/(j+1)\). This completes the proof.

## Verification

The standalone `verify.py` uses exact integer arithmetic to calculate the first \(6000\) mixed Wythoff representation counts directly from their defining Beatty sequences, cross-checks an independent indicator convolution over a smaller range, checks the interval description, and compares the observed profile errors and empirical first two moments with the theorem. It uses high-precision integer floors via \(\lfloor k\varphi\rfloor=\lfloor(k+\sqrt{5k^2})/2\rfloor\). The computations are finite consistency checks; equations (1)--(4) rest on the proof above.

## Relationship to prior work

Ashburn (2026), on the same OEIS sequence A259598, proves the exact characterizations of \(r(n)=1\) and \(r(n)=2\), while crediting Kawsumarng et al. for \(r(n)=0\). These sparse-value results neither assert nor determine the global normalized empirical distribution in (2). Shallit (2020, Section 11.2) gives a rank-19 linear representation for computing the mixed sum counts exactly in Fibonacci numeration; algorithmic exact computability does not itself state the explicit uniform phase profile, atom, or quantitative weak-law rate. The OEIS A259598 entry supplies the generating function and classifications but not (1)--(4). Pongsriiam (2022) studies finite-order sumset covering and combinatorial structure for golden-ratio Beatty sequences; those existence results are distinct from an empirical distribution of representation multiplicities. The earlier Kawsumarng--Khemaratchatakumthorn--Noppakaew--Pongsriiam paper (2021) was identified as highly relevant but could not be fully inspected; its exact text may contain stronger related statements. No historical uniqueness or independent validation is claimed.

## Limitations

The distribution is for \(r(n)/n\), not unnormalized \(r(n)\). Equation (3) controls Lipschitz observables, not uniform convergence of distribution functions at the limiting atom. The \(O(\log n)\) error is a proved upper bound, not asserted sharp. The 2021 mixed-sumset paper could not be checked in full; this is a priority uncertainty. No independent audit has been performed, and computational checks cover only a finite range.

## References

1. A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words* (2026), arXiv:2610.04842v1, https://arxiv.org/abs/2610.04842 (first posted 2026-10-04).
2. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond* (2020), arXiv:2006.04177v1, especially Section 11.2, https://arxiv.org/abs/2006.04177.
3. OEIS Foundation, A259598, *Number of representations of n as lower plus upper Wythoff numbers*, https://oeis.org/A259598.
4. P. Pongsriiam, *Combinatorial structure and sumsets associated with Beatty sequences generated by powers of the golden ratio*, Electronic Research Archive 30 (2022), 2385--2405, https://doi.org/10.3934/era.2022121.
5. Kawsumarng, Khemaratchatakumthorn, Noppakaew and Pongsriiam, *Sumsets associated with Wythoff sequences and Fibonacci numbers* (2021), https://doi.org/10.1007/s10998-020-00343-0 (identified, not fully inspected).
