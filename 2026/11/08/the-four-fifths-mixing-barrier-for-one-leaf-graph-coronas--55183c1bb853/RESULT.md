# The four-fifths mixing barrier for one-leaf graph coronas

## Finding

Let \(H\) be any finite, connected, simple, noncomplete graph. Form its one-leaf corona \(G=H\circ K_1\) by attaching one distinct degree-one vertex to every vertex of \(H\). Among all real symmetric, entrywise nonnegative, row-stochastic matrices \(P\) whose off-diagonal support lies in the edges of \(G\), with arbitrary holding probabilities allowed, write \(\mu(P)=\|P-\mathbf{1}\mathbf{1}^\top/|V(G)|\|_2\). Then
\[
\inf_P\mu(P)\ge \frac45.
\]
This universal obstruction is sharp on *every* balanced complete multipartite core \(H=K_{m,\ldots,m}\) with \(r\ge2\) parts of equal size \(m\ge2\):
\[
\min_P\mu(P)=\frac45,\qquad 1-\mu^*=\frac15.
\]
Writing \(d=(r-1)m\), a globally optimal chain assigns \(3/(5d)\) to each core-to-core edge, \(2/5\) to each core-to-private-leaf edge, zero holding at every core vertex and \(3/5\) holding at every leaf. Global optimality applies to **all** feasible symmetric chains, not only automorphism-invariant ones.

For every complete bipartite core \(H=K_{p,q}\) with positive integers \(p,q\) and \(p+q\ge3\), equality in the universal lower bound occurs **if and only if** \(p=q\ge2\). In that balanced bipartite case the optimal transition matrix is unique: every core edge has weight \(3/(5p)\) and every core-to-leaf edge has weight \(2/5\), with the holding probabilities above. Consequently every unequal-side complete bipartite corona has a strictly larger optimal SLEM, although an exact formula for that larger value is not claimed.

## Assumptions and scope

The graph \(H\) is finite, connected, loopless, simple and noncomplete; hence it contains two nonadjacent vertices. Its one-leaf corona has a core vertex \(i\) and a private leaf \(i'\) for each \(i\in V(H)\). There are no leaf-to-leaf edges. The admissible transition matrix \(P\) is symmetric and stochastic, has nonnegative entries, and has no off-diagonal transitions except along the actual graph edges; zero weights on allowed edges are permitted. The stationary distribution is uniform. The objective is the second-largest eigenvalue *modulus* including negative eigenvalues, not merely the second-largest eigenvalue. The finite-dimensional feasible set is compact.

The general lower bound requires no vertex-transitivity, regularity, equal weights, or automorphism averaging. Equal multipartite part size is needed only for the explicit construction. The bipartite equality classification includes star cores, with one part of size one, but excludes the complete graph \(K_{1,1}\), for which the nonedge obstruction is absent.

## Proof

**1. Universal lower bound.** Choose nonadjacent core vertices \(i,j\) and the real vector \(x\) on \(G\) whose only nonzero coordinates are \(x_i=1\), \(x_j=-1\), \(x_{i'}=2\), \(x_{j'}=-2\). It has \(\mathbf{1}^\top x=0\) and \(\|x\|^2=10\). Let \(u_k=\sum_{\ell\in V(H),\ell\ne k}P_{k\ell}\) be the total off-diagonal core transition from \(k\), and \(b_k=P_{kk'}\) the weight of its private leaf edge. Since \(i,j\) are nonadjacent, the Dirichlet-form identity for a symmetric stochastic matrix gives
\[
\frac{x^\top P x}{x^\top x}
=1-\frac{u_i+b_i+u_j+b_j}{10}
\ge 1-\frac2{10}=\frac45,
\]
using \(u_k+b_k\le1\). The centered spectral norm dominates this Rayleigh quotient because \(x\perp\mathbf{1}\). This proves the bound for every admissible \(P\).

**2. Balanced multipartite construction.** For \(H=K_{m,\ldots,m}\) let \(A\) be the adjacency matrix. Its eigenvalues and multiplicities are
\[
 d=(r-1)m\quad(1),\qquad 0\quad(r(m-1)),\qquad -m\quad(r-1).
\]
Set \(a=3/(5d)\), \(b=2/5\), and order coordinates as core followed by corresponding leaves. The proposed transition matrix is
\[
P=\begin{pmatrix}aA&bI\\bI&(1-b)I\end{pmatrix}.
\]
Every core row sums to \(ad+b=1\); every leaf row also sums to one. All entries are nonnegative and graph-supported. For an adjacency eigenvector with eigenvalue \(\lambda\), the invariant two-dimensional block is
\[
B_\lambda=\begin{pmatrix}a\lambda&2/5\\2/5&3/5\end{pmatrix}.
\]
At \(\lambda=d\), its eigenvalues are \(1\) and \(1/5\). At \(\lambda=0\), its eigenvalues are \(4/5\) and \(-1/5\). At \(\lambda=-m\), put \(t=1/(r-1)\), so \(0<t\le1\), and write
\[
5B_{-m}=\begin{pmatrix}-3t&2\\2&3\end{pmatrix}=M_t.
\]
Both \(4I-M_t\) and \(4I+M_t\) are positive semidefinite: the former has nonnegative diagonal and determinant \(3t\), and the latter has nonnegative diagonal and determinant \(24-21t\ge3\). Thus every nonstationary eigenvalue of \(P\) has absolute value at most \(4/5\), and the zero-adjacency block attains \(4/5\) since \(m\ge2\). This proves global optimality by step 1.

**3. Complete-bipartite equality classification.** Let \(H=K_{p,q}\), with \(p,q\ge2\), and suppose an admissible chain attains \(\mu=4/5\). For every nonadjacent core pair in the same part, the lower-bound Rayleigh quotient from step 1 must equal \(4/5\), because its value is at least \(4/5\) and at most the centered spectral norm. Therefore each such core vertex has \(u_k+b_k=1\). Moreover every corresponding vector \(x\) is an eigenvector of \(P\) with eigenvalue \(4/5\) (Rayleigh equality at the largest eigenvalue on \(\mathbf{1}^\perp\)). Looking at its private-leaf coordinates gives \(2-b_k=(4/5)2\), whence \(b_k=2/5\), and so \(u_k=3/5\). Looking at any opposite-part core coordinate shows that its edge weights to the two selected same-part vertices coincide. Applying this to both parts forces a common weight \(a\) on every core edge. Their row sums imply \(qa=3/5=pa\), hence \(p=q\). Conversely, step 2 supplies a chain when \(p=q\). The same eigenvector equalities force all weights and holdings uniquely when the sides balance.

If \(p=1\), \(q\ge2\), the same reasoning on two vertices of the size-\(q\) part forces each of their unique core-to-center edges to have weight \(3/5\); applying it to all of those vertices gives a center core-row sum at least \(3q/5>1\), a contradiction. The case \(q=1\), \(p\ge2\) is symmetric. Compactness then makes the optimal SLEM strictly greater than \(4/5\) for all remaining unequal-side cases.

## Verification

The standalone Python standard-library program `verify.py` checks, with exact fractions, that the universal Rayleigh inequality holds on every connected noncomplete labeled graph of orders three through five under three deterministic nonuniform rational stochastic kernels; that the construction is symmetric, nonnegative, stochastic and graph-supported for all \(2\le r,m\le7\); and that the spectral blocks satisfy the exact \(4/5\) bounds. It also tests the forced-weight incompatibility for unequal complete-bipartite side sizes from two through fourteen. The observed output was:

`VERIFY_OK universal_exact_rayleigh_checks= 9681 balanced_multipartite_exact_matrices= 36 unbalanced_bipartite_necessary_condition_checks= 156`

Run `python3 verify.py` alongside this document. These finite checks are not used to infer the infinite theorem; the exact argument above proves it for all stated graphs.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduce the general symmetric stochastic SLEM minimization and its SDP formulation, including an exact calculation on a *bare* complete bipartite graph. Boyd, Diaconis, Parrilo and Xiao (2007/2009) establish automorphism-based reduction and analyze bare complete multipartite and wheel graphs. The new argument instead produces a sharp lower bound for **every noncomplete core with private leaves**, proves matching optimal weights for all balanced multipartite cores, and characterizes equality versus strictness for the complete-bipartite corona. It does not claim the known general SDP or adjacency-spectrum tools as new.

A previously recorded fastest-mixing calculation for sunlets covers the particular core \(C_4=K_{2,2}\); that one instance is acknowledged as covered and is not treated as an independent novel case. The infinite family with higher-order complete bipartite and multipartite cores, and the universal obstruction/equality classification, are the present scope. Jafarizadeh's clique-lift reduction concerns a different graph operation and does not immediately yield the private-leaf corona theorem. Generalized-corona spectral-polynomial literature studies fixed graph spectra rather than transition-probability optimization; full-text access to one plausible spectral source was unavailable.

## Limitations

No formula is asserted for the optimal SLEM on unequal complete-bipartite coronas, only strict exceedance of \(4/5\). Optimal weight uniqueness is proved only for balanced complete-bipartite cores; for multipartite cores with three or more parts the displayed optimizer need not be unique. The statement concerns uniform-stationary symmetric stochastic chains with optional holding, not arbitrary nonreversible or nonuniform-stationary chains, nor finite-time total-variation mixing. The available originality search cannot rule out unindexed earlier exact formulas. No independent mathematical audit has been performed.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264; author-accessible PDF at https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first posted 2007-09-06, subsequently SIAM Journal on Optimization 20 (2009), 792–819; https://arxiv.org/abs/0709.0955.
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104; openly accessible later copy https://arxiv.org/html/2501.02421v1.
4. A. R. Fiuj Laali, H. Haj Seyyed Javadi and D. Kiani, *Spectra of generalized corona of graphs*, Linear Algebra and its Applications 493 (2016), 411–425, DOI: 10.1016/j.laa.2015.11.032.
