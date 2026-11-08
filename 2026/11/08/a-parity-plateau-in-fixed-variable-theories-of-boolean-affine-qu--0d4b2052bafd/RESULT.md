# A parity plateau in fixed-variable theories of Boolean affine quadruple systems

## Finding
For every integer \(d\ge 0\), define the finite relational structure
\[
\mathcal A_d=(\mathbb F_2^d;P),\qquad
P(a,b,c,e)\iff a+b+c+e=0.
\]
Only equality and the displayed **quaternary relation** belong to the signature; there is no named origin, group operation, extra relation, or counting quantifier. For integers \(k\ge1\), set
\[
\tau(k)=\begin{cases}
0,&k=1,\\
k-1,&2\le k\le5,\\
k-2,&k\ge6\text{ even},\\
k-1,&k\ge7\text{ odd}.
\end{cases}
\]
Then for all integers \(d,e\ge0\), counting-free first-order logic with at most \(k\) distinct reusable variable names, at **unrestricted quantifier depth**, satisfies
\[
\boxed{\mathcal A_d\equiv_{\mathrm{FO}^k}\mathcal A_e
\quad\Longleftrightarrow\quad
\min\{d,\tau(k)\}=\min\{e,\tau(k)\}.}
\]
In particular, \(\mathcal A_4\equiv_{\mathrm{FO}^6}\mathcal A_5\), although the structures have respectively \(16\) and \(32\) points, but \(\mathcal A_4\not\equiv_{\mathrm{FO}^7}\mathcal A_5\). Exactly \(\tau(k)+1\) different \(\mathrm{FO}^k\) theories occur as \(d\) varies. There is a genuine equality of the entire theory partitions at widths \(5\) and \(6\), \(7\) and \(8\), and so on, whereas the other adjacent widths separate previously indistinguishable dimensions.

For \(d\ge2\), the distinct-point quadruples satisfying \(P\) are precisely the affine two-planes of \(\operatorname{AG}(d,2)\), the blocks of the Boolean Steiner quadruple system. In the usual four-place block language, \(P\) is interdefinable at width four with the block relation and equality: \(P(a,b,c,e)\) holds exactly when the four entries are distinct and constitute a block, or each value occurs an even number of times. Thus the displayed classification also applies to standard Boolean Steiner quadruple systems for \(d\ge2\), including all widths below four (where the block relation cannot hold on tuples using fewer than four distinct positions).

## Assumptions and scope
The vector spaces are finite, binary, and may have dimension zero (the one-point structure). The relation is interpreted on *all* ordered quadruples, including repeated entries. In the Steiner-design interpretation, a block is an unordered **four-element** subset, and dimensions below two are excluded. All comparisons are relative to this particular family, not among arbitrary four-uniform hypergraphs. Equality is logical equality. The language is relational, not functional: writing the vector-space addition in the semantic definition does not make addition a term-forming symbol in formulas.

## Proof
**1. Even affine dependencies are expressible with one auxiliary name.** For an even integer \(r\ge2\) and point variables \(x_1,\dots,x_r\), write \(E_r(x_1,\ldots,x_r)\) for \(x_1+\cdots+x_r=0\). The case \(r=2\) is equality, and \(E_4\) is atomic \(P\). For every even \(r\ge6\), define recursively
\[
E_r(x_1,\ldots,x_r):=\exists y\,[P(x_1,x_2,x_3,y)\land E_{r-2}(y,x_4,\ldots,x_r)].
\]
The existential witness is uniquely determined by the first three arguments. The recursion therefore expresses precisely the desired parity equation. It uses at most \(r+1\) different variable names, not a new name at each level: within the recursive conjunct, unused names among \(x_1,x_2,x_3\) may be rebound locally as auxiliaries. For example \(E_6\) uses seven names. The formula for a particular six-subtuple of seven named points can reuse the seventh name locally, without changing its value in other conjuncts.

Call an ordered tuple of \(s\) points *affinely independent* when its \(s-1\) differences from the first point are linearly independent. Over \(\mathbb F_2\), affine dependence is equivalent to some **nonempty even** subset of the points having zero sum. Consequently, the existential statement that \(s\) points are affinely independent can be written as a conjunction of negations of \(E_r\), over all even index subsets of sizes \(2\le r\le s\). For \(s\le3\), pairwise inequality suffices; for \(s=4\), \(E_4\) itself uses four names; for \(s\ge5\), the displayed recursion gives width at most \(s\) if \(s\) is odd, and at most \(s+1\) if \(s\) is even. A set of \(s\) affinely independent points exists in \(\mathcal A_d\) if and only if \(d\ge s-1\). The witnesses for \(d\ge s-1\) are an arbitrary origin followed by \(s-1\) independent directions.

If \(d<e\) and \(d<\tau(k)\), choose \(s=d+2\). Then the existence of \(s\) affine-independent points is a \(k\)-variable sentence, true in \(\mathcal A_e\) and false in \(\mathcal A_d\). Indeed, \(s\le\tau(k)+1\), and at the maximal even number \(k\ge6\) the largest allowed \(s=k-1\) is odd, whereas at odd \(k\ge5\) the maximal \(s=k\) is odd. The small widths \(2,3,4\) follow directly from pairwise inequality and atomic \(P\). At \(k=1\), all nonempty members have the same one-variable theory.

**2. A permanent pebble strategy proves the converse.** Consider a position of the \(k\)-pebble game and regard its pebbled points as an indexed tuple, allowing repetitions. For odd \(k\ge5\), maintain all even-subset zero-sum dependencies of sizes at most \(k-1\) among the currently pebbled coordinates; for even \(k\ge6\), maintain those of sizes at most \(k-2\). For \(k=4\), preserve dependencies of sizes \(2\) and \(4\), and for \(k=2,3\), preserve equalities. Each invariant preserves all atomic equalities and all atomic instances of \(P\), because any four-place atom with repeated variables reduces to equality or to a four-distinct-coordinate dependence.

Before each move remove the selected pebble, leaving at most \(k-1\) named points. All affine dependencies among these surviving points are then preserved: an affine dependence in characteristic two has even support, and the maximum even support among \(k-1\) positions is exactly \(k-1\) if \(k\) is odd and \(k-2\) if \(k\) is even. Hence there is a unique affine isomorphism between the **affine spans of the surviving configurations** taking corresponding points to one another. It also preserves repeated positions. If Spoiler's new point belongs to that span, Duplicator takes its affine-isomorphic image, preserving every dependence in the full pebbled tuple.

If Spoiler chooses outside the surviving span, Duplicator also chooses outside the corresponding span whenever possible. For odd \(k\ge3\), the dimension threshold \(\tau(k)=k-1\) exceeds the maximum possible span dimension \(k-2\). For \(k=4\), \(\tau(k)=3\) likewise exceeds the maximum survivor span dimension \(2\); and for \(k=2\) the same holds. Therefore in these cases an outside point is always available on both sides, provided both dimensions are at least \(\tau(k)\).

The only exceptional situation is even \(k\ge6\), where \(\tau(k)=k-2\), and the surviving \(k-1\) points may already be affinely independent and span the entire smaller space. If a new point outside the span is played in the larger space, Duplicator answers in the smaller space with the **sum of all \(k-1\) surviving points**. Since \(k-1\) is odd, this is an affine combination; its addition creates only the single full-support dependency of size \(k\), and no zero-sum dependency of size at most \(k-2\). This is exactly the dependence invisible to the maintained invariant, and to the four-place atomic language (\(k\ge6\)). If the survivor span is proper, there is an outside reply in both structures instead. The argument is symmetric in which structure Spoiler chooses. Thus Duplicator can maintain the invariant after every move indefinitely.

For \(k\ge2\), if both dimensions are at least \(\tau(k)\), this permanent strategy gives equivalence at *every* quantifier depth. If both dimensions lie below the threshold but agree after truncation, they are equal and the structures are isomorphic. This proves both implications and the theory count. The width plateaux follow directly from \(\tau(2j+1)=\tau(2j+2)=2j\) for \(j\ge2\).

**3. Distinct-point Steiner blocks.** With four variables, the atomic Boolean quadruple condition is the disjunction of (i) blockhood on four pairwise distinct entries and (ii) the equality configurations with even multiplicities. In the reverse direction, blockhood is \(P\) conjoined with pairwise distinctness. These translations do not increase variable count. For fewer than four variables, any four-place block atom with repeated variable names is false, so only equality patterns are visible; the low-width cases of the theorem therefore agree in both signatures.

## Verification
The standalone `affine_pebble.py` enumerates affine tuple orbits of finite binary spaces by greedy independent-difference normal forms, creates every one-coordinate pebble successor, and computes the greatest colour refinement of the resulting finite labelled transition system. It independently confirms the six-variable equivalence of dimensions four and five, five-variable equivalence of dimensions four and five, four-variable equivalence of dimensions three and four, and seven-variable distinction of dimensions four and five. It also tests multiple sharp lower boundaries. The script's printed rounds are *algorithmic refinement rounds*, not first-order quantifier-depth bounds.

The separate `check_affine_algebra.py` directly evaluates the recursive even-sum formulas against XOR parity for \(71{,}388\) complete/sampled tuples and checks standard affine-independent witnesses across dimensions zero through six. Run with `python affine_pebble.py` and `python check_affine_algebra.py` in a directory containing those files. Their captured outputs are also included. These finite checks corroborate the explicit infinite proof; no enumeration is asserted to prove the theorem for arbitrary dimensions or variable widths.

## Relationship to prior work
Grohe and Otto (2012, arXiv:1204.1990) study counting and counting-free pebble games through graph isomorphism and Boolean-semiring linear systems. Their graph-algorithm results and more general game methodology do not give a dimension-indexed classification of four-ary Boolean affine structures; their conference paper explicitly focuses on graphs and notes the difficulty of higher-arity signatures. Zinoviev and Zinoviev (2007) study the Boolean Steiner quadruple systems as minimum-rank incidence designs and classify low-rank designs; those incidence/coding results do not imply a bounded-variable first-order theory classification. Kuusisto, Meyers and Virtema (2012) consider first-order theories of monadic expansions of real-affine betweenness geometries, with a different ambient domain and signature.

The closely related group representation \((\mathbb F_2^d;R,0)\), with ternary **relational addition** and a named zero, is not variable-width-identical to the unpointed four-ary affine structure. Choosing a parameter as origin transforms \(P\) into relational addition only with an extra permanently occupied name; conversely, defining \(P\) from ternary addition requires an existential intermediate sum. Consequently, a width classification in that pointed ternary signature does not automatically imply the present alternating-width formula. General back-and-forth methodology is classical; the exact affine/dimensional parity threshold is the distinct claim here.

## Limitations
Historical-priority verification is not exhaustive; a general published theorem about torsors, finite-variable logic, or Boolean Steiner quadruple systems may subsume the formula. No independent mathematical audit has been performed. The equivalence is only for these Boolean affine examples in the pure four-ary language; it says nothing about arbitrary Steiner quadruple systems, counting logic, adding a named origin, an operation symbol, or other fields. Computation is finite corroboration, not a certificate of the unrestricted theorem.

## References
1. Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990 (first posted 2012-04-09); CSL 2012, DOI 10.4230/LIPIcs.CSL.2012.289.
2. V. A. Zinoviev and D. V. Zinoviev, *On Resolvability of Steiner Systems \(S(v=2^m,4,3)\) of Rank \(r\le v-m+1\) over \(\mathbb F_2\)*, Problems of Information Transmission 43 (2007), 33–47, DOI 10.1134/S003294600701005X.
3. Antti Kuusisto, Jeremy Meyers and Jonni Virtema, *Undecidable First-Order Theories of Affine Geometries*, arXiv:1208.4930 (first posted 2012-08-24); CSL 2012, DOI 10.4230/LIPIcs.CSL.2012.470.
