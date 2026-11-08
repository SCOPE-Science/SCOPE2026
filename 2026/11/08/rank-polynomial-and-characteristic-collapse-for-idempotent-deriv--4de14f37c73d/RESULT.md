# Rank-polynomial and characteristic collapse for idempotent derivations of complete-bipartite graph Lie algebras

## Finding
Let \(a,b\geq 2\), let \(q\) be a prime power, and let \(\mathfrak g_{a,b}(q)\) be the two-step nilpotent Lie algebra of the complete bipartite graph with separately labeled edges, defined below. For each integer \(r\geq0\), count **distinct linear derivation operators** \(D\) satisfying \(D^2=D\) and \(\operatorname{rank}D=r\); do not quotient by automorphisms. The complete rank enumerator is
\[
P_{a,b,q}(z)=\sum_{\substack{0\le i\le a,\,0\le j\le b\\ \operatorname{char}(\mathbb F_q)=2\ \mathrm{or}\ ij=0}}
{a\brack i}_q{b\brack j}_q
q^{i(a-i)+j(b-j)+(a+b-i-j)s_{ij}+(i+j)(ab-s_{ij})}
z^{i+j+s_{ij}},\quad s_{ij}=i(b-j)+(a-i)j.
\]
Here \({d\brack k}_q\) is the Gaussian binomial coefficient. The formula applies unchanged to extension fields, including nonprime finite fields.

For balanced graphs \(a=b=n\ge2\), the distribution has a sharp characteristic transition as \(n\to\infty\), for each **fixed** prime power \(q\). In odd characteristic,
\[
P_{n,n,q}(z)=1+2\sum_{k=1}^{n}{n\brack k}_q
q^{k(n-k)+nk(3n-2k)}z^{(n+1)k},
\]
and, for a uniformly selected such derivation, \(\operatorname{rank}D/n^2\to3/4\) in probability. More precisely, its rank equals \((n+1)k\), with probability \(1-O_q(q^{-n})\) that \(k\) belongs to the two adjacent integers surrounding
\[
x_n=\frac{3n^2+2n}{4n+4}=\frac{3n}{4}-\frac14+O(n^{-1}).
\]
In characteristic two, \(q^{2n^3}\) different idempotent derivations have rank exactly \(2n\), and
\[
\Pr\bigl(\operatorname{rank}D=2n\bigr)=1-O_q(q^{-n^2/3}),
\qquad \frac{\operatorname{rank}D}{n^2}\xrightarrow{\mathsf P}0.
\]
These are asymptotics for *different fixed-field sequences*, not a joint limit over variable \(q\).

## Assumptions and scope
Take \(U=\mathbb F_q^a\), \(W=\mathbb F_q^b\), \(Z=U\otimes W\), and the direct sum \(\mathfrak g=U\oplus W\oplus Z\). Its bracket is defined by \([u,w]=u\otimes w\), \([w,u]=-u\otimes w\), \([U,U]=[W,W]=[Z,\mathfrak g]=0\); extend bilinearly. In characteristic two it is **alternating**, so it remains a Lie bracket. The dimension is \(a+b+ab\), and \(Z=[\mathfrak g,\mathfrak g]\). We require \(a,b\ge2\) throughout: the argument eliminating cross-block derivations uses two independent vectors on each side. The indeterminate \(z\) records *operator rank*, not rank of the induced map on the abelianization and not a grading-isomorphism invariant.

## Proof
**1. All derivations, not just graded ones.** Since \(Z=[\mathfrak g,\mathfrak g]\), every derivation preserves \(Z\). Write its induced map on \(U\oplus W\) using four blocks. The identity \(D[u,u']=0\), for independent \(u,u'\in U\), forces the component \(U\to W\) to vanish: each coefficient of the independent tensors \(u\otimes w\) and \(u'\otimes w'\) must vanish. The identity \(D[w,w']=0\) similarly eliminates the component \(W\to U\). For \(D[u,w]=[Du,w]+[u,Dw]\), the action on \(Z\) is then uniquely determined. Thus every derivation, and only such a map, is of the form
\[
D=\begin{pmatrix}T&0\\\Phi&S\end{pmatrix},\qquad
T=A\oplus B,\quad S=A\otimes I_W+I_U\otimes B,\quad
\Phi\in\operatorname{Hom}(U\oplus W,Z),
\]
with arbitrary \(A\in\operatorname{End}(U)\) and \(B\in\operatorname{End}(W)\).

**2. Classify idempotence.** Squaring the block matrix yields precisely
\[
T^2=T,\qquad S^2=S,\qquad S\Phi+\Phi T=\Phi.
\]
The first condition says \(A^2=A\) and \(B^2=B\). In that case \(S^2-S=2A\otimes B\). In characteristic two this always vanishes; in odd characteristic it vanishes exactly when \(A=0\) or \(B=0\), because the tensor product of two nonzero linear maps is nonzero over a field. Consequently \(i=\operatorname{rank}A\) and \(j=\operatorname{rank}B\) range over all possible pairs in characteristic two, but satisfy \(ij=0\) in odd characteristic.

**3. Count central shears and ranks.** Both \(T\) and \(S\) are diagonalizable projections under these conditions. Their ranks are respectively \(t=i+j\) and
\[
s=i(b-j)+(a-i)j.
\]
Indeed, on the four eigentensor types of \(A\) and \(B\), \(S\) has value one exactly when one factor has eigenvalue one (and the other zero); the double-one type cannot arise in odd characteristic. Decompose the source and target into their zero and one eigenspaces. The equation \(S\Phi+\Phi T=\Phi\) allows exactly the blocks \(\ker T\to\operatorname{im}S\) and \(\operatorname{im}T\to\ker S\), yielding
\[
e(i,j)=(a+b-t)s+t(ab-s)
\]
free parameters over \(\mathbb F_q\), hence \(q^{e(i,j)}\) shears. Since an idempotent map has rank equal to the trace of its image projection in the ordinary vector-space sense, or directly by its block-triangular characteristic polynomial, \(\operatorname{rank}D=t+s\). More elementarily, for any idempotent block operator, the trace-independent dimension of the image is the sum of the image dimensions induced on the quotient and on the invariant subspace, giving the same formula even in characteristic two.

The number of rank-\(i\) projections on \(\mathbb F_q^a\) is \({a\brack i}_q q^{i(a-i)}\): choose their image, then a complementary kernel. Similarly for \(B\). Multiplying these independent factors and the shear count gives the claimed polynomial, including the unique zero operator.

**4. Odd-characteristic concentration.** For \(a=b=n\), the only positive-rank terms have \((i,j)=(k,0)\) or \((0,k)\). Here \(s=nk\), \(t=k\), and \(e=nk(3n-2k)\), producing the closed polynomial. The Gaussian-binomial estimate
\[
q^{k(n-k)}\le {n\brack k}_q\le C_q q^{k(n-k)},\qquad C_q=\prod_{h\ge1}(1-q^{-h})^{-1}<\infty
\]
shows that the logarithmic base-\(q\) weight differs by a uniformly bounded amount from
\[
F_n(k)=(3n^2+2n)k-(2n+2)k^2
=F_n(x_n)-(2n+2)(k-x_n)^2.
\]
Outside the two integers adjacent to \(x_n\), the squared distance exceeds the best adjacent distance by at least one, so summing the Gaussian tail gives \(O_q(q^{-n})\) probability. The rank is \((n+1)k\), hence its normalized limit is \(3/4\). The separate rank-zero summand has negligible mass.

**5. Characteristic-two collapse.** At \(A=I_U\), \(B=I_W\), one has \(T=I_{2n}\), \(S=0\). Every \(\Phi\in\operatorname{Hom}(\mathbb F_q^{2n},\mathbb F_q^{n^2})\) satisfies the shear equation, giving exactly \(q^{2n^3}\) distinct operators of rank \(2n\).

For every other pair of projection ranks set \(t=i+j<2n\). The upper Gaussian-binomial bound shows that its total contribution is at most \(C_q^2q^{e(i,j)+2i(n-i)+2j(n-j)}\). If \(n\le t<2n\), then \(e(i,j)\le tn^2\) and the remaining exponent is at most \(2n(2n-t)\); the resulting gap from \(2n^3\) is at least \((2n-t)n(n-2)\). If \(t<n\), then \(s\le nt\), giving \(e(i,j)\le nt(3n-2t)\le9n^3/8\), while the projection exponent is at most \(n^2\). For every \(n\ge4\), all competing terms are therefore bounded by \(C_q^2q^{2n^3-n^2/2}\). At most \((n+1)^2\) terms occur, so the probability of leaving the \(A=B=I\) stratum is at most \(C_q^2(n+1)^2q^{-n^2/2}=O_q(q^{-n^2/3})\). This establishes the rank concentration and its normalized limit.

## Verification
The accompanying standalone Python 3 program `verify.py` independently enumerates all idempotent matrices \(A,B\) for small prime fields. It forms the actual linear system for \(\Phi\) using matrix multiplication and Gaussian elimination, measures the dimension of its solution space, computes the rank of the corresponding derivation matrix, and compares the resulting full rank histograms with the formula. The tests include \((a,b,q)=(2,2,2),(2,2,3),(2,2,5),(2,3,2)\). For example,
\[
P_{2,2,2}(z)=1+3072z^3+74752z^4+3072z^5+512z^6,
\]
\[
P_{2,2,3}(z)=1+157464z^3+13122z^6.
\]
Run `python3 verify.py`; successful completion prints `VERIFY_OK`. The finite checks do **not** prove the infinite family or asymptotics, which are established in Steps 1–5.

## Relationship to prior work
Godoy Molina and Lagos introduced the graph-associated Lie algebra construction and examined strata-preserving derivations of complete bipartite graph Lie algebras with distinct labels; their treatment restricts its main proofs to characteristic other than two. Their Section 5.2 provides the corresponding structural matrix identities, but not the idempotent-operator rank census, unrestricted central shears, or finite-field concentration law. Burde and Moens study derivations obeying polynomial identities and resulting nilpotency conditions, but not this particular counting invariant. Eick and Moede compute characteristic-two gradings from *inner* idempotent derivations in **simple** Lie algebras over small fields; this nilpotent family instead has zero square of every inner derivation, while its noninner idempotent derivations exhibit the measured spectrum. These are distinct statements; the underlying graph and general polynomial-derivation themes are established mathematics, not originality claims.

## Limitations
The proof requires both bipartite part sizes at least two and individually labeled edges; neither the one-label quotient nor arbitrary graphs are covered. Counts are for individual embedded linear derivations, not conjugacy classes. The asymptotic claims are for balanced part sizes and fixed field size. Numerical verification covers only the indicated prime fields and low dimensions; arbitrary prime powers follow from the algebraic argument. Searches of existing literature and accessible research records did not locate equivalent counts, but publication priority is not independently certified, and a more general, uninspected counting theorem may imply the result.

## References
1. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272 (first submitted 1 August 2023), especially Sections 2 and 5.2. https://arxiv.org/abs/2308.00272
2. D. Burde and W. A. Moens, *The structure of Lie algebras with a derivation satisfying a polynomial identity*, arXiv:2009.05434 (first submitted 11 September 2020), especially the main polynomial-identity framework. https://arxiv.org/abs/2009.05434
3. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155 (first submitted 6 May 2022), especially Section 2.1. https://arxiv.org/abs/2205.03155
