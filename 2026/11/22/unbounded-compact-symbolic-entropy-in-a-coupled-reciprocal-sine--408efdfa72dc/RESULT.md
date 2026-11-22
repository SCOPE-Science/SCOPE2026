# Unbounded compact symbolic entropy in a coupled reciprocal-sine map

## Finding
For each fixed \(a>0\), \(b>0\), and each integer \(N\geq2\), the map
\[
F_{a,b}(x,y)=\bigl(\sin^2(a\pi/x+by),\,\sin^2(b\pi y+ax)\bigr)
\]
on the nonsingular phase domain \((0,1]\times[0,1]\) possesses a nonempty compact forward-invariant set \(K_N\) on which \(F_{a,b}\) is continuous, and a continuous onto coding \(\Pi_N:K_N\to\{1,\ldots,N\}^{\mathbb N_0}\) satisfying \(\Pi_N\circ F_{a,b}=\sigma\circ\Pi_N\), where \(\sigma\) is the left shift. Consequently,
\[
h_{\rm top}(F_{a,b}|_{K_N})\geq\log N,
\]
and for every integer \(p\geq1\), \(F_{a,b}^p\) has at least \(N^p\) distinct fixed points on \(K_N\).
In particular, the supremum of entropy among compact invariant subsystems of this singular map is infinite, for every positive pair \((a,b)\).

## Assumptions and scope
All trigonometric functions use radians. Define \(G(x,y)=\sin^2(b\pi y+ax)\). The theorem concerns exact real arithmetic and only compact subsystems bounded away from the singular line \(x=0\). It does not assign topological entropy to a globally continuous map on a compact full state square, since the formula is singular at \(x=0\). A topological factor is asserted, not a global conjugacy or a two-sided Smale horseshoe.

Choose a sufficiently small \(v\in(0,1/2)\) and set \(u=v/2\) and \(h=4(a+1)^2v^2\). Take \(v\) so small that
\[
h<1,\quad bh<\pi/4,\quad av+b\pi h\leq(a+1)v,
\]
and
\[
q_v=\max\left\{\frac{v^2}{2a\pi\sqrt{u(1-v)}}+\frac{bv^2}{a\pi},\quad
2(a+b\pi)(av+b\pi h)\right\}<\tfrac13.
\]
These inequalities hold eventually as \(v\downarrow0\). The rectangle \(R_v=[u,v]\times[0,h]\) is a compact subset of the map's domain.

## Proof
**1. Inverse branches and quantitative count.** The positive integers
\[
\mathcal I_v=\{k\in\mathbb N:a/v+1<k<2a/v-1\}
\]
number at least \(\lfloor a/v\rfloor-3\), which becomes arbitrarily large as \(v\downarrow0\). For every \(k\in\mathcal I_v\), \(w\in[u,v]\), and \(y\in[0,h]\), put
\[
\psi_k(w,y)=\frac{a\pi}{k\pi+\arcsin\sqrt w-by}.
\]
Since \(0<\arcsin\sqrt w<\pi/2\) and \(bh<\pi/4\), the denominator lies strictly between \(a\pi/v\) and \(2a\pi/v\); thus \(u<\psi_k(w,y)<v\). The first component of \(F_{a,b}(\psi_k(w,y),y)\) equals \(w\) exactly. All branch-image intervals \(J_k=\psi_k([u,v]\times[0,h])\) are compact and mutually disjoint: the phase ranges of successive indices are separated by \(\pi\), while each range has width strictly below \(\pi\). The derivative bounds are
\[
|\partial_w\psi_k|\leq\frac{v^2}{2a\pi\sqrt{u(1-v)}},
\qquad |\partial_y\psi_k|\leq\frac{bv^2}{a\pi}.
\]
Furthermore \(0\leq G(x,y)\leq(av+b\pi h)^2\leq h/4\), and
\[
|\partial_xG|+|\partial_yG|\leq2(a+b\pi)(av+b\pi h).
\]
Thus each inverse branch and the transverse update have uniform maximum-row-sum Lipschitz bound \(q_v<1/3\) on \(R_v\).

**2. Arbitrary one-sided itinerary.** Pick any \(N\) distinct indices \(k_1,\ldots,k_N\) from \(\mathcal I_v\). Fix a code \(s=(s_0,s_1,\ldots)\in\{1,\ldots,N\}^{\mathbb N_0}\) and an initial transverse value \(\eta\in[0,h]\). On the complete metric space \(R_v^{\mathbb N_0}\) with the sup norm, define the operator \(T_{s,\eta}\) by
\[
(T_{s,\eta}z)^x_n=\psi_{k_{s_n}}(x_{n+1},y_n),\quad
(T_{s,\eta}z)^y_0=\eta,\quad
(T_{s,\eta}z)^y_{n+1}=G(x_n,y_n).
\]
It maps the space into itself and is a contraction with constant at most \(q_v\). Its unique fixed point \(z(s,\eta)=((x_n,y_n))_{n\geq0}\) is a genuine forward orbit of \(F_{a,b}\) because \(\sin^2(k\pi+\arcsin\sqrt{x_{n+1}})=x_{n+1}\). Moreover \(x_n\in J_{k_{s_n}}\).

**3. Compact coding subsystem.** The initial-state map \(P(s,\eta)=(x_0(s,\eta),\eta)\) is continuous. Indeed, fixed-point iteration beginning with a constant seed has a uniform error at most \(q_v^m\operatorname{diam}(R_v)/(1-q_v)\) after \(m\) steps; its coordinate-zero output depends only on finitely many initial code symbols and continuously on \(\eta\). Hence \(K_N=P(\{1,\ldots,N\}^{\mathbb N_0}\times[0,h])\) is nonempty and compact. Shifting the fixed-point orbit shows \(F_{a,b}(P(s,\eta))=P(\sigma s,G(x_0(s,\eta),\eta))\), so \(F_{a,b}(K_N)\subset K_N\). Since the disjoint intervals \(J_{k_j}\) identify the itinerary uniquely, \(\Pi_N(P(s,\eta))=s\) defines a continuous surjection onto the full shift. The standard entropy inequality under continuous factors gives \(h_{\rm top}(F_{a,b}|_{K_N})\geq\log N\).

**4. Periodic points.** Fix a word of length \(p\) and repeat it to form \(s=\sigma^p s\). The map \(\eta\mapsto y_p(s,\eta)\) is continuous from \([0,h]\) into itself and therefore has a fixed point. At that fixed value, the state after \(p\) steps has the same initial code and initial transverse coordinate. Uniqueness of the coded orbit implies \(F_{a,b}^p(P(s,\eta))=P(s,\eta)\). The \(N^p\) distinct length-\(p\) words give distinct such states because their itineraries differ. Finally \(\lfloor a/v\rfloor-3\to\infty\), proving the unbounded compact-subsystem entropy assertion.

## Verification
The accompanying `check.py` implements high-precision phase-inverse identities, branch separation, derivative upper bounds, and finite segments of the coded-orbit contraction for two concrete positive parameter pairs. Run `python check.py` with `mpmath` installed. It reproduces diagnostics but is **not** a proof of the statements for arbitrary parameters or all one-sided sequences. The infinite-code and unbounded-entropy statements follow from the complete analytic contraction and compact-factor argument above.

## Relationship to prior work
Zhu, Deng, Zhang and Zhu introduced this exact coupled reciprocal-sine map and investigated numerical Lyapunov exponents, bifurcation diagrams and empirical entropy measures. Their published paper does not give a compact full-shift factor for arbitrary symbol cardinality. A separately published mathematical note establishes two saddles in each sufficiently high reciprocal phase band, but isolated fixed-point proliferation does not imply a full-shift factor or positive entropy. An earlier exact inverse-sheet count for the same map establishes targetwise inverse multiplicity and asymptotic inverse-coordinate statistics, not recurrent orbit coding. Standard results on contraction fixed points, symbolic factors and entropy are used as established tools, not claimed new.

## Limitations
No assertion is made about a natural invariant measure, a physical attractor, encryption strength, finite-precision implementation, full-space entropy, or the status of trajectories reaching \(x=0\). The entropy bound is for separately constructed compact subsystems, and does not claim that one single compact subsystem has infinite entropy. Priority against unindexed mathematically equivalent literature remains a risk.

## References
1. S. Zhu, X. Deng, W. Zhang and C. Zhu, *Construction of a New 2D Hyperchaotic Map with Application in Efficient Pseudo-Random Number Generator Design and Color Image Encryption*, Mathematics **11** (2023), 3171, first public date 2023-07-19, https://doi.org/10.3390/math11143171.
2. *Two fixed-point saddles per reciprocal phase band in a coupled sine-square map*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-fixed-point-saddles-per-reciprocal-phase-band-in-a-coupled-s--99bf14d32624.
3. Banach contraction theorem and the factor monotonicity theorem for topological entropy, classical results.
