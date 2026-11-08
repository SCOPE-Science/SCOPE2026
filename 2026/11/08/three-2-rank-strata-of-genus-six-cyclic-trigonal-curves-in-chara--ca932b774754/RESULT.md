# Three 2-rank strata of genus-six cyclic trigonal curves in characteristic two

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). For each monic squarefree degree-seven polynomial
\[
f(x)=x^7+a_6x^6+a_5x^5+a_4x^4+a_3x^3+a_2x^2+a_1x+a_0\in k[x],
\]
let \(C_f\) be the smooth projective model of \(y^3=f(x)\). The curve has genus \(6\). Set \(b=a_2+a_3a_6\) and \(c=a_3+a_6^4\), with additions in characteristic \(2\). The \(2\)-rank of its Jacobian is exactly
\[
\gamma(C_f)=\begin{cases}
4&b\ne0,\\
2&b=0,\ c\ne0,\\
0&b=c=0.
\end{cases}
\]
For every integer \(r\ge1\), the ranks of the iterated Cartier operator on holomorphic differentials, listed in increasing order of \(r\), are respectively
\[
(4,4,4,4,\ldots),\qquad(4,3,2,2,\ldots),\qquad(4,3,2,1,0,0,\ldots).
\]
All curves in the family have \(a\)-number \(2\) (the constancy of this \(a\)-number is consistent with Elkin's general characteristic-two theorem and is **not** claimed new). In the open parameter space \(U\subset\mathbb A^7_k\) of monic squarefree septics, the \(2\)-rank-zero stratum is the nonempty smooth irreducible codimension-two subvariety
\[
a_3=a_6^4,\qquad a_2=a_6^5,
\]
and the \(2\)-rank-two stratum is the complement of this subvariety in the smooth hypersurface \(a_2=a_3a_6\). The \(2\)-rank-four locus is their open complement. In particular **all three ranks occur on smooth curves**.

## Assumptions and scope
The statement applies to every algebraically closed characteristic-two field and every monic squarefree \(f\) of degree \(7\). The coefficients \(a_i\) are parameters of the *marked affine polynomial model*; no claim is made about a global equation on the coarse moduli space of unmarked curves. The \(2\)-rank is the dimension over \(\mathbb F_2\) of geometric rational \(2\)-torsion, equivalently the stable rank of Cartier on \(H^0(C_f,\Omega^1)\). The \(a\)-number equals genus minus the rank of the first Cartier operator. The supersingular Newton polygon and full Ekedahl–Oort type are **not** determined here.

## Proof
**Genus and basis.** The map \(x:C_f\to\mathbb P^1\) is a tame cyclic cover of degree \(3\), totally ramified at the seven simple roots of \(f\) and at infinity. Riemann–Hurwitz gives \(2g-2=-6+8(3-1)=10\), hence \(g=6\). There is a unique point at infinity, where \(v(x)=-3\), \(v(y)=-7\), and \(v(dx)=-4\). At every finite ramification point the forms below are regular. A basis of the six holomorphic differentials is
\[
A_0=dx/y,\quad A_1=x\,dx/y,\quad B_j=x^j\,dx/y^2\quad(0\le j\le3).
\]
The valuation bounds at infinity are exactly those displayed indices, and linear independence follows from distinct monomials in the function field.

**Cartier matrix.** For a rational differential on the base, characteristic-two Cartier obeys \(\mathcal C(x^jdx)=0\) for even \(j\) and \(\mathcal C(x^{2j+1}dx)=x^jdx\). Also \(\mathcal C(h^2\omega)=h\mathcal C(\omega)\). Because \(1/y=(1/y^2)^2 f(x)\), applying these identities yields
\[
\begin{aligned}
\mathcal C(A_0)&=\sqrt{a_1}B_0+\sqrt{a_3}B_1+\sqrt{a_5}B_2+B_3,\\
\mathcal C(A_1)&=\sqrt{a_0}B_0+\sqrt{a_2}B_1+\sqrt{a_4}B_2+\sqrt{a_6}B_3,\\
\mathcal C(B_0)&=\mathcal C(B_2)=0,\qquad
\mathcal C(B_1)=A_0,\quad \mathcal C(B_3)=A_1.
\end{aligned}
\]
These formulas define a \(2^{-1}\)-linear operator. Write the block matrix as \(M=\bigl(\begin{smallmatrix}0&Q\\P&0\end{smallmatrix}\bigr)\), with \(P\) of size \(4\times2\) and \(Q\) of size \(2\times4\); \(Q\) extracts the \(B_1,B_3\) coefficients and has rank \(2\).

**Critical independence.** The columns of \(P\) are independent for every squarefree \(f\). Indeed, if the second were \(\lambda\) times the first, comparison of the four coefficients forces
\[
a_6=\lambda^2,\ a_4=\lambda^2a_5,\ a_2=\lambda^2a_3,\ a_0=\lambda^2a_1,
\]
so \(f(x)=(x+\lambda^2)(x^6+a_5x^4+a_3x^2+a_1)\). The degree-six factor is a square over \(k\), contradicting squarefreeness. Therefore \(\operatorname{rank}\mathcal C=\operatorname{rank}P+\operatorname{rank}Q=4\), and \(a(C_f)=6-4=2\).

**Iteration and degeneration.** Denote by \(D^{[q]}\) the matrix obtained by applying the indicated field-power map to every entry, also allowing fractional powers in the perfect field \(k\). On the two-dimensional \(A\)-space the operator \(\mathcal C^2\) has \(2^{-2}\)-linear coefficient matrix \(K=(QP)^{[1/2]}\). Put
\[
H=QP=\begin{pmatrix}s&t\\1&u\end{pmatrix},\quad s=\sqrt{a_3},\quad t=\sqrt{a_2},\quad u=\sqrt{a_6}.
\]
Then \(\det H=\sqrt{b}\). On the \(B\)-space the coefficient matrix of \(\mathcal C^2\) is \(PQ\), of rank exactly \(2\). Hence \(\operatorname{rank}\mathcal C^2=2+\operatorname{rank}H\), and \(\operatorname{rank}\mathcal C^3=2\operatorname{rank}H\). At the fourth iterate, the ranks on the \(A\)- and \(B\)-spaces are respectively \(\operatorname{rank}(K K^{[1/4]})\) and \(\operatorname{rank}H\).

If \(b\ne0\), \(H\) is invertible: all Cartier powers have rank \(4\). If \(b=0\), then \(t=su\) and \(H=v w\) is rank one with \(v=(s,1)^T\), \(w=(1,u)\). Taking entrywise eighth powers shows
\[
(KK^{[1/4]})^{[8]}=H^{[4]}H=v^{[4]}(s+u^4)w.
\]
Thus \(K K^{[1/4]}\) vanishes exactly when \(s=u^4\), equivalently \(c=0\), and \(b=0\) then gives \(a_2=a_6^5\). In this case \(\mathcal C^4\) has rank \(1\) and the displayed block products show \(\mathcal C^5=0\). If \(b=0,c\ne0\), the one-dimensional semilinear image of \(K\) persists under \(\mathcal C^2\); the ranks stabilize at \(2\) from the third iterate onward. These statements give all asserted rank sequences and stable \(2\)-ranks.

**Geometry and nonemptiness.** Since the squarefree condition defines an open subset of affine coefficient space, the equations \(a_3=a_6^4\), \(a_2=a_6^5\) cut out the intersection with the graph of a polynomial map \(\mathbb A^5\to\mathbb A^2\). It is therefore smooth and irreducible of codimension \(2\), provided nonempty. The intermediate rank hypersurface \(a_2=a_3a_6\) is similarly smooth, and its complement by the graph is open. Explicit squarefree witnesses for ranks \(4,2,0\) respectively are
\[
y^3=x^7+x^2+1,\qquad y^3=x^7+x^3+1,\qquad y^3=x^7+x+1.
\]
Their derivatives are respectively \(x^6\), \(x^6+x^2\), and \(x^6+1\), coprime to each displayed septic. Hence all three strata are nonempty.

## Verification
The self-contained Python program `verification/verify.py` uses exact field arithmetic and semilinear matrix composition; it needs no nonstandard packages. Run `python3 verification/verify.py`. Its full recorded output is `verification/output.txt`. It exhaustively checks all \(4^7\) monic septics over \(\mathbb F_4\), filtering precisely those that are squarefree, and verifies every predicted Cartier rank through the sixth iterate. Counts by \(2\)-rank are \(9216\) for rank four, \(2304\) for rank two, and \(768\) for rank zero. It also checks explicit \(\mathbb F_2\) witnesses and 898 exact tests over \(\mathbb F_8\), including nontrivial fourth-power coefficient conditions. These finite checks corroborate, but do not replace, the preceding algebraic proof for arbitrary \(k\).

## Relationship to prior work
Elkin [1, Theorem 3.4] gives a general Cartier-action formula for cyclic covers, while his Corollary 1.4 already proves that the first Cartier rank (and hence the \(a\)-number) in characteristic two depends only on the ramification type. Those general facts are not claimed here. The additional assertion is the **complete coefficient-level stable-rank stratification and all iterated Cartier ranks** for this genus-six \((3,7)\) model, with a smooth explicit codimension-two \(2\)-rank-zero locus. England [2, §2] studies precisely the genus-six \((3,7)\) polynomial family over \(\mathbb C\), with holomorphic differentials and abelian functions rather than characteristic-two Cartier strata. Özman–Pries–Weir [3, §§5–7] study cyclic triple-cover \(p\)-rank strata and the signature \((2,4)\), but their dimension theorems for that signature in §6 assume \(p\) is odd and do not give these characteristic-two equations or rank sequences. The algebraic computations here specialize classical Cartier formalism, and claims of historical priority remain subject to unlocated specialist literature.

## Limitations
This is a classification in the affine polynomial coefficient space, not an isomorphism classification in moduli. It does not determine Newton polygons beyond their \(2\)-rank, nor the full \(2\)-torsion group scheme. The first Cartier rank and the associated \(a\)-number are known from broader theory; only the explicit higher-iterate and rank-stratum classification is offered as additional information. The arithmetic verification is finite, while the proof applies to all algebraically closed characteristic-two fields.

## References
[1] Arsen Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431 (first posted 2007-08-02), especially Theorem 3.4 and Corollary 1.4. https://arxiv.org/abs/0708.0431

[2] Matthew England, *Higher Genus Abelian Functions Associated with Cyclic Trigonal Curves*, SIGMA 6 (2010), 025, arXiv:1003.4144 (first posted 2010-03-22), especially §2. https://sigma-journal.com/2010/025/

[3] Ekin Özman, Rachel Pries and Colin Weir, *The Boundary of the p-Rank 0 Stratum of the Moduli Space of Cyclic Covers of the Projective Line*, Nagoya Mathematical Journal 248 (2022), 865–887, DOI:10.1017/nmj.2022.12, especially §§5–7. https://doi.org/10.1017/nmj.2022.12
