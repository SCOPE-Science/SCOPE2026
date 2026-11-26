# Minimum six-block trades among labelled Steiner triple systems of order nine

## Finding

Let \(V=\{0,1,\ldots,8\}\). A Steiner triple system on \(V\) is a set \(S\) of twelve distinct three-element blocks such that every two-element subset of \(V\) belongs to exactly one block. Let \(\mathcal T\) be the graph whose vertices are **all distinct labelled** Steiner triple systems on this fixed point set, with no identification under relabelling. Distinct systems \(S,T\) are adjacent precisely when a trade replaces six blocks, equivalently \(|S\cap T|=6\).

**Theorem.** The graph \(\mathcal T\) is the transposition-generated Schreier graph for the natural action of \(S_9\) on \(S_9/\operatorname{AGL}(2,3)\). It is connected and \(36\)-regular, with \(840\) vertices, \(15{,}120\) edges, and diameter \(3\). Every six-block trade between systems is exactly the effect of transposing two point labels; conversely, every point transposition realizes a six-block trade.

For any two systems \(S,T\), the exact graph distance is determined solely by the number \(k=|S\cap T|\) of common blocks:

| Common blocks \(k\) | Trade-graph distance \(d(S,T)\) | Number of such \(T\) for every fixed \(S\) |
|---:|---:|---:|
| \(12\) | \(0\) | \(1\) |
| \(6\) | \(1\) | \(36\) |
| \(4\) | \(2\) | \(27\) |
| \(3\) | \(2\) | \(152\) |
| \(2\) | \(2\) | \(216\) |
| \(1\) | \(3\) | \(216\) |
| \(0\) | \(3\) | \(192\) |

No other values of \(k\) occur. Hence every vertex has distance distribution \((1,36,395,408)\), at distances \(0,1,2,3\). These are exact assertions over all \(840\) labelled systems, not numerical approximations.

## Assumptions and scope

A *trade* from \(S\) to \(T\) means replacing exactly the blocks in \(S\setminus T\) by those in \(T\setminus S\); its volume is \(|S\setminus T|=12-|S\cap T|\). Both endpoints must be ordinary (proper) Steiner triple systems throughout. A trade step is a simultaneous six-block replacement, **not** six separate one-block steps, and intermediate improper or incomplete systems are not admitted. A graph path may have several six-block steps, and its length counts the number of these steps. Graph isomorphism classes are *not* collapsed. The chosen labels of the nine points do not affect the statement.

## Proof

**1. Complete finite domain.** Index the \(84=\binom{9}{3}\) triples and the \(36=\binom{9}{2}\) pairs in lexicographic order. Associate to a triple the \(36\)-bit mask of its three contained pairs. In the exact-cover search, choose an as-yet-uncovered pair, branch over every triple containing this pair whose pair mask is disjoint from all covered pairs, and recurse. Reaching the full \(36\)-pair mask produces one system with twelve blocks. Every system is reached because it contains a unique triple covering each selected pair, and no system is produced twice because each recursion choice is forced by the pair covering relation. This terminating, exhaustive search yields exactly \(840\) distinct systems. The full executable search and all assertions are in `verify/exact_cover_bfs.py`.

**2. Schreier structure.** Identify the nine points with \(\mathbb F_3^2\) and let \(S_0\) consist of the triples of distinct vectors whose sum is zero. A direct verification shows that \(S_0\) is a Steiner triple system; its entire relabelling orbit contains exactly the \(840\) systems from step 1. Its stabilizer is the affine group \(\operatorname{AGL}(2,3)\) of order \(9\cdot48=432\): all such affine maps preserve its lines, and \(9!/840=432\), so no further stabilizers exist. Thus the labelled configuration space is the stated coset space.

Fix any two distinct labels \(a,b\). Four blocks contain \(a\), four contain \(b\), and their unique common block contains both. This common block is unchanged by transposing \(a,b\). The other three blocks through \(a\) and other three through \(b\) are replaced, so the transposition changes exactly six blocks. The \(36\) transpositions yield \(36\) distinct neighboring systems: if two yielded the same system, their product would be a nontrivial stabilizer moving at most four points. Yet a nonidentity affine map on \(\mathbb F_3^2\) has at most three fixed points, so it moves at least six. The exhaustive exact-cover test examines all \(\binom{840}{2}=352{,}380\) unordered system pairs and finds exactly \(36\) neighbors with six common blocks per system. Therefore these transposition images are **all** six-block trades. Since transpositions generate \(S_9\), the graph is connected, and its edge count is \(840\cdot36/2=15{,}120\).

**3. Exact distance law.** A permutation \(\pi\in S_9\) has minimum transposition length \(9-c(\pi)\), where \(c(\pi)\) counts its cycles, including fixed points. If \(T=\pi(S_0)\), the Schreier identification implies
\[
 d(S_0,T)=9-\max_{h\in\operatorname{AGL}(2,3)}c(\pi h).
\]
The independent coset verifier lists all \(9!\) permutations, all \(432\) affine stabilizer elements, and one representative for each of the \(840\) cosets. For each coset it evaluates the displayed formula over all \(432\) representatives; it also determines the number of shared blocks with \(S_0\). This exact calculation yields the seven rows of the table. Separately, the exact-cover verifier performs breadth-first search from **every** one of the \(840\) systems and confirms that every pair's distance has the stated value. Relabelling transitivity transfers the coset calculation at \(S_0\) to every base system, so the table holds for every ordered pair. The largest distance is \(3\).

This is a finite exhaustive proof: the computational assertions are applied to precisely enumerated finite sets. The code gives the complete search trees/loops and fails on any violated count or identity; it does not extrapolate from tested sizes.

## Verification

Two standalone Python 3 files, with no third-party dependencies, are supplied in `verify/`.

* `verify/exact_cover_bfs.py` constructs all Steiner triple systems from pair-coverage constraints, tests every unordered system pair, confirms the \(15{,}120\) legal trades, and independently performs all \(840\) breadth-first searches and intersection comparisons.
* `verify/group_cosets.py` constructs \(\mathbb F_3^2\), the entire \(432\)-element affine group and all \(9!\) relabellings, generates the trade graph via point transpositions, and verifies the coset transposition-length formula and its common-block spectrum.

From a directory containing the `verify` folder, run `python3 verify/exact_cover_bfs.py` and `python3 verify/group_cosets.py`. Both programs return normally only after all assertions pass and print their corresponding `PASS` messages. All arithmetic is integer arithmetic; there is no randomness, floating-point threshold, external database, or unproved extrapolation.

## Relationship to prior work

The uniqueness up to isomorphism of the Steiner triple system of order nine, its known count \(840\) of labelled realizations, the classical possibilities for the number of common blocks, and the general definitions of Steiner trades are **not new claims**. Lindner and Rosa's intersection theorem, quoted in Chee–Ling–Shen, already gives precisely the possible common-block sizes \(\{0,1,2,3,4,6,12\}\). Forbes's trade classification documents the small trade volumes and configurations.

Cameron's 2002 Markov-chain notes explain connectivity under a **different** transition rule that includes improper triple systems, and in the order-nine case a point transposition takes two of those moves (the proof cited from Grannell and Griggs). That is not the graph of proper systems connected directly by a simultaneous six-block trade. Forbes, Grannell and Griggs investigate minimum **one-trade volume after allowing an isomorphism of the target** and concentrate on the eighty unlabelled systems of order fifteen; their distance is not the number of minimum-trade steps between two labelled order-nine systems.

The present contribution is the exact order-nine **proper six-block trade graph**, its Schreier-graph identification, and especially its complete shortest-path metric expressed by common-block intersection (including the \(395\)- and \(408\)-element distance layers). A 2003 chapter by Griggs and Rosa on uniformly intersecting collections of order-nine systems was identifiable but not available in full; it is a concrete remaining priority risk.

## Limitations

This theorem covers only ordinary labelled Steiner triple systems of **order nine**, with edges given by trades of volume exactly six. It says nothing about trade graphs on higher-order systems, other trade volumes, rates of mixing of random walks, or unlabelled quotient graphs. Its proof uses finite exhaustive enumeration and two standalone checkers; no independent scholarly audit or priority certification has been performed. Literature not available in full, notably the 2003 Griggs–Rosa chapter, could contain an equivalent statement under different terminology.

## References

1. Y. M. Chee, A. C. H. Ling, and H. Shen, *The Fine Intersection Problem for Steiner Triple Systems*, arXiv:0807.2500, first publicly posted 2008-07-16. https://arxiv.org/abs/0807.2500 (including its quotation of Lindner and Rosa's 1975 theorem).
2. P. J. Cameron, *A Markov Chain for Steiner Triple Systems*, notes dated February 2002, especially sections 3–5. https://webspace.maths.qmul.ac.uk/p.j.cameron/csgnotes/random.pdf
3. A. D. Forbes, M. J. Grannell, and T. S. Griggs, *Distance and Fractional Isomorphism in Steiner Triple Systems*, author preprint copyright 2006, especially sections 1 and 3. https://grannell.net/Papers/FRACISO.pdf
4. A. D. Forbes, *Configurations and Colouring Problems in Block Designs*, PhD thesis, Open University, November 2006, chapters 5–6. https://oro.open.ac.uk/64246/1/13917230.pdf
5. T. S. Griggs and A. Rosa, *Sets of Steiner Triple Systems of Order 9 Revisited*, in *Designs 2002*, 2003, pages 255–276. DOI:10.1007/978-1-4613-0245-2_10 (abstract verified; full text not inspected).
