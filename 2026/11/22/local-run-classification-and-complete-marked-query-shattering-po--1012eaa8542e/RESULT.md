# Local-run classification and complete marked-query shattering polynomial for ternary cycle colourings

## Finding
Let \(C_n\) be a simple cycle with \(n\ge3\) labelled vertices, let \(\mathcal F_n\) be its proper colourings by three named colours \(\{0,1,2\}\), and make every colouring \(f\) a Boolean concept with \(h_f(i,a)=\mathbf1_{\{f(i)=a\}}\). A query support is any subset of the \(3n\) distinct pairs \((i,a)\). It is *shattered* when all binary answer assignments are realized by members of \(\mathcal F_n\).

**Complete classification.** A support is shattered if and only if the following conditions hold:

1. At most one colour query occurs at any vertex.
2. The selected vertices form a proper subset of the cycle; every maximal cyclic run of selected vertices has length at most three.
3. In a selected run of length two, the two target colours differ. In a selected run of length three, the target colours read \(a,b,a\) with \(a\ne b\). A singleton selected run may target any of the three colours.

Here a selected run is a maximal consecutive component of selected vertices in the cyclic order, separated from other runs by one or more unselected vertices. The empty support is shattered. Thus singleton, doubleton and triple-run weights are, respectively, \(3z\), \(6z^2\) and \(6z^3\).

Define \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\), counting *distinct marked vertex-colour query sets* rather than unmarked vertex supports. For every \(n\ge3\),

\[
\boxed{\displaystyle
\Phi_n(z)=1+n[t^n]\log\!\left(
\frac{1-t}{1-t-3zt^2-6z^2t^3-6z^3t^4}
\right).}
\]

Equivalently, with \(r=a+b+c\), the coefficient of \(z^k\), for \(k\ge1\), is

\[
\boxed{\displaystyle
[z^k]\Phi_n(z)=\sum_{\substack{a,b,c\ge0,\;a+2b+3c=k\\ r=a+b+c\ge1,\;r\le n-k}}
\frac{n(r-1)!}{a!b!c!}\binom{n-k-1}{r-1}3^a6^{b+c}.}
\]

In particular, the complete local restriction refines the previously established dimension \(\operatorname{VCdim}=\lfloor3n/4\rfloor\). It yields \([z]\Phi_n=3n\), \([z^2]\Phi_n=9\binom n2-3n\), and, for \(n\ge4\),

\[
[z^3]\Phi_n(z)=\frac{3n}{2}(3n^2-15n+16),
\]

while \([z^3]\Phi_3=0\). For example,

\[
\Phi_5(z)=1+15z+75z^2+120z^3,\qquad
\Phi_8(z)=1+24z+228z^2+1056z^3+2322z^4+1872z^5+144z^6.
\]

**Nonpurity corollary.** For every even cycle \(C_{2m}\), \(m\ge3\), the shattered-support complex has inclusion-maximal faces of size \(m\) as well as larger faces of size \(\lfloor3m/2\rfloor\). Among the two alternating parity classes of \(m\) vertices, exactly

\[
\boxed{2\bigl(2^m+2(-1)^m\bigr)}
\]

marked supports are inclusion-maximal: choose target colours on each alternating parity class to be a proper three-colouring of the auxiliary \(m\)-cycle. Thus the shattering complex is nonpure for every even order at least six.

## Assumptions and scope
The cycle is finite, simple and has length at least three. Colours are named and are not identified under palette permutations. Each query asks equality of one specified vertex colour to one specified palette symbol; shattering is ordinary fixed-support Boolean VC shattering, not graph-structure learning or online Littlestone shattering. The generating function is a formal power series in \(t\), polynomial in \(z\) coefficientwise; \([t^n]\) and \([z^k]\) extract coefficients. All quantifiers range over every integer \(n\ge3\), every possible query set and every binary trace. No claim is made for other graph families or palettes.

## Proof
**At most one marked query per vertex.** If two different colours are queried at one vertex, the binary answer assignment making both queries positive has no realizing colouring. Duplicates cannot occur in a query set. Consequently a shattered support marks at most one colour at each selected vertex.

**Extension lemma.** Every proper three-colouring of an induced subgraph on a *proper* subset of vertices of a cycle extends to a proper three-colouring of the cycle. Each component of the uncoloured vertices is a path between two precoloured vertices. With one uncoloured interior vertex, choose a colour different from both endpoints; with more, colour the first interior vertex differently from its predecessor and apply induction, finishing at a two-edge segment with at least one available third colour. If the precoloured set is empty, use any proper three-colouring of the cycle. Hence, for a proper selected-vertex subset, the feasibility of any query-answer pattern is equivalent to the existence of a proper three-colouring on each induced selected path that respects the prescribed positive and negative equality tests. Different selected runs can be treated independently.

**Local obstructions.** On a selected edge with targets \(a,b\), the all-positive answer requires \(a\ne b\). On three consecutive selected vertices with targets \(a,b,c\), the all-positive answer implies \(a\ne b\ne c\) in the adjacent-edge sense. The trace \((1,0,1)\) fixes the endpoints to \(a,c\) and forbids \(b\) at the middle. If \(a\ne c\), the only colour permitted at the middle is the remaining third colour, which the all-positive constraint forces to equal \(b\). This is impossible. Therefore \(a=c\) is necessary.

If four consecutive vertices are selected, the overlapping triple condition forces alternating targets \((a,b,a,b)\), with \(a\ne b\). The answer word \((1,0,0,1)\) fixes the endpoints to \(a,b\) and forces each inner vertex to the third colour, since each must avoid both its adjacent positive endpoint and its own target. The two middle vertices would then have equal colours despite being adjacent. Thus no run of four selected vertices is shattered. For the triangle \(C_3\), selecting all three vertices cannot shatter: there are only six proper three-colourings, fewer than the eight possible three-bit traces. For any larger cycle the four-run obstruction excludes the entire cycle. These establish all necessary conditions.

**Run sufficiency.** A singleton with target \(a\) realizes positive and negative responses using \(a\) and another colour. On an edge with distinct targets \((a,b)\), let \(c\) denote the third colour. The four answer patterns \((1,1),(1,0),(0,1),(0,0)\) are realized by \((a,b),(a,c),(c,b),(b,a)\), respectively. On a three-vertex path with targets \((a,b,a)\), write \(c\) for the third colour. The eight answer patterns \(111,110,101,100,011,010,001,000\) are realized by colour strings \(aba,abc,aca,acb,cba,cbc,bca,bac\), respectively. Every displayed string is proper and meets exactly its indicated target tests. Thus each permitted run realizes every binary answer assignment. The extension lemma joins any choices for separated runs into a proper colouring of the whole cycle, proving the sufficient direction.

**Enumeration.** Write \(A(t,z)=3zt+6z^2t^2+6z^3t^3\) for one marked selected run and \(B(t)=t/(1-t)\) for one positive-length unselected gap. For a nonempty support with \(r\) selected runs, choose an ordered list of \(r\) run-gap pairs and choose one of the \(n\) labelled starting positions. Each resulting labelled configuration has exactly \(r\) possible choices of which selected run was first, so its contribution is \(\frac nr[t^n](AB)^r\). Summing over \(r\ge1\) gives \(n[t^n]\sum_{r\ge1}(AB)^r/r\), the stated logarithm. The one empty support contributes \(1\).

Alternatively, if there are \(a\) singleton, \(b\) doubleton and \(c\) triple selected runs, there are \(r!/(a!b!c!)\) ordered run-type lists. There are \(\binom{n-k-1}{r-1}\) ways to distribute the \(n-k\) unselected positions as \(r\) nonempty gaps. The marked-run multiplicity is \(3^a6^{b+c}\), and dividing the \(n\) root choices by \(r\) gives the coefficient formula. Both formulas are exact for every finite \(n\ge3\).

The maximal selected density is three out of every four consecutive sites, yielding the already-known \(\lfloor3n/4\rfloor\) VC dimension; this is a corollary, not a novel dimension claim. Counting triples by their induced selected pattern (independent triple, edge plus singleton, or three consecutive sites) gives the displayed cubic coefficient.

**Nonpurity corollary proof.** On \(C_{2m}\), choose every other vertex and mark it by any proper three-colouring, in cyclic order, of the auxiliary \(C_m\). The chosen vertices are pairwise nonadjacent, so all \(m\) equality tests are shattered. Each omitted vertex lies between two selected vertices whose target colours are different, and inserting any equality test there would create a selected three-run violating the necessary alternating-target rule. Adding a second test at an already selected vertex also fails. Hence this is an inclusion-maximal support of size \(m\). Conversely, if two adjacent targets in the auxiliary cycle agree, the intervening omitted vertex can be queried using a different target, producing a permitted length-three selected run; therefore the alternating support was not maximal. The number of proper three-colourings of an \(m\)-cycle is \(2^m+2(-1)^m\), the trace of the \(3\times3\) transition matrix with zero diagonal and ones elsewhere. There are two choices of alternating parity class, giving the displayed exact count. Larger shattered supports exist by placing marked runs of up to three vertices separated by gaps, attaining the known rank \(\lfloor3(2m)/4\rfloor=\lfloor3m/2\rfloor>m\).

## Verification
The accompanying independent direct-trace checker `check_cycle_marks.py` enumerates all proper three-colourings for each \(3\le n\le8\). For every one-test-per-vertex marked query support it compares the *entire observed trace set* with the local-run theorem and independently matches each polynomial coefficient with the binomial expression. This checks \(4^n\) marked supports at each size, including the empty support and all excluded supports. It also tests the maximal polynomial degree through \(n=40\) and the alternating-parity nonpure-facet characterization through even order twelve. Running `python check_cycle_marks.py` produces the included `checks_output.txt`, ending with `ALL_MARKED_CYCLE_CHECKS_PASS`. These finite checks corroborate but do not substitute for the all-\(n\) proof.

## Relationship to prior work
The previously published *Exact VC and Littlestone ranks for proper three-colourings of finite cycles* establishes \(\operatorname{VCdim}=\lfloor3n/4\rfloor\) and online dimension \(n-1\) for this **same query family**. Its full proof identifies four-consecutive-vertex obstructions and a specific maximizing construction; its Limitations section explicitly does **not** classify all individual shattered supports. Thus the scalar dimension and local obstruction are credited, while the complete marked-run classification, its exact multiplicities, and the full polynomial are the new contribution assessed here. The previous path analogue likewise gives a four-run obstruction and a rank formula, but not the cyclic marked-support enumerator.

Blanca, Chen, Štefankovič and Vigoda (2017) study identifying an *unknown graph* from random proper colourings and do not determine which fixed equality queries on a known cycle are shattered. Guingona, Kolesnikov, Nierwinski and Soucy (2021) study zero sets of linear function systems, a different class with general dimension results, not these constrained colourings. Walker (2022) provides general static/adaptive Sauer–Shelah-style bounds, not coefficientwise cycle counts. The 2026 Fourier-spectrum studies of proper ternary cycle colourings analyze additive character cancellations, not the combinatorial indicator of shattered query subsets. No listed result implies the displayed polynomial or exactly classifies the allowed marked runs. The comparison concerns theorem implications, not superficial matching of titles.

## Limitations
The formula is for exactly three named colours, simple cycles, and binary vertex–colour equality tests. It does not determine the analogous polynomial for other palettes, arbitrary graphs, or adaptive mistake trees. The proof is self-contained; the finite checker stops at the sizes stated above. Public index searches and inspected primary results do not establish absolute historical priority; equivalent unindexed or inaccessible work remains possible. Independent mathematical validation has not been conducted.

## References
1. A. Blanca, Z. Chen, D. Štefankovič and E. Vigoda, *Structure Learning of H-colorings*, arXiv:1708.05118, first public version 17 August 2017, https://arxiv.org/abs/1708.05118.
2. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first public version 10 September 2021, https://arxiv.org/abs/2109.04805.
3. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first public version 23 March 2022, https://arxiv.org/abs/2203.12211.
4. *Exact VC and Littlestone ranks for proper three-colourings of finite cycles*, openly archived 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-vc-and-littlestone-ranks-for-proper-three-colourings-of-fi--22fcc09464b4.
5. *A sharp three-colour palette threshold for VC and online shattering of path colourings*, openly archived 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-three-colour-palette-threshold-for-vc-and-online-shatter--5ed55547f077.
