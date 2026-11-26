# Fibonacci Fourier rank of finite Coxeter descent-profile convolution

## Finding
Let \((W,S)\) be a finite irreducible Coxeter system of rank \(r=|S|\ge1\). Put \(d(w)=\mathbf1_{\operatorname{Des}_R(w)}\in\mathbb F_2^S\), where \(\operatorname{Des}_R(w)=\{s\in S:\ell(ws)<\ell(w)\}\). Define the nonnegative integer counting kernel \(f(x)=|\{w:d(w)=x\}|\). Counting convolution \(Tg=f*g\) acts on all complex functions on \(\mathbb F_2^S\), and equally on real functions.

For every \(J\subseteq S\), the unnormalized Walsh multiplier is
\[
\widehat f(J)=\sum_{w\in W}(-1)^{|J\cap\operatorname{Des}_R(w)|}
=\frac{|W|}{|W_J|}P_{W_J}(-1),
\]
where \(W_J\) is the standard parabolic subgroup and \(P_V(t)=\sum_{v\in V}t^{|\operatorname{Des}_R(v)|}\) its descent-Eulerian polynomial. Moreover, \(\widehat f(J)\ne0\) if and only if **every connected component of the Coxeter graph induced by \(J\) has an even number of vertices**. The empty induced graph passes vacuously.

Write \(F_0=0\), \(F_1=1\), \(F_{m+2}=F_{m+1}+F_m\). Then
\[
\boxed{\operatorname{rank}_{\mathbb C}T=\operatorname{rank}_{\mathbb R}T=F_{r+1}.}
\]
More generally, if \(W\) decomposes into irreducible factors of ranks \(r_1,\ldots,r_k\), its convolution rank is \(\prod_{i=1}^kF_{r_i+1}\). No claim about the full multiplier magnitudes or endpoint inverse norms is made.

## Assumptions and scope
The Coxeter system is finite and its simple-reflection generating set is fixed. Right descents are used consistently; reversing to left descents gives the same counting distribution by inversion. The Walsh transform uses the unnormalized convention \(\widehat f(J)=\sum_xf(x)(-1)^{|J\cap x|}\). The irreducible finite Coxeter diagrams are the path diagrams of types \(A\), \(B\), \(I_2\), and the other simply-laced or exceptional finite diagrams, all trees of maximum vertex degree three; isolated rank-one nodes are allowed. The rank assertion is for linear convolution, not for the support cardinality of distinct descents.

## Proof
**Parabolic reduction.** Every element \(w\in W\) has a unique right parabolic decomposition \(w=uv\), with \(v\in W_J\), \(u\) the minimal right \(W_J\)-coset representative, and \(\ell(uv)=\ell(u)+\ell(v)\). Then \(\operatorname{Des}_R(w)\cap J=\operatorname{Des}_R(v)\). There are \(|W|/|W_J|\) choices for \(u\), giving the displayed multiplier formula. If the induced diagram \(\Gamma[J]\) has components \(J_1,\ldots,J_t\), the parabolic group and its Eulerian polynomial split as products over these components.

**Exact nonvanishing for connected parabolics.** Let \(V\) be finite irreducible of rank \(m\). Its longest element reverses the number of descents, so \(P_V(t)=t^mP_V(t^{-1})\). Thus \(P_V(-1)=0\) for odd \(m\). For even \(m\), the complete finite classification together with the explicit Coxeter Eulerian polynomial formulas proves nonvanishing:

* For type \(A_{2a}\), \(P(-1)=(-1)^aE_{2a+1}\), where \(E_j>0\) are Euler zigzag numbers.
* For type \(B_{2a}\), \(P(-1)=(-1)^a2^{2a}E_{2a}\).
* For type \(D_{2a}\) with \(a\ge2\), \(P(-1)=(-1)^a2^{2a-1}\bigl(2E_{2a}-2aE_{2a-1}\bigr)\). The first parenthesis is nonzero, since \(E_{2a}\) is odd while \(E_{2a-1}\) is even for \(2a-1\ge3\): the bracket is \(2\) modulo \(4\).
* For dihedral type \(I_2(m)\), \(P(t)=1+(2m-2)t+t^2\), so \(P(-1)=4-2m\ne0\) for \(m\ge3\).
* The even-rank exceptional evaluations are \(P_{F_4}(-1)=208\), \(P_{H_4}(-1)=3856\), \(P_{E_6}(-1)=-3104\), and \(P_{E_8}(-1)=17111296\). The values for \(F_4,E_6,E_8\) follow by alternating the coefficients of Cohen's Table 1. The printed \(H_4\) row instead sums to \(7200\) at \(t=1\), not \(|W(H_4)|=14400\), so we evaluate this case from the parabolic indices. For any finite Coxeter system \((W,S)\), expansion of \(\prod_{s\in S}(2\mathbf 1_{s\notin\operatorname{Des}_R(w)}-1)\) and the parabolic representative count give
  \[
  P_W(-1)=\sum_{J\subseteq S}(-1)^{|S|-|J|}2^{|J|}\frac{|W|}{|W_J|}.
  \]
  For the path \(H_4\) with edge labels \(5,3,3\), the two-vertex parabolic orders are \(10,6,6,4,4,4\), and the three-vertex orders are \(120,24,20,12\). Together with orders \(1,2,14400\) for the empty, singleton and full sets, this gives \(14400-57600+68160-21120+16=3856\), as required.

The Euler-number parity statements follow from the classical secant/tangent generating-function recurrences, or direct induction on the corresponding Euler-number recurrence. These formulas are established in the classical work cited below; the claim here is their consequence for **all subset-frequency supports**. It follows that a multiplier vanishes precisely when at least one induced parabolic connected component has odd rank.

**Universal subcubic-tree counting lemma.** Let \(G\) be any tree with \(r\) vertices and maximum degree at most three. The number of vertex subsets \(J\) for which every component of \(G[J]\) is even is \(F_{r+1}\). To prove this, define \(H\subseteq E(G)\) to be *admissible* when every vertex has \(H\)-degree either zero or odd. Send \(H\) to its odd-degree boundary \(J\). Since every edge of \(H\) joins two vertices of \(J\), the components of \(G[J]\) are unions of even-order components of \(H\), and are even. Conversely, in each component of the forest \(G[J]\), pair up the vertices and take the symmetric difference of their connecting paths. The resulting edge set has odd-degree boundary equal to the whole component. It is unique: the symmetric difference of two solutions would be an edge set with empty odd-degree boundary, but every nonempty edge set in a forest has a vertex of degree one. Combining the component solutions, with no edges outside \(G[J]\), supplies the unique admissible \(H\).

Root \(G\) at a leaf, or at its only vertex if \(r=1\), so each vertex has zero, one or two children. In a rooted subtree, let \(A\) count admissible choices when the parent edge is absent, and \(B\) count choices when the parent edge is present, with the degree constraint enforced at the root too. For a leaf, \((A,B)=(1,1)\). For a single child with counts \((a,b)\), one has \((A,B)=(a+b,a)\). For two children with counts \((a,b)\) and \((c,d)\), the permitted configurations give \((A,B)=(ac+bc+ad,ac+bd)\). Induction using the Fibonacci addition formulas gives \((A,B)=(F_{s+1},F_s)\) for every subtree of \(s\) vertices. The whole-tree answer is \(A=F_{r+1}\), proving the lemma.

Since irreducible finite Coxeter diagrams are subcubic trees, the lemma counts exactly the nonzero Walsh multipliers. The Walsh matrix is invertible over \(\mathbb R\) and \(\mathbb C\), hence the number of nonzero multipliers is the convolution rank. For reducible products, both the kernel and transform factor across components, yielding the stated product formula.

## Verification
The supplied standalone `verify.py` checks the subcubic-tree parity counting lemma on generated labelled trees, and independently evaluates all \(2^r\) binary Walsh characters from exact enumerations of type \(B_r\) and \(D_r\) signed permutations at ranks four through seven. It compares each nonzero character individually against the even-induced-component criterion, and checks the Fibonacci rank. These tests do not check the exceptional evaluations; the \(H_4\) computation is spelled out above. This is finite corroboration only; the all-ranks assertion follows from the proof above and the classical Coxeter Eulerian identities used there.

## Relationship to prior work
Reiner's 1995 paper establishes classical Coxeter descent-distribution and parabolic reduction machinery and explicitly discusses refinements to entire descent sets. Cohen's 2008 paper tabulates and relates the Coxeter Eulerian polynomials, including the type-\(D\) identity and exceptional cases. These are acknowledged as essential premises: neither the parabolic factorization nor the Eulerian polynomial values are claimed as original. The mathematically distinct assertion here is the uniform all-frequency nonvanishing criterion, together with the universal Fibonacci count over Coxeter diagrams, including the subcubic-tree bijection and two-state proof. Related treatments of root-poset incidence and reflection-representation Fourier operators concern different supports and do not by themselves imply the counting-convolution rank here.

## Limitations
The result depends on the *standard Coxeter descent-set distribution*, not on arbitrary edge labelings. It does not classify the sizes of all nonzero multipliers, singular values beyond their support, or optimal endpoint inverse norms. The finite Coxeter classification and classical Eulerian formulas are used as established inputs. Possible unindexed equivalent formulations in Coxeter descent-algebra or graph-parity literature remain a historical-priority risk; no independent mathematical audit has been performed.

## References
1. Victor Reiner, "The distribution of descents and length in a Coxeter group," *Electronic Journal of Combinatorics* **2** (1995), R25, first publicly dated 25 November 1995, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r25 . Full article https://www.combinatorics.org/ojs/index.php/eljc/article/download/v2i1r25/pdf/ .
2. Arjeh M. Cohen, "Eulerian polynomials of spherical type," *Münster Journal of Mathematics* **1** (2008), 1–8, https://research.tue.nl/en/publications/eulerian-polynomials-of-spherical-type/ . Author-accessible full text https://pure.tue.nl/ws/files/2928709/Metis225320.pdf .
