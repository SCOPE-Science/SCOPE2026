# Complete size spectrum of near-GC-balanced, strand-closed, substitution-detecting DNA five-mer synchronization codes

## Finding

Let \(\Sigma=\{A,C,G,T\}\), with Watson–Crick complement \(A\leftrightarrow T\), \(C\leftrightarrow G\). Consider the labeled codebooks \(C\subseteq\Sigma^5\) satisfying four conditions: (i) each codeword has two or three \(C/G\) symbols; (ii) \(\rho(C)=C\), where \(\rho\) is reverse complement; (iii) every nonempty proper prefix of any codeword differs from every same-length suffix of any codeword, including itself; and (iv) distinct codewords have aligned Hamming distance at least \(2\).

For the number \(c_j\) of such codebooks with exactly \(2j\) words, including the empty codebook, the complete cardinality enumerator is

\[
\boxed{\sum_{j\ge0}c_jz^j=1+104z+1068z^2+3472z^3+4648z^4+2776z^5+720z^6+56z^7.}
\]

Therefore the sharp maximum code size is \(14\) words. Exactly \(56\) labeled codebooks attain it, forming seven orbits of eight under the group of Watson–Crick-preserving nucleotide permutations. Including the empty code, there are \(12{,}845\) codebooks.

## Assumptions and scope

Write \(\rho(w_1\cdots w_5)=\overline{w_5}\cdots\overline{w_1}\), with \(\overline A=T\), \(\overline T=A\), \(\overline C=G\), and \(\overline G=C\). Non-overlap forbids prefix–suffix equality of lengths \(1,2,3,4\) for every ordered pair, even repeated words. The Hamming-distance requirement includes two distinct words from one reverse-complement pair. It detects one aligned substitution, not necessarily correcting it. The GC fractions \(2/5\) and \(3/5\) are the closest possible to one half for an odd-length word. Codebooks are unordered sets with letters labeled; the symmetry quotient is taken only after counting labeled maxima.

## Proof

**Exact orbit reduction.** There are \(2^5[\binom52+\binom53]=640\) eligible individual words by composition. No odd-length word is fixed by reverse complementation, since the middle letter cannot complement itself. Thus the universe consists of exactly \(320\) two-element orbits. Every permitted codebook is a union of these pairs. Requiring the two members of an orbit to meet the self-overlap, cross-overlap and distance-two conditions leaves precisely \(104\) eligible orbits, enumerated directly and exhaustively by `verify.py`.

**Graph equivalence.** Construct a graph \(G\) whose vertices are those \(104\) eligible orbits. Join two vertices if and only if every cross-orbit pair of words satisfies both oriented non-overlap conditions and aligned Hamming distance at least two. The graph has \(1068\) edges. The map from codebooks to selected reverse-complement orbits is a bijection from valid codebooks to cliques in \(G\). Indeed, internal constraints were checked for each vertex, and every remaining defining condition applies to individual pairs of words.

**Sharp upper bound and witness.** `certificate.json` assigns each vertex a color from \(\{0,1,\ldots,6\}\), with class sizes \((16,16,16,16,12,14,14)\). The verifier regenerates \(G\) from the word definitions and checks that every edge joins differently colored vertices. Any clique has at most seven vertices, giving at most \(14\) codewords. The seven orbit representatives

```text
AACAC AACCT AAGTC AATCC AGACC AGTTC GATAC
```

and their reverse complements are checked directly against all four conditions and give a code of \(14\) words. This proves sharpness by an independently checkable finite coloring certificate and a matching witness.

**Full exact enumeration.** For a subset \(S\) of vertices let \(F(S;z)\) enumerate cliques by size. Splitting into cliques excluding and including \(v\in S\) gives

\[
F(S;z)=F(S\setminus\{v\};z)+zF((S\setminus\{v\})\cap N(v);z),\qquad F(\varnothing;z)=1.
\]

The increasing-index recursion in `verify.py` implements this recurrence and visits each clique exactly once, as its unique increasing vertex sequence. The integer coefficients for sizes \(0\) through \(7\) are \((1,104,1068,3472,4648,2776,720,56)\), summing to \(12{,}845\). The seven-color proof independently excludes larger cliques. A separate all-clique enumeration based on a graph-library routine matched every coefficient during review; the included verifier needs no external library.

**Symmetry.** The group of permutations commuting with Watson–Crick complement chooses whether to exchange the two complementary nucleotide pairs and whether to flip the two members of either pair. It has order \(2^2\cdot2=8\). Exchanging the pairs interchanges GC counts \(2\) and \(3\), so every group element preserves the four conditions. Enumerating the images of all \(56\) maxima shows exactly seven disjoint group orbits, all with eight members, as asserted.

## Verification

In the directory containing `verify.py` and `certificate.json`, run:

```bash
python3 verify.py
```

The standard-library program regenerates all \(640\) balanced candidate words, their \(320\) complement pairs, the \(104\) allowed orbits and \(1068\) graph edges; checks the upper coloring and \(14\)-word witness directly; enumerates all codebooks exactly; and computes the maximum-orbit classification. It uses integer arithmetic and finite exhaustive recursion. The certificate is an explicit finite proof, not an inference from an incomplete computation or a timeout.

## Relationship to prior work

Levy and Yaakobi (2018, arXiv:1804.05371) study mutually uncorrelated codes with balanced and Hamming-distance constraints; Yazdi, Kiah, Gabrys and Milenkovic (2017, arXiv:1709.05214) study balanced error-correcting primer designs and general bounds. Neither full available 2017 text nor the accessible 2018 material supplies this finite combined enumeration. Stanovnik, Moškon and Mraz (2024, arXiv:2410.18458) characterize nearly balanced non-overlapping code constructions; their full accessible text neither imposes strand closure nor gives this substitution-detecting five-mer spectrum, and the conclusion explicitly calls for joint Hamming-distance studies.

Two particularly close published mathematical reports were compared in full. *Exact capacity of strand-invariant, GC-balanced, non-overlapping DNA five-mers* gives maximum \(24\) at exactly the same length, balance, closure and overlap restrictions **without imposing Hamming distance**. It yields only the nonsharp upper bound \(24\) for this problem. *The complete four-mer spectrum of reverse-complement-closed non-overlapping DNA codes detecting one substitution* imposes closure, non-overlap and distance two at **length four and without a GC restriction**, with reverse-complement-fixed words possible. Its size polynomial does not imply this five-mer result. The present claim is the exact five-mer intersection: a strict capacity decrease to \(14\), all \(12{,}845\) codebooks counted, and a complete seven-orbit equality classification.

## Limitations

This is an exact computer-assisted finite classification only at length five and for the precisely stated four conditions. It does not cover insertions/deletions, single-substitution correction, secondary-structure constraints, melting-temperature behavior, biochemical performance, or longer lengths. The included graph and coloring are fully regenerable, but independent mathematical audit and historical priority verification have not been performed. An unindexed table under equivalent terminology could alter the novelty assessment.

## References

1. L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, first posted 2024-10-24, arXiv:2410.18458, https://arxiv.org/abs/2410.18458 .
2. M. Levy and E. Yaakobi, *Mutually Uncorrelated Codes for DNA Storage*, first posted 2018-04-15, arXiv:1804.05371, https://arxiv.org/abs/1804.05371 .
3. S. M. H. Tabatabaei Yazdi, H. M. Kiah, R. Gabrys and O. Milenkovic, *Mutually Uncorrelated Primers for DNA-Based Data Storage*, first posted 2017-09-13, arXiv:1709.05214, https://arxiv.org/abs/1709.05214 .
4. *Exact capacity of strand-invariant, GC-balanced, non-overlapping DNA five-mers*, publicly archived report, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-capacity-of-strand-invariant-gc-balanced-non-overlapping-d--b39eb37f2435 .
5. *The complete four-mer spectrum of reverse-complement-closed non-overlapping DNA codes detecting one substitution*, publicly archived report, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-complete-four-mer-spectrum-of-reverse-complement-closed-non--4848b308e1f3 .
