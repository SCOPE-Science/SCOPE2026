# The two-defect tree parity automaton is a reversible path wave after transients

## Finding

**Theorem.** Let \(G\) be any finite simple tree with exactly two even-degree vertices \(a\) and \(b\). Set \(d=\operatorname{dist}_G(a,b)\geq1\), \(m=d+1\), and \(N=|V(G)|\). Fix any finite field \(\mathbb F_q\), where \(q=2^f\) and \(f\geq1\). Let the synchronous parity update be \(F:\mathbb F_q^{V(G)}\to\mathbb F_q^{V(G)}\),
\[
(Fu)_v=\sum_{w\sim v}u_w.
\]
Write \(Q_m(X)=1+X+\cdots+X^m\). Then \(N\geq2m\), the characteristic polynomial of \(F\) is
\[
\chi_F(X)=X^{N-2m}Q_m(X)^2,
\]
and the invariant nonnilpotent (invertible-primary) part of \(F\) is similar over \(\mathbb F_q\) to the reversible second-order path wave
\[
T_m(u,v)=(B_mu+v,u),\qquad B_m=A(P_m),\quad (u,v)\in\mathbb F_q^{m}\oplus\mathbb F_q^{m}.
\]
More precisely its module is cyclic, isomorphic to \(\mathbb F_q[X]/(Q_m(X)^2)\). Every state is eventually periodic; there are exactly \(q^{2m}\) states already periodic at time zero, and the exact global eventual period is \(2(m+1)=2(d+2)\), attained by some state.

For every positive integer \(t\), define
\[
D_m(t)=\deg\gcd_{\mathbb F_2[X]}\bigl(Q_m(X)^2,X^t+1\bigr).
\]
Then the number of states fixed by \(F^t\) is exactly \(q^{D_m(t)}\). Equivalently, if \(m+1=2^\alpha u\), \(t=2^\beta v\) with \(u,v\) odd and \(g=\gcd(u,v)\), then
\[
D_m(t)=(g-1)\min(2^{\alpha+1},2^\beta)+\min(2^{\alpha+1}-2,2^\beta).
\]
The number of initially primitive-period-\(t\) configurations is \(\sum_{s\mid t}\mu(t/s)q^{D_m(s)}\), and the number of distinct primitive \(t\)-cycles is this sum divided by \(t\). These counts are zero unless \(t\mid2(m+1)\). Thus every periodic-point and orbit count is independent of the sizes and shapes of all branches away from the unique \(a\)-to-\(b\) path.

## Assumptions and scope

The graph is a finite connected **simple tree**; the two vertices of even degree are distinct and are the only such vertices. Degrees and distances refer to the original unweighted tree. The local update has no self-interaction, and all arithmetic is in characteristic two. The theorem concerns initially periodic configurations and global eventual periods, not the exact entry time of an arbitrary nonperiodic state. The result is false without the two-defect parity hypothesis in this form. Every tree satisfying the hypothesis has at least four vertices and an even number of vertices.

For orientation, when \(d=1\), the reversible component has dimension four and order six; when \(d=2\), it has dimension six and order eight. The number of transient degrees of freedom is \(N-2(d+1)\), which can grow arbitrarily with branch size while the eventual clock stays fixed.

## Proof

**1. Rooted branch identity.** Work first over \(\mathbb F_2(X)\). A rooted tree \(H\) is called even-offspring if every vertex has an even number of children. Let \(K_H=XI-A(H)\), and \(e\) be its root coordinate vector. We claim
\[
\det K_H=X^{|V(H)|},\qquad e^{\mathsf T}K_H^{-1}e=X^{-1}.
\]
The one-vertex case is immediate. Remove the root to obtain even-offspring child subtrees \(H_j\). By induction each \(K_{H_j}\) is invertible and has root diagonal inverse entry \(1/X\). The Schur complement of their direct sum at the root is \(X-\sum_j X^{-1}=X\), since there are evenly many children. Its determinant is \(X\prod_j X^{|H_j|}\), and its inverse root entry is \(1/X\). This proves the claim. It also shows that every off-path branch matrix is invertible over \(R=\mathbb F_2[X,X^{-1}]\), since its determinant is a power of \(X\).

**2. Eliminate the branches.** Label the unique path from \(a\) to \(b\) as \(v_1,\ldots,v_m\). Each component off that path, rooted at its neighbor of the path, is even-offspring: at its root and at every subsequent vertex, the number of children is its original odd degree minus one. Every path vertex has an **odd** number of off-path neighbors: the endpoints have even total degree minus one path edge, and internal path vertices have odd total degree minus two path edges. Schur-eliminating all the off-path components therefore replaces the diagonal entry \(X\) at every path vertex by \(X-\text{(odd)}X^{-1}=X+X^{-1}\). The spine retains its adjacent off-diagonal entries, so over \(R\) the presentation matrix \(XI-A(G)\) is equivalent to identity blocks and
\[
S_m=(X+X^{-1})I_m+A(P_m).
\]
Multiplying its rows by the unit \(X\) gives \(H_m=(X^2+1)I_m+XA(P_m)\). The determinant calculation also holds in \(\mathbb F_2(X)\):
\[
\det(XI-A(G))=X^{N-m}\det S_m=X^{N-2m}\det H_m.
\]
Each path vertex has at least one off-path neighbor, so \(N\geq2m\).

**3. Polynomial and module.** Let \(h_j=\det((X^2+1)I_j+XA(P_j))\). Tridiagonal expansion gives \(h_0=1\), \(h_1=X^2+1\), and \(h_j=(X^2+1)h_{j-1}+X^2h_{j-2}\). Induction yields \(h_j=1+X^2+\cdots+X^{2j}=Q_j(X)^2\). This proves the characteristic-polynomial formula.

The Schur reductions are invertible over \(R\), so they identify the nonzero-primary part of the \(\mathbb F_2[X]\)-module \(\operatorname{coker}(XI-A(G))\) with \(\operatorname{coker}H_m\). The latter has no \(X\)-torsion because \(\det H_m=Q_m^2\) has constant term one. Over \(R\), the relations \((X^2+1)e_i+Xe_{i-1}+Xe_{i+1}=0\), with zero boundary generators, express every generator in terms of the first because \(X\) is a unit. In this finite module \(X^{-1}\) is a polynomial in \(X\), so the module is cyclic already over \(\mathbb F_2[X]\). Its monic annihilator must be \(\det H_m=Q_m^2\) by its dimension. Extending scalars to \(\mathbb F_q\) leaves this description unchanged.

The path-wave presentation \(XI-T_m\), with \(T_m(u,v)=(B_mu+v,u)\), eliminates one block of generators using a unit coefficient and leaves exactly the relations \(H_m e=0\). Hence its \(\mathbb F_q[X]\)-module is also \(\operatorname{coker}H_m\). The invertible-primary component of \(F\) and \(T_m\) are similar.

**4. Period and fixed spaces.** The characteristic polynomial factors into coprime \(X\)-primary and \(Q_m\)-primary factors. The first contributes no periodic states except zero. The second is a \(2m\)-dimensional invertible module, so there are exactly \(q^{2m}\) periodic states and every other state eventually enters it.

Since \((X+1)Q_m=X^{m+1}+1\), the polynomial \(Q_m^2\) divides \(X^{2(m+1)}+1\); the order divides \(2(m+1)\). It cannot be smaller: the minimal annihilator \(Q_m^2\) has degree \(2m\), so any candidate \(X^t+1\) has \(t\geq2m\); for \(m\geq2\), neither \(X^{2m}+1\) nor \(X^{2m+1}+1\) is divisible by \(Q_m^2=1+X^2+\cdots+X^{2m}\) (the only possible quotients have degrees zero and one, respectively, and their coefficients disagree). Hence the exact order is \(2m+2\).

On \(\mathbb F_q[X]/(Q_m^2)\), the fixed space of the \(t\)-th iterate is the kernel of multiplication by \(X^t+1\), of dimension \(\deg\gcd(Q_m^2,X^t+1)\). For the displayed valuation formula, write \(m+1=2^\alpha u\) and \(t=2^\beta v\) with odd \(u,v\). The root-one factor has multiplicities \(2^{\alpha+1}-2\) in \(Q_m^2\) and \(2^\beta\) in \(X^t+1\), while the other common factors have total squarefree degree \(\gcd(u,v)-1\) and multiplicities \(2^{\alpha+1}\) and \(2^\beta\). The minimum multiplicities yield the formula. Finally Möbius inversion gives primitive-period populations and division by the period gives orbit counts.

## Verification

The standalone standard-library programs `verify/matching_check.py` and `verify/dynamics_check.py` provide independent finite checks. The first exhaustively examines all labelled Prüfer trees with exactly two even-degree vertices at orders four, six, and eight, using a matching-polynomial recursion independent of the matrix-module proof. It checked respectively \(12\), \(840\), and \(101696\) such trees, with exact characteristic-polynomial agreement. The second uses independent binary matrix multiplication, ranks, and direct orbit enumeration on \(96\) constructed/random two-defect trees of orders up to \(22\), including \(5440\) directly iterated binary initial states, and checks eventual-space dimensions and fixed-point counts against the theorem. Both programs completed successfully from the package paths.

To reproduce: execute `python verify/matching_check.py` and `python verify/dynamics_check.py` from the directory containing `RESULT.md`; both use the Python standard library only. Finite enumerations verify instances; the proof above establishes the infinite family.

## Relationship to prior work

Jacobs, Machado and Trevisan (2005) give a general algorithm for computing characteristic polynomials of trees; its determinant-elimination mechanism is relevant, but no uniform two-even-vertex wave reduction or period census is stated in the inspected paper. Macfarlane (2004) studies reversible one-dimensional second-order cellular automata and matrix equivalents; his published abstract supports the wave context, but its full text was not accessible for comparison. Akın's arXiv study of linear cellular automata on regular Cayley trees (first posted 2012, inspected in its later revision) concerns different uniform tree rules and reversibility/entropy, not this irregular two-defect periodic-state classification. A pre-existing result for trees with *one* even-degree vertex gives pure nilpotency; a separate path-wave result determines wave clocks. Neither individually provides the present tree-to-wave conjugacy, and it is not obtained by simply replacing one degree defect with two.

## Limitations

The theorem does not determine the individual transient entry-time distribution, nor assert any result for three or more even-degree vertices, for graphs with cycles, or for odd characteristic. Independent mathematical review has not been performed. Priority remains subject to any unindexed earlier derivation of the same characteristic-two two-defect reduction; full text for Macfarlane (2004) was unavailable, so its detailed coverage remains an access risk. No assertion of worldwide novelty follows solely from unsuccessful searches.

## References

1. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A: Mathematical and General **37** (2004), 10791–10814, published 2004-10-28, DOI: 10.1088/0305-4470/37/45/006.
2. D. P. Jacobs, C. M. S. Machado and V. Trevisan, *An \(O(n^2)\) algorithm for the characteristic polynomial of a tree*, Journal of Combinatorial Mathematics and Combinatorial Computing **54** (2005), 213–221. Public publisher record dated 2005-08-31: https://combinatorialpress.com/jcmcc-articles/volume-054/an-on2-algorithm-for-the-characteristic-polynomial-of-a-tree/ .
3. H. Akın, *The entropy and reversibility of cellular automata on Cayley tree*, arXiv:1211.7362 (first publicly submitted 2012; later revision inspected), https://arxiv.org/abs/1211.7362 .
