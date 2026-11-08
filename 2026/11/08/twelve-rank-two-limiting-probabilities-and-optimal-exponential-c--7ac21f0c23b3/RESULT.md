# Twelve rank-two limiting probabilities and optimal exponential convergence for random total preorders

## Finding
For each integer \(n\ge 1\), choose uniformly a **total preorder** on \(\{1,\ldots,n\}\), equivalently an ordered partition into nonempty equivalence (tie) blocks. Interpret its reflexive, transitive, total comparison relation \(\preceq\) as the only nonlogical symbol in first-order logic with equality. Write \(\rho=\log 2\).

**Theorem.** The set of all possible limits of \(\Pr(W_n\models\varphi)\), as \(\varphi\) ranges over first-order sentences of quantifier rank at most two, is exactly
\[
\left\{a\rho^2+b\rho(1-\rho)+c(1-\rho)^2:\ a,c\in\{0,1\},\ b\in\{0,1,2\}\right\}.
\]
These twelve numbers are pairwise distinct. Every such sentence has a limiting probability and obeys
\[
\Pr(W_n\models\varphi)=\Pr_\infty(\varphi)+O_\varphi(\rho^n).
\]
The base \(\rho\) is optimal uniformly over rank-two sentences: if \(H\) expresses the existence of an **interior nonsingleton tie block**, then
\[
1-\Pr(W_n\models H)\sim 2\rho(e-1)^2\rho^n.
\]
The set of limit probabilities for rank-one sentences is \(\{0,1\}\), so quantifier rank two is the first level at which nontrivial limiting probabilities occur.

## Assumptions and scope
An ordered partition \((B_1,\ldots,B_k)\) of \([n]\) induces \(x\preceq y\) precisely when the block containing \(x\) is not later than that containing \(y\). The relation \(x\sim y\) abbreviates \(x\preceq y\wedge y\preceq x\), and \(x\prec y\) abbreviates \(x\preceq y\wedge\neg(y\preceq x)\). There are no fixed constants, colours, successor predicates, additional counting primitives, or random independent predicates. Quantifier rank counts maximum nesting of quantifiers, and Boolean combinations preserve the maximum rank. All limits take \(n\to\infty\) with the sentence fixed. Small \(n\) are included in the exact enumeration, but the asymptotic statements concern \(n\to\infty\).

A tie block is **interior** when it is neither the first nor the last block. For a world \(x\), its three realized atomic-neighbour conditions are: existence of a strictly earlier world, existence of a strictly later world, and existence of a different world tied with \(x\). For a block at position \(j\) of a partition with \(k\) blocks, these conditions form the triple
\[
\bigl(\mathbf1_{j>1},\mathbf1_{j<k},\mathbf1_{|B_j|>1}\bigr).
\]

## Proof
**1. Exact two-round logical profiles.** Let \(T(W)\subseteq\{0,1\}^3\) be the set of the displayed triples realized by its points. For any two finite nonempty total preorders \(W,V\), the duplicator wins the two-round Ehrenfeucht–Fraïssé game if and only if \(T(W)=T(V)\). Indeed, after a first choice \(x\), the second-round legal atomic relations to that first point are exactly equality, strictly earlier, strictly later, and distinct but tied. The availability of each of the last three possibilities is precisely the corresponding coordinate of its triple. If profiles match, duplicator chooses a point with the same triple, and then matches the second atomic relation. Conversely, if a triple occurs in only one structure, the spoiler chooses a point realizing it; every response has a different availability set, which the spoiler exposes in the second move. This establishes the equivalence for all sentences of quantifier rank at most two, without any finite-size approximation.

Define the typical event \(\mathcal G_n\): there are at least three blocks and both a singleton and a nonsingleton interior block occur. On \(\mathcal G_n\), the entire profile set is determined by the two indicators \(L,R\) recording whether the first and last blocks, respectively, are singletons:
\[
T(W_n)=\{(0,1,1-L),(1,0,1-R),(1,1,0),(1,1,1)\}.
\]
Here the expression \(1-L\) is interpreted as a Boolean value, so the endpoint third coordinate is zero exactly for a singleton endpoint. All four possibilities for \((L,R)\) yield distinct rank-two theories: a singleton first block is expressed by
\[
P_L:=\exists x\,\forall y\,[\,x\preceq y\ \wedge\ ((y\preceq x)\rightarrow y=x)\,],
\]
and a singleton last block by
\[
P_R:=\exists x\,\forall y\,[\,y\preceq x\ \wedge\ ((x\preceq y)\rightarrow y=x)\,].
\]
Both have quantifier rank two. Their Boolean combinations specify any subset of the four endpoint states.

**2. Total preorder enumeration and endpoint probabilities.** Set \(A(z)=e^z-1\). Writing \(F(z)=\sum_{n\ge0}c_n z^n\), where \(n!c_n\) counts labelled ordered partitions, the labelled product/sequence construction gives
\[
F(z)=\frac1{1-A(z)}=\frac1{2-e^z}.
\]
The unique singularity of least modulus is the simple pole \(z=\rho=\log 2\); every other pole is \(\rho+2\pi i m\) with nonzero integer \(m\). Therefore, for any fixed real \(R\) with \(\rho<R<|\rho+2\pi i|\),
\[
c_n=\frac1{2\rho^{n+1}}+O_R(R^{-n}).
\]
At \(n\ge2\), the exact probabilities of a singleton first block and of both endpoint blocks being singletons are, respectively,
\[
\Pr(L=1)=\frac{c_{n-1}}{c_n},\qquad
\Pr(L=R=1)=\frac{c_{n-2}}{c_n}.
\]
(The first formula holds for \(n\ge1\); for \(n=1\), the first and last endpoints are the same block.) Their limits are \(\rho\) and \(\rho^2\), respectively. By reflection the last endpoint also has limit \(\rho\), so \((L,R)\) converges to two independent Bernoulli variables with success probability \(\rho\). Moreover, since one can take \(R>1\) in the pole estimate, the deviations of all four endpoint-state probabilities from their limits are \(o(\rho^n)\).

**3. An exponentially rare exceptional logical profile.** The class of ordered partitions in which no interior block is nonsingleton has exponential generating function
\[
1+A(z)+\frac{A(z)^2}{1-z}.
\]
The coefficient of \(z^n\) tends to \(A(1)^2=(e-1)^2\) because \(A(z)^2\) is entire and the coefficients of \(A(z)^2/(1-z)\) are partial sums of its absolutely convergent coefficient series. Thus the probability of this obstruction is asymptotic to
\[
\frac{(e-1)^2}{c_n}\sim2\rho(e-1)^2\rho^n.
\]
The class having no singleton interior block has exponential generating function
\[
1+A(z)+\frac{A(z)^2}{1-(e^z-1-z)}=1+A(z)+\frac{A(z)^2}{2+z-e^z}.
\]
Its coefficients are \(O(R_0^{-n})\) for some \(R_0>1\), because on \(|z|\le1\) the sum of absolute values of \(e^z-1-z\)'s coefficients is \(e-2<1\), and the inequality remains true in a slightly larger disk. Dividing by \(c_n\) shows that this second obstruction has probability \(o(\rho^n)\). All partitions with fewer than three blocks are covered by the first obstruction. By a union bound,
\[
\Pr(W_n\notin\mathcal G_n)=O(\rho^n).
\]

**4. Classification and optimality.** On \(\mathcal G_n\), the rank-two theory depends only on \((L,R)\). It follows from the game characterization that, for each fixed rank-two sentence \(\varphi\), there is a subset \(S_\varphi\subseteq\{0,1\}^2\) such that the sentence is true precisely for endpoint states in \(S_\varphi\), whenever \(\mathcal G_n\) holds. Steps 2 and 3 imply the claimed \(O_\varphi(\rho^n)\) convergence. The four endpoint atom masses tend to \(\rho^2,\rho(1-\rho),\rho(1-\rho),(1-\rho)^2\), so the collection of all subset-sum limits is exactly the displayed twelve-element set: the middle two equal-mass atoms contribute a coefficient \(b\in\{0,1,2\}\), while the two outer atoms contribute \(a,c\in\{0,1\}\). Boolean combinations of \(P_L,P_R\) attain every subset sum. Distinct triples \((a,b,c)\) yield distinct quadratic polynomials in \(\rho\): subtracting two such expressions gives a nonzero polynomial in \(\rho\) unless all coefficients agree. The number \(\log 2\) is transcendental by the Hermite–Lindemann theorem, so all twelve are distinct.

Finally define
\[
H:=\exists x\,[\,(\exists y\ y\prec x)\wedge(\exists y\ x\prec y)\wedge(\exists y\ (x\sim y\wedge x\ne y))\,].
\]
This has quantifier rank two and holds exactly when an interior nonsingleton block exists. Step 3 gives the positive asymptotic constant for its failure probability, hence no uniform replacement of the convergence base \(\rho\) by any smaller exponential base is possible. At rank at most one, every nonempty total preorder has the same one-move game theory (only one-point atomic information is visible), so all rank-one probabilities are identically zero or one.

## Verification
The accompanying standalone program `checker.py` enumerates all ordered integer compositions of sizes one through five (31 shapes), compares the two-round game to the claimed point-profile characterization on all 961 ordered shape pairs, and checks exact weighted labelled counts and endpoint identities on 16,383 compositions through size fourteen. It also verifies the count of twelve distinct limiting polynomials and evaluates the sharp-obstruction probabilities at three finite sizes. To reproduce: run `python3 checker.py` with Python 3; the expected terminal marker is `RANK_TWO_RANDOM_PREORDER_CHECKS_OK`. These finite checks are independent consistency tests; the infinite result is proven in the preceding steps.

## Relationship to prior work
Uniform random preorders and their ordered-Bell generating function are classical; Cameron, Kang and Stark derive \(F(z)=1/(2-e^z)\) and endpoint-related block statistics. Those enumeration results are used as established premises, **not** claimed new. Mwesigye and Truss analyze low-move Ehrenfeucht–Fraïssé equivalence for finite coloured **linear** orders; their methods concern a different class and do not give this probabilistic total-preorder spectrum. Koponen's 2026 work on finite-model properties and convergence under random expansions, and Falgas-Ravry, Markström, Räty and Skerman's 2026 work on first-order limiting probabilities of **permutation classes**, motivate the general model-theoretic question. The latter examines pairs of strict linear orders, not uniformly sampled total preorders. The contribution here is the exact twelve-value rank-two spectrum together with its optimal exponential convergence rate for uniform total preorders; it is not a new formula for ordered-Bell numbers or a generic claim that low-rank EF games are novel.

## Limitations
The theorem uses the uniform distribution over labelled ordered partitions and the bare one-relation total-preorder signature. It does not assert an analogous spectrum for higher quantifier rank, enriched signatures, random nonuniform preorders, or random permutations. The stated sharpness is among rank-two first-order sentences; the constant is established for a specific witness, not claimed as a universal asymptotic for all sentences. No independent validation or exhaustive historical-priority certification is claimed. An equivalent specialized result might exist in earlier total-preorder limit-law literature.

## References
- V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1, first public 2026-10-12, https://arxiv.org/abs/2610.16163.
- V. Falgas-Ravry, K. Markström, E. Räty, F. Skerman, *On first-order limiting probabilities for small permutation classes*, arXiv:2610.34328v1, first public 2026-10-25, https://arxiv.org/abs/2610.34328.
- P. J. Cameron, D. Kang, D. Stark, *Random preorders and alignments*, Discrete Mathematics 310 (2010), 591–603; preprint dated 2006-07-21, https://webspace.maths.qmul.ac.uk/p.j.cameron/preprints/pre-align.pdf (classical ordered-partition enumeration).
- F. Mwesigye, J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, Order 36 (2019), 107–117, https://doi.org/10.1007/s11083-018-9458-3.
