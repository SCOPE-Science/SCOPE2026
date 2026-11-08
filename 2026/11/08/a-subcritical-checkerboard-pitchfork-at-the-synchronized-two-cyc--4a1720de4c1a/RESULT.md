# A subcritical checkerboard pitchfork at the synchronized two-cycle stability edge

## Finding
For every fixed even integer \(N\ge4\), the nearest-neighbour quadratic Chebyshev coupled map lattice has a **subcritical spatial checkerboard pitchfork** of its synchronized primitive temporal two-cycle at
\[
a_*=\frac{11-4\sqrt6}{5}=0.240408205773457\ldots.
\]
On the lower-coupling side \(a<a_*\), sufficiently near \(a_*\), there are exactly two additional primitive two-cycles in a neighbourhood of the synchronized orbit, related by a one-site spatial shift. Both have precisely one expanding two-step Floquet multiplier and all other multipliers strictly within the unit disk; on the upper side \(a>a_*\) no such nearby nonsynchronized two-cycle exists. The synchronized orbit itself has exactly one expanding spatial mode immediately above \(a_*\) and is linearly attracting immediately below it.

For the two new orbits, fix the temporal phase near the larger synchronized value and write the even/odd site coordinates as \(m_0\pm d_0\). With the positive constant \(K\) defined in the proof, their amplitudes obey
\[
d_0=\pm\sqrt{K(a_*-a)}+O((a_*-a)^{3/2}),\quad K=1.10076997586155\ldots.
\]
Their unique unstable two-step multiplier has the sharp law
\[
\Lambda_{\mathrm{unst}}=1+16\sqrt6\,(a_*-a)+O((a_*-a)^2).
\]
The assertions are local in coupling and state space, with the admissible neighbourhood allowed to depend on \(N\). No claim is made of uniform neighbourhood size as \(N\to\infty\), global basin coverage, or nonlinear endpoint stability exactly at \(a=a_*\).

## Assumptions and scope
Take the even periodic ring \(\mathbb Z/N\mathbb Z\), \(N\ge4\), with synchronous dynamics
\[
(F_a(x))_j=(1-a)(2x_j^2-1)+\frac a2(x_{j-1}+x_{j+1}),\quad x\in[-1,1]^N,\quad 0\le a\le1.
\]
Both nearest-neighbour contributions are counted with weight \(a/2\). The cube is invariant by convexity. For \(0\le a<1/3\), set
\[
p(a)=\frac{-1-a+\sqrt{9a^2-18a+5}}{4(1-a)},\quad q(a)=\frac{-1-a-\sqrt{9a^2-18a+5}}{4(1-a)}.
\]
The spatially synchronized configurations \((p,\ldots,p)\) and \((q,\ldots,q)\) form a primitive temporal two-cycle. We classify two-step fixed points in a sufficiently small neighbourhood of its \(p\)-phase, thus counting each temporal two-cycle exactly once.

## Proof
**1. Exact linear collision and spectral gap.** The synchronized two-cycle follows by substitution in the scalar map \(h_a(z)=(1-a)(2z^2-1)+az\). The two-step Jacobian on spatial Fourier frequency \(c=\cos(2\pi k/N)\) has multiplier
\[
L_a(c)=[4(1-a)p(a)+ac][4(1-a)q(a)+ac]
=a^2c^2-2a(1+a)c-4+20a-8a^2.
\]
As \(\partial_cL_a=2a^2c-2a(1+a)<0\) when \(0<a<1\) and \(-1\le c\le1\), the largest multiplier occurs uniquely at \(c=-1\) (the one-dimensional checkerboard mode). It equals \(L_a(-1)=-5a^2+22a-4\), crosses \(+1\) at \(a_*=(11-4\sqrt6)/5\), and has derivative \(22-10a_*=8\sqrt6>0\). At the collision \(L_{a_*}(1)=-4+18a_*-9a_*^2\in(-1,1)\). Monotonicity then puts *all remaining* Fourier multipliers strictly in \((-1,1)\) for each fixed even ring; only the checkerboard eigenvalue is \(+1\). This gives a simple spatial-symmetry-breaking kernel with a contracting complementary subspace.

**2. Exact two-colour reduction.** For an alternating configuration \(x_{2j}=m+d\), \(x_{2j+1}=m-d\), the map acts by
\[
m'=2(1-a)(m^2+d^2)-(1-a)+am,\qquad d'=[4(1-a)m-a]d.
\]
Put \(u=1-a\), \(b(m,a)=4um-a\), \(A(m,a)=4um+a\). A two-step orbit in the \(p\)-phase is described by \((m_0,d_0)\to(m_1,d_1)\to(m_0,d_0)\). Set \(t=d_0^2\), so \(d_1=b(m_0,a)d_0\). The equations for the two means become
\[
\begin{aligned}
m_1&=2u(m_0^2+t)-u+am_0,\\
m_0&=2u\bigl(m_1^2+b(m_0,a)^2t\bigr)-u+am_1.
\end{aligned}
\]
At \((a,t)=(a_*,0)\), they have \((m_0,m_1)=(P,Q):=(p(a_*),q(a_*))\). Their Jacobian determinant with respect to the two means is \(1-A_0A_1\ne0\), where \(A_0=4(1-a_*)P+a_*\), \(A_1=4(1-a_*)Q+a_*\). Indeed \(A_0A_1=L_{a_*}(1)\in(-1,1)\). Hence the analytic implicit-function theorem gives unique analytic means \(m_0(a,t),m_1(a,t)\) near \((a_*,0)\), continuing \(p(a),q(a)\) on \(t=0\).

Differentiate the mean equations in \(t\) at the collision. Denote \(b_0=4(1-a_*)P-a_*\), \(b_1=4(1-a_*)Q-a_*\), and \(c_j=\partial_t m_j(a_*,0)\). We obtain
\[
c_1=A_0c_0+2(1-a_*),\quad
c_0=A_1c_1+2(1-a_*)b_0^2,
\]
so that
\[
c_0=\frac{2(1-a_*)(A_1+b_0^2)}{1-A_0A_1},\quad
c_1=A_0c_0+2(1-a_*).
\]
The remaining two-cycle equation is \(d_0H(a,t)=0\), where
\[
H(a,t)=b(m_0(a,t),a)b(m_1(a,t),a)-1.
\]
On the synchronized branch \(H(a,0)=-5a^2+22a-5\), hence \(H_a(a_*,0)=8\sqrt6\). Also
\[
B:=H_t(a_*,0)=4(1-a_*)(b_1c_0+b_0c_1)=17.802009840364\ldots>0.
\]
Positivity is exact: using the displayed radical formulae for \(a_*,P,Q\), rational squaring bounds give \(0.2404<a_*<0.2405\), \(-0.41<b_0<-0.37\), \(-2.60<b_1<-2.55\), \(0.07<A_0<0.12\), and \(-2.13<A_1<-2.05\). Inserting these into the rational expressions for \(c_0,c_1\) gives \(-3<c_0<-2\) and \(1<c_1<2\), so \(b_1c_0+b_0c_1>2.55\cdot2-0.41\cdot2>0\). Each interval bound may be checked by squaring positive rational bounds for the two nested radicals.

By the implicit-function theorem for \(H(a,t)=0\), the only nearby nonzero checkerboard solutions have
\[
t(a)=\frac{8\sqrt6}{B}(a_*-a)+O((a_*-a)^2).
\]
Thus exactly two real signs \(d_0=\pm\sqrt{t(a)}\) occur when \(a<a_*\), none when \(a>a_*\); both stay within the interior of the invariant cube.

**3. No missed non-checkerboard orbits.** For the full return equation \(F_a^2(x)-x=0\), the critical linear kernel is exactly the one-dimensional checkerboard eigenspace and the derivative restricted to its translation-invariant complement is invertible. Lyapunov–Schmidt reduction uniquely solves the complementary equation as a function of the checkerboard coordinate and \(a\). The translation by two sites fixes the kernel and commutes with the map, so uniqueness forces the entire reconstructed state to be fixed by translation by two. Every nearby return-fixed state is therefore precisely of the two-colour form already classified. As \(P\ne Q\), these are primitive temporal two-cycles, and the two opposite checkerboard signs are distinct cycles, not the two temporal phases of one cycle.

**4. Saddle nature and coefficient.** On the two-colour return map, the mean direction has multiplier \(A_0A_1\in(-1,1)\) at the collision. Eliminating its fixed-point equation gives the scalar reduced fixed-point equation \(d_0H(a,d_0^2)=0\). Along either nonzero branch, its derivative in the difference coordinate is \(2Bt(a)+O(t(a)^2)\), giving the Floquet eigenvalue
\[
\Lambda_{\mathrm{unst}}=1+2Bt(a)+O(t(a)^2)
=1+16\sqrt6\,(a_*-a)+O((a_*-a)^2)>1.
\]
All other full-ring multipliers remain strictly in the unit disk by the spectral gap and continuity, for each fixed \(N\). Hence each new orbit has exactly one unstable direction. This proves the pitchfork is subcritical; the synchronized orbit changes from attracting to one-direction unstable at \(a_*\).

## Verification
The complete standalone Python 3 program `verify_pitchfork.py` (NumPy required) directly applies the two-colour update, constructs both full-ring Jacobians and their products, and checks the exact synchronized Fourier polynomial, critical radicals, positive branch coefficient, two-step orbit equations, and full-ring saddle spectra. It passed 124 assertions across ring sizes \(N=4,6,8,10,12,16\) and the three tested distances \(10^{-3},10^{-4},10^{-5}\) below the critical coupling. Numerical sampling is supportive, not a substitute for the analytic existence, uniqueness and all-size spectral arguments above. Run `python3 verify_pitchfork.py` beside the embedded source file.

## Relationship to prior work
Dettmann (2001 preprint, 2002 publication) gives synchronized two-cycle formulae and the associated linear stability window for the backward-coupled Chebyshev 2B system, including the upper boundary \(a_*\). Lippolis (first available 2025-10-14) re-examines synchronized coupled-map stability via spatiotemporal Floquet methods; the critical Fourier mode is implicit in that analysis. Both contributions are prior art. Neither inspected account computes the nonlinear checkerboard pitchfork direction, proves the exact two-saddle local branch count, or gives the positive coefficient \(B\) and its unstable multiplier asymptotics. The 2001 manuscript text was accessible through the CiteseerX PDF text view, although screenshot retrieval returned access errors; relevant formulae, Tables 1–3 and conclusions were read. Dettmann–Lippolis (2003 preprint) studies finite two-site Chebyshev cycles primarily at weak coupling and does not supply this all-even-ring bifurcation.

A separate exact checkerboard **travelling** two-cycle with values \((\sqrt5-1)/4\) and \(-(\sqrt5+1)/4\) is known for all couplings and is stable at strong coupling; it is different from the two spatially nonuniform saddle cycles born here near \(P\approx-0.049\), \(Q\approx-0.768\) at \(a\approx0.2404\). A prior published theorem proving the travelling branch's Floquet spectrum was checked in full (published-finding corpus record identifier ending `9a03241b8715`). Standard pitchfork and Lyapunov–Schmidt methods are not themselves claimed new.

## Limitations
The result is a local finite-ring bifurcation theorem; the neighbourhood may shrink with \(N\), and it does not classify global attractors, basins, non-period-two orbits, infinite-lattice bifurcations, or neutral dynamics exactly at the threshold. General symmetry-breaking literature and unindexed historical results remain potential priority risks. No independent scientific validation has been performed.

## References
1. D. Lippolis, *Spatiotemporal stability of synchronized coupled map lattice states*, arXiv:2510.12532 (first publicly posted 2025-10-14), *Physica D* 490 (2026), 135148. https://arxiv.org/html/2510.12532.
2. C. P. Dettmann, *Stable synchronised states of coupled Tchebyscheff maps*, arXiv:nlin/0110007 (first available 2001-10-29), *Physica D* 172 (2002), 88–102. https://arxiv.org/abs/nlin/0110007. Accessible text: https://citeseerx.ist.psu.edu/document?doi=125979fdc1e23d4fd9d2222da976eea6383b4bf8&repid=rep1&type=pdf.
3. C. P. Dettmann and D. Lippolis, *Periodic orbit theory of two coupled Tchebyscheff maps*, arXiv:nlin/0312024 (2003 preprint), *Chaos, Solitons & Fractals* 23 (2005), 43–54. https://arxiv.org/abs/nlin/0312024.
4. *A sharp strong-coupling window for a two-colour travelling wave*, published-finding corpus public research record `2026/10/11/SCOPE-a-sharp-strong-coupling-window-for-a-two-colour-travelling-wave--9a03241b8715` (all-even-ring travelling branch). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-strong-coupling-window-for-a-two-colour-travelling-wave--9a03241b8715.
