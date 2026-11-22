# An infinite ladder of reentrant positivity windows on a directed fractional triangle

## Finding

Let \(P\) be the cyclic permutation matrix with first row \((0,1,0)\) and put \(L=I-P\). For \(0<\alpha\le3\) set \(K_\alpha(t)=\exp(-tL^\alpha)\), \(t\ge0\), with the principal spectral power and \(0^\alpha=0\). All statements concern real entries of this real, generally nonsymmetric, circulant semigroup.

For \(0<\alpha\le1\), \(K_\alpha(t)\) is entrywise strictly positive for every \(t>0\). For \(1<\alpha<3\), write
\[
\theta=\frac{\pi\alpha}{6},\quad r=3^{\alpha/2},\quad d=\cot\theta,\quad s=r\sin\theta\,t,
\quad \gamma_n=\frac\pi3+\frac{2\pi n}{3}\quad(n\in\mathbb Z_{\ge0}).
\]
Define \(B(d)=\arctan d+d^{-1}\log(2/\sqrt{1+d^2})\). Then the number of **disjoint open negative-entry time windows** is exactly
\[
N(\alpha)=\left\lceil\frac{3}{2\pi}\left(B(d)-\frac\pi3\right)\right\rceil.
\]
They are indexed \(n=0,\ldots,N(\alpha)-1\), occur in this order, and involve one and only one negative entry per row: first the two-step transition (\(j=2\)), then the diagonal (\(j=0\)), then the one-step transition (\(j=1\)), repeating every three windows. At every time outside these windows the entire matrix is entrywise nonnegative; at a boundary or an exceptional tangency zero entries may remain. The unique negative-entry component in window \(n\) is the cyclic coefficient \(j_n=(n+2)\bmod3\). Each window is the connected component of the strict inequality
\[
1+2e^{-ds}\cos\left(s-\frac{2\pi j_n}{3}\right)<0
\]
in the cosine lobe centered at \(\gamma_n\); for \(n=0\) its left endpoint is \(s=0\), while every subsequent window has two positive endpoints. Thus its endpoints are exactly the corresponding roots of the displayed scalar equation, divided by \(r\sin\theta\) to return to time.

There is a strictly increasing sequence of critical orders \(\alpha_n\in(1,3)\), \(n\ge1\), converging to \(3\), characterized as follows: \(d_n=\cot(\pi\alpha_n/6)\) is the unique solution in \((0,\sqrt3)\) of
\[
\log\frac{2}{\sqrt{1+d_n^2}}=d_n(\gamma_n-\arctan d_n).
\]
Window \(n\ge1\) is present precisely when \(\alpha>\alpha_n\); at \(\alpha=\alpha_n\) it reduces to one tangential zero with no negative interval. In particular, the **first genuine positivity reentry** (a later negative diagonal window after initial recovery) begins at \(\alpha_1=2.570230659003063\ldots\). For all \(1<\alpha<\alpha_1\) only the initial two-step transition is negative, on one initial time interval.

Writing \(T_\alpha=\sup\{t>0:\min_{i,j}(K_\alpha(t))_{ij}\le0\}\), the last nonpositive time, one has
\[
N(\alpha)=\frac{9\log2}{\pi^2(3-\alpha)}+O(1),\qquad
T_\alpha=\frac{2\log2}{\pi\sqrt3(3-\alpha)}+O(1),\quad\alpha\uparrow3.
\]
Every \(1<\alpha<3\) has \(K_\alpha(t)>0\) entrywise for all \(t>T_\alpha\), although positivity may be lost and regained earlier. Since every row sums to one and at most one of its entries is negative,
\[
\|K_\alpha(t)\|_{\ell^\infty\to\ell^\infty}
=1+2\max_{j=0,1,2}\bigl(-(K_\alpha(t))_{0j}\bigr)_+.
\]
At \(\alpha=3\), the semigroup is periodic and has **no strictly positive time**: it is entrywise nonnegative exactly when \(3\sqrt3\,t\in(2\pi/3)\mathbb Z_{\ge0}\), and is then a cyclic permutation matrix. Between those discrete times exactly one matrix entry per row is negative.

## Assumptions and scope

The state space is \(\mathbb R^3\), with the coordinate order and the standard \(\ell^\infty\) norm. \(P\) is precisely the forward one-step directed three-cycle permutation; the unit edge rate is fixed. Fractional powers are defined spectrally using the conjugate nonzero eigenvalues of \(L\), with principal argument and zero mapped to zero. The range \(0<\alpha\le3\) is essential for the stated classification. In particular, the semigroup is contractive in the Euclidean norm for \(0<\alpha\le3\), but need not be order-preserving or contractive in the coordinate maximum norm above order one. The count \(N(\alpha)\) counts open negative-entry windows, not isolated zeros at critical orders.

## Proof

**Spectral formula.** Put \(\omega=e^{2\pi i/3}\). The eigenvalues of \(L\) are \(0\) and \(1-\omega^{\pm1}=\sqrt3\,e^{\mp i\pi/6}\). Fourier diagonalization, followed by exponentiation, gives every row of the circulant matrix as a cyclic permutation of
\[
q_j(s)=\frac13\left(1+2e^{-ds}\cos(s-2\pi j/3)\right),\quad j\in\{0,1,2\}.
\]
The row sum is \(\sum_jq_j=1\). For \(0<\alpha\le1\), the off-diagonal entries of \(-L^\alpha\) are nonnegative, since their spectral formula gives the signs of \(-\cos(\theta+2\pi j/3)\), \(j=1,2\), with \(0<\theta\le\pi/6\). The off-diagonal graph is irreducible (at \(\alpha=1\) it is exactly the directed cycle), so the matrix exponential is strictly positive for every positive time.

**Ordering of lobes.** For \(1<\alpha<3\), one has \(0<d<\sqrt3\). Any negative coefficient requires \(\cos(s-2\pi j/3)<-e^{ds}/2<-1/2\). These arcs of width strictly less than \(2\pi/3\) are disjoint among the three phases. Consequently, at most one coefficient is negative at each time. The negative-cosine lobes on \(s\ge0\) occur in the order of centers \(\gamma_0,\gamma_1,\ldots\), with component \(j_n=(n+2)\bmod3\). On lobe \(n\), the positive function
\[
g_n(s)=-2e^{-ds}\cos\left(s-2\pi j_n/3\right)
\]
has its unique maximum at \(s_n=\gamma_n-\arctan d\). For \(n=0\), \(s_0>0\), \(g_0(0)=1\), and \(g_0\) initially increases (since \(d<\sqrt3\)). The first window therefore always exists, has left endpoint zero and one further root. For \(n\ge1\), both cosine-lobe endpoints give \(g_n=0\); hence \(g_n>1\) exactly on one open interval if its maximum exceeds one, on no interval if it does not. Equality makes a single tangency zero.

**Thresholds and count.** The peak criterion is
\[
H_n(d):=\log\frac2{\sqrt{1+d^2}}-d(\gamma_n-\arctan d)>0.
\]
Differentiation yields \(H_n'(d)=-(\gamma_n-\arctan d)<0\) on \((0,\sqrt3)\), except that the derivative vanishes only at the excluded endpoint for \(n=0\). Now \(H_n(0)=\log2>0\); \(H_0(\sqrt3)=0\), whereas \(H_n(\sqrt3)<0\) for all \(n\ge1\). This proves the unique threshold for each additional window. The criteria \(H_n(d)>0\) are equivalent to \(\gamma_n<B(d)\). Because the centers form an arithmetic progression and the inequality is strict, their count is precisely the displayed ceiling. At \(d=d_n\), the tangency is not counted, consistent with the ceiling at integral arguments. Strictly decreasing \(d_n\) gives strictly increasing \(\alpha_n\).

**Last time and singular asymptotics.** For \(d>0\), \(q_j(s)\ge(1-2e^{-ds})/3>0\) when \(s>\log2/d\), so the last nonpositive time exists. The right endpoint of the final negative window (or the last critical tangency) lies between its peak \(s_n\) and \(\log2/d\). Since consecutive peak centers are spaced by \(2\pi/3\), the final peak is at \(\log2/d+O(1)\) as \(d\downarrow0\). Also
\[
B(d)=\frac{\log2}{d}+O(d),\quad d=\frac{\pi(3-\alpha)}6+O((3-\alpha)^3),\quad r\sin\theta=3^{3/2}+O(3-\alpha).
\]
The ceiling formula and conversion \(t=s/(r\sin\theta)\) give both stated asymptotics. At \(\alpha=3\), \(d=0\), \(s=3\sqrt3t\) and \(q_j=(1+2\cos(s-2\pi j/3))/3\). The minimum of the three cosines is always at most \(-1/2\), with equality only at \(s\in(2\pi/3)\mathbb Z\); at these times the coefficients are a cyclic permutation of \((1,0,0)\). Otherwise exactly one is negative. Finally, row sums equal one, and at most one row coefficient can be negative, which proves the maximum-norm identity.

## Verification

The complete proof is analytic. The included `verify.py` independently assembles and exponentiates the diagonalized three-by-three matrix, compares all three kernel components with the explicit Fourier formula, checks the first 39 tangency thresholds and a randomized census of peak signs, and tests near-critical counting. Run `python verify.py` with Python 3, NumPy and SciPy installed. All tests are finite floating-point checks; they do not establish any universal quantified conclusion and are not a substitute for the preceding derivation.

## Relationship to prior work

Benzi, Bertaccini, Durastante and Simunec (arXiv:1912.07288, first public 2019-12-16), Sections 2 and 5, develop fractional powers of directed graph Laplacians and Fourier formulas for directed cycles, principally in the Markovian range \(0<\alpha\le1\). Their foundational spectral representation is used here, but the repeated high-order time-sign windows, sharp count, tangency hierarchy, and singular accumulation at order three are not claimed there. Daners and Glück (arXiv:1801.05179, first public 2018-01-16), particularly Theorem 3.1, provide general criteria for uniform eventual positivity, but not exact sign-time classifications or critical-order formulas for this three-state fractional family. Existing discrete rational time-stepping positivity results and a three-cycle inverse time-average problem concern different operator functions and do not directly imply the present exponential-fractional spectrum calculation.

## Limitations

The result is for the unit-rate directed three-cycle, not arbitrary directed networks, heterogeneous cycles, or all fractional orders beyond three. General Fourier diagonalization is known; the contribution is the exact positivity-window classification obtained from it. A complete historical-priority guarantee is not asserted, especially against specialized three-by-three circulant matrix-function literature. The numerical checker uses floating-point arithmetic; all quantified claims rely on the displayed proof. No independent validation has been performed.

## References

1. M. Benzi, D. Bertaccini, F. Durastante and I. Simunec, *Nonlocal network dynamics via fractional graph Laplacians*, arXiv:1912.07288 (submitted 16 December 2019), https://arxiv.org/abs/1912.07288 . See Sections 2 and 5.
2. D. Daners and J. Glück, *A criterion for the uniform eventual positivity of operator semigroups*, arXiv:1801.05179 (submitted 16 January 2018), https://arxiv.org/html/1801.05179v1 . See Theorem 3.1 and its proof.
