# Restricted commuting varieties of square-zero derivations on characteristic-two truncated points

## Finding
Let \(k\) be **any field of characteristic two**, and let \(N\ge2\), \(h=\lfloor N/2\rfloor\), \(c=\lfloor h/2\rfloor+1\), and \(r\ge2\). Consider the truncated algebra \(A_N=k[t]/(t^N)\), its ordinary Lie algebra of \(k\)-linear Leibniz derivations \(L_N=\operatorname{Der}_k(A_N)\), and the reduced restricted commuting variety
\[
\mathcal C_{N,r}(k)=\{(D_1,\ldots,D_r)\in L_N^r:D_i^2=0,\ [D_i,D_j]=0\ \text{for all }i,j\}.
\]
Here \(D_i^2\) is composition, and brackets are Lie brackets. There are exactly \(c\) distinct \(h\)-dimensional **linear subspaces** \(V_j\subseteq L_N\), indexed by \(\lceil h/2\rceil\le j\le h\), such that
\[
\boxed{\mathcal C_{N,r}=\bigcup_{j=\lceil h/2\rceil}^{h} V_j^r.}
\]
In particular, every pairwise commuting family of square-zero derivations lies in a **single abelian linear subspace** of this list. The \(c\) products \(V_j^r\) are exactly the irreducible components of the reduced variety, all of dimension \(rh\). For \(j<\ell\),
\[
\dim(V_j^r\cap V_\ell^r)=r(h-\ell+j).
\]
For every finite field \(k=\mathbb F_q\) of characteristic two, the exact count of **ordered** commuting square-zero derivation \(r\)-tuples is
\[
\boxed{T_{N,r}(q)=q^{rh}+\lfloor h/2\rfloor\big(q^{rh}-q^{r(h-1)}\big).}
\]
Consequently \(T_{2h,r}(q)=T_{2h+1,r}(q)\), and this count coincides numerically with the number of single square-zero derivations on \(A_N\) over \(\mathbb F_{q^r}\); the latter count is background, not independently claimed as new.

## Assumptions and scope
The base field need not be algebraically closed. The parameter \(N\) is an integer at least two, and \(r\) is any integer at least two. For \(N=2h\), set \(u=t^2\), \(S=k[u]/(u^h)\); each derivation has unique form \(D_f=f\,d/dt\) with \(f=a(u)+t b(u)\), where \(a,b\in S\). For \(N=2h+1\), set \(S'=k[u]/(u^{h+1})\), \(S=k[u]/(u^h)\), and the corresponding derivations are exactly \(f=a(u)+tb(u)\) with \(a\in uS'\), \(b\in S\). Let \(H=h\) in even length and \(H=h+1\) in odd length. In either case, let \(v_u\) be the \(u\)-adic valuation, with valuation of zero equal to the module length, and define
\[
V_j=\{D_{a+tb}:a\in u^{H-j}k[u]/(u^H),\ b\in u^j S\},\quad \lceil h/2\rceil\le j\le h.
\]
For odd length, \(u^{H-j}\subseteq uS'\), so this definition stays within the derivation Lie algebra.

## Proof
First, \(d/dt\) is a derivation of \(A_N\) when \(N\) is even, and multiplication by \(t\) is required in its coefficient when \(N\) is odd; this follows from differentiating \(t^N=0\). In characteristic two, if \(f=a(u)+tb(u)\), then \(f'=b(u)\). Since the square of a derivation is itself a derivation in characteristic two, \(D_f^2=0\) is equivalent to \(D_f^2(t)=f f'=0\), and comparing even and odd coefficients yields exactly
\[
a b=0\text{ in }k[u]/(u^H),\qquad b^2=0\text{ in }S.
\]
Thus \(v_u(b)\ge\lceil h/2\rceil\), and if \(b\ne0\) of valuation \(j\), the annihilator condition forces \(a\in u^{H-j}k[u]/(u^H)\). If \(b=0\), the same derivation lies in \(V_h\). It follows that the square-zero locus is \(\bigcup_j V_j\).

Second, the commutator of derivations has coefficient
\[
[D_{a+tb},D_{c+td}](t)=(a+tb)d+(c+td)b=ad+cb
\]
in characteristic two. If two derivations lie in a fixed \(V_j\), both products vanish modulo \(u^H\), hence \(V_j\) is an abelian Lie subspace.

Conversely, suppose \((D_{a_i+tb_i})_{i=1}^r\) is square-zero and pairwise commuting. If all \(b_i=0\), every element lies in \(V_h\). Otherwise choose an index \(i\) such that \(j=v_u(b_i)\) is minimum among the nonzero \(b_i\). Then \(v_u(b_\ell)\ge j\) for every \(\ell\), and \(a_i b_i=0\) implies \(a_i\in u^{H-j}k[u]/(u^H)\), hence \(a_i b_\ell=0\) for all \(\ell\). Because \([D_i,D_\ell]=0\), we get \(a_\ell b_i=0\), so \(a_\ell\in u^{H-j}k[u]/(u^H)\). Therefore every \(D_\ell\in V_j\). This proves the union identity for arbitrary \(r\).

Each \(V_j\) is \(h\)-dimensional: \(a\) has exactly \(j\) free coefficients and \(b\) has \(h-j\). For \(j<\ell\), their intersection has \(j+(h-\ell)=h-\ell+j\) dimensions. Since neither is contained in another, their products are exactly the distinct irreducible components of the reduced union. For a finite field, add products \(V_j^r\) in increasing index \(j\). Each has \(q^{rh}\) points; the intersection of the new product with all earlier products equals its intersection with the immediately preceding one, which has \(q^{r(h-1)}\) points (all nonadjacent pair intersections are contained in that nearest intersection). Starting with one product and adding \(c-1=\lfloor h/2\rfloor\) copies proves the count. No assertion about nonreduced scheme structure is made.

## Verification
A standalone Python 3 checker in `verify_tuples.py` enumerates all coefficients over the prime field \(\mathbb F_2\) and over the extension \(\mathbb F_4\). It tests the Leibniz condition, literal derivative coefficient multiplication, square-zero conditions and every pairwise bracket, and compares full tuple totals to the formula. The checker is independent of the geometric component count. Its reproduced cases include dimensions \(N=2,3,4,5,6,7,8\) in characteristic two, ordered tuple lengths \(r=2,3,4\), and extension-field cases with \(N=4\), \(r=3\); see `verification-output.txt`. These are finite checks, not a proof of all dimensions.

## Relationship to prior work
Evans and Fuchs (2001), Theorem 1, determine the restricted power in the \(p\)-dimensional Witt algebra, including the \(p=2\) first-truncation case; their paper does not classify all-length restricted commuting tuple varieties. Yao and Chang (2013), Theorem 3.6, determine nilpotent commuting-pair components for the \(p\)-dimensional Witt algebra under the explicit hypothesis \(p>3\); this excludes characteristic two and arbitrary truncation length. General results on nilpotent commuting varieties in classical Lie algebras concern different objects. Single-derivation square-zero cones and their component counts provide related background and are *not* claimed as new. The additional condition that **all members of a commuting tuple must lie in one common component** is the structural ingredient behind the simultaneous-count formula.

## Limitations
The result is restricted to characteristic two, one-variable truncated polynomial algebras, and **reduced** restricted commuting varieties. It does not enumerate higher restricted nilpotence, noncommuting tuples, orbit decompositions, or nonreduced scheme structures. Historical priority has not been independently certified: an undiscovered general theorem about commuting varieties or higher infinitesimal group-scheme actions could imply the result. The proof is mathematical; finite experiments merely corroborate it.

## References
1. T. Evans and D. Fuchs, *On the restricted Lie algebra structure for the Witt Lie algebra in finite characteristic*, arXiv:math/0111271v1, 2001-11-27. https://arxiv.org/html/math/0111271v1 .
2. Y.-F. Yao and H. Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1, 2013-01-23. https://arxiv.org/abs/1301.5667 .
3. A. Premet, *Nilpotent commuting varieties of reductive Lie algebras*, Inventiones Mathematicae 154 (2003), 653–683. https://doi.org/10.1007/s00222-003-0315-6 .
