# An infinite odd-period ladder under one confidence-radius parameter

## Finding

Fix four opinion vectors in \(\mathbb R^3\): \(a_0=(0,0,0)\), \(a_1=(9,0,0)\), \(a_2=(0,9,0)\), and \(a_3=(0,0,9)\). Each of these four agents has the fixed, strictly positive confidence radius \(1/10\). Equip the space with the \(\ell_1\) norm. The fifth agent has variable confidence radius \(R=9+r\), where \(0<r<1\).

For every integer \(m\geq1\), define
\[
q_m=10^{-m},\quad
u_{m,j}=1-\frac{10^{-j}}{2-q_m}\ (0\le j\le m),\quad
I_m=(\nu_{m,m-1},\nu_{m,m}).
\]
For every \(r\in I_m\), the **same frozen four-anchor configuration** admits a primitive period-\(2m+1\) orbit of the fifth agent. Its ordered scalar coordinates, with vector coordinate \(t\) denoting \((t,t,t)\), are
\[
\nu_{m,0},\ 2\nu_{m,1},\ \nu_{m,1},\ 2\nu_{m,2},\ \nu_{m,2},\ldots,\ 2\nu_{m,m},\ \nu_{m,m},
\]
followed by return to \(\nu_{m,0}\). The cycle is exponentially attracting for nearby fifth-agent opinions while all four anchors are held fixed. Its exact period-return derivative is \(2^{-1}10^{-m}\) times the \(3\times3\) identity.

The open parameter intervals \(I_m\) are pairwise disjoint, approach \(r=1\) from below, and have exact lengths
\[
|I_m|=\frac{9\cdot10^{-m}}{2-10^{-m}}.
\]
These are the maximal **strict-switching** parameter intervals for the *displayed orbit itinerary*, not a classification of all possible cycles or of boundary orbits. Thus varying one radius, without moving any of the four anchors or changing their radii, realizes unbounded primitive odd periods \(3,5,7,\ldots\) on robust open parameter windows accumulating at \(R=10\).

## Assumptions and scope

The synchronous heterogeneous Hegselmann–Krause rule is \(z_i^{+}=|N_i|^{-1}\sum_{j\in N_i}z_j\), with \(N_i=\{j:\|z_j-z_i\|_1\le\rho_i\}\), and every agent includes itself. There are exactly five agents. The four anchor opinions and their radius \(1/10\) do not change with \(m\) or \(r\). Only the fifth confidence radius \(9+r\) and fifth initial opinion vary. The theorem concerns these finite periodic solutions and attraction in the three-dimensional fiber with the anchor opinions fixed. It makes no claim of global attraction or of asymptotic stability in the unrestricted fifteen-dimensional agent state space.

## Proof

First consider diagonal vectors \(z=(t,t,t)\) with \(0<t<2\). The fifth agent has \(\ell_1\)-distance \(3t\) to \(a_0\), and \(9+t\) to each outer anchor \(a_1,a_2,a_3\). Since \(R=9+r>9\) and \(3t<6<R\), it always trusts itself and \(a_0\). It trusts all three outer anchors exactly when \(t\le r\). Consequently the scalar update is
\[
F_r(t)=\begin{cases}(t+9)/5,&t\le r,\\t/2,&t>r.\end{cases}
\]
The four anchors each trust only themselves throughout the constructed orbit: pairwise anchor distances are at least \(9\), while the mobile agent has distance at least \(3\nu_{m,0}>1\) from the origin and distance at least \(9\) from each outer anchor. All these distances exceed the anchors' common radius \(1/10\).

Put \(q=q_m\) and \(\nu_j=\nu_{m,j}\). Direct calculation gives
\[
\nu_0=\frac{1-q}{2-q},\qquad \nu_{j+1}=\frac{\nu_j+9}{10},\qquad \nu_m=2\nu_0.
\]
The scalar sequence satisfies \(0<\nu_0<\nu_1<\cdots<\nu_m<1\) and \(2\nu_j>1\) for \(1\le j\le m\). For \(r\in(\nu_{m-1},\nu_m)\), all \(\nu_0,\ldots,\nu_{m-1}\) lie strictly below \(r\); all \(2\nu_1,\ldots,2\nu_m\) and \(\nu_m\) lie strictly above \(r\). Therefore
\[
\nu_j\xrightarrow{F_r}2\nu_{j+1}\xrightarrow{F_r}\nu_{j+1}\quad(0\le j<m),
\qquad \nu_m\xrightarrow{F_r}\nu_m/2=\nu_0.
\]
All \(m+1\) values \(\nu_0,\ldots,\nu_m\) are distinct and less than \(1\), and the \(m\) distinct values \(2\nu_1,\ldots,2\nu_m\) exceed \(1\). Thus the orbit contains exactly \(2m+1\) distinct phase points and has that primitive period.

Every relevant confidence inequality is strict. Hence each phase has a three-dimensional neighborhood in which the corresponding HK neighbor sets are unchanged, with the anchors fixed. For \(m\) five-neighbor updates the fifth-state derivative is \(I_3/5\), and for \(m+1\) two-neighbor updates it is \(I_3/2\). The affine period return has derivative \(I_3/(2\cdot10^m)\), proving local exponential attraction.

The displayed itinerary uniquely forces its phase coordinates: \(m\) alternating full/partial update pairs compose to \(H^m(\nu_0)\), with \(H(t)=(t+9)/10\); the final half-update requires \(H^m(\nu_0)=2\nu_0\), which has the unique solution above. The requisite strict inequalities are equivalent to \(\nu_{m-1}<r<\nu_m\); hence \(I_m\) is precisely the strict-switching window for this itinerary. Finally,
\[
\nu_m-\nu_{m-1}=\frac{9\cdot10^{-m}}{2-10^{-m}}.
\]
Writing \(q=10^{-m}\), the upper endpoint of \(I_m\) is \(1-q/(2-q)\), while the lower endpoint of \(I_{m+1}\) is \(1-q/(2-q/10)\), which is strictly larger. Both endpoints tend to \(1\). The intervals therefore are disjoint, and their lengths decrease geometrically to zero. This completes the proof.

## Verification

A standalone exact-arithmetic checker, `check_hk.py`, independently instantiates the full five-agent synchronous neighbor rule using rational three-dimensional coordinates. For each integer \(1\le m\le30\), it verifies every neighbor set on every phase, exact return after \(2m+1\) updates, pairwise distinctness of phase coordinates, positive and disjoint windows, the interval-width identity, and the claimed multiplier. All thirty cases pass. This is a finite consistency check only; the unrestricted theorem follows from the identities proved above.

## Relationship to prior work

Proskurnikov and Zabarianska (2026), Example 1, introduced exactly the four anchor positions used here and demonstrated a period-two orbit with a larger mobile radius. Their Theorem 8 realizes each period by adapting the geometric construction; their Corollary 10 holds confidence radii fixed across a finite family while allowing different initial anchor configurations. Neither statement fixes all four anchor positions once and obtains the unbounded odd-period ladder by varying only the fifth radius. Their results remain the foundation of the present construction.

Granados, Alsedà and Krupa (2014/2017) establish general period-adding and period-incrementing mechanisms for piecewise contracting maps. The scalar map in this proof is an increasing-branch member of that broader dynamical class, so existence of parameter-dependent periodic behavior is not a general novelty claim. The narrower model-specific contribution here is the exact, fixed-geometry HK realization, explicit rational orbit coordinates, and all strict parameter windows with geometric accumulation. General period-adding theory is not claimed to be new.

## Limitations

The result does not classify other periodic itineraries at a given radius, the behavior at confidence equality, or cycles outside the invariant diagonal. Attraction is **conditional on anchors remaining fixed**; in the unrestricted state space the anchor directions are neutral. An older equivalent fixed-geometry HK calculation or a direct specialization of a general piecewise-contraction result could affect priority. Independent mathematical verification remains outstanding.

## References

1. A. V. Proskurnikov and I. Zabarianska, *Cycles of Arbitrary Period in Multidimensional Heterogeneous Hegselmann–Krause Dynamics*, arXiv:2611.21656v1 (first public 2026-10-30), https://arxiv.org/abs/2611.21656.
2. A. Granados, L. Alsedà and M. Krupa, *The period adding and incrementing bifurcations: from rotation theory to applications*, arXiv:1407.1895 (2014), later *SIAM Review* 59 (2017), 225–292, https://arxiv.org/abs/1407.1895.
3. P. Hegarty and E. Wedin, *The Hegselmann–Krause dynamics for equally spaced agents*, *J. Difference Equations Appl.* 22 (2016), 1621–1645, https://doi.org/10.1080/10236198.2016.1234611.
