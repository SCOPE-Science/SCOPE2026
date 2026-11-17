# Dihedral characters and mod-twenty quotient cohomology of three-independence cycle complexes

## Finding
For every integer \(n\ge12\), let \(K_n\) be the simplicial complex of subsets of \(\mathbb Z/n\mathbb Z\) containing **no four cyclically consecutive vertices**. Equivalently, \(K_n=\operatorname{Ind}_3(C_n)=D(C_n;P_4)\). Let \(r(i)=i+1\), \(s(i)=-i\), and \(D_n=\langle r,s\rangle\), of order \(2n\). The classical nonequivariant homotopy classification gives precisely one nonzero reduced rational homology group, in degree \(q(n)\), of rank \(4\) when \(5\mid n\) and rank \(1\) otherwise. Write \(n=5t+u\), \(0\le u\le4\), and set
\[
q(n)=\begin{cases}3t-1,&u=0,1,\\3t+u-2,&u=2,3,4.\end{cases}
\]
The **complete character** \(\chi_n\) of \(D_n\) on \(\widetilde H_{q(n)}(K_n;\mathbb Q)\) is as follows. For every integer \(a\), with \(d=\gcd(n,a)\),
\[
\boxed{\chi_n(r^a)=(-1)^{q(n)+d}\bigl(1-5\mathbf1_{5\mid d}\bigr).}
\]
Define the integer \(W(n,a)\) on reflections by the following base values and recurrences:

* For odd \(n\), \(W(11,0),W(13,0),W(15,0),W(17,0),W(19,0)=(-1,1,0,-1,1)\); its value is independent of \(a\), and \(W(n+10,a)=-W(n,a)\).
* For even \(n\), \(W(12,0),W(14,0),W(16,0),W(18,0),W(20,0)=(1,-1,-1,1,0)\); \(W(n,a)=(-1)^aW(n,0)\), and \(W(n+10,a)=-W(n,a)\).

Then for every \(a\),
\[
\boxed{\chi_n(r^as)=(-1)^{q(n)+1}W(n,a).}
\]
As a consequence, the **ordinary geometric quotient** has positive-degree rational cohomology precisely in four residue classes:
\[
\boxed{\widetilde H^j(|K_n|/D_n;\mathbb Q)\cong
\begin{cases}\mathbb Q,&j=q(n)\text{ and }n\equiv1,7,13,19\pmod{20},\\0,&\text{otherwise}.\end{cases}}
\]
There is no claim of a homotopy equivalence between these quotient spaces and spheres; the statement concerns rational additive cohomology only.

## Assumptions and scope
The cycle is simple, \(n\ge12\); all group actions are the indicated simplicial actions; homology is reduced, with rational coefficients for characters and rational cohomology for quotient statements. The topological group quotient is the quotient of the **geometric realization**, not the abstract orbit-vertex quotient without admissible subdivision. The theorem applies to all integer powers of rotations and reflections, including the identity. The homotopy ranks and degrees are previously known from Taylan and Deshpande–Singh; they are used, not newly asserted.

## Proof
**1. Homology concentration.** The known matching-tree computation of the cycle complex avoiding \(P_4\) provides \(K_n\simeq\bigvee^4S^{3t-1}\) when \(n=5t\), and a single sphere of dimension \(q(n)\) for the other four residues. Hence the character is determined by the reduced homological Lefschetz number: \(\widetilde L(g)=(-1)^{q(n)}\chi_n(g)\).

**2. Orbit-face sign identity.** For any permutation \(g\) preserving a finite simplicial complex, the trace on an oriented face fixed setwise is the sign of its restricted vertex permutation. If the face comprises \(h\) complete \(g\)-orbits, its contribution to the reduced alternating trace, including the empty face in degree \(-1\), is \((-1)^{h-1}\). Thus
\[
\widetilde L(g)=-\sum_{J\subseteq\mathcal O_g\,\text{admissible}}(-1)^{|J|},
\]
where \(\mathcal O_g\) denotes vertex orbits and admissibility means that the union of the selected orbits is a face of \(K_n\). This is the reduced Euler characteristic of the geometric fixed space, but the identity here follows directly from signed simplicial traces.

**3. Rotations.** If \(g=r^a\), its orbits are the residue classes modulo \(d=\gcd(n,a)\). Invariant admissible faces correspond exactly to cyclic binary words of period \(d\) that avoid four successive ones in their infinite periodic repetition. Introduce the weighted automaton with four states, indexed by the terminal run length \(0,1,2,3\) of ones, and transfer matrix (columns are preceding states)
\[
T=\begin{pmatrix}1&1&1&1\\-1&0&0&0\\0&-1&0&0\\0&0&-1&0\end{pmatrix}.
\]
Writing a zero has weight \(+1\); writing a one has weight \(-1\). Periodic state walks are in bijection with admissible cyclic words, including at periods \(d=1,2,3\), because a permitted periodic word contains a zero and hence has a uniquely determined terminal run. Therefore the signed orbit sum is \(\operatorname{tr}(T^d)\). Direct multiplication, or the characteristic polynomial \((x^5+1)/(x+1)\), gives \(T^5=-I\), and its four distinct eigenvalues are \(-\zeta_5^j\), \(j=1,2,3,4\). Consequently
\[
\widetilde L(r^a)=-\operatorname{tr}(T^d)=(-1)^d\bigl(1-5\mathbf1_{5\mid d}\bigr),
\]
which proves the rotation character.

**4. Reflections and endpoint conditions.** For \(g=r^as\), orbits fold the circle into a line. The selected orbit positions form a binary string with no internal four-run, subject to special boundary conditions. An odd cycle has one vertex axis and one edge axis: with \(m=(n-1)/2\), the string has length \(m+1\), cannot have its first three entries all one, and cannot have its last two all one. An even cycle with \(a\) even has two vertex axes: its string has length \(n/2+1\) and forbids the first three and last three entries all one. An even cycle with \(a\) odd has two edge axes: its string has length \(n/2\) and forbids the first two and last two entries all one. These conditions follow by expanding the reflected word around its two symmetry axes; \(n\ge12\) avoids boundary overlaps.

Let \(F(L;\ell,h)\) denote the signed sum \(\sum(-1)^{\#\text{ones}}\) over length-\(L\) binary strings that avoid four successive ones, an all-one prefix of length \(\ell\), and an all-one suffix of length \(h\). Then the three cases above yield
\[
W(n,a)=\begin{cases}
 F((n+1)/2;3,2),&n\text{ odd},\\
 F(n/2+1;3,3),&n\text{ even},\ a\text{ even},\\
 F(n/2;2,2),&n\text{ even},\ a\text{ odd}.
\end{cases}
\]
To compute \(F\), process its prefix restriction, then apply \(T\) for each further digit, and finish by summing states with terminal run shorter than \(h\). The explicit identity \(T^5=-I\) proves \(F(L+5;\ell,h)=-F(L;\ell,h)\). Direct enumeration of the finitely many base strings gives the two lists of seeds stated above; the two even reflection-axis types have opposite signed sums for the five initial values and hence forever. The orbit-face identity yields \(\widetilde L(r^as)=-W(n,a)\), giving the reflection character with the stated sign.

**5. Quotient invariant classes.** The average of the homology character over \(D_n\) is the dimension of the fixed vector space. From the rotation formula,
\[
\sum_{a=0}^{n-1}\widetilde L(r^a)=\sum_{a=0}^{n-1}(-1)^{\gcd(n,a)}\bigl(1-5\mathbf1_{5\mid\gcd(n,a)}\bigr).
\]
For even \(n\), each parity sum cancels; for odd \(n\) it equals \(-n\) if \(5\nmid n\) and zero if \(5\mid n\). Even-cycle reflections also sum to zero, since their two axis types have opposite values. Odd-cycle reflections contribute \(-nW(n,0)\). For odd \(n\) not divisible by five, \(q(n)\) is odd, so averaging the actual character gives \((1+W(n,0))/2\). The reflection seeds show that this is one exactly at residues \(1,7,13,19\pmod{20}\). All other cases give zero. Rational cohomology of a geometric quotient by a finite group equals invariant rational cohomology after barycentric subdivision (averaging is exact in characteristic zero). This proves the quotient formula.

## Verification
The standalone script `verify_character.py`, using only the Python standard library, checks \(T^5=-I\), the reflection endpoint recurrence and quotient invariants for every \(12\le n\le150\), and independently enumerates all admissible oriented simplices for every \(12\le n\le17\). It computes signed Lefschetz traces directly for all \(174\) group elements in those six dihedral groups, rather than using the orbit transfer formula for that last check. Its exact output is embedded in `verification_output.txt`. These finite checks corroborate the symbolic proof but do not replace its all-\(n\) argument.

## Relationship to prior work
Taylan (2015, Theorem 5.2) established the nonequivariant sphere-wedge type of the path-devoid cycle complex. Deshpande and Singh (2020, Theorem 4.6) independently compute the corresponding higher-independence cycle homotopy types. Neither result gives action-by-action rational homology characters or ordinary dihedral quotient cohomology. Previously indexed equivariant classifications for the complexes avoiding *three* consecutive cycle vertices concern a different parameter: those have a four-periodic rank anomaly and mod-eight quotient behavior, unlike the five-periodic rank anomaly and mod-twenty quotient behavior established here. Constructions with tight three-uniform cyclic noncover complexes are likewise not the Alexander dual of the present four-run-forbidden complex. The original and alternate names and their Alexander-dual comparison were specifically considered for overlap.

## Limitations
This theorem calculates rational representations and additive rational cohomology of quotient spaces; it does not determine integral representation lattices, torsion in the quotients, their homotopy types, or the full fixed-space homotopy classification. The literature comparison is best-effort and cannot exclude an equivalent statement in inaccessible or unindexed sources. Independent mathematical review has not been performed.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first posted 2015-01-27, Theorem 5.2, especially pp. 2 and 14–16. https://arxiv.org/abs/1501.06754
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15, Section 4 and Theorem 4.6. https://arxiv.org/abs/2001.05448
