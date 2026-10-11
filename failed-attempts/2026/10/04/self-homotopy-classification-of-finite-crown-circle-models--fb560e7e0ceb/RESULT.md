# Self-homotopy classification of finite crown circle models
## Finding
For every integer \(n\ge 2\), let \(\mathfrak C_n\) be the \(2n\)-point crown poset with elements \(0,1,\ldots,2n-1\) modulo \(2n\), where each even point \(i\) is below the two odd points \(i-1\) and \(i+1\). Every monotone self-map \(f:\mathfrak C_n\to\mathfrak C_n\) has winding number \(\deg(f)\in\{-1,0,1\}\). The maps of winding \(1\) or \(-1\) are exactly the \(2n\) order automorphisms, with \(n\) of each winding, while every winding-zero self-map is null-homotopic through finite-space maps. Distinct automorphisms are not homotopic. Consequently \(\lvert[\mathfrak C_n,\mathfrak C_n]\rvert=2n+1\): one null class and one singleton class for each automorphism.

## Assumptions and scope
For an integer \(n\ge 2\), write \(\mathfrak C_n\) for the finite \(T_0\)-space whose specialization order has underlying set \(\mathbb Z/(2n)\), with even residues minimal, odd residues maximal, and cover relations \(i<i-1\) and \(i<i+1\) for each even \(i\). Continuous maps are exactly order-preserving maps. The order complex is a \(2n\)-cycle and therefore has the weak homotopy type of \(S^1\).

The winding number is the integer obtained from a lift to the infinite fence: if \(p_n:\mathbb Z\to\mathfrak C_n\) is reduction modulo \(2n\) and \(\widehat f\) is a lift of \(f p_n\), then
\[
\deg(f)=\frac{\widehat f(2n)-\widehat f(0)}{2n}.
\]
This agrees with the degree induced on the first homology of the order complex.

## Proof
Because consecutive points of the fence are comparable, order preservation implies
\[
\widehat f(i+1)-\widehat f(i)\in\{-1,0,1\}
\]
for every integer \(i\). Summing over one period gives
\[
2n\,|\deg(f)|=|\widehat f(2n)-\widehat f(0)|\le 2n,
\]
so \(\deg(f)\in\{-1,0,1\}\).

If \(|\deg(f)|=1\), equality holds in the preceding triangle inequality. Hence all \(2n\) increments are \(1\) when \(\deg(f)=1\), and all are \(-1\) when \(\deg(f)=-1\). Thus
\[
f(i)=a+i\pmod{{2n}}
\]
or
\[
f(i)=a-i\pmod{{2n}}.
\]
Order preservation of the relation \(0<1\) forces \(a\) to be even. These are exactly the \(n\) rotations by an even offset and the \(n\) reflections preserving the two levels of the crown. Therefore every nonzero-winding self-map is an order automorphism, and there are exactly \(2n\) of them.

Now suppose \(\deg(f)=0\). Choose the lift with \(\widehat f(2n)=\widehat f(0)\). If the image of \(f\) contained all \(2n\) residues, then the integer walk \(\widehat f(0),\ldots,\widehat f(2n)\) would have range width at least \(2n-1\). Any closed integer walk that reaches both extremes has total variation at least twice its range width, hence at least \(4n-2\). But this walk has only \(2n\) steps, each of absolute size at most \(1\), so its total variation is at most \(2n\), a contradiction for \(n\ge2\). Thus the image omits some point \(v\).

The subspace \(\mathfrak C_n\setminus\{v\}\) is an alternating finite fence. Removing endpoint beat points successively reduces it to a singleton, so it is contractible as a finite space. Hence every winding-zero map factors through a contractible subspace and is null-homotopic. Since the crown is connected, all constant maps are homotopic, so all winding-zero maps lie in one homotopy class.

Finally, \(\mathfrak C_n\) has no beat points: each minimal point has two distinct covers and each maximal point has two distinct lower covers. It is therefore a minimal finite space. For a minimal finite space, a self-map homotopic to the identity is the identity. If two automorphisms \(g,h\) were homotopic, then \(h^{-1}g\) would be homotopic to the identity, forcing \(g=h\). Therefore the \(2n\) automorphisms give \(2n\) singleton homotopy classes, disjoint from the single null class.

## Verification
The symbolic proof above is the infinite argument. The bundled standard-library script `verify_crown.py` independently enumerates all monotone self-maps for \(n=2,3,4,5\), computes winding from the cyclic edge walk, checks that every nonzero-winding map is an automorphism and that every winding-zero image omits a target point, and directly computes map-space comparability components for \(n=2,3,4\).

The replay gives \(36,234,1544,10030\) self-maps for \(n=2,3,4,5\), respectively. The nonzero-winding bins contain exactly \(n\) maps of each sign, and the direct component counts are \(5,7,9\) for \(n=2,3,4\), matching \(2n+1\). The final line is `VERIFY_OK`.

## Relationship to prior work
Barmak and Minian's archive preprint develops the finite-space framework used here: finite \(T_0\)-spaces as posets, continuous maps as order-preserving maps, Stong beat points and cores, and minimal finite models of graphs. It does not state a self-map classification for crown models.

Cavallo and Sattler later define the same crown posets via the infinite fence and define the winding number of maps between crowns. Their Appendix A proves that a map \(\mathfrak C_m\to\mathfrak C_n\) has zero winding when \(m<n\). The inspected appendix does not state the present equal-size classification, does not identify the nonzero-winding self-maps with automorphisms, and does not classify finite-space homotopy classes of crown self-maps. The present result uses their natural winding formalism and closes the self-map case exactly.

## Limitations
The theorem concerns endomorphisms of a single crown \(\mathfrak C_n\). It does not classify homotopy classes of maps \(\mathfrak C_m\to\mathfrak C_n\) for unequal \(m,n\), nor the full endomorphism monoid multiplication. The finite enumeration is only a regression check through \(n=5\); it is not used as proof for general \(n\). Search non-detection is not a proof of novelty, and older order-theory literature on fence or crown endomorphisms remains a residual bibliographic risk.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first posted 2006-11-06.
2. E. Cavallo and C. Sattler, *Relative elegance and Cartesian cubes with one connection*, Canadian Journal of Mathematics, DOI:10.4153/S0008414X25101466; Appendix A.2.2 defines crown posets and winding number and proves the shorter-to-longer zero-winding lemma.
