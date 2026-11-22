# A mod-four collision law for Walsh nullity of minimal dominating sets on \(K_{a,b}\)

## Finding
Let \(a,b\ge2\). The Fourier spectrum of the binary-incidence indicator of every inclusion-minimal dominating set of \(K_{a,b}\) is explicit. For a Walsh frequency selecting \(i\) coordinates on the first shore and \(j\) on the second, its unnormalized multiplier is
\[
\lambda_{i,j}=(a-2i)(b-2j)+(-1)^i+(-1)^j.
\]
Write \(Z(a,b)\) for the nullity of convolution by this indicator on \(\mathbb C^{(\mathbb Z/2\mathbb Z)^{a+b}}\). Its complete formula is:

- Both \(a,b\) odd: \(Z(a,b)=0\).
- Both \(a,b\) even, with \(C_a=\binom a{a/2}\), \(C_b=\binom b{b/2}\):
  \[
  Z(a,b)=C_a2^{b-1}+C_b2^{a-1}
  -\mathbf1_{\{a/2\not\equiv b/2\pmod2\}}C_aC_b.
  \]
- \(a\) even, \(b\) odd:
  \[
  Z(a,b)=\binom a{a/2}2^{b-1}
   +\binom a{a/2-1}\binom b{(b-1)/2}.
  \]
- \(a\) odd, \(b\) even: interchange \(a\) and \(b\) in the preceding expression.

In particular, **convolution is invertible precisely when both shores have odd size**. The spectral norm is \(ab+2\), and the smallest strictly positive singular value is \(1\) for two odd shores and \(2\) otherwise. Thus the sharp condition number on the orthogonal complement of the kernel is \(ab+2\) or \((ab+2)/2\), respectively. When both sizes are even, the central-frequency families overlap and must be subtracted exactly when the two half-sizes have opposite parity; this produces the mod-four collision.

## Assumptions and scope
The graph is the finite simple complete bipartite graph \(K_{a,b}\) with labelled nonempty shores \(A,B\) of sizes \(a,b\ge2\). A set \(D\) of vertices is *dominating* if every vertex lies in \(D\) or has a neighbor in \(D\); *inclusion-minimal* means no proper subset is dominating. Identify vertex subsets with incidence vectors in the Boolean group \(H=\mathbb F_2^{a+b}\), where the operation is XOR. Define \(f(x)=1\) precisely on inclusion-minimal dominating sets, zero otherwise, and
\[
(T_f g)(x)=(f*g)(x)=\sum_{y\in H}f(y)g(x-y).
\]
Walsh characters are \(\chi_\omega(x)=(-1)^{\langle\omega,x\rangle}\); the Fourier transform is the *unnormalized* sum \(\widehat f(\omega)=\sum_x f(x)\chi_\omega(x)\). Rank and nullity are over \(\mathbb C\). The singular values are absolute values of these multipliers, each counted with its character multiplicity. No claims are made for shores of size one or arbitrary bipartite graphs.

## Proof
**1. Identify the support.** A dominating subset meeting both shores automatically dominates every vertex. For \(a,b\ge2\), such a set is inclusion-minimal exactly when it contains one vertex from each shore: removing either vertex would leave another vertex on its shore undominated. A dominating subset entirely within \(A\) must equal \(A\), since no vertex of \(A\) is adjacent to another vertex of \(A\); the whole shore \(A\) is inclusion-minimal. Likewise for \(B\). These are all the inclusion-minimal dominating sets:
\[
\mathcal D=\{A,B\}\cup\{\{u,v\}:u\in A,\ v\in B\}.
\]
The union is disjoint, so \(|\mathcal D|=ab+2\).

**2. Transform.** For a frequency with \(i\) selected first-shore coordinates and \(j\) selected second-shore coordinates, the Walsh sums over single vertices on the shores are \(a-2i\) and \(b-2j\). Summing over the \(ab\) cross-shore pairs gives their product. The full-shore sets \(A,B\) contribute \((-1)^i,(-1)^j\), yielding the stated \(\lambda_{i,j}\). There are \(\binom ai\binom bj\) such frequencies. Fourier diagonalization of convolution gives \(Z(a,b)=\sum_{i,j}\binom ai\binom bj\mathbf1_{\{\lambda_{i,j}=0\}}\).

**3. Classify all zero multipliers.** Put \(x=a-2i\), \(y=b-2j\), \(\epsilon=(-1)^i\), \(\eta=(-1)^j\). We need \(xy+\epsilon+\eta=0\).

If both shores have odd size, \(xy\) is odd whereas \(\epsilon+\eta\) is even. There is no zero.

If both shores have even size, \(xy\) is divisible by four and \(\epsilon+\eta\in\{-2,0,2\}\). Vanishing is equivalent to \(xy=0\) and \(\epsilon=-\eta\). The family \(x=0\) has \(\binom a{a/2}2^{b-1}\) members; the family \(y=0\) has \(\binom b{b/2}2^{a-1}\). Their intersection has \(\binom a{a/2}\binom b{b/2}\) members exactly when \((-1)^{a/2}=-(-1)^{b/2}\), and is empty otherwise. Inclusion–exclusion proves the even-even formula.

Now assume \(a=2r\) and \(b=2s+1\). Every zero with \(\epsilon=-\eta\) must have \(x=0\), contributing \(\binom a r2^{b-1}\). Every other zero must have \(\epsilon=\eta\) and \(xy=-2\epsilon\), which forces \(|x|=2\), \(|y|=1\). The two possible values of \(x\) have the same sign \(\epsilon=-(-1)^r\); the two possible values of \(y\) have \(\eta=(-1)^s\operatorname{sgn}(y)\). These two constraints fix a *unique* sign choice:
\[
x=-2(-1)^s,\qquad y=-(-1)^{r+s}.
\]
It contributes \(\binom a{r-1}\binom b s\) frequencies, disjoint from the \(x=0\) class. This gives the even-odd formula. Symmetry supplies the remaining case.

**4. Sharp spectral bounds.** By the triangle inequality \(|\widehat f(\omega)|\le ab+2\) at every frequency, with equality at the trivial character. When both sizes are odd, every multiplier is odd and hence any positive one is at least \(1\). Choose \(|x|=|y|=1\) and \(\epsilon=-\eta\), possible because each odd shore admits two adjacent central frequencies of opposite sign; then \(|\lambda|=1\). If at least one shore is even, all multipliers are even. On that shore choose the central frequency \(x=0\), and on the opposite shore choose the same character parity, obtaining \(|\lambda|=2\). The smallest positive singular values and stated condition numbers follow.

## Verification
The accompanying standalone integer program `verification_mindom.py` constructs the graph adjacency and tests the minimal-dominating-set property for each vertex subset, without assuming the support decomposition. It independently computes the full Walsh transform using the integer butterfly algorithm. It compares every Fourier coefficient, every predicted nullity, the invertibility criterion and both sharp singular-value endpoints for all \(2\le a,b\le7\) with \(a+b\le12\): **33 graph shapes and 30,901 exact assertions passed**. These finite checks support implementation integrity; the preceding algebraic proof, not the finite test, establishes the universal claim.

For two shore sizes increasing comparably, the exact nullity fraction has the parity-dependent expansion
\[
\frac{Z(a,b)}{2^{a+b}}=\frac12\mathbf1_{\{a\text{ even}\}}\sqrt{\frac{2}{\pi a}}+\frac12\mathbf1_{\{b\text{ even}\}}\sqrt{\frac{2}{\pi b}}+O\bigl((ab)^{-1/2}+a^{-3/2}+b^{-3/2}\bigr),
\]
by Stirling's formula and the exact expressions above. In the odd-odd case the nullity fraction is identically zero, not just asymptotically small.

## Relationship to prior work
Kanté, Limouzy, Mary and Nourine's archival study of inclusion-minimal dominating sets (arXiv:1407.2053, first posted 8 July 2014) provides the natural graph-enumeration problem and the minimal-neighborhood/transversal perspective; its results concern enumeration complexity and structural reductions, not the present signed character multiplicities. Golovach, Heggernes, Kanté, Kratsch and Villanger (2016) study enumeration on chordal bipartite graphs, a class containing all complete bipartite graphs. De Wolf (2008) describes the Boolean Fourier framework used here. The displayed multiplier, mod-four collision subtraction, exact convolution nullity, and sharp positive conditioning are the specific claims of this note; general transform machinery or unspecialized enumeration does not itself state these parameter-resolved formulas.

## Limitations
The theorem covers only labelled \(K_{a,b}\) with \(a,b\ge2\). The character-level spectrum is explicit, but no inverse kernel or group-wide classification for arbitrary bipartite graphs is claimed. Similar signed-enumerator specializations in unindexed literature cannot be ruled out by search alone. Independent mathematical review and separate priority verification have not been carried out.

## References
1. M. M. Kanté, V. Limouzy, A. Mary, L. Nourine, *On the Enumeration of Minimal Dominating Sets and Related Notions*, arXiv:1407.2053 (version 1, 2014-07-08), https://arxiv.org/abs/1407.2053 .
2. P. A. Golovach, P. Heggernes, M. M. Kanté, D. Kratsch, Y. Villanger, *Enumerating minimal dominating sets in chordal bipartite graphs*, Discrete Applied Mathematics 199 (2016), 30–36, https://doi.org/10.1016/j.dam.2014.12.010 .
3. R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library 1 (2008), https://doi.org/10.4086/toc.gs.2008.001 .
