# Chromatic commutator length and nonzero fibers of radical-square-zero quiver algebras

## Finding

Let \(Q\) be any finite **loopless** quiver, with \(n\) vertices and \(m\) arrows (parallel and opposite arrows permitted), and let \(k=\mathbb F_q\) be any finite field. Write \(A=kQ/J^2\), where \(J\) is the arrow ideal; let \(G\) be its underlying undirected multigraph. For a radical element \(w=\sum_{e\in E(G)}\gamma_e e\), let \(S(w)=\{e:\gamma_e\ne0\}\) and let \(G[S(w)]\) be the spanning subgraph supported by those edges. Define the additive commutator length \(\ell_A(w)\) as the minimum number of terms \(x_i y_i-y_i x_i\) whose sum equals \(w\), with \(\ell_A(0)=0\).

**Chromatic length theorem.** Every associative commutator belongs to \(J\), every element of \(J\) is an additive sum of commutators, and for all \(w\in J\),
\[
\boxed{\ell_A(w)=\left\lceil\log_{q^2}\chi\bigl(G[S(w)]\bigr)\right\rceil.}
\]
Here the spanning graph with no edges has chromatic number one. In particular \(w\) is one commutator exactly when \(\chi(G[S(w)])\le q^2\), provided \(w\ne0\). The additive commutator width of \(A\) is therefore
\[
\boxed{\operatorname{cw}(A)=\left\lceil\log_{q^2}\chi(G)\right\rceil.}
\]
Both statements are independent of edge orientations and multiplicities except insofar as these determine which radical coordinates are supported.

**Exact individual fibers.** For \(w\in J\), put \(S=S(w)\), and let \(N_A(w)\) count ordered pairs \((x,y)\in A^2\) with \(xy-yx=w\). For a coloring \(c:V(G)\to k^2\), let \(h_{E\setminus S}(c)\) be the number of arrows outside \(S\) whose endpoints receive the same color. Then
\[
\boxed{N_A(w)=q^m\sum_{\substack{c:V(G)\to k^2\\c(u)\ne c(v)\text{ for }uv\in S}}q^{h_{E\setminus S}(c)}.}
\]
In particular, the fiber size depends only on the support \(S\), never on the individual nonzero coefficients of \(w\). Equivalently, for \(T\subseteq E\setminus S\), contract all edges of \(T\), retain the images of edges of \(S\), and denote their chromatic polynomial (zero if a loop occurs) by \(P_{(V/T,S)}(z)\). Then
\[
\boxed{N_A(w)=q^m\sum_{T\subseteq E\setminus S}(q-1)^{|T|}P_{(V/T,S)}(q^2).}
\]
For a target with nonzero semisimple vertex component, the fiber is zero. The \(w=0\) specialization is the previously known Tutte/Potts-type commuting-pair formula, and is *not* claimed as an independently new consequence.

**Sharp obstruction and complexity consequence.** Over \(\mathbb F_2\), orient the complete graph on five vertices according to a total order and form its radical-square-zero algebra. Exactly **one** element of the ten-dimensional arrow radical is not a single commutator: the sum of all ten arrows. That element is the sum of exactly two commutators. More generally, for arbitrary finite simple graphs \(G\) given as acyclic orientations and the radical element supported nontrivially on every arrow, deciding whether it is a single commutator over \(\mathbb F_2\) is equivalent to 4-colorability and hence NP-complete.

## Assumptions and scope

All algebras are finite-dimensional, associative and unital, and all elements and commutators are in the full algebra \(A\). The field \(k\) may have arbitrary positive characteristic. No acyclicity assumption is needed because the relation \(J^2=0\) kills all paths of length at least two; loops are excluded to ensure every arrow belongs to the commutator span. The vertices and arrows are separately labeled, and the underlying graph retains parallel edges for the fiber sum. The chromatic number ignores their multiplicity, as usual. The logarithm base \(q^2>1\) is the real logarithm; its ceiling is an integer.

A target outside \(J\) cannot be an additive sum of commutators, so \(\ell_A\) is only defined above on \(J=[A,A]_{\mathrm{span}}\). The complexity statement treats the quiver, presented by its arrow list, and the target radical coefficients as input; it does not claim hardness for any fixed algebra.

## Proof

Let \(e_v\) be the primitive vertex idempotents and \(a_e\) the arrow basis. For each arrow \(e:s\to t\), the only nonzero idempotent-arrow products are \(e_s a_e=a_e=a_e e_t\); all products of arrows vanish. Write
\[
x=\sum_{v}\alpha_v e_v+\sum_e u_e a_e,\qquad
y=\sum_{v}\beta_v e_v+\sum_e v_e a_e.
\]
The commutator coordinates are exactly
\[
[x,y]_e=(\alpha_s-\alpha_t)v_e-(\beta_s-\beta_t)u_e.\tag{1}
\]
There are no vertex components. Conversely, every arrow \(a_e=[e_s,a_e]\) (as \(s\ne t\)), so the additive span of all commutators is \(J\).

**One commutator and its fibers.** Assign to each vertex the ordered pair \(c(v)=(\alpha_v,\beta_v)\in k^2\). Equation (1) is the zero functional in \((u_e,v_e)\) precisely when its endpoint colors agree. If the colors differ, the coordinate map \(k^2\to k\) is a nonzero linear functional and each prescribed output has exactly \(q\) preimages. When the colors agree, there are \(q^2\) preimages for zero output and none for nonzero output. As arrow variables are independent across edges, multiplying these counts produces the first fiber formula. Since the summands are nonnegative integers, a fiber is nonempty exactly when its support graph has a proper coloring using the \(q^2\) elements of \(k^2\). This proves the one-commutator criterion and orientation independence.

To obtain the contracted-graph expansion, note that for \(e\notin S\), the factor for its arrow variables is \(q\bigl(1+(q-1)\mathbf1_{c(s(e))=c(t(e))}\bigr)\). Expanding the product over \(E\setminus S\) selects subsets \(T\) of edges forced monochromatic. Identifying the endpoints of every edge of \(T\) produces the contracted vertex set; edges of \(S\) are still required bichromatic. Hence their number of valid colorings is \(P_{(V/T,S)}(q^2)\), including the convention that loops contribute zero. Factoring out \(q^m\) gives the second fiber formula. This expansion remains valid for multiple or opposing arrows.

**Sums of commutators.** For \(r\) ordered commutator pairs, concatenate the \(r\) two-component vertex labels into a label \(C(v)\in k^{2r}\). If an edge has identical endpoint labels, equation (1) gives zero on that edge for every summand. Hence a representation of \(w\) as \(r\) commutators forces \(C\) to properly color \(G[S(w)]\) with at most \(q^{2r}\) colors. Conversely, if \(G[S(w)]\) has such a coloring, identify its colors injectively with \(k^{2r}\) and split each vertex label into \(r\) ordered pairs. For each supported arrow choose one index \(i\) at which the two endpoint pairs differ. Its equation (1) is a surjective linear map of the two arrow variables in summand \(i\), so set them to realize \(\gamma_e\); set the remaining arrow variables for that edge to zero. Do this independently on every edge. The resulting \(r\) commutators sum to \(w\). The minimal \(r\) is exactly the stated logarithmic ceiling. Maximizing over support subgraphs gives the full-graph chromatic number because the all-nonzero arrow target has support \(E\), proving the width formula. This also handles \(m=0\), where \(\chi(G)=1\) and the commutator width is zero.

**Five vertices and computational complexity.** A graph on five vertices with all ten edges needs five colors. For any proper subgraph of the complete graph on five vertices, two nonadjacent vertices can share a color and the remaining three vertices receive their own colors, giving a four-coloring. Therefore in characteristic two the all-arrow target is the unique nonzero single-commutator obstruction; its length is two because \(5\le 2^4\). The polynomial-time map taking a simple graph, orienting each edge from smaller to larger vertex label, and setting every arrow coefficient to one preserves 4-colorability exactly by the one-commutator criterion. Verifying a proposed pair is polynomial-time, so this target-membership decision problem is in NP; NP-hardness follows from the classical NP-completeness of 4-colorability.

## Verification

Run `python3 verify.py` from the directory holding that standalone file. It reconstructs the full multiplication/commutator output without relying on the theorem's counting formula, enumerating all ordered pairs for representative loopless quivers, including a parallel-arrow example, over \(\mathbb F_2\) and \(\mathbb F_3\). It compares every target fiber with the independent contraction/chromatic-polynomial expression. It additionally tests a complete-graph obstruction and constructs an explicit two-commutator representation of the binary all-arrow target for five vertices. The expected final output line is `VERIFY_OK`.

The universal finite-field assertion is proved symbolically from (1), not inferred from these finite checks. In particular the verifier does not enumerate fields of nonprime order; the proof requires only that every nonzero \(k^2\to k\) functional have exactly \(q\) preimages.

## Relationship to prior work

Green and Schroll (arXiv:2302.08169v1, first public 16 February 2023, primary MSC 16P10) study a quotient called the *commuting algebra*, formed by identifying parallel paths. Their full text (Sections 1–6) concerns structural and Morita-equivalence properties of that quotient; the term "commuting" is unrelated to prescribed additive commutator values or their lengths in the radical-square-zero quotient studied here.

Shumyatsky and Vannacci (arXiv:2307.12633v1, 24 July 2023) establish structural constraints from the **zero** commutator probability in finite rings. Their inspected full text has no nonzero-fiber or graph-chromatic length theorem.

Earlier calculations for generalized Kronecker path algebras (two vertices with parallel arrows) already give every nonzero radical commutator an equal fiber size, and an earlier general radical-square-zero quiver result gives the commuting-pair **zero fiber** as a Potts/Tutte partition function. These results are prior coverage of the corresponding special cases; neither supplies the support-sensitive nonzero fibers, the exact chromatic-number law for additive commutator length, or the graph-coloring obstruction for arbitrary loopless quivers. The zero-fiber specialization above is provided solely to demonstrate consistency and is excluded from the novelty claim.

Targeted searches for “commutator width radical square zero quiver chromatic number”, “nonzero commutator fibers quiver algebra graph coloring”, “Tutte polynomial commutator word map”, and related aliases did not locate a stronger covering theorem. This is a best-knowledge originality assessment, not a claim of exhaustive publication priority.

## Limitations

The chromatic formula relies on the radical-square-zero relation, independent arrow coordinates, and absence of loops. It does not extend automatically to nonzero products of two arrows, loops, arbitrary coefficient rings, or arbitrary finite-dimensional algebras. The complexity consequence concerns variable input quivers, not fixed-algebra calculations. The five-vertex statement is special to the binary field and to the stated complete-graph quiver. No claim is made that the previously known zero-fiber or two-vertex results are new. An unlocated general word-map or quiver-commutator theorem could subsume part of the result; independent scholarly validation remains outstanding.

## References

1. E. L. Green and S. Schroll, “The Commuting Algebra,” arXiv:2302.08169v1, submitted 16 February 2023, https://arxiv.org/abs/2302.08169 .
2. P. Shumyatsky and M. Vannacci, “Commuting and product-zero probability in finite rings,” arXiv:2307.12633v1, submitted 24 July 2023, https://arxiv.org/abs/2307.12633 .
3. “Commutator fibers and commuting probabilities of finite Kronecker path algebras,” published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d .
4. M. R. Garey and D. S. Johnson, *Computers and Intractability*, Freeman, 1979 (classical fixed-color graph decision complexity).
