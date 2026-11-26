# The signed five-point dihedral character of generalized Petersen independence complexes

## Finding
For every integer \(q\ge1\) let \(n=5q\), and let \(G_n=\operatorname{GP}(n,2)\) have vertices \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_iu_{i+1}\), \(v_iv_{i+2}\), and \(u_iv_i\). Its independence complex \(X_n=\operatorname{Ind}(G_n)\) carries the natural dihedral action of \(D_n=\langle r,f\mid r^n=f^2=1, frf=r^{-1}\rangle\) by \(r(u_i)=u_{i+1}\), \(r(v_i)=v_{i+1}\), \(f(u_i)=u_{-i}\), and \(f(v_i)=v_{-i}\).

The only nonzero reduced rational homology is \(\widetilde H_{3q-1}(X_n;\mathbb Q)\cong\mathbb Q^4\), and its **complete rational dihedral character** is
\[
\operatorname{tr}(r^s)=(-1)^{(n+1)s}\begin{cases}4,&5\mid s,\\-1,&5\nmid s,\end{cases}
\qquad
\operatorname{tr}(r^sf)=0\quad(0\le s<n).
\]
Equivalently, with \(U_5=\ker(\mathbb Q^5\xrightarrow{\mathrm{sum}}\mathbb Q)\) for the natural action of \(D_5\) on five vertices and with \(\varepsilon_n(r)=(-1)^{n+1}\), \(\varepsilon_n(f)=1\), one has
\[
\widetilde H_{3q-1}(X_n;\mathbb Q)\cong\varepsilon_n\otimes \operatorname{Inf}_{D_5}^{D_n}U_5.
\]
Consequently the fixed subspace under rotations, and hence under all of \(D_n\), is zero; the geometric quotient \(|X_n|/D_n\) has no positive-degree rational homology.

## Assumptions and scope
Indices are reduced modulo \(n\), graphs are finite simple graphs, \(n\ge5\) is divisible by five, and \(\operatorname{Ind}(G)\) is the abstract simplicial complex of all independent vertex subsets. The action is on the actual geometric realization, not on an ordered-word model. Rational homology is taken with ordinary \(\mathbb Q\) coefficients. The homotopy classification \(X_{5q}\simeq\bigvee^4S^{3q-1}\) is a previously published input (Kim, 2026), not claimed here as new. Some small cases, especially \(n=10\), have independently known stronger automorphism representations; the finding is the **uniform dihedral family**, not individual small-case priority.

## Proof
**1. Lefschetz evaluation by independent orbit sets.** Let \(g\) be any graph automorphism of a finite graph \(G\). Its cycles on vertices are denoted \(\mathcal O(g)\). Delete any cycle that contains the two endpoints of a graph edge. On the remaining cycles create an edge when any original edge joins their vertices, obtaining the simple orbit-compatibility graph \(Q_g\). A \(g\)-invariant independent set is precisely a union of cycles corresponding to an independent set of \(Q_g\). If that union contains \(j\) cycles and \(m\) original vertices, its simplicial orientation permutation has sign \((-1)^{m-j}\) and the reduced chain trace weight is \((-1)^{m-1}(-1)^{m-j}=(-1)^{j-1}\). The empty simplex in degree minus one contributes \(-1\). Thus, writing \(I_H(z)=\sum_{S\text{ independent in }H}z^{|S|}\), the reduced Lefschetz number is exactly
\[
\widetilde L(g)= -I_{Q_g}(-1).
\]
This is an integral combinatorial identity; no assumption about free group actions is made.

**2. Rotation orbit graph.** For \(g=r^s\), let \(d=\gcd(n,s)\), with \(\gcd(n,0)=n\). The rotation cycles are the two index layers modulo \(d\). When \(d\ge5\), the graph \(Q_g\) is exactly \(\operatorname{GP}(d,2)\). When \(d=1\) both cycles are forbidden and \(Q_g\) is empty, hence \(I_{Q_g}(-1)=1\). When \(d=2\), both inner-layer cycles are forbidden by length-two inner edges, and the remaining graph is a single outer edge, hence \(I_{Q_g}(-1)=-1\). When \(d=3\), \(Q_g\) is the triangular prism, whose independence polynomial is \(1+6z+6z^2\), giving value \(1\). When \(d=4\), direct enumeration gives \(I_{Q_g}(-1)=-1\); these four boundary cases are also reproduced by the checker.

**3. Input homotopy formula and all rotation traces.** Kim's Theorem 4.6 states, for \(d\ge5\), that \(\operatorname{Ind}(\operatorname{GP}(5a,2))\simeq\bigvee^4 S^{3a-1}\) and \(\operatorname{Ind}(\operatorname{GP}(5a+b,2))\simeq S^{3a+b-2}\) for \(1\le b\le4\), including the initial cases \(d=6,7,8,9\). Taking reduced Euler characteristics gives, uniformly for all \(d\ge1\) by Step 2,
\[
I_{Q_{r^s}}(-1)=F(d)=\begin{cases}4(-1)^{d/5},&5\mid d,\\(-1)^{d+1},&5\nmid d.\end{cases}
\]
Because all reduced homology of \(X_n\) lies in dimension \(3q-1\), the Lefschetz formula gives \(\operatorname{tr}(r^s)=(-1)^q F(\gcd(n,s))\). If \(n\) is odd, both \(q\) and every divisor \(d\mid n\) are odd, producing trace four at \(5\mid s\) and minus one otherwise. If \(n\) is even, then \(q\) is even, \(\gcd(n,s)\) has the same parity as \(s\), and when \(5\mid s\) the integer \(\gcd(n,s)/5\) has the same parity as \(s\). The trace formula in the statement follows.

**4. Every reflection has trace zero.** The rotation character just obtained agrees with that of \(\varepsilon_n\otimes\operatorname{Inf}_{D_5}^{D_n}U_5\); over \(\mathbb C\), rotation has four distinct eigenvalues \(\varepsilon_n(r)\zeta_5^j\) for \(j=1,2,3,4\). Any reflection \(t\) conjugates \(r\) to its inverse, so \(t\) interchanges each rotation eigenspace with its inverse-eigenvalue eigenspace. None of these four eigenvalues equals its inverse: \(\zeta_5^{2j}\ne1\) for \(j=1,2,3,4\). Hence \(\operatorname{tr}(r^sf)=0\). The complex character of the homology therefore agrees on all elements of \(D_n\) with the proposed signed inflated augmentation representation. Semisimplicity of rational finite-group representations identifies them over \(\mathbb Q\).

**5. Rational quotient.** The four rotation eigenvalues contain no \(1\), so the invariant positive-degree rational homology vanishes. For a finite cellular group action, rational homology of the ordinary orbit space is naturally the invariants of rational homology of the original space (use an equivariant simplicial subdivision and rational orbit chains). Since the complex is connected, the quotient is connected and rationally acyclic in positive degrees.

## Verification
Run `python check_gp_dihedral.py` with Python 3.10 or later, using only the standard library. It independently constructs each automorphism-orbit compatibility graph and computes \(I_{Q_g}(-1)\) by a memoized exact deletion recurrence. For \(n=5,10,15,20\) and all \(n\) rotations plus \(n\) reflections, it checks 100 exact trace identities. It also checks the small-divisor boundary cases encountered by rotations. These finite checks corroborate, but do not substitute for, the all-parameter orbit and representation proof.

## Relationship to prior work
Agarwal and Basak (first public 2026-08-31) studied homotopy types of independence complexes for a different symmetric cubic graph family (Möbius ladders), motivating topological classification across symmetric families. Kim (first public 2026-11-17) later computed the non-equivariant homotopy types of the generalized Petersen family \(\operatorname{GP}(n,2)\), including the four-sphere wedge on multiples of five. Neither inspected paper determines the uniform \(D_{5q}\) rational homology character, the sign transition at even \(n\), or the rational homology of every dihedral orbit space. Previously indexed special cases at \(n=10\) have fuller symmetry classifications and are not claimed as first results. No absolute publication-priority claim follows from a finite search.

## Limitations
The result is a rational representation theorem for the standard dihedral subgroup; it does not determine the integral homology lattice as a \(\mathbb Z[D_n]\)-module, quotient torsion, geometric fixed-point sets, equivariant homotopy types, or the full graph-automorphism group in exceptional low orders. It relies on the previously published nonequivariant homotopy classification for all \(n\), and its originality assessment has residual risk from inaccessible or unindexed equivalent results. Independent mathematical validation has not been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601, first posted 2026-08-31, https://arxiv.org/abs/2608.30601.
2. Y. Kim, *Perfect matching complexes of antiprism graphs and independence complexes of generalized Petersen graphs GP(n,2)*, arXiv:2611.22021, first posted 2026-11-17, Theorem 4.6, https://arxiv.org/abs/2611.22021.
3. J. A. Barmak, *Star clusters in independence complexes of graphs*, Advances in Mathematics 241 (2013), 33–57, Theorem 4.11 (Petersen base case).
