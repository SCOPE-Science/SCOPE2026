# Cyclotomic adjoint-rank spectra of width-two quantum complete intersections over finite fields

## Finding
For every prime power \(q\), integer \(n\ge3\), and \(\lambda\in\mathbb F_q^\times\), put
\[
 A_{n,\lambda}=\mathbb F_q\langle x,y\rangle/(x^2,y^n,yx-\lambda xy).
\]
Write \(d=\operatorname{ord}(\lambda)\), with \(d=1\) when \(\lambda=1\), and define
\[
 S_d=\{i\in\{1,\ldots,n-1\}:d\nmid i\},\qquad
 H_d(m)=\begin{cases}m-\lfloor m/d\rfloor,&m>0,\\0,&m\le0.\end{cases}
\]
Every element has a unique form \(a=f(y)+xg(y)\), with \(f,g\in R=\mathbb F_q[y]/(y^n)\). Define \(s(a)\) to be the least \(i\in S_d\) with nonzero coefficient in \(f\), or \(n\) if there is none. Define \(t(a)\) to be the least exponent occurring in \(g\), or \(n\) if \(g=0\). Then its inner derivation satisfies
\[
 \boxed{\operatorname{rank}_{\mathbb F_q}(b\mapsto ab-ba)=n-s(a)+H_d(s(a)-t(a)-1).}
\]

For every integer \(r\), the exact number \(\mathcal N_{n,q,d}(r)\) of elements \(a\in A_{n,\lambda}\) whose inner derivation has rank \(r\) is
\[
 \boxed{\mathcal N_{n,q,d}(r)=
  \sum_{s\in S_d\cup\{n\}}\sum_{t=0}^{n}
   W_f(s)W_g(t)\,\mathbf1_{\{r=n-s+H_d(s-t-1)\}},}
\]
where
\[
 W_f(s)=\begin{cases}(q-1)q^{n-H_d(s)},&s\in S_d,\\q^{n-H_d(n-1)},&s=n,\end{cases}
 \quad W_g(t)=\begin{cases}(q-1)q^{n-t-1},&0\le t<n,\\1,&t=n.\end{cases}
\]
In particular the distribution depends only on the order \(d\), not the particular unit \(\lambda\) of that order; the element-centralizer dimension is \(2n-r\), and the exact ordered commuting-pair count and probability are respectively
\[
 \mathcal C_{n,q,d}=\sum_{r=0}^{n-1}\mathcal N_{n,q,d}(r)q^{2n-r},
 \qquad \operatorname{cp}(A_{n,\lambda})=q^{-4n}\mathcal C_{n,q,d}.
\]
When \(d\ge n\), the nonresonant case has the particularly simple universal spectrum
\[
 \boxed{\mathcal N(0)=q^2,\quad
 \mathcal N(r)=(q^2-1)q^{2r}\ (1\le r\le n-1),\quad
 \mathcal C=(q+1)q^{3n}-q^{2n+1}.}
\]
For \(d>1\), the center has \(\mathbb F_q\)-dimension \(2+\lfloor(n-1)/d\rfloor\). When \(d=1\), the algebra is commutative and all \(q^{2n}\) elements have rank zero. As a concrete resonance, for \(n=3\), \(d\ge3\) yields \(\operatorname{cp}=q^{-2}+q^{-3}-q^{-5}\), whereas \(d=2\) yields \(\operatorname{cp}=2q^{-2}-q^{-4}\). The latter case occurs only when \(q\) is odd.

## Assumptions and scope
The field is any finite field, including nonprime extensions and characteristic two. \(\lambda\) is nonzero and \(n\ge3\). The algebra is unital, of dimension \(2n\), and \(\operatorname{ad}_a\) is the ordinary linear commutator map on the whole algebra. Elements and commuting pairs are labeled; no quotient by automorphisms or conjugacy is taken. The numbers count actual finite-field elements rather than geometric or scheme-theoretic components. The special \(n=2\) family and its commuting-tuple locus were previously studied and are excluded from the claimed contribution.

## Proof
**Multiplication and commutator.** The relations give a basis \(1,y,\ldots,y^{n-1},x,xy,\ldots,xy^{n-1}\). If \(\sigma:R\to R\) is the automorphism \(\sigma(h(y))=h(\lambda y)\), then for \(f,g,h,j\in R\),
\[
 (f+xg)(h+xj)=fh+x\bigl(\sigma(f)j+gh\bigr).
\]
Thus with \(\delta=\sigma-\mathrm{id}\),
\[
 [f+xg,h+xj]=x\bigl(\delta(f)j-g\delta(h)\bigr).
\]
Consequently the commutator image, identified with a subspace of \(R\) via multiplication by \(x\), is exactly \(\delta(f)R+g\delta(R)\). This directly proves the bound \(0\le\operatorname{rank}(\operatorname{ad}_a)\le n-1\).

**Rank calculation.** Write \(f=\sum_{i=0}^{n-1}f_i y^i\). Because \(\delta(y^i)=(\lambda^i-1)y^i\), the image \(\delta(R)\) is the direct span of \(y^i\) with \(i\in S_d\). The ideal \(\delta(f)R\) is \(y^sR\) when \(s<n\), and is zero otherwise; in both cases it has dimension \(n-s\). If \(g\ne0\), write \(g=y^t u(y)\) with \(u\) a unit of \(R\). In \(R/y^sR\), the nonzero elements \(g\delta(y^i)\) are indexed by \(i\in S_d\) with \(i+t<s\). Their first nonzero monomials have pairwise distinct degrees \(i+t\), and multiplication by the fixed unit \(u\) is invertible. Hence they are linearly independent and their number is \(H_d(s-t-1)\). For \(g=0\), the same expression vanishes because \(t=n\). Adding the dimensions proves the boxed rank formula. In the commutative case \(d=1\), \(S_d\) is empty and the formula returns zero.

**Exact multiplicities.** To have \(s=i\in S_d\), each earlier index in \(S_d\) has a zero coefficient of \(f\), the coefficient \(f_i\) is any nonzero field element, and all other coefficients are arbitrary. There are \(H_d(i)-1\) earlier eligible indices, giving exactly \((q-1)q^{n-H_d(i)}\) choices. Having \(s=n\) forces every eligible coefficient to zero, giving \(q^{n-H_d(n-1)}\) choices. Similarly, the possible valuations \(t<n\) of \(g\) have \((q-1)q^{n-t-1}\) realizations, with one realization for \(t=n\). The choices of \(f\) and \(g\) are independent, so multiplying their counts and grouping by the rank expression proves the complete histogram. In particular \(\sum_r\mathcal N(r)=q^{2n}\) without omissions. For any \(a\), the kernel of its commutator map is its algebra centralizer, giving \(q^{2n-r}\) commuting partners. Summing gives \(\mathcal C\) and the stated probability.

**Nonresonant simplification and boundaries.** If \(d\ge n\), \(\delta(R)=yR\) and \(\delta(f)R=y^sR\) for the usual nonconstant coefficient valuation \(s\in\{1,\ldots,n\}\). The commutator image is the ideal \(y^{\min(s,t+1)}R\). The number of \((f,g)\) with \(s\ge m\) and \(t+1\ge m\) is \(q^{2(n-m+1)}\), for \(1\le m\le n\). The differences of successive filtration counts give \(\mathcal N(0)=q^2\) and \(\mathcal N(r)=(q^2-1)q^{2r}\) for \(1\le r<n\). Summing this geometric progression against \(q^{2n-r}\) gives \((q+1)q^{3n}-q^{2n+1}\). For \(d>1\), an element is central exactly when \(f_i=0\) for every \(i\in S_d\) and \(g\in y^{n-1}R\), giving center dimension \(2+\lfloor(n-1)/d\rfloor\). In the case \(n=3,d=2\), only \(i=1\) is eligible. Direct substitution into the histogram gives \(\mathcal N(0)=q^3\), \(\mathcal N(1)=(q^2-1)q^3\), and \(\mathcal N(2)=(q-1)q^5\), yielding \(2q^{-2}-q^{-4}\). All claims hold uniformly in characteristic.

## Verification
A standalone pure-Python verifier, `verify.py`, independently builds the algebra multiplication in its \(2n\)-element basis, computes the commutator linear map by multiplying each basis element in both orders, and performs finite-field Gaussian elimination. For each tested field, exponent, and twisting parameter, it exhaustively visits every algebra element, compares actual and predicted rank, and separately evaluates all predicted histogram weights. Tests include the extension field \(\mathbb F_4\), the identity parameter, resonant order two, nonresonant order at least the exponent, and order-three resonance. The independent small-instance checks corroborate but cannot substitute for the unrestricted algebraic proof.

## Relationship to prior work
Quantum complete intersections have well-established presentations and Hochschild-theoretic classifications. Bergh--Erdmann establish a codimension-two bimodule resolution and Hochschild (co)homology results; their degree-zero cohomology already contains center information. Bergh--Oppermann study representation dimension, and Oppermann later gives a general graded Hochschild basis, again encompassing degree-zero center calculations. The present claim is the full **elementwise commutator-rank histogram** and the resulting **exact finite-field pairwise commuting count** throughout the width-two exponent family, not merely the center dimension or a Hochschild invariant. A previously established dimension-four \(n=2\) commuting-tuple result is excluded. Work on commuting pairs for distinct radical-square-zero path algebras or adjoint-rank spectra for Lie algebras does not imply the quantum-complete-intersection histogram. Equivalent accounts through Ore extensions, centralizer distributions, or commutator-word maps are conceivable priority risks; no global uniqueness theorem is asserted.

## Limitations
Only the exponent pair \((2,n)\) and invertible twist \(\lambda\) are covered. The formula counts algebra elements, not unit-group conjugacy classes or isomorphism types, and proves no statement about the geometry of a commuting scheme. Its degree-zero/center subresult has antecedents in Hochschild cohomology. The proof establishes mathematical formulas for all specified finite fields; computation verifies only finite examples. No independent audit or exhaustive literature-priority guarantee is claimed.

## References
1. P. A. Bergh and K. Erdmann, *\(\mathrm{(Co)homology}\) of quantum complete intersections*, arXiv:0709.3029v1 (public 19 September 2007), https://arxiv.org/abs/0709.3029.
2. P. A. Bergh and S. Oppermann, *The representation dimension of quantum complete intersections*, arXiv:0710.2606v1 (public October 2007), https://arxiv.org/abs/0710.2606.
3. S. Oppermann, *Hochschild cohomology and homology of quantum complete intersections*, Algebra & Number Theory 4 (2010), 821--837, https://msp.org/ant/2010/4-7/ant-v4-n7-p01-p.pdf.
