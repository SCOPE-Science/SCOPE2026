# The distributive lattice of totally invariant varieties for power-linear projective maps

## Finding
Let \(N\ge2\), \(d\ge2\), and \(A=(a_{ij})_{0\le i,j<N}\in\operatorname{GL}_N(\mathbb C)\). Consider the finite surjective endomorphism
\[
F_A:\mathbb P^{N-1}_{\mathbb C}\longrightarrow\mathbb P^{N-1}_{\mathbb C},\qquad
[x_j]_{j=0}^{N-1}\longmapsto\left[\sum_{j=0}^{N-1}a_{ij}x_j^d\right]_{i=0}^{N-1}.
\]
For each nonempty \(I\subseteq\{0,\ldots,N-1\}\), let \(L_I\) be the coordinate projective subspace spanned by \(e_j\) for \(j\in I\). Then the **complete collection of nonempty irreducible closed totally invariant subvarieties**, in the set-theoretic sense \(F_A^{-1}(V)=V\), is precisely
\[
\left\{L_I: \varnothing\ne I\subseteq\{0,\ldots,N-1\},\quad a_{ij}=0\ \text{for all }i\notin I,\ j\in I\right\}.
\]
Define the directed graph \(G_A\) by an arrow \(j\to i\) whenever \(i\ne j\) and \(a_{ij}\ne0\). A permitted \(I\) is exactly a set closed under arrows, equivalently an upper set for reachability in the directed acyclic graph of strongly connected components. With the empty variety adjoined, the inclusion lattice of totally invariant irreducible varieties is the finite distributive lattice of upper sets of this condensation poset. In particular, the exact number of nonempty totally invariant irreducible varieties equals the number of nonempty upper sets, and it depends only on the zero pattern of \(A\), not on \(d\) or the nonzero coefficient values.

For every \(0\le r\le N-2\), the locus in the labelled parameter space \(\operatorname{PGL}_N\) where \(F_A\) admits at least one totally invariant \(r\)-plane has exactly \(\binom N{r+1}\) irreducible components, each of codimension \((r+1)(N-r-1)\). Each component is the condition that one *specified* coordinate \(r\)-plane is invariant. Moreover, every finite distributive lattice with at least two elements occurs as the incidence lattice (including the empty variety) of such a map for some \(N\) and \(d\).

## Assumptions and scope
All varieties and equations are over \(\mathbb C\). Here \(N\ge2\), \(d\ge2\), \(A\) is invertible, and invariance is equality of underlying closed sets under **the first inverse image**, rather than forward invariance alone or invariance under a power. The empty variety is included solely as a formal bottom element when discussing lattices. Subspaces are labelled in the fixed coordinates used to write \(F_A\). The coefficient matrix is defined up to a common nonzero scalar.

## Proof
**1. Reduction to linear varieties.** The theorem of Luo and Meng, *Totally invariant subvarieties of* \(\mathbf P^n\), gives: every irreducible nonempty closed set \(V\) with \(F_A^{-1}(V)=V\) is a linear projective subspace. Its hypotheses hold because \(F_A\) is the composite \(A\circ P_d\), where \(P_d([x_j])=[x_j^d]\) is a finite surjective endomorphism of algebraic degree \(d>1\). This deep linearity theorem is a cited input, not reproved here.

**2. The deck symmetry forces coordinate support.** Write \(W\subseteq\mathbb C^N\) for the vector subspace with \(V=\mathbb P(W)\). The equality of inverse images can be written
\[
\mathbb P(W)=P_d^{-1}(A^{-1}\mathbb P(W)).
\]
For each coordinate \(j\), choose any nontrivial \(d\)-th root of unity \(\zeta\), and define \(g_j\) on \(\mathbb C^N\) to multiply the \(j\)-th coordinate by \(\zeta\) while fixing all others. Since \(P_d\circ g_j=P_d\), the inverse-image equality implies \(g_j(V)=V\), hence \(g_j(W)=W\). If \(w\in W\) has \(j\)-th component \(w_j\), then
\[
\frac{g_jw-w}{\zeta-1}=w_je_j\in W.
\]
Therefore every coordinate axis appearing in any vector of \(W\) lies inside \(W\). Thus \(W\) is the sum of a subset of the coordinate axes: \(V=L_I\) for a uniquely determined nonempty subset \(I\).

**3. Matrix-zero equivalence and its converse.** Since \(P_d(L_I)=L_I\) and \(P_d^{-1}(L_I)=L_I\) set-theoretically, and \(F_A\) is surjective, total invariance of \(L_I\) implies
\[
L_I=F_A(L_I)=A(L_I).
\]
This is equivalent to \(a_{ij}=0\) for all \(j\in I\), \(i\notin I\): the span of the selected columns is contained in \(\mathbb C^I\). Conversely these zero conditions give \(A(L_I)=L_I\) (containment becomes equality by invertibility), so
\[
F_A^{-1}(L_I)=P_d^{-1}(A^{-1}(L_I))=P_d^{-1}(L_I)=L_I.
\]
This proves both directions for every \(I\).

**4. Graph and lattice.** The matrix-zero condition says every arrow leaving a vertex in \(I\) ends in \(I\). Closure under arrows equals closure under directed reachability; it forces each strongly connected component to be entirely inside or outside \(I\), and the included components form an upper set in the condensation poset. Their unions and intersections remain upper sets. Under \(I\mapsto L_I\), the intersection of subspaces agrees with intersection of coordinate sets (possibly empty), and the smallest containing coordinate subspace agrees with union. The resulting lattice is distributive. In particular, if \(G_A\) is strongly connected there is no nonempty proper irreducible totally invariant set, whereas a diagonal \(A\) yields all \(2^N-1\) nonempty coordinate sets. The numerical upper bound itself was already available from Chang--Luo; the classification of which subsets occur is the assertion here.

**5. Parameter-space components.** Fix \(s=r+1\) with \(1\le s\le N-1\). For a given subset \(I\) of size \(s\), the entries in the rectangular block with row outside \(I\) and column in \(I\) must vanish. They are \(s(N-s)\) independent linear equations on the entries of \(A\). The resulting linear subspace of the projective matrix space intersects \(\operatorname{PGL}_N\) in a nonempty irreducible subset of codimension \(s(N-s)\) (it contains the identity). It is closed relative to \(\operatorname{PGL}_N\). The union over all \(\binom Ns\) choices of \(I\) is the desired existence locus. Distinct subsets give distinct, equally dimensional components and none contains another; hence this is exactly its irreducible-component decomposition.

**6. Realizing every finite distributive lattice.** By Birkhoff's representation theorem, every finite distributive lattice is the lattice of upper sets of some finite poset \(Q\) (using the opposite poset if the chosen convention calls them lower sets). If \(Q\) has \(m\ge2\) elements, linearly order its vertices compatibly with the partial order, and choose the upper-triangular matrix \(A=I+B\), with \(B_{ij}=1\) whenever the element \(i\) is strictly above \(j\) in \(Q\), and otherwise \(0\). This matrix is invertible; its reachability poset is exactly \(Q\). The classification above realizes its upper-set lattice in \(\mathbb P^{m-1}\). The two-element distributive lattice is also realized in \(\mathbb P^1\) by any invertible \(2\times2\) matrix all of whose entries are nonzero. Every finite distributive lattice with at least two elements is therefore obtained.

## Verification
The accompanying dependency-free `verify.py` enumerates all binary off-diagonal coefficient patterns in sizes \(N=2,3,4\) with fixed nonzero diagonal and retains the invertible matrices. For each matrix it compares the direct matrix-zero criterion against reachability-closed sets, checks the set operations and the parametrized component-codimension formula, and tests representative strongly connected, chain and diagonal cases. Executing it prints `VERIFY_OK`. These finite checks are corroboration; the proof above applies for every \(N\), \(d\), and invertible complex \(A\).

## Relationship to prior work
Luo--Meng (arXiv:2610.10103v1, October 7, 2026), Section 1's Linearity Theorem and its full proof, establishes the essential general linearity input. It does not describe this special matrix family or classify its allowable coordinate subspaces by directed-graph reachability or parameter-space components. Chang--Luo (arXiv:2607.27738v1, July 30, 2026) independently proves the sharp general binomial bound on numbers of totally invariant prime cycles in each codimension and notes that pure coordinate-power maps attain it; the upper-bound consequence here is **not** claimed to be new. The new object is the exact incidence classification and its parameter-space stratification for mixed power-linear maps, including arbitrary coefficients and graph patterns. Standard diagonal group representation theory and Birkhoff's poset representation theorem are acknowledged ingredients, not original claims.

## Limitations
Only irreducible closed totally invariant subvarieties are classified. Reducible unions may be totally invariant by permuting components and are not classified here. The result concerns inverse-image invariance under the first iterate, not the potentially larger totally periodic exceptional set. It does not provide a classification of arbitrary projective endomorphisms or a new proof of the Luo--Meng theorem. The Chang--Luo paper was compared through available abstract-level materials, not its complete manuscript; an equivalent specialized result in inaccessible or unindexed literature remains possible. No independent validation has been performed.

## References
Luo, Y., and Meng, S., *Totally invariant subvarieties of* \(\mathbf P^n\), arXiv:2610.10103v1 (October 7, 2026), https://arxiv.org/abs/2610.10103.

Chang, W., and Luo, Y., *Sharp Bounds for Totally Invariant Cycles of Projective Varieties*, arXiv:2607.27738v1 (July 30, 2026), https://arxiv.org/abs/2607.27738.

Birkhoff, G., *Rings of sets*, Duke Math. J. 3 (1937), 443--454 (finite distributive-lattice representation).
