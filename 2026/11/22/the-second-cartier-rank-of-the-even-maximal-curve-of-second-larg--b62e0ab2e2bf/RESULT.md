# The second Cartier rank of the even maximal curve of second-largest genus

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(q=2^n\) with \(n\ge3\). Put \(r=q/2\), and let \(C_q\) be the smooth projective model of
\[
 y^{q+1}=x+x^2+x^4+\cdots+x^{q/2}.
\]
Write \(\mathcal C\) for the Cartier operator on \(H^0(C_q,\Omega^1)\). Its **second-iterate rank** is
\[
\boxed{\operatorname{rank}(\mathcal C^2)=\frac{9q^2}{64}-\frac{5q}{8}}.
\]
Equivalently, the dimension of \(\ker(\mathcal C^2)\) is
\[
 \frac{7q^2}{64}+\frac{q}{8}.
\]
This distinguishes a second step of the Cartier filtration beyond the previously calculated \(a\)-number. No claim concerning all higher iterates or a full Ekedahl–Oort classification is made.

## Assumptions and scope
Work over an algebraically closed field of characteristic \(2\). Set \(r=2^{n-1}\), \(m=2r+1\),
\[
 L(X)=\sum_{a=0}^{n-1}X^{2^a},\qquad T(X)=\sum_{a=0}^{n-2}X^{2^a},
 \qquad L(X)=X+T(X)^2.
\]
Here \(r\) is divisible by \(4\). The function field is \(k(x,y)\) subject to \(L(x)=y^m\). The affine curve is smooth because \(L'(x)=1\). It has a unique point \(P_\infty\) at infinity with
\[
 v_\infty(x)=-m,\qquad v_\infty(y)=-r.
\]
The genus is \(g=r(r-1)=q(q-2)/4\). All ranks refer to the Cartier operator on **holomorphic differentials**, not the matrix rank of Frobenius acting on an arbitrarily chosen larger ambient space. Semilinearity is harmless for ranks over a perfect field.

## Proof
### The canonical differential basis
The morphism \(y:C_q\to\mathbb P^1\) has separable degree \(r\): \(L(X)-y^m\) has derivative \(1\), while at infinity the valuation of a root over \(k(y)\), normalized by \(v(y)=-1\), is \(-m/r\); coprimality of \(m\) and \(r\) forces ramification index \(r\), proving irreducibility and unique total ramification over infinity. Its Galois group is translation \(x\mapsto x+a\) for \(a\in\ker L\), of order \(r\). The cover is unramified at finite points because \(L'(x)=1\). At infinity the element \(u=y^2/x\) is a uniformizer, since \(v_\infty(u)=m-2r=1\). For any nonzero \(a\in\ker L\),
\[
 v_\infty\bigl(\sigma_a(u)-u\bigr)
 =v_\infty\left(\frac{a y^2}{x(x+a)}\right)=2m-2r=m+1.
\]
The local different exponent is therefore \((r-1)(m+1)\), and Riemann–Hurwitz gives
\[
 2g-2=-2r+(r-1)(m+1)=2r(r-1)-2.
\]
Consequently \(\operatorname{div}(dy)=(2g-2)P_\infty\). The following are holomorphic and have distinct pole-order labels:
\[
 \omega_{i,j}=x^i y^jdy,\qquad
 j\in\{2h,2h+1\},\quad0\le h\le r-2,\quad
 0\le i<N_h:=r-1-h.
\]
Indeed \(mi+rj\le2g-2\) is precisely the displayed range. For \(0\le i<r\), equality of two pole-order labels forces equality of both indices (reduce modulo \(r\)). There are \(2\sum_{h=0}^{r-2}(r-1-h)=r(r-1)=g\) monomials, so these form a basis.

### Cartier action in the basis
Differentiating \(L(x)=y^m\), using \(L'(x)=m=1\) in characteristic \(2\), yields \(dx=y^{m-1}dy\). The separating variable \(y\) permits the usual rule
\[
 \mathcal C\bigl((A^2+yB^2)dy\bigr)=Bdy.
\]
Substituting \(x=y^m+T(x)^2\) gives the following exact four-case action for all admissible \((i,j)\):
\[
\mathcal C(x^iy^jdy)=
\begin{cases}
 0 & i,j\text{ both even},\\
 x^{i/2}y^{(j-1)/2}dy & i\text{ even},\ j\text{ odd},\\
 x^{(i-1)/2}y^{r+j/2}dy & i\text{ odd},\ j\text{ even},\\
 x^{(i-1)/2}T(x)y^{(j-1)/2}dy & i,j\text{ both odd}.
\end{cases}
\]
For fixed \(j=2h\) the first image, if nonzero, has \(y\)-degree \(r+h\); for \(j=2h+1\) it has \(y\)-degree \(h\). As these degrees are pairwise distinct over the two collections whenever the first image is nonzero, their contributions to the rank of the second iterate can be counted separately.

### A low-degree injectivity lemma
For every polynomial \(P(x)\) with \(\deg P<r\), write uniquely
\[
 P(x)=E(x)^2+xO(x)^2.
\]
For an odd nonnegative integer \(j'\), the preceding formula, extended linearly, gives
\[
 \mathcal C(P(x)y^{j'}dy)
  =(E(x)+T(x)O(x))y^{(j'-1)/2}dy.
\]
If this is zero, then \(E=TO\) and \(P=(T^2+x)O^2=L(x)O^2\). Since \(\deg L=r\), this forces \(P=0\). Thus **Cartier is injective on each subspace of \(x\)-degree less than \(r\) at odd fixed \(y\)-degree**. At even fixed \(y\)-degree, Cartier retains precisely the odd-degree part \(xO(x)^2\), sending it to \(O(x)y^{r+j'/2}dy\).

### Rank contribution for each paired \(y\)-degree
Fix \(0\le h\le r-2\) and put \(N=N_h=r-1-h\), \(e=\lceil N/2\rceil\), and \(o=\lfloor N/2\rfloor\).

For the input degree \(j=2h\), the first image is spanned by \(x^a y^{r+h}dy\) for \(0\le a<o\). If \(h\) is even, the target \(y\)-degree is even, leaving \(\lfloor N/4\rfloor\) independent terms upon another application of Cartier. If \(h\) is odd, the target degree is odd and the injectivity lemma gives \(\lfloor N/2\rfloor\) independent terms.

For the input degree \(j=2h+1\), the first image is spanned by
\[
 \{x^a y^hdy:0\le a<e\}\ \cup\
 \{x^aT(x)y^hdy:0\le a<o\}.
\]
These \(N\) elements are independent because the first family has degree below \(r/2\) and the second has distinct highest degrees at least \(r/2\), all below \(r\). If \(h\) is odd, the injectivity lemma gives second-iterate rank \(N\). If \(h\) is even, then \(N\) is odd and \(e=o+1\). Cartier retains the odd-degree parts of these polynomials. The plain monomials give \(\lfloor e/2\rfloor\) terms. For even \(a\), the odd part of \(x^aT(x)\) is \(x^{a+1}\), already present among the plain monomials. For odd \(a\), the odd part has distinct leading degree \(a+r/2\) outside their span. Thus these contribute \(\lfloor o/2\rfloor\) further independent terms.

Consequently, the two input degrees together contribute the following rank:
\[
 R_h=\begin{cases}
 \lfloor N/4\rfloor+\lfloor\lceil N/2\rceil/2\rfloor
               +\lfloor\lfloor N/2\rfloor/2\rfloor,&h\text{ even},\\
 \lfloor N/2\rfloor+N,&h\text{ odd}.
 \end{cases}
\]
The output \(y\)-degrees after the second Cartier step are distinct for different nonzero input branches, since the first-step \(y\)-degree map is injective and the second-step map is injective on the parity-indexed degrees. Thus their ranks add.

### Evaluation of the finite sum
Write \(r=4K\). For \(h=4t+s\), \(0\le s\le3\), set \(u=K-t\). If \(u\ge2\), the values of \(R_h\) for \(s=0,1,2,3\) are respectively
\[
 3u-2,\quad6u-3,\quad3u-3,\quad6u-6,
\]
whose sum is \(18u-14\). For \(u=1\), the allowed values \(s=0,1,2\) contribute \(1+3+0=4\). Hence
\[
 \operatorname{rank}(\mathcal C^2)
 =4+\sum_{u=2}^{K}(18u-14)
 =9K^2-5K
 =\frac{9r^2}{16}-\frac{5r}{4}
 =\frac{9q^2}{64}-\frac{5q}{8},
\]
as asserted.

## Verification
The accompanying standalone script `check_cartier.py` constructs the entire holomorphic monomial basis, computes each first Cartier image using binary exact arithmetic, squares the resulting matrix, and obtains ranks by Gaussian elimination over \(\mathbb F_2\). Its checked cases are

| \(q\) | Genus | \(\operatorname{rk}\mathcal C\) | \(\operatorname{rk}\mathcal C^2\) |
|---:|---:|---:|---:|
| 8 | 12 | 8 | 4 |
| 16 | 56 | 40 | 26 |
| 32 | 240 | 176 | 124 |
| 64 | 992 | 736 | 536 |

The script is a finite consistency check; the preceding argument proves the formula for every \(n\ge3\). The first-rank values match the published \(a\)-number \(q^2/16\), because \(\operatorname{rk}\mathcal C=g-a\).

## Relationship to prior work
Higashine (2026) studies the same characteristic-two maximal curve and its Galois lines in the Frobenius embedding, recording its equation and genus, but does not calculate the Cartier filtration. Nourozi, Tafazolian, and Rahmati (2021, Theorem 4.1) compute the **\(a\)-number** \(q^2/16\) of the same curve, which determines only the first Cartier rank; that fact is prior work, not new here. Almeida Filho, Tafazolian, and Vieira (2026) determine higher Cartier ranks of **odd-characteristic** van der Geer–van der Vlugt Artin–Schreier curves, a different family and a different covering map. Pries and Weir (2015) treat Hermitian curves rather than this lower-genus quotient. The second-iterate formula here is not a formal consequence of those single-rank or different-family results. An equivalent unpublished or unindexed calculation could nevertheless exist.

## Limitations
The theorem describes one further Cartier rank only; it does not determine all iterates or the full isomorphism class of the Jacobian's \(2\)-torsion group scheme. The case \(q=4\) is excluded from the formula. The novelty comparison is limited to accessible primary sources, searchable databases, and source-specific checks, not a proof of publication priority. The author's 2021 dissertation on Cartier ranks was identified bibliographically but a full accessible text was not established, so this remains a specific priority risk. Independent verification of the mathematical argument has not been performed.

## References
1. K. Higashine, *Galois lines for the maximal curve with the second largest genus in characteristic two*, arXiv:2611.08810v1 (first submitted 2026-11-06). https://arxiv.org/html/2611.08810v1
2. V. Nourozi, S. Tafazolian, and F. Rahmati, *The a-number of Jacobians of certain maximal curves*, Transactions on Combinatorics **10** (2021), 121–128, Theorem 4.1. https://doi.org/10.22108/toc.2021.124678.1758
3. G. B. Almeida Filho, S. Tafazolian, and S. C. Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves*, arXiv:2610.17476v1 (2026). https://arxiv.org/abs/2610.17476
4. R. Pries and C. Weir, *The Ekedahl–Oort type of Jacobians of Hermitian curves*, Asian Journal of Mathematics **19** (2015), 845–869.
