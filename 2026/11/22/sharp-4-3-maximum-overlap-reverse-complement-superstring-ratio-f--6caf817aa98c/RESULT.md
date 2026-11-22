# Sharp \(4/3\) maximum-overlap reverse-complement superstring ratio for binary four-mers

## Finding

Let \(\Sigma=\{0,1\}\), with complement \(\bar0=1\), \(\bar1=0\). Define \(\operatorname{rc}(x_1\cdots x_m)=\bar x_m\cdots\bar x_1\). Each binary four-mer belongs to the class \([u]=\{u,\operatorname{rc}(u)\}\). Their ten classes have lexicographically least representatives, in this fixed order:

`0000 0001 0010 0011 0100 0101 0110 1000 1010 1100`.

An instance is a nonempty subset \(S\) of these classes. Let \(L(S)\) be the minimum length of a *linear* word containing at least one member of each class in \(S\). Start greedy assembly with the listed representative of each selected class. At each step orient two *distinct* components arbitrarily by applying \(\operatorname{rc}\), order them arbitrarily, and join by the maximum proper suffix-prefix overlap. Globally maximize overlap over all such choices, allowing arbitrary ties. Remove any remaining component contained in an assembled component, in either orientation (no such removal actually arises in this exhaustive domain). Continue until one component remains. Let \(G(S)\) be the longest final word possible under legal tie choices.

Then the exact sharp ratio is

\[
\max_{\varnothing\ne S\subseteq \Sigma^4/\operatorname{rc}} \frac{G(S)}{L(S)}=\frac43.
\]

Exactly six instances attain equality. Encoding selected representatives by bit positions \(0,\ldots,9\) in the displayed order, their masks are `131`, `159`, `183`, `215`, `407`, `663`. At `131`, \((L,G)=(6,8)\); for each other mask, \((L,G)=(9,12)\). For all ten classes, \((L,G)=(13,16)\). These numbers concern the simple pairwise maximum-overlap GREEDY-RC algorithm, *not* MGREEDY-RC or TGREEDY-RC.

## Assumptions and scope

All words are binary and all initial reads have length exactly four. Input sets are irredundant: no two selected representatives are in the same reverse-complement class. The physical complement is an involution without fixed symbols. The algorithm is nondeterministic only in its global overlap-maximizing tie choices; \(G\) takes the **maximum**, not an expectation or a prescribed tie-breaking rule. Only proper suffix-prefix overlaps between distinct current components count. The input and output are linear words. Substring containment removal is permissible and is inert on these reachable states, as verified explicitly. \(L\) is the unrestricted optimal covering length, not an overlap-graph surrogate.

## Proof

**1. Finite complete input space.** The action of reverse complementation on the sixteen four-mers has four fixed points and six two-element orbits, hence ten distinct classes. A valid irredundant input is exactly one of the \(2^{10}-1=1023\) nonempty subsets. The fixed ten representatives above enumerate them once each.

**2. Exact optimal length.** The word `0010100001100` has length thirteen and contains at least one member of every class, as direct four-window scanning confirms. Hence \(L(S)\le13\) for every instance. For each binary length \(4\le m\le13\), enumerate all \(2^m\) words \(w\), compute its mask \(C(w)\) of covered reverse-complement four-mer classes, and update the best known length for **every** mask \(S\subseteq C(w)\). Every shortest covering word is present, because one of length at most thirteen exists. Thus the resulting \(L(S)\) table is exact, without an unsearched length range.

**3. Exact greedy length.** Encode a current state by its sorted collection of strings after quotienting the independent reverse-complement orientation of each component. For each pair of distinct components, exhaust both orders and both orientations. Let \(h\) be the maximum proper suffix-prefix overlap over these choices; retain **all** merges achieving \(h\), normalize, and recurse. For a one-component state return its length; for a larger state return the maximum over all legal successors. Each merge reduces component count, so induction on component count proves that this recurrence yields **exactly** \(G(S)\), including all tie choices. Canonical orientation preserves the successor set because each component may be independently reversed and complemented at the next merge. The two independent implementations agree on every one of the \(1023\) instance pairs \((L,G)\). The C++ checker explores \(40082\) normalized states; the Python checker reaches \(41391\) states under a different cache/normalization traversal. The complete nonzero \((L,G)\) frequency table is printed by both checkers.

**4. Sharp bound and all equality cases.** Exhaustive integer comparison \(3G(S)\le4L(S)\) passes for all \(1023\) instances, and equality occurs at precisely the six stated masks. For mask `131` the instance is `0000,0001,1000`; the length-six word `011110` covers all its classes. A legal greedy execution first merges oriented `0111` with `1110` at overlap three, producing `01110`, then merges `0000` with `01110` at overlap one, giving `00001110` of length eight. The independently exhaustive optimal-word table establishes that no covering length below six exists; the greedy recurrence establishes that eight is the largest greedy outcome. Consequently \(8/6=4/3\) is attained. At all ten classes a length-thirteen optimal word is displayed above, while the maximum greedy length is sixteen.

## Verification

Compile and execute `verify_cpp.cpp` using `g++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp`; execute `python3 verify_python.py`. Both independently enumerate all \(1023\) nonempty input masks, compute exact optimal coverings by checking binary words of length four through thirteen and exact worst greedy outcomes by complete memoized recursion, then print all equality masks and the full joint frequency table. Their recorded results are in `verify_cpp_output.txt` and `verify_python_output.txt`. The observed joint tables agree entry for entry; their counts sum to \(1023\). Each program recomputes results rather than trusting the recorded logs. The explicit six/eight witness also admits direct hand checking.

## Relationship to prior work

The SCS-RC formulation and pairwise orientation-aware greedy assembly are standard in the cited SCS-RC literature. Yamano and Shibuya (2026, November 12 version, arXiv:2611.16573) establish general approximation guarantees for cycle-cover-based **MGREEDY-RC** and **TGREEDY-RC**, not an exact maximum for the simple **GREEDY-RC** over all subsets of the ten binary four-mer reverse-complement classes. Their earlier 2026 work (arXiv:2603.26176, March 27) gives general SCS-RC algorithms and hardness. A related published exact binary three-mer result concerns **ordinary** SCS, where input orientation is not free. The previous complete binary four-mer greedy spectrum concerns the *full* ordinary-SCS four-mer set, not arbitrary reverse-complement subsets. These distinctions are by mathematical input domain and algorithm, not merely terminology. Earlier reverse-complement universal-word work identifies optimal full-coverage constructions, without this worst-tie greedy census.

## Limitations

This is a complete but finite classification, not a proof of a corresponding \(4/3\) bound for arbitrary read lengths, larger alphabets, multisets, or other greedy variants. The numerical outputs depend on counting every global tie choice, and on the stated reverse-complement orientation rule. The unindexed literature could contain an equivalent finite census. No independent external validation is asserted.

## References

1. R. Yamano and T. Shibuya, *Tight Cycle-Cover Inequalities and Improved Approximation for Shortest Common Superstring with Reverse Complements*, arXiv:2611.16573v1, publicly posted 2026-11-12, https://arxiv.org/abs/2611.16573.
2. R. Yamano and T. Shibuya, *Improved Approximation Algorithms and Hardness Results for Shortest Common Superstring with Reverse Complements*, arXiv:2603.26176v1, 2026-03-27, https://arxiv.org/abs/2603.26176.
3. R. Yamano and T. Shibuya, *Improved Approximation Ratios for the Shortest Common Superstring Problem with Reverse Complements*, CPM 2026, https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.15/LIPIcs.CPM.2026.15.html.
4. Y. Orenstein and R. Shamir, *Design of shortest double-stranded DNA sequences covering all k-mers*, Bioinformatics 29(13), 2013, https://pmc.ncbi.nlm.nih.gov/articles/PMC3694677/.
5. *Sharp binary three-word greedy superstring ratio and all equality cases*, prior exact ordinary-SCS finite census, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-binary-three-word-greedy-superstring-ratio-and-all-equalit--f43f5caa07c5.
