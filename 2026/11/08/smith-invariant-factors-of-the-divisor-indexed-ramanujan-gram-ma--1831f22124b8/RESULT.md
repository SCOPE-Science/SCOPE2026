# Smith invariant factors of the divisor-indexed Ramanujan Gram matrix

## Finding

For every positive integer \(n\), enumerate its positive divisors in any common order and form the integer matrix
\[
 C_n=(c_d(t))_{d,t\mid n},\qquad
 c_d(t)=\sum_{e\mid\gcd(d,t)}e\,\mu(d/e),\qquad G_n=C_nC_n^{\mathsf T}.
\]
The complete Smith normal form of \(G_n\) is given by a prime-power scanning rule. Write \(n=\prod_{p\mid n}p^{a_p}\), and let \(r=\tau(n)=\prod_{p\mid n}(a_p+1)\). For each prime \(p\mid n\), construct a nondecreasing list \(E(p,a_p)\) of \(a_p+1\) exponents by scanning the integers \(i=0,1,\ldots,a_p\) from left to right:

- If \(p\mid(a_p-i+1)\), output \(2i+1\) **twice** and advance \(i\) by two.
- Otherwise output \(2i\) once and advance \(i\) by one.

The first case never arises at \(i=a_p\), so the rule is well defined. Repeat every entry of \(E(p,a_p)\) exactly \(r/(a_p+1)\) times, then sort the expanded list to obtain \(e_{p,1}\le\cdots\le e_{p,r}\). The invariant factors are precisely
\[
 \boxed{d_j=\prod_{p\mid n}p^{e_{p,j}}\quad(1\le j\le r)},
 \qquad d_j\mid d_{j+1}.
\]
The product of the empty family when \(n=1\) is one, yielding \(G_1=(1)\). Consequently the finite abelian group \(\mathbb Z^r/G_n\mathbb Z^r\) is isomorphic to \(\bigoplus_{j=1}^{r}\mathbb Z/d_j\mathbb Z\).

The theorem yields three exact structural consequences:
\[
 \boxed{|\det G_n|=n^{\tau(n)}},\qquad
 \boxed{\operatorname{exp}(\operatorname{coker}G_n)=
 \begin{cases}n^2,&n\text{ odd},\\ n^2/2,&n\text{ even},\end{cases}}
\]
and, for every \(p^{a}\parallel n\),
\[
 \boxed{\operatorname{rank}_{\mathbb F_p}(G_n\bmod p)
 =\begin{cases}0,&p\mid(a+1),\\ \tau(n)/(a+1),&p\nmid(a+1).\end{cases}}
\]
For instance, at \(n=16\) the invariant factors are \(1,8,8,128,128\); at \(n=625\) they are \(5,5,625,15625,390625\); and at \(n=12\) they are \(1,1,8,72,72,72\).

## Assumptions and scope

All matrices are over \(\mathbb Z\); their Smith forms use positive invariant factors. Here \(\mu\) is the ordinary Möbius function, \(\tau\) is the divisor-counting function, and \(p^a\parallel n\) means that \(a\ge1\) is the exact exponent of \(p\) in \(n\). Both the row and column indexing sets contain **all** positive divisors, including one and \(n\). The Gram form is **unweighted**: there are no Euler-totient weights in the sum over the columns. Reordering divisors changes neither the asserted Smith factors nor the cokernel.

## Proof

**Divisor incidence reduction.** Order the divisors of \(n\) compatibly with divisibility. Let \(Z_{t,e}=\mathbf1_{e\mid t}\), let \(M_{d,e}=\mu(d/e)\mathbf1_{e\mid d}\), and let \(D\) be the diagonal matrix with diagonal entries \(e\), indexed by divisors. The classical Ramanujan identity gives
\[
 C_n=M D Z^{\mathsf T}.
\]
Both \(M\) and \(Z\) are unitriangular integer matrices and hence unimodular. Accordingly \(G_n\) is integrally equivalent to \(D(Z^{\mathsf T}Z)D\). This is **not** the ordinary Smith form of \(C_n\); the unweighted middle factor is essential.

**Prime-power core.** For \(n=p^a\), index rows and columns by \(i,j=0,\ldots,a\) corresponding to divisors \(p^i\). Then
\[
 D=\operatorname{diag}(1,p,\ldots,p^a),\qquad
 U_{ij}:=(Z^{\mathsf T}Z)_{ij}=a-\max(i,j)+1.
\]
Thus the required elementary divisors over the discrete valuation ring \(\mathbb Z_p\) are those of \(B=DUD\). The leading \(i\)-by-\(i\) principal minor of \(U\), for \(1\le i\le a+1\), has determinant \(a-i+2\). This follows by successive differences between neighboring rows and columns.

**Local pivot lemma.** Suppose indices \(0,\ldots,i-1\) have been eliminated in singleton or adjacent-pair blocks, and their corresponding leading block of \(U\) is invertible over \(\mathbb Z_p\). For \(i\ge1\) put \(L=a-i+2\); by the induction this denominator is a \(p\)-adic unit. Direct Schur complementation gives, for \(j,k\ge i\),
\[
 R_i(j,k)=a-\max(j,k)+1-
 \frac{(a-j+1)(a-k+1)}{L}.
\]
For \(i=0\), simply take \(R_0=U\). In particular, for \(i\ge1\),
\[
 R_i(i,i)=\frac{a-i+1}{L},\qquad
 R_i(i,i+1)=\frac{a-i}{L},\qquad
 \det R_i[\{i,i+1\}]=\frac{a-i}{L}.
\]
At \(i=0\), the corresponding three values are \(a+1\), \(a\), and \(a\).

If \(p\nmid(a-i+1)\), the first diagonal entry of the weighted residual \(D_{\ge i}R_iD_{\ge i}\) is exactly \(p^{2i}\) times a unit. Its cross entries with later indices are divisible by \(p^{2i+1}\); integral row and column operations split a singleton factor \(p^{2i}\), then proceed to \(i+1\). The enlarged leading \(U\)-minor is a \(p\)-adic unit, as required for the induction.

If \(p\mid(a-i+1)\), then \(i<a\), the adjacent off-diagonal entry \(R_i(i,i+1)\) is a \(p\)-adic unit, and the two-by-two \(R_i\)-block has unit determinant. After the weights \(p^i,p^{i+1}\), every entry of this block is divisible by \(p^{2i+1}\), while its quotient by \(p^{2i+1}\) has determinant a unit. Thus its Smith elementary divisors are **both** \(p^{2i+1}\). More explicitly, the quotient has a unit off-diagonal entry and a bottom-right entry divisible by \(p\), so its determinant is a unit even if the top-left entry is not. For any later index \(j\ge i+2\), multiplication of the weighted cross-block by the inverse of this two-by-two block has \(p\)-integral entries, since its factors include \(p^{j-i}\) and \(p^{j-i-1}\). Thus unimodular operations split off the pair, and the residual Schur complement is the one for \(i+2\). The new leading principal minor of \(U\) is a unit because \(a-i\equiv-1\pmod p\).

The two alternatives exhaust all indices and never create a pair beyond \(a\). Hence the local scan gives all \(a+1\) elementary divisors. Because \(2i+1<2(i+2)\), the output list is already nondecreasing.

**Passage to general moduli.** Ramanujan sums are multiplicative in coprime moduli. With compatible divisor indexing, \(C_n\) and \(G_n\) are, up to row and column permutations, respectively the tensor products of \(C_{p^{a_p}}\) and \(G_{p^{a_p}}\). Localizing at a fixed \(p\), every other prime-power Gram factor is invertible over \(\mathbb Z_p\), so each local exponent appears \(\prod_{q\mid n,q\ne p}(a_q+1)=r/(a_p+1)\) times. The classification of Smith forms by valuations of their invariant factors yields the stated global product formula.

**Consequences.** The determinant of the prime-power core is the square of \(\prod_{i=0}^a p^i\), namely \(p^{a(a+1)}\). Tensor products then give \(|\det G_n|=n^r\). For odd \(p\), the last index \(i=a\) is a singleton with exponent \(2a\). For \(p=2\), the last two indices always form a pair with exponent \(2a-1\), so the largest invariant factor is \(n^2\) if \(n\) is odd and \(n^2/2\) otherwise. Finally, the local list has one zero exponent precisely when \(p\nmid(a+1)\), and none otherwise, proving the modular rank formula.

## Verification

The accompanying `verify.py` uses only the Python standard library. It builds the Ramanujan matrix from the Möbius-divisor formula, independently determines the Smith factors through gcds of **all** square minors using exact fraction-free determinants for 27 test moduli, and compares them against the theorem's scan. It separately checks the determinant, cokernel exponent and ranks modulo every prime divisor. Running `python3 verify.py` on the checked package prints:

`VERIFY_OK cases=27 determinant_minors=22203 independent_smith=PASS determinant=PASS cokernel_exponent=PASS modular_ranks=PASS`

The exhaustive minor checks are finite evidence only; the uniform result for every positive integer \(n\) follows from the proof above.

## Relationship to prior work

Ramanujan's divisor formula and its Möbius inversion are classical; see Tóth (2010). Fowler, Garcia and Karaali (2012/2013) identify the divisor-indexed Ramanujan supercharacter table, its Kronecker factorization, its weighted orthogonality and the identity \(S_n^2=nI\). With a permutation of the columns, this is the table \(C_n\) used here. Their weighted orthogonality does **not** give the Smith form of the unweighted integer Gram matrix: weights are generally nonunits over \(\mathbb Z_p\). Schlage-Puchta (2021) computes \(|\det C_n|=n^{\tau(n)/2}\), and hence the already-known determinant of its Gram matrix; that determinant does not identify its individual invariant factors. The presently determined prime-power pair transitions, integral cokernel and modular rank collapse are additional arithmetic data. No claim is made that ordinary Ramanujan formulas, tensor factorization, the weighted orthogonality, or the determinant are new.

## Limitations

The theorem concerns only the unweighted Gram matrix of the square divisor-indexed table, not a Gram matrix indexed by all residues modulo \(n\), nor a differently weighted superclass inner product. The literature comparison did not locate an equivalent integral Smith classification, but the absence of a search result cannot certify historical uniqueness. No independent external mathematical audit has been conducted.

## References

- L. Tóth, *Some remarks on Ramanujan sums and cyclotomic polynomials*, arXiv:1002.3221v1, submitted 17 February 2010; Bull. Math. Soc. Sci. Math. Roumanie 53 (2010), 277–292. https://arxiv.org/abs/1002.3221
- C. F. Fowler, S. R. Garcia, and G. Karaali, *Ramanujan sums as supercharacters*, arXiv:1201.1060v1, submitted 5 January 2012; Ramanujan Journal (2013). https://arxiv.org/abs/1201.1060
- J.-C. Schlage-Puchta, *A determinant involving Ramanujan sums and So's conjecture*, Archiv der Mathematik 117 (2021), 379–384, DOI:10.1007/s00013-021-01643-8. https://doi.org/10.1007/s00013-021-01643-8
