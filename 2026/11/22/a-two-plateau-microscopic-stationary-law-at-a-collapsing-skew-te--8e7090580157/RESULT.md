# A two-plateau microscopic stationary law at a collapsing skew-tent band pair

## Finding
Let \(0<\varepsilon<1/16\), put \(s=1+2\varepsilon\), and define the continuous interval map
\[
T_\varepsilon(x)=\begin{cases}2x,&0\le x\le1/2,\\1-s(x-1/2),&1/2<x\le1.\end{cases}
\]
For every absolutely continuous invariant probability \(\mu_\varepsilon\) carried by its alternating pair of invariant bands, rescale the conditional law on the lower band to \([0,1]\) with coordinate \(t\), and that on the upper band with coordinate \(z\) as below. Their densities converge in \(L^1([0,1])\) as \(\varepsilon\downarrow0\) to, respectively,
\[
h_-(t)=\begin{cases}4/3&0<t<1/2,\\2/3&1/2<t<1,\end{cases}
\qquad h_+(z)=h_-(1-z).
\]
In particular the stationary mean has the precise second-order expansion
\[
\int_0^1 x\,d\mu_\varepsilon(x)=\frac34-\frac{\varepsilon}{2}+\frac56\varepsilon^2+o(\varepsilon^2).
\]
Unscaled stationary laws collapse to \((\delta_{1/2}+\delta_1)/2\), even though at the limiting neutral parameter there is **no physical invariant probability** (no single invariant probability has a basin of positive Lebesgue measure).

## Assumptions and scope
The source family is its continuous two-affine-branch map with endpoint data \(a=0\), \(b=1/2\), \(c=1/2-\varepsilon\). All probabilities are Borel measures on \([0,1]\). “Absolutely continuous” refers to Lebesgue measure. The theorem concerns absolutely continuous invariant probabilities supported on the indicated trapping pair, not arbitrary atomic invariant probabilities on unstable periodic orbits. The boundary \(\varepsilon=0\) is assessed separately. The original source also has a conference precursor publicly dated July 17, 2023.

## Proof
**1. Trapping pair and coordinates.** Define
\[
L_\varepsilon=[\tfrac12-\varepsilon,\tfrac12+\varepsilon+4\varepsilon^2],\quad U_\varepsilon=[1-2\varepsilon,1].
\]
These intervals are disjoint because \(4\varepsilon^2+3\varepsilon<1/2\) on the stated range. Direct substitution proves \(T_\varepsilon(L_\varepsilon)=U_\varepsilon\), \(T_\varepsilon(U_\varepsilon)=L_\varepsilon\). Each invariant probability carried by this pair has half its mass on either component. The lower coordinate and upper coordinate are
\[
t=\frac{x-(1/2-\varepsilon)}{2\varepsilon s},\qquad z=\frac{x-(1-2\varepsilon)}{2\varepsilon}.
\]
On upper-to-lower passage, \(t=1-z\). Two iterates restricted to the lower band become exactly
\[
R_s(t)=\begin{cases}1-2st,&0\le t\le a_s,\\s^2(t-a_s),&a_s<t\le1,\end{cases}\quad a_s=(2s)^{-1}.
\]
This follows by composing each affine branch, with no approximation. At \(s=1\) the formula is \(R_1(t)=1-2t\) on \([0,1/2]\) and \(R_1(t)=t-1/2\) on \([1/2,1]\).

**2. Uniformly expanding return and density stability.** For \(1\le s\le9/8\), set \(A_s=[0,a_s]\), \(B_s=(a_s,1]\). The right image has maximum \(m_s=s(s-1/2)\le45/64\), while \(a_s\ge4/9\). If \(t,R_s(t)\in B_s\), then \(R_s^2(t)\le s^2(m_s-a_s)\le1341/4096<4/9\le a_s\); consequently three consecutive right visits are impossible, and every three-fold branch derivative has modulus at least \(2s\cdot s^4\ge2\). More precisely, the first return to \(A_s\) has return times at most three and three affine branches. Two branches map onto all of \(A_s\), with derivatives \(-2s\) and \(-2s^3\). The third maps into a short interval shrinking to zero as \(s\downarrow1\), with derivative \(-2s^5\). At the limit the third branch disappears and the first-return map consists of two onto branches, each of slope \(-2\), on equal halves of \(A_1\).

The elementary piecewise-expanding perturbation theorem for invariant BV densities (uniform finite-branch Lasota–Yorke/Rychlik estimate plus the \(BV\hookrightarrow L^1\) compact embedding; see references) applies to this first-return family. Here the inverse slopes are bounded by \(1/2\), the two onto branch domains have lengths bounded away from zero, branch maps and slopes vary continuously, and the sole extra branch has vanishing domain and uniformly bounded inverse slope; the explicit return itinerary above gives the required uniform bounded return time and distortion (zero on every affine branch). Thus invariant densities of the return family are \(L^1\)-precompact, and any limit is an invariant density for the two-branch full return map. That limit has the unique normalized constant density \(2\) on \(A_1\). The bounded-return suspension/Kac formula then yields \(L^1\) convergence of stationary densities for \(R_s\).

**3. Exact two-plateau limiting law.** At \(s=1\), the normalized Lebesgue return density on \(A_1=[0,1/2]\) is \(2\). Half of the return trajectories have return time one and half return time two, so the expected return time is \(3/2\). The stationary \(R_1\)-law gives mass \(2/3\) to \(A_1\), and mass \(1/3\) to its complement. Its density is therefore \(4/3\) on \(A_1\) and \(2/3\) on \((1/2,1]\). This is also checked directly by the Perron–Frobenius identity \(P_1h(t)=\tfrac12h((1-t)/2)+\mathbf1_{t\le1/2}h(t+1/2)\). It is the unique absolutely continuous invariant density because the return map is full-branch and uniformly expanding. The conditional upper-band density is the reflection of the lower one since upper-to-lower dynamics is the reflection \(t=1-z\).

**4. Exact mean identity and neutral boundary.** Write \(m_s=\int t h_s(t)\,dt\) for the conditional lower mean; the previous steps give \(m_s\to5/12\). The two coordinate changes and the reflection imply the exact identity
\[
\int x\,d\mu_\varepsilon=\frac34-\frac\varepsilon2+2\varepsilon^2 m_s.
\]
This proves the displayed second-order law. Support diameters tend to zero and both bands carry mass \(1/2\), giving the weak two-atom limit. At \(\varepsilon=0\), each positive point doubles under the left branch until it enters \([1/2,1]\), where the dynamics is the involution \(x\mapsto3/2-x\). Each individual one- or two-cycle has only countably many preimages, hence Lebesgue-zero basin; no invariant probability is physical. This last statement does not exclude invariant probabilities: there are infinitely many neutral periodic orbit laws.

## Verification
The companion exact-rational checker `verify.py` reconstructs the band endpoints, two-iterate conjugacy, itinerary bound, and the limiting transfer-operator density. Exact computations cover rational \(\varepsilon\) and spatial test points. The checker does not replace the infinite-time transfer-operator argument.

## Relationship to prior work
Moysis et al. define the endpoint-interpolated skew-tent map but fix \(c=0\) for their systematic parameter simulations. Cheng and Palmer classify skew-tent attractors and pointwise asymptotic fates across slopes, including band structures and their collapse; these facts motivate the present calculation but do not determine the microscopic conditional stationary densities or the second-order stationary mean. Standard stability theory is used as an ingredient and is not claimed as new. A related exact Markov result at the distinct parameter curve \(c=b^2\) does not imply the \(c\uparrow b\) two-scale asymptotic.

## Limitations
The theorem provides an asymptotic law for absolutely continuous invariant probabilities in one symmetric one-parameter slice, and it does not assert a rate for the \(L^1\) convergence. Atomic repelling-orbit measures are excluded. The proof invokes established piecewise expanding statistical stability after verifying the finite-branch return structure; the result is not an independent mathematical certification. Broader published skew-tent statistical literature may contain equivalent limiting laws, so publication priority is provisional.

## References
1. L. Moysis, M. Lawnik, M. S. Baptista, S. K. Goudos, C. Volos, *Construction of Piecewise Chaotic Maps With Tunable Statistical Mean*, MOCAST (2023), doi:10.1109/MOCAST57943.2023.10176612 (publicly dated 2023-07-17).
2. L. Moysis, M. Lawnik, C. Volos, M. S. Baptista, S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry 15 (2023), 2138, doi:10.3390/sym15122138, equations (1)–(3).
3. K. Cheng and K. Palmer, *On the dynamics of skew tent maps*, arXiv:1710.10880 (2017), Sections 2–4.
4. J. F. Alves and O. R. Etubi, *Hölder continuity of invariant density and entropy for piecewise expanding maps*, arXiv:2409.18805 (2024); standard perturbation context.
5. G. Keller and C. Liverani, *Stability of the spectrum for transfer operators*, Annali della Scuola Normale Superiore di Pisa (1999), standard spectral-perturbation framework.
