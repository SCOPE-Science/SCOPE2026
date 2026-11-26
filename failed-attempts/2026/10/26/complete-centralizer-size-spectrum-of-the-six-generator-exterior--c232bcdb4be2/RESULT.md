# Complete centralizer-size spectrum of the six-generator exterior algebra over odd finite fields

## Finding
Let \(q\) be an **odd prime power**, \(V=\mathbb F_q^6\), and \(A=\bigwedge V\), an associative unital algebra of dimension \(64\). For \(a\in A\), its additive centralizer is
\[
C_A(a)=\{b\in A:ab=ba\}.
\]
Write \({n\brack k}_q=\prod_{j=0}^{k-1}(q^{n-j}-1)/(q^{k-j}-1)\), and define
\[
D=(q-1){6\brack 3}_q,\quad B={6\brack1}_q\bigl(q^{10}-1-(q-1){5\brack2}_q\bigr),\quad G=q^{20}-1-D-B.
\]
**Theorem.** Exactly the following six cardinalities of additive centralizers occur, with multiplicities among all \(q^{64}\) elements of \(A\):

| Centralizer order | Multiplicity |
|---|---|
| \(q^{64}\) | \(q^{32}\) |
| \(q^{63}\) | \(q^{32}(q^6-1)\) |
| \(q^{60}\) | \(q^{38}D\) |
| \(q^{58}\) | \(q^{38}B\) |
| \(q^{57}\) | \(q^{38}G\) |
| \(q^{48}\) | \(q^{58}(q^6-1)\) |

Every displayed multiplicity is positive for odd \(q\). Their sum is \(q^{64}\). The result holds uniformly over finite fields of every odd characteristic, with no algebraic-closure assumption.

## Assumptions and scope
The exterior product satisfies \(v\wedge v=0\). Denote the even and odd subspaces by \(A_{\rm ev}\) and \(A_{\rm od}\), each of dimension \(32\). For any element \(a=a_{\rm ev}+u\), \(u\in A_{\rm od}\), put \(r(u)=\operatorname{rank}(b\mapsto u\wedge b:A_{\rm od}\to A_{\rm ev})\). No characteristic-two assertion is made: there the ordinary associative exterior algebra is commutative, so all centralizers are the whole algebra. No multiplicative unit-group centralizers are counted.

## Proof
**Step 1 (commutator rank).** Graded commutativity and the invertibility of \(2\in\mathbb F_q\) give \([a,b]=2u\wedge b_{\rm od}\). Thus \(C_A(a)\) is the direct sum of all even elements and the kernel of a linear map from the 32-dimensional odd subspace of rank \(r(u)\). Hence \(|C_A(a)|=q^{64-r(u)}\). The even component of \(a\) is arbitrary, contributing a factor \(q^{32}\) to every stratum.

**Step 2 (nonzero linear component).** Write \(u=v+\omega+\eta\), with respective exterior degrees \(1,3,5\). If \(v\ne0\), choose a basis starting with \(v\). The substitution of its first generator by \(u\) and the remaining generators by themselves defines a parity-preserving filtered algebra automorphism (every odd element squares to zero, and the associated graded generator map is invertible). It conjugates multiplication by \(u\) to multiplication by that generator. The latter map from odd to even exterior degrees has rank \(16\), since its image consists of the 16 even monomials containing the generator. There are \((q^6-1)q^{20}q^6=(q^6-1)q^{26}\) such odd \(u\).

**Step 3 (vanishing cubic).** If \(v=0\) and \(\omega=0\), multiplication by \(\eta\in\bigwedge^5 V\) annihilates all odd homogeneous pieces except \(\bigwedge^1 V\); for \(\eta\ne0\), the map from degree one to \(\bigwedge^6 V\) has rank \(1\). There are \(q^6-1\) such elements, and one zero odd element has rank \(0\).

**Step 4 (nonzero cubic).** If \(v=0\) and \(\omega\ne0\), put \(W_\omega=\{x\in V:x\wedge\omega=0\}\) and \(k=\dim W_\omega\). Multiplication on odd inputs has a degree-four output from \(\bigwedge^1 V\) of rank \(6-k\), and a degree-six output from \(\bigwedge^3 V\) of rank \(1\) by the perfect complementary-degree pairing. The degree-five summand \(\eta\) only adds a map from degree one to degree six; that degree-six target is already in the image of multiplication by \(\omega\). Thus \(r(u)=7-k\), independently of \(\eta\).

If \(k>0\), fix a line \(\ell=\langle x\rangle\subset W_\omega\). The exterior divisibility identity \(x\wedge\omega=0\iff\omega=x\wedge\beta\), with \(\beta\in\bigwedge^2(V/\ell)\), is exact. A nonzero bivector in the five-dimensional quotient has alternating rank \(2\) or \(4\). At rank \(2\), \(\omega\) is a decomposable trivector and its wedge-annihilator equals its unique three-dimensional support (\(k=3\)); at rank \(4\), the induced bivector has trivial wedge-annihilator on the quotient, so \(W_\omega=\ell\) (\(k=1\)). If no such line exists then \(k=0\). Consequently \(r(u)\in\{4,6,7\}\) for \(\omega\ne0\). This also proves the absence of other centralizer sizes.

**Step 5 (counting cubic strata).** Nonzero decomposable trivectors are uniquely determined by a 3-plane and a nonzero element of its top exterior power; hence there are \(D=(q-1){6\brack3}_q\) of them. Those having a one-dimensional wedge-annihilator have a unique line \(\ell\), and the induced bivector in the five-dimensional quotient must have rank \(4\). Since \(\dim\bigwedge^2\mathbb F_q^5=10\), and exactly \((q-1){5\brack2}_q\) of its nonzero bivectors have rank \(2\), the number of rank-four bivectors is \(q^{10}-1-(q-1){5\brack2}_q\). Multiplying by \({6\brack1}_q\) yields \(B\). The remaining \(G=q^{20}-1-D-B\) nonzero trivectors have \(k=0\). Each admits \(q^6\) independent degree-five tails, and every odd element admits \(q^{32}\) independent even parts. These factors give every table multiplicity.

## Verification
The independent-of-formula finite-field code `verify_centralizers6.py` constructs explicit exterior products and calculates the rank of the full \(32\)-by-\(32\) odd-to-even multiplication matrix using modular elimination. It checks representative forms and 70 pseudorandom odd elements per field for \(q=3,5,7\), 228 matrix cases altogether. It also checks that the six closed multiplicities sum to \(q^{64}\) for all three tested field orders. A separate symbolic calculation verifies that \(\sum_a |C_A(a)|\) equals the established six-generator commuting-pair polynomial \(q^{115}+q^{112}+q^{111}-q^{106}-q^{105}+q^{96}-q^{95}\). Finite checks support, but do not replace, the general proof.

## Relationship to prior work
The classical classification of alternating trilinear forms over finite fields by Cohen and Helminck (1988), the symplectic trivector orbit classification summarized by De Bruyn and Kwiatkowski (2013), and Shaw's binary trivector geometry are pertinent sources for the cubic part. Those classifications operate on alternating tensors and group orbits; the present invariant counts centralizers of **all** elements of the 64-dimensional associative algebra and combines the linear, cubic, quintic and arbitrary even components. A previously obtained polynomial for the total number of commuting pairs is recovered by taking a weighted sum of this distribution, but that single aggregate does not determine the six multiplicities. The finite-field cubic incidence counts are elementary Grassmannian consequences; no novelty is claimed for Gaussian binomial coefficients or alternating-form normal forms.

## Limitations
The theorem only treats six generators and finite fields of odd characteristic. It does not classify conjugacy classes, scheme-theoretic centralizers, or unit-group centralizers. Earlier complete trivector classifications may contain implicit equivalent numerical refinements; historical-priority verification, particularly against the full Cohen–Helminck article, is incomplete. No independent mathematical audit has been performed.

## References
1. A. M. Cohen and A. G. Helminck, *Trilinear alternating forms on a vector space of dimension 7*, Communications in Algebra 16 (1988), 1–25. DOI: 10.1080/00927878808823558. Earlier trilinear-form classification through dimension seven; publicly accessible publisher abstract, complete article not materially inspected.
2. B. De Bruyn and M. Kwiatkowski, *The classification of the trivectors of a 6-dimensional symplectic space: summary, consequences and connections*, Linear Algebra and its Applications 438 (2013), 3516–3529. DOI: 10.1016/j.laa.2013.01.002. Open-access manuscript: https://biblio.ugent.be/publication/3217932/file/3226894.pdf.
3. R. Shaw, *Trivectors yielding spreads in PG(5,2)*, Journal of Geometry (2010), DOI: 10.1007/s00022-010-0030-6; public release recorded 2010-09-16.
