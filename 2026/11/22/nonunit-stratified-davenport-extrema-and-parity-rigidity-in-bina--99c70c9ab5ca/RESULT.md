# Nonunit-stratified Davenport extrema and parity rigidity in binary truncated polynomial rings

## Finding
For each integer \(n\ge1\), let \(R_n=\mathbb F_2[t]/(t^n)\) and let \(S_n\) be its multiplicative semigroup. A finite indexed sequence is *irreducible* if its product differs from the product of every proper subsequence, including the empty subsequence (whose product is \(1\)). For \(0\le r\le n\), let \(L_n(r)\) be the largest length of an irreducible sequence containing exactly \(r\) nonunits. Define
\[
 d_n=1+\sum_{m=1}^{n-1}2^{\nu_2(m)}\quad(n\ge1).
\]
Then the **complete nonunit-stratified extremal length law** is
\[
 \boxed{L_n(r)=\begin{cases}
 d_n-1,&r=0,\\
 r+d_{n-r}-1,&1\le r<n,\\
 n,&r=n.
 \end{cases}}
\]
No irreducible sequence contains more than \(n\) nonunits. In particular, the maximum length without prescribing \(r\) is
\[
 \max_r L_n(r)=\begin{cases}n,&n\in\{1,2\},\\d_n-1,&n\ge3.\end{cases}
\]
The latter *numerical* maximum is not asserted to be new: it follows from published results on Davenport constants of finite commutative rings. The new subject is the entire stratification and the inverse classification of nonunit counts at maximum length.

The possible nonunit counts in an irreducible sequence of global maximum length are exactly
\[
 \boxed{\begin{array}{c|c}
 n&\text{possible counts}\;r\\\hline
 1,2&\{n\}\\
 3&\{0,3\}\\
 4&\{0,1,4\}\\
 \text{odd }n\ge5&\{0\}\\
 \text{even }n\ge6&\{0,1\}.
 \end{array}}
\]
For odd \(n\ge5\), *every* maximal irreducible sequence consists entirely of units. For even \(n\ge6\), a maximal irreducible sequence that contains nonunits contains exactly one of valuation one, and its remaining \(d_{n-1}-1\) units form a maximal product-one-free sequence after reduction modulo \(t^{n-1}\). Conversely every such lift is maximal irreducible. At \(n=4\), the same one-nonunit alternative exists and there is also a length-four zero-product alternative; at \(n=3\), maximal zero-product lists also occur.

## Assumptions and scope
The integer \(n\) is positive. For an element \(a\in R_n\) write \(v(a)=\min\{\nu_t(a),n\}\), with \(v(0)=n\); thus units have valuation zero. The term *nonunit* always means \(v(a)>0\). A sequence is an indexed multiset: repeated elements are allowed and deletion means deletion of at least one occurrence.

A list \(u_1,\ldots,u_s\) in \(U_j=R_j^\times\) is *product-one-free* if none of its nonempty sublists multiply to \(1\) in \(U_j\). This is a condition in the smaller group, not necessarily in \(U_n\). We count length, not equivalence classes of sequences.

The theorem concerns multiplicative semigroups of binary truncated one-variable polynomial rings. It does not classify the unit-group sequences themselves up to automorphism, and does not claim a general inverse theorem for other finite local rings.

## Proof
**1. An exact deletion test.** Split an arbitrary finite list \(A\) into its \(r\) nonunits and its unit sublist \(B\). Put \(V=\sum_{a\in A,\,v(a)>0}v(a)\). If \(V<n\), deleting even one nonunit strictly decreases the product valuation, so any deletion preserving the product must delete units only. Factor the product of the nonunits as \(t^Vw\), where \(w\) is a unit. Multiplication by \(t^Vw\) identifies equality of two unit products in \(R_n\) with equality of their reductions in \(R_{n-V}\). Consequently
\[
 A\text{ irreducible}\iff B\bmod t^{n-V}\text{ is product-one-free in }U_{n-V}\qquad(V<n).
\]
If \(V\ge n\), the full product is zero. Deleting any unit leaves the product zero, so an irreducible list contains no units. Deleting a nonunit \(a\) leaves product zero exactly when \(V-v(a)\ge n\). Because deleting more terms cannot increase the valuation, it suffices to test single deletions. Thus
\[
 A\text{ irreducible}\iff B=\varnothing\text{ and }V-v(a)<n\text{ for every }a\in A\qquad(V\ge n).
\]
In particular, any irreducible zero-product list has at most \(n\) elements: after removal of any one element, all remaining \(r-1\) nonunit valuations sum to at most \(n-1\). The bound \(r=n\) forces every valuation to be exactly one.

**2. The exact unit-group constant.** For each odd integer \(j<n\), let \(e_j\) be the unique positive integer satisfying \(j2^{e_j-1}<n\le j2^{e_j}\). The elements \(g_j=1+t^j\) in \(U_n\) have order \(2^{e_j}\). Their powers generate all of \(U_n\) independently: every degree \(1\le m<n\) has the unique form \(m=2^s j\) with \(j\) odd, and \(g_j^{2^s}=1+t^m\); eliminating successive lowest nonconstant coefficients builds each unit uniquely. Therefore
\[
 U_n\cong\prod_{\substack{1\le j<n\\j\,\mathrm{odd}}}C_{2^{e_j}},\qquad
 D(U_n)=1+\sum_{j\,\mathrm{odd}<n}(2^{e_j}-1)
 =1+\sum_{m=1}^{n-1}2^{\nu_2(m)}=d_n.
\]
Here \(D(U_n)\) denotes the least length at which every unit list has a nonempty subproduct equal to one. For completeness, the lower bound is attained by \(2^{e_j}-1\) copies of each independent generator. The upper bound follows from the augmentation ideal of \(\mathbb F_2[U_n]\): in the cyclic-coordinate presentation its generators \(g_j-1\) satisfy \((g_j-1)^{2^{e_j}}=0\), so every product of \(1+\sum_j(2^{e_j}-1)\) augmentation elements vanishes. For a hypothetical product-one-free list, the coefficient of the identity in \(\prod(1-g_i)\) would instead be one. Hence the two bounds agree. The trivial group at \(n=1\) has \(d_1=1\).

Taking the difference of the displayed formula gives
\[
 d_n-d_{n-1}=2^{\nu_2(n-1)}\qquad(n\ge2).
\]

**3. Sharp extremal length for a prescribed nonunit count.** If \(r=0\), the first deletion test reduces to the group result, yielding \(L_n(0)=d_n-1\). If \(1\le r<n\) and \(V<n\), then \(V\ge r\) and the unit sublist has length at most \(d_{n-V}-1\le d_{n-r}-1\), so total length is at most \(r+d_{n-r}-1\). For a zero-product list the length is exactly \(r\), no greater than the same bound. This bound is attained with \(r\) copies of \(t\) and a lift of a maximum product-one-free sequence in \(U_{n-r}\), proving the second line of the formula. When \(r=n\), all \(n\) valuation-one nonunits give an irreducible zero-product list and no longer irreducible list with \(n\) nonunits is possible. If \(r>n\), removal of any one nonunit still leaves a zero product, so the list is reducible.

**4. Global inverse parity classification.** For \(1\le r<n\), compare \(L_n(r)\) with the all-unit length \(d_n-1\):
\[
 (d_n-1)-L_n(r)=\sum_{m=n-r}^{n-1}\bigl(2^{\nu_2(m)}-1\bigr).
\]
The right side is zero exactly when \(r=1\) and \(n\) is even; it is strictly positive for odd \(n\) or \(r\ge2\), since every interval of two consecutive positive integers contains an even number. Compare the zero-product length \(n\): for \(n=3,4\) it equals \(d_n-1\); for \(n=1,2\) it is larger; and for every \(n\ge5\) it is strictly smaller, since \(d_5-1=8>5\) and \((d_{n+1}-1)-(n+1)\ge(d_n-1)-n\). This proves the complete global nonunit-count table.

In every global one-nonunit case, \(V=1\) is forced because \(d_{n-V}\) strictly decreases as \(V\) increases; the first deletion test therefore describes the rest of the list exactly. For a global zero-product case of length \(n\), all \(n\) nonunits have valuation one by Step 1. These observations prove the claimed inverse descriptions and their converses.

## Verification
The accompanying self-contained `verify.py` performs exact polynomial arithmetic using bit masks, directly enumerates all proper subsequences, and independently checks the deletion criterion. Its fresh output, `verification_output.txt`, records 81,340 successful assertions. This includes exhaustive irreducibility checks for all multisets up to length four over \(R_n\) for \(1\le n\le5\); exhaustive Davenport thresholds, global nonunit profiles, and prescribed-nonunit maxima for \(1\le n\le4\); independent unit-generator checks through \(n=12\); and 1,000 randomized longer-list comparisons. These are finite sanity checks, **not** a replacement for the proof of the universal assertions above.

To reproduce: run `python3 verify.py` with Python 3 and no nonstandard dependencies. The encoded multiplication, valuation, independent full-subsequence irreducibility predicate, and predicted criteria are contained entirely in that file.

## Relationship to prior work
Zhang, Wang, and Qu (2015) prove Davenport-constant bounds for quotients of \(\mathbb F_2[x]\) and set this family in context. Deng (2016) subsequently proves a general exact ring Davenport-constant formula, which already determines the *unrestricted numerical* maximum length for this family. Wang (2014) establishes complementary results for polynomial quotient rings over larger residue fields. This finding does not reassert those numerical facts as new.

The new assertion refines an unrestricted scalar invariant into exact maxima for **every prescribed number of nonunits**, and then an all-depth inverse rigidity theorem identifying exactly when nonunit-containing global extremizers exist. Those finer statements are not stated by the inspected principal theorems and do not follow from the scalar value alone. The proof derives them from the explicit valuation deletion test, the binary unit-group structure, and equality analysis at the sharp bound. Schmid's inverse zero-sum work illustrates the separate motivation for inverse extremal classifications in classical groups.

## Limitations
This resolves the nonunit count and associated valuation-one rigidity, not the generally harder equivalence-class classification of maximum product-one-free unit lists. The classification is restricted to \(\mathbb F_2[t]/(t^n)\) and is not a classification of all finite local rings. Historically, a more general inverse-semigroup theorem, including one with different terminology, could imply the same result; the present novelty assessment is based on inspected sources and targeted research searches rather than a mathematical proof of priority. Exhaustive computation covers only finite depths.

## References
1. L. Zhang, H. Wang, Y. Qu, *A problem of Wang on Davenport constant for the multiplicative semigroup of the quotient ring of F2[x]*, arXiv:1507.03182, first posted 12 July 2015. https://arxiv.org/abs/1507.03182
2. C. Deng, *Davenport constant for commutative rings*, arXiv:1602.03445, first posted 9 February 2016. https://arxiv.org/abs/1602.03445
3. G. Wang, *Davenport constant for semigroups II*, arXiv:1409.2077, first posted 7 September 2014. https://arxiv.org/abs/1409.2077
4. W. A. Schmid, *Inverse Problems Associated to the Davenport Constant for C2 plus C2 plus C2n*, *Electronic Journal of Combinatorics* 18 (2011), P33. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v18i1p33
