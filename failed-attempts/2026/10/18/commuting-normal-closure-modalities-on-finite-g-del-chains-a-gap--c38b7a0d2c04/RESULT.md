# Commuting normal closure modalities on finite Gödel chains: a gap classification

## Finding

For each integer \(n\ge2\), let \(G_n=\{0<1<\cdots<n-1\}\) denote the bounded finite Gödel chain. Call \(c:G_n\to G_n\) a *normal S4-style closure modality* if it preserves the least element and binary joins and satisfies \(x\le c(x)\) and \(c(c(x))=c(x)\) for every \(x\in G_n\). These conditions entail monotonicity. We count **ordered** pairs of such modalities on a fixed, labeled chain; no quotient by algebra isomorphisms is taken.

Every modality has a unique fixed-point set \(F\subseteq G_n\) containing the two endpoints and takes the form
\[
c_F(x)=\min\{f\in F:f\ge x\}.
\]
For two sets \(F,H\), let \(C=F\cap H\). The following are equivalent:

1. The modalities commute, \(c_F\circ c_H=c_H\circ c_F\).
2. Both composites equal \(c_C\).
3. For every pair \(a<b\) of consecutive elements of \(C\), at least one of the two sets \((F\setminus C)\cap(a,b)\) and \((H\setminus C)\cap(a,b)\) is empty.

Consequently, the number \(b_n\) of ordered commuting pairs is
\[
b_n=\sum_{\substack{k\ge1,\ d_1,\ldots,d_k\ge1\\ d_1+\cdots+d_k=n-1}}\prod_{i=1}^{k}(2^{d_i}-1)
=\frac{(2+\sqrt2)^{n-1}-(2-\sqrt2)^{n-1}}{2\sqrt2}.
\]
Equivalently,
\[
\sum_{n\ge2}b_nz^{n-1}=\frac{z}{1-4z+2z^2},\qquad b_2=1,\quad b_3=4,\quad b_n=4b_{n-1}-2b_{n-2}\quad(n\ge4).
\]
The first counts for \(n=2,\ldots,9\) are \(1,4,14,48,164,560,1912,6528\). All normal modalities number \(2^{n-2}\), so the commuting proportion among ordered pairs is \(b_n/4^{n-2}\), which tends to zero exponentially.

## Assumptions and scope

The carrier is a finite linear Heyting algebra with its usual total order, join, and endpoints. Normal means preserving the bottom element, and the stated closure conditions supply the analogues of inflationary and idempotent modal laws. Commuting means equality of the *two compositions on every element*, corresponding algebraically to an interchange identity. This is **not** a classification of arbitrary non-normal closure maps, higher-arity modalities, or topologies on an underlying discrete set. The two modalities may coincide.

## Proof

**Step 1: fixed-point form.** A join-preserving unary map on a chain is monotone: if \(x\le y\), then \(c(y)=c(x\vee y)=c(x)\vee c(y)\), implying \(c(x)\le c(y)\). Inflationarity and idempotence imply that \(c(x)\) is a fixed point above \(x\). If \(f\) is any fixed point above \(x\), monotonicity gives \(c(x)\le c(f)=f\). Hence \(c(x)\) is the *least* fixed point above \(x\). Inflationarity gives \(c(n-1)=n-1\); normality gives \(c(0)=0\). Conversely, every set \(F\) containing both endpoints defines upper rounding \(c_F\), which is bottom-preserving, monotone, extensive, idempotent, and binary-join-preserving. Therefore the correspondence is bijective.

**Step 2: necessity of the gap condition.** Suppose \(c_Fc_H=c_Hc_F\), and consider consecutive common fixed points \(a<b\) in \(C=F\cap H\). Suppose, for a contradiction, that \(u\in(F\setminus C)\cap(a,b)\) and \(v\in(H\setminus C)\cap(a,b)\). They are distinct. If \(u<v\), set \(t=c_H(u)\). Because \(u\notin H\), we have \(u<t\le v<b\), and \(t\in H\setminus C\). But \(c_F(u)=u\), so commutation yields \(c_F(t)=c_Fc_H(u)=c_Hc_F(u)=t\), forcing \(t\in F\cap H=C\), impossible between \(a,b\). If \(v<u\), swap the roles of \(F,H\) to obtain the same contradiction. Thus at most one modality has extra fixed points in each common gap.

**Step 3: sufficiency and the common composite.** Suppose the gap condition holds. For a common fixed point \(x\in C\), both modalities fix \(x\). For \(a<x<b\) in a common gap, both maps send the interval \((a,b]\) into itself, and at least one has no fixed point strictly between \(a\) and \(b\). If \(F\cap(a,b)=\varnothing\), then \(c_F(y)=b\) for every \(a<y\le b\), whence \(c_Fc_H(x)=c_Hc_F(x)=b\). The alternative \(H\cap(a,b)=\varnothing\) is symmetric. In either case \(b=c_C(x)\). This proves both compositions equal \(c_C\), and hence they commute. If they commute, Step 2 provides the gap condition and the same conclusion; all three statements are equivalent.

**Step 4: exact enumeration.** Order the common fixed points as \(0=a_0<a_1<\cdots<a_k=n-1\), giving positive gap lengths \(d_i=a_i-a_{i-1}\) whose sum is \(n-1\). Inside any gap there are \(d_i-1\) available points. By Step 2, each may be fixed by neither map or by exactly one map, but all noncommon fixed points in this gap must belong to *the same* map. The possibilities with only the first map having additional fixed points number \(2^{d_i-1}\), as do those for only the second map; their common empty choice is double counted. Thus each gap contributes \(2^{d_i}-1\) choices, independently of the other gaps. Summing over the positive compositions gives the stated formula.

Writing \(W(z)=\sum_{d\ge1}(2^d-1)z^d=z/((1-z)(1-2z))\), the generating function for nonempty concatenations of gaps is \(W(z)/(1-W(z))=z/(1-4z+2z^2)\). Partial fractions give the closed form and recurrence. Because the characteristic roots are \(2\pm\sqrt2\) and \(2+\sqrt2<4\), dividing by the \(4^{n-2}\) ordered pairs of all normal modalities gives exponential decay.

## Verification

The standalone `checker.py` enumerates every endpoint-containing fixed-point set for each \(2\le n\le9\), constructs every associated upper-rounding table, tests actual composition equality for all ordered pairs, compares that result to the common-gap criterion, and separately evaluates the positive-composition count. No sampling is used in these finite tests. Expected successful output ends with `TWO_S4_CHAIN_COMMUTATION_OK`. The all-\(n\) theorem follows from Steps 1–4, **not** from the finite checker.

## Relationship to prior work

Aguilera, Fernández-Duque, and Pacheco (2026) develop polytopological semantics for constructive and intuitionistic versions of modal \(\mathsf{K4}\) and \(\mathsf{S4}\), motivating a precise analysis of interactions of closure modalities. Their topological operators act on powersets, whereas the operators classified here act directly on finite Gödel-chain truth values; no equivalence between those model classes is asserted. Their paper does not provide this two-operator chain enumeration.

Santocanale (2019) describes the composition monoid of join-continuous maps on finite chains and classifies individual idempotents using discrete paths and emmentalers. The present theorem restricts to normal *extensive* idempotents and supplies the distinct, simultaneous two-map commutation criterion and exact joint census; the general monoid results are prior background and could offer an alternate route to the theorem.

The resulting number sequence is **already known**: \(b_n\) agrees with OEIS A007070 at index \(n-2\). That database lists the same recurrence and a generalized-composition interpretation but does not identify the above commuting-modality interpretation. Novelty is claimed only for the precise structural relationship between two modes and its specific counting application, not for the numeric sequence or general fixed-point rounding facts.

## Limitations

No claim is made for infinite chains, nonnormal operators, arbitrary lattices, or three or more commuting modalities. The exact numeric sequence has prior independent interpretations. The available comparative literature does not certify absolute historical priority: an older general theorem about commuting extensive semigroup idempotents could subsume this formulation. Historical priority remains uncertain.

## References

1. J. P. Aguilera, D. Fernández-Duque, L. Pacheco, *Polytopological Semantics for Intuitionistic Modal Logics* (2026), arXiv:2604.23234, first posted 25 April 2026. https://arxiv.org/html/2604.23234v1
2. L. Santocanale, *On discrete idempotent paths* (2019), arXiv:1906.05590. https://www.researchgate.net/publication/333773513_On_discrete_idempotent_paths
3. The On-Line Encyclopedia of Integer Sequences, A007070, sequence and generalized-composition formulas. https://oeis.org/A007070
