# The first counting-logic collision for two-letter transition systems

## Finding
For a finite nonempty set \(X\), consider an ordered pair of total transformations \(f,g:X\to X\), represented by two **binary relation symbols** \(F(x,y)\) and \(G(x,y)\), interpreted as \(f(x)=y\) and \(g(x)=y\), respectively. No initial state, accepting states, colors, or function symbols are present.

**Sharp threshold.** Any two such structures on at most four points are equivalent in two-variable first-order logic with counting quantifiers, \(C^2\), if and only if they are isomorphic as ordered pairs of transformations. The isomorphism counts and the \(C^2\)-equivalence-class counts, by domain size \(1,2,3,4\), are each \(1,10,129,2836\). At size five, nonisomorphic \(C^2\)-equivalent structures exist: on \(\mathbb Z/5\mathbb Z\), let \(f(x)=x+1\); take \(g(x)=x+2\) in the first structure and \(g(x)=x+3\) in the second.

Hence, **five is the least finite cardinality** admitting a nonisomorphic \(C^2\)-equivalent pair of two-letter transition systems in this binary relational language. The known enumeration of transformation-pair isomorphism types is not claimed as new; the claimed finding is the exact logical-coincidence threshold for **all** ordered pairs of total maps, including noninvertible and noncommuting pairs.

## Assumptions and scope
Two symbols \(F,G\) are distinct and named; renaming the two symbols is **not** an isomorphism. Each is the graph of one total unary map. Structures have nonempty finite domains. Counting quantifiers range over points. The relational vocabulary is essential: function terms such as \(f(g(x))\) are not permitted as terms in \(C^2\) here. In particular the claim does not concern two unary function **symbols** or pointed/accepting automata.

## Proof
### Reduction to finite exact search
For \(n\in\{1,2,3,4\}\), every structure is specified by \(2n\) integers in \(\{0,\ldots,n-1\}\), so there are exactly \(n^{2n}\) labeled pairs \((f,g)\). The algorithm in `verify.py` runs through all these pairs and generates their full simultaneous-conjugacy orbits under all permutations \(p\in S_n\), where \((f,g)\) is sent to \((pfp^{-1},pgp^{-1})\). It retains exactly one representative from each orbit and asserts that the union of these orbits has cardinality \(n^{2n}\). Thus no isomorphism type is omitted or repeated.

As a separate check of the number of representatives, Burnside's lemma yields
\[
N_n=\frac{1}{n!}\sum_{p\in S_n}\left(\prod_{C\in\operatorname{Cyc}(p)}\bigl|\operatorname{Fix}(p^{|C|})\bigr|\right)^2.
\]
Indeed, specifying one transformation commuting with \(p\) means choosing an image for each cycle representative fixed by the corresponding power of \(p\), and then equivariantly extending around that cycle. The two transformations can be chosen independently. The separate Burnside implementation and exhaustive orbit generation both give \(N_n=(1,10,129,2836)\) for \(n=1,2,3,4\).

### Exact \(C^2\) test
For every ordered pair of points \(x,y\), the complete atomic two-variable type is the five-bit record
\[
\bigl(x=y,F(x,y),F(y,x),G(x,y),G(y,x)\bigr).
\]
Starting with uniform vertex colors, one round of counting refinement replaces the color of \(x\) with its old color and the **multiset**, as \(y\) ranges over the domain, of pairs consisting of this atomic two-type and the old color of \(y\). The next colors are assigned using **one shared palette for all structures of fixed order**. By the standard counting-logic / equitable-coloring equivalence for finite binary relational structures, a difference in these histograms implies a distinguishing \(C^2\) sentence; equality of stable histograms is equivalent to \(C^2\)-equivalence.

The verifier calculates these joint histograms through \(n+4\) rounds. At every order \(n\le4\), **all \(N_n\) isomorphism representatives have pairwise distinct histograms**, so every nonisomorphic pair is \(C^2\)-distinguishable. This is a finite exhaustive proof: it neither samples the input space nor infers an infinite theorem from four small cases. Nothing depends on a claim that \(n+4\) is a universal stabilization bound; it suffices that the tested finite histograms are already distinct.

### Five-point collision
Write \(A=(x\mapsto x+1,x\mapsto x+2)\) and \(B=(x\mapsto x+1,x\mapsto x+3)\) on \(\mathbb Z/5\mathbb Z\). In both structures, each point sees exactly one incoming and outgoing edge of each relation, and these four neighbors are distinct. The complete atomic two-type count is identical at every point in both structures. Therefore the uniform color is counting-stable across the joint disjoint union and \(A\equiv_{C^2}B\).

An isomorphism must commute with the common first map \(x\mapsto x+1\), hence must be a translation. But every translation also commutes with \(x\mapsto x+2\), so cannot conjugate it to \(x\mapsto x+3\). Consequently \(A\not\cong B\), completing the sharpness proof.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. No external data or nonstandard packages are needed. The algorithm exhausts all \(n^{2n}\) labeled transition-pair tables for each \(1\le n\le4\), independently verifies isomorphism counts using Burnside's formula, evaluates the complete atomic two-variable types under joint refinement, and checks the five-state witness via all \(5!\) bijections. Its deterministic output is supplied in `expected_output.txt`; the final line is `VERIFY_OK first_C2_collision=5 types_at_4=2836`.

## Relationship to prior work
Harrison's 1965 census already counts unlabeled finite automata, including ordered pairs of transition functions. Thus the sequence \(1,10,129,2836\) is prior enumeration and is **not** the novelty claim. Kiefer, Schweitzer, and Selman (2015) prove general logical characterizations of structures identified by \(C^2\) among *all* finite structures; the present computation instead establishes a sharp first collision **relative to the two-total-map class**. The general principle connecting joint counting colors and \(C^2\) is used, not newly established. A restriction to commuting permutations does not prove the claimed four-point lower bound for the much larger class of arbitrary pairs of maps.

## Limitations
The search verifies all structures only through size four and exhibits a single collision at size five; it does **not** give a complete five-point census, describe collisions at larger orders, or assert absolute \(C^2\)-identification against unrelated relational structures. Claims of historical novelty remain provisional because unindexed calculations or alternative terminology may cover this cutoff. The proof and code have not been independently audited.

## References
1. M. A. Harrison, *A Census of Finite Automata*, Canadian Journal of Mathematics 17 (1965), 100–113, DOI:10.4153/CJM-1965-010-9. The publisher's accessible HTML extract concerns enumeration; its full paper was not materially inspected here.
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1 (first publicly available 2015-03-30), DOI:10.1007/978-3-662-48057-1_25.
3. OEIS A054050, enumeration of isomorphism classes of two-letter finite automata.
