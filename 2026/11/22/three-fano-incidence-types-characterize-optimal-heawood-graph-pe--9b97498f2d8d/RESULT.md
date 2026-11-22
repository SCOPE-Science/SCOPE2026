# Three Fano incidence types characterize optimal Heawood graph pegging

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, the point–line incidence graph of the Fano plane. A *pegging distribution* is a vertex subset \(D\). A move removes pegs from distinct adjacent occupied vertices \(a,b\), and places a peg at an unoccupied vertex \(c\) adjacent to \(b\), where \(a\ne c\). A target vertex is *reachable* if some finite sequence of moves (possibly empty) results in a peg at that target. The required sequence may depend on the target. Write \(R(D)\) for the set of reachable targets and call \(D\) *universal* if \(R(D)=V(H)\).

**Theorem.** The minimum size of a universal distribution on \(H\) is four, and there are exactly 336 universal four-sets. They are precisely the subsets with two points and two lines whose induced point–line incidence graph is one of:

1. one edge and two isolated vertices (168 sets);
2. two independent edges (84 sets);
3. a four-vertex path (84 sets).

The family of inclusion-minimal universal distributions has exactly 770 members: all 336 universal four-sets and 434 additional five-sets. The five-sets form four full graph-automorphism orbits, of sizes 168, 168, 56, and 42. With \(P_i\) denoting the nonzero binary point vector \(i\) and \(L_j\) the line with normal \(j\), orbit representatives are:

| Orbit size | Representative |
|---:|---|
| 168 | \(\{P_1,P_2,P_3,P_4,L_1\}\) |
| 168 | \(\{P_1,P_2,P_3,P_5,L_1\}\) |
| 56 | \(\{P_1,P_2,P_4,P_6,L_1\}\) |
| 42 | \(\{P_3,P_4,P_7,L_1,L_2\}\) |

Exactly 140 five-sets are not universal: 56 are independent, and the remaining 84 consist of four points forming a Fano quadrangle together with a secant line, or the point–line dual. Here *quadrangle* means four points with no collinear triple, and *secant* means a line incident to exactly two of them. For six or seven pegs, the only nonuniversal distributions are independent sets: respectively 14 and 2. Hence every eight-peg distribution is universal, and the pegging number is eight.

In full, if \(u_k\) counts universal size-\(k\) distributions, then

\[
\sum_{k=0}^{14}u_k z^k=336z^4+1862z^5+2989z^6+3430z^7+3003z^8+2002z^9+1001z^{10}+364z^{11}+91z^{12}+14z^{13}+z^{14}.
\]

## Assumptions and scope

The graph is fixed and labelled as follows. Points \(P_1,\ldots,P_7\) are the nonzero vectors of \(\mathbb F_2^3\), encoded by integers 1 through 7. Lines \(L_1,\ldots,L_7\) are the nonzero normal vectors, with \(P_i\) incident to \(L_j\) exactly when their binary dot product is zero. Thus \(H\) has fourteen vertices, twenty-one edges, degree three and girth six. The two vertex sorts may be interchanged by duality. This model uniquely specifies every labelled configuration used above.

Every move consumes precisely one peg; a target need not be the sole surviving peg. The result uses the nonreversible Helleloid–Khalid–Moulton–Wood graph-pegging rule, not the alternative terminal-one-peg formulation of peg solitaire and not graph pebbling with multiple pebbles at the same vertex. All counting is over distinct labelled subsets unless explicitly grouped into symmetry orbits.

## Proof

**1. Exact finite recurrence.** For every bitmask \(D\subseteq V(H)\), define

\[
R(D)=D\cup \bigcup_{(a,b,c)\text{ a legal move from }D}
R\big((D\setminus\{a,b\})\cup\{c\}\big).
\]

This is a well-founded recurrence because each successor has one fewer peg. The base case for distributions with no legal move is \(R(D)=D\). Induction on \(|D|\) proves the recurrence includes *all and only* reachable targets: any nonempty valid move sequence starts with a legal triple, and any target reachable after that move appears in the corresponding successor. The graph definition gives exactly 84 oriented triples \((a,b,c)\) with \(a,b\) and \(b,c\) adjacent and \(a\ne c\). Thus all 16,384 state values can be calculated exactly with fourteen-bit integer operations, without sampling or heuristic stopping.

The result of this exact recurrence, independently reconstructed by the supplied Python and C++17 programs, is the coefficient vector

\[
(u_0,u_1,\ldots,u_{14})=(0,0,0,0,336,1862,2989,3430,3003,2002,1001,364,91,14,1).
\]

The four-peg threshold follows from the first nonzero entry. A universal set of size \(k\) is inclusion-minimal exactly when deleting each of its \(k\) vertices destroys universality. Applying this criterion to all states yields 336 minimal four-sets, 434 minimal five-sets, and none at any other size.

**2. Symmetry reduction and the four-peg criterion.** Each invertible binary linear map \(A\in\mathrm{GL}(3,2)\) acts on points by \(x\mapsto Ax\) and on line normals by \(n\mapsto A^{-T}n\). Each preserves the incidence relation; swapping points and lines gives another automorphism. There are \((2^3-1)(2^3-2)(2^3-2^2)=168\) linear maps and 336 maps after adjoining duality. These are all automorphisms: every automorphism must either preserve or swap the unique connected bipartition, and a bipartition-preserving automorphism is a collineation of the seven-point Fano plane.

The explicit group permutations generated by the Python certificate partition the 1,001 four-sets into twelve orbits. Evaluating the exact recurrence on an orbit representative and transporting the result under the group identifies exactly three universal orbits. All are balanced point–line sets and have respective edge patterns \(K_2\sqcup 2K_1\), \(2K_2\), and \(P_4\), with orbit sizes 168, 84, and 84. The only other balanced patterns are zero incidences or two incidences sharing an endpoint; both fail. Every unbalanced four-set also fails. This proves the stated geometric iff criterion independently of any orbit-name conventions. The certificate additionally checks this criterion directly against every labelled four-set.

**3. Five-peg failures and irredundant successes.** Applying the same recurrence to all 2,002 five-sets yields 1,862 universal and 140 nonuniversal. Testing Fano collinearity (three nonzero binary point vectors are collinear iff their XOR is zero) and duality identifies the 140 failed sets exactly as the 56 independent five-sets and 84 quadrangle-plus-secant sets. The latter consist of 42 configurations with four points and one line and 42 duals: there are seven point quadrangles and six secants of each. Of the 1,862 universal five-sets, precisely 434 contain no universal four-subset. The 336 automorphisms partition these 434 sets into four orbits of sizes 168, 168, 56, 42, with the labelled representatives stated above.

**4. Larger distributions and pegging number.** Exact recurrence values show the only failed six-sets are 14 independent sets and the only failed seven-sets are the two bipartition classes. For eight pegs every set reaches all targets. Conversely the two seven-vertex bipartition classes have no legal move, so no smaller uniform bound can suffice. Consequently the pegging number is eight. The well-known monotonicity of pegging reach under added pegs (also directly testable from the state table) ensures that an inclusion-minimal universal set cannot first appear after size five; this is independently checked by deletion tests on all states.

## Verification

Three standalone source files accompany this result. `verify_fano_pegging.py` constructs the binary incidence graph, computes recursive exact reach for all subsets, constructs the 336 collineation/duality automorphisms, checks every orbit and the geometric criteria, and tests every inclusion-minimal distribution. `verify_fano_pegging.cpp` uses a separately written bottom-up cardinality-ordered reach computation and independently checks the coefficient vector, minimal counts, and all four-set geometry. `verify_peg_bfs.py` does not use the recurrence: it performs direct forward state exploration from each of the 1,001 four-sets and 2,002 five-sets, checking the 336 and 434 counts and their irredundancy. All three were executed successfully with their package versions before review.

Reproduction commands from a directory containing the three source files:

```sh
python3 verify_fano_pegging.py
c++ -O2 -std=c++17 verify_fano_pegging.cpp -o verify_fano_pegging
./verify_fano_pegging
python3 verify_peg_bfs.py
```

Every assertion must succeed and each program prints `PASS`. These checks are finite, complete for the stated fourteen-vertex graph, and depend only on the mathematical graph definition and the move rule. They are not a proof about larger incidence graphs.

## Relationship to prior work

Helleloid, Khalid, Moulton and Wood (2008) introduced the graph-pegging numbers and proved general bounds and monotonicity of reach. Their arXiv full text, including the move definition and its small-diameter section, was inspected. Its results do not provide this Heawood-specific set census or Fano orbit description. The distinguished Heawood graph has diameter three, and the paper's diameter-two examples do not directly settle the present counts.

Beeler and Gray (2013) study *freely solvable peg solitaire* beginning with pegs on all but one vertex and aiming to leave one peg. Engbers and Stocker (2014) investigate the reversible version of that terminal-one-peg game. Both have a different initial-condition/target quantifier from the universal reachability studied here and do not imply the stated four- and five-peg classifications. Likewise graph pebbling permits multiple pebbles on one vertex and moves two from a single site, so related Heawood pebbling results are not interchangeable. Relevant published mathematical records were checked for aliases, numbers and equivalent formulations; absence of an indexed matching result is not a proof of historical priority.

## Limitations

This is a finite, self-contained, computer-assisted exact enumeration and Fano-symmetry classification, not an asymptotic statement for higher-order projective planes. The analysis distinguishes independent target reachability from one path visiting all targets or a peg-solitaire terminal state. Previous unindexed computations, unpublished notes or inaccessible results could contain overlap; independent mathematical audit and priority certification have not been performed.

## References

1. G. Helleloid, M. Khalid, D. P. Moulton, P. M. Wood, *Graph pegging numbers* (first public arXiv version April 7, 2008), https://arxiv.org/abs/0804.1095, https://doi.org/10.1016/j.disc.2008.03.029.
2. R. A. Beeler and A. D. Gray, *Freely Solvable Graphs in Peg Solitaire* (2013), https://doi.org/10.1155/2013/605279.
3. J. Engbers and C. Stocker, *Reversible peg solitaire on graphs* (first public arXiv version October 14, 2014), https://arxiv.org/abs/1410.3796.
4. *MSC2020 Mathematics Subject Classification*, entry 05C57: Games on graphs, https://mathscinet.ams.org/msc/msc2020.html?t=05-08.
