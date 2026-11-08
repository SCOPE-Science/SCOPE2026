# Characteristic-two Rota–Baxter index jump and sharp finite-field counts on square-zero local algebras

## Finding

Let \(k\) be a field and \(A=k\oplus V\) the split unital commutative algebra whose ideal \(V\) has square zero. The weight-zero Rota–Baxter equation is
\[
P(x)P(y)=P\bigl(P(x)y+xP(y)\bigr)\qquad(x,y\in A).
\]
Every \(k\)-linear solution, and no other map, has the form
\[
P(a+v)=a u+L(v),\qquad u\in V,\quad L\in\operatorname{End}_k(V),\quad L^2=0,\quad 2Lu=0.
\tag{1}
\]
Consequently, if \(\operatorname{char}k=2\) then \(P^3=0\) always, while \(P^2\) may be nonzero when \(\dim V\ge2\). If \(\operatorname{char}k\ne2\), then every such \(P\) has \(P^2=0\). Thus the maximal nilpotency index of weight-zero Rota–Baxter operators is \(3\) in characteristic two for \(\dim V\ge2\), and \(2\) in other characteristics for \(\dim V\ge1\); when \(\dim V=1\) the index is \(2\) in every characteristic.

For an even prime power \(q\), put \(d=\dim_{\mathbb F_q}V\ge1\), and for \(0\le r\le\lfloor d/2\rfloor\) define
\[
N_{d,r}(q)=\binom{d}{r}_q\binom{d-r}{r}_q\lvert\operatorname{GL}_r(\mathbb F_q)\rvert
=q^{2r(d-r)}\frac{Q_d(q)}{Q_r(q)Q_{d-2r}(q)},\qquad
Q_j(q)=\prod_{i=1}^{j}(1-q^{-i}),\quad Q_0(q)=1.
\tag{2}
\]
There are exactly
\[
\boxed{\#\operatorname{RB}_0(A)=q^d\sum_{r=0}^{\lfloor d/2\rfloor}N_{d,r}(q)}
\tag{3}
\]
weight-zero Rota–Baxter operators and exactly
\[
\boxed{\#\{P:P^2\ne0\}=\sum_{r=0}^{\lfloor d/2\rfloor}N_{d,r}(q)(q^d-q^{d-r})}
\tag{4}
\]
with nilpotency index three. For any odd prime power \(q\), the total is instead \(\sum_r N_{d,r}(q)q^{d-r}\), and all operators square to zero.

There is also a sharp probability law as \(d\to\infty\) with \(q\) fixed and even. Write \(d=2m+\varepsilon\) with \(\varepsilon\in\{0,1\}\), and let
\[
S_\varepsilon(q)=\sum_{j=0}^{\infty}\frac{q^{-2j(j+\varepsilon)}}{Q_{2j+\varepsilon}(q)},\qquad
T_\varepsilon(q)=\sum_{j=0}^{\infty}\frac{q^{j-2j(j+\varepsilon)}}{Q_{2j+\varepsilon}(q)}.
\tag{5}
\]
Both series converge to strictly positive finite numbers. For a uniformly chosen weight-zero Rota–Baxter operator on \(A\),
\[
\boxed{\Pr(P^2=0)=q^{-m}\left(\frac{T_\varepsilon(q)}{S_\varepsilon(q)}+o(1)\right).}
\tag{6}
\]
In particular, the proportion with nilpotency index exactly three tends to one, and the exceptional square-zero proportion has an explicit parity-dependent leading constant.

## Assumptions and scope

The algebra is exactly \(A=k\oplus V\) with \((a+v)(b+w)=ab+aw+bv\). All maps are linear over the indicated field, not merely additive. An operator's nilpotency index is the least positive exponent at which it becomes zero; the zero map has index one. The maximal index above refers to the maximum over all weight-zero Rota–Baxter operators on this fixed algebra. Formulas (2)–(6) refer to labeled linear operators, not equivalence classes under algebra automorphisms. For finite \(q\), every rank \(r\) has its usual square-zero meaning \(r=\operatorname{rank}L\). The limit holds along each parity subsequence with fixed \(q=2^e\).

## Proof

**1. Structural reduction, in every characteristic.** Write \(P(v)=f(v)+L(v)\) for \(v\in V\), with \(f:V\to k\) linear and \(L:V\to V\) linear. Apply the Rota–Baxter identity with \(x=y=v\). Since \(v^2=0\), the scalar parts give \(f(v)^2=2f(v)^2\). Subtracting yields \(f(v)^2=0\), so \(f=0\). Next put \(P(1)=a+u\). Taking \(x=y=1\), the scalar parts give \(a^2=2a^2\), hence \(a=0\). Its \(V\)-part gives \(2Lu=0\). For \(x=1\), \(y=v\), now \(P(1)P(v)=uL(v)=0\), while the right-hand side equals \(P(L(v))=L^2(v)\). Hence \(L^2=0\).

Conversely assume the conditions in (1), and put \(x=a+v\), \(y=b+w\). Both images lie in the square-zero ideal, so the left-hand side of the Rota–Baxter identity is zero. The argument on its right is \(aL(w)+bL(v)+2ab\,u\); applying \(P\) gives \(aL^2(w)+bL^2(v)+2ab\,Lu=0\). Thus all displayed conditions are necessary and sufficient. Moreover \(P^2(1)=Lu\) and \(P^2(V)=0\), so \(P^3=0\). When the characteristic is odd, \(Lu=0\), and \(P^2=0\). When it is two and \(\dim V\ge2\), take independent \(e_1,e_2\in V\), set \(L(e_2)=e_1\), \(L(e_1)=0\), annihilate a complement, and take \(u=e_2\). Then \(P^2(1)=e_1\ne0\). In dimension one the only square-zero endomorphism is zero, while any nonzero \(u\) gives a nonzero \(P\) of index two. The odd-characteristic index two is likewise realized with \(L=0\) and \(u\ne0\).

**2. Exact finite-field counts.** For a square-zero endomorphism \(L\) of rank \(r\), its image \(U\) lies in its kernel \(K\), with \(\dim U=r\) and \(\dim K=d-r\). Select \(U\) in \(\binom{d}{r}_q\) ways, select \(K\supseteq U\) in \(\binom{d-r}{r}_q\) ways, and select the induced isomorphism \(V/K\to U\) in \(\lvert\operatorname{GL}_r(q)\rvert\) ways. This proves the first expression in (2); multiplying the standard Gaussian-product expressions gives the second. In characteristic two, all \(q^d\) choices of \(u\) are allowed for each \(L\). The exceptional condition \(P^2=0\) means \(Lu=0\), with precisely \(q^{d-r}\) choices. This proves (3), (4) and the complementary square-zero count \(\sum_r N_{d,r}(q)q^{d-r}\). In odd characteristic, \(Lu=0\) is compulsory, giving the stated total.

The formula also resolves the complete operator nilpotency type if desired. In characteristic two, for each square-zero \(L\) of rank \(r\), the disjoint cases \(u\in\operatorname{im}L\), \(u\in\ker L\setminus\operatorname{im}L\), and \(u\notin\ker L\) have respective multiplicities \(q^r\), \(q^{d-r}-q^r\), and \(q^d-q^{d-r}\). Their rank pairs \((\operatorname{rank}P,\operatorname{rank}P^2)\) are respectively \((r,0)\), \((r+1,0)\), and \((r+1,1)\). Zero multiplicities are permitted at boundary ranks. These rank pairs determine Jordan partitions since \(P^3=0\), yielding the complete rank/Jordan-type profile without an additional assumption.

**3. Sharp limiting law.** Set \(d=2m+\varepsilon\) and write \(r=m-j\). Formula (2) becomes
\[
\frac{N_{2m+\varepsilon,m-j}(q)}{q^{2m(m+\varepsilon)}}=
q^{-2j(j+\varepsilon)}\frac{Q_{2m+\varepsilon}(q)}{Q_{m-j}(q)Q_{2j+\varepsilon}(q)},\quad 0\le j\le m.
\tag{7}
\]
For fixed \(j\), the ratio \(Q_{2m+\varepsilon}(q)/Q_{m-j}(q)\) tends to one, and it lies between zero and one because \(Q_h(q)\) decreases with \(h\). Thus (7) is dominated by the summable weights appearing in \(S_\varepsilon(q)\). Multiplying the numerator of (7) by \(q^j\) produces the likewise summable weights defining \(T_\varepsilon(q)\). Dominated convergence for these nonnegative series gives
\[
\sum_r N_{d,r}(q)=q^{2m(m+\varepsilon)}\bigl(S_\varepsilon(q)+o(1)\bigr),\qquad
\sum_r q^{m-r}N_{d,r}(q)=q^{2m(m+\varepsilon)}\bigl(T_\varepsilon(q)+o(1)\bigr).
\]
The square-zero probability from part 2 is \(\sum_r q^{-r}N_{d,r}/\sum_r N_{d,r}\), which is precisely (6). Finiteness and positivity of the constants follow from the quadratic decay of their summands and \(Q_j(q)\ge\prod_{i\ge1}(1-q^{-i})>0\). This completes all infinite claims.

## Verification

`verify.py` requires Python 3 with the standard library. Run `python verify.py` in a directory containing that file. It enumerates every linear map on the split square-zero algebra over the prime fields of orders two, three and five in dimensions stated in its output. For each map it evaluates the original Rota–Baxter identity on every ordered pair of algebra elements, independently tests the nilpotency powers and matrix ranks, and compares the resulting rank-pair multiplicities with (2) and the three classes in part 2. All five small exhaustive instances pass. It also computes exact formula totals for binary dimensions one through six. Successful completion prints `VERIFY_OK`.

For example, over \(\mathbb F_2\) with \(\dim V=2\), there are exactly \(16\) weight-zero operators, of which \(10\) square to zero and \(6\) have index three. Over \(\mathbb F_3\) with \(\dim V=2\), there are \(33\), all of which square to zero. These finite tests are not a proof of (6) or of the universal algebraic classification; those claims are proved above.

## Relationship to prior work

Gubarev (2018 preprint, revised 2019) introduced the Rota–Baxter index and proved general weight-zero nilpotence results in characteristic zero, providing the conceptual invariant used here. Farooq (2026) proves the weight-zero classification for exactly the same algebra \(k\oplus V\), **under the explicit assumption that the field has characteristic zero**, yielding \(P^2=0\). This source therefore covers the characteristic-zero special case of (1), which is acknowledged as prior, but it does not cover the characteristic-two index-three phenomenon, the finite-field rank counts, or the sharp limiting proportions. The general theory of cohomology and deformation of weighted Rota–Baxter operators by Das (2021) does not calculate these invariants. Zheng and Guo (2019) classify operators on different low-order semigroup algebras, again with a characteristic-zero assumption in their stated principal results. Existing enumeration of square-zero matrices through Gaussian coefficients is standard and is not claimed as new; the new point is its algebraic identification with the characteristic-two weight-zero Rota–Baxter family and the resulting operator-index distribution.

## Limitations

The algebra has a split square-zero maximal ideal; higher radical powers and nonsplit algebras are outside scope. The count refers to all labeled field-linear operators, not conjugacy or deformation equivalence classes. In characteristic two the asymptotic holds for each fixed finite field as the radical dimension grows, with separate even/odd dimension constants; it is not claimed uniformly as \(q\) also varies. Finite exhaustive checks use prime fields only; the finite extension-field result follows by the general proof. Searches and source inspections cannot establish absolute publication priority; the possibility of an unindexed stronger classification or a prior equivalent finite-field enumeration remains. No independent mathematical audit was conducted.

## References

1. V. Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723, publicly posted 2018-05-02, revised 2019; especially Section 5.2 and its Rota–Baxter index definition. https://arxiv.org/abs/1805.00723
2. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670, publicly posted 2026-05-15; Section 3, characteristic-zero classification of the same algebra. https://arxiv.org/abs/2605.15670
3. A. Das, *Cohomology and deformations of weighted Rota-Baxter operators*, arXiv:2108.05411, publicly posted 2021-08-11. https://arxiv.org/abs/2108.05411
4. S. Zheng and L. Guo, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, Communications in Algebra (2019), DOI:10.1080/00927872.2018.1552278.
