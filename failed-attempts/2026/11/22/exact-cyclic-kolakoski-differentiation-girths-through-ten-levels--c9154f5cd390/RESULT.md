# Exact cyclic Kolakoski differentiation girths through ten levels

## Finding

For \(k\ge 0\), let \(X_k\subset\{1,2\}^{\mathbb Z}\) consist of the bi-infinite sequences for which \(k\) successive run-length differentiations are defined, with all intermediate maximal constant-symbol runs having lengths in \(\{1,2\}\). (Here \(X_0\) is the full binary shift.) Write \(g_k\) for the least shift period of a point of \(X_k\). Then the following exact finite-stage classification holds:

| \(k\) | Primitive cycles of exact differentiation height \(k\) | \(g_k\) | Cycles of exact height \(k\) attaining \(g_k\) |
|---:|---:|---:|---:|
|0|2|1|2|
|1|2|2|1|
|2|4|3|2|
|3|6|8|1|
|4|8|12|2|
|5|14|18|4|
|6|24|27|8|
|7|30|80|4|
|8|52|120|8|
|9|78|180|16|
|10|128|269|16|

In particular, six levels admit a period-\(27\) point but seven levels require period at least \(80\). The complete cyclic length spectra at levels six and seven are, respectively,

\[\begin{aligned}
L_6&=\{27:8,63:8,66:2,69:2,116:2,118:2\},\\
L_7&=\{80:4,82:4,99:4,174:4,177:4,188:4,190:4,204:1,210:1\}.
\end{aligned}\]

Here a notation such as \(27:8\) means eight primitive cyclic classes of least period \(27\) and exact differentiation height six. All period values and counts count orbits up to cyclic rotation, not labeled orbits.

## Assumptions and scope

For a nonconstant primitive cyclic word \(w\) of least period \(n\), cyclic differentiation \(D(w)\) records the successive lengths of its maximal runs, reading the cyclic word at a run boundary, and then chooses the primitive cyclic representative. The derivative exists if every run length is \(1\) or \(2\). Constant cyclic words have no derivative. Cyclic rotation of a word does not affect its derivative's cyclic class. Let \(S_k\) be the finite set of primitive cyclic word classes of *exact* height \(k\), where height is the number of defined derivative steps before the next derivative is undefined. Thus \(S_0=\{[1],[2]\}\). Every periodic point of \(X_k\) has height at least \(k\).

For arbitrary bi-infinite aperiodic sequences, the usual run-length derivative is defined by maximal runs; the theorem only counts periodic points of the nested finite-level systems. The term 'finite-level approximant' does not imply a finite-state presentation is used in the computation.

## Proof

**Strict descent.** If a nonconstant primitive cyclic word \(w\) has a defined derivative, its period is strictly shorter than that of \(w\), because a run consists of at least one symbol and a cyclic nonconstant binary word cannot have every run of length one without its derivative becoming constant. More explicitly, if all runs have length one, \(w\) is alternating, its derivative is the constant cyclic word \([1]\) and the period drops from two to one. Otherwise at least one run has length two, so the number of runs is less than the period of \(w\). Thus any periodic word has finite height.

**Exhaustive inverse lemma.** Let \(v\) be a primitive cyclic word of length \(m\), and suppose \(D(w)=[v]\). The runs of \(w\) necessarily alternate letters \(1,2\). Hence the total number of runs in one primitive period of \(w\) is even. The shortest even number of runs carrying the primitive periodic length sequence \(v\) equals \(m\) if \(m\) is even and \(2m\) if \(m\) is odd. There is no freedom other than choosing the first run symbol, up to cyclic rotation, so construct precisely two candidates by alternating run symbols beginning with \(1\) or \(2\), with the run-length list \(v\) (if \(m\) is even) or \(vv\) (if \(m\) is odd). Reduce to least period and canonical cyclic rotation. Conversely these candidates have cyclic derivative \([v]\). Thus the set of distinct normalized candidates is exactly the full fiber of \(D\) over \([v]\).

**Induction and minimum.** Consequently, starting from \(S_0=\{[1],[2]\}\), the complete exact-height sets obey
\[S_{k+1}=\bigcup_{v\in S_k}\{[I_1(v)],[I_2(v)]\},\]
where \(I_c(v)\) is the preceding run-expansion with first run symbol \(c\), and union removes duplicate cyclic classes. A periodic point of height at least \(k\) has a derivative at exact height \(k\), whose period is strictly smaller under each nonterminal derivative step. It follows that \(g_k=\min\{|w|:w\in S_k\}\); no higher-height word can yield a shorter period. The exhaustive finite recurrence therefore proves every entry in the table, not just existence.

**The depth-six-to-seven threshold.** The exact length multiset of \(S_6\) has eight classes of length \(27\), eight of length \(63\), two of length \(66\), and the remaining eight at lengths \(69,116,118\). Each primitive word of odd length \(27\) requires two consecutive copies of its length list in a cyclic antiderivative. The eight length-\(27\) words yield four distinct length-\(80\) expansions and four distinct length-\(82\) expansions (the digits \(2\) occur \(13\) or \(14\) times). Every length-\(63\) expansion has length at least \(126\), while even length-\(66\) yields length \(99\); the remaining classes yield no shorter expansions. This certifies \(g_7=80\) with four extremal cycles. The same complete recurrence gives the further entries through depth ten.

## Verification

`verify_cyclic_girth.py` and `verify_cyclic_girth.cpp` independently construct and cyclically normalize every primitive inverse at levels zero through ten, assert all class counts, shortest periods and minimizer multiplicities, and check each computed inverse under cyclic differentiation. The C++ executable additionally exhaustively examines every primitive binary word of periods \(1\) through \(18\) without using the inverse enumeration, confirming the initial lower bounds. `level_statistics.csv` lists every exact-height length multiplicity at each level, not a truncated sample. The reproducible commands are:

```sh
python3 verify_cyclic_girth.py
g++ -O2 -std=c++17 verify_cyclic_girth.cpp -o verify_cyclic_girth
./verify_cyclic_girth
```

The general inverse lemma and strict descent establish exhaustiveness; finite tests are not used as proofs of any unbounded assertion.

## Relationship to prior work

Mitchell, Walton, and Whittaker (2026) establish transitivity of the *infinitely* differentiable Kolakoski shift. Cassaigne and Henry (2026) analyze factor complexity and finite-word derivatives, including the shortest lengths of bispecial smooth **finite** words. The present invariant instead counts primitive **periodic bilateral** points surviving a prescribed number of run-length derivatives. A shortest bispecial finite-word length is not a shortest periodic-orbit period, and transitivity of the infinite system supplies neither the finite-stage girths nor their exact cyclic multiplicities. The nonperiodicity of infinitely smooth sequences is previously known and not claimed as new.

## Limitations

The classification ends at level ten; no formula is asserted for later levels, nor for the growth rate of \(g_k\). It concerns alphabet \(\{1,2\}\), cyclic bilateral derivatives, and primitive cyclic orbits; it is not a classification of finite smooth-word factor complexity. Distinct periodic points in one orbit are counted once. Historical or unindexed descriptions of periodic finite-order smooth sequences may overlap; the novelty assessment is restricted to inspected evidence. No independent mathematical audit has occurred.

## References

1. A. C. Mitchell, J. J. Walton, M. F. Whittaker, *The full Kolakoski shift is topologically transitive*, arXiv:2611.06878v1 (first submitted 2026-11-04), https://arxiv.org/abs/2611.06878.
2. J. Cassaigne, R. Henry, *The complexity of smooth words over binary alphabets*, arXiv:2603.10733 (first submitted March 2026; revised 2026-11-05), https://arxiv.org/html/2603.10733.
3. M. Zwierzyński, *Shuffle Squares in Differentiable Words*, arXiv:2610.07828 (2026-10-06), https://arxiv.org/abs/2610.07828.
