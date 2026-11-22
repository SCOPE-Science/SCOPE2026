# A sharp twelve-command reset threshold under a forbidden double zero

## Finding

Consider every complete deterministic automaton on the **labeled** state set \(Q=\{0,1,2,3\}\) with two **ordered**, distinguished input letters \(0\) and \(1\). The letter actions \(a,b:Q\to Q\) are arbitrary, with no accessibility, minimality, or strong-connectivity assumption. An input word is *admissible* when it contains no contiguous factor `00`. It is a *reset word* when it maps all four initial states to one final state. Write \(\ell(a,b)\) for the shortest admissible reset-word length, and \(\ell(a,b)=\infty\) when none exists.

**Theorem (complete four-state census).** Among the \(4^8=65,536\) ordered labeled automata, exactly \(46,096\) admit an admissible reset word. The distribution is:

| \(\ell\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) | \(7\) | \(8\) | \(9\) | \(10\) | \(11\) | \(12\) | \(\infty\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 2032 | 17088 | 15456 | 4992 | 3696 | 1056 | 984 | 312 | 288 | 72 | 96 | 24 | 19440 |

The sharp maximal **finite** length is \(12\), and its \(24\) automata form **one** orbit under simultaneous relabeling of the four states (letters remain distinguished). A representative, listing target states for inputs \(0,1,2,3\) in that order, is

\[
a=(3,2,1,2),\qquad b=(1,3,2,0).
\]

This representative is ordinarily synchronizing with shortest unrestricted reset word of length \(6\), yet its shortest admissible reset word has length \(12\). One such word is `011101101110`. Exactly \(5,424\) of the \(51,520\) ordinarily synchronizing four-state automata cease to be synchronizable when `00` is forbidden.

## Assumptions and scope

Every letter acts as a total transformation \(Q\to Q\). The two input letters are distinguished: exchanging \(a\) and \(b\) is **not** an allowed symmetry because the restriction forbids repeated uses of only the first letter. All \(256^2\) pairs of maps are included, including duplicate maps and nonminimal automata. A word is applied from left to right. No result for more than four states, more letters, or other forbidden factors is asserted.

## Proof

A subset \(S\subseteq Q\) denotes the set of possible current states after applying a common input word. Given a letter action \(c\), its image is \(c(S)=\{c(s):s\in S\}\). Start at \(S=Q\) and retain the last letter \(p\in\{0,1,\bot\}\). The start state is \((Q,\bot)\). From a state \((S,p)\), use input \(c\in\{0,1\}\), except when \(p=c=0\), to reach \((c(S),c)\). A singleton subset is accepting.

**Reachability lemma.** Paths of exactly \(t\) steps from the start are in correspondence with admissible words of length \(t\), with the subset coordinate equal to the precise image of \(Q\) under that word and the last-letter coordinate recording its final symbol. This follows by induction on \(t\), directly from the transition rule. Hence the shortest path to a singleton is exactly \(\ell(a,b)\). There are at most \(1+2(2^4-1)=31\) distinct nonempty-subset/last-letter states, so ordinary breadth-first search terminates and reports \(\infty\) exactly when no admissible reset word exists.

**Finite exhaustive step.** Each map on four labeled states is uniquely represented by four base-four digits, making \(256\) maps; their ordered pairs give \(65,536\) nonduplicated inputs. `verify.py` loops over every pair, computes the above shortest path, and increments exactly one histogram bin. A separate implementation propagates the reachable-subset families ending in each letter by exact length without using a visited-state breadth-first queue: if \(R_0(t),R_1(t)\) are the families at length \(t\), then

\[
R_0(t+1)=\{a(S):S\in R_1(t)\},\qquad
R_1(t+1)=\{b(S):S\in R_0(t)\cup R_1(t)\}.
\]

Both families start with images of \(Q\) under single letters. This second recurrence finds a singleton at the first feasible length, or detects a repeated ordered pair of families, which conclusively excludes all later singleton visits. The two algorithms agree for **all** \(65,536\) inputs and give the table. Running the unrestricted breadth-first search separately gives \(51,520\) ordinarily synchronizing inputs, so subtraction yields \(5,424\) lost cases.

Finally, the checker collects precisely the \(24\) inputs whose constrained threshold is \(12\). For each of the \(4!=24\) state permutations \(\pi\), it constructs the simultaneous conjugate \((\pi a\pi^{-1},\pi b\pi^{-1})\) of the displayed representative. These \(24\) conjugates are distinct and the computed collection equals them exactly, proving the unique-orbit assertion. The representative's word `011101101110` has no `00`; successive bitmask images of \(Q\), including the initial image, are

`15, 14, 13, 7, 14, 6, 12, 5, 10, 9, 3, 10, 4`.

The final mask `4` is a singleton. The exhaustive search excludes all shorter admissible reset words for the representative. This completes the finite classification. The program includes the full finite exhaustive certificate as executable source, not merely precomputed counts.

## Verification

From the same directory, run `python3 verify.py` using only the Python standard library. The script executes two algorithmically different exact checks on every transition table, verifies the entire histogram, independently checks ordinary synchronization, proves the extremizer set equals the \(24\) conjugates, and replays the explicit witness. Its expected success marker is `VERIFY_OK`. The verifier was executed on the packaged source before the claim was accepted. Every computation is over finite sets of four-bit masks; there are no random choices, floating-point calculations, or sampling cutoffs.

## Relationship to prior work

The classical subset-automaton method for shortest reset words appears in Kisielewicz, Kowalski and Szykuła, whose preprint was publicly posted on March 13, 2012. Their 2012 study computes ordinary unrestricted reset lengths, not the admissible-language distribution or the \(24\)-element extremal orbit above. The later account by Volkov treats synchronization constrained to a regular language as a separate problem and provides practical motivation; it does not give this finite forbidden-double-zero census. Hoffmann's work investigates the complexity of constrained synchronization for commutative automata and automata with simple idempotents. Its inspected introduction, main theorems and proof passages address those structural restrictions and do not report this all-four-state exact distribution. Related finite automaton classifications and unrestricted reset-word state-complexity results concern different predicates and cannot determine the table solely by their published totals.

## Limitations

This is a complete finite classification for four states, rather than an asymptotic or arbitrary-state theorem. The proof of the numerical census is computationally exhaustive with small-state, transparent graph-search invariants. Its originality assessment is based on inspected accessible texts, database queries and mathematical implication comparisons, not on an assertion that all earlier literature was searchable. The relevant portions of a later constrained-synchronization paper were inspected, but unnoticed equivalent finite tabulations elsewhere remain a possible priority risk. No independent human or external mathematical validation is claimed.

## References

1. A. Kisielewicz, J. Kowalski and M. Szykuła, *A Fast Algorithm Finding the Shortest Reset Words*, first arXiv submission March 13, 2012, https://arxiv.org/abs/1203.2822 .
2. A. Kisielewicz, J. Kowalski and M. Szykuła, *Computing the shortest reset words of synchronizing automata*, published online November 17, 2013, https://doi.org/10.1007/s10878-013-9682-0 .
3. M. V. Volkov, *Synchronization of finite automata*, Russian Mathematical Surveys 77 (2022), section 2.2 on regular constraints, https://www.mathnet.ru/eng/rm10005 .
4. S. Hoffmann, *Constrained Synchronization for Commutative Automata and Automata with Simple Idempotents*, first arXiv submission September 6, 2021, https://arxiv.org/abs/2109.02743 .
