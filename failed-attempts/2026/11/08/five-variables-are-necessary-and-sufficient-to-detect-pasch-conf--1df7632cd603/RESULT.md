# Five variables are necessary and sufficient to detect Pasch configurations in finite Steiner triple systems

## Finding

Consider nontrivial finite Steiner triple systems as relational structures \((V,R)\), where \(R(a,b,c)\) holds if and only if \(a,b,c\) are three **distinct** points belonging to one block. Equality is available; there are no named points, functions, counting quantifiers, or additional relations. Let \(\mathrm{FO}^{k}\) denote ordinary first-order logic using at most \(k\) variable names, reused arbitrarily often, with no bound on quantifier rank.

**Theorem.** Every two finite Steiner triple systems with at least seven points satisfy exactly the same \(\mathrm{FO}^{4}\) sentences. The property of containing a Pasch configuration is definable in \(\mathrm{FO}^{5}\), but not in \(\mathrm{FO}^{4}\), even when restricted to finite Steiner triple systems of order at least seven. Thus five is its exact first-order variable width. In particular, the Fano system of order seven and the affine-plane system of order nine are \(\mathrm{FO}^{4}\)-equivalent but are distinguished by an \(\mathrm{FO}^{5}\) sentence.

More broadly, every \(\mathrm{FO}^{4}\) sentence is either true in every nontrivial finite Steiner triple system or false in every such system. This is a complete classification at variable width four, independent of system order and block arrangement.

## Assumptions and scope

A Steiner triple system \((V,\mathcal B)\) has a set \(V\) and a family \(\mathcal B\) of three-element blocks such that every unordered pair of distinct points lies in exactly one block. Every nontrivial finite system has \(|V|\ge7\). Throughout, \(R(a,b,c)\) abbreviates \(\{a,b,c\}\in\mathcal B\), and is **false** when any two arguments coincide. The theorem is about this one-sorted, pure ternary block language; it must not be transferred without proof to the functional Steiner-quasigroup language.

A Pasch configuration consists of six pairwise distinct points \(a,b,c,d,e,f\) with the four blocks
\[
\{a,b,c\},\qquad \{a,d,e\},\qquad \{f,b,d\},\qquad \{f,c,e\}.
\]

## Proof

**1. Uniform extension of three-point atomic types.** For distinct \(a,b\), denote by \(a\circ b\) the unique third point in the block on \(a,b\). If at most three points are stationary, all possible atomic extensions by a fourth point depend only on the equality pattern and on whether three distinct stationary points are a block.

For three distinct stationary points \(a,b,c\) that form a block, the unique completion of every stationary pair is the third stationary point. A new point is either one of \(a,b,c\) or belongs to a generic category of size \(|V|-3\), on which none of \(R(a,b,x),R(a,c,x),R(b,c,x)\) holds.

If the three stationary points do **not** form a block, the completions \(a\circ b\), \(a\circ c\), and \(b\circ c\) are three pairwise distinct points outside \(\{a,b,c\}\). For example, if \(a\circ b=a\circ c=x\), then the pair \(\{a,x\}\) would have two different completions \(b,c\), contrary to the Steiner property. Hence the extension categories are the three stationary points, the three separate completion points, and a generic category of size \(|V|-6\). Since \(|V|\ge7\), every category is nonempty. With two or fewer distinct stationary points the conclusion follows immediately from unique pair completion and the presence of further points. All ordered placements and repetitions of stationary pebbles are covered.

**2. Permanent four-pebble equivalence.** Place four matched pebbles on any two systems with at least seven points. After any pebble is removed, the remaining three pebbles determine only an equality pattern and, when distinct, one Boolean block value. If these atomic data match in the two systems, Step 1 guarantees a response realizing the same complete atomic four-tuple type, including equality and all instances of \(R\) involving the moved pebble. Starting from empty positions, Duplicator can maintain a partial isomorphism indefinitely. The standard counting-free finite-variable pebble-game characterization therefore proves
\[
\mathcal S\equiv_{\mathrm{FO}^{4}}\mathcal T
\]
for every pair of nontrivial finite Steiner triple systems \(\mathcal S,\mathcal T\). The argument does not restrict quantifier depth.

**3. An actual five-variable Pasch sentence.** Let \(D(x,y,z,u,v)\) be the conjunction asserting that the five displayed variables are pairwise unequal. The following sentence uses **only** variable names \(x,y,z,u,v\); the inner \(\exists x\) deliberately shadows the outer \(x\):
\[
\exists x\,\exists y\,\exists z\,\exists u\,\exists v\;\bigl[
D(x,y,z,u,v)\land R(x,y,z)\land R(x,u,v)
\land \exists x\,(R(x,y,u)\land R(x,z,v))\bigr].
\]
The fourth block is \(R(f,c,e)\) and the third is \(R(f,b,d)\) after renaming the inner \(x\) to \(f\). Distinctness of \(f\) from \(b,c,d,e\) follows because \(R\) is irreflexive, and distinctness from the former outer \(a\) follows because otherwise \(\{a,b,c\}\) and \(\{a,b,d\}\) would be distinct blocks on the same pair. Thus the sentence is true exactly when a Pasch configuration exists.

**4. Sharpness from two explicit systems.** The Fano system has point set \(\mathbb F_2^3\setminus\{0\}\) and blocks on three distinct vectors summing to zero. Choose linearly independent vectors \(a,b,d\), and set \(c=a+b\), \(e=a+d\), \(f=b+d\). These are six distinct nonzero vectors satisfying all four required blocks, so the Pasch sentence is true.

The affine system of order nine has point set \(\mathbb F_3^2\) and blocks on three distinct vectors summing to zero. If a Pasch existed, its four block equations would give \(c=-a-b\), \(e=-a-d\), and \(f=-b-d\). The remaining equation \(f+c+e=0\) would imply \(-2(a+b+d)=0\), hence \(a+b+d=0\) in characteristic three, and therefore \(f=a\), contrary to the six-point distinctness. So the affine system is Pasch-free. Step 2 makes these two systems indistinguishable by \(\mathrm{FO}^{4}\); Step 3 distinguishes them at width five. No smaller width can define the Pasch property.

## Verification

The standalone finite checks in `verify.py` construct the Fano system, the affine system of order nine, and systems of orders fifteen and twenty-seven, and verify the unique-completion condition for every unordered pair. For every ordered stationary triple, including tuples with repeated points, the program enumerates all fourth-point atomic extension types; all four systems have the same six stationary atomic classes and the same twenty-five distinct extension categories in total. It also exhaustively finds a Pasch in the Fano system and excludes Pasch configurations in the affine system of order nine. Run `python3 verify.py` and compare with `verification_output.txt`. These examples corroborate but do **not** prove the unrestricted equivalence; that follows from Step 1 and the permanent strategy in Step 2. The proof of Pasch-freeness in the order-nine example is algebraic and does not rely on a bounded search.

## Relationship to prior work

The ordinary counting-free pebble-game framework is standard; Grohe and Otto (2012) discuss finite-variable equivalence and its algebraic representations. Their results do not assert the specific extension uniformity for Steiner triple systems proved in Step 1. Barbina and Casanovas (2018/2020) study the model completion and model-theoretic properties of Steiner quasigroups, primarily in their **functional** language; their examined introductory sections, relevant definitions, and theorem statements do not give this finite relational variable-width threshold. Ling, Colbourn, Grannell and Griggs (2000) and Grannell, Griggs and Whitehead (2000) establish the significance and broad existence of anti-Pasch systems, not a finite-variable logical width theorem. Heinlein and Östergård (2022) analyze generation and counting of Pasch configurations; their three-point generating-set complexity is distinct from the number of reusable first-order variables in the pure relational language.

The novelty claim is limited to the **combined complete \(\mathrm{FO}^{4}\) collapse and exact five-variable definability threshold**. No claim is made that Pasch configurations, their algebraic examples, general pebble games, or anti-Pasch constructions are new.

## Limitations

The result does not classify five-variable theories of all Steiner triple systems; it identifies one nonconstant five-variable property. It does not apply to the trivial systems of order one or three in the universal-collapse statement. The relational and functional representations are not interchangeable for bounded-variable counts without additional analysis. The precise historical priority of this variable-width theorem remains subject to independent literature review. The provided computations are checks of finite instances, not automated certificates of a statement over all finite orders.

## References

1. A. C. H. Ling, C. J. Colbourn, M. J. Grannell, T. S. Griggs, *Construction Techniques for Anti-Pasch Steiner Triple Systems*, Journal of the London Mathematical Society 61 (2000), 641–657. DOI: 10.1112/S0024610700008838. First publicly published 2000-06-01.
2. M. J. Grannell, T. S. Griggs, C. A. Whitehead, *The Resolution of the Anti-Pasch Conjecture*, Journal of Combinatorial Designs 8 (2000), 300–309. DOI: 10.1002/1520-6610(2000)8:4<300::AID-JCD7>3.0.CO;2-R.
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, Computer Science Logic (2012), 289–304. DOI: 10.4230/LIPIcs.CSL.2012.289.
4. S. Barbina and E. Casanovas, *Model Theory of Steiner Triple Systems*, arXiv:1805.06767 (first posted 2018-05-17); Journal of Mathematical Logic 20 (2020), 2050010.
5. D. Heinlein and P. R. J. Östergård, *Algorithms and Complexity for Counting Configurations in Steiner Triple Systems*, Journal of Combinatorial Designs 30 (2022), 527–546. DOI: 10.1002/jcd.21839.
