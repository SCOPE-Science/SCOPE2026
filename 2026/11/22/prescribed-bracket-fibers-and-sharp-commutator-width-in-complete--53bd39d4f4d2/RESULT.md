# Prescribed bracket fibers and sharp commutator width in complete-bipartite graph Lie algebras

## Finding
Fix integers \(a,b\ge 2\) and a finite field \(k=\mathbb F_q\), where \(q\) is any prime power. Let \(L=U\oplus W\oplus Z\), with \(U=k^a\), \(W=k^b\), \(Z=U\otimes_k W\), and central \(Z\). The bracket is
\[
[(u,w,z),(u',w',z')]=u\otimes w'-u'\otimes w.
\]
This is the edge-labeled two-step graph Lie algebra associated to the complete bipartite graph \(K_{a,b}\). Identify \(Z\) with the \(a\)-by-\(b\) matrix space. For every **prescribed** central target \(M\in Z\) of matrix rank \(r\), the number \(F_{a,b,q}(M)\) of ordered pairs \((x,y)\in L^2\) with \([x,y]=M\) is exactly
\[
\boxed{F_{a,b,q}(M)=q^{2ab}\begin{cases}
q^{2b}+(q+1)(q^a-1)q^b+(q^a-1)(q^a-q),&r=0,\\
(q^2-1)(q^a+q^b-q),&r=1,\\
(q^2-1)(q^2-q),&r=2,\\
0,&r\ge3.
\end{cases}}
\]
The rank-zero expression is symmetric in \(a,b\): it also equals \(q^{2a}+q^{2b}+(q+1)q^{a+b}-(q+1)(q^a+q^b)+q\). Thus, for \(a,b\ge3\), the single-bracket image is the proper determinantal variety of matrices of rank at most two, even though the derived Lie ideal is all of \(Z\). For arbitrary fields \(k\), the minimum number of additive Lie brackets whose sum equals \(M\in Z\) is **exactly** \(\lceil\operatorname{rank}(M)/2\rceil\), with zero represented by zero brackets. Hence the commutator width of \(L\) is \(\lceil\min(a,b)/2\rceil\), and the first nonsurjectivity boundary occurs when both vertex parts have at least three elements.

## Assumptions and scope
The Lie algebra is nonassociative only via the displayed Lie bracket: both \(U\) and \(W\) are abelian as Lie subspaces, and \(Z\) is central. No characteristic restriction is imposed. The displayed formula counts **ordered pairs from the full Lie algebra**, including central summands and zero elements; it does not count conjugacy classes or multiplication factorizations of any other algebra. The target \(M\) lies in the central derived subspace \([L,L]=Z\), and the rank is the ordinary matrix rank after selecting bases of the two parts; the rank does not depend on those bases. The width assertion is valid over **any** field, including characteristic two, whereas numerical counts require finite \(q\). All statements concern \(a,b\ge2\).

## Proof
**1. Rank-two factorization of the bracket.** Write \(x=(u,w,z)\), \(y=(u',w',z')\). Let \(A\) be the \(a\)-by-two matrix with columns \(u,u'\), and \(B\) the two-by-\(b\) matrix whose rows are \(w'\) and \(-w\). Then \([x,y]=AB\). The assignment from \((u,w,u',w')\) to \((A,B)\) is a bijection of \(k^{2(a+b)}\) with \(M_{a,2}(k)\times M_{2,b}(k)\). Therefore every single bracket has rank at most two. Conversely, a matrix of rank at most two admits a factorization with inner dimension two over any field, so every such target is attained. The two central inputs \(z,z'\) are unconstrained and, when \(k=\mathbb F_q\), multiply every fiber by \(q^{2ab}\).

**2. Zero target.** Count \(AB=0\) by the rank of \(A\). If \(\operatorname{rank}A=0\), then \(B\) is arbitrary, giving \(q^{2b}\) pairs. There are \((q^a-1)(q+1)\) rank-one \(a\)-by-two matrices; for each, every column of \(B\) can be any vector in the one-dimensional kernel of \(A\), giving \(q^b\) choices. There are \((q^a-1)(q^a-q)\) rank-two matrices \(A\), and each forces \(B=0\). Summing proves the rank-zero formula.

**3. Nonzero rank-one target.** Fix a rank-one \(M\) and write \(\ell=\operatorname{col}(M)\). If \(\operatorname{rank}A=1\), its image must be \(\ell\); there are exactly \(q^2-1\) choices of such \(A\). The equation \(AB=M\) then has \(q^b\) solutions in \(B\), because the kernel of \(A\) has dimension one. If \(\operatorname{rank}A=2\), the column space of \(A\) is any two-plane containing \(\ell\), of which there are \((q^{a-1}-1)/(q-1)\); each two-plane has \((q^2-1)(q^2-q)\) ordered bases. For each rank-two \(A\), the matrix \(B\) is **unique** when \(AB=M\), because \(A\) is injective from \(k^2\) onto its column space. Thus the total is
\[
(q^2-1)q^b+\frac{q^{a-1}-1}{q-1}(q^2-1)(q^2-q)
=(q^2-1)(q^a+q^b-q).
\]
This also covers \(a=2\). The formula is symmetric in \(a,b\), as expected by transposing the factorization.

**4. Rank-two target.** For fixed rank-two \(M\), any factorization \(AB=M\) requires \(A\) and \(B\) to have rank two and \(\operatorname{col}(A)=\operatorname{col}(M)\). There are exactly \(|\operatorname{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)\) possible ordered bases \(A\) of this column plane, and each uniquely determines \(B\). Rank at least three is impossible. This completes the complete fiber formula.

**5. Exact width.** A sum of \(t\) single brackets is a sum of matrices of rank at most two, hence has rank at most \(2t\). This gives the lower bound \(t\ge\lceil\operatorname{rank}(M)/2\rceil\). Conversely, a rank-\(r\) matrix is a sum of \(r\) rank-one outer products by choosing a rank factorization. Group these terms in pairs: each group has rank at most two, so by step 1 is a single Lie bracket. Therefore \(\lceil r/2\rceil\) brackets suffice. Taking a full-rank matrix gives the asserted width.

**6. Size of the image and normalization.** The number of \(a\)-by-\(b\) matrices of rank \(r\) is
\[
R_r(a,b;q)=\frac{\prod_{j=0}^{r-1}(q^a-q^j)(q^b-q^j)}{\prod_{j=0}^{r-1}(q^r-q^j)}.
\]
Thus the single-bracket image has cardinality \(\sum_{r=0}^{\min(2,a,b)}R_r(a,b;q)\). Equivalently, for \(a,b\ge3\), its defining equations are the vanishing of the three-by-three minors, giving an affine determinantal variety of codimension \((a-2)(b-2)\). By partitioning all ordered factors \((A,B)\), the exact normalization \(\sum_{r=0}^{\min(a,b)}R_r(a,b;q)q^{-2ab}F_{a,b,q}(r)=q^{2(a+b)}\) follows; it was also checked directly in the finite verification. The central coordinates do not affect widths or matrix ranks.

## Verification
The standalone Python 3 file `verify_biclique_fibers.py` computes the original Lie bracket for every ordered pair of vertex coordinates and compares **every target**, including unattainable rank-three targets, to the stated four-case formula for seven cases: \((a,b,q)=(2,2,2),(2,3,2),(3,2,2),(3,3,2),(2,2,3),(2,3,3),(2,2,4)\). It implements a separate Gaussian-elimination rank computation and independently enumerates all target ranks; the extension-field case uses \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). The recorded output `checker_output.txt` contains seven PASS lines ending `BICLIQUE_LIE_BRACKET_FIBERS_OK 7`. Its normalized vertex-pair total is \(q^{2(a+b)}\) in each case. These finite checks do **not** replace the arbitrary-field proof in steps 1–5.

## Relationship to prior work
Dani and Mainkar's original graph-Lie construction was electronically published on 2004-04-27; Mainkar's corrected 2013 graph-rigidity paper, first public 2013-10-12, supplies a later exposition of the same object; it addresses isomorphisms, not the distribution or width of prescribed single brackets. Its introductory exposition assumes characteristic different from two, whereas the present bracket is independently defined and proved alternating in every characteristic. DeCoste, DeMeyer and Mainkar (2015) study geometric properties of the corresponding graph Lie algebras, not the present finite-field fiber count. The classical matrix-rank factorization principle is central to the proof and is explicitly treated as **known linear algebra**, not new in itself.

Relevant adjacent results count **Lie ideals** and **abelian subalgebras** of complete-bipartite graph Lie algebras, which are different enumerative questions even though their structural objects agree. A prescribed-bracket theorem for **forest** graphical Lie algebras does not cover \(K_{a,b}\) with \(a,b\ge2\), because such a graph contains a four-cycle; a separately studied triangle-with-leaves family has a different graph and fiber stratification. These comparisons were made against the actual mathematical statements and full available result texts, not merely titles. The contribution assessed here is the combined complete prescribed-target fiber and sharp commutator-width classification for this natural infinite family, rather than matrix rank decomposition itself.

## Limitations
This theorem does not supply prescribed-bracket fibers for arbitrary graphs, graph Lie algebras with repeated edge labels, or the class-three graphical construction. Its rank-specific formulas concern the graph with **every** edge between the two vertex parts, not arbitrary bipartite graphs. It gives exact rational point counts but does not classify scheme-theoretic singularities or establish a new general theory of matrix factorizations. The close relationship to elementary matrix-factorization theory creates a real priority risk: an earlier general rank-factorization formula may implicitly specialize to these fiber counts even if not indexed under graphical Lie terminology. No independent mathematical audit has been performed.

## References
1. S. G. Dani and M. G. Mainkar, *Anosov automorphisms on compact nilmanifolds associated with graphs*, electronically published 2004-04-27, *Transactions of the AMS* **357** (2005), 2235–2251, DOI:10.1090/S0002-9947-04-03518-4.
2. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, arXiv:1310.3414v1, first posted 2013-10-12, https://arxiv.org/html/1310.3414v1 ; published in *Groups, Geometry, and Dynamics* **9** (2015), 55–65, DOI:10.4171/GGD/305.
3. R. DeCoste, L. DeMeyer and M. Mainkar, *Graphs and Metric 2-step Nilpotent Lie Algebras*, arXiv:1512.07944v1, first posted 2015-12-25, https://arxiv.org/abs/1512.07944 .
4. *Complete ideal-dimension polynomials for complete-bipartite graph Lie algebras*, public research result (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-complete-ideal-dimension-polynomials-for-complete-bipartite-grap--f31f1793ea7b .
5. *Complete abelian-subalgebra census for biclique graph Lie algebras*, public research result (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-complete-abelian-subalgebra-census-for-biclique-graph-lie-algebr--05a73a94483e .
6. *Prescribed bracket fibers of finite-field graphical Lie algebras on forests*, public research result (2026-10-13), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-prescribed-bracket-fibers-of-finite-field-graphical-lie-algebras--c92e90370f3f .
7. *Exact bracket fibers and a width-two transition in triangle-with-leaves Lie algebras*, public research result (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-bracket-fibers-and-a-width-two-transition-in-triangle-with--4fd12b2e1ff8 .
