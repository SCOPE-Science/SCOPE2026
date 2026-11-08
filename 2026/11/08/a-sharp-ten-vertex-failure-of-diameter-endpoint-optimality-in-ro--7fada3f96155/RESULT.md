# A sharp ten-vertex failure of diameter-endpoint optimality in rooted-tree parking

## Finding

Let \(T\) be a finite unweighted tree on \(n\) vertices. Fix a destination root \(r\). Each of \(m\) labelled cars, \(1\le m\le n\), independently chooses a uniformly random initial vertex. In order, a car parks at its chosen vertex if free; otherwise it follows the unique path towards \(r\), parking in the first free place, and exits unsuccessfully if none remains. Write \(N_r(T,m)\) for the number of preference sequences in \(V(T)^m\) for which every car parks, so the success probability is \(N_r(T,m)/n^m\). A *diameter endpoint* lies on a longest path as an endpoint.

**Theorem (first nonperipheral optimum and an infinite witness family).** For every tree of order \(n\le9\) and every \(1\le m\le n\), a diameter endpoint maximizes \(N_r(T,m)\) over the roots \(r\in V(T)\). Among the \(106\) unlabelled ten-vertex trees, exactly one isomorphism type fails this property, and it fails exactly when \(m=4\) or \(m=5\). It is the tree \(B(3,3)\) described below. At \(m=4\), the unique optimal root is its central pendant vertex; its count is \(9290\), whereas every diameter endpoint has count \(9263\). Therefore the success-probability advantage is exactly \(27/10^4\).

More generally, form \(B(a,b)\) from a central junction \(o\) with three neighbors: a pendant \(c\) and hubs \(u,v\); attach \(a\) further pendant vertices to \(u\) and \(b\) to \(v\), with integers \(a,b\ge1\). This tree has \(a+b+4\) vertices. For \(m=4\), the following are **exact counts of successful ordered preference sequences**, with \(x\) any pendant neighbor of \(u\) and \(y\) any pendant neighbor of \(v\):

\[
\begin{aligned}
N_c-N_o&=59(a+b)+38,\\
N_c-N_u&=a(19a+16b+40),\\
N_c-N_v&=b(16a+19b+40),\\
N_c-N_x&=27(a-2),\\
N_c-N_y&=27(b-2).
\end{aligned}
\]

Thus for every \(a,b\ge3\), the central pendant \(c\) is the **unique** optimal root, even though all diameter endpoints are outer pendants. This gives an infinite family of nonperipheral optimal roots. The threshold is sharp within this family: if either hub has only two outer pendants, a diameter endpoint ties \(c\); with one, a corresponding diameter endpoint beats \(c\).

The smallest counterexample is also load-sensitive. For \(B(3,3)\), the counts at the central pendant and each diameter endpoint respectively are \(85500\) and \(85378\) when \(m=5\), but \(724620\) and \(734070\) when \(m=6\); hence increasing the load reverses their ordering.

## Assumptions and scope

Trees are finite, simple, connected and unweighted; the root is a fixed vertex; cars are distinguished and their initial preferences are independent uniform choices with replacement. All root placements are compared on the *same* underlying unrooted tree. The class \(B(a,b)\) has the indicated vertices and edges only. The theorem concerns the all-cars-park event, not mean travel distance, expected number successfully parked or randomization of the tree itself. Roots are optimized anew for each specified \(m\).

The underlying probability model and its Abelian property have been studied in random-tree parking theory; the present claim is a fixed-tree root-location comparison. The displayed integer identities hold for **all** integers \(a,b\ge1\), not only the finite range used for the first-failure classification.

## Proof

**1. Exact labelled-car recurrence.** Root any tree at \(r\). For a vertex \(w\), let \(c_w\) be the number of cars whose initial preference is \(w\). Because movements always go upwards and each occupied vertex absorbs one car, the number of cars exiting the descendant subtree through its parent satisfies

\[
q_w=\max\left\{0,c_w+\sum_{t\text{ child of }w}q_t-1\right\}.
\]

This identity is unchanged by permuting driver order (the Abelian property). For each descendant subtree, keep a table \(F_w(q,k)\) counting preference sequences for \(k\) labelled cars initially inside that subtree, producing exactly \(q\) exits. A one-vertex table is obtained by placing \(c=k\) cars at that vertex. To merge two disjoint subtrees containing \(k\) and \(\ell\) of the car labels, multiply their counts by \(\binom{k+\ell}{k}\), which chooses and interleaves the two ordered label subsequences; add the child exit counts, insert the cars initially preferring \(w\), and apply the displayed update. The result is \(N_r(T,m)=F_r(0,m)\). This is an exact integer recurrence, not a simulation or a floating-point approximation.

**2. Four-car orbit polynomial.** For each of the six root classes \(o,u,v,c,x,y\), fix the root and take a representative tree with five outer leaves at each hub. Classify all four-entry preference sequences according to which positions choose the four distinguished core vertices and which choose outer leaves, retaining *only the equality pattern* among outer leaves of each type. When a root is an outer leaf, treat that chosen leaf as an additional fixed vertex. If a successful canonical pattern uses \(i\) distinct *undistinguished* leaves of the \(u\)-class and \(j\) of the \(v\)-class, its multiplicity in \(B(a,b)\) is

\[
(a-\varepsilon_u)_{\underline i}(b-\varepsilon_v)_{\underline j},
\]

where \(\varepsilon_u=1\) only for root \(x\), and \(\varepsilon_v=1\) only for root \(y\). The falling factorial counts injective choices of actual leaf labels. Whether the pattern parks successfully depends only on the core, equality patterns and the fixed root: an unused pendant cannot be entered from any other vertex while moving towards the root. Consequently this orbit sum is an *exact polynomial identity for every* \(a,b\ge1\), of total degree at most four. The standalone checker enumerates every canonical pattern, applies the deterministic parking rule, forms all six symbolic polynomials, and simplifies the five differences to the displayed identities. No numerical interpolation is used. Positivity for \(a,b\ge3\) follows term by term. Every diameter path in \(B(a,b)\) joins a pendant at \(u\) to one at \(v\) and has four edges, whereas \(c\) has eccentricity three.

**3. Sharp finite cutoff.** Generate each unlabelled free tree on \(n=1,\ldots,10\) vertices exactly once using the standard nonisomorphic-tree generator, and verify the known type counts

\[
1,1,1,2,3,6,11,23,47,106.
\]

For each such tree, each \(m=1,\ldots,n\), and each possible root, evaluate the exact integer recurrence from Step 1. Compare the largest count among diameter endpoints with the largest count among all vertices. The checker executes \(16755\) root/load evaluations. All cases through order nine pass; among order-ten trees the only failures are \(B(3,3)\) with \(m=4\) and \(m=5\). This is an exhaustive finite computation because the generated tree types cover all free trees at each listed order, all admissible loads are iterated, and no roots are skipped. The independent direct enumerator checks the \(10^4\) and \(10^5\) possible preference sequences for each of four symmetry-representative roots of \(B(3,3)\), agreeing with Step 1. This establishes the sharpness and the values asserted above.

## Verification

Execute `python checker.py` with the versions in `requirements.txt`. The checker prints success only after verifying: (i) exhaustive direct preference enumeration for the ten-vertex witness at four and five cars, (ii) all unlabelled tree types through ten vertices and all loads and roots, (iii) the exact six orbit polynomials and their five identities, and (iv) independent evaluations of those symbolic formulas on several parameter pairs. The observed output is `ALL CHECKS PASSED`. All numerical comparisons use exact integers; the polynomial calculations use exact symbolic arithmetic.

## Relationship to prior work

Curien and Hénard, *The Phase Transition for Parking on Galton–Watson Trees* (arXiv:1912.06012, first publicly submitted December 12, 2019; primary MSC 60C05), develops the same root-directed parking process, including its Abelian flux law, but studies random Galton–Watson trees and large-scale phase transitions rather than the best root of a fixed free tree. King and Yan, *Prime Parking Functions on Rooted Trees* (arXiv:1804.01616), gives a subtree-count criterion for full parking when the number of drivers equals the number of vertices, not the present all-load root-placement cutoff. King and Yan, *Parking Functions on Directed Graphs and Some Directed Trees* (DOI 10.37236/9051), gives a general reachability/Hall characterization and studies source-versus-sink orientation, not the ten-vertex diameter-endpoint comparison or the infinite \(B(a,b)\) formula. The broader prior criteria are compatible with and can underpin computation of the new finite counts; the claim is **not** that root-directed parking itself or its general enumeration recurrences are new.

## Limitations

The exhaustive minimality assertion stops at ten vertices. No classification of all larger trees, all optimal roots for loads above four, or all graph orientations is claimed. The infinite family is proved specifically for exactly four uniformly preferring cars. The finite checker depends on the documented completeness of the nonisomorphic-tree generator; standard tree counts are checked independently as a coverage safeguard. These are exact mathematical results subject to independent historical-priority and proof review, not independently certified discoveries.

## References

1. N. Curien and O. Hénard, *The Phase Transition for Parking on Galton–Watson Trees*, arXiv:1912.06012 (v1, 2019-12-12), *Discrete Analysis* 2022:1, DOI: 10.19086/da.33167. https://arxiv.org/abs/1912.06012
2. W. King and C. H. Yan, *Prime Parking Functions on Rooted Trees*, arXiv:1804.01616 (v1, 2018-04-04), *J. Combin. Theory A* 168 (2019), 1–25. https://arxiv.org/abs/1804.01616
3. W. King and C. H. Yan, *Parking Functions on Directed Graphs and Some Directed Trees*, *Electronic Journal of Combinatorics* 27(2) (2020), P2.48, DOI: 10.37236/9051. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v27i2p48
4. Q. Chen and C. Goldschmidt, *Parking on a Random Rooted Plane Tree*, arXiv:1911.03816 (2019-11-10). https://arxiv.org/abs/1911.03816
