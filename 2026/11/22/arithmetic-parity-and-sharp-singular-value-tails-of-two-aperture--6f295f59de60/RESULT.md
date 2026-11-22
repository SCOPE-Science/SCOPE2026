# Arithmetic parity and sharp singular-value tails of two-aperture circle convolution

## Finding
Let \(0<a<1/3\) be irrational. For each separation \(a<b<1-a\), write \(\mathbb T=\mathbb R/\mathbb Z\) and define the *single-channel coherent two-aperture convolution*
\[
K_{a,b}f=\bigl(\mathbf1_{[0,a]}+\mathbf1_{[b,b+a]}\bigr)*_{\mathbb T}f
\]
on complex mean-zero \(L^2_0(\mathbb T)\), with unnormalized indicator intervals and normalized circle arclength. Denote the positive singular values, with multiplicities and in nonincreasing order, by \(s_k(K_{a,b})\), and let \(N_{a,b}(t)\) count all singular values strictly greater than \(t>0\). Then
\[
\lim_{t\downarrow0}tN_{a,b}(t)
=\lim_{k\to\infty}k s_k(K_{a,b})=:C(a,b)>0.
\]
The constant has the following exact arithmetic laws.

**Rational displacement.** If \(b=p/q\) is reduced, with \(q\ge2\), then
\[
\boxed{C(a,p/q)=\begin{cases}
\dfrac{8}{\pi^2q}\cot\bigl(\dfrac{\pi}{2q}\bigr),&q\text{ even},\\[3pt]
\dfrac{8}{\pi^2q}\csc\bigl(\dfrac{\pi}{2q}\bigr),&q\text{ odd}.
\end{cases}}
\]
The numerator \(p\) does not enter the constant. For even \(q\), the null Fourier modes are *exactly* \(n\equiv q/2\pmod q\); their density among positive integer modes is \(1/q\). For odd \(q\), no nonzero Fourier mode vanishes. Among all admissible rational separations, the sharp minimum is \(4/\pi^2\), attained only at \(b=1/2\), and the sharp maximum is \(16/(3\pi^2)\), attained only at \(b=1/3\) and \(b=2/3\).

**Independent irrational displacement.** If \(1,a,b\) are linearly independent over \(\mathbb Q\), then
\[
\boxed{C(a,b)=\frac{16}{\pi^3}.}
\]
Every rational displacement with even denominator has a strictly smaller constant, and every one with odd denominator has a strictly larger constant.

**A dependent irrational contrast.** The admissible irrational separation \(b=2a\) has
\[
\boxed{C(a,2a)=\frac{16\sqrt2-8}{3\pi^2},}
\]
which differs from the independent-irrational value. Thus irrationality of the displacement alone does not ensure the generic spectral density.

For every listed regime, \(K_{a,b}\) belongs to the Schatten class \(\mathcal S_r\) if and only if \(r>1\), and
\[
\lim_{M\to\infty}\frac1{\log M}\sum_{k=1}^{M}s_k(K_{a,b})=C(a,b).
\]

## Assumptions and scope
The unit circle carries Lebesgue probability arclength. The two intervals are disjoint, since \(0<a<b\) and \(b+a<1\). The fixed width \(a\) is irrational, so neither boxcar factor has any nonzero Fourier zero. Both interval indicators have coefficient one; replacing their sum with the probability density obtained by division by \(2a\) divides every singular-value constant by \(2a\). A single summed observation is considered, not two separately recorded channels. The singular values include Fourier multiplicities for both positive and negative integer frequencies. The rational and linearly independent cases, together with the particular irrational relation \(b=2a\), do **not** exhaust every rational-dependence class of irrational \(b\).

## Proof
**1. Multiplier and compactness.** At each \(n\in\mathbb Z\setminus\{0\}\), Fourier diagonalization gives
\[
\widehat K_{a,b}(n)=\frac{1-e^{-2\pi ina}}{2\pi in}(1+e^{-2\pi inb}),\qquad
|\widehat K_{a,b}(n)|=\frac{2}{\pi|n|}|\sin(\pi na)\cos(\pi nb)|.
\]
The multiplier tends to zero, so the operator is compact. Its positive singular multiset consists of the absolute values on positive frequencies, each counted twice (from \(\pm n\)). Set
\[
F_n=\frac2\pi|\sin(\pi na)\cos(\pi nb)|,\quad 0\le F_n\le\frac2\pi.
\]
Then \(N_{a,b}(t)=2\sum_{n\ge1}\mathbf1_{\{F_n>tn\}}\).

**2. Counting lemma.** Suppose a bounded nonnegative sequence \((F_n)\) has an empirical distribution converging weakly to a probability measure \(\mu\) on \([0,B]\). Then
\[
\lim_{t\downarrow0}t\sum_{n\ge1}\mathbf1_{\{F_n>tn\}}=\int_0^B x\,d\mu(x).
\]
Indeed, restrict to \(n\le B/t\), divide \([0,B]\) into finitely many short intervals whose endpoints are continuity points of the distribution, and bound the indicator on a block \(t n\in[u,v]\) between \(\mathbf1_{\{F_n>v\}}\) and \(\mathbf1_{\{F_n>u\}}\). Weak empirical convergence applies to each macroscopic block because its two endpoints are asymptotically fixed multiples of \(1/t\); the difference of two convergent initial-segment empirical counts handles moving blocks. Letting the maximum block width decrease to zero gives the layer-cake integral. An atom at zero is harmless because the first block may be treated by its length bound alone. The lemma holds for the distributions arising below. Doubling its limit accounts for \(\pm n\).

**3. Equidistribution.** If \(1,a,b\) are rationally independent, Weyl's theorem makes \((\{na\},\{nb\})\) equidistributed on \([0,1]^2\). Since \(|\sin\pi u|\) and \(|\cos\pi v|\) both have mean \(2/\pi\), the limiting mean of \(F_n\) is \((2/\pi)(2/\pi)^2=8/\pi^3\). The counting lemma and frequency doubling give \(C(a,b)=16/\pi^3\).

If \(b=p/q\) is reduced, split the positive frequencies into their \(q\) residue classes modulo \(q\). In every class, irrationality of \(a\) makes \(\{na\}\) equidistributed on \([0,1]\). Hence the limiting mean of \(F_n\) equals
\[
\frac4{\pi^2q}\sum_{r=0}^{q-1}|\cos(\pi rp/q)|
=\frac4{\pi^2q}\sum_{r=0}^{q-1}|\cos(\pi r/q)|.
\]
Doubling yields \(C=(8/\pi^2q)\sum_r|\cos(\pi r/q)|\). The finite sums are evaluated by the standard finite cosine identity:
\[
\sum_{r=0}^{q-1}|\cos(\pi r/q)|=\begin{cases}
\cot(\pi/(2q)),&q\text{ even},\\
\csc(\pi/(2q)),&q\text{ odd}.
\end{cases}
\]
For example, when \(q=2m\), pair the terms symmetrically around \(m\) to obtain \(1+2\sum_{r=1}^{m-1}\cos(\pi r/q)\), equal to the displayed cotangent by summing a geometric series. For odd \(q=2m+1\), the paired sum is \(1+2\sum_{r=1}^{m}\cos(\pi r/q)\), which equals the displayed cosecant. This proves the two rational formulas independently of numerator.

With \(x=\pi/(2q)\), these finite means divided by \(2/\pi\) are \(x\cot x<1\) for even \(q\) and \(x\csc x>1\) for odd \(q\). The former is strictly increasing as \(q\) increases and the latter strictly decreasing, by the standard derivatives of \(x\cot x\) and \(x\csc x\). Their extremes occur at \(q=2\) and \(q=3\). Since \(a<1/3\), all of \(1/2,1/3,2/3\) are admissible. The claims of strict comparison and rational extrema follow.

**4. Exact null modes.** Since \(a\) is irrational, \(\sin(\pi na)\ne0\) for every nonzero integer \(n\). Thus a multiplier vanishes exactly when \(nb\in\mathbb Z+1/2\). If \(b\) is irrational this never occurs. If \(b=p/q\) is reduced, it is equivalent to \(2np=q(2j+1)\). Such integers exist precisely when \(q\) is even, and, because \(p\) is then odd, are exactly those \(n\equiv q/2\pmod q\). This agrees with the known Fourier-zero obstruction for two equal separated intervals; the new spectral-count assertion is not inferred from this zero classification.

**5. Dependent irrational separation.** For \(b=2a\), the orbit is the irrational circle rotation \(u\mapsto u+a\), and the limiting mean of \(F_n\) is
\[
\frac2\pi\int_0^1|\sin(\pi u)\cos(2\pi u)|\,du.
\]
With \(v=\cos(\pi u)\), the inner integral equals
\[
\frac1\pi\int_{-1}^1|2v^2-1|\,dv
=\frac{4\sqrt2-2}{3\pi}.
\]
Multiplying by \(2\) for the two frequency signs yields \(C(a,2a)=(16\sqrt2-8)/(3\pi^2)\).

**6. Ordered spectrum and Schatten consequences.** For any positive constant \(C\), the counting asymptotic \(N(t)\sim C/t\) is equivalent, by monotone inversion, to \(s_k\sim C/k\) for the decreasing positive singular sequence. Comparison with the harmonic series proves both the logarithmic partial-sum limit and the exact Schatten threshold \(r>1\). The rational-even zero eigenspace does not affect the positive sequence or its counting asymptotic.

## Verification
The self-contained standard-library `check.py` verifies the finite Fourier multiplier identity, the numerator-invariant trigonometric sums through denominator 199, the exact zero residues for denominators 2 through 19, the rational ordering through denominator 399, and six large finite frequency samples with three threshold counts each. It completed 18,153 assertions. These finite computations test normalizations and arithmetic but are not used to prove any infinite limit. Reproduce using `python check.py` in the same directory as this file.

## Relationship to prior work
Johnstone and Raimondo analyze a **single interval** on a periodic domain, its Fourier zeros and the consequences of small divisors for statistical deconvolution [1]. De Canditiis and Pensky analyze **multiple separately observed channels**, combining squared channel multipliers; they do not treat the singular spectrum of a single coherent sum of shifted boxcars [2]. A published two-interval Fourier-zero classification [3] covers (and is credited for) the underlying zero-set obstruction, but its theorem concerns the real Fourier zero loci and Wiener translation cyclicity; it gives no reordered singular-value counting, denominator-parity weak-trace constants or rationally dependent irrational example. The result above uses classical equidistribution and elementary trigonometric sums in a combined operator-theoretic calculation; these tools themselves are not claimed as novel.

## Limitations
No statement is made about every irrational displacement with an integer relation among \(1,a,b\), beyond the explicit \(b=2a\) case. A zero-free Fourier multiplier need not have a bounded inverse or good numerical conditioning; the theorem quantifies large-index singular distributions rather than stability of arbitrary regularized estimators. The sharp rational lower and upper constants refer to the specified fixed irrational width and **rational** admissible displacements; they are not asserted to be global extrema over all real displacements. A previous general rearrangement theorem or unindexed exact two-interval count could subsume this result; the historical equivalence risk remains.

## References
1. I. M. Johnstone and M. Raimondo, *Periodic boxcar deconvolution and diophantine approximation*, Annals of Statistics 32 (2004), 1781–1804; dated open preprint arXiv:math/0503663, 2005-03-29. https://arxiv.org/abs/math/0503663
2. D. De Canditiis and M. Pensky, *Simultaneous Wavelet Deconvolution in Periodic Setting*, Scandinavian Journal of Statistics 33 (2006), 293–306, DOI:10.1111/j.1467-9469.2006.00463.x. https://sciences.ucf.edu/math/mpensky/wp-content/uploads/sites/9/2016/09/ScandJOS-2006.pdf
3. *Arithmetic Fourier-zero lattices and Wiener cyclicity for two separated intervals*, published mathematical result (2026), identifier 2b9667f7502f. Its complete theorem concerns real Fourier zeros and translation cyclicity, not singular-value tails.
4. H. Weyl, classical equidistribution theorem; used for irrational torus rotations, with no claim of priority for that theorem.
