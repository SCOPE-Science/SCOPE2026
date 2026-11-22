# Exactly six perfect cyclic Kendall codes on five symbols

## Finding
Let \(S_5\) be the set of all one-line permutations of \(\{0,1,2,3,4\}\). One cyclic adjacent swap exchanges positions \(i\) and \(i+1\pmod 5\), for any \(i\in\{0,1,2,3,4\}\). A perfect one-error-correcting code is a subset of \(S_5\) whose closed one-swap balls partition \(S_5\).

**Theorem.** Define the twenty-word affine code
\[
H=\bigl\{(b,a+b,2a+b,3a+b,4a+b)\bmod 5:
 a\in\mathbb F_5^{\times},\ b\in\mathbb F_5\bigr\}.
\]
There are **exactly six labeled perfect one-error-correcting codes** for this cyclic adjacent-swap channel, and they are precisely the six left cosets \(\varphi H=\{\varphi\circ h:h\in H\}\), for \(\varphi\in S_5\), using ordinary function composition. Every one has twenty words. Consequently all perfect designs are equivalent by a relabeling of symbols; no nonaffine perfect code exists.

## Assumptions and scope
The alphabet is the labeled set \(\mathbb F_5=\{0,1,2,3,4\}\). A permutation is the tuple of its values at positions \(0,1,2,3,4\). Exactly one substitution-free transposition is permitted, including the wraparound swap of positions \(4\) and \(0\). A closed ball includes the unchanged center as well as the five distinct one-swap outputs. “Perfect” means that **every one** of the \(5!=120\) received permutations is covered exactly once, not merely that the code is largest in a different metric. The claim is confined to length five and radius one; it does not classify ordinary (noncyclic) Kendall codes or other lengths.

## Proof
1. Put \(T=\{e,(0\ 1),(1\ 2),(2\ 3),(3\ 4),(4\ 0)\}\), where each transposition acts on **positions**. The radius-one ball about \(g\in S_5\) is exactly \(gT\). Every ball has six elements, so a perfect code must contain \(120/6=20\) centers.

2. The set \(H\) consists of the affine permutations \(x\mapsto ax+b\) of \(\mathbb F_5\), hence is a subgroup of order twenty. The six right translates \(Ht\), for \(t\in T\), are distinct. Indeed, if \(s,t\in T\) are different, \(st^{-1}\notin H\): a single adjacent-position transposition fixes three letters and cannot be a nonidentity affine permutation; two adjacent edges give a three-cycle (impossible in a group of order twenty); and two disjoint edges give \((i\ i+1)(j\ j+1)\), which, if affine, would be an involution \(x\mapsto-x+b\), forcing \(b=2i+1=2j+1\pmod5\), hence \(i=j\), contrary to distinct edges. Thus the right translates are disjoint and exhaust \(S_5\). Equivalently, the balls \(hT\), \(h\in H\), partition \(S_5\). Hence \(H\) and all its left cosets are perfect.

3. Relabeling the five symbols by any \(\varphi\in S_5\) is a channel isometry: it preserves which two **positions** are swapped. If a perfect code \(C\) contains a word \(c\), relabel by \(c^{-1}\), obtaining a perfect code that contains \(e\). It suffices to classify identity-containing perfect codes.

4. The finite certificate in `src/verify_python.py` enumerates **all** identity-containing perfect codes by exact cover, without imposing affine structure. It indexes all 120 permutations in lexicographic order, constructs every closed ball by applying each of the five swaps, starts with the ball of \(e\), and repeatedly chooses an uncovered permutation with the smallest number of remaining compatible balls. Each compatible choice is branched on. The recursion is exhaustive: in any completion, the selected uncovered permutation must lie in exactly one chosen ball, and every possible such center is considered. A branch having no compatible center is impossible. The search visits exactly 41 recursion nodes, finds four dead branches and **one** complete solution. That solution is exactly the twenty-member affine set \(H\). The separately implemented C++17 checker `src/verify_cpp.cpp` builds the incidence structure independently and returns the same 41/4/1 certificate.

5. Consequently, every perfect \(C\) is a left coset of \(H\). Distinct left cosets partition \(S_5\), so there are exactly \([S_5:H]=120/20=6\) labeled perfect codebooks. This proves both completeness and uniqueness up to symbol relabeling.

## Verification
Run from a directory containing the two supplied files:

```sh
python3 src/verify_python.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic src/verify_cpp.cpp -o verify_cpp
./verify_cpp
```

The Python checker reports `n_permutations=120`, `ball_size=6`, `normalized_exact_cover_nodes=41`, `dead_ends=4`, `normalized_solutions=1`, and `all_codebooks=6`; its normalized-node counts by selected centers are \(1,3,5,5,5,5,3,2\) at depths one through eight and one each at depths nine through twenty. The C++ checker independently reports `nodes=41; dead_ends=4; normalized_solutions=1; affine_solution=TRUE`. The Python verifier additionally constructs all six relabeled codebooks and checks that their one-swap balls are disjoint and cover all 120 permutations.

The proof of the all-codebook classification uses a finite **exhaustive** calculation, not an asymptotic extrapolation. The included complete implementations, the elementary exact-cover exhaustiveness argument and the small search tree supply replayable evidence; neither a timing log nor a sampled census is substituted for a proof.

## Relationship to prior work
Buzaglo and Etzion (first posted 2013-10-21) introduced this cyclic variant and explicitly constructed the twenty-word code \(H\) as an example. The existence of a perfect code, its size, and the affine construction are **not** new. The theorem here establishes that **every** perfect code is one of its six cosets, a uniqueness statement not supplied in their construction. Their later bounds work and the work of Wang and collaborators concern the *ordinary*, noncyclic Kendall channel, whose balls omit the wraparound transposition.

A published exact census of ordinary five-symbol Kendall-distance-three codes reports 3,192 maximum codebooks in 24 symbol-relabeling-and-reversal orbits, including one six-member orbit. This census contains the affine examples as ordinary codes, but its stated results do not impose wraparound correction or classify which of the other ordinary maxima meet the cyclic condition. The present exact-cover argument excludes all additional cyclic-perfect candidates, rather than claiming a new ordinary-Kendall optimum or a new affine construction.

## Limitations
The result does not extend the classification to \(S_n\) for \(n\ne5\), to more than one error, or to non-perfect cyclic codes. It also does not establish independent validation; the included programs are re-playable finite correctness certificates. The literature comparison cannot rule out unpublished or unindexed earlier enumerations of the same cyclic constraint. A 2016 article on ordinary five- and six-symbol Kendall optima was accessible through its abstract and bibliographic details, not a verified complete full-text inspection; its ordinary metric differs from the cyclic channel.

## References
1. Sarit Buzaglo and Tuvi Etzion, *Perfect Permutation Codes with the Kendall's \(\tau\)-Metric*, arXiv:1310.5515, first posted 2013-10-21, especially Section IV, https://arxiv.org/html/1310.5515v5.
2. Sarit Buzaglo and Tuvi Etzion, *Bounds on the Size of Permutation Codes with the Kendall \(\tau\)-Metric*, arXiv:1408.4963, first posted 2014-08-21, https://arxiv.org/abs/1408.4963.
3. Wang Xiang, Wang Yuanjie, Yin Wenjuan and Fu Fang-Wei, *Nonexistence of perfect permutation codes under the Kendall \(\tau\)-metric*, arXiv:2011.01600, first posted 2020-11-03, https://arxiv.org/abs/2011.01600.
4. Saravanan Vijayakumaran, *Largest Permutation Codes With the Kendall \(\tau\)-Metric in \(S_5\) and \(S_6\)*, IEEE Communications Letters 20(10), 1912–1915 (2016), DOI:10.1109/LCOMM.2016.2591003.
5. *Equality census for optimal \(S_5\) Kendall-\(\tau\) codes at distance \(3\)*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-equality-census-for-optimal-s-5-kendall-tau-codes-at-distance-3--01233b6e774d.
