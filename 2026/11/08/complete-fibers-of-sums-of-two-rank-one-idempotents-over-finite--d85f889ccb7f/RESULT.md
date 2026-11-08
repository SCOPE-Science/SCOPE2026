# Complete fibers of sums of two rank-one idempotents over finite fields

## Finding

Let \(k=\mathbb F_q\) be any finite field, let \(n\geq2\), and let \(\mathcal P_n(k)\) be the set of rank-one idempotent matrices in \(M_n(k)\). For every target \(C\in M_n(k)\), put
\[
F(C)=\#\{(P,Q)\in\mathcal P_n(k)^2:P+Q=C\},\qquad
L_n=q^{n-1}\frac{q^n-1}{q-1}.
\]
All ordered target fibers are given by the following exhaustive rules.

1. If \(\operatorname{rank}C>2\), or \(\operatorname{tr}C\ne 2\) in \(k\), then \(F(C)=0\).
2. If \(C=0\), then \(F(C)=L_n\) in characteristic two, and \(F(C)=0\) otherwise.
3. If \(\operatorname{rank}C=1\) and \(\operatorname{tr}C=2\) in \(k\), then
\[
F(C)=\begin{cases}2q^{n-1},&\operatorname{char}k=2,\\2q^{n-1}-1,&\operatorname{char}k\ne2.\end{cases}
\]
4. If \(\operatorname{rank}C=2\) and \(\operatorname{tr}C=2\) in \(k\), set \(W=\operatorname{im}C\) and \(M=C|_W:W\to W\). Let \(e(M)\) be the number of \(k\)-rational \(M\)-invariant lines of \(W\), and \(e_1(M)\) the number of these on which \(M\) acts as the identity. Then
\[
F(C)=\begin{cases}
q(q+1),&M=I_W,\\
0,&M=\lambda I_W\text{ with }\lambda\ne1,\\
q+1-e(M)+q e_1(M),&M\text{ nonscalar}.
\end{cases}
\]
The first two scalar alternatives are exclusive, and \(e(M),e_1(M)\) are genuine rational-line counts, not algebraic-closure eigenvalue multiplicities.

As a second part of the same complete census, the exact numbers of ordered pairs with sum-rank two, one, and zero are
\[
\begin{aligned}
N_2&=L_n\bigl(L_n-2q^{n-1}+1\bigr),\\
N_1&=\begin{cases}L_n\bigl(2q^{n-1}-2\bigr),&\operatorname{char}k=2,\\ L_n\bigl(2q^{n-1}-1\bigr),&\operatorname{char}k\ne2,\end{cases}\\
N_0&=\begin{cases}L_n,&\operatorname{char}k=2,\\0,&\operatorname{char}k\ne2.\end{cases}
\end{aligned}
\]
Their sum is \(L_n^2\). Thus the rank-two probability has the same expression in every characteristic, while characteristic two transfers exactly \(L_n\) ordered pairs from sum-rank one to sum-rank zero.

For odd \(q\), every rank-one or rank-two target of trace \(2\) is representable. For even \(q\), all rank-one targets of trace zero are representable, while among rank-two trace-zero targets the *only* obstruction is \(M=\lambda I_W\) with \(\lambda\ne1\). In particular, this obstruction can occur even when the ambient target is nilpotent (\(M=0\), possible for \(n\ge4\)).

## Assumptions and scope

All counts concern ordered pairs of **rank exactly one** idempotents, not unrestricted idempotents, orthogonal projections in an inner-product sense, or unordered decompositions. Field characteristic and extension degree are unrestricted. The matrix dimension satisfies \(n\ge2\), while the restricted operator \(M\) in the rank-two case acts on a two-dimensional space. All equalities of traces and scalar constants such as \(2\) are interpreted inside the field.

## Proof

**Step 1: rank-one idempotents.** Every rank-one matrix has the form \(u\varphi\), where \(u\in k^n\) is a nonzero column and \(\varphi\in(k^n)^*\) is a row. It is idempotent precisely when \(\varphi(u)=1\). For each of the \((q^n-1)/(q-1)\) image lines, fixing one nonzero representative leaves \(q^{n-1}\) admissible rows. Therefore \(\#\mathcal P_n(k)=L_n\). Every two summands have trace one and rank one, proving the stated necessary conditions.

**Step 2: zero target.** The equation \(P+Q=0\) forces \(Q=-P\). If \(P\ne0\) is idempotent, then \(-P\) is idempotent if and only if \(1=-1\) in \(k\). This proves the zero-fiber formula.

**Step 3: nonzero rank-one target.** Fix a rank-one factorization \(C=z\gamma\) and suppose \(\gamma(z)=\operatorname{tr}C=2\). For any representation \(C=P+Q\), either the image lines of \(P,Q\) coincide or their row spaces coincide. Indeed, writing \(P=u\alpha\) and \(Q=v\beta\), the product factorization \([u\ v]\begin{bmatrix}\alpha\\\beta\end{bmatrix}\) has rank two if both displayed factors have rank two; hence target rank one forces one factor to have rank one.

If the two image lines coincide, they both equal \(kz\). Write \(P=z\varphi\), \(Q=z(\gamma-\varphi)\); both are idempotent precisely when \(\varphi(z)=1\), giving \(q^{n-1}\) solutions. If the two row spaces coincide, both equal \(k\gamma\), and all solutions have \(P=u\gamma\), \(Q=(z-u)\gamma\) with \(\gamma(u)=1\), again \(q^{n-1}\) solutions. In odd characteristic, the two families intersect exactly at \(P=Q=C/2\), which is a rank-one idempotent because \(C^2=2C\). In characteristic two, their intersection is empty: any nonzero rank-one scalar multiple of \(C\) is square-zero, not idempotent. Inclusion–exclusion yields both formulas.

**Step 4: rank-two target.** If \(C=P+Q\) has rank two, the image lines \(\operatorname{im}P\) and \(\operatorname{im}Q\) are distinct and span \(W=\operatorname{im}C\). Thus there is a unique rank-one projector \(T:W\to W\) onto \(\operatorname{im}P\) along \(\operatorname{im}Q\), and \(P=TC\), \(Q=(I_W-T)C\). Conversely, any such \(T\) produces nonzero rank-one maps \(P,Q\) summing to \(C\), because \(C:k^n\to W\) is surjective. Write \(T=u\varphi\) on \(W\), with \(\varphi(u)=1\). The map \(P=TC\) is idempotent if and only if \(\varphi(Mu)=1\). As \(\operatorname{tr}M=\operatorname{tr}C=2\), this same equality makes \(Q=(I_W-T)C\) idempotent: the scalar trace of its rank-one image is \(\operatorname{tr}M-\varphi(Mu)=1\).

Now count projectors \(T\) by their image line \(ku\). If it is not \(M\)-invariant, the vectors \(u,Mu\) form a basis and the conditions \(\varphi(u)=\varphi(Mu)=1\) determine exactly one row. There are \(q+1-e(M)\) such lines. If \(Mu=\lambda u\), the two conditions are compatible if and only if \(\lambda=1\); in that case there are \(q\) admissible rows. This gives \(q+1-e(M)+q e_1(M)\) for nonscalar \(M\). For a scalar \(M=\lambda I_W\), all \(q+1\) lines are invariant; the condition is soluble for every rank-one projector if \(\lambda=1\), and never otherwise. This completes the target-by-target law.

**Step 5: global rank spectrum.** Fix one rank-one idempotent \(P=u\varphi\). Among the \(L_n\) rank-one idempotents \(Q\), exactly \(q^{n-1}\) have the same image line as \(P\), and exactly \(q^{n-1}\) have the same row line as \(P\). These two sets intersect exactly at \(Q=P\). The sum \(P+Q\) has rank less than two exactly on their union (by the factorization in Step 3). Hence \(L_n-2q^{n-1}+1\) choices produce rank two, proving \(N_2\). The zero-sum classification in Step 2 determines \(N_0\); subtraction yields \(N_1\). This proves the mass identity without relying on finite experiments.

**Step 6: representability.** For a nonscalar two-dimensional \(M\), \(e(M)\le2\), so \(q+1-e(M)+q e_1(M)\ge q-1>0\). For scalar rank-two targets the preceding classification is exact. When the characteristic is odd, trace \(M=2\) and scalarity force \(M=I_W\); when the characteristic is two, any scalar restriction has trace zero. The asserted boundary cases follow.

## Verification

The proof applies to all finite prime-power fields and all \(n\ge2\). Independent direct code enumerates rank-one idempotents via outer products and counts *every* ordered sum and *every* target for \((n,q)=(2,2),(2,3),(2,5),(2,7),(3,2),(3,3),(4,2)\). Across these cases, the code checks target fibers for a total of \(88{,}854\) targets and checks the full total-mass identity in each case. An additional independent extension-field implementation checks all \(256\) targets of \(M_2(\mathbb F_4)\). Both verification scripts are provided with their exact outputs. These finite checks corroborate but do not replace the unrestricted proof.

## Relationship to prior work

De Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field* (first publicly posted 2009-07-25, arXiv:0907.4436), characterizes which matrices are sums or prescribed linear combinations of two unrestricted idempotents using Jordan blocks and invariant factors. De Seguins Pazzis, *On sums of idempotent matrices over a field of positive characteristic* (first posted 2009-07-30, arXiv:0907.5360), studies representability and minimum numbers of unrestricted summands. The 2011 paper *Sums of two triangularizable quadratic matrices over an arbitrary field* (arXiv:1109.2255) treats existence for broader quadratic-sum classes. Those results are credited; none of the inspected statements supplies this rank-one-constrained **ordered fiber count**. In particular, an existence classification does not give the number of pairs with a prescribed sum. The present projective-line count is a distinct, more quantitative question. Unidentified prior convolution formulas for conjugacy classes of idempotents could potentially imply the result; exhaustive historical priority is not certified.

## Limitations

The summands must both be rank-one idempotents. The result says nothing about sums with higher prescribed idempotent ranks, sums over general finite rings, or decompositions modulo conjugation. Priority is provisional; independent validation has not been performed. The finite examples do not constitute proofs of the unrestricted formulas.

## References

1. C. de Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field*, arXiv:0907.4436, first posted 2009-07-25, published in Linear Algebra and its Applications 433 (2010), 625–636.
2. C. de Seguins Pazzis, *On sums of idempotent matrices over a field of positive characteristic*, arXiv:0907.5360, first posted 2009-07-30.
3. C. de Seguins Pazzis, *Sums of two triangularizable quadratic matrices over an arbitrary field*, arXiv:1109.2255, first posted 2011-09-10.
