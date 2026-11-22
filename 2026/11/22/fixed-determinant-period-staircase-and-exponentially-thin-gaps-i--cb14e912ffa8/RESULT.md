# Fixed-determinant period staircase and exponentially thin gaps in a max-plus oscillator

## Finding
For every fixed real \(r>1\), put \(D=r^2\) and consider
\[
F_T(x,y)=(y+\max(0,Tx),\ 1-\max(0,r^2x)),\qquad 0<T<2r.
\]
Starting at \((1,1)\), define the unreset linear-branch coordinate \(X_j(T)\) by \(X_0=1\), \(X_1=T+1\), and \(X_{j+1}=TX_j+1-r^2X_{j-1}\). For each sufficiently large integer \(n\), the *first half-turn roots* \(a_n,b_n\) are the unique roots, respectively of \(X_n(a_n)=0\) and \(X_n(b_n)=r^{-2}\), in the shrinking angular neighborhood of \(\arccos(T/(2r))=\pi/(n+1-1/(r-1))+o(n^{-2})\). They satisfy \(a_n<b_n<a_{n+1}\), and for all sufficiently large \(n\) the parameter window
\[
\boxed{\quad b_{n-1}<T<a_n\quad}
\]
produces a *primitive, superattracting* orbit of exactly \(n+2\) steps, including the reset point \((1,1)\). The lengths of these period windows and the intervening gaps have sharp asymptotics:
\[
\boxed{\begin{aligned}
W_n:=a_n-b_{n-1}&\sim\frac{2r\pi^2}{n^3},\\
G_n:=b_n-a_n&\sim\frac{2\pi^2(r-1)}{r^2}\frac{r^{-n}}{n^3},\\
\frac{G_n}{W_n}&\sim\frac{r-1}{r^3}r^{-n}.
\end{aligned}}
\]
In particular there is one such reset orbit of every sufficiently large primitive period as \(T\) approaches \(2r\) from below. The theorem describes the canonical reset itinerary, and makes **no assertion** that other periodic orbits are absent in the gaps.

## Assumptions and scope
Fix \(r>1\) independently of \(n\). All asymptotics are as \(n\to\infty\) with \(r\) fixed; no uniform assertion as \(r\downarrow1\) is made. The real parameter \(T\) lies in \((0,2r)\). The root labels refer to the first postive-to-negative half-turn of the **unreset** coordinate, not to all global roots of its degree-\(n\) polynomial. Strict parameter inequalities are necessary for the superattraction statement; boundary trajectories with coordinate zero are excluded. The map uses synchronous two-coordinate updates at each discrete step.

## Proof
Put \(T=2r\cos\theta\) and restrict to small \(\theta>0\). Let
\[
A(\theta)=r^2+1-2r\cos\theta,\quad
\psi(\theta)=\arctan\frac{\sin\theta}{r-\cos\theta},\quad
\Phi_n(\theta)=(n+1)\theta-\psi(\theta).
\]
Here \(\psi\) is analytic near zero because \(r>1\), and \(\psi(\theta)=\theta/(r-1)+O_r(\theta^3)\). The generating function of the scalar recurrence is
\[
\sum_{j\ge0}X_j(T)z^j=\frac1{(1-z)(1-Tz+r^2z^2)}.
\]
Equivalently, summing the damped-angle Green kernel gives the *exact* formula
\[
X_n(2r\cos\theta)=\frac1{A(\theta)}+
\frac{r^{n+1}}{\sqrt{A(\theta)}\sin\theta}\sin\Phi_n(\theta).\tag{1}
\]
For all large \(n\), \(\Phi_n(\theta)=\pi\) has a unique small solution \(\theta_n^*\), with \(\theta_n^*=\pi/(n+1-1/(r-1))+O_r(n^{-4})\). This follows from \(\Phi_n'=n+1-\psi'>0\) in a fixed neighborhood of zero. For either target \(u\in\{0,r^{-2}\}\), the equation \(X_n=u\) immediately after this half-turn is exactly
\[
\Phi_n(\theta)-\pi=
\arcsin\left(\frac{(A(\theta)^{-1}-u)\sqrt{A(\theta)}\sin\theta}{r^{n+1}}\right).\tag{2}
\]
The argument on the right is positive and \(O_r(r^{-n}/n)\): indeed \(A(0)^{-1}=(r-1)^{-2}>r^{-2}\). The left derivative is \(n+O_r(1)\), while the right derivative is exponentially small. Thus (2), by monotonicity or the implicit-function theorem, has exactly one solution \(\theta_n(u)\) near \(\theta_n^*\), displaced by \(O_r(r^{-n}n^{-2})\). Set \(a_n=2r\cos\theta_n(0)\) and \(b_n=2r\cos\theta_n(r^{-2})\). Since the right side of (2) is larger for \(u=0\), \(\theta_n(0)>\theta_n(r^{-2})\), hence \(a_n<b_n\). Differentiating (2) with respect to \(u\), or subtracting its two equations with the mean-value theorem, gives
\[
\theta_n(0)-\theta_n(r^{-2})\sim
\frac{(r-1)\pi}{r^{n+3}n^2}.
\]
Multiplication by \(2r\sin\theta_n^*\sim2r\pi/n\) proves the formula for \(G_n=b_n-a_n\).

For consecutive half-turn roots, \(\theta_{n-1}(r^{-2})-\theta_n(0)\sim\pi/n^2\). It follows from the derivative \(dT/d\theta=-2r\sin\theta\) that \(W_n=a_n-b_{n-1}\sim2r\pi^2/n^3>0\). Consequently the interleaving \(b_{n-1}<a_n<b_n<a_{n+1}\) holds for all large \(n\). Dividing the two asymptotics gives the stated gap-to-window ratio.

To certify the physical itinerary, take \(b_{n-1}<T<a_n\). As \(T\) increases, \(\theta\) decreases. In this interval the half-turn of \(X_n\) has just been crossed but that of \(X_{n-1}-r^{-2}\) has not: (1) and the same monotonic root analysis give \(X_n<0\) and \(X_{n-1}>r^{-2}\). For all \(0\le j<n\), \(X_j>0\): for indices \(j\) tending to infinity with \(j/n\) bounded away from zero, the angle \(\Phi_j\) lies in \((0,\pi)\) (except the last \(O(1)\) indices, where positivity follows from the strict \(X_{n-1}>r^{-2}\) crossing and decreasing-phase order); the remaining bounded indices converge to strictly positive values \(\sum_{k=0}^jr^k(k+1)\) as \(\theta\to0\). Equivalently, for all sufficiently large fixed indices \(J\) the phase \(\Phi_j\) is positive for every \(J\le j\le n-1\), and remains below \(\pi\) through the last positive index; formula (1) then shows \(X_j>0\). For the finitely many \(j<J\), the positive finite Green sums give the same conclusion. Therefore the actual map agrees with the affine recurrence until step \(n\), at which \(x_n=X_n<0\) and \(y_n=1-r^2X_{n-1}<0\). Its next two steps are \((y_n,1)\) and \((1,1)\). No earlier return to \((1,1)\) is possible: for every \(1\le j\le n\) the second coordinate equals \(1-r^2X_{j-1}<1\), because all earlier first coordinates are strictly positive. At step \(n+1\) the first coordinate is negative, not one. Thus the least period is \(n+2\). In each negative-first-coordinate step the Jacobian equals \(N=\begin{pmatrix}0&1\\0&0\end{pmatrix}\). Two consecutive such steps occur before resetting, so the full-return derivative is zero: the cycle is superattracting.

## Verification
The exact formula (1) and the boundary conditions are independently reproduced by the included `check.py` using high-precision root solving and direct iteration of the full max-plus map. Tests use \(r=1.1,\sqrt2,2,3\) and increasing \(n\), and explicitly check first-negative times, consecutive negative coordinates, reset return, strict root ordering, and convergence of the three normalized asymptotic coefficients. These finite checks support the algebra but are **not** a replacement for the analytic asymptotic and quantifier arguments above.

## Relationship to prior work
Ohmori and Yamazaki (2024) define this generalized max-plus map, derive exact finite-step affine formulas, and locate reset cycles through root curves with numerical period tables, including the fixed-\(D=2\) slice. The present contribution is the exact, all-fixed-\(D>1\) high-period staircase with explicit asymptotic constants for its windows and exponentially smaller intervening gaps. A separately reported earlier special-path calculation gives exponential gaps when \(T=D\to4\); this concerns a *moving determinant* and does not establish the fixed-\(D\) constants here. These are refinements of the source's finite-step formulas, not a claim to discover the original periodic orbits or their reset mechanism.

## Limitations
Constants are pointwise in fixed \(r>1\); the double scaling \(r\downarrow1\) is not analyzed. The theorem concerns the distinguished reset itinerary and does not classify alternative invariant sets in the gaps or all cycles elsewhere in parameter space. The old special-path result is available through a public abstract but not its complete proof, leaving a modest priority risk regarding equivalent general parameter derivatives. Independent mathematical audit has not been performed.

## References
1. S. Ohmori and Y. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230 (first posted 2024-02-09), https://arxiv.org/html/2402.06230v1 . See the exact solution and tabulated region limits in Sections 3--5.
2. *Exponentially thin parameter gaps in a max-plus reset oscillator*, public published-finding corpus finding (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exponentially-thin-parameter-gaps-in-a-max-plus-reset-oscillator--532755a6950a (special moving-determinant path, title/summary checked; full proof not accessible).
