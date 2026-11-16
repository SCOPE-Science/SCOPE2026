# Fourier rank separation between cyclic and Klein four-colour palettes on triangular books

## Finding
Let \(B_n=K_2\vee\overline{K_n}\), \(n\ge3\), be a graph with two adjacent spine vertices and \(n\) independent page vertices, each adjacent to both spine vertices. Colour its vertices properly by an abelian group \(H\) of order four. Regard its proper-colouring indicator as a function on the finite additive group \(H^{n+2}\) and use the **unnormalized** Fourier transform \(W_{H,n}\).

There are exactly \(12\cdot2^n\) proper colourings, regardless of the group structure. Yet the two groups of order four have different Fourier recovery ranks:
\[
\operatorname{rank}T_{\mathbb Z/4,n}=4\cdot2^n+3^{n+1}-(-1)^n-2,
\qquad \operatorname{rank}T_{(\mathbb Z/2)^2,n}=12\cdot2^n-8.
\]
Here \(T_{H,n}f=\mathbf1_{P_{H,n}}*f\) is counting convolution on \(\ell^2(H^{n+2})\), with counting measure. The maximum multiplier modulus is \(12\cdot2^n\) for either group; the minimum *positive* multiplier modulus is \(2^{\lfloor n/2\rfloor+3}\) for the cyclic group and \(4\cdot2^n\) for the Klein group. Consequently the respective sharp positive singular-value condition numbers are
\[
\kappa_{\mathbb Z/4,n}=3\cdot2^{\lceil n/2\rceil-1},\qquad
\kappa_{(\mathbb Z/2)^2,n}=3.
\]
The inverse norm on the orthogonal complement of the nullspace is the reciprocal of the corresponding minimum positive multiplier modulus. For the first three nontrivial book sizes \(n=3,4,5\), the cyclic ranks are \(112,304,856\) while the Klein ranks are \(88,184,376\), respectively.

## Assumptions and scope
Fix \(n\ge3\). Let the spine vertices be \(u,v\) and the pages \(w_1,\dots,w_n\). A proper colouring \(c\in H^{n+2}\) has \(c(u)\ne c(v)\), with every page colour avoiding both spine colours. Thus there are \(4\cdot3\cdot2^n\) such colourings. For frequencies \(\xi=(\alpha,\beta,t_1,\dots,t_n)\in\widehat H^{n+2}\) write
\[
W_{H,n}(\xi)=\sum_{c\text{ proper}}\alpha(c(u))\beta(c(v))\prod_{j=1}^n t_j(c(w_j)).
\]
We call a frequency **balanced** when the product of its \(n+2\) characters is trivial. Frequency multiplicities always count distinct characters, not colourings. The two possible abelian palettes are \(H\cong\mathbb Z/4\mathbb Z\) and \(H\cong(\mathbb Z/2\mathbb Z)^2\). No assumption that palette labels have an ordering is needed.

## Proof
**Character reduction.** Put \(a=c(u)\), \(b=c(v)=a+d\), with \(d\in H\setminus\{0\}\). For any page frequency \(t\), define
\[
\ell_t(d)=\sum_{x\in H\setminus\{0,d\}}t(x)
=\begin{cases}2,&t=1,\\-1-t(d),&t\ne1.\end{cases}
\]
The page sum equals \(t(a)\ell_t(d)\). Summing over the common translation \(a\in H\) proves that \(W(\xi)=0\) for unbalanced frequencies, and for balanced ones gives the exact identity
\[
\boxed{W_{H,n}(\xi)=4\sum_{d\in H\setminus\{0\}}\beta(d)\prod_{j=1}^n\ell_{t_j}(d).}
\]
For every choice of \(\beta\) and \(t_1,\dots,t_n\), balancedness determines \(\alpha\) uniquely. There are therefore \(4^{n+1}\) balanced frequencies.

**Klein palette.** Every nontrivial character \(t\) is \(\pm1\)-valued and has a kernel of order two: \(\ell_t(d)=-2\) on its unique nonzero kernel element and vanishes at the other two nonzero elements. If the page frequencies contain two *different* nontrivial characters, their nonzero supports are disjoint; the multiplier vanishes for each choice of \(\beta\). If all page characters are trivial, the three-term sum is \(3\) for \(\beta=1\) and \(-1\) otherwise. If the page characters use one fixed nontrivial character together with trivial ones, exactly one \(d\) contributes, and every \(\beta\) gives modulus \(4\cdot2^n\). Thus the nonzero balanced frequencies consist of four from the all-trivial page word, plus four for each of the \(3(2^n-1)\) words supported on one nontrivial character and the trivial character. Their number is \(12\cdot2^n-8\), and their absolute multiplier multiset is one value \(12\cdot2^n\) and \(12\cdot2^n-9\) copies of \(4\cdot2^n\).

**Cyclic palette.** Identify the dual group with \(\mathbb Z/4\mathbb Z\), with a character \(t\) taking the value \(i^{td}\) at \(d\). Write \(z\), \(h\), and \(m\) for the numbers of page characters of types \(0\), \(2\), and \(1\) or \(3\), respectively, so \(z+h+m=n\).

If \(h>0\) and \(m>0\), the type-2 factor is supported only at \(d=2\), while odd-type factors vanish there, so **all four** balanced choices of \(\beta\) give zero. If \(h>0\) and \(m=0\), only \(d=2\) contributes, and all four multipliers have modulus \(4\cdot2^n\). If \(h=m=0\), the four multipliers have moduli \(12\cdot2^n\) once and \(4\cdot2^n\) three times.

It remains to treat \(h=0\), \(m>0\). For \(d=2\), every odd factor vanishes, and the products at \(d=1,3\) are complex conjugates. If \(a\) page frequencies equal \(1\) and \(b\) equal \(3\), then \(m=a+b\) and
\[
W=4\cdot2^z\left(i^\beta(-1-i)^a(-1+i)^b+i^{3\beta}(-1+i)^a(-1-i)^b\right).
\]
Since \((-1-i)^a(-1+i)^b\) has phase a multiple of \(\pi/4\), for **odd** \(m\), every one of the four balanced \(\beta\) gives nonzero modulus \(4\cdot2^{n-(m-1)/2}\). For **even** \(m>0\), exactly two choices of \(\beta\) yield zero; the other two give modulus \(8\cdot2^{n-m/2}\). This is a complete classification of all magnitudes and zeros in terms of the page frequency word.

There are \(\binom nm2^m\) page words with exactly \(m\) odd-type characters and no type 2. Therefore the nonzero cyclic rank equals
\[
4\cdot2^n+4\sum_{\substack{1\le m\le n\\m\text{ odd}}}\binom nm2^m
+2\sum_{\substack{2\le m\le n\\m\text{ even}}}\binom nm2^m
=4\cdot2^n+3^{n+1}-(-1)^n-2.
\]
The largest modulus is \(12\cdot2^n\), attained at frequency zero and nowhere else. The least nonzero modulus is attained among the maximal possible odd/even values of \(m\) and equals \(2^{\lfloor n/2\rfloor+3}\). In the Klein palette, the least modulus is \(4\cdot2^n\). Fourier diagonalization of counting convolution proves the stated ranks, inverse norms, and condition numbers.

**Sharp separation.** At \(n=3\) the two ranks equal \(112\) and \(88\). Their difference for general \(n\ge3\) is \(3^{n+1}-8\cdot2^n-(-1)^n+6\), strictly positive because \(3^{n+1}>8\cdot2^n\) for all \(n\ge3\). Thus the group-sensitive rank separation holds at every claimed size.

## Verification
Two standalone exact-arithmetic checkers are supplied in `checks/verify_book_direct.py` and `checks/verify_book_formula.py`. Run them using Python 3 without third-party packages. The first enumerates all four-colorings and Fourier frequencies for each group through \(n=4\), summing exact Gaussian-integer characters. The second uses the independent three-term character formula and enumerates every balanced frequency through \(n=8\). Each reconstructs the rank, minimum nonzero modulus, maximum modulus, and total frequency count, comparing against the stated closed expressions. They both ran successfully before packaging. These finite checks corroborate but do **not** prove the arbitrary-\(n\) theorem, which rests on the support/phase case analysis above.

## Relationship to prior work
The general external-field Potts/V-polynomial framework of Ellis-Monaghan and Moffatt [1] provides graph-weighted partition functions and deletion–contraction machinery; it does not state the complete character-wise Fourier zero pattern of four-colour book graphs or the cyclic-versus-Klein spectral rank separation. Crew and Spirkl [2] develop chromatic symmetric functions for complete multipartite graphs, including this graph family, but symmetric colour inventories do not distinguish the additive structures on the four colour labels. The explicit group-sensitive Fourier rank and sharp recovery constants here refine the unweighted count \(12\cdot2^n\) and are not claimed as consequences requiring only a substitution in ordinary chromatic counting. More generally, these calculations exhibit a first shared-edge triangular book where a vertex-attached triangular-block product law is inapplicable.

## Limitations
The theorem concerns **exactly** the two abelian palette groups of order four, triangular-book graphs, and unnormalized counting convolution. It says nothing about other palette orders, other graph families, or eigenvalue multiplicities of arbitrary graph external-field partition functions. Bounded searches and inspected published sources did not identify a dominating prior theorem; they cannot rule out unindexed historical tables or a distinct equivalent formulation. Scientific review was performed without independent mathematical validation.

## References
1. J. A. Ellis-Monaghan and I. Moffatt, *The Tutte–Potts connection in the presence of an external magnetic field*, arXiv:1005.5470 (first public arXiv version 2010-05-29), https://arxiv.org/abs/1005.5470.
2. L. Crew and S. Spirkl, *A complete multipartite basis for the chromatic symmetric function*, arXiv:2009.14141 (first public arXiv version 2020-09-29), https://arxiv.org/abs/2009.14141.
