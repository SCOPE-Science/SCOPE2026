# Smith forms of unitary divisors of polynomial-value differences

## Finding

For an integer \(N\ge 1\) and integer \(d\), define the unitary-divisor selector
\[
U_N(d)=\prod_{q\parallel N}\begin{cases}q,&q\mid d,\\1,&q\nmid d,\end{cases}
\]
where \(q\parallel N\) means a maximal prime-power divisor of \(N\) (the empty product is \(1\)). Given an arbitrary integer polynomial \(P\in\mathbb Z[T]\), consider the integral \(N\)-by-\(N\) matrix
\[
M_N(P)_{x,y}=U_N(P(x)-P(y)),\qquad x,y\in\mathbb Z/N\mathbb Z.
\]

**Theorem (all moduli and all integer polynomials).** For each maximal prime power \(q\parallel N\), put \(s_q=|P(\mathbb Z/q\mathbb Z)|\). Form the multiset
\[
\mathcal L(q,s_q)=\begin{cases}
\{q\},&s_q=1,\\
\{1\}\uplus\{q-1\}^{\uplus(s_q-2)}\uplus\{(q-1)(q-1+s_q)\},&2\le s_q\le q.
\end{cases}
\]
Take all products with one element from every \(\mathcal L(q,s_q)\), counting multiplicities, to obtain \(R=\prod_{q\parallel N}s_q\) positive integers \(v_1,\ldots,v_R\). For every rational prime \(\ell\), sort their \(\ell\)-adic valuations into
\(e_{\ell,1}\le\cdots\le e_{\ell,R}\), and set \(d_j=\prod_\ell\ell^{e_{\ell,j}}\). Then
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(M_N(P))=\operatorname{diag}(d_1,\ldots,d_R,0^{N-R}).}
\]
For \(N=1\), the formula means the one-by-one matrix \((1)\). The finite torsion order of the cokernel is
\[
\boxed{\prod_{q\parallel N}\bigl((q-1)^{s_q-1}(q-1+s_q)\bigr)^{R/s_q}.}
\]
In particular, the matrix rank is exactly \(R\), and **two integer polynomials have identical full integer Smith forms for every \(N\)** if and only if their numbers of represented residues agree modulo each individual prime power. The number of inputs representing each residue does not affect any invariant factor.

For squares, the requisite local image cardinalities are explicit:
\[
\begin{aligned}
s_{p^a}(T^2)&=1+\frac{p-1}{2}\sum_{j=0}^{\lfloor(a-1)/2\rfloor}p^{a-2j-1}&&\text{if }p\text{ is odd},\\
s_{2^a}(T^2)&=1+\sum_{j=0}^{\lfloor(a-1)/2\rfloor}u(a-2j),
\end{aligned}
\]
where \(u(1)=u(2)=1\), and \(u(h)=2^{h-3}\) for \(h\ge3\). These formulas thus supply every integer Smith form for the square-value difference matrices without computing large determinants.

The example \(N=15\), \(P(T)=T^2\) has positive Smith factors \(1,4,4,8,224,224\), followed by nine zeros. Notably, \(7\)-torsion occurs although \(7\nmid15\). For \(N=4\), the two polynomials \(P(T)=T^2\) and \(Q(T)=T^3-T\) have different output-fiber sizes, respectively \((2,2)\) and \((3,1)\), but both matrices have the same integral Smith diagonal \((1,15,0,0)\).

## Assumptions and scope

The polynomial \(P\) has arbitrary integer coefficients and no nonsingularity, degree, or injectivity hypothesis. All divisibility tests use standard integer divisibility; in particular every positive divisor divides zero. The matrix rows and columns range over a complete set of residue classes modulo \(N\), and \(U_N\) is the largest unitary divisor of \(N\) dividing its integer argument, not the ordinary gcd. Smith equivalence means independent unimodular integer row and column operations; zeros record the free rank of the cokernel. Equal invariant factors at all moduli means equal lists including zero multiplicities. Empty prime products are \(1\).

## Proof

**1. Prime-power splitting.** Write \(N=\prod_iq_i\) over its maximal prime-power factors. Chinese remainder coordinates identify \(\mathbb Z/N\mathbb Z\) with \(\prod_i\mathbb Z/q_i\mathbb Z\). Because an integer polynomial respects these coordinates and \(U_N\) is a product of independent local selectors, simultaneous row and column permutations give
\[
M_N(P)\cong\bigotimes_i K_{q_i}(P),\qquad K_q(P)_{x,y}=1+(q-1){\bf1}_{P(x)\equiv P(y)\pmod q}.
\]

**2. Elimination of arbitrary fiber multiplicities.** Partition the \(q\) indices by the \(s=|P(\mathbb Z/q\mathbb Z)|\) distinct values of \(P(x)\pmod q\). Every row belonging to the same fiber is identical, as is every corresponding column. Choose one representative of each fiber, subtract the representative row from all other rows in that fiber, and do the corresponding column subtractions. These are unimodular integral operations, and yield
\[
K_q(P)\sim_{\mathbb Z}\bigl((q-1)I_s+J_s\bigr)\oplus0_{q-s},
\]
where \(J_s\) is the all-ones matrix. Thus local Smith data depend only on \(s\), not on individual fiber sizes.

**3. Exact local Smith form.** Put \(a=q-1\). When \(s=1\), the one-by-one positive block is \((q)\). Suppose \(s\ge2\). For each \(1\le j<s\), every \(j\)-minor of \(aI_s+J_s\) is divisible by \(a^{j-1}\): after taking differences of \(j-1\) rows inside the minor, all those difference rows are divisible by \(a\). This lower bound is sharp, because the minor on rows \(1,\ldots,j\) and columns \(2,\ldots,j+1\) equals \(\pm a^{j-1}\). The matrix determinant is \(a^{s-1}(a+s)\), by the rank-one determinant identity (or by its eigenvalues). Therefore the determinantal divisors are \(\Delta_j=a^{j-1}\) for \(1\le j<s\) and \(\Delta_s=a^{s-1}(a+s)\). Their successive ratios are exactly
\[
1,\quad\underbrace{a,\ldots,a}_{s-2\text{ copies}},\quad a(a+s),
\]
which divide successively, as required for the integer Smith normal form.

**4. Global Smith forms.** Tensor the integral left/right reduction matrices from steps 2–3. Their Kronecker products remain unimodular because determinants are \(\pm1\). They reduce \(M_N(P)\) to a diagonal matrix whose nonzero entries are exactly the products \(v_i\) in the theorem. A diagonal integer matrix has canonical invariant factors obtained by independently sorting the valuations of its nonzero diagonal entries for every rational prime and then recombining positionwise. This gives the stated formula, its rank, and the finite torsion order by multiplying the local nonzero determinants, each taken \(R/s_q\) times.

**5. Universal equivalence and square application.** At \(N=p^a\), the rank just proved is precisely \(s_{p^a}(P)\). Hence equal Smith diagonals for all \(N\) force equality of the prime-power image cardinalities; the converse follows from the product construction. For \(P(T)=T^2\), any square modulo \(p^a\) has either zero value or even \(p\)-adic valuation \(2j<a\). At that valuation its unit factor is a square modulo \(p^{a-2j}\), with exactly \(\varphi(p^{a-2j})/2\) possibilities for odd \(p\). For \(p=2\), the numbers of odd square units at levels \(1,2,h\ge3\) are \(1,1,2^{h-3}\). Distinct valuations do not overlap, which proves both explicit image formulas.

All steps use finite integer algebra and are valid for arbitrarily large moduli and polynomial coefficients.

## Verification

A standalone Python 3 checker, `CHECKER.py`, independently constructs the integer matrix \(M_N(P)\) and performs exact Euclidean Smith reductions without external libraries. It compares these results with the separate prime-power formula for five contrasting polynomials and nineteen moduli, including composite nonsquarefree moduli. It separately enumerates squares modulo selected powers of \(2,3,5,7,11\), checks their derived formula, and checks the two displayed Smith examples. In the delivered package it passed 126 grouped tests. These finite checks detect implementation errors but are not substitutes for the general determinantal-divisor proof above.

To reproduce, extract `CHECKER.py` unchanged and run `python3 CHECKER.py` in any standard Python 3 environment. The proof itself has no software dependency.

## Relationship to prior work

Smith's determinant theory and later work on gcd, lcm, and unitary-divisor matrices motivate the arithmetic kernels. Haukkanen and Sillanpää (1996) prove determinant identities for unitary GCD/LCM analogues on divisor-closed sets. Haukkanen and Korkee (2005) study divisibility of gcd/lcm matrices and unitary analogues; Haukkanen, Ilmonen, Nalli, and Sillanpää (2009/2010) study determinants of unitary gcd reciprocal-lcm matrices. Those objects index positive integers and concern gcd/unitary-gcd values or determinant divisibility, rather than **unitary divisors of differences of polynomial values indexed by an entire residue ring**. The corresponding integer Smith forms and universal value-image equivalence criterion do not follow as statements of the inspected theorems.

Existing exact Smith formulas for ordinary gcd-difference circulants in squarefree moduli cover the boundary case \(P(T)=T\) with squarefree \(N\), since ordinary gcd equals the unitary-divisor selector there. That special case is acknowledged, not claimed new. The present classification includes all prime-power moduli, arbitrary noninjective polynomials, a fiber-multiplicity invariance statement and torsion outside the modulus. General Smith algorithms and the local matrix lemma \(aI+J\) are standard tools; the new content proposed here is the full arithmetically indexed classification and its equivalence criterion.

## Limitations

This classifies the explicitly defined **unitary-divisor selector** and does not classify ordinary \(\gcd(N,P(x)-P(y))\) when \(N\) has a repeated prime factor. The prime-power image cardinalities for an arbitrary input polynomial may require separate arithmetic work; the theorem reduces the matrix classification to them but does not magically compute them. It makes no assertion about eigenvectors, canonical isomorphisms between cokernels, or Smith form of arbitrary unitary-gcd matrices indexed by unrelated integers. A complete historical priority proof is not possible from the inspected literature alone; a general Smith form for rank-one perturbations is long known, and an earlier broader arithmetic formulation may exist. Independent verification has not been performed.

## References

1. P. Haukkanen and J. Sillanpää, *Some Analogues of Smith's Determinant*, Linear and Multilinear Algebra **41** (1996), 233–244. https://doi.org/10.1080/03081089608818478 (1996 original print; precise first-public day not verified).
2. P. Haukkanen and I. Korkee, *Notes on the Divisibility of GCD and LCM Matrices*, International Journal of Mathematics and Mathematical Sciences **2005**, 925–935, first published 25 May 2005. https://doi.org/10.1155/IJMMS.2005.925.
3. P. Haukkanen, P. Ilmonen, A. Nalli and J. Sillanpää, *On Unitary Analogs of GCD Reciprocal LCM Matrices*, Linear and Multilinear Algebra **58** (2010), 599–616, first published online 6 October 2009. https://doi.org/10.1080/03081080902816576.
4. P. H. van der Kamp, *On the Fourier Transform of the Greatest Common Divisor*, Integers **13** (2013), A24. https://integers.hindawi.com/vol13.html.
5. C. Telloni and K. S. Williams, *Smith Forms of Circulant Polynomial Matrices*, Linear Algebra and its Applications (2014). https://doi.org/10.1016/j.laa.2014.06.032.
