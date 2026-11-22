# Off-axis Lee–Yang density peaks induced by triangular decoration

## Finding

Let \(F_m=K_1\vee(mK_2)\) be the friendship graph consisting of \(m\ge1\) edge-disjoint triangles sharing a hub. In the uniform ferromagnetic Ising model at finite positive inverse temperature \(\beta\) and bond strength \(J>0\), put \(q=e^{-2\beta J}\), \(u=q^2\in(0,1)\), and use the complex uniform-field fugacity \(z=e^{-2\beta h}\). After removing a nonzero factor, the partition polynomial is exactly
\[
Z_m(z)=(1+2uz+uz^2)^m+z(u+2uz+z^2)^m. \tag{1}
\]

Every one of its \(2m+1\) zeros is simple and lies on the complex unit circle. The empirical measure of their arguments converges, as \(m\to\infty\) with \(\beta J\) fixed, to the strictly positive probability density
\[
\rho_u(\theta)=\frac{(1-u)(1+u+2u\cos\theta)}{2\pi\left([2u+(1+u)\cos\theta]^2+(1-u)^2\sin^2\theta\right)},\qquad -\pi\le\theta\le\pi. \tag{2}
\]
This density has **exactly two strict maxima**, at \(\theta=\pm\arccos c_u\), where
\[
c_u=\frac{-(1+u)+(1-u)\sqrt{1+3u}}{2u}\in(-1,1). \tag{3}
\]
Both \(\theta=0\) and \(\theta=\pi\) (viewed modulo \(2\pi\)) are strict local minima. Thus closing disjoint pairs of leaves of a high-degree Ising star into triangles changes the Lee–Yang limiting density from a single antipodal peak to **two off-axis peaks**. No limiting Lee–Yang density of a ferromagnetic star with arbitrary positive heterogeneous bonds can equal (2): every such star density is monotone on \((0,\pi)\), whereas (2) increases and then decreases there.

The closest zero to positive real fugacity has arguments \(\pm\theta_m\), with
\[
\theta_m=\frac{\pi}{1+2m(1-u)/(1+3u)}+O_u(m^{-3}),\qquad
m\theta_m\longrightarrow\frac{\pi(1+3u)}{2(1-u)}. \tag{4}
\]
In particular, this growing-degree graph family has no fixed positive-angle zero-free arc around \(z=1\), at any fixed \(\beta J>0\). Formulae (1)--(4) are exact finite-system or rigorously derived fixed-coupling limits, not assertions of an ordinary infinite-lattice thermodynamic critical point.

## Assumptions and scope

The graph \(F_m\) has \(2m+1\) labeled vertices: one hub and \(m\) disjoint peripheral pairs, each pair joined by an edge and both endpoints joined to the hub. The physical energy is \(H(\sigma)=-J\sum_{ij\in E(F_m)}\sigma_i\sigma_j-h\sum_{i\in V(F_m)}\sigma_i\), with \(\sigma_i\in\{-1,+1\}\). The fugacity polynomial is \(Z_m(z)=\sum_{U\subseteq V}z^{|U|}q^{|\delta(U)|}\), where \(U\) is the set of negative spins and \(\delta(U)\) the cut set. It differs from the physical partition function by a nonzero factor at every nonzero \(z\). All claims assume finite \(0<\beta J<\infty\) and fixed \(u\in(0,1)\) when \(m\to\infty\); the boundary cases \(u=0,1\) are excluded from the strict-density-peak statement.

The comparator is the growing ferromagnetic star \(K_{1,n}\), with arbitrary positive edge couplings whose \(q\)-parameters lie in \([0,1)\). Every finite star's boundary phase is strictly increasing; every weak-limit density in the uniformly positive-coupling regime is a positive mixture of \(\frac{1-q^2}{2\pi(1+q^2+2q\cos\theta)}\), which is nondecreasing on \([0,\pi]\). No claim is made about arbitrary non-star graphs or graphs with antiferromagnetic bonds.

## Proof

**Hub decomposition.** Condition on the hub spin. With hub positive, the possible negative-spin counts in one peripheral pair are \(0,1,2\); their cut weights sum to \(A(z)=1+2uz+uz^2\). With hub negative, its field contributes \(z\), and the pair contributes \(B(z)=u+2uz+z^2\). Multiplication over the \(m\) independent pairs gives (1).

**Exact boundary quantization and simplicity.** For \(z=e^{i\theta}\), set
\[
w_u(\theta)=e^{-i\theta}A(e^{i\theta})=2u+(1+u)\cos\theta-i(1-u)\sin\theta.
\]
Since \(0<u<1\), this ellipse never meets the origin and winds clockwise once around it. Choose its continuous argument \(f_u(0)=0\), \(f_u(-\pi)=\pi\), and \(f_u(\pi)=-\pi\). The identity \(B(z)=z^2A(1/z)\) gives on the circle \(A(z)=zw_u(\theta)\), \(B(z)=z\overline{w_u(\theta)}\). Consequently
\[
Z_m(e^{i\theta})=e^{im\theta}|w_u(\theta)|^m\big(e^{imf_u(\theta)}+e^{i\theta-imf_u(\theta)}\big),
\]
so zeros are exactly the solutions of \(2mf_u(\theta)-\theta\equiv\pi\pmod{2\pi}\). Direct differentiation yields
\[
f_u'(\theta)=-\frac{(1-u)(1+u+2u\cos\theta)}{|w_u(\theta)|^2}<0.
\]
The phase \(2mf_u(\theta)-\theta\) decreases strictly from \((2m+1)\pi\) to \(-(2m+1)\pi\) over \([-\pi,\pi]\). Its odd-multiple quantization gives \(2m+1\) distinct circle zeros after identifying the two endpoints. At each such zero the derivative of the phase is strictly negative and \(w_u\ne0\), so the zero is simple. Since (1) has degree \(2m+1\), these are all the zeros, including off-circle candidates.

**Density and leading-zero scale.** The normalized quantized phase levels have spacing \(2\pi/(2m+1)\) in angle-count units. Strict phase monotonicity and uniform smoothness therefore imply weak convergence of the empirical zero-angle measures to \(-f_u'(\theta)\,d\theta/(2\pi)\), which is (2). It is positive and integrates to one because \(f_u(-\pi)-f_u(\pi)=2\pi\). The smallest positive root solves \(2m[-f_u(\theta_m)]+\theta_m=\pi\). From
\[
-f_u(\theta)=\frac{1-u}{1+3u}\theta+O_u(\theta^3)
\]
and the strictly positive derivative coefficient, first \(\theta_m=O_u(m^{-1})\) and then equation (4) follows, with the displayed \(O_u(m^{-3})\) remainder.

**Exact peak count and star separation.** Write \(c=\cos\theta\) and omit the positive factor \((1-u)/(2\pi)\) from (2). The remaining fraction is
\[
\frac{1+u+2uc}{1-2u+5u^2+4u(1+u)c+4uc^2}.
\]
Its derivative with respect to \(c\) has the sign of
\[
P_u(c)=-4uc^2-4(u+1)c+3u^2-6u-1.
\]
On \([-1,1]\), \(P_u'=-8uc-4(u+1)<0\), while \(P_u(-1)=3(1-u)^2>0\) and \(P_u(1)=3u^2-14u-5<0\). Thus \(P_u\) has exactly one root \(c_u\in(-1,1)\), given by (3). As \(c\) decreases from \(1\) to \(-1\), (2) increases up to \(c_u\) and decreases thereafter, giving exactly the two stated strict peaks and the two strict endpoint minima. For comparison, each star Poisson kernel \((1-q^2)/(1+q^2+2q\cos\theta)\) is strictly increasing on \((0,\pi)\) for \(q>0\); any positive mixture is nondecreasing. Hence no such mixture can agree with the strictly bimodal density (2).

## Verification

The standalone `check.py` performs 18 exact-rational independent spin-configuration enumerations (up to 13 spins), reconstructing the partition polynomial from all cut weights, and 18 numerical polynomial-root and phase-quantization comparisons at distinct size/coupling pairs. It symbolically checks the density derivative identity, checks the unique interior peak for five couplings, checks monotonicity of the star comparator, numerically integrates the limiting density for four couplings, and checks first-zero asymptotic scaling at three large sizes for each coupling. The replay reports `ALL_CHECKS_PASSED`. These finite computations corroborate, but do not replace, the all-size analytic proof.

## Relationship to prior work

The Lee–Yang circle theorem already forces zeros of finite ferromagnetic Ising models onto the unit circle; **circle location alone is not claimed new**. Krasnytska, Berche, Holovatch and Kenna [1] analyze zero scaling on complete graphs and annealed scale-free networks, rather than this fixed triangular-petal geometry. Biskup, Borgs, Chayes, Kleinwaks and Kotecký [2] give general asymptotic phase-coexistence zero principles; they motivate phase quantization but do not supply the exact finite friendship-graph law or the off-axis two-peak separation. Peters and Regts [3] determine zero-free arcs for bounded-maximum-degree families; the degree of the shared hub here grows with size, so their fixed-degree theorem does not cover the collapsing gap in (4).

The published inhomogeneous-Ising-star analysis [4] provides a stronger *star-only* limiting zero distribution and boundary scaling, which are treated as prior results; it cannot imply the present twin-peak law, since all positive star-kernel mixtures are monotone on \((0,\pi)\). The peripheral-pair factor \(A(z)=1+2uz+uz^2\) has discriminant \(4u(u-1)<0\), so it cannot be the product of two independent positive-real star-leaf factors; the triangular decoration is not a positive-coupling star reweighting. Barata and Goldbaum [5] study periodic/aperiodic Ising chains and Cayley trees, not the friendship-graph family. The standard phase principle and star/Lee–Yang location facts are used as prior science, not claimed as inventions.

## Limitations

The claim is an exact finite-system and fixed-coupling increasing-degree limit. It does not prove an infinite-lattice bulk phase transition, infer an experimental realization, or generalize the peak classification to arbitrary triangle cacti, arbitrary edge weights, or uniform bounded-degree graphs. Finite root computations have numerical conditioning limits at very weak coupling; the simplicity theorem is analytic. Historical originality outside the inspected literature, including unindexed calculations of decorated stars, remains uncertain. Independent scientific audit has not been performed.

## References

[1] M. Krasnytska, B. Berche, Yu. Holovatch, R. Kenna, *Partition function zeros for the Ising model on complete graphs and on annealed scale-free networks*, arXiv:1510.00534v1, first posted 2015-10-02. https://arxiv.org/abs/1510.00534

[2] M. Biskup, C. Borgs, J. T. Chayes, L. J. Kleinwaks, R. Kotecký, *A General Theory of Lee–Yang Zeros in Models with First-Order Phase Transitions*, Phys. Rev. Lett. 84 (2000), 4794–4797. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/General-Theory-of-Lee-Yang-Zeros-in-Models-with-First-Order-Phase-Transitions.pdf

[3] H. Peters, G. Regts, *Location of zeros for the partition function of the Ising model on bounded degree graphs*, J. Lond. Math. Soc. 101 (2020), 765–785, first published online 2019-11-05. https://doi.org/10.1112/jlms.12286

[4] *Coupling-law tomography from Lee–Yang zeros of inhomogeneous Ising stars*, published result, 2026-10-12. https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-coupling-law-tomography-from-lee-yang-zeros-of-inhomogeneous-isi--fd8334aa6b45/RESULT.md

[5] J. C. A. Barata, P. S. Goldbaum, *On the distribution and gap structure of Lee–Yang zeros for the Ising model: periodic and aperiodic couplings*, J. Stat. Phys. 103 (2001), 857–891. https://doi.org/10.1023/A:1010332500031
