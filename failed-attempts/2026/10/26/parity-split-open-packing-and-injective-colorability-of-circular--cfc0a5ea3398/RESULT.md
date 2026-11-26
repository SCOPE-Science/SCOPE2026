# Parity-split open packing and injective colorability of circular prisms

## Finding
For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the circular prism with vertices \((i,t)\), where \(i\in\mathbb Z/n\mathbb Z\) and \(t\in\{0,1\}\). A set is an *open packing* when the open neighborhoods of any two of its distinct vertices are disjoint. Define its enumerator by
\[
\mathcal O_n(z)=\sum_{S\subseteq V(P_n)\;\mathrm{open\ packing}} z^{|S|}.
\]
For each integer \(m\ge3\), write
\[
I_m(z)=\sum_{j=0}^{\lfloor m/3\rfloor}
\frac{m}{m-2j}\binom{m-2j}{j}z^j.
\]
(The \(j=0\) summand is \(1\).) The exact all-set identity is
\[
\boxed{\mathcal O_n(z)=\begin{cases}I_n(z)^2,&n\text{ even},\\I_{2n}(z),&n\text{ odd}.\end{cases}}
\]
Equivalently, the common-neighbor graph of \(P_n\) is the disjoint union of two copies of \(C_n^2\) for even \(n\), and the single graph \(C_{2n}^2\) for odd \(n\). Here \(C_m^2\) joins two distinct cycle positions at circular distance at most two.

In particular, the maximum open packing cardinality and the number of such maximum sets with labeled vertices are
\[
\boxed{\rho^{\mathrm o}(P_n)=\begin{cases}2\lfloor n/3\rfloor,&n\text{ even},\\\lfloor2n/3\rfloor,&n\text{ odd},\end{cases}}
\qquad
\boxed{N_n=\begin{cases}b(n)^2,&n\text{ even},\\b(2n),&n\text{ odd},\end{cases}}
\]
where, writing \(m=3a+r\) and \(r\in\{0,1,2\}\),
\[
b(m)=\begin{cases}3,&r=0,\\m,&r=1,\\m(a+1)/2,&r=2.\end{cases}
\]
An *injective coloring* is a partition into open packings. Its minimum number of colors satisfies
\[
\boxed{\chi_i(P_n)=\begin{cases}3,&3\mid n,\\4,&3\nmid n.\end{cases}}
\]
Moreover, \(P_n\) has an injective coloring all of whose color classes are maximum open packings (is *perfect injectively colorable*) **if and only if** \(3\mid n\) or \(n\in\{4,8\}\).

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled as above. \(C_n\) means the usual simple cycle for \(n\ge3\); the product is Cartesian, not categorical. The open neighborhood \(N(v)\) excludes \(v\), and the empty set is counted in \(\mathcal O_n\). All equalities and classifications hold for every integer \(n\ge3\), without asymptotic qualifications. Colors are available as names but the perfect-colorability assertion is existential; \(N_n\) counts vertex subsets, not colors or dihedral orbits.

## Proof
**1. The conflict graph.** Let \(H_n\) have vertex set \(V(P_n)\), where distinct vertices are adjacent precisely when they possess a common neighbor in \(P_n\). A direct calculation from
\[
N(i,t)=\{(i-1,t),(i+1,t),(i,1-t)\}
\]
shows that \((i,t)\) and \((j,s)\) are adjacent in \(H_n\) if and only if exactly one of the following holds:
\[
\begin{aligned}
&t=s\quad\text{and}\quad j-i\equiv\pm2\pmod n,\\
&t\ne s\quad\text{and}\quad j-i\equiv\pm1\pmod n.
\end{aligned}
\]
For \(n=3\), the first condition also correctly records triangle-mediated common neighbors, since \(\pm2\equiv\mp1\pmod3\). No same-column cross-layer pair is conflicting.

If \(n\) is odd, the mapping \(f:\mathbb Z/(2n)\mathbb Z\to V(P_n)\) defined by \(f(k)=(k\bmod n,k\bmod2)\) is a bijection. Under \(f\), cyclic steps of one flip the layer and steps of two preserve it. The displayed adjacency criterion therefore identifies \(H_n\cong C_{2n}^2\).

If \(n\) is even, \(i+t\pmod2\) is constant along every conflict edge. Each parity class contains exactly one vertex in every column \(i\); restriction to that class identifies conflicting pairs with column separations of one or two. Thus \(H_n\cong C_n^2\sqcup C_n^2\). In every case an open packing in \(P_n\) is precisely an independent set of \(H_n\).

**2. Exact independence polynomial.** For \(m\ge3\), an independent subset of \(C_m^2\) of size \(j\ge1\) is a circular selection of \(j\) positions whose consecutive cyclic gaps are all at least three. Writing these gaps as \(3+h_1,\ldots,3+h_j\), with \(h_i\ge0\) and \(\sum_i h_i=m-3j\), there are \(\binom{m-2j-1}{j-1}\) ordered gap vectors. Choosing an initial marked selected position gives \(m\) choices, while each unmarked selected set was counted \(j\) times. Hence the coefficient is
\[
\frac mj\binom{m-2j-1}{j-1}
=\frac{m}{m-2j}\binom{m-2j}{j}.
\]
The empty set contributes one. Independence polynomials multiply under disjoint union, so part 1 proves the displayed formula for \(\mathcal O_n\).

**3. Maxima and their counts.** The nonnegative coefficients of \(I_m(z)\) occur exactly in degrees \(0,\ldots,\lfloor m/3\rfloor\). Thus its highest degree is \(a=\lfloor m/3\rfloor\). Writing \(m=3a+r\), \(0\le r\le2\), its leading coefficient is
\[
\frac ma\binom{a+r-1}{a-1}
=\begin{cases}3,&r=0,\\m,&r=1,\\m(a+1)/2,&r=2.\end{cases}
\]
The degree and leading coefficient of the product \(I_n(z)^2\) are twice the degree and the square of the leading coefficient, respectively. This proves both exact extremal formulas, including \(n=3,4\).

**4. Injective chromatic number.** Every three consecutive vertices of \(C_m^2\) form a triangle. In a proper three-coloring, the colors are therefore forced to repeat after every third position, which closes around the cycle exactly when \(3\mid m\). Conversely, when \(3\mid m\) the cyclic repetition of \(123\) is a proper three-coloring. For every even \(m\ge4\) not divisible by three, choose \(b=1\) if \(m\equiv1\pmod3\), or \(b=2\) if \(m\equiv2\pmod3\), and put \(a=(m-4b)/3\). Then \(a\ge0\), and the cyclic concatenation of \(a\) blocks \(123\) and \(b\) blocks \(1234\) is a proper four-coloring of \(C_m^2\). At all joins, including the cyclic join, vertices separated by one or two positions have distinct colors. Only even values \(m=n\) or \(m=2n\) arise in part 1; hence no exceptional five-cycle occurs. Since the chromatic number of a disjoint union is the maximum of its component chromatic numbers, \(\chi_i(P_n)=3\) for \(3\mid n\), and \(4\) otherwise.

**5. Perfect injective colorability.** If \(3\mid n\), repeat \(123\) on each component of \(H_n\); every color class has size \(\rho^{\mathrm o}(P_n)=2n/3\). If \(n=4\) or \(8\), use \(1234\) repeated in each of the two components \(C_n^2\); each class has \(n/2=2\lfloor n/3\rfloor\) vertices and is maximum.

Conversely, suppose \(3\nmid n\). The formulas in part 3 give \(n/2\le\rho^{\mathrm o}(P_n)<2n/3\), so any partition of \(2n\) vertices into maximum open packings must use an integer number of classes strictly greater than three and at most four. It must therefore use exactly four, with \(\rho^{\mathrm o}(P_n)=n/2\). If \(n\) is odd this is impossible because the left side is an integer and the right side is not. If \(n\) is even, the equation becomes \(n=4\lfloor n/3\rfloor\), whose only solutions with \(n\ge4\) are \(4\) and \(8\). This proves the asserted classification. \(\square\)

## Verification
The standalone `verify_prism.py` computes neighborhoods directly from the Cartesian product and reconstructs the common-neighbor graph without using the structural proof. For every \(3\le n\le10\), it exhaustively tests all \(2^{2n}\) vertex subsets against the original disjoint-open-neighborhood definition, and compares every coefficient with the formula. It also verifies the explicit conflict-graph isomorphism for those values, independently checks the adjacency structure for \(11\le n\le80\), and checks the cyclic coloring constructions and numerical necessary condition for \(3\le n\le300\). A total of 1,398,080 vertex subsets were tested. All tests passed; the exact program output is included as `verification_output.txt`. The finite tests are diagnostic, not a proof for arbitrary \(n\).

## Relationship to prior work
Brešar, Klavžar and Rall (2023), Theorem 2.2, prove \(\rho^{\mathrm o}(G\square K_2)=2\rho_2(G)\) when the base graph \(G\) is bipartite. This covers the *numerical maximum* for even cyclic prisms, but not the polynomial, the number of maximizers, the odd cases or perfect injective colorability. The full text studies bipartite prisms and hypercubes; the claimed classification concerns both bipartite and nonbipartite cycle bases.

Brešar, Samadi and Yero (2021; published 2023) formalize the two-step-graph interpretation of injective coloring and discuss perfect injective colorability of cycles and hypercubes. Those general definitions are used here, but their studied cycles are not the Cartesian cycle prisms, and their cycle coloring results do not identify the latter's common-neighbor graphs. Samadi, Soltankhah and Yero (2023) analyze primarily direct, lexicographic and corona products, not this Cartesian-prism all-set classification. The formula for \(I_m(z)\) is a direct self-contained cyclic-gap count, not a claim to have newly discovered cyclic packing enumeration in isolation.

## Limitations
The theorem is specific to \(C_n\square K_2\), with \(n\ge3\), and does not determine analogous polynomials for arbitrary prisms or higher-dimensional products. For even \(n\), the extremal cardinality itself is already implied by the published bipartite-prism theorem; the present additional claims are its exact full enumerator, optimizer count, injective coloring result and complete perfect-colorability classification. The bibliographic searches and inspected literature do not establish absolute priority; an unindexed equivalent classification remains a possible risk. The finite code checks do not substitute for the infinite combinatorial argument. No independent mathematical validation has been performed.

## References
1. B. Brešar, S. Klavžar and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1 (first posted 2023-09-10), Section 2, Theorem 2.2. https://arxiv.org/abs/2309.04963
2. B. Brešar, B. Samadi and I. G. Yero, *Injective coloring of graphs revisited*, arXiv:2106.09823v1 (first posted 2021-06-17); Discrete Mathematics 346 (2023), 113348. https://arxiv.org/abs/2106.09823
3. B. Samadi, N. Soltankhah and I. G. Yero, *Injective coloring of product graphs*, arXiv:2306.01488v1 (2023-06-02). https://arxiv.org/abs/2306.01488
4. D. A. Mojdeh, I. Peterin, B. Samadi and I. G. Yero, *(Open) packing number of some graph products*, Discrete Mathematics & Theoretical Computer Science 22 (2020), general product bounds.
