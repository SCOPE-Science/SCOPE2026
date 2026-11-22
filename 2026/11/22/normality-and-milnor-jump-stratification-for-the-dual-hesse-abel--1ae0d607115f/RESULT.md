# Normality and Milnor-jump stratification for the dual-Hesse abelian nonic

## Finding
Over \(\mathbb C\), put
\[
P=(X^3-Y^3)(Y^3-Z^3)(Z^3-X^3),\qquad B=V(P)\subset\mathbb P^2.
\]
The reduced curve \(B\) is the dual-Hesse arrangement of nine lines, with exactly twelve ordinary triple points. For **every nonzero** homogeneous quadratic \(Q(X,Y,Z)\), let
\[
S_Q=V(W^3Q(X,Y,Z)^3-P(X,Y,Z))\subset\mathbb P^3,
\qquad C=V(Q)_{\mathrm{red}}\subset\mathbb P^2.
\]

**Theorem.** The surface \(S_Q\) is integral and normal if and only if \(Q\) is nonzero at each of the twelve triple points of \(B\). If normal, its singular locus consists of the twelve points \([0:p]\) above the triple points and the vertex \(v=[1:0:0:0]\). Each of the first twelve germs is a simple elliptic cone of type \(\widetilde E_6\) with \((\mu,p_g)=(8,1)\). The vertex has multiplicity \(6\), geometric genus \(45\), and
\[
\boxed{\mu(S_Q,v)=341+3e(C)-3\#(B\cap C)}.
\]
The topological Euler characteristic is \(e(S_Q)=22-3e(C)+3\#(B\cap C)\). In particular, the complete rank-stratification of the vertex Milnor number is:

* For smooth \(C\), let \(r\) be the number of distinct lines of \(B\) tangent to \(C\). Then \(\#(B\cap C)=18-r\), and \(\mu_v=293+3r\).
* For \(Q=L_1L_2\) with distinct lines, the intersection point \(L_1\cap L_2\) lies either outside \(B\), giving \(\mu_v=296\), or in the smooth part of \(B\), giving \(\mu_v=299\).
* For \(Q=L^2\), the reduced conic is one line, and \(\mu_v=320\).

The theorem addresses exactly the normal parameters; if \(Q\) passes through a triple point, \(S_Q\) has a positive-dimensional singular locus. No assertion is made about equianalytic classification of vertex germs.

## Assumptions and scope
The ground field is \(\mathbb C\), and \(Q\ne0\) is any ternary quadratic (possibly singular or nonreduced). The \(\#\) symbol counts distinct geometric points rather than scheme lengths. Topological Euler characteristic is that of the associated complex analytic space. Local Milnor numbers are defined for isolated hypersurface singularities; for parameters outside the normal locus the displayed Milnor numbers are not asserted.

## Proof
**1. The branch arrangement and normality.** Over \(\mathbb C\), \(P\) splits into three pencils, each containing three lines, and the only singularities of \(B\) are their three pencil centers and nine additional triple crossings, all ordinary. Thus \(e(B)=9e(\mathbb P^1)-12(3-1)=18-24=-6\).

Put \(H=W^3Q^3-P\). On \(S_Q\) wherever \(WQ\ne0\), the derivative \(\partial H/\partial W=3W^2Q^3\) is nonzero. When \(WQ=0\), the defining equation forces \(P=0\), and its three spatial derivatives reduce to \(-\nabla P\). The only possible nonvertex singular points therefore project to the twelve triples of \(B\). If \(Q(p)\ne0\), the only point above a triple \(p\) is \([0:p]\), whereas if \(Q(p)=0\), the entire projective line joining \(v\) to \([0:p]\) lies in the singular locus. Conversely, when \(Q\) avoids all triples it shares no component with \(P\) (each of the nine lines passes through a triple). In the function field \(\mathbb C(\mathbb P^2)\), the rational function \(P/Q^3\) is not a cube, because a component of \(B\) has valuation one. Hence \(T^3-P/Q^3\) is irreducible; the projective equation is primitive and defines an integral hypersurface. All its singularities are isolated, so the hypersurface is normal by Serre's \(R_1+S_2\) criterion. If \(Q\) meets a triple, its line of singularities precludes normality. This proves the criterion.

**2. The other twelve germs.** In a local chart centered at a triple \(p\), the unit \(Q\) can be divided out, so the equation is analytically equivalent to \(w^3=\ell_1\ell_2\ell_3\) for three transverse linear branches. It is the affine cone over a smooth plane cubic, a \(\widetilde E_6\) simple elliptic singularity, with local Milnor number \(8\) and geometric genus \(1\).

**3. Euler characteristic by projection.** Project from \(v\) to \(\mathbb P^2\). The morphism \(S_Q\setminus\{v\}\to\mathbb P^2\) has exactly three reduced points over \(\mathbb P^2\setminus(B\cup C)\), one point over \(B\setminus C\), no points over \(C\setminus B\), and an affine-line fiber over each point of \(B\cap C\). Over the open first stratum it is a finite étale cover of degree three, so Euler characteristic multiplies by three. If \(c=e(C)\) and \(t=\#(B\cap C)\), additivity yields
\[
e(S_Q)=1+3(3-e(B)-c+t)+(e(B)-t)+t=22-3c+3t.
\]
Here the initial \(1\) is the removed vertex and \(e(B)=-6\).

**4. Milnor and geometric genera.** Any smooth complex hypersurface of degree nine in \(\mathbb P^3\) has Euler characteristic \(9(9^2-4\cdot9+6)=459\). A small general degree-nine perturbation smooths the thirteen isolated hypersurface singularities; the Euler jump in complex dimension two is the sum of their Milnor numbers. Subtracting the twelve known contributions gives
\[
\mu(S_Q,v)=459-e(S_Q)-12\cdot8=341+3c-3t.
\]
The function-field substitution \(T=WQ\) identifies all these surfaces birationally with the triple cyclic plane \(T^3=P\), which is birational to the abelian surface \(E\times E\) of Chen–Lazarsfeld–Moretti, where \(E:y^2=x^3+1\). Thus the minimal resolution has \(\chi(\mathcal O)=0\). The hypersurface itself has \(\chi(\mathcal O_{S_Q})=1+\binom83=57\). The local geometric genera add to the discrepancy \(57\); the twelve elliptic points contribute \(12\), leaving \(p_g(S_Q,v)=45\). In the vertex chart the lowest homogeneous term is \(Q^3\), of degree six; the other term has degree nine, so its multiplicity is six.

**5. Exhaustion of quadratic ranks.** If \(Q\) has rank three, its smooth conic meets each branch line in two distinct points except for a tangency. Since all triples are excluded, intersection supports on different lines cannot coincide, yielding \(c=2\) and \(t=18-r\). If \(Q\) has rank two, \(C=L_1\cup L_2\) has \(c=3\); each of nine branch lines intersects \(C\) twice, except that the node may lie on one of the lines of \(B\), reducing the support count from \(18\) to \(17\). No more than one branch line can contain that node, because triple points are avoided. If \(Q\) has rank one, \(C=L\), \(c=2\), and the line meets all nine branch lines in distinct points, hence \(t=9\). Substitution proves all cases.

## Verification
A standalone exact-arithmetic script `check_examples.py` verifies that five explicit quadratic parameters avoid all twelve triples, determines their ranks and relevant tangent/node conditions, and checks the claimed Milnor values from the proven formula. The five examples represent smooth transverse, smooth tangent, rank-two node off \(B\), rank-two node on smooth \(B\), and double-line regimes. These computations do not establish the infinite parameter theorem, which is proved above using the Jacobian, Euler, and Milnor identities.

## Relationship to prior work
Nathan Chen, Robert Lazarsfeld, and Federico Moretti, *Some normal abelian surfaces in \(\mathbb P^3\)* (arXiv:2611.09613v1, 6 November 2026), establish the generic normal nonic construction and its abelian birational type. The established cyclic-cover/normality argument applies to generic auxiliary forms; the theorem above treats **every** nonzero quadratic parameter, including degenerate conics and tangency boundaries, and explicitly computes all resulting vertex Milnor jumps. Standard facts used are the Euler characteristic of smooth degree-nine surfaces, the local Milnor smoothing formula, and the simple-elliptic cubic-cone invariant.

## Limitations
The theorem is over \(\mathbb C\), not positive characteristic. It does not determine a full analytic type or minimal resolution graph of the vertex for arbitrary special quadratic parameters, and it assigns no Milnor number to nonisolated singularities outside the normal locus. It does not establish publication priority against inaccessible or unindexed literature. The vertex geometric genus statement uses the birational abelian type established in the cited source; the independence of \(Q\) follows from the substitution \(T=WQ\).

## References
Chen, N.; Lazarsfeld, R.; Moretti, F., *Some normal abelian surfaces in \(\mathbb P^3\)*, arXiv:2611.09613v1 (2026-11-06), https://arxiv.org/abs/2611.09613. See Proposition A and Proposition 1.6, and §1 for the cyclic covering.
