# An exact oriented renewal kernel for the critical random interval map

## Finding

In the critical modified Boyarsky–Góra–Islam (mBGI) random interval map of Hata and Yano, successive visits to the central junction form an explicitly computable **two-state Markov renewal process**, when the initial point is Lebesgue-uniform on either central cell. The entire joint distribution of the first-return time and whether the orbit changes from the left to the right cell is encoded by a cubic algebraic generating function. In particular, the return-time mean is infinite while the induced side chain mixes geometrically in the *number of returns*, with an exact nonzero switching probability.

Use the probabilities \(p=2/3\) and \(q=1/3\). Let \(F(z,s)\) denote the power-series solution, with \(F(0,s)=0\), of
\[
F(z,s)=z\left(\frac23+\frac{s}{3}F(z,s)^3\right).
\]
For a uniformly distributed initial point in either central cell, let \(R\) be the first positive return time to their union and let \(U\) count all side switches during the excursion, and set \(B=U\bmod 2\), the indicator that the side at return is opposite (otherwise \(B=0\)). Then the exact joint generating function is
\[
\boxed{H(z,s):=\mathbb E[z^R s^U]=\frac{2z/3}{2-F(z,s)}+\frac{zs}{3}F(z,s)^2.}
\]
The exponent of \(s\) counts all side switches; evaluating at \(s=1\) gives the generating function of \(R\), and at \(s=-1\) gives the signed transform \(\mathbb E[z^R(-1)^B]\). Thus the generating functions of \(R\) jointly with \(B=0\) and \(B=1\) are respectively
\[
\frac{H(z,1)+H(z,-1)}2,\qquad
\frac{H(z,1)-H(z,-1)}2.
\]
This distinction between total switches and their parity is essential.

Write \(a\) for the unique root in \((0,1)\) of \(a^3+3a-2=0\), and set
\[
\eta=\frac13\left(\frac{2}{2-a}-a^2\right),\qquad
\sigma=\frac{1-\eta}{2}.
\]
Then \(\Pr(B=1)=\sigma\approx0.321787880890943\), \(\Pr(B=0)=1-\sigma\), and the side transition matrix of the process observed at consecutive junction returns is
\[
\begin{pmatrix}1-\sigma&\sigma\\\sigma&1-\sigma\end{pmatrix}.
\]
Its nontrivial eigenvalue is \(\eta\approx0.356424238218114\). After \(m\) junction returns, the probability of the original side is exactly \((1+\eta^m)/2\). The return-time marginal satisfies
\[
\boxed{\Pr(R>n)\sim\frac{4}{3\sqrt\pi}\,n^{-1/2},}\qquad \mathbb E[R]=\infty.
\]
These conclusions apply to every integer \(n\ge0\) and \(m\ge0\) as appropriate; asymptotics are as \(n\to\infty\).

## Assumptions and scope

The state space is \((0,1)\), with independent maps chosen at each integer step:
\[
\tau_1(x)=\begin{cases}
2x,&0<x<1/4,\\1-2x,&1/4<x<1/2,\\2-2x,&1/2<x<3/4,\\2x-1,&3/4<x<1,
\end{cases}\quad
\tau_2(x)=\begin{cases}
1-x/4,&0<x<1/2,\\(1-x)/4,&1/2<x<1.
\end{cases}
\]
Map \(\tau_1\) is selected with probability \(2/3\) and \(\tau_2\) with probability \(1/3\). Set \(I_k^-=(2^{-k-2},2^{-k-1})\) and \(I_k^+=(1-2^{-k-1},1-2^{-k-2})\) for integers \(k\ge0\), and \(J=I_0^-\cup I_0^+\). At time zero, a side \(+\) or \(-\) is prescribed, and \(X_0\) is Lebesgue-uniform on its \(I_0\) cell, independently of future map choices. We ignore the countable set of partition boundaries, which has probability zero under this assumption. The result is **annealed** and concerns the return process under this initial law; it does not assert the same renewal law for individual deterministic initial points.

## Proof

**1. Labeled cell transitions.** The cell transitions from the source's Section 4 are, for any \(k\ge1\),
\[
\tau_1(I_k^\pm)=I_{k-1}^\pm,\qquad \tau_2(I_k^\pm)=I_{k+2}^\mp.
\]
On each central cell, \(\tau_1\) maps bijectively onto the corresponding entire half-interval and \(\tau_2\) maps bijectively onto the opposite \(I_2\). If the starting point is uniform on its central cell, the \(\tau_1\) image belongs to \(I_j\) with probability \(2^{-j-1}\), for each integer \(j\ge0\). On these paths the first-return branch is affine and bijectively covers the returned \(I_0\) cell.

**2. One-level descent transform.** Outside \(J\), the level makes independent \(-1\) steps with probability \(p\), preserving side, and \(+2\) steps with probability \(q\), switching side. For a first descent by one level, put a weight \(z\) on each time step and \(s\) on every \(+2\) step. A first \(-1\) step contributes \(pz\), whereas a first \(+2\) step contributes \(qzs\) followed by three independent successive one-level descents (strong Markov property). The resulting transform therefore obeys \(F=pz+qzsF^3\). This identifies uniquely its power series with nonnegative coefficients in the variables \(z\) and \(s\). The level walk has mean step \(-p+2q=0\) and finite variance, hence hits the lower level almost surely. Therefore \(F(1,1)=1\), and a descent from level \(j\) has transform \(F^j\).

For completeness, Lagrange inversion gives the exact first-descent coefficients from depth \(k\ge1\):
\[
\Pr\{D_k=3u+k,\ U_k=u\}
=\frac{k}{3u+k}\binom{3u+k}{u}
\left(\frac23\right)^{2u+k}\left(\frac13\right)^u
\quad (u\ge0).
\]
Here \(U_k\) counts \(+2\) steps and hence side switches; the endpoint side changes iff \(U_k\) is odd. The formula independently checks the time-count parity and the cubic transform.

**3. First-return kernel.** On the first step out of \(J\), choice \(\tau_1\) contributes
\[
pz\sum_{j\ge0}2^{-j-1}F^j=\frac{pz}{2-F},
\]
while choice \(\tau_2\) enters the opposite cell of depth two, contributes one extra switch, and thereafter gives \(qzsF^2\). Summing yields \(H(z,s)\). The first-return time is finite almost surely by recurrence of the centered skip-free walk. At each fixed sequence of chosen maps and intermediate cells that returns to \(J\) for the first time, the corresponding affine branch maps a subinterval of \(I_0\) bijectively onto the entire terminal \(I_0\) cell. Since its slope is constant, the returned coordinate conditional on that itinerary is uniform on that cell. Therefore the returned coordinate is also uniform conditional on \((R,B)\). Independent future map choices and induction prove that **successive pairs of (return length, side-change indicator) have the same joint law and are independent**, provided the initial coordinate has the stated uniform distribution. This is the two-state Markov renewal property. In particular, the transition matrix is symmetric as displayed.

**4. Exact switching rate.** Set \(z=1,s=-1\). Writing \(a=F(1,-1)\) gives \(a=2/3-a^3/3\). It has a unique root in \((0,1)\), because \(a^3+3a-2\) is strictly increasing and changes sign. The alternating expectation is
\[
\eta=H(1,-1)=\frac{2/3}{2-a}-\frac{a^2}{3}.
\]
Since total first-return probability is one, \(\Pr(B=1)=(1-\eta)/2\). The result \(0<\eta<1\) follows, for example, from \(0<a<2/3\): then \(\eta>1/3-a^2/3>0\) and \(\eta<2/3<1\). The \(m\)-return side correlation equals \(\eta^m\) by matrix multiplication.

**5. Infinite mean and tail.** At \(s=1\), the equation for \(F\) has the local expansion \(F(z,1)=1-\sqrt{1-z}+O(1-z)\) as \(z\uparrow1\) (substitution into its cubic relation verifies the constant). Hence
\[
H(z,1)=\frac{2z/3}{2-F(z,1)}+\frac z3 F(z,1)^2
=1-\frac43\sqrt{1-z}+O(1-z).
\]
The identity \((1-H(z,1))/(1-z)=\sum_{n\ge0}\Pr(R>n)z^n\) and the Hardy–Littlewood Tauberian theorem applied to the nonincreasing nonnegative tail sequence give \(\Pr(R>n)\sim4/(3\sqrt{\pi n})\). Its sum diverges, so \(\mathbb E[R]=\infty\). This concludes the claim.

## Verification

The accompanying standalone Python checker verifies the exact first-descent count by a dynamic-programming enumeration for finite depths and numbers of upward steps, checks the signed transforms against explicit positive return-path enumeration at selected finite horizons, and evaluates the algebraic root and switching probability numerically. These computations do **not** certify the infinite-horizon theorem; the preceding proof supplies that argument. Run `python3 verify.py` from the directory containing the checker. No external packages are required.

## Relationship to prior work

Hata and Yano, *Arcsine and Darling–Kac laws for piecewise linear random interval maps*, arXiv:2108.01332, Section 4, give exactly the mBGI cell-transition rules (4.1)–(4.3), prove its recurrence and infinite invariant measure, and derive the **unlabeled** one-level first-passage equation (4.13). Their Theorem 1.3 gives an occupation-time Darling–Kac limit, not the parity-labeled first-return kernel. The novelty claimed here is only the explicit bivariate joint kernel on the two central sides, the induced renewal independence, its exact side-switching eigenvalue, and the return-length tail for **this** induced law; the underlying maps, walk recurrence, cubic first-passage setup, and standard combinatorial/Tauberian ingredients are not new. The 2022 related random-dynamics-with-core article studies a different induced system. A complete priority guarantee across uncatalogued random-map and renewal literature is not asserted.

## Limitations

This is a same-authority analytic derivation, not an independently audited theorem. It assumes independent map choices, the critical map probabilities, and a uniform conditional entrance point on a fixed central side. The Markov renewal property need not hold without the uniform entrance law. The side changes and return lengths are correlated **within** each excursion; the proof asserts independence only **across** complete excursions. The tail asymptotic applies to the full return length, not conditional on a prescribed long-return side outcome. Existing abstract renewal/Markov-chain theory may contain algebraically equivalent kernel descriptions not indexed under this map's name.

## References

1. G. Hata and K. Yano, “Arcsine and Darling–Kac laws for piecewise linear random interval maps,” arXiv:2108.01332 (initial release 2021-08-03), especially Theorem 1.3 and Section 4. https://arxiv.org/html/2108.01332v3 ; https://arxiv.org/abs/2108.01332 .
2. F. Nakamura, Y. Nakano, H. Toyokawa and K. Yano, “Arcsine law for random dynamics with a core,” arXiv:2206.00226 (2022). https://arxiv.org/abs/2206.00226 .
3. Standard tools used with proof explicitly spelled out above: Lagrange inversion for one-variable formal power series and the Hardy–Littlewood Tauberian theorem for nonnegative monotone sequences.
