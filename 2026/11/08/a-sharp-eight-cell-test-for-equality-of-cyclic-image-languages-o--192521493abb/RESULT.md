# A sharp eight-cell test for equality of cyclic image languages of elementary cellular automata

## Finding

For each Wolfram elementary binary cellular automaton rule \(r\in\{0,\ldots,255\}\), let \(F_{r,n}:\{0,1\}^n\to\{0,1\}^n\) be one simultaneous update on an **indexed cyclic ring** of length \(n\ge1\). Define its cyclic image language
\[
L_r=\bigcup_{n\ge1} F_{r,n}(\{0,1\}^n).
\]
The words in different lengths are kept distinct; rotations and bit complementation of outputs are **not** identified.

**Theorem.** The \(256\) languages \(L_r\) fall into exactly \(100\) equality classes. Moreover, for any rules \(r,s\),
\[
L_r=L_s\quad\Longleftrightarrow\quad
L_r\cap\{0,1\}^{\le8}=L_s\cap\{0,1\}^{\le8}.
\]
The cutoff \(8\) is optimal: Rules \(57\) and \(99\) have identical cyclic image words at every length from \(1\) through \(7\), but \(00010011\) is an image of Rule \(57\) and is not an image of Rule \(99\) on an eight-cell ring. Rule \(57\) maps the cyclic input \(11100101\) to that output.

The class-size distribution is: \(8\) singleton classes, \(75\) two-rule classes, \(10\) four-rule classes, \(3\) six-rule classes and \(4\) ten-rule classes. Every class is listed exactly, with its smallest-rule representative first, in `classes.json`.

## Assumptions and scope

Use the standard Wolfram numbering: for a triple \((a,b,c)\in\{0,1\}^3\), the output bit is bit number \(4a+2b+c\) (zero-based from the least significant bit) in the integer \(r\). Hence
\[
F_{r,n}(x)_i=\operatorname{bit}_{4x_{i-1}+2x_i+x_{i+1}}(r),\qquad i\in\mathbb Z/n\mathbb Z.
\]
Repeated neighbor indices for \(n=1\) and \(n=2\) are intentional. Output words have specified positions, not necklace/bracelet equivalence. Equality of languages means equality for **every positive** ring length, not equal cardinalities or the same asymptotic entropy.

## Proof

**1. Cyclic image acceptance by a four-vertex graph.** For each rule, form a directed multigraph with vertices the two-bit states \(ab\in\{00,01,10,11\}\). For every triple \(abc\), include an edge \(ab\to bc\) labeled by the rule output on \(abc\). Cyclic input configurations of length \(n\) correspond exactly to closed walks of length \(n\), and their outputs are the label words of those walks. This equivalence also holds when \(n=1\) or \(n=2\).

Let \(M_0,M_1\) be the Boolean adjacency matrices of those two labeled graphs. Define Boolean matrix multiplication by OR/AND arithmetic. A word \(y=y_0\cdots y_{n-1}\) belongs to \(L_r\) if and only if
\[
\bigvee_{j=0}^3(M_{y_0}M_{y_1}\cdots M_{y_{n-1}})_{jj}=1.
\]
This is a finite-state assertion, not an approximation: products of Boolean matrices track all possible labeled paths, and a nonzero diagonal entry is exactly a closed path.

**2. Deterministic finite recognition of all lengths.** Start at the four-by-four identity relation \(I\), read an output bit \(b\) by the deterministic update \(R\mapsto R M_b\), and accept if the resulting relation has at least one diagonal entry. There are at most \(2^{16}\) possible relations, so this is a deterministic automaton for the **entire infinite** cyclic image language, including all positive lengths. For two rules, the product of their relation automata accepts a distinguishing word exactly when their two acceptance flags disagree. Exhaustive breadth-first reachability in this finite product proves whether their image languages coincide at every length.

**3. Exact short-word partition.** Independently apply each of the \(256\) local rules to all \(2^n\) possible cyclic inputs for each \(1\le n\le8\), retaining actual image-word sets, not only cardinalities. The numbers of distinct short-image signatures through lengths \(1,2,3,4,5,6,7,8\), respectively, are
\[
3,\ 8,\ 40,\ 72,\ 75,\ 92,\ 99,\ 100.
\]
Thus the eight-cell signatures form exactly \(100\) nonempty groups. Any rules in different groups already have an explicit distinguishing word of length at most \(8\).

**4. No hidden longer distinctions within a group.** For each of those short-signature groups, choose its smallest numbered rule. For every other member, build the two complete finite relation automata from Step 2 and perform breadth-first search in their synchronized product from \((I,I)\). At every reachable pair, the acceptance flags agree. Exactly \(156=256-100\) representative-to-member comparisons are performed. The largest visited product graph contains \(2375\) state pairs, for Rules \(22\) and \(104\). Because the entire reachable product is exhausted, induction on output-word length proves that all members of a group accept exactly the same words at **every** length. Combining this with Step 3 proves the \(100\)-class classification and the uniform cutoff \(8\).

**5. Sharpness.** Direct enumeration gives identical image-word sets for Rules \(57\) and \(99\) at all lengths \(1\) through \(7\). At length \(8\), output `00010011` belongs to the image of Rule \(57\), witnessed by input `11100101`, but no input under Rule \(99\) yields it (confirmed both by all \(256\) inputs and by the Boolean relation criterion). Hence cutoff \(7\) fails.

All finite searches in Steps 3–5 are exhaustive and are reproduced by the complete standard-library `verify.py`; the finite-automaton lemma in Step 2 is the reason those finite calculations certify the infinite equality statement. A short finite prefix comparison alone would not suffice.

## Verification

Run `python3 verify.py` from a directory containing the files `verify.py` and `classes.json`. The program independently enumerates all cyclic inputs at each length through \(8\), constructs all \(256\) Boolean relation machines, checks their membership predictions against the direct enumeration for every candidate word through length \(8\), and exhausts all \(156\) representative-to-member product automata. It asserts the sharp witness, group sizes, number of groups and product-search maximum before printing `VERIFY_OK`. The class table is a standalone exact supplement, rather than a truncated illustrative list.

The canonical compact JSON class-list encoding has SHA-256 `8046dbeaba56d5cdec15119e6407b9c712af515a19d6c70adc31613f9a841cee`. This hash is an integrity reference, not a substitute for executing the verifier. All claims about infinitely many lengths are established by the finite-state product argument, not by an extrapolation from length \(8\).

## Relationship to prior work

Wolfram's 1983 foundational treatment introduced the elementary binary rules and their global dynamical properties. Martínez's 2013 classification survey documents the familiar \(88\) classes under spatial reflection and state-complement conjugacy; those are **not** equivalence classes of identical indexed cyclic image-word languages, since output relabeling changes the language being compared. Castillo-Ramírez and Gadouleau study the semigroup ranks of all cellular automata on finite cyclic groups, a different enumerative invariant. Salo investigates split epicness and regularity of elementary cellular automata; his section on image subshifts lists forbidden words for selected rules, but does not establish the \(100\)-class full cyclic image-language classification or the sharp cutoff \(8\). The Elementary CA Zoo's Garden-of-Eden census counts unreachable configurations at selected ring lengths and identifies rules modulo symmetries; finite counts do not establish equality of the actual output-word sets at all lengths.

The classification here is stronger than equality of one-step image cardinalities at every length and different from either eventual dynamical equivalence or equivalence up to output complementation. Some groups include rules whose equality is explained by input relabeling; the exhaustive result accounts for all such equalities and also all inequivalences.

## Limitations

The theorem concerns binary radius-one rules only and **one update** with cyclic periodic boundary conditions. It does not classify images of iterations, infinite nonperiodic outputs, higher-radius rules, rotations/bracelets, semigroup ranks, or inverse multiplicities. The finite-state proof and reproducible computation have not undergone independent mathematical validation. A literature search cannot establish absolute priority; unindexed earlier equivalence tables or full image-language enumerations remain a residual risk.

## References

1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55** (1983), 601–644, published 1 July 1983. DOI: https://doi.org/10.1103/RevModPhys.55.601. Open manuscript: https://new.math.uiuc.edu/im2008/dakkak/papers/files/wolfram.smca.pdf.
2. G. J. Martínez, “A Note on Elementary Cellular Automata Classification,” 2013, arXiv:1306.5577, first posted 24 June 2013. https://arxiv.org/abs/1306.5577.
3. A. Castillo-Ramírez and M. Gadouleau, “Ranks of finite semigroups of one-dimensional cellular automata,” arXiv:1510.00197, first posted 1 October 2015. https://arxiv.org/abs/1510.00197.
4. V. Salo, “Von Neumann regularity, split epicness and elementary cellular automata,” arXiv:1804.03913, first posted 11 April 2018, notably §6.3. https://arxiv.org/abs/1804.03913.
5. “Gardens of Eden — Elementary CA Zoo,” undated online computational census, inspected for finite-length output counts and de Bruijn approach. https://cellular.solves.ca/gardens-of-eden.
