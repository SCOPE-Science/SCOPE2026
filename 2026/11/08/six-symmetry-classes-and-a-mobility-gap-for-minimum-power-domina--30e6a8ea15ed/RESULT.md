# Six symmetry classes and a mobility gap for minimum power domination of the five-cube

## Finding

Let \(Q_5\) be the five-dimensional binary hypercube. Its vertices are the integers \(0,\ldots,31\), regarded as five-bit vectors, and two vertices are adjacent if their Hamming distance is one. A power-dominating set initially observes its closed neighborhood; subsequently, an observed vertex with exactly one unobserved neighbor observes that last neighbor. A *minimum* power-dominating set (PDS) has the smallest possible cardinality. Let \(\mathcal P\) be the family of minimum PDSs, and consider two graphs on \(\mathcal P\): \(R_{\mathrm{TS}}\), whose moves exchange one selected vertex for an **adjacent** unselected vertex, and \(R_{\mathrm{TJ}}\), whose moves exchange one selected vertex for **any** unselected vertex.

**Theorem (complete finite classification).** The known minimum cardinality is \(\gamma_P(Q_5)=4\). There are exactly \(3600\) minimum PDSs, forming exactly six orbits under bit translations and coordinate permutations, with the following representatives and invariants. Each representative is a set of integer-labelled five-bit vertices. The degree and eccentricity refer to \(R_{\mathrm{TJ}}\).

| Representative | Orbit size | TJ degree | TJ eccentricity |
|:--|--:|--:|--:|
| \(\{0,1,14,15\}\) | 160 | 16 | 5 |
| \(\{0,1,14,23\}\) | 960 | 22 | 5 |
| \(\{0,1,14,30\}\) | 320 | 14 | 5 |
| \(\{0,3,13,14\}\) | 240 | 16 | 6 |
| \(\{0,3,13,22\}\) | 960 | 22 | 6 |
| \(\{0,3,13,28\}\) | 960 | 18 | 6 |

Every minimum PDS is **token-slide frozen**: \(R_{\mathrm{TS}}\cong 3600K_1\). In contrast, \(R_{\mathrm{TJ}}\) is connected with \(35200\) undirected edges, radius \(5\), and diameter \(6\). Its degree distribution is \(14^{320},16^{400},18^{960},22^{1920}\), and its eccentricity distribution is \(5^{1440},6^{2160}\), where exponents mean state multiplicities. Thus maintaining optimal monitoring is compatible with globally connected unrestricted replacements but not even one adjacent relocation on the five-cube.

## Assumptions and scope

The hypercube is the simple Cartesian product of five copies of \(K_2\), not a geometric graph with extra diagonals. Monitoring is the **standard** power-domination propagation rule, and replacement moves require *all intermediate configurations* to retain minimum cardinality and power domination. Tokens and vertices are unlabelled and labelled, respectively; exchanges with the same selected subset do not create loops. The classification is for the single natural host graph \(Q_5\), not a claim for every dimension. The known value \(\gamma_P(Q_5)=4\) follows already from the hypercube bounds in Dean et al. (2011), and is not claimed as new.

## Proof

**Step 1 (minimum size).** For the five-cube, Dean et al. proved the inequalities \(2^{n-1}/n\le\gamma_P(Q_n)\le 2^{n-\lfloor\log_2 n\rfloor-1}\). Setting \(n=5\) gives \(16/5\le \gamma_P(Q_5)\le4\), so \(\gamma_P(Q_5)=4\). The attached verification independently checks all subsets of at most three vertices and finds none power-dominating.

**Step 2 (complete finite power-domination decision).** Fix \(S\subseteq\{0,\ldots,31\}\) of size four. The following deterministic decision algorithm is necessary and sufficient. Form a 32-bit observed mask \(O=\bigcup_{s\in S}N[s]\). While an observed vertex \(u\) has an unobserved-neighbor mask \(N(u)\setminus O\) consisting of exactly one bit, set that bit in \(O\). The operation is monotone and the least closed observed set is independent of the order of legal forces: if some force is legal at a stage, its target is either already observed later or is still that observed vertex's unique unobserved neighbor. Hence termination at the all-ones 32-bit mask is equivalent to power domination. Every loop has at most 32 strict additions. All \(\binom{32}{4}=35960\) four-subsets are examined in `verification/check_orbits.py` and, using a different update order and representation, in `verification/check_independent.cpp`; both return exactly \(3600\) successes.

**Step 3 (symmetry classes).** All Hamming isometries preserve the monitoring and reconfiguration rules. These maps are exactly the bit translations \(v\mapsto v\oplus t\) together with the coordinate permutations; there are \(32\cdot5!=3840\) such maps. The executable certificate applies all of them to the lexicographically first remaining successful set. It checks that every orbit element is successful, deletes that orbit from the remaining successful sets, and repeats until no states remain. The six rows in the theorem are exactly the six resulting representatives; their orbit sizes sum to \(3600\). This is an exhaustive orbit partition, not a sample or an inference from pairwise-distance multisets (which do not always determine the orbit).

**Step 4 (all legal moves).** For every successful \(S\), for each \(u\in S\) and \(v\notin S\), the code forms \(T=(S\setminus\{u\})\cup\{v\}\) and tests membership in the complete successful-state set. This traverses every possible token jump once per orientation. Exactly \(70400\) oriented jumps occur, giving \(35200\) undirected TJ edges, and none has Hamming distance \(d(u,v)=1\); therefore the TS graph has no edges. The resulting TJ degrees on each of the six orbits appear in the table. The independently written C++ checker reconstructs these edges by direct mask exchanges and agrees exactly.

**Step 5 (exact metric).** Breadth-first search from each of the six orbit representatives reaches all \(3600\) states, proving connectedness. Their respective maximum distances are \(5,5,5,6,6,6\). Since each Hamming isometry induces an automorphism of \(R_{\mathrm{TJ}}\), eccentricity is constant on each orbit. Thus the entire graph has radius \(5\), diameter \(6\), and the specified eccentricity histogram. The C++ checker independently performs full breadth-first search from **every** one of the \(3600\) states, providing a separate exhaustive confirmation.

## Verification

The attached `verification/check_orbits.py` (Python 3, standard library only) performs exact exhaustive power-domination tests, a full six-orbit Hamming-symmetry certificate, every TS/TJ move test, and the six representative BFS searches. Run `python3 verification/check_orbits.py` from the package root. The independently implemented `verification/check_independent.cpp` uses direct sequential propagation, a different set encoding, and all-pairs BFS; run `g++ -std=c++17 -O2 verification/check_independent.cpp -o check && ./check`. The executed outputs are embedded as `verification/python_output.txt` and `verification/cpp_output.txt`. The written programs use assertions for all stated cardinalities, orbit rows, degrees and distances.

The exhaustive bounds are explicit: \(\sum_{j=1}^{3}\binom{32}{j}=5488\) smaller candidate sets and \(35960\) four-subsets, \(3840\) isometries applied to each of six representatives, at most \(4\cdot28\) candidate exchanges per successful set, and BFS over no more than \(3600\) states. Machine computation is a **finite** proof of these finite enumerative assertions, supported by two differently structured exact programs; no assertion is made about larger cubes.

## Relationship to prior work

Dean, Ilic, Ramirez, Shen and Tian (2011) establish bounds on the power-domination number of hypercubes that already imply the cardinality four at dimension five. Their four-page full text contains no enumeration of all minimum sets, Hamming-symmetry orbit decomposition, or fixed-host TS/TJ reconfiguration metrics. Benson et al. (2015) generalize the power-domination/zero-forcing inequality and study graph products, without supplying the present exact five-cube classification. Bjorkman et al. (2026) study reconfiguration of power-dominating sets using token addition/removal and token jumping, state TS as a further research direction, and do not give this exact five-cube state graph. A 2012 conference note by Pai and Chiu on hypercube power domination was identified, but only abstract material was accessible and complete coverage by that note cannot be excluded from the accessible material. The present claim is restricted to the new enumerative and reconfiguration facts, not the known minimum cardinality.

## Limitations

The classification is exact only for \(Q_5\). It does not imply universal rigidity in higher-dimensional hypercubes, nor prove a general polynomial-time algorithm. The full 2012 Pai–Chiu note and any unindexed equivalent finite computation remain a historical-priority risk. Independent scholarly audit has not occurred. Reproduction requires Python 3 and a C++17 compiler; the supplied code is short and deterministic, and its assertions must be executed rather than inferred from output text alone.

## References

1. N. Dean, A. Ilic, I. Ramirez, J. Shen, K. Tian, *On the Power Dominating Sets of Hypercubes*, 14th IEEE International Conference on Computational Science and Engineering, pp. 488–491 (2011), author-hosted full text: https://kjtian.github.io/PDSHypercube.pdf.
2. K. F. Benson, D. Ferrero, M. Flagg, V. Furst, L. Hogben, V. Vasilevska, B. Wissman, *Zero forcing and power domination for graph products*, preprint first posted 2015-10-08: https://arxiv.org/abs/1510.02421; full text https://ar5iv.labs.arxiv.org/html/1510.02421.
3. B. Bjorkman et al., *Power Domination Reconfiguration*, La Matematica (2026), open-access full text: https://link.springer.com/article/10.1007/s44007-025-00187-5.
4. K.-J. Pai and W.-J. Chiu, *A Note on “On the Power Dominating Sets of Hypercubes”*, 29th Workshop on Combinatorial Mathematics and Computation Theory, pp. 65–68 (2012); bibliographic record and abstract: https://www.yumpu.com/en/document/view/27830454/a-note-on-on-the-power-dominating-sets-of-hypercubes.
