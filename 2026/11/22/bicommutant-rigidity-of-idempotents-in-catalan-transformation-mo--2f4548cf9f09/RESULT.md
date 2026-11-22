# Bicommutant rigidity of idempotents in Catalan transformation monoids

## Finding
For every integer \(n\ge 2\), let \(\mathcal C_n\) be the monoid of nondecreasing regressive maps of the chain \([n]=\{1,\ldots,n\}\), and write \(C(f)=\{g\in\mathcal C_n:g\circ f=f\circ g\}\). Let \(0\) denote the constant-one map and \(1\) the identity. For **every idempotent** \(e\in\mathcal C_n\),
\[
C(C(e))=Z(C(e))=\begin{cases}
\{0,1\},&e\in\{0,1\},\\
\{0,e,1\},&e\notin\{0,1\}.
\end{cases}
\]
Here \(C(C(e))\) means the set of elements commuting with **every** member of \(C(e)\), and \(Z(C(e))\) is the center of the centralizer submonoid. When \(n=1\), both sides consist of the unique map. In particular, every nontrivial idempotent is the unique nonzero, nonidentity central element of its centralizer: the full commutation structure reconstructs it.

## Assumptions and scope
Composition is conventional function composition \((f\circ g)(x)=f(g(x))\). The order relation is the usual total order. Every element of \(\mathcal C_n\) is order-preserving and satisfies \(f(x)\le x\). An idempotent \(e\) has fixed points \(S=\{s_1=1<s_2<\cdots<s_m\}\) and consecutive fiber blocks \(B_i=[s_i,s_{i+1}-1]\) for \(i<m\), with \(B_m=[s_m,n]\); on \(B_i\), \(e\) is constant \(s_i\). There are no restrictions on \(m\) or the block lengths. The conclusion concerns centers of full transformation centralizers, not merely the set of commuting idempotents.

## Proof
**1. The center of the whole Catalan monoid.** For \(2\le j\le n\), let \(t_j\) fix every point except \(j\), which it maps to \(j-1\). If \(h\) commutes with \(t_j\), comparison at \(j\) gives
\[
h(j-1)=t_j(h(j))=\begin{cases}j-1,&h(j)=j,\\h(j),&h(j)<j.\end{cases}
\tag{1}
\]
For every \(x\ne j\), the same commutation implies \(h(x)\ne j\): otherwise \((h\circ t_j)(x)=j\) while \((t_j\circ h)(x)=j-1\). A map central in \(\mathcal C_n\) commutes with all \(t_j\). Start with \(h(1)=1\). If \(h(2)=2\), relation (1), together with the exclusion of any other preimage of \(2\), inductively forces \(h(j)=j\) for every \(j\). If \(h(2)=1\), the same relation and exclusion inductively force \(h(j)=1\). Thus \(Z(\mathcal C_n)=\{0,1\}\) for \(n\ge2\). The same statement holds on the chain of \(m\) roots, with the singleton interpretation when \(m=1\).

**2. Elementary maps constrain any element of the double centralizer.** Fix an idempotent \(e\), and take \(h\in C(C(e))\). Since \(e\in C(e)\), automatically \(h\in C(e)\); hence \(C(C(e))=Z(C(e))\). Each \(t_j\) with \(j\notin S\) lies in \(C(e)\), because \(j\) and \(j-1\) belong to the same fiber block of \(e\). Apply (1) and the excluded-other-preimage observation at every such \(j\). Since \(h\in C(e)\), the images \(h(s_i)\) are fixed by \(e\), so each is some root \(s_{\tau(i)}\) with \(\tau(i)\le i\). The map \(\tau\colon[m]\to[m]\) is nondecreasing.

If \(h(s_i)<s_i\), recurrence (1) forces \(h\) to be constant on the entire block \(B_i\), with value \(h(s_i)\). If \(h(s_i)=s_i\), the same recurrence forces the restriction of \(h\) to \(B_i\) to be either the identity or the constant map with value \(s_i\). Indeed, the first nonroot position can either remain fixed or collapse to the root; any subsequent switch would violate (1) or give a second preimage of a nonroot position. This covers singleton blocks, on which the two choices coincide.

**3. The root action is central and therefore trivial or constant.** For every \(\sigma\in\mathcal C_m\), define \(g_\sigma\) to be constant \(s_{\sigma(i)}\) on \(B_i\). It is nondecreasing and regressive, and \(e\circ g_\sigma=g_\sigma\circ e=g_\sigma\). Thus \(g_\sigma\in C(e)\). The equality \(h\circ g_\sigma=g_\sigma\circ h\), evaluated on roots, gives \(\tau\circ\sigma=\sigma\circ\tau\). By Step 1, \(\tau\) is either the identity or the constant-one map on the root-index chain (which coincide when \(m=1\)).

If \(\tau\) is constant one and \(m\ge2\), every block after the first collapses to \(1\), and nondecreasingness forces the first block to collapse to \(1\) as well; hence \(h=0\). For \(m=1\), the block analysis already gives \(h\in\{0,1\}\).

**4. Mixed block behavior does not centralize.** Suppose \(\tau\) is the identity. Then on each non-singleton block, \(h\) either fixes every point or collapses the block to its left endpoint. Assume two non-singleton blocks \(B_i\) and \(B_j\), with \(i<j\), have different choices. Define \(g\) on blocks preceding \(B_i\) and following \(B_j\) to be the identity; on each \(B_k\) for \(i\le k<j\), set \(g\) constantly equal to \(s_i\); and on \(B_j\) set \(g(s_j)=s_i\) and \(g(x)=s_i+1\) for \(x>s_j\). Since \(|B_i|\ge2\), the two target values \(s_i,s_i+1\) both lie in \(B_i\). The map \(g\) is nondecreasing and regressive and maps each fiber of \(e\) into a fiber in a way compatible with the root action; hence \(g\in C(e)\). At \(x=s_j+1\),
\[
(h\circ g)(x)=h(s_i+1),\qquad(g\circ h)(x)=\begin{cases}s_i+1,&h|_{B_j}=\mathrm{id},\\s_i,&h|_{B_j}=e|_{B_j}.
\end{cases}
\]
The first expression is \(s_i+1\) precisely when \(h|_{B_i}\) is the identity, and otherwise \(s_i\). Since the two block choices differ, the compositions differ, contrary to the assumption on \(h\). Thus all non-singleton blocks have the same choice, so \(h=e\) or \(h=1\).

Finally, \(0\) and \(1\) are central in the whole monoid, and \(e\) is central in \(C(e)\) by definition. The candidates obtained in Steps 2–4 therefore all belong to \(Z(C(e))\). When \(e\) is neither constant nor identity these three maps are distinct; otherwise there are two. This establishes the theorem for all \(n\ge2\).

## Verification
The standalone C++17 file `check_bicommutant.cpp` exhaustively constructs all \(\mathcal C_n\) for \(1\le n\le8\), identifies every idempotent, explicitly constructs its centralizer and that submonoid's center, and compares both the size and exact members with the theorem. There are respectively \(1,2,5,14,42,132,429,1430\) monoid elements and \(1,2,4,8,16,32,64,128\) idempotents; all pass with final marker `CATALAN_BICOMMUTANT_OK`. Compile with `c++ -O3 -std=c++17 check_bicommutant.cpp -o check && ./check`. Finite checking does not establish the infinite theorem; Steps 1–4 provide the proof.

## Relationship to prior work
Stein's October 6, 2026 paper on the stylic-to-Catalan quotient identifies Catalan transformations, images, kernels, and idempotents, but its results concern quotient representations rather than the center of a centralizer. Konieczny and Korkmaz (first posted November 16, 2026) characterize full centralizers of Catalan monoid elements and enumerate the idempotent centralizers and certain subclasses. Their structural description is a particularly strong input against which this result was checked: a formula for \(C(e)\) neither states nor directly counts \(C(C(e))\), and the new proof determines all elements commuting simultaneously with the entire centralizer. Earlier published counts and compatibility results for pairs of commuting idempotents concern a smaller universe and likewise do not imply the full bicommutant statement. These distinctions are logical statements about what was established, not claims of exclusive priority.

## Limitations
The theorem is for **idempotents** of the ordinary order-preserving regressive Catalan monoid. It does not classify double centralizers of arbitrary non-idempotent transformations, nor does it claim analogous rigidity in other Catalan-like or full transformation monoids. The November 16 paper's explicit general centralizer characterization may permit an alternative derivation; the historical-priority comparison is provisional, particularly for specialist centralizer literature not fully accessible. The computational test ends at \(n=8\); no untested finite enumeration is used as an infinite argument.

## References
- Itamar Stein, *From stylic monoid to Catalan monoid*, arXiv:2610.07983v1, first public October 6, 2026. https://arxiv.org/abs/2610.07983
- Janusz Konieczny and Emrah Korkmaz, *Centralizers in Catalan Monoids*, arXiv:2611.21071v1, first public November 16, 2026. https://arxiv.org/html/2611.21071v1
- GAP Semigroups package documentation, *CatalanMonoid(n)*, defining generators and underlying transformation monoid. https://semigroups.github.io/Semigroups/doc/chap7_mj.html
