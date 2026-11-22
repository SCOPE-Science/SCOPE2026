# Weight-dependent affine components and exact Rota–Baxter rank spectra on a split Leibniz family

## Finding

Let \(k\) be a field and \(n\ge2\). Write \(L_n=ku\oplus kv\oplus W\), where \(\dim W=n-2\), with the **left Leibniz** bracket whose only nonzero basic bracket is \([v,u]=u\). Let \(\lambda\in k\). A weight-\(\lambda\) Rota–Baxter operator is a linear map \(R:L_n\to L_n\) satisfying
\[
[Rx,Ry]=R\bigl([Rx,y]+[x,Ry]+\lambda[x,y]\bigr)
\qquad(x,y\in L_n).
\]

Set \(f(x)=\text{the coefficient of }v\text{ in }x\) and \(g(x)=\text{the coefficient of }u\text{ in }x\). The *complete* solution locus is as follows, with every displayed condition holding as an equality of maps or linear functionals.

For \(\lambda=0\), it is the union of **three linear spaces**:
\[
\begin{aligned}
\mathcal A&=\{R:fR=gR=0\},\\
\mathcal B&=\{R:R(u)=0,\ fR=0\},\\
\mathcal C&=\{R:R(u)=0,\ gR=0\}.
\end{aligned}
\]
They have a common pairwise intersection \(\mathcal D=\{R:R(u)=0,\ fR=gR=0\}\).

For \(\lambda\ne0\), the solution locus is the union of **six affine linear spaces**:
\[
\begin{array}{lll}
\mathcal F_1:\ R(u)=0,\ fR=0,&
\mathcal F_2:\ R(u)=0,\ gR=0,&
\mathcal F_3:\ fR=0,\ gR=-\lambda g,\\[3pt]
\mathcal F_4:\ gR=0,\ fR=-\lambda f,&
\mathcal F_5:\ R(u)=-\lambda u,\ fR=-\lambda f,&
\mathcal F_6:\ R(u)=-\lambda u,\ gR=-\lambda g.
\end{array}
\]
For \(n\ge3\), these are precisely the geometric irreducible components of the **reduced solution locus**, with dimensions \(\dim\mathcal F_3=\dim\mathcal F_4=n(n-2)\) and \(\dim\mathcal F_i=(n-1)^2\) for \(i=1,2,5,6\). Their only pairwise intersections are \(\mathcal F_1\cap\mathcal F_2\), \(\mathcal F_2\cap\mathcal F_4\), \(\mathcal F_5\cap\mathcal F_6\), and \(\mathcal F_3\cap\mathcal F_6\), each an affine space of dimension \((n-1)(n-2)\); the four intersections are mutually disjoint. The locus has exactly **two geometric connected components**, the unions \(\mathcal F_1\cup\mathcal F_2\cup\mathcal F_4\) and \(\mathcal F_3\cup\mathcal F_5\cup\mathcal F_6\). At weight zero, for \(n\ge3\), there are three irreducible components through the same linear intersection \(\mathcal D\).

Over every finite field \(k=\mathbb F_q\), define
\[
M_{a,b}(r)= {a\brack r}_q\prod_{j=0}^{r-1}(q^b-q^j),
\]
where \({a\brack r}_q\) is the Gaussian coefficient, empty products are one, and \(M_{a,b}(r)=0\) if \(r<0\) or \(r>\min(a,b)\). Thus \(M_{a,b}(r)\) counts rank-\(r\) matrices of size \(a\times b\). Put \(m=n-1\), \(h=n-2\), and write \(P_{n,q,\lambda}(T)=\sum_{r=0}^{n}N_{n,q,\lambda}(r)T^r\). Then
\[
\boxed{N_{n,q,0}(r)=M_{h,n}(r)+2M_{m,m}(r)-2M_{h,m}(r).}
\]
For every \(\lambda\ne0\), **independently of its nonzero value**,
\[
\boxed{\begin{aligned}
N_{n,q,\lambda}(r)={}&2M_{m,m}(r)+2q^h M_{h,m}(r-1)
+q^{2n-3}M_{h,h}(r-2)+M_{m,m}(r-1)\\
&-M_{h,m}(r)-q^hM_{h,h}(r-1)
-q^hM_{h,h}(r-2)-M_{h,m}(r-1).
\end{aligned}}
\]
In particular, with
\[
H_{n,q}=q^{n(n-2)}+2q^{(n-1)^2}-2q^{(n-1)(n-2)},
\]
one has the exact **weight-doubling law**
\[
\boxed{\#\operatorname{RB}_0(L_n)=H_{n,q},\qquad
\#\operatorname{RB}_{\lambda}(L_n)=2H_{n,q}\quad(\lambda\ne0).}
\]
No weight-zero solution is invertible. In contrast, at every nonzero weight the exact number of invertible solutions is
\[
\boxed{|\mathrm{GL}_{n-1}(\mathbb F_q)|+
\bigl(q^{2n-3}-q^{n-2}\bigr)|\mathrm{GL}_{n-2}(\mathbb F_q)|.}
\]
Here \(|\mathrm{GL}_0(\mathbb F_q)|=1\). The enumerative statements include \(n=2\). The six-component and three-component assertions refer to \(n\ge3\); in dimension two some affine spaces coincide with proper intersections of larger ones.

## Assumptions and scope

The classification is for the explicitly displayed left Leibniz algebra over **any field**, in any characteristic; the bracket is \([x,y]=f(x)g(y)u\). For odd characteristic, the 2023 theorem of Di Bartolo, La Rosa, and Mancini shows that this algebra represents the entire nonnilpotent non-Lie one-dimensional-derived-ideal class in each finite dimension. No corresponding universal classification over characteristic two is assumed. The rank polynomials count labeled endomorphisms of the underlying vector space that satisfy the stated operator identity, not automorphism orbits. All geometric claims concern reduced algebraic sets over an algebraic closure, not the possibly nonreduced scheme cut out by the original quadratic equations.

## Proof

**1. A single tensor equation.** Put \(a=f\circ R\), \(b=g\circ R\), and \(z=R(u)\). Since \([x,y]=f(x)g(y)u\), the operator identity is equivalent for every \(x,y\) to
\[
a(x)b(y)u=\bigl(a(x)g(y)+f(x)b(y)+\lambda f(x)g(y)\bigr)z.\tag{1}
\]
In particular \(a(u)=f(z)\) and \(b(u)=g(z)\).

**2. Exhaustive solution classification.** Suppose first that \(z\notin ku\). Linear independence of \(u,z\) in (1) forces \(a\otimes b=0\) and \(a\otimes g+f\otimes b+\lambda f\otimes g=0\). As a pure tensor vanishes only when one factor is zero, if \(a=0\) then \(b=-\lambda g\), whereas if \(b=0\) then \(a=-\lambda f\). For \(\lambda=0\), both reduce to \(a=b=0\). Now suppose \(z=cu\). Evaluating (1) on \(y=u\) and using \(f(u)=0,g(u)=1,a(u)=0,b(u)=c\) gives \(c(c+\lambda)f=0\), hence \(c=0\) or \(c=-\lambda\). If \(c=0\), equation (1) says \(a\otimes b=0\), so \(a=0\) or \(b=0\). If \(\lambda\ne0\) and \(c=-\lambda\), equation (1) says \((a+\lambda f)\otimes(b+\lambda g)=0\), so \(a=-\lambda f\) or \(b=-\lambda g\). Every resulting family is exactly one of the displayed linear or affine spaces; substitution into (1) proves the converse. These field-theoretic steps work without excluding characteristic two.

**3. Component geometry.** At weight zero, \(\mathcal A\cong\operatorname{Hom}(k^n,k^{n-2})\) and \(\mathcal B,\mathcal C\cong\operatorname{Hom}(k^{n-1},k^{n-1})\). Their pairwise intersections are the same subspace \(\mathcal D\cong\operatorname{Hom}(k^{n-1},k^{n-2})\). At nonzero weight, direct comparison of the six defining affine constraints gives exactly the four pairwise intersections listed; each has \(q^{(n-1)(n-2)}\) rational points over \(\mathbb F_q\) and the stated affine dimension. The first triple is defined by \(g(R(u))=0\), while the second is defined by \(g(R(u))=-\lambda\). Because these two scalars are distinct, the triples are disjoint and open-and-closed in their union. For \(n\ge3\), no listed space is contained in another; hence the listed affine spaces are precisely the geometric irreducible components of the reduced locus. The disjoint pairwise intersection spaces are its singular locus; this additional observation is not an assertion about the scheme-theoretic singularities of the unreduced quadratic ideal.

**4. Exact ranks.** A rectangular \(a\times b\) matrix has rank \(r\) in exactly \(M_{a,b}(r)\) ways: choose its \(r\)-dimensional image, then a surjection onto that image. At zero weight, inclusion-exclusion on \(\mathcal A,\mathcal B,\mathcal C\) gives the first rank formula.

At nonzero weight, the rank distributions for \(\mathcal F_1,\ldots,\mathcal F_6\), respectively, are
\[
\begin{array}{lll}
M_{m,m}(r),&M_{m,m}(r),&q^hM_{h,m}(r-1),\\
q^hM_{h,m}(r-1),&q^{2n-3}M_{h,h}(r-2),&M_{m,m}(r-1).
\end{array}
\]
Indeed, \(\mathcal F_3,\mathcal F_4\) each have a nonzero fixed pivot plus an arbitrary \(h\times m\) residual matrix and \(h\) free scalar entries. In \(\mathcal F_5\), the two fixed pivots \(R(u)=-\lambda u\) and the \(v\)-coefficient of \(R(v)=-\lambda v+\cdots\) leave an arbitrary \(h\times h\) Schur block and \(2n-3\) free entries. In \(\mathcal F_6\), the fixed \(u\)-pivot leaves an arbitrary \(m\times m\) block. The rank distributions at the four respective pairwise intersections \((1,2),(2,4),(5,6),(3,6)\) are
\[
M_{h,m}(r),\quad q^hM_{h,h}(r-1),\quad
q^hM_{h,h}(r-2),\quad M_{h,m}(r-1).
\]
There are no triple intersections. Inclusion-exclusion gives the second boxed rank formula. At \(r=n\), only components \(\mathcal F_5\) and \(\mathcal F_6\) and their intersection contribute, giving the invertible count.

**5. Total counts.** At weight zero the three component sizes are \(q^{n(n-2)},q^{(n-1)^2},q^{(n-1)^2}\), with the common intersection of size \(q^{(n-1)(n-2)}\). Thus the total is \(H_{n,q}\). At nonzero weight the six components split into two disjoint triples, each with these same three component sizes and exactly two pairwise intersections of the stated size. Each triple therefore has \(H_{n,q}\) points, giving \(2H_{n,q}\). This is an equality of point counts, not an isomorphism of the weight-zero and nonzero-weight geometric loci.

## Verification

The standalone `verify_weighted_rb.py` independently enumerates **every** linear matrix over the prime fields and dimensions \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\). For each matrix it tests all basis-pair instances of the original weighted identity and separately checks membership in the stated affine families, then computes its ordinary matrix rank and compares the full rank polynomial. Every weight was checked for \(n=2\) in the listed prime fields, and weights zero and one (also weight two for \(q=3\)) were checked at higher dimensions. All 17 case-and-weight runs passed. Representative polynomials by rank, starting at rank zero, are
\[
\begin{array}{c|c|c|l}
n&q&\lambda&\bigl(N_{n,q,\lambda}(0),\ldots,N_{n,q,\lambda}(n)\bigr)\\\hline
3&2&0&(1,19,12,0)\\
3&2&1&(1,17,34,12)\\
3&3&0&(1,74,96,0)\\
3&3&1&(1,59,186,96)\\
4&2&0&(1,101,714,336,0)\\
4&2&1&(1,81,734,1152,336).
\end{array}
\]
Execute `python3 verify_weighted_rb.py` using only the Python standard library. These finite checks do not prove the arbitrary-field classification or finite-field formulas; the tensor reduction, component analysis, and rank enumeration above do.

## Relationship to prior work

Di Bartolo–La Rosa–Mancini (arXiv:2307.09102, first public version 2023-07-18, specifically the non-Lie splitting theorem) supply the naturally motivated full family \(L_n\); their results concern structural classification, derivations, automorphisms, and biderivations, not a complete Rota–Baxter locus. Zhang–Li–Zheng (2018, Theorems 17 and 21 and Section 3) classify weight-zero and weight-minus-one Rota–Baxter operators on all two- and three-dimensional non-Lie Leibniz algebras. **Every small-dimensional subcase of the present classification is therefore credited as previously covered.** The contribution here is the all-dimensional family, exact rank distribution, and geometric/weight-doubling phenomena, not rediscovery of those low-dimensional cases. Mondal–Saha (arXiv:2208.00560, Sections 2–6) treat general Rota–Baxter Leibniz cohomology and deformation, without these all-dimensional counts. A published endomorphism/retraction rank classification of this identical \(L_n\) (published-finding corpus, 2026-11-02) counts a different operator identity; its formulas do not directly imply the weighted Rota–Baxter locus. Likewise, an earlier subalgebra census on \(L_n\) does not classify graphs inside the doubled Leibniz algebra required by the Rota–Baxter equation.

## Limitations

The geometric assertions are for the **reduced** operator set; no claim of radicality, flatness, or scheme-theoretic smoothness is made for the quadratic defining ideal. For \(n=2\), some named affine pieces are not maximal irreducible components. The finite-field results count labeled maps, not conjugacy classes, and the proof says nothing about all non-Lie Leibniz algebras in characteristic two. The cited 2018 low-dimensional cases are not novel. No exhaustive literature-priority proof is possible; a more general prior statement giving the exact all-dimensional rank formulas would supersede this claim if found. Exhaustive computational tests are confined to the specified prime-field cases; extension-field universality follows from the algebraic proof, not an independent enumeration over extension fields.

## References

- A. Di Bartolo, G. La Rosa, M. Mancini, *Non-nilpotent Leibniz algebras with one-dimensional derived subalgebra*, arXiv:2307.09102, first public version 2023-07-18, https://arxiv.org/abs/2307.09102; open-access journal version https://doi.org/10.1007/s00009-024-02679-0.
- L. Zhang, L. Li, H. Zheng, *Rota-Baxter Leibniz Algebras and Their Constructions*, *Advances in Mathematical Physics* (2018), https://doi.org/10.1155/2018/8540674, especially Theorems 17 and 21 and Section 3.
- B. Mondal, R. Saha, *Cohomology, deformations and extensions of Rota-Baxter Leibniz algebras*, first public version 2022-08-01, arXiv:2208.00560, https://arxiv.org/abs/2208.00560.
- *Endomorphism and retraction rank spectra of a split non-nilpotent Leibniz family*, publicly accessible finite-field classification of the same \(L_n\) under the different endomorphism identity, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-endomorphism-and-retraction-rank-spectra-of-a-split-non-nilpoten--a54e42eaa57d.
