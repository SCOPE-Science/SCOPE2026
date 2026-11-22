# A linear adaptive shattering gap in fixed-composition ternary words

## Finding
For each integer \(m\ge1\), let \(\mathcal H_m\) consist of all length-\(4m\) words over the named alphabet \(\{A,B,C\}\), with **exactly** \(2m\) occurrences of \(A\), \(m\) of \(B\), and \(m\) of \(C\). The Boolean test \((i,c)\) asks whether the letter at position \(i\) is \(c\). Then
\[
\boxed{\operatorname{VCdim}(\mathcal H_m)=2m,\qquad
\operatorname{Ldim}(\mathcal H_m)\ge3m.}
\]
Thus these exact-content classes have an **unbounded linear adaptive-minus-static shattering gap**. For the four-position seed with content \((2,1,1)\), the exact dimensions are \(\operatorname{VCdim}=2\) and \(\operatorname{Ldim}=3\). The contribution asserted as new is the online lower bound and its direct-product amplification, not the classical fixed-composition feasibility/closure structure.

## Assumptions and scope
Positions are labeled; three colors are distinct, even when their multiplicities agree. A single test has yes/no outcome. VC dimension concerns a fixed set of such tests on which every binary assignment is realized. Littlestone dimension concerns a complete *adaptive* binary tree of such tests, where the choice of test may depend on previous outcomes and every root-to-leaf answer sequence is realized by a word. No assumptions about random words, multivalued feedback, or incorrect labels are made. Only the displayed exact static dimension and adaptive *lower bound* are established for arbitrary \(m\); a larger online dimension is not excluded.

## Proof
**1. Static upper bound.** Consider any shattered test support \(S\). A pair of tests asking for different colors at the same position cannot both return yes, so at most one test per position can occur. Suppose \(|S|\ge2m+1\). Prescribe 'no' to every test of the form \((i,A)\), and 'yes' to every test of the form \((i,B)\) or \((i,C)\). This prescribes a definite non-\(A\) letter at *each* of the \(|S|\) tested positions, leaving at most \(4m-|S|\le 2m-1\) positions for the requisite \(2m\) occurrences of \(A\). The prescribed answer pattern is impossible. Hence \(\operatorname{VCdim}\le2m\).

**2. Static lower bound.** Select \(m\) distinct positions and query whether each contains \(B\); select \(m\) further distinct positions and query whether each contains \(C\). There are \(2m\) unqueried positions. For any labeling of these \(2m\) tests, put the indicated \(B\) or \(C\) at each yes position and put \(A\) at every no position. If \(p\) queries were yes, the tests use \(2m-p\) copies of \(A\); exactly \(p\) copies of \(A\), together with the unplaced \(B\) and \(C\), occupy the remaining \(2m\) unqueried positions in any order. All prescribed multiplicities and answers are realized. Hence \(\operatorname{VCdim}\ge2m\), proving equality.

**3. Explicit depth-three seed.** On four positions, there are exactly \(4!/(2!1!1!)=12\) words with content \(AABC\). The following table specifies a complete adaptive tree. Ask \((1,A)\) first. After two answers, ask the third-level test in the table; the final columns give a realizing word for each third answer. A '0' means no, and a '1' means yes.

| First two answers | Second test | Third test | Word for final 0 | Word for final 1 |
|---|---|---|---|---|
| 00 | \((1,B)\) | \((2,A)\) | `CBAA` | `CAAB` |
| 01 | \((1,B)\) | \((2,A)\) | `BCAA` | `BAAC` |
| 10 | \((2,A)\) | \((2,B)\) | `ACAB` | `ABAC` |
| 11 | \((2,A)\) | \((3,B)\) | `AACB` | `AABC` |

In this table the two-digit prefix always means the answers to the *first test and then the indicated second test*. Every listed word has two \(A\)'s, one \(B\), one \(C\), and realizes all three prescribed answers. Hence the entire depth-three tree is shattered. A depth-four complete binary tree would require at least \(16\) distinct concepts, because distinct leaves have incompatible answer histories, but the seed has just \(12\). Therefore its Littlestone dimension is exactly three.

**4. Amplification without weakening the global composition constraint.** Partition the \(4m\) positions into \(m\) predesignated four-element groups. Restrict to the subfamily in which *every* group has composition \(AABC\). This is a Cartesian product of \(m\) copies of the seed and is contained in \(\mathcal H_m\), since the global multiplicities are \((2m,m,m)\). At every branch of a depth-three tree for the first group, append the same depth-three seed tree for the second group, and so on. Test only positions within the currently active group. Every length-\(3m\) answer path is realized by independently choosing, group by group, the leaf word prescribed in the seed table. Thus \(\operatorname{Ldim}(\mathcal H_m)\ge3m\). Combining with the static result gives the claimed gap for all \(m\ge1\).

The proof uses an exact finite seed, a fully explicit finite tree, and a genuine all-order product argument. It does not infer an infinite assertion from finite enumeration.

## Verification
Run `python3 checker/verify_online.py` in the extracted package root. This standard-library-only program reads `checker/depth3_tree.json`, enumerates the twelve distinct seed words, verifies all eight full paths against their leaf witness words, and checks the cardinality obstruction to a depth-four tree. It prints `TERNARY_FIXED_CONTENT_DEPTH3_PASS 12 hypotheses 8 certified leaves` and `BASE_VC_2_LITTLESTONE_3`.

An additional independent finite corroboration of the underlying fixed-content static support criterion is supplied as `checker/check_quota.cpp`. Compile with `g++ -std=c++17 -O2 checker/check_quota.cpp -o check_quota && ./check_quota`, which reproduces `checker/quota_output.txt`. The enumerator computes the traces of each candidate support directly for nine finite multiplicity profiles, including the seed \((2,1,1)\) and the balanced profile \((2,2,2)\); it reports `QUOTA_SHATTERING_EXHAUSTIVE_PASS 61481 supports`. The general static and adaptive claims do **not** depend on that enumeration.

## Relationship to prior work
Generalized chessboard complexes with per-row and per-color capacity constraints were studied by Jojić, Panina, Vrećica and Živaljević (2020). In particular the abstract capacity complex and its row/column faces are not new here. A prior fixed-composition formal-concept-lattice classification establishes all feasible partial assignments and their closures; this implies static support-compatibility conditions and is **prior stronger structural coverage** for that aspect. A separate previous result on onto maps gives shattering for *unrestricted surjective words*, whose variable multiplicities prevent direct application to a fixed content class. Those earlier results do not analyze the adaptive decision tree on fixed composition words or imply its linear-versus-static gap.

Earlier results showing VC/Littlestone separation for proper graph colorings, size-constrained equivalence relations, and uniform triple partitions use different concept families or different query semantics, so their mistake trees cannot be transplanted to these three-color fixed-content words without new argument. The self-contained four-position seed and its all-parameter repetition are the specific mathematical contributions here. Direct comparisons are grounded in the named primary source materials, but the possibility of equivalent online-learning results under other terminology remains a priority risk.

## Limitations
There is no claim of an exact Littlestone dimension for \(m\ge2\); only a constructive lower bound is established. The static dimension proof and the fixed-composition feasibility mechanism are elementary consequences of existing stronger context/closure results, not standalone novelty. No homology or higher-dimensional topology of the associated shattering complex is claimed. The finite tree is verified exhaustively, but the all-order online assertion rests on the concatenation proof. Independent expert audit and definitive historical priority verification have not been performed.

## References
1. D. Jojić, G. Panina, S. T. Vrećica, R. T. Živaljević, *Generalized chessboard complexes and discrete Morse theory*, arXiv:2003.04018, first publicly posted 2020-03-09; Section 3 (generalized chessboard complexes and capacities). https://arxiv.org/abs/2003.04018
2. J.-S. Leboeuf, F. LeBlanc, M. Marchand, *Generalization Properties of Decision Trees on Real-valued and Categorical Features*, arXiv:2210.10781, first publicly posted 2022-10-18; Section 5.3 (unconstrained nominal categorical tests). https://arxiv.org/abs/2210.10781
3. *Fixed-composition concept lattices: optimal one-pass bases and all-interval Möbius values*, published-finding corpus research record 2026-10-25, full RESULT.md; complete closure of positive position--color assertions at exact prescribed multiplicities. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-fixed-composition-concept-lattices-optimal-one-pass-bases-and-al--0007de354604
4. *Shattering complexes of finite onto maps: a duplicate-color criterion and a matroid boundary*, published-finding corpus research record 2026-11-08, full RESULT.md; support classification for unrestricted onto maps, explicitly excluding capacities. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-shattering-complexes-of-finite-onto-maps-a-duplicate-color-crite--372d7004c379
5. *First adaptive-shattering gap for size-prescribed two-block equivalence relations*, published-finding corpus research record 2026-11-02; an adjacent but different pair-equality query class. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-first-adaptive-shattering-gap-for-size-prescribed-two-block-equi--2b18e419d19e
