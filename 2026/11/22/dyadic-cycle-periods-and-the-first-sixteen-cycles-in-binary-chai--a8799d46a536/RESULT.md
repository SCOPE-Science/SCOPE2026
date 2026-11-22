# Dyadic cycle periods and the first sixteen-cycles in binary chain-ring structure graphs

## Finding
For every integer \(m\ge 1\), put \(R_m=\mathbb F_2[t]/(t^m)\) and let \(T_m:R_m^2\to R_m^2\) be the Vieta/structure-graph map \(T_m(a,b)=(a+b,ab)\). Its periodic-point set is exactly
\[
\{(a,0):a\in tR_m\}\ \sqcup\ \{(1+u,b):u,b\in tR_m\}.
\]
Every periodic orbit has power-of-two length. As \(m\) varies, these lengths are unbounded.

The **least** nilpotency length \(m\) for which a directed cycle of length \(16\) occurs is \(m=10\). At \(m=10\), the complete directed-cycle census is:

| Primitive period | Number of distinct directed cycles |
|---:|---:|
| \(1\) | \(1024\) |
| \(2\) | \(1280\) |
| \(4\) | \(5888\) |
| \(8\) | \(17152\) |
| \(16\) | \(6144\) |

There are no other directed cycles at \(m=10\). In particular the structure graph of \(R_{10}\) has exactly \(31488\) weakly connected components, one per directed cycle. The family \(R_m\) has no sixteen-cycle when \(m\le 9\).

## Assumptions and scope
Here \(t\) is the image of a polynomial indeterminate, \(tR_m\) is the maximal nilpotent ideal, and a periodic point is one satisfying \(T_m^r(a,b)=(a,b)\) for some positive integer \(r\). A primitive period is the least such positive integer. A directed cycle is counted up to cyclic rotation, not up to reversal; transient vertices are not cycles. All operations and coefficients are over \(\mathbb F_2\). The claims concern these truncated polynomial rings, not arbitrary chain rings or fields of characteristic two.

## Proof
**1. Periodic core.** Modulo \(t\), the four possible residue pairs follow \((0,0)\mapsto(0,0)\), \((1,0)\mapsto(1,0)\), \((0,1)\mapsto(1,0)\), and \((1,1)\mapsto(0,1)\). Thus any periodic pair has residues either \((0,0)\) or \((1,0)\). In the former case, both coordinates remain in \(tR_m\); while \(b\ne0\), the \(t\)-adic valuation of \(ab\) strictly exceeds the valuation of \(b\). Such an orbit reaches \(b=0\) and is periodic only if already fixed, giving the first displayed set.

In the second residue class write \(a=1+u\), with \(u,b\in tR_m\). The map becomes
\[
F_m(u,b)=(u+b,(1+u)b).
\]
Given output \((v,w)\), its preimage satisfies \(b=v+u\) and \(u^2+(1+v)u+v+w=0\). This equation has exactly one solution in \(tR_m\): solve its coefficients successively in increasing powers of \(t\). At each positive degree the still-unknown coefficient of \(u\) occurs with coefficient one, while all other terms are already determined. Therefore \(F_m\) is a permutation of \((tR_m)^2\); every point in this finite set is periodic.

**2. Dyadic periods.** Reduction from \(R_{m+1}\) to \(R_m\) intertwines the permutations on their periodic cores. Each fiber has two new binary coefficients, and changing them by \((x,y)\in\mathbb F_2^2\) changes the next coefficients by \((x+y,y)\). This is the order-two shear matrix \(M=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\). If the permutation at level \(m\) has order a power of two, its powered lift acts on each fiber as an affine map with linear part a power of \(M\); every such affine map has power-of-two order (at most four). Starting from the singleton core at \(m=1\), induction proves the assertion.

The allowed powers of two are unbounded. Indeed, over \(\mathbb F_2[u,b]\), write the \(n\)th iterate of \(F(u,b)=(u+b,(1+u)b)\) as \((P_n,Q_n)\). At \(n=1\), \(\deg P_1=1\), \(\deg Q_1=2\). Since
\[
P_{n+1}=P_n+Q_n,\qquad Q_{n+1}=(1+P_n)Q_n,
\]
and \(\deg Q_n>\deg P_n\ge1\), the degree pair evolves by \((d,e)\mapsto(e,d+e)\). Hence no positive iterate is the polynomial identity. A nonzero polynomial cannot vanish at every pair in the infinite set \((t\mathbb F_2[[t]])^2\), viewed inside \(\mathbb F_2((t))^2\). Therefore for every \(k\) some finite quotient \(R_m\) admits a core point moved by \(F_m^{2^k}\). Its period is a power of two greater than \(2^k\), proving unboundedness.

**3. Sharp absence through length nine.** Compute the eighth iterate symbolically over \(\mathbb F_2[u,b]\) and discard terms of total degree at least nine. Its two coordinate differences from the identity have no terms of total degree less than eight; their degree-eight parts are, respectively,
\[
H_1=u^2b^6+u^4b^4+u^6b^2+u^7b,
\]
\[
H_2=ub^7+u^3b^5+u^5b^3+u^6b^2.
\]
These polynomial identities are computed by eight explicit applications of the preceding recurrence and can be checked independently by `verify.py`. Both homogeneous forms are divisible by \(ub(u+b)\). For \(u,b\in tR_m\) over \(\mathbb F_2\), this product belongs to \(t^4R_m\): if both leading coefficients at degree one are nonzero, the degree-one coefficients of \(u+b\) cancel; otherwise at least one of \(u,b\) already lies in \(t^2R_m\). The remaining homogeneous factor of degree five belongs to \(t^5R_m\). Thus \(H_1,H_2\in t^9R_m\), and the discarded terms also lie in \(t^9R_m\). Consequently \(F_m^8\) is the identity on the periodic core for every \(m\le9\), and every other periodic point is fixed. No sixteen-cycle exists at these lengths.

**4. First sixteen-cycle.** In \(R_{10}\), start at \((a,b)=(1+t,t^2)\). Direct ring arithmetic yields
\[
T_{10}^{8}(1+t,t^2)=(1+t+t^9,t^2)\ne(1+t,t^2),
\]
and \(T_{10}^{16}(1+t,t^2)=(1+t,t^2)\). The period is exactly \(16\), establishing the claimed minimal length.

**5. Complete cycle census at length ten.** A complete finite evaluation of the core permutation on its \(2^{18}=262144\) elements gives the following exact fixed-point counts for the powers \(1,2,4,8,16\): respectively \(512,3072,26624,163840,262144\). A separate full functional-graph traversal of all \(2^{20}=1048576\) vertices yields the same primitive cycle counts. The additional \(512\) periodic points outside the core are fixed. Subtracting successive fixed-point counts and dividing by the primitive period gives the five entries in the table; the sum \(1024+1280+5888+17152+6144=31488\) is the component count. The standalone source and its exact output are included, not only summarized logs.

## Verification
Run `python3 verify.py` with the Python 3 standard library. It contains: (i) a degree-truncated symbolic iteration that reproduces both homogeneous eighth-iterate forms; (ii) a complete functional-graph traversal for every \(m\) from one through ten; (iii) a second, coefficientwise multiplication implementation that independently counts fixed points on the \(m=10\) periodic core; and (iv) an explicit sixteen-cycle witness test. `verification_output.txt` records the complete reference output, including `VERIFY_OK`.

The symbolic jet plus valuation argument proves the nonexistence of sixteen-cycles for **every** \(m\le9\) without extrapolating a partial census. The finite enumeration is exhaustive at \(m=10\), not an infinite-degree proof. The all-\(m\) claims are established by the separate algebraic arguments above.

## Relationship to prior work
Chernev and Chernev, *On the Connected Components of Structure Graphs of Associative Rings* (arXiv:2611.07521v1, November 5, 2026) study when these directed graphs have only fixed-point components. They cite the established criterion for the existence of a two-cycle in rings with nonzero nilpotents and test selected finite fields. Their conclusion explicitly identifies longer cycle lengths as a future direction. The present statement treats the different question of complete primitive periods in one natural nonreduced chain-ring tower, proves unbounded dyadic periods, locates its first sixteen-cycles, and gives an exact census at that threshold.

Lipkovski's earlier foundational work introduces the Vieta map, and Lipkovski–Daoub–Shafah (2022) study cycles for residue rings \(\mathbb Z/n\mathbb Z\). None of those statements implies the cutoff or counts for \(\mathbb F_2[t]/(t^{10})\). Earlier analyses of the same map on finite fields use reduced rings and likewise do not imply nilpotent-thickening behavior.

## Limitations
The numerical census is specific to \(\mathbb F_2[t]/(t^{10})\); the theorem does not give a closed form for the number of cycles at every higher length or for all chain rings. The unboundedness argument is existential and does not determine the first occurrence of every larger dyadic period. Originality is judged relative to identified literature; unpublished or unindexed equivalent calculations cannot be ruled out, and no independent mathematical audit is claimed.

## References
1. A. M. Chernev and N. A. Chernev, *On the Connected Components of Structure Graphs of Associative Rings*, arXiv:2611.07521v1, first posted 2026-11-05. https://arxiv.org/abs/2611.07521
2. A. Lipkovski, *Structure graphs of rings: definitions and first results*, Fundamentalnaya i Prikladnaya Matematika (2015 original; English journal version 2017). https://research.matf.bg.ac.rs/handle/123456789/2452
3. A. Lipkovski, H. Daoub, and O. Shafah, *An Association between Digraphs and Rings*, Filomat 36(3), 2022. https://journal.pmf.ni.ac.rs/filomat/index.php/filomat/article/view/3518
