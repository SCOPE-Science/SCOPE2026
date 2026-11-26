# Sharp six-symbol boundary synchronization cutoff for elementary cellular automata

## Finding

For an elementary binary cellular automaton with Wolfram rule number \(r\in\{0,\ldots,255\}\), let \(L(r)\) be the smallest length of an obtainable one-step output word that determines the **rightmost two input bits** uniquely, with \(L(r)=\infty\) if no such word exists. The exact distribution is

| \(L(r)\) | 1 | 2 | 3 | 4 | 5 | 6 | \(\infty\) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| Number of rules | 24 | 90 | 72 | 12 | 4 | 4 | 50 |

In particular, any elementary rule possessing a boundary-synchronizing output word has one of length at most six, and this bound is sharp: **exactly Rules 37, 91, 164 and 218** have shortest length six. Among these, words `100101` synchronize Rules 37 and 164, while `010010` synchronize Rules 91 and 218. Exactly 206 rules synchronize in this sense and 50 do not. The provided catalog specifies the minimum length, a shortest word, the number of reachable nonempty subsets and the number of shortest words for every rule.

## Assumptions and scope

Let \(f_r:\{0,1\}^3\to\{0,1\}\) denote the standard Wolfram local map,
\[
f_r(a,b,c)=\left\lfloor\frac{r}{2^{4a+2b+c}}\right\rfloor\bmod2.
\]
The corresponding one-step cellular automaton is \((F_rx)_i=f_r(x_i,x_{i+1},x_{i+2})\) on bi-infinite binary configurations (this is simply a shifted presentation of the usual radius-one convention). For a nonempty output word \(w\) of length \(n\), a finite predecessor is \(x_0\cdots x_{n+1}\) satisfying \(f_r(x_i,x_{i+1},x_{i+2})=w_i\) for every \(0\le i<n\). Call \(w\) *right-boundary synchronizing* when it has at least one such predecessor and **all** predecessors end in the same pair \((x_n,x_{n+1})\). Every finite predecessor extends to a bi-infinite configuration, so finite and global one-step predecessor interpretations agree for this question.

The theorem concerns the existence of at least one finite synchronizing word, not the frequency of such words, uniqueness of the full input, arbitrary multi-time observations, or the opposite left boundary. The opposite boundary generally has a different minimum for an individual unreflected rule.

## Proof

Let \(Q=\{00,01,10,11\}\) be the four states of the de Bruijn predecessor graph, representing adjacent input bits. A triple \(abc\) gives an edge \(ab\to bc\) labeled \(f_r(a,b,c)\). For a set \(S\subseteq Q\) and output bit \(d\in\{0,1\}\), define the exact forward-subset transition
\[
T_{r,d}(S)=\{bc:ab\in S,\ c\in\{0,1\},\ f_r(a,b,c)=d\}.
\]
Starting at \(S_0=Q\), apply these transitions along a word. Induction on the word length shows that the resulting subset consists **exactly** of the feasible final input pairs, since every graph path corresponds to an input word and vice versa. The word is right-boundary synchronizing if and only if the resulting subset is a singleton. Empty subsets represent impossible output words and cannot be witnesses.

The complete search is therefore a finite graph computation on the at most 15 nonempty subsets of \(Q\), beginning at \(Q\) and taking both labeled successors from every reached set. Breadth-first search returns the exact minimum word length leading to a singleton. If none occurs in this fully closed reachable graph, **no synchronizing word of any finite length exists**, because any later word follows the already examined state-transition graph. This is a finite exhaustion argument with no unbounded-search inference.

The attached standalone `verify.py` implements this closed-graph search using exact four-bit subset masks and performs it for every one of the 256 Wolfram rules. It checks that the complete length multiset is exactly \((24,90,72,12,4,4,50)\), and that the length-six list is exactly \((37,91,164,218)\). It verifies the exhibited length-six words. These finite, explicitly defined calculations establish the stated unrestricted classification by the preceding graph equivalence and closure theorem.

## Verification

Run `python verify.py --csv classification.csv` with Python 3 and no external dependencies. The verifier recomputes every row of the CSV and compares its bytes with the packaged catalog; it also compares all reachable-state transitions against a separately implemented direct enumeration of all input blocks for every output word of lengths one through six. The direct comparison covers 32,256 word/rule/length cases, and separately checks the shortest synchronizing length in each of the 256 rules. All successor sets in the visited-subset closure are checked. Successful exact execution reports `VERIFY_OK`.

The direct input-block enumeration by itself proves results only through length six. The global assertion, including all 50 impossible cases, comes instead from the complete reachable-subset closure on 15 possible nonempty states and the exact path-to-predecessor correspondence.

## Relationship to prior work

Kari (2002) studies synchronization and stability for **complete deterministic** graph colorings. Kisielewicz–Kowalski–Szykuła (2012) develop shortest-reset-word algorithms for deterministic finite automata. Those general frameworks motivate subset-search methods but do not themselves provide the 256-rule right-predecessor-boundary census: here each output letter induces a potentially **nondeterministic or partial** transition on a four-state de Bruijn graph. Fukś (2013) studies elementary cellular automata via local structure and block probability maps; Grigorchuk–Kogan–Vorobets (2021) study finite-state coding and images of Markov measures. These address related finite-state representations but not the exact boundary-synchronization spectrum classified here.

The result is also distinct from determining forbidden image words, image entropy, finite-ring bijectivity, or period inflation of periodic predecessors: those concern existence, language size, bijectivity or periodicity, rather than a single admissible output word forcing its terminal predecessor context.

## Limitations

This is a finite exact classification of the **one-step** 256-rule elementary family. It does not establish analogous cutoffs for larger alphabets, wider neighborhoods, arbitrary block codes or time iterates. The classification has been checked against available mathematical literature and relevant indexed results, but an equivalent older table in unindexed or inaccessible sources cannot be ruled out. No independent audit has been performed.

## References

1. J. Kari, “Synchronization and Stability of Finite Automata,” *Journal of Universal Computer Science* **8** (2002), 270–277. DOI: `10.3217/jucs-008-02-0270` (journal appearance 2002-02-28).
2. A. Kisielewicz, J. Kowalski and M. Szykuła, “A Fast Algorithm Finding the Shortest Reset Words,” arXiv:`1203.2822v1` (2012-03-13).
3. H. Fukś, “Construction of local structure maps for cellular automata,” arXiv:`1304.8035v1` (2013-04-30).
4. R. Grigorchuk, R. Kogan and Y. Vorobets, “On Mealy-Moore coding and images of Markov measures,” arXiv:`2102.05539v1` (2021).
