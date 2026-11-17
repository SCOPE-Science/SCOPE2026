# Attractor-corrected sign-reversal zeta identity for symmetric Lorenz maps

## Finding
Let \(F\) be an odd, increasing-branch Lorenz map as specified below, and \(G=-F\). At every positive odd integer \(n\), the difference of regular period-dividing-\(n\) point counts is exactly
\[
 a_n(G)-a_n(F)=2-2A_n(F),
\]
where \(A_n(F)\) is the number of regular attracting fixed points of \(F^n\), counted as points rather than cycles. At even \(n\) the difference is zero. Consequently, if \(b_\ell(F)\) counts attracting primitive cycles of \(F\) of odd least period \(\ell\), then, as an identity of formal power series,
\[
\frac{\zeta_G(t)}{\zeta_F(t)}=\frac{1+t}{1-t}\prod_{\substack{\ell\ge1\\\ell\ \mathrm{odd}}}\left(\frac{1-t^\ell}{1+t^\ell}\right)^{b_\ell(F)}.
\]
The expanding-case quotient \((1+t)/(1-t)\) therefore has an exact attractor correction without any expansion assumption. Moreover, for every integer \(k\ge1\), there are real-analytic branches satisfying the geometric assumptions with exactly \(4k\) regular fixed points of \(F\) and exactly two of \(G\), so the first-period difference \(2-4k\) is unbounded below. This realization assertion does not require the all-period hyperbolicity assumptions of the zeta identity.

## Assumptions and scope
Let \(I=[-1,1]\), with the cut \(0\) removed. Assume \(F:I\setminus\{0\}\to(-1,1)\) is odd, its positive branch is strictly increasing and continuously differentiable on \((0,1]\) with continuous one-sided extension to \(0\), and
\[
F(0^+)=-1,\quad F(0^-)=1,\quad 0<F(1)<1.
\]
The negative branch is determined by oddness. Define \(Q:[0,1]\to[0,1]\) by \(Q(0)=1\) and \(Q(u)=|F(u)|\) for \(u>0\). This is a continuous unimodal map with one minimum \(c\in(0,1)\) and \(Q(c)=0\). For the all-period identity, further assume (i) \(0\) is not periodic under \(Q\); and (ii) every regular periodic point of \(F\) is nonneutral, meaning \((F^n)'(x)\ne1\) whenever \(F^n(x)=x\) and the orbit avoids the cut. A regular periodic point is attracting if the derivative of its least-period return has absolute value strictly below one. All counts are finite under these assumptions. The dynamical zeta function is the formal series \(\zeta_T(t)=\exp(\sum_{n\ge1}a_n(T)t^n/n)\). No convergence of the infinite product as a numerical function is claimed or needed.

## Proof
**The sign reversal and absolute-value quotient.** Oddness implies that \(F\) commutes with reflection, hence \(G^n=(-1)^nF^n\) on every orbit avoiding the cut. Induction gives \(Q^n(u)=|F^n(u)|\) wherever the right-hand side is defined. For even \(n\), the fixed-point sets of \(G^n\) and \(F^n\) coincide.

**Crossing count for odd \(n\).** Put \(H_n(u)=Q^n(u)-u\). Since \(0\) is not periodic for \(Q\), \(H_n(0)=Q^n(0)>0\). Also \(H_n(1)<0\): otherwise \(Q^n(1)=1\); because \(Q^{-1}(1)=\{0\}\) and \(Q(0)=1\), this would make \(0\) periodic. There are finitely many monotonicity intervals of \(Q^n\). Any fixed point of \(Q^n\) avoiding the minimum \(c\) is regular and belongs to a smooth monotonicity interval; a periodic orbit hitting \(c\) would include \(0\) and make \(0\) periodic, which is excluded. Nonneutrality excludes a tangent crossing at an increasing-branch fixed point; a decreasing-branch fixed point always crosses strictly downward. Thus every fixed point gives a sign-changing crossing of \(H_n\).

Let \(D_n\) be the number of decreasing-branch fixed points of \(Q^n\), and let \(S_n,R_n\) be the number of increasing-branch fixed points with derivative below and above one, respectively. The signed crossing count between positive and negative endpoint values yields
\[
D_n+S_n-R_n=1.
\]
At an increasing-branch fixed point, \(F^n(u)=u\), so its two signed lifts \(\pm u\) are fixed by \(F^n\). At a decreasing-branch fixed point, \(F^n(u)=-u\), so the two lifts are fixed by \(G^n\) when \(n\) is odd. Consequently,
\[
a_n(F)=2(S_n+R_n),\quad a_n(G)=2D_n,\quad A_n(F)=2S_n.
\]
Combining these equalities gives \(a_n(G)-a_n(F)=2-4S_n=2-2A_n(F)\). The endpoint and hyperbolicity assumptions ensure that the fixed points are isolated and finite: there are finitely many monotone laps, with no accumulation at a critical iterate, zero or either endpoint.

**Formal zeta quotient.** Each attracting primitive cycle of least period \(\ell\) contributes exactly \(\ell\) attracting points to \(A_n(F)\) when \(\ell\mid n\), and none otherwise. Thus \(A_n(F)=\sum_{\ell\mid n}\ell b_\ell(F)\). The coefficient-wise formal logarithm of the quotient is
\[
\sum_{\substack{n\ge1\\n\text{ odd}}}\frac{(2-2A_n(F))t^n}{n}.
\]
Using \(\sum_{j\text{ odd}}t^j/j=\tfrac12\log((1+t)/(1-t))\), and interchanging sums coefficient-wise, gives exactly the stated product. The product is locally finite to every prescribed coefficient degree.

**Unbounded sharp sign-reversal defects.** Given \(k\ge1\), choose distinct \(0<r_1<\cdots<r_{2k}<1\), and set \(P(u)=\prod_{j=1}^{2k}(u-r_j)/r_j\). For sufficiently large real \(K\), define \(F_K(u)=u-e^{-Ku}P(u)\) on \(0<u\le1\), and extend oddly to the negative branch. Since \(P(0)=1\), \(F_K(0^+)=-1\); also \(0<F_K(1)<1\) when \(K\) is large. On \([0,r_1/2]\), \(P\) is bounded positively away from zero, so \(KP-P'>0\) for all sufficiently large \(K\). On \([r_1/2,1]\), \(e^{-Ku}(KP-P')\) tends uniformly to zero. Therefore \(F'_K(u)=1+e^{-Ku}(KP-P')>0\) everywhere. The positive fixed points of \(F_K\) are precisely \(r_j\); the derivative there is \(1-e^{-Kr_j}P'(r_j)\). Odd-indexed roots are repelling and even-indexed roots attracting, each hyperbolic for large \(K\). By reflection \(F_K\) has \(4k\) fixed points. The positive fixed-point equation for \(G_K=-F_K\) is \(F_K(u)+u=0\), with strictly increasing left side from \(-1\) to a positive number, hence it has exactly one positive root and, by reflection, one negative root. Therefore \(a_1(G_K)-a_1(F_K)=2-4k\), demonstrating that the correction is not uniformly bounded below. This part only uses the displayed branch conditions, not nonperiodicity of \(0\) or hyperbolicity of higher periods.

## Verification
The accompanying standalone `check.py` performs algebraic-root checks for an explicit rational-coefficient quadratic branch, verifies fixed-point stability and the first-period defect, and numerically tests odd-iterate fixed-count identities. It also samples the analytic realization family at multiple choices of \(k\). None of the finite numerical tests serves as a proof for the all-period identity; the proof is the crossing argument above.

## Relationship to prior work
Oliveira, *Homological reduction and entropy of discontinuous interval maps* (arXiv:2611.03287v1, first public November 2, 2026), Theorem 10.3 proves \(\zeta_{-F}/\zeta_F=(1+t)/(1-t)\) for uniformly expanding symmetric increasing Lorenz maps. The theorem here removes expansion while retaining a transparent nonneutrality condition, identifies the exact correction from attracting cycles, and constructs analytic maps with arbitrarily negative first-period defects. Anušić, Bruin and Činč (arXiv:1910.03361, 2019) analyze the unimodal/Lorenz correspondence and period forcing, but do not state this attractor-corrected zeta identity or the unbounded-defect realization. General fixed-point-index and kneading-zeta literature remains a potential source of stronger equivalent coverage; priority is not independently certified.

## Limitations
The all-period statement does not include periodic critical/cut orbits or neutral periodic points; at such parameters endpoint and tangent-crossing contributions can change. Analytic realizations establish the first-period defect only, without claiming that the exhibited branches satisfy every hypothesis of the all-period zeta identity. Formal zeta identities do not imply analytic continuation. No claim is made for nonsymmetric Lorenz maps or nonmonotone branch maps. Historical originality is subject to literature not located in the targeted search.

## References
- H. M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1 (first public 2026-11-02), Sections 10.1–10.2, especially Theorem 10.3. https://arxiv.org/html/2611.03287v1
- A. Anušić, H. Bruin, J. Činč, *Topological properties of Lorenz maps derived from unimodal maps*, arXiv:1910.03361 (first public 2019-10-08); Journal of Difference Equations and Applications 26 (2020), 1174–1191. https://arxiv.org/abs/1910.03361
- V. Baladi, G. Keller, *Zeta functions and transfer operators for piecewise monotone transformations*, Communications in Mathematical Physics 127 (1990), 459–477. https://doi.org/10.1007/BF02104498
