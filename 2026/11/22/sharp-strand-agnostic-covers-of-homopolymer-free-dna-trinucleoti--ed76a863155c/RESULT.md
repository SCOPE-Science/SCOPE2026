# Sharp strand-agnostic covers of homopolymer-free DNA trinucleotides

## Finding

Let \(\Sigma=\{A,C,G,T\}\), with Watson–Crick complementation \(A\leftrightarrow T\) and \(C\leftrightarrow G\). A *homopolymer-free* word has unequal adjacent letters, including the last–first pair when circular. For a three-letter word \(x=abc\), let \(\rho(x)=\bar c\bar b\bar a\). A host is *complete* if its contiguous three-letter windows meet every reverse-complement orbit of homopolymer-free three-letter words.

There are exactly \(36\) allowed oriented target three-mers and \(18\) reverse-complement orbits. The **shortest complete linear word has \(21\) symbols**, giving \(19\) nonwrapping windows. **Exactly \(57{,}984\) labeled length-\(21\) linear words** attain this minimum. The **shortest complete circular word has \(20\) symbols**, giving \(20\) cyclic windows. **Exactly \(14{,}496\) length-\(20\) cycles up to rotation** attain this minimum (equivalently \(289{,}920\) indexed circular words).

The tight redundancy is rigid. A shortest linear word meets each reverse-complement class exactly once except that it visits precisely one of the classes \(\{ATA,TAT\}\) and \(\{CGC,GCG\}\) twice. A shortest circular word meets each class once except that **both** of these two classes are visited twice. In the linear case \(28{,}992\) optima repeat each of the two possible classes. A linear witness is `ATACACGACTCAGATGCGCTA`; a shortest circular witness, shown with a distinguished origin, is `ACACGACTATCAGAGCGCAT`.

## Assumptions and scope

The target set comprises exactly the three-mers \(abc\) with \(a\ne b\) and \(b\ne c\), not all DNA three-mers. A host is itself homopolymer-free. In a *linear* host only nonwrapping windows count. In a *circular* host all windows including wraparound count. A circular word of length \(L\) has \(L\) windows; two circular hosts are identified only when related by cyclic rotation. Reverse complementation, reversal, letter permutation, and shifts of linear words are **not** identification rules. Every enumeration is for the fixed four-letter labeled alphabet and order three; no biological binding-performance guarantee is claimed.

The three-mer reverse-complement involution has no fixed points because a fixed three-mer would require its middle letter to equal its own Watson–Crick complement. Thus the \(36\) allowed targets form precisely \(18\) two-element classes.

## Proof

**Quotient overlap graph.** Let \(G\) have one directed vertex for each of the \(12\) heterodimers \(ab\) with \(a\ne b\), and one directed edge \(ab\to bc\), labeled \(abc\), for every allowed three-mer. The involution on vertices is \(\rho(ab)=\bar b\bar a\). An edge \(ab\to bc\) is paired with the reverse-oriented edge \(\rho(bc)\to\rho(ab)\). Identifying vertices and edges with their reverse complements produces an undirected quotient multigraph \(Q\) with \(8\) vertices and \(18\) edges. A host path or closed walk in \(G\) projects to an undirected walk in \(Q\), with each target class recorded as its corresponding edge. A quotient loop contributes two to its vertex degree.

The four singleton vertex classes \(AT,TA,CG,GC\) have degree \(3\) each. The other four classes, represented by \(AC,AG,CA,GA\), have degree \(6\) each. The only edges of \(Q\) connecting *two distinct odd-degree vertices* are the classes \(\{ATA,TAT\}\), linking \(AT\) to \(TA\), and \(\{CGC,GCG\}\), linking \(CG\) to \(GC\). These assertions follow directly by tabulating the \(36\) allowed directed edges, pairing under \(\rho\), and adding their quotient incidences; both supplied programs reconstruct the same fixed tables.

**Sharp lower bounds and necessary repetitions.** If a linear host had just \(18\) windows, it would traverse all \(18\) edges of \(Q\) exactly once, giving an Euler trail. Four vertices of odd degree prohibit such a trail. Hence at least \(19\) windows, i.e. \(21\) symbols, are necessary. At exactly \(19\) windows one quotient edge is repeated. An open Euler trail can have only two odd vertices, so repeating that edge must join two of the original four odd vertices. Consequently only one of the two stated alternating-three-mer classes can be repeated, exactly once.

A complete circular host is a closed quotient walk. Starting with four odd vertices, repeating just one edge cannot make all degrees even. Thus at least \(20\) cyclic windows are required. At exactly \(20\) windows there are two surplus edge traversals. To correct the parity of all four odd vertices, their endpoints must be the four distinct odd vertices. The only odd-to-odd quotient edges are the two stated classes, so each must be traversed exactly twice and all other classes exactly once.

**Sharpness.** Direct inspection of the linear witness `ATACACGACTCAGATGCGCTA` gives \(19\) allowed three-mers, one from every class, with precisely the class \(\{CGC,GCG\}\) repeated. Direct inspection of the cyclic witness `ACACGACTATCAGAGCGCAT` gives \(20\) allowed cyclic three-mers, meeting all classes, with the \(\{ATA,TAT\}\) and \(\{CGC,GCG\}\) classes each repeated. Both are homopolymer-free including the required cyclic boundary. Thus both lower bounds are attained.

**Exact finite enumeration.** Number the \(18\) target classes by the lexicographically smaller element under the digital order \(A=0,C=1,G=2,T=3\). They are indices \(0,\ldots,17\); the two repeatable classes are indices \(5\) and \(11\). For a fixed initial heterodimer \(s\) and current heterodimer \(v\), let \(F_s(v,M,d_5,d_{11})\) count completions, where \(M\) is the \(18\)-bit mask of classes already visited and each flag records whether that exceptional class has been visited a second time. Along each legal edge \(v\xrightarrow{abc}w\) of class \(j\), add

- \(F_s(w,M\cup\{j\},d_5,d_{11})\) when \(j\notin M\);
- \(F_s(w,M,1,d_{11})\) when \(j=5\in M\), \(d_5=0\), and the extra-repeat budget permits it;
- \(F_s(w,M,d_5,1)\) when \(j=11\in M\), \(d_{11}=0\), and the budget permits it.

All other transitions contribute zero. In the linear case the terminal value is \(1\) when \(M\) is full and \(d_5+d_{11}=1\), regardless of \(v\). In the circular case it is \(1\) only when \(M\) is full, \(d_5=d_{11}=1\), and \(v=s\). The total count begins at \((v,M,d_5,d_{11})=(s,\varnothing,0,0)\). As each recursive transition either adds a new class to the mask or consumes an as-yet-unspent repetition flag, this recurrence terminates and counts every admissible optimum exactly once by its edge sequence.

For linear words, exactly the four starts \(AT,CG,GC,TA\) give nonzero completions, with \(14{,}496\) each, totaling \(57{,}984\). For closed \(20\)-window paths, the four fixed dinucleotide starts each give \(28{,}992\), while the eight other starts each give \(21{,}744\), totaling \(289{,}920\) indexed cycles. Every such cycle has all \(18\) classes represented, so its least period cannot be a proper divisor of \(20\), since any smaller period would have at most \(10\) different three-mer classes. Therefore each rotation orbit has exactly \(20\) members, and the quotient contains exactly \(289{,}920/20=14{,}496\) cycles. The \(28{,}992\)-per-class linear split also follows from the linear terminal profile and the two complement-pair symmetries.

**Closing-and-cutting correspondence.** In every shortest linear path, the two remaining odd quotient vertices are either \(AT,TA\) or \(CG,GC\). Since these fixed dinucleotides are the actual start and end vertices, they are joined in the required closing direction by exactly one oriented three-mer, respectively `ATA`/`TAT` or `CGC`/`GCG`. Adding this unique closing window turns the linear optimum into a shortest circular optimum. Conversely every shortest circle has exactly four occurrences belonging to the two twice-visited classes; cutting away any one of these four windows leaves a shortest linear host, and all four cuts are distinct because the circle is primitive. This gives an additional exact check \(57{,}984=4\cdot14{,}496\).

The second, independently written exhaustive verifier directly traverses every feasible class-capped directed trail through length \(20\), without memoization or the recursive completion-count table, reproducing the same numbers. The parity arguments show that its restrictions on repeatable classes exclude **no** optimal host.

## Verification

From a directory containing the supplied programs, run:

```sh
python3 verify_dp.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_dfs.cpp -o verify_dfs
./verify_dfs
```

The Python program constructs all allowed edges, reverse-complement classes and the parity certificate; performs exact integer memoized dynamic programming; verifies both witnesses and all root-class counts. It reports `DP_VERIFY_OK` with linear count \(57{,}984\), rooted circular count \(289{,}920\), and rotational count \(14{,}496\). The independent C++ program rebuilds the graph and directly explores \(3{,}221{,}436\) finite trail states without memoization, confirms no \(18\)-window perfect cover, and reproduces the same two optimal counts, reporting `DFS_VERIFY_OK`.

No external numerical solver, floating-point arithmetic, or unverifiable precomputed certificate is needed. The exhaustive enumeration proves only the specified finite four-letter instance; the lower bounds additionally have a conceptual parity proof. The source files themselves, not merely their reported outputs, are required for reproduction.

## Relationship to prior work

Orenstein and Shamir (2013) construct shortest reverse-complement-complete DNA sequences for **all** three-mers on the unrestricted four-letter alphabet. They prove that for odd window length the orbit-count lower bound can be achieved in the unrestricted graph. That theorem does not imply the analogous conclusion after forbidding every adjacent identical pair: the restricted graph has four odd quotient vertices and **cannot** attain its \(18\)-class lower bound. Their enumeration question concerns optimal sequences more generally, but their Table 1 and constructions do not enumerate these constrained \(21\)-letter linear words or \(20\)-letter circles.

Burris, Motta and Shipman (2016) develop an undirected quotient-graph and Euler-parity method for *reversal*, without Watson–Crick complementation or the no-homopolymer target restriction. The general graph principle is acknowledged, but their classification neither states nor implies the specific constrained reverse-complement parity pattern and count of optimal DNA hosts.

The nearest indexed related computational results consider shortest *dinucleotide* reverse-complement covering cycles (\(544\) rotationally distinct, with the full unrestricted dinucleotide target space), unrestricted covers of reverse-complement palindromic four-mers, or covers forbidding repeated runs of one **distinguished** letter while requiring every permitted oriented window. None has the same three-mer orbit set and simultaneous prohibition on all homopolymers. Thus neither the exact lengths nor the equality counts are entailed by those statements. The original scientific priority of possible unindexed earlier small-alphabet computations remains open for external audit.

## Limitations

The constraint is a mathematical hard prohibition of every adjacent identical base, not a claim that homopolymers of length two are biologically unacceptable. Circular words are counted only modulo rotation, not modulo reverse complement or complement-preserving relabeling. The enumeration is exact only for four labeled nucleotides and three-mer windows, and offers no all-alphabet or higher-order counting formula. The quotient-degree argument proves lower bounds and necessary multiplicities; equality counts require the finite exhaustive completion recurrence. Search-index coverage and inaccessible historical calculations limit literature-priority assurance. No independent mathematical audit has been performed.

## References

1. Y. Orenstein and R. Shamir, *Design of shortest double-stranded DNA sequences covering all k-mers with applications to protein-binding microarrays and synthetic enhancers*, **Bioinformatics** 29(13), i71–i79 (first published 19 June 2013). https://doi.org/10.1093/bioinformatics/btt230 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3694677/
2. C. S. Burris, F. C. Motta, P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences* (first public version 30 August 2016). https://arxiv.org/abs/1608.08480
3. Related published restricted-language covering and reverse-complement census records were compared at the statement level; their different target sets and objective conditions are described in the preceding section.
