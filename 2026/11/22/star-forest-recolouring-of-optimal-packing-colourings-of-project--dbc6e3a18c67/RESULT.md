# Star-forest recolouring of optimal packing colourings of projective-plane incidence graphs

## Finding

Let \(\Pi\) be any finite projective plane of order \(q\ge2\), let \(v=q^2+q+1\), and let \(G\) be its bipartite point–line incidence graph. A *packing colouring* assigns names \(1,\ldots,k\) to vertices, requiring vertices of the same name \(i\) to be more than distance \(i\) apart. Give two colourings an edge when they differ at exactly one vertex and both use the *minimum possible palette* \(\{1,\ldots,\chi_\rho(G)\}\). Distinct colour names are distinguished; names cannot be permuted during a single move.

**Theorem.** The known optimum palette size is \(\chi_\rho(G)=v+1\). The following classification and reconfiguration assertions hold for every such plane, including non-Desarguesian ones:

1. Every optimal colouring has one of precisely two forms. Choose a shore \(A\) (all points or all lines) and an opposite-shore element \(b\). In type I, every element of \(A\) has colour 1, \(b\) has colour 2, and the other \(v-1\) opposite-shore elements receive distinct names \(3,\ldots,v+1\). In type II, choose one \(x\in A\) *not incident* with \(b\), recolour \(x\) from 1 to 2, and leave all remaining names fixed. These exhaust the optimum colourings.
2. There are exactly \(2v(1+q^2)(v-1)!\) **named** optimal colourings, and exactly \(2v(1+q^2)\) optimal colour-class configurations after forgetting only the assignments of the singleton names \(3,\ldots,v+1\).
3. Their one-vertex recolouring graph is exactly
   \[
   \mathcal R_{\mathrm{opt}}(G)\cong \bigsqcup^{\,2v(v-1)!}K_{1,q^2}.
   \]
   It has \(2vq^2(v-1)!\) edges, no isolated configurations, and every component has diameter two. The type I configurations are the star centres and type II configurations are the leaves.

In particular, for the Fano-plane incidence graph (the Heawood graph), there are \(50{,}400\) named eight-colour optima forming \(10{,}080\) disjoint copies of \(K_{1,4}\). At order three there are \(260\) singleton-name-free configurations, forming \(26\) copies of \(K_{1,9}\).

## Assumptions and scope

A projective plane of order \(q\) has \(v=q^2+q+1\) points and the same number of lines; each point is incident with exactly \(q+1\) lines, each line contains \(q+1\) points, and each pair of distinct points (lines) determines exactly one line (intersection point). Existence is assumed, not asserted, for general \(q\). The graph has \(2v\) vertices, is connected and regular of degree \(q+1\), and has diameter three. The recolouring graph uses the full **named** optimum palette, not colour-permutation equivalence, Kempe moves or simultaneous exchanges. For colours \(i\ge3\) there may be at most one vertex of each colour because the graph diameter is three.

## Proof

**Step 1 — metric and packing bounds.** Distinct vertices on the same shore have distance two. A point and a line have distance one if incident, and three if nonincident. Consequently a 2-packing contains at most two vertices; if it contains two, they must be a nonincident point–line pair. A regular bipartite graph has a perfect matching, so any independent set contains at most one endpoint of each of the \(v\) matched edges and therefore has size at most \(v\).

**Step 2 — a sharp mixed-shore independence gap.** We prove that an independent set meeting both shores has size at most \(v-q\). Let \(T\) be its nonempty set of selected lines, write \(t=|T|\), and let \(N(T)\) be their point-neighbourhood. Because at least one selected point lies on no line of \(T\), all lines through that point are absent, so \(1\le t\le v-(q+1)=q^2\). For each point \(p\), put \(m_p=|\{\ell\in T:p\in\ell\}|\). The incidence axioms give
\[
\sum_p m_p=(q+1)t,\qquad
\sum_p m_p^2=(q+1)t+t(t-1)=t(t+q).
\]
Cauchy–Schwarz on points in \(N(T)\) yields
\[
|N(T)|\ge\frac{t(q+1)^2}{t+q},\qquad
|N(T)|-t\ge\frac{t(v-t)}{t+q}\ge q.
\]
The last inequality is equivalent to \((t-1)(q^2-t)\ge0\), valid throughout the stated interval. The selected point set is contained in the complement of \(N(T)\), so the whole independent set has size at most \(t+v-|N(T)|\le v-q\). Since \(q\ge2\), an independent set of size at least \(v-1\) is contained entirely in one shore; thus the size-\(v\) independent sets are exactly the two shores, and the size-\(v-1\) independent sets are precisely those shores with one element deleted.

**Step 3 — optimum and exhaustion.** With \(k\) colours, at most \(v\) vertices carry colour 1, at most two carry colour 2, and at most \(k-2\) carry higher colours. Hence \(2v\le v+k\), so \(k\ge v\). Equality \(k=v\) would require \(v\) vertices of colour 1 and two of colour 2. By Step 2, colour 1 then fills a shore, forcing colour 2 entirely into the opposite shore, where two vertices have distance two: impossible. Thus \(k\ge v+1\), and a type I colouring shows equality. At palette \(v+1\), omitting any higher colour would again force the forbidden pair \((|C_1|,|C_2|)=(v,2)\), so all \(v-1\) higher names occur exactly once. Therefore \(|C_1|+|C_2|=v+1\), with possibilities \((v,1)\) or \((v-1,2)\). Step 2 confines \(C_1\) to one shore. In the second case the two colour-2 vertices must be the unique missing same-shore element \(x\) and an opposite-shore element \(b\) nonincident with \(x\). This proves the classification.

**Step 4 — count.** Choose either shore, then \(b\) in the opposite shore (\(v\) choices), and bijectively assign the \(v-1\) singleton names to the remaining opposite-shore vertices (\((v-1)!\) choices). Each resulting type I colouring has precisely \(v-(q+1)=q^2\) choices of nonincident \(x\) producing type II. Each type II colouring uniquely recovers its type I parent, so counting introduces no duplicates.

**Step 5 — all possible recolourings.** Every name \(i\ge3\) is already used and cannot be duplicated because the diameter is three. A vertex currently carrying such a name lies opposite the almost-full colour-1 shore and has at least \(q\ge2\) adjacent vertices coloured 1, so cannot change to 1. It cannot change to 2: in type I its shore already contains the colour-2 vertex \(b\) (distance two), and in type II colour 2 is already a maximum two-packing. Thus singleton-name vertices never move. No colour-1 vertex can change to any already-used higher name, and its only possible move is to colour 2 when the configuration is type I; this is legal exactly for the \(q^2\) elements \(x\) nonincident with \(b\). In type II, the only possible move is to return \(x\) from 2 to 1: the opposite-shore vertex \(b\) is adjacent to \(q+1\) colour-1 vertices, so cannot switch to 1. Hence every type I colouring is the unique centre of a \(q^2\)-leaf star. The stars partition all states.

## Verification

The standalone programs `verification/check_fano.py` and `verification/check_pg3.py` are included. Run with `python verification/check_fano.py` and `python verification/check_pg3.py` using Python 3. The first enumerates all \(2^{14}\) vertex subsets, constructs all \(50{,}400\) named optimal Fano-colourings, and checks every potentially valid one-vertex replacement into colours 1 or 2 against graph distances; all moves into a different higher colour are excluded because every higher colour is already used and the diameter is three. Its actual output confirms degree histogram \(\{1:40320,4:10080\}\) and \(40{,}320\) edges. The second independently constructs the order-three projective plane using homogeneous coordinates, enumerates near-maximum independent sets, checks all \(260\) optimum colour-class configurations, and directly enumerates colour-1/colour-2 vertex moves to obtain degree histogram \(\{1:234,9:26\}\). The second program checks the reduced class graph rather than the astronomically large named-colouring graph; the passage from reduced classes to named states is proved in Step 5. Finite computations check small instances but are not offered in place of the all-order proof.

## Relationship to prior work

The *packing chromatic number* \(\chi_\rho(G)=q^2+q+2\) for projective-plane incidence graphs is **previously established**, particularly in Fresán-Figueroa, González-Moreno and Olsen (2019), Theorem 3.1, whose Lemma 3.1 also proves that maximum independent sets are the two shores. The present statement does **not** claim either fact as new. Its additional contributions are the near-maximum independence gap for mixed shores, the exact exhaustive characterization and enumeration of named optimum packings, and the complete one-vertex optimal-recolouring graph. The original broadcast-colouring framework was introduced by Goddard and collaborators (2008). Related exact domination-colouring results on these incidence graphs use a different admissibility condition and do not imply packing-colouring mobility; ordinary proper recolouring and graph-edge changes likewise concern different moves or state spaces.

## Limitations

The theorem is conditional on existence of the projective plane and covers \(q\ge2\), not the order-one degenerate triangle. It treats optimal palette colourings only, with fixed colour names and one-vertex moves. It says nothing about recolouring with an extra colour, permuting names in one move, or a sequence of non-optimal states. The exact palette size is credited to the 2019 literature. The finite verifiers do not certify the infinite statement independently of its proof, and an unindexed equivalent earlier classification cannot be excluded.

## References

1. W. Goddard, S. M. Hedetniemi, S. T. Hedetniemi, J. M. Harris, D. F. Rall, *Broadcast Chromatic Numbers of Graphs*, Ars Combinatoria **86** (2008), 33–49. Published 2008-01-31. https://combinatorialpress.com/ars-articles/volume-086-ars-articles/broadcast-chromatic-numbers-of-graphs/
2. J. Fresán-Figueroa, D. González-Moreno, M. Olsen, *On the packing chromatic number of Moore graphs*, arXiv:1909.11638 (first submitted 2019-09-25), Theorem 3.1 and Lemma 3.1. https://arxiv.org/abs/1909.11638
3. W. Goddard and H. Xu, *The S-packing chromatic number of a graph*, Discussiones Mathematicae Graph Theory **32** (2012), 795–806. https://doi.org/10.7151/dmgt.1642
