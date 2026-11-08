# High-order moment camouflage among conditional random-search-tree leaf laws

## Finding

Let \(L_n\) be the number of nonempty-tree leaves in a uniformly random insertion-order binary search tree on \(n\) keys, and \(J\) the rank of its first key. Put \(L_0=0\). For any integer \(r\ge1\) and \(n\ge4r+3\), every root split \(J=a+1\) with \(2r\le a\le n-1-2r\) gives the same first \(r\) moments of \(L_n\), although distinct unordered splits yield distinct distributions incomparable in first-order stochastic order.

Specifically, for every \(1\le s\le r\),
\[
\kappa_s(L_n\mid J=a+1)=(n+1)c_s,
\qquad c_s=\frac{\kappa_s(L_{2s})}{2s+1}.
\]
For positive left and right subtree sizes \(a,b=n-1-a\),
\[
\Pr(L_n=2\mid J=a+1)=\frac{2^{n-3}}{a!b!}.
\]
This increases strictly when the smaller subtree increases toward balance. Yet all such conditional means equal \((n+1)/3\), so no two distinct conditional laws in the specified family are stochastically ordered. The phenomenon persists for arbitrary prescribed finite moment order \(r\), rather than just the mean and variance.

## Assumptions and scope

Keys are distinct and their insertion order is uniform over all \(n!\) permutations. An internal vertex is a leaf exactly when it has zero children; empty subtrees contribute zero leaves. Conditional on \(J=a+1\), the left and right subtrees have \(a\) and \(b=n-1-a\) vertices and are independent random insertion-order trees. Cumulants are ordinary logarithmic moment-generating-function coefficients, with \(\kappa_1\) the mean and \(\kappa_2\) the variance. The finite-cutoff assertion holds for all integers \(s\ge1,m\ge2s\); the comparison claim requires two distinct split values, guaranteed by \(n\ge4r+3\).

## Proof

Assign independent continuous priorities \(U_1,\ldots,U_m\) to keys in key order, where a smaller priority signifies earlier insertion. A key is a tree leaf if and only if its priority exceeds those of its immediate key neighbors, treating missing neighbors as having priority smaller than every actual priority. Indeed, if a neighbor has later insertion time, it must enter as a descendant of the key; conversely, any descendant of a key has on its left or right side an immediately adjacent key that was inserted later than that key. This may also be proved inductively by splitting at the minimum priority.

Adjoin one artificial globally smallest priority before the first key, thereby forming a cycle of \(N=m+1\) priorities. The number of cyclic strict local maxima equals \(L_m\). By cyclic exchangeability, the cyclic-peak count for \(N\) iid continuous priorities has the same law as the peak count conditional on one fixed location holding the global minimum; this is exactly the preceding model.

Let \(I_i\) indicate a cyclic strict local maximum at location \(i\), and set \(S_N=\sum_{i=1}^{N}I_i\). Each indicator depends only on the priorities at locations \(i-1,i,i+1\), so the dependency graph joins locations at circular distance one or two. Multilinearity of joint cumulants yields
\[
\kappa_s(S_N)=\sum_{i_1,\ldots,i_s}\kappa(I_{i_1},\ldots,I_{i_s}).
\]
Any summand vanishes when the dependency graph on its distinct locations is disconnected. When \(N\ge2s+1\), every connected configuration with at most \(s\) distinct locations has one and only one cyclic gap greater than two between successive occupied locations: some gap exceeds two because the total circumference exceeds twice the number of occupied locations; two such gaps would disconnect the configuration. Cutting at this unique gap produces a fixed finite linear configuration, unaffected by changes in \(N\). Every such configuration has exactly \(N\) rotational positions, and all joint cumulants depend only on that fixed local configuration. Thus \(\kappa_s(S_N)=N c_s\) whenever \(N\ge2s+1\), where setting \(N=2s+1\) identifies \(c_s=\kappa_s(L_{2s})/(2s+1)\). Consequently \(\kappa_s(L_m)=(m+1)c_s\) for \(m\ge2s\).

Given \(J=a+1\), subtree independence gives \(L_n\overset{d}=L_a+L_b\) with independent summands. For all \(1\le s\le r\), both sizes exceed \(2s\), so cumulant additivity gives \((a+1)c_s+(b+1)c_s=(n+1)c_s\). Cumulants through order \(r\) determine raw moments through the same order.

For \(m\ge1\), \(L_m=1\) exactly when the tree is a path. At every recursive split the first key must be an extremal key; there are exactly \(2^{m-1}\) insertion permutations with this property, hence \(\Pr(L_m=1)=2^{m-1}/m!\). When \(a,b\ge1\), a conditional total of exactly two leaves requires one leaf in each independent subtree. This gives the displayed probability. For \(a<b\), the ratio of the two-leaf probabilities at splits \(a+1,b-1\) and \(a,b\) equals \(b/(a+1)>1\), up to the point of equality of sizes. Thus different unordered splits in the stated range give distinct laws. Their common mean is \((n+1)c_1=(n+1)/3\): at any cyclic location, a uniformly random priority is the largest of its three neighbors with probability \(1/3\). Finally, if one integrable law first-order stochastically dominates another and their means agree, their distributions must agree, contradicting the distinct two-leaf probabilities. This proves pairwise stochastic incomparability.

## Verification

The accompanying standalone Python script constructs the exact probability generating polynomials by the root-split recurrence, converts rational moments to cumulants, and checks the cutoff cumulant identity for orders one through eight and tree sizes through 26. It also independently constructs actual insertion-order binary search trees for all permutations through eight keys, compares their leaf counts with the endpoint-augmented cyclic-peak statistic, and checks conditional split distributions, moments and the two-leaf probability. Its successful run comprised 93,551 exact assertions.

For instance, with \(n=11\), the root ranks five and six give subtree sizes \((4,6)\) and \((5,5)\). Both conditional laws have mean \(4\) and variance \(8/15\), but their probabilities of exactly two leaves are respectively \(2/135\) and \(4/225\).

## Relationship to prior work

Warren and Seneta (1996) already study peak counts of random permutations, their circular analogues and linear cumulants; that underlying linearity is not asserted to be new. Bóna and Pittel (first arXiv version December 8, 2014) provide a full generating function for leaf counts of random search trees and the standard recursive decomposition. Döring and Eichelsbacher (first arXiv version December 22, 2010) develop dependency-graph cumulant methods. The contribution considered here is the combined all-orders **conditional-root moment indistinguishability despite stochastic-order incomparability**, including an explicit separating two-leaf event across arbitrarily many split values. The component tools and several unconditioned statements predate this observation.

## Limitations

This is a theorem for uniform insertion-order binary search trees, not for uniformly chosen Catalan tree shapes or arbitrary split-tree models. Moment equality is finite-order, not equality of laws. No universal sharpness of the cutoff \(2s\) is claimed. The 1996 circular-peak paper's full text was not available for comparison; its abstract explicitly covers cumulant linearity, so historical priority of conditional consequences remains uncertain. No independent scientific audit has been performed.

## References

- D. Warren and E. Seneta, *Peaks and Eulerian numbers in a random sequence*, Journal of Applied Probability 33 (1996), 101–114, DOI: https://doi.org/10.2307/3215267.
- M. Bóna and B. Pittel, *On a random search tree: asymptotic enumeration of vertices by distance from leaves*, arXiv:1412.2796, first posted 2014-12-08, https://arxiv.org/abs/1412.2796.
- H. Döring and P. Eichelsbacher, *Moderate deviations via cumulants*, arXiv:1012.5027, first posted 2010-12-22, https://arxiv.org/abs/1012.5027.
