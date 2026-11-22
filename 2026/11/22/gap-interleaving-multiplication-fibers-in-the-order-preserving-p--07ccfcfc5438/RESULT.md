# Gap-interleaving multiplication fibers in the order-preserving partial-injection monoid

## Finding
Let \(\mathrm{POI}_n\) be the monoid of increasing partial bijections of the chain \([n]=\{1,\ldots,n\}\), including the empty map, with left-to-right composition. For a prescribed increasing partial bijection \(h:A\to D\) of rank \(t\), let \(F_{r,s}(h)\) count ordered factorizations \(h=fg\) with \(\operatorname{rk} f=r\) and \(\operatorname{rk}g=s\). For a \(t\)-subset \(U=\{u_1<\cdots<u_t\}\), write \(u_0=0\), \(u_{t+1}=n+1\), and \(\gamma_j(U)=u_{j+1}-u_j-1\) for \(0\le j\le t\). For each possible intermediate survivor set \(I\) of size \(t\), set \(a_j=\gamma_j(A)\), \(d_j=\gamma_j(D)\), and \(b_j=\gamma_j(I)\). Then, for every \(n\ge1\) and \(0\le r,s,t\le n\),

\[
F_{r,s}(h)=[x^{r-t}y^{s-t}]\sum_{\substack{I\subseteq[n]\\|I|=t}}\prod_{j=0}^{t}\left(\sum_{\substack{u,v\ge0\\u+v\le b_j}}\binom{a_j}{u}\binom{d_j}{v}\binom{b_j}{u}\binom{b_j-u}{v}x^uy^v\right).
\]

Terms with impossible binomial parameters vanish; negative coefficient indices also give zero. Thus the formula includes the empty target, arbitrary prescribed endpoints, and impossible-rank boundaries.

There is a sharp near-unit classification. For \(n\ge2\), put \(N=n-1\) and require both factors to have rank \(n-1\). Every rank-\(n-1\) target has exactly \(n\) factorizations. For a rank-\(n-2\) target, write its two missing domain positions \(u<v\) and its two missing range positions \(a<b\). Its factorization count is

\[
F_{n-1,n-1}(h)=4+\sum_{p\in\{u,v-1\}}\sum_{q\in\{a,b-1\}}\mathbf1_{p=q},
\]

where the braces are **multisets** (multiplicities matter). Among all rank-\(n-2\) targets the only possible fiber sizes are \(4,5,6,8\), with respective multiplicities

\[
\frac{N(N-1)(N^2-N+2)}4,\qquad N(N-1)(N-2),\qquad\frac{5N(N-1)}2,\qquad N.
\]

Zero multiplicities are allowed for the small cases: for \(n=2\), only \(8\) occurs; for \(n=3\), only \(4,6,8\) occur; for \(n\ge4\), all four occur. No target of rank at most \(n-3\) is the product of two rank-\(n-1\) factors. In particular, the seemingly intermediate fiber value \(7\) never occurs, and fiber \(8\) occurs exactly when both missing pairs are the same adjacent pair.

## Assumptions and scope
All maps are partial, injective, and strictly increasing on their domains. Each is uniquely encoded by its ordered domain and ordered range. Multiplication \(fg\) applies \(f\) and then \(g\). No characteristic or field assumptions occur. The target is specified as an actual partial map, not solely by its rank. The displayed coefficient formula is an exact integer identity with finitely many summands, not an asymptotic approximation.

## Proof
**Intermediate survivors.** Fix a factorization \(h=fg\). Its intermediate survivor set is \(I=f(A)=\operatorname{ran}(f)\cap\operatorname{dom}(g)\). The restrictions \(f|_A:A\to I\) and \(g|_I:I\to D\) are the unique increasing bijections. Their composite is necessarily \(h\), so no additional value choices remain.

**Gap bijection.** Write \(B=\operatorname{dom}(f)\setminus A\), \(V=\operatorname{ran}(f)\setminus I\), \(W=\operatorname{dom}(g)\setminus I\), and \(X=\operatorname{ran}(g)\setminus D\). The sets \(V,W\) are disjoint: otherwise the corresponding element of \(B\) survives both factors, contradicting \(\operatorname{dom}(h)=A\). Conversely, any four such sets of the right sizes, with increasing-order insertion matched gapwise, determine unique \(f\) and \(g\). In gap \(j\), if \(|B_j|=|V_j|=u\) and \(|W_j|=|X_j|=v\), there are exactly \(\binom{a_j}{u}\binom{b_j}{u}\binom{b_j-u}{v}\binom{d_j}{v}\) choices. Choices in separate gaps are independent. Since \(|B|=r-t\) and \(|X|=s-t\), the product of gap factors, coefficient extraction, and sum over all \(I\) give the formula. This also proves the impossible-rank cases because the disjoint intermediate subsets have total size \(r+s-t\le n\).

**Near-unit factors.** If \(r=s=n-1\), the intermediate domain/range of the two factors each miss one position, so their product has rank \(n-1\) if these missing positions coincide and rank \(n-2\) otherwise. For a prescribed rank-\(n-1\) target, the matching missing intermediate position is arbitrary, giving exactly \(n\) factorizations.

For a prescribed rank-\(n-2\) target, there are exactly two choices of which missing source position belongs to the extra source domain of \(f\), and two choices of which missing target position belongs to the extra output range of \(g\). These give four ordered pairs of insertion gaps. Each ordered pair contributes one intermediate two-deletion pattern if its insertion gap indices differ, and two patterns if the indices coincide: two deleted intermediate positions can then be assigned in either order to the extra image of \(f\) and the extra domain of \(g\). For source holes \(u<v\), the two insertion-gap indices are \(u\) and \(v-1\); for target holes \(a<b\), they are \(a\) and \(b-1\). The stated dot-product-of-multiplicities formula follows.

**Spectrum.** The map \(\{u,v\}\mapsto\{u,v-1\}\) is a bijection from two-subsets of \([n]\) to size-two multisets of \([N]\). The extra term in the fiber formula is the scalar product of two multiplicity vectors of these multisets. Equal repeated multisets give scalar product \(4\) (\(N\) ordered pairs), distinct multisets with scalar product \(2\) give \(2N(N-1)+\binom N2=5N(N-1)/2\), pairs of distinct two-element multisets sharing one index give \(N(N-1)(N-2)\), and all remaining ordered pairs give scalar product \(0\). Subtracting these from \(\binom n2^2\) yields \(N(N-1)(N^2-N+2)/4\). A scalar product of \(3\) cannot occur, proving the missing \(7\) claim. Repeated multisets correspond precisely to adjacent missing pairs, proving the maximum statement.

## Verification
Run the self-contained `CHECKER.py` with a standard Python 3 interpreter. `CHECK_OUTPUT.txt` records the result. The program constructs all order-preserving partial injections and directly multiplies each ordered pair for \(n=1,2,3,4\), independently evaluating every nonzero rank-conditioned prescribed fiber by the coefficient formula. It separately verifies the complete near-unit spectrum by direct multiplication for every \(2\le n\le12\), including the missing \(7\) and the \(n\)-factorization class. These finite checks validate the implementation and sample cases; the universal statements are proved by the preceding bijections.

As an auxiliary distinction, summing all targets of rank \(t\) gives \(\binom nr^2\binom ns\binom rt\binom{n-r}{s-t}\), the same aggregate count as unrestricted partial bijections. Yet the near-unit prescribed fibers range from \(4\) to \(8\), showing that the aggregate law does not recover the target-specific coefficients.

## Relationship to prior work
Fernandes (2001) studies the monoid's structure and presentation. Dimitrova–Koppitz (2009) determine maximal subsemigroups of its ideals. Laradji–Umar (2013) enumerate related order-preserving partial transformations using lattice paths. Lopez (2019) gives economical generators and notes the top-rank product condition. Their inspected statements do not supply the above rank-conditioned prescribed-target factorization formula or the sharp \(4,5,6,8\) near-unit spectrum. Published rank-uniform convolution for the *full symmetric inverse monoid* gives an aggregate rank distribution but does not imply the order-restricted target fibers, which are nonuniform.

## Limitations
This is a formula and a near-unit classification; no claim is made about the optimal asymptotic behavior or all possible prescribed-fiber multiplicities for general ranks. A close earlier equivalent enumeration may exist outside inspected literature; the older structural paper of Ganyushkin–Mazorchuk (2003) was accessible only in abstract, and the full text of a relevant separately indexed unrestricted inverse-monoid result could not be inspected.

## References
- V. H. Fernandes, *The Monoid of All Injective Order Preserving Partial Transformations on a Finite Chain*, Semigroup Forum 62 (2001), 178–204. DOI: https://doi.org/10.1007/s002330010056
- I. Dimitrova and J. Koppitz, *The maximal subsemigroups of the ideals of some semigroups of partial injections*, Discussiones Mathematicae General Algebra and Applications (2009). DOI: https://doi.org/10.7151/dmgaa.1155
- A. Laradji and A. Umar, *Lattice Paths and Order-preserving Partial Transformations*, arXiv:1304.7574v1 (publicly posted 2013-04-29). https://arxiv.org/abs/1304.7574
- S. Lopez, *Economical Generating Sets of the Monoid of Partial Order-preserving Injections*, DIMENSIONS (2019). https://www.fullerton.edu/nsmssc/_resources/pdfs/2019_dimensions.pdf
- O. Ganyushkin and V. Mazorchuk, *On the structure of IOn*, Semigroup Forum 66 (2003), 455–483. https://doi.org/10.1007/s00233-002-0006-4
