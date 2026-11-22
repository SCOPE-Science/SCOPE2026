# Sharp Lipschitz norms of single-harmonic projections on finite cycles

## Finding
For each integer \(n\ge3\), equip the cyclic vertex set \(C_n=\mathbb Z/n\mathbb Z\) with shortest-path graph distance and the real Lipschitz seminorm
\[
  \operatorname{Lip}(f)=\max_{j\in C_n}|f(j+1)-f(j)|.
\]
For \(1\le k\le\lfloor n/2\rfloor\), let \(P_{n,k}\) be the orthogonal projection with normalized counting measure onto the real Fourier harmonic spanned by \(\cos(2\pi kj/n)\) and \(\sin(2\pi kj/n)\). When \(n\) is even and \(k=n/2\), this is the one-dimensional alternating harmonic. Set \(L=n/\gcd(n,k)\). The exact operator norm on real Lipschitz functions modulo constants is
\[
\boxed{\displaystyle
 \|P_{n,k}\|_{\mathrm{Lip}\to\mathrm{Lip}}=\kappa_L=
 \begin{cases}
 1, &L=2,\\[2mm]
 \dfrac{2}{L}\left(\csc\dfrac{\pi}{2L}-\sin\dfrac{\pi}{2L}\right), &L\ge3\text{ odd},\\[3mm]
 \dfrac4L\cot\dfrac\pi L, &4\mid L,\\[3mm]
 \dfrac4L\csc\dfrac\pi L, &L\equiv2\pmod4,\ L\ge6.
 \end{cases}}
\]
In particular, across **all** cycles and single real harmonics,
\[
\boxed{\displaystyle\sup_{n\ge3}\ \max_{1\le k\le\lfloor n/2\rfloor}
  \|P_{n,k}\|_{\mathrm{Lip}\to\mathrm{Lip}}=\frac43.}
\]
Equality holds precisely when \(6\mid n\) and \(k=n/6\). At an edge where the output Lipschitz norm is attained, the input edge-increments of every extremizer are, after an overall sign and cyclic translation, the repeated six-step pattern \((1,1,-1,-1,-1,1)\) multiplied by a common nonzero scalar. For every other effective period the constant is strictly less than \(4/3\).

There is also a three-phase sampling law. As \(L\to\infty\) within the indicated residue classes,
\[
\kappa_L=\frac4\pi+
\begin{cases}
 -\dfrac{5\pi}{6L^2}+O(L^{-4}), &L\text{ odd},\\[2mm]
 -\dfrac{4\pi}{3L^2}+O(L^{-4}), &4\mid L,\\[2mm]
 +\dfrac{2\pi}{3L^2}+O(L^{-4}), &L\equiv2\pmod4.
\end{cases}
\]
Thus the limit is \(4/\pi\), approached from above in precisely the last class and from below in the other two.

## Assumptions and scope
All functions are **real-valued**. The distance on \(C_n\) is the integer shortest-path metric with unit edges, so its Lipschitz seminorm equals the maximum adjacent difference. Constants are factored out to obtain a normed real space of dimension \(n-1\). The Fourier projection is defined with the standard normalized counting inner product, not as a best Lipschitz approximation or as an arbitrary contractive projection. The frequency restriction prevents double-counting the conjugate pair; the Nyquist frequency is handled separately. No complex-valued operator norm is asserted.

For an extremizer, the phrase “at an edge” means an edge \(j\to j+1\) where the projected function achieves its Lipschitz seminorm. With a choice of output edge and orientation, the corresponding cosine row determines the signs of the maximizing input increments. At effective period six, this cosine row has no zero entries, making its pattern rigid. Constants and nonzero scalar multiples of the input do not affect norm attainment.

## Proof
**1. Transfer to the zero-sum increment cube.** Define \((Df)(j)=f(j+1)-f(j)\). Its range is exactly
\[
 Z_n=\left\{u\in\mathbb R^n:\sum_{j=0}^{n-1}u_j=0\right\},
\]
and \(\operatorname{Lip}(f)=\|Df\|_\infty\). Every element of \(Z_n\) integrates to a periodic \(f\), unique modulo constants. Because both \(D\) and \(P_{n,k}\) are circulant, they commute. Consequently,
\[
  \|P_{n,k}\|_{\mathrm{Lip}\to\mathrm{Lip}}
  =\|P_{n,k}|_{Z_n}\|_{\infty\to\infty}.
\]
For \(2k\ne n\), the convolution row of this real rank-two projection is
\[
 a_j=\frac2n\cos\left(\frac{2\pi kj}{n}\right).
\]
Translation symmetry makes every row have the same norm.

**2. Exact centered-row duality.** For any real row \(a=(a_j)\),
\[
\sup_{\substack{\|u\|_\infty\le1\\\sum u_j=0}}\left|\sum_j a_ju_j\right|
=\min_{c\in\mathbb R}\sum_j|a_j-c|.
\]
The inequality \(\le\) follows by subtracting \(c\sum u_j\). For the reverse inequality, choose a median \(c\) of the entries \(a_j\); put \(u_j=1\) on entries above it and \(u_j=-1\) below it. The remaining entries can be chosen in \([-1,1]\) to make \(\sum_j u_j=0\), since the counts strictly above and strictly below any median are each at most half the total. This choice gives equality. This argument also characterizes all maximizing rows: the signs at entries strictly away from a chosen median are forced, while ties permit only the indicated zero-sum adjustment.

Write \(g=\gcd(n,k)\) and \(L=n/g\). Coprimality of \(k/g\) and \(L\) means that the samples \(\cos(2\pi kj/n)\) are a permutation of \(g\) copies of the \(L\) samples \(\cos(2\pi r/L)\). Applying the median identity and cancelling the repeats gives
\[
\|P_{n,k}\|_{\mathrm{Lip}\to\mathrm{Lip}}
=\frac2L\min_{c\in\mathbb R}
 \sum_{r=0}^{L-1}\left|\cos\frac{2\pi r}L-c\right|.
\tag{1}
\]
This is the crucial difference from the uncentered maximum-row or ordinary Fourier Lebesgue constant: a best constant **must** be subtracted before taking the absolute sum.

**3. Evaluate all finite cosine medians.** If \(L\) is even, symmetry about zero makes \(c=0\) a median. Elementary finite geometric sums give
\[
\sum_{r=0}^{L-1}\left|\cos\frac{2\pi r}L\right|
=\begin{cases}
2\cot(\pi/L),&4\mid L,\\
2\csc(\pi/L),&L\equiv2\pmod4.
\end{cases}
\]
Inserting this into (1) proves both even formulas for the rank-two cases.

Suppose next that \(L\) is odd and put \(\delta=\pi/(2L)\). The sample median is
\[
 c_L=(-1)^{(L-1)/2}\sin\delta.
\]
It occurs twice. If \(L=4m+1\), the samples strictly above the median are the central Dirichlet block \(r=0,\pm1,\ldots,\pm(m-1)\). Their sum is
\[
 A=1+2\sum_{r=1}^{m-1}\cos\frac{2\pi r}L
 =\frac{\cos(3\delta)}{\sin(2\delta)}.
\]
There are \(2m-1\) entries above, \(2m\) below, and two at the median. Using that the full cosine sum is zero, the centered absolute sum is
\[
2A+3\sin\delta
=\frac{\cos(3\delta)}{\sin\delta\cos\delta}+3\sin\delta
=\csc\delta-\sin\delta.
\]
If \(L=4m+3\), the samples strictly above the median are instead \(r=0,\pm1,\ldots,\pm m\), with sum
\[
 A=1+2\sum_{r=1}^{m}\cos\frac{2\pi r}L
=\frac{\cos\delta}{\sin(2\delta)}=\frac{1}{2\sin\delta}.
\]
There are \(2m+1\) entries above, \(2m\) below, and two equal to the median \(-\sin\delta\). Therefore the absolute sum is \(2A-\sin\delta=\csc\delta-\sin\delta\). Both cases yield the stated odd formula. This includes \(L=3\), where the projection acts as the identity on the quotient.

When \(L=2\), the conjugate frequencies coincide, so the kernel has only half the rank-two normalization. The alternating function spans the projection range, and its gradient projection has \(\ell_\infty\) norm one on the zero-sum subspace. Hence \(\kappa_2=1\).

**4. Sharp universal bound and all equality cases.** If \(L\) is odd, writing \(y=\pi/(2L)\) gives
\[
\kappa_L=\frac4\pi\frac{y\cos^2y}{\sin y}<\frac4\pi,
\]
since \(0<\cos y<1\) and \(\sin y>y\cos y\) for \(y>0\). If \(4\mid L\), then with \(x=\pi/L\),
\[
 \kappa_L=\frac4\pi x\cot x<\frac4\pi,
\]
because \(\tan x>x\). Both are strictly smaller than \(4/3\), as \(\pi>3\). For \(L\equiv2\pmod4\), \(L\ge6\), one has
\[
\kappa_L=\frac4\pi\frac{x}{\sin x},\qquad x=\frac\pi L.
\]
The function \(x/\sin x\) is strictly increasing on \((0,\pi/6]\), because \(\sin x-x\cos x>0\). This branch is therefore strictly decreasing with \(L\), and at its first value \(L=6\) it equals \((4/6)\csc(\pi/6)=4/3\). The Nyquist case is only one. Finally \(L=6\) for a frequency \(1\le k\le n/2\) is equivalent to \(6\mid n\) and \(k=n/6\).

For effective period six, a row consists of repeats of the cosine samples \((1,1/2,-1/2,-1,-1/2,1/2)\). Its centered median may be taken zero; none of its entries vanishes. The duality equality condition therefore forces, up to global sign and row translation, precisely the repeated increment pattern \((1,1,-1,-1,-1,1)\). Conversely, this pattern has zero sum, integrates to a periodic Lipschitz function, and realizes the ratio \(4/3\). Thus no other extremizers for the global universal bound occur.

**5. Sampling corrections.** Taylor expansion at the origin of \(\csc y-\sin y\), \(x\cot x\) and \(x\csc x\), respectively, yields the three displayed expansions with errors \(O(L^{-4})\). The coefficients have the indicated strict signs, completing the limiting classification.

## Verification
Run `python3 verify.py` with Python 3.9 or newer; the file uses only the Python standard library. Independently of the median derivation, it enumerates every vertex of the zero-sum increment cube and calculates each associated spectral row for \(3\le n\le16\), all admissible frequencies. It also checks the six-cycle constant with exact rational arithmetic, compares the cosine-median formula for all effective periods from three through three hundred, checks general frequency-period reductions for cycle lengths up to one hundred twenty, and checks the three second-order asymptotics numerically. The final diagnostic is `ALL_LIPSCHITZ_CYCLE_FOURIER_CHECKS_PASSED`. These finite tests support but cannot replace the proof for unbounded orders and frequencies.

## Relationship to prior work
The use of normalized finite Fourier idempotents and their trigonometric kernels belongs to the classical literature. Anderson–Ash–Jones–Rider–Saffari study concentration of idempotent trigonometric polynomials. Bonami–Révész study both continuous and finite cyclic \(L^p\) concentration. Their published formulas are for concentration ratios, not operator norms on real Lipschitz quotients. In particular, they do not identify the zero-sum-gradient median in (1).

The published result *Exact three-frequency Fourier projection norm on every cyclic group* computes the ordinary \(\ell^\infty\) norm for a **three-consecutive-frequency** projection, which includes the constant character, whereas our operator projects onto a **single real nonconstant harmonic** and uses the derivative-constrained Lipschitz norm. The published result *Exact endpoint norms and residue law for consecutive cyclic Fourier projections* computes uncentered endpoint norms for consecutive frequency blocks, rather than the centered median expression (1) on the cycle Lipschitz space. The published result *Exact two-frequency \(L^1\) concentration on every cyclic group* provides related absolute-cosine sums and divisor reductions; those ingredients can recover parts of the even-period trigonometric arithmetic, but its point-concentration ratios neither give the odd-period centered formula nor the sharp universal \(4/3\) operator-norm classification. These ingredients are credited rather than claimed independently.

The exact statement here is the simultaneous family of real Lipschitz spectral-projection norms, the exceptional effective-six-period sharp universal bound and rigid norming gradients, and the three-sided second-order sampling law. Literature searches under cyclic Lipschitz Fourier projection, centered cosine median, mean-zero Fourier operator norm, and effective-period aliases did not identify a stronger published result implying all these assertions. That search outcome is not proof of priority: an implicit calculation in classical approximation-theory treatments of finite cyclic Fourier multipliers remains possible.

## Limitations
The theorem applies to real Lipschitz functions on unweighted undirected cycles and to single Fourier harmonics selected by **orthogonal** projection. It does not characterize the norms of sums of multiple separated harmonics, arbitrary weighted cycles, complex-valued Lipschitz functions, other \(\ell^p\) derivative norms or best-approximation projections. The finite verifier cannot establish claims beyond its tested range. Independent external mathematical validation has not been performed.

## References
1. B. Anderson, J. M. Ash, R. L. Jones, D. G. Rider and B. Saffari, “Exponential sums with coefficients 0 or 1 and concentrated \(L^p\) norms,” arXiv:0705.0636v1, first posted 2007-05-04, https://arxiv.org/html/0705.0636v1.
2. A. Bonami and Sz. Gy. Révész, “Integral Concentration of idempotent trigonometric polynomials with gaps,” arXiv:0707.3023v1, first posted 2007-07-20, https://arxiv.org/abs/0707.3023.
3. A. Bonami and Sz. Gy. Révész, “Concentration of the integral norm of idempotents,” arXiv:0811.4576v1, first posted 2008-11-27, https://arxiv.org/html/0811.4576v1.
4. “Exact three-frequency Fourier projection norm on every cyclic group,” public research record `b176a6018242`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242.
5. “Exact endpoint norms and residue law for consecutive cyclic Fourier projections,” public research record `8f1466cba7af`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-endpoint-norms-and-residue-law-for-consecutive-cyclic-four--8f1466cba7af.
6. “Exact two-frequency \(L^1\) concentration on every cyclic group,” public research record `aabfaa5078e3`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-two-frequency-l-1-concentration-on-every-cyclic-group--aabfaa5078e3.
