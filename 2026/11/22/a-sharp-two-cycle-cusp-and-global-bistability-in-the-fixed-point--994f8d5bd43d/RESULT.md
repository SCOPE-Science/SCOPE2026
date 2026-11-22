# A sharp two-cycle cusp and global bistability in the fixed-point-free cosine map

## Finding
For the cosine piecewise map of Lawnik–Moysis–Volos [1], on the entire strict-alternation parameter region \(0<c<b<a<1\), every forward orbit converges to a primitive period-two orbit. There are never more than three such orbits, and all invariant Borel probability measures are mixtures of the corresponding uniform orbit measures. A complete sharp phase diagram is as follows.

Define \(A=\pi/2\), \(q=(1-a)/(1-b)\), \(r=c/b\), so \(0<q,r<1\), and for \(0\le u\le1\) put
\[
C_q(u)=\cos\!\left(Aq\cos(Au)\right),\quad Q_q(u)=\frac{u}{C_q(u)},\quad H_q(u)=C_q(u)-u C_q'(u).
\]
Let \(s_*\) denote the **unique** solution of \(s\tan s=1\) in \((0,\pi/2)\), and set
\[
\boxed{q_*=\frac{2}{\pi\sin s_*}=0.8398011138606\ldots}\qquad
u_*=\frac{2s_*}{\pi}=0.5477053736017\ldots.
\]
* If \(0<q\le q_*\), exactly **one** primitive two-cycle exists for every \(0<r<1\). It is hyperbolically attracting except at \((q,r)=(q_*,q_*)\), where its two-step multiplier is \(+1\) and its attraction is algebraic.
* If \(q_*<q<1\), the function \(H_q\) has precisely two zeros \(u_-<u_+\) in \((0,1)\). Put \(r_{\rm high}=Q_q(u_-)\), \(r_{\rm low}=Q_q(u_+)\), where \(0<r_{\rm low}<r_{\rm high}\) and \(r_{\rm low}<1\). For admissible \(0<r<1\), the number of geometrically distinct primitive two-cycles is **three** if \(r_{\rm low}<r<r_{\rm high}\), **two** if \(r=r_{\rm low}\) or \(r=r_{\rm high}\), and **one** otherwise. Boundary equalities outside \((0,1)\) are omitted. In the three-cycle region the outer cycles attract, and the middle one repels. At each admissible fold, the colliding orbit has multiplier \(+1\), and the other orbit attracts.

Both fold collisions are nondegenerate. In particular the three-cycle region contains the entire curve \(q=r\in(q_*,1)\) and an open neighborhood of each of its points, so the two attracting cycles genuinely coexist on an open set of the original three-parameter family.

At the unique cusp \(q=r=q_*\), write \(u_n\) for the normalized left-branch position after \(n\) full two-step returns. For **every** \(u_0\in[0,1]\setminus\{u_*\}\),
\[
\boxed{\lim_{n\to\infty}\sqrt n\,(u_n-u_*)=\frac{\operatorname{sgn}(u_0-u_*)}{\sqrt{2K_*}},\qquad K_*=\frac{\pi^2}{4}\left(\frac13+\frac{s_*^2}{2}\right)>0.}
\]
Numerically \(K_*=1.7356199618\ldots\). For original starting points on the right branch, first apply one iteration to enter the left branch before using this law.

## Assumptions and scope
The state space is \([0,1]\), with the left formula used at the switching point \(x=b\). The map is
\[
F_{a,b,c}(x)=\begin{cases}
1-(1-a)\cos\!\left(\frac{\pi x}{2b}\right),&0\le x\le b,\\[2pt]
c\cos\!\left(\frac{\pi(x-1)}{2(1-b)}\right),&b<x\le1.
\end{cases}
\]
Parameters are real and satisfy \(0<c<b<a<1\). A primitive two-cycle is a two-element orbit, counted as a set rather than by its two starting phases. At a cycle \(\{x,y\}\) the two-step multiplier means \((F^2)'(x)=(F^2)'(y)\), since both points are away from the switching location. The count includes nonhyperbolic fold and cusp cycles. The normalized return coordinate is \(u=x/b\) on the left; its partner on the right is represented by \(v=(1-y)/(1-b)\).

## Proof
**1. Exact branch alternation and return.** Because \(a>b>c\), the left branch maps \([0,b]\) into \([a,1]\subset(b,1]\) and the right branch maps \((b,1]\) into \((0,c]\subset[0,b)\). Consequently, after at most one step the dynamics alternates between these two halves. The left-to-right map in normalized coordinates is \(v=q\cos(Au)\), and the right-to-left map is \(u'=r\cos(Av)\). Therefore the exact two-step return is
\[
G_{q,r}(u)=r\cos\!\left(Aq\cos(Au)\right)=r C_q(u),\quad 0\le u\le1.
\]
It is strictly increasing in the interior, maps \([0,1]\) into \((0,r]\subset(0,1)\), and has \(G(0)>0\), \(G(1)=r<1\). Each fixed point gives exactly one primitive two-cycle of \(F\), and every such cycle arises in this way. A continuous increasing self-map of an interval has no periodic points other than fixed points and every orbit converges to a fixed point: the first increment fixes the direction of all later increments. Thus there are no other periodic or recurrent orbit types, and all orbits of \(F\) converge to one of the period-two cycles.

**2. Unique derivative peak and the shape of \(Q_q\).** Put \(p=Aq\in(0,\pi/2)\) and \(s(u)=p\cos(Au)\). In the open interval,
\[
C_q'(u)=Ap\sin(Au)\sin s(u)>0.
\]
Its logarithmic second derivative is
\[
(\log C_q')''=-A^2\csc^2(Au)+s''(u)\cot s(u)-(s'(u))^2\csc^2s(u)<0.
\]
Indeed \(s''=-A^2s<0\) and \(0<s<p<\pi/2\). As \(C_q'\to0\) at both endpoints, it has exactly one interior maximum \(m_q\). Hence \(C_q''\) changes sign once, from positive to negative. Now
\[
Q_q'(u)=\frac{H_q(u)}{C_q(u)^2},\qquad H_q'(u)=-u C_q''(u).
\]
Thus \(H_q\) strictly decreases to its unique minimum at \(m_q\) and then strictly increases; its endpoint values \(H_q(0)=\cos p>0\), \(H_q(1)=1>0\). There can be at most two zeros, and \(Q_q\) has at most one local maximum and one local minimum. A horizontal line \(r\in(0,1)\) therefore meets its graph at most three times.

**3. Exact cusp threshold.** For fixed interior \(u\), differentiation with respect to \(p\) yields
\[
\frac{\partial H}{\partial p}=-\cos(Au)\sin s-uA\sin(Au)\bigl(\sin s+p\cos(Au)\cos s\bigr)<0.
\]
Define \(s_*\) by \(s_*\tan s_*=1\); existence and uniqueness follow because \(s\tan s\) increases continuously from zero to infinity. Set \(q_*=1/(A\sin s_*)\) and \(u_*=s_*/A\). The decreasing cosine map \(f_q(u)=q\cos(Au)\) satisfies \(f_{q_*}(u_*)=u_*\) and \(f_{q_*}'(u_*)=-1\). Its square is \(G_{q_*,q_*}\), hence \(G(u_*)=u_*\), \(G'(u_*)=1\), and \(G''(u_*)=0\). Thus \(H_{q_*}(u_*)=0\) and \(C_{q_*}''(u_*)=0\); the derivative-peak uniqueness in Step 2 shows this is the unique minimum, equal to zero. Strict monotonicity in \(p\) proves \(H_q>0\) everywhere for \(q<q_*\), and a strictly negative interior minimum for \(q>q_*\). For \(q=q_*\), \(H_q\ge0\), with exactly one zero at \(u_*\). This proves the unique-cycle regime and the two-turning-point regime stated in the finding.

For \(q>q_*\), the two simple zeros of \(H_q\) determine a strict local maximum and minimum of \(Q_q\) as claimed. Since \(Q_q(0)=0\) and \(Q_q(1)=1\), elementary intersection counting yields precisely the listed one/two/three-cycle census, including equality cases. The multiplier at a root \(r=Q_q(u)\) is
\[
\lambda=G'(u)=rC_q'(u)=1-\frac{H_q(u)}{C_q(u)}>0.
\]
It is below one on increasing portions of \(Q_q\), above one on the decreasing portion, and exactly one at a turning point. The turning points are nondegenerate because \(H_q'=-uC_q''\ne0\) there; Taylor expansion of \(rC_q(u)-u\) gives the usual nonzero square-root fold coefficient, explicitly \(\sqrt{-2C_q(u_c)\delta/(r_c C_q''(u_c))}\) in the direction where the radicand is positive, where \(r=r_c+\delta\).

**4. Sharpness, physical basins, and invariant measures.** For every \(q>q_*\), the map \(f_q(u)=q\cos(Au)\) has exactly one fixed point \(z_q\); it moves strictly upward with \(q\), and its derivative satisfies \(f_q'(z_q)<-1\). For \(r=q\), the return is \(G=f_q^2\). Hence \(z_q\) is a repelling fixed point of \(G\), while \(G(0)>0\) and \(G(1)<1\) guarantee one further fixed point on either side. Step 2 makes three the maximum, so both outer fixed points attract. Hyperbolicity and continuity in the parameters give an open neighborhood of bistability. For any three-cycle parameter point, the unique middle repeller separates the two basins in normalized left coordinates; the matching right-hand boundary is its partner. The discontinuity may contribute further preimage boundary points; the exact full boundary topology is not asserted. Each forward orbit converges to a cycle; applying dominated convergence to the even iterates of any invariant probability, and then invariance under one step, shows that every invariant Borel probability is a convex combination of the uniform measures on the finitely many cycles.

**5. Exact critical relaxation.** At \(q=r=q_*\), Taylor-expand \(f(u_*+e)-u_*\):
\[
-e-\frac{A s_*}{2}e^2+\frac{A^2}{6}e^3+O(e^4).
\]
Composition gives
\[
G(u_*+e)-(u_*+e)=-K_*e^3+O(e^4),\qquad K_*=A^2\left(\frac13+\frac{s_*^2}{2}\right)>0.
\]
The return map is increasing with a unique fixed point, so all its nonfixed orbits converge monotonically to \(u_*\) without changing sign of the error. For their errors \(e_n\), the expansion implies \(e_{n+1}^{-2}-e_n^{-2}=2K_*+o(1)\). Cesàro summation yields \(n e_n^2\to (2K_*)^{-1}\) and the signed square-root limit.

## Verification
The companion `verify_cosine_cusp.py` checks the original two-branch map against the normalized return, verifies the analytical cusp equations and cubic coefficient, checks exactly three numerical roots at \((a,b,c)=(51/100,1/2,49/100)\), and verifies the global basin classification for a representative grid. It also independently checks rational Taylor bounds used to sign-certify this explicit example; the proof above does not depend on floating-point root enumeration. At the rational benchmark the three normalized left fixed points are approximately \(0.03278103685\), \(0.58928797223\), and \(0.97870107150\), with multipliers approximately \(0.1218988\), \(1.5128615\), \(0.1218988\). The checker is diagnostic: global uniqueness and parameter-uniform claims are proved analytically in Steps 1–5, not inferred from finite scans.

## Relationship to prior work
Lawnik, Moysis and Volos [1] introduced these cosine branches and supplied numerical fixed-point and Lyapunov phase diagrams, but not the strict-alternation sharp two-cycle cusp, its complete phase diagram or the critical relaxation constant. The closely related prior indexed theorem [2] analyzes the **complementary** cosine parameter range \(b=1/2\), \(1/4\le a<1/2\), \(0<c<1/2\): there the normalized gain \(q>1\), the left branch does not map wholly to the right, and the theorem counts zero/one/two cycles. It neither contains nor implies the \(q<1\) global alternating three-cycle regime, exact cusp, or all-orbit convergence proved here. A prior exact cusp and bistability analysis for a *polynomial* fixed-point-free interval map [3] illustrates the general mechanism but uses different power-law branches, algebraic thresholds and proof; its statements do not yield the trigonometric threshold \(s_*\tan s_*=1\). The related 2024 work [4] uses modified logistic/tent transformations rather than the present cosine branches.

## Limitations
All claims are restricted to the strict-alternation region \(0<c<b<a<1\) and to exact-real arithmetic; dynamics outside it can have different itineraries. The full fold diagram is implicit through unique scalar extrema of an explicitly defined trigonometric function, not a closed elementary expression for its fold locations. At the cusp and folds the indicated cycles are neutral and should not be called hyperbolically attracting. The result does not establish numerical pseudorandomness or cryptographic security. Publication priority is limited to the inspected literature and indexed sources; a broader unindexed equivalent analysis could exist, and the full text of [4] was not examined.

## References
[1] M. Lawnik, L. Moysis, C. Volos, “A Family of 1D Chaotic Maps without Equilibria,” *Symmetry* **15** (2023), 1311, first published 27 June 2023, doi:10.3390/sym15071311, Section 4.2, Equation (20). Full HTML text: https://www.mdpi.com/2073-8994/15/7/1311.

[2] “A sharp two-cycle fold in the fixed-point-free cosine interval map,” published mathematical record, 2 November 2026, public `RESULT.md` at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-two-cycle-fold-in-the-fixed-point-free-cosine-interval-m--ea85f36942c0 (full theorem and proof inspected).

[3] “Exact two-cycle cusp, bistability, and global convergence in a fixed-point-free quadratic map,” published mathematical record, 1 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-two-cycle-cusp-bistability-and-global-convergence-in-a-fix--46dbd0563009 (indexed scientific statement compared).

[4] M. Lawnik, L. Moysis, M. S. Baptista, C. Volos, “Discrete one-dimensional piecewise chaotic systems without fixed points,” *Nonlinear Dynamics* **112** (2024), 6679–6693, doi:10.1007/s11071-024-09349-6 (publisher and university abstracts inspected).
