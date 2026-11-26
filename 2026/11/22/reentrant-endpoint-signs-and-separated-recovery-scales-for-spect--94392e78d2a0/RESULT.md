# Whole-kernel recovery and separated time scales for spectral-power heat on the four-vertex path

## Finding

Let \(L\) be the unnormalized combinatorial Laplacian of the unit-weight path \(1-2-3-4\), and let \(K_\alpha(t)=e^{-tL^\alpha}\), where the power is defined spectrally. For every \(\alpha>1\), the distance-two entries \((K_\alpha)_{13}=(K_\alpha)_{24}\) are negative up to a unique positive time \(t_2(\alpha)\), zero at that time, and strictly positive thereafter. All adjacent entries and diagonal entries are strictly positive for \(t>0\).

Write \(t_3(\alpha)\) for the positive endpoint zero when \(1<\alpha\le2\) and \(t_-(\alpha)<t_+(\alpha)\) for the two positive endpoint zeros when \(\alpha>2\), using the endpoint classification in [1]. The **whole matrix** is entrywise nonnegative exactly at \(\{0\}\cup[T(\alpha),\infty)\), where
\[
T(\alpha)=\begin{cases}
\max\{t_2(\alpha),t_3(\alpha)\},&1<\alpha<2,\\
t_3(2),&\alpha=2,\\
t_+(\alpha),&\alpha>2.
\end{cases}
\]
In particular the initial endpoint positivity above order two does not create an early interval of whole-matrix nonnegativity. The strict comparison for every \(\alpha>2\) is
\[
t_-<2^{-\alpha}\log2<t_2<2^{1-\alpha}<t_+.
\]
The two early times are on the same scale, and whole-matrix recovery is on a much later scale. Putting \(a=2-\sqrt2\),
\[
\lim_{\alpha\to\infty}2^\alpha t_-=\tfrac12\log2,\quad
\lim_{\alpha\to\infty}2^\alpha t_2=-\log(1-1/\sqrt2),\quad
\lim_{\alpha\to\infty}a^\alpha T(\alpha)=\log(1+1/\sqrt2).
\]

## Assumptions and scope

The path is simple, unweighted, and has exactly four vertices; there is no normalization by vertex degree. Times are nonnegative and the exponent is real. The finding concerns the whole-matrix nonnegativity set, the distance-two crossing, and its comparison with the endpoint crossings, including the large-exponent scales. The endpoint-only sign transition is an input from [1], not a claim of this result. Ordinary heat and its fractional subordinates for \(0<\alpha\le1\) are entrywise positive for \(t>0\); that standard fact is also not part of the contribution.

## Proof

Use \(\tau=2^\alpha t\), \(r=1-1/\sqrt2\), \(q=1+1/\sqrt2\), \(u=r^\alpha\), and \(w=q^\alpha\). Write \(P=e^{-u\tau}\), \(M=e^{-\tau}\), \(J=e^{-w\tau}\), \(A=(2+\sqrt2)/8\), \(C=(2-\sqrt2)/8\), and \(c=\sqrt2/8\). The eigenvalues of \(L\) are \(0,2r,2,2q\). The spectral projectors (for instance from \(\prod_{\mu\ne\lambda}(L-\mu I)/(\lambda-\mu)\)) give the distance-two and endpoint entries respectively as
\[
D(\tau)=\tfrac14(1-M)-c(P-J),\qquad E(\tau)=\tfrac14-AP+\tfrac14 M-CJ.
\]
The two distinct adjacent entries are \((1-M)/4+c(P-J)\) and \((1-P)/4+(M-J)/4+c(P-J)\). These are positive because \(0<u<1<w\) and \(\tau>0\). Every diagonal entry is at least \(1/4\), from the constant spectral projector and the nonnegative diagonal of each remaining projector. Reflection and symmetry account for the other entries.

**Distance two.** The function \(e^{w\tau}D'(\tau)=cu e^{(w-u)\tau}+e^{(w-1)\tau}/4-cw\) increases strictly from a negative value to infinity. Its value at zero is negative since \(w-u>\sqrt2\) for \(\alpha>1\) (the difference increases strictly from its value at \(\alpha=1\)). Thus \(D\) first decreases from zero and then increases to \(1/4\), giving the unique positive zero and its signs.

**Comparison of crossings.** The endpoint classification in [1, Finding, items 2–3] applies exactly to this \(E\) after the change of time: there is one negative-to-positive crossing for \(1<\alpha\le2\); for \(\alpha>2\) the signs at positive times are successively positive, negative, positive. We compare those times with the distance-two crossing using fixed scaled-time tests. For \(\alpha\ge2\), \(u\le r^2\), \(w\ge q^2>5/2\). At \(\tau=\log2\), \(2^{-u}>1-r^2\) and \(2^{-w}<1/(4\sqrt2)\), so
\[
E(\log2)<\tfrac38-A(1-r^2)=\frac{4-3\sqrt2}{16}<0,
\qquad
D(\log2)<\frac{-3/4+\sqrt2/2}{8}<0.
\]
At \(\tau=2\), use \(e^{-2u}>1-2r^2\), \(P<1\), and \(e^{-2}<1/4\):
\[
D(2)>\tfrac14(1-e^{-2})-c>0,\qquad
E(2)<\tfrac14(1+e^{-2})-A(1-2r^2)=\tfrac14(1+e^{-2}-\sqrt2)<0.
\]
Thus for \(\alpha>2\) the two negativity intervals overlap and their union in positive time is \((0,t_+)\); the same tests give \(t_2<t_3\) at \(\alpha=2\). For \(1<\alpha<2\), the two intervals start at zero, and their union extends to the larger crossing. The matrix at time zero is the identity. This proves the nonnegativity set with all boundary times included.

**Large exponent.** At fixed positive \(\tau\), \(u\to0\), \(w\to\infty\), so \(D(\tau)\to(1-e^{-\tau})/4-c\) and \(E(\tau)\to e^{-\tau}/4-c\). Each limiting function has a simple zero: \(-\log r\) for \(D\) and \((\log2)/2\) for \(E\). Two fixed positive points bracketing a limiting zero eventually have opposite signs in the corresponding finite-\(\alpha\) function. The crossing of \(E\) so bracketed below \(\log2\) is the first, by the ordering just proved. For the last crossing, use \(\sigma=u\tau=a^\alpha t\). At fixed positive \(\sigma\), \(E(\sigma/u)\to1/4-A e^{-\sigma}\), whose simple zero is \(\log(4A)=\log q\). Fixed positive bracketing points here correspond to \(\tau>2\) eventually, so their crossing is the last one and hence gives the global recovery time. Shrinking all brackets proves the stated limits.

## Verification

The proof compares exact scalar functions and gives all-parameter bounds and crossing counts using the endpoint sign theorem [1]. The companion spectral checker is a finite numerical diagnostic for entries and root brackets; no grid is used to certify the quantified conclusions.

## Relationship to prior work and limitations

The endpoint-only record [1] has the same endpoint equation and exact sign phases, and derives onset laws as the exponent approaches one or two. Its claim is explicitly for a single entry. The comparison here identifies which entry blocks *whole-matrix* nonnegativity and determines the late recovery scale relative to the two early events. The mixed generator \(L+\eta L^2\) [2] on this same path is not the spectral-power family for arbitrary \(\alpha\); its mixed-strength limits are different. The three-cube [3] exhibits three separated scales, including a Lambert-function intermediate scale absent here. Connected-graph eventual positivity does not itself supply the temporal ordering or the limiting constants. No claim is made for weighted paths or longer paths.

## References

1. [Two order transitions in endpoint positivity for four-site fractional graph heat](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-two-order-transitions-in-endpoint-positivity-for-four-site-fract--4ec9967002dc/RESULT.md), Finding and Proof.
2. [Two exact positivity-recovery barriers for mixed graph heat on the four-site path](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-two-exact-positivity-recovery-barriers-for-mixed-graph-heat-on-t--14874d60df43/RESULT.md).
3. [Three separated positivity scales for fractional heat on the three-cube](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-three-separated-positivity-scales-for-fractional-heat-on-the-thr--9d68e70a362b/RESULT.md).
