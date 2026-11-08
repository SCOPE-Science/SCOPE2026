# An Airy-edge law for finite-survivor entropy in a mixing infinite-entropy interval map

## Finding
Consider the explicit infinite-entropy mixing interval map \(D_+\) built from successively more oscillatory affine blocks by Vinod Kumar P B [1]. For each integer \(K\ge1\), retain **all points that never leave the first \(K+1\) unit blocks**:
\[
S_K=\{x\in[0,K+1]:D_+^n(x)\in[0,K+1]\text{ for every integer }n\ge0\}.
\]
This is a natural compact invariant subsystem, and its entropy \(h_K=h_{\rm top}(D_+|_{S_K})\) is exactly computable. Set \(M_K=(m_{ij})_{0\le i,j\le K}\) with
\[
m_{ij}=\begin{cases}2(i+2)+1,&j=i,\\2(i+2),&|i-j|=1,\\0,&|i-j|>1.\end{cases}
\]
Then \(h_K=\log\rho(M_K)\). If \(a_1=2.338107410\ldots\) denotes the absolute value of the first negative zero of the Airy function, then
\[
\boxed{\rho(M_K)=6K-a_1 72^{1/3}K^{1/3}+o(K^{1/3})},
\]
and therefore
\[
\boxed{h_K=\log(6K)-\frac{a_1 72^{1/3}}6 K^{-2/3}+o(K^{-2/3}).}
\]
The coefficient \(a_1 72^{1/3}\) is approximately \(9.726918802\). Thus the natural finite-core entropy does not merely diverge logarithmically: its **sharp noninteger-power boundary correction** is determined by a Dirichlet Airy eigenvalue.

For every finite \(K\), \(\rho(M_K)\) is the largest zero of the explicitly recursive polynomial
\[
P_0(z)=1,\qquad P_1(z)=z-5,\qquad
P_{j+1}(z)=(z-2j-5)P_j(z)-4(j+1)(j+2)P_{j-1}(z),\ j\ge1.
\]
In particular, \(\rho(M_1)=11\).

## Assumptions and scope
The map is **precisely** the piecewise-affine map from Proposition 5.2 of [1]. Write \(B_j=[j,j+1]\), \(N_j=j+2\), and specify its values at successive subdivision vertices. On \(B_0\) the vertex-value sequence is \(0,(1,2,1,0)\) repeated \(N_0=2\) times, and then \(1\). On each \(B_j\), \(j\ge1\), the sequence is \(j,(j-1,j,j+1,j+2,j+1,j)\) repeated \(N_j\) times, and then \(j+1\). Between successive equally spaced subdivision vertices the map is affine. The sequences agree at block endpoints, defining a continuous map of the nonnegative half-line. Every affine subdivision interval maps homeomorphically onto exactly one unit block. Its absolute slope is at least five [1].

The entropy is the topological entropy of the **closed forward survivor** \(S_K\). No assertion equates this with all bounded orbits, the full noncompact map's infinite entropy, or an arbitrary cutoff scheme. The limit is over positive integers \(K\to\infty\), using natural logarithms. The Airy constant is defined by \(\operatorname{Ai}(-a_1)=0\) with \(a_1>0\) minimal. No probabilistic or random-matrix assertion is used.

## Proof
**1. Exactly count permitted transitions.** Fix a cutoff \(K\). From the defining vertex sequence on \(B_0\), precisely \(2N_0+1=5\) affine pieces map onto \(B_0\) and \(2N_0=4\) map onto \(B_1\). For \(j\ge1\), each six-step repetition contains exactly two pieces mapping onto each of \(B_{j-1}\), \(B_j\), and \(B_{j+1}\). The final subdivision piece maps onto \(B_j\). Thus the counts inside cutoff blocks are exactly the entries of \(M_K\). Branches whose images are \(B_{K+1}\) leave the core except possibly at endpoints, a set with zero entropy.

Every allowed finite directed path in this multigraph defines a nonempty interval of initial points following its specified affine branches. Since each branch expands by an absolute factor at least five, a nested infinite itinerary defines a unique point. The symbolic coding maps the finite edge shift onto the survivor and is injective away from orbits that eventually meet a subdivision boundary. Although a fixed boundary point can have multiple symbolic addresses, this exceptional set has zero Parry measure: there are at most two branch choices at each subsequent visit to a fixed integer boundary, whereas each length-\(n\) cylinder has Parry measure at most \(C\rho(M_K)^{-n}\) with \(\rho(M_K)\ge5>2\). Preimages of the countably many subdivision boundaries also have zero Parry measure. Thus the maximal-entropy Parry measure projects with its entropy unchanged; conversely entropy cannot increase under the coding factor. This proves \(h_K=\log\rho(M_K)\). The matrix is irreducible and nonnegative.

**2. Symmetrization and exact finite recurrence.** Conjugating \(M_K\) by the positive diagonal matrix with entries \(\sqrt{j+2}\) yields the symmetric Jacobi matrix \(J_K\) whose diagonal and successive positive off-diagonal entries are
\[
d_j=2j+5,\qquad b_j=2\sqrt{(j+2)(j+3)},\qquad 0\le j<K.
\]
Consequently \(\rho(M_K)=\lambda_{\max}(J_K)\). Expansion of \(\det(zI-J_K)\) along its last row gives the stated recurrence for its characteristic polynomial, including \(P_1=z-5\) and the factor \(b_{j-1}^2=4(j+1)(j+2)\).

**3. A Dirichlet-form identity.** Extend \(b_j=2\sqrt{(j+2)(j+3)}\) also to \(j=-1\) and \(j=K\), and set \(v_{-1}=v_{K+1}=0\). For every real unit vector \(v=(v_0,\ldots,v_K)\), writing \(V_j=d_j+b_{j-1}+b_j\) gives the exact identity
\[
6K-\langle v,J_Kv\rangle
=\sum_{j=-1}^{K}b_j(v_{j+1}-v_j)^2
+\sum_{j=0}^{K}(6K-V_j)v_j^2.
\]
The explicit square roots imply the uniform bound \(|V_j-(6j+13)|\le C\) for all \(j\ge0\), with an absolute finite constant \(C\). In particular, the right side is bounded below by \(\sum b_j(v_{j+1}-v_j)^2+6\sum(K-j)v_j^2-C'\). This localizes top eigenvectors within \(O(K^{1/3})\) sites of the final block.

**4. The Airy limit, including the lower bound.** Put \(\ell=K^{1/3}\), and for a smooth compactly supported function \(u\) on the positive half-line satisfying \(u(0)=0\), choose a trial vector by
\[
v_j=\ell^{-1/2}u((K+1-j)/\ell),\quad 0\le j\le K,
\]
then normalize it in Euclidean norm. Riemann sums, \(b_j/K\to2\) uniformly for \(K-j=O(\ell)\), and \(6K-V_j=6(K-j)+O(1)\) show that its quotient by \(\ell\) converges to
\[
\mathcal E(u)=\frac{2\int_0^\infty |u'(t)|^2dt+6\int_0^\infty t|u(t)|^2dt}{\int_0^\infty|u(t)|^2dt}.
\]
This proves \(\limsup_{K\to\infty}(6K-\rho(M_K))/\ell\le\inf\mathcal E\).

For the converse, let \(v^{(K)}\) be unit positive top eigenvectors. The trial estimate and the nonnegative gradient term imply
\[
\sum_{j=0}^K(K-j)|v_j^{(K)}|^2=O(\ell),\qquad
\sum_{j=-1}^Kb_j|v_{j+1}^{(K)}-v_j^{(K)}|^2=O(\ell).
\]
Consequently the \(\ell^{1/2}\)-rescaled piecewise-linear interpolants with mesh \(1/\ell\) in the coordinate \(t=(K+1-j)/\ell\) are tight in \(L^2(0,\infty)\), have bounded \(H^1\) energy on every compact interval, and satisfy a Dirichlet condition at \(t=0\). Indeed the first bound gives a tail-mass bound \(O(1/R)\) beyond \(t=R\); on \(j\ge K/2\) the second bound controls the full rescaled discrete derivative since \(b_j\ge cK\). Subsequences therefore converge strongly in \(L^2\) and weakly in local \(H^1\) to a norm-one Dirichlet function. Lower semicontinuity of the gradient energy, together with Fatou's lemma for the nonnegative linear potential, gives
\[
\liminf_{K\to\infty}\frac{6K-\rho(M_K)}{\ell}\ge\inf\mathcal E.
\]
Both inequalities are thus equalities, without assuming convergence merely from a numerical profile.

**5. Identify the constant.** The minimizer of \(\mathcal E\) is the ground state of \(-2d^2/dt^2+6t\) on \((0,\infty)\) with Dirichlet boundary at zero. Solving this ODE using the decaying Airy function gives its lowest eigenvalue \(a_1(2\cdot6^2)^{1/3}=a_1 72^{1/3}\). Therefore \(6K-\rho(M_K)\sim a_1 72^{1/3}K^{1/3}\). Expanding the logarithm of \(6K\) times \(1-(a_1 72^{1/3}/6)K^{-2/3}+o(K^{-2/3})\) proves the entropy formula.

## Verification
The standalone `CHECK.py` reconstructs the source's subdivision vertex lists and independently counts all target blocks for cutoff sizes up to \(K=24\). It checks finite-dimensional characteristic roots with a Sturm recurrence on the symmetric Jacobi matrix, including the exact \(K=1\) root \(11\). It completed 359 deterministic checks. Numerical values of the scaled edge deficit are \(7.807746969\) at \(K=1000\), \(8.520953729\) at \(K=4000\), versus the proved asymptotic \(9.726918802\). Their slow approach is consistent with, not a proof of, the asymptotic; the infinite statement follows from Steps 3–5. Run `python3 CHECK.py` with Python 3 standard library.

## Relationship to prior work
Vinod Kumar P B [1] constructs \(D_+\) to obtain a mixing map of infinite entropy, using unbounded block horseshoes. That source does not calculate entropy of the compact bounded-block survivors or a finite-cutoff asymptotic. A published result [2] gives a finite-core dynamical-zeta and Perron correction for a **different** countable interval map with four-adically growing branches; its compressed transition matrix and edge scale differ and do not imply this theorem. Another published result [3] obtains a Dirichlet Airy correction for the numerical radius of an **infinite geometrically weighted periodic shift**; neither its operator nor its limit parameter is the growing finite-block interval map here. Classical studies [4–5] give general asymptotic bounds for extreme zeros of orthogonal polynomials, providing methodological background rather than a checked assertion of these exact finite-survivor entropy constants. The present derivation is self-contained.

## Limitations
The cutoff is the initial consecutive block family, not an arbitrary finite subsymbolic subsystem. The theorem does not count individual periodic orbits, determine a maximizing measure for the full noncompact map, provide a uniform finite-\(K\) remainder estimate, or transfer automatically to other infinite-entropy interval maps. Generic Jacobi-matrix asymptotic literature may contain closely related limiting techniques; historical priority remains subject to broader specialist review. The verification script tests finite cases only.

## References
1. Vinod Kumar P B, *The entropy spectra of chaotic maps of an interval*, arXiv:2610.39443v1, first public October 29, 2026, especially Proposition 5.2 and Section 6. https://arxiv.org/html/2610.39443v1
2. *Exact finite-cutoff zeta and Perron correction for a countable Markov map*, public mathematical result, October 11, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-finite-cutoff-zeta-and-perron-correction-for-a-countable-m--35b9405279c4
3. *A sharp Airy-edge law for four-periodic geometric weighted shifts*, public mathematical result, October 11, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-airy-edge-law-for-four-periodic-geometric-weighted-shift--cffc9a187d0d
4. A. Máté, P. Nevai and V. Totik, *Asymptotics for the zeros of orthogonal polynomials associated with infinite intervals*, J. London Math. Soc. 33 (1986), 303–310. https://doi.org/10.1112/jlms/s2-33.2.303
5. I. Krasikov, *Turán inequalities and zeros of orthogonal polynomials*, arXiv:math/0401299 (2004). https://arxiv.org/abs/math/0401299
