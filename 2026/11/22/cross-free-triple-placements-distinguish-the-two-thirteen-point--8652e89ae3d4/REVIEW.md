# Scientific review: cross-free placements of both thirteen-point Steiner designs

## Correctness — PASS

The two explicit block tables are valid Steiner triple systems: 26 distinct three-point blocks in each, exactly once covering all 78 point pairs. The classical classification of designs of order thirteen identifies these two block systems as representatives of the only isomorphism types. The upper bound of three for cross-free equal-size triples follows without computation: size four would leave one unused point, and the twenty blocks not through it would require distinct same-class pairs, although only eighteen exist. Explicit valid triples establish attainment in both types. The counting identity examines exactly 200200 unordered disjoint three-class candidates. A bit-mask Python enumerator and a separately coded two-bit-colour C++ enumerator both exhaust these candidates, verify forbidden triples, construct every permitted single-point exchange and calculate component data by graph traversal. Their outputs agree: 6214/6148 states, 25896/25032 edges and the claimed small-component decompositions. Each degree is divisible by three, as required by the independently proved all-or-none exchange lemma; reverse adjacency and all component sizes are verified. For a seven-vertex component, the six leaves span exactly two triangles, not a six-cycle. Scientific limit: computational proof only for these two 13-point designs, no assertion for arbitrary orders.

## Originality — PASS with residual priority risk

The 2015 paper by Gyárfás introduces the cross-free object and proves general extremal inequalities and constructions. Its direct results do not specify the 6214/6148 balanced partial-colouring counts or the exchange component profiles; the maximum size three is background rather than the new claim. Pavone's 2023 full-text sections identify the two systems and their Pasch switch and discuss weak proper 3-colourings: forbidding monochromatic full-system blocks is not equivalent to forbidding rainbow blocks of a partial three-colouring of nine points. Heinlein and Östergård (2022) count fixed-line configurations and do not derive these balanced cross-free exchange graphs. Published results on thirteen-point cap/line-avoiding complexes classify single independent point subsets, not three disjoint balanced families. Targeted indexed searches found no statement implying the exact enumerations and component decompositions; absence of a match is not a universal novelty proof. Unindexed design enumerations remain a priority risk.

## Value — PASS

The order thirteen is the first Steiner triple-system size admitting two nonisomorphic designs. Cross-free sets are motivated by the extremal component problem of Gyárfás. A full classification of all maximum equal-size three-class configurations in *both* systems therefore tests how that extremal notion depends on design structure, rather than choosing an arbitrary small graph or arbitrary parameter. The Pasch switch changes the configuration count by 66 and changes the accessible exchange topology: 39 isolated four-cliques versus eighteen four-cliques and four seven-state pairs of glued four-cliques. This is a meaningful finite structural discriminator, despite no claimed asymptotic application. The general all-or-none insertion lemma explains the forced four-cliques and the divisibility-by-three of every exchange degree.

## Closest literature and limitations

- A. Gyárfás (2015), *Large Cross-Free Sets in Steiner Triple Systems*, arXiv:1509.05527, https://arxiv.org/abs/1509.05527. This motivates the underlying extremal notion and supplies general background.
- M. Pavone (2023), *A visual representation of the Steiner triple systems of order 13*, https://iris.unipa.it/retrieve/674a8990-dc17-457f-b6b2-f2261c09ebde/Picture%20STS%2813%29_2023_01_05.pdf. This supplies concrete representatives and the Pasch switch, and discusses a different colouring notion.
- D. Heinlein and P. R. J. Östergård (2022), *Algorithms and complexity for counting configurations in Steiner triple systems*, https://doi.org/10.1002/jcd.21839. Its counting problem is about prescribed systems of blocks.

This is a self-review of an exhaustive finite argument, not external peer review. Complete historical priority is unproved; unindexed historical literature was not represented as checked. The large connected components are not classified up to abstract isomorphism beyond the stated invariants.

Self-review: passed. Independent audit: not yet performed.
