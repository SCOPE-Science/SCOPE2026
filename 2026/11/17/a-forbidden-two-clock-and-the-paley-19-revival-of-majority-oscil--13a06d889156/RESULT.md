# A forbidden two-clock and the Paley-19 revival of majority oscillations

## Finding
For any finite loopless **tournament** (one oriented arc between each pair of distinct vertices), synchronous binary out-neighbor majority with the incumbent opinion retained on a tie has **no primitive temporal two-cycle**. If the tournament is regular, its only fixed states are the two unanimous states.

For the quadratic-residue (Paley) tournaments \(T_p\) at the first four primes \(p\equiv3\pmod4\), the *complete* recurrent census is:

| \(p\) | Fixed states | Primitive period-3 orbits | Primitive period-4 orbits | Primitive period-7 orbits | Primitive period-19 orbits | Sharp maximum entry time |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 0 | 0 | 0 | 0 |
| 7 | 2 | 0 | 0 | 6 | 0 | 3 |
| 11 | 2 | 0 | 0 | 0 | 0 | 5 |
| 19 | 2 | 0 | 342 | 0 | 18 | 7 |

There are **no other periodic orbits** at these four orders. Thus, while every state of \(T_{11}\) reaches consensus, the next admissible prime order \(19\) has both primitive temporal four-cycles and nineteen-cycles. This is a dynamical period classification, not a count of directed graph-theoretic cycles.

On \(T_{19}\), the \(1368\) recurrent period-four configurations form **two** classes of \(684\) each, and the \(342\) recurrent period-nineteen configurations form **one** class, under the natural transformations of translation, multiplication by nonzero squares, global bit complement and temporal shift. Together with the two unanimous states, there are precisely **four** such classes of recurrent configurations. The two period-four representatives have integer state encodings \(3543\) and \(5751\); the period-nineteen representative has encoding \(511\).

## Assumptions and scope
For each \(p\in\{3,7,11,19\}\), identify vertices with \(\mathbb Z/p\mathbb Z\) and let \(Q_p\) be the set of nonzero quadratic residues modulo \(p\). Put an arc \(i\to j\) when \(j-i\in Q_p\). Since \(-1\notin Q_p\), this is a tournament, and it is regular of out-degree \((p-1)/2\). For an opinion vector \(x\in\{0,1\}^p\), define
\[
(F_p(x))_i=\begin{cases}1,&\displaystyle\sum_{q\in Q_p}x_{i+q}>(p-1)/4,\\0,&\text{otherwise.}\end{cases}
\]
Every out-degree here is odd, so no tie occurs in these four cases. For the universal tournament statements, an even out-degree tie is resolved by retaining the current bit. A configuration's **first periodic-entry time** is the least \(t\ge0\) such that \(F^{t+\ell}(x)=F^t(x)\) for some \(\ell\ge1\); the primitive temporal period is the least such positive \(\ell\). Configurations are labelled; temporal orbits identify their phases, but no spatial symmetries are imposed on the orbit counts in the table.

Encode \(x\) by \(\sum_{i=0}^{p-1}2^i x_i\), with vertex zero as the least significant bit. In particular, all \(2^{19}=524288\) possible nineteen-vertex states are covered.

## Proof
**No two-step clock on any tournament.** Suppose distinct states \(x,y\) satisfy \(F(x)=y\) and \(F(y)=x\). Let \(A=\{i:x_i=1,y_i=0\}\), \(B=\{i:x_i=0,y_i=1\}\) and write \(a=|A|\), \(b=|B|\). A changing vertex must have a *strict* local majority against its incumbent bit (a tie retains it). Consequently, for every \(i\in A\) the number of out-neighbors belonging to \(B\), minus those belonging to \(A\), is at least one; for every \(i\in B\) the reverse difference is at least one. Summing gives
\[
 e(A,B)+e(B,A)-e(A,A)-e(B,B)\ge a+b,
\]
where \(e(S,T)\) counts arcs from \(S\) to \(T\). In a tournament the left side equals
\[
 ab-\frac{a(a-1)}2-\frac{b(b-1)}2=\frac{a+b-(a-b)^2}{2}.
\]
Thus \(-(a-b)^2\ge a+b\), impossible because \(a+b>0\). This proves the global two-cycle exclusion, including tournaments of nonconstant out-degree.

**Only consensus is fixed on a regular tournament.** Suppose each vertex has out-degree \(k\), so the vertex count is \(2k+1\). Let a nonunanimous fixed configuration have \(s\) one-vertices and \(t\) zero-vertices. Each one-vertex needs at least \(\lceil k/2\rceil\) out-neighbors in its own opinion class, including the possibility of a retaining tie. Summing across that class and using the tournament identity \(e(S,S)=s(s-1)/2\) gives \(s\ge2\lceil k/2\rceil+1\). The same argument gives \(t\ge2\lceil k/2\rceil+1\). Hence \(s+t\ge4\lceil k/2\rceil+2>2k+1\), a contradiction.

**Exact finite census.** For the four specified prime orders, `verify_functional.py` explicitly enumerates each integer state in \([0,2^p)\). For every vertex it constructs the nine-, five-, three- or one-neighbor bit mask directly from the residue set and evaluates its strict-majority successor. It then traverses the entire functional graph, following every as-yet-unclassified path until it hits a previous state or an already-classified vertex. Since the map is deterministic on a *finite* set, this path-and-cycle decomposition assigns the correct least period and first entry time to every state, with no truncation or sampling. Its exact output is in `output_functional.json`.

A second implementation, `verify_iterates.c`, reconstructs updates independently from the residue lists by individual bit tests. It checks the global identities
\[
F_3^3=\mathrm{id},\qquad F_7^{10}=F_7^3,\qquad F_{11}^{6}=F_{11}^{5},\qquad F_{19}^{83}=F_{19}^{7}
\]
for *every* labelled state, and checks each indicated positive entry cutoff is sharp by finding a state for which the preceding identity fails. The final identity has exponent difference \(76=\operatorname{lcm}(4,19)\). Its independent period and entry-time counts match the full functional-graph enumeration.

**Geometric classes.** For each \(p\), the transformations \(i\mapsto i+1\) and \(i\mapsto ai\) for \(a\in Q_p\) preserve the tournament because \(aQ_p=Q_p\). Complement commutes with odd-degree majority, and time evolution permutes recurrent states. Breadth-first closure of these transformations and \(F_p\), restricted to the already certified recurrent configurations, gives the claimed exact geometric class sizes. The closure enumerates *all* members of each generated class, subtracts them, and repeats until no recurrent configuration remains.

## Verification
The two complete independent implementations reproduce the table. The period-resolved first-entry census for \(T_{19}\) is:

| Entry step | Period 1 | Period 4 | Period 19 |
|---:|---:|---:|---:|
| 0 | 2 | 1368 | 342 |
| 1 | 40280 | 2052 | 684 |
| 2 | 276374 | 1710 | 342 |
| 3 | 126350 | 1026 | 0 |
| 4 | 52554 | 0 | 0 |
| 5 | 14706 | 0 | 0 |
| 6 | 4446 | 0 | 0 |
| 7 | 2052 | 0 | 0 |

These counts sum to \(524288\). The associated basin totals are \(516764\) for consensus, \(6156\) for period four and \(1368\) for period nineteen. The two independent programs reproduce these values from different computational procedures. `verify_functional.py` requires only Python 3 standard modules; compile the independent program using `cc -std=c11 -O2 verify_iterates.c -o verify_iterates` and execute it. The recorded standard outputs are embedded. Exhaustion proves the stated finite cases, not claims for any other prime order.

## Relationship to prior work
Jørgensen [1, Section 1] identifies Paley tournaments as doubly regular tournaments, but its construction and spectral theory do not enumerate threshold-voting orbits. Benjamini, Chan, O'Donnell, Tamuz and Tan [2, Theorem 1.1] review the eventual period-at-most-two theorem for **undirected** finite majority dynamics; directed tournaments fall outside that hypothesis. General threshold-automata network dynamics was investigated earlier by Goles [3], including cycles, so the existence of longer cycles in asymmetric networks is not by itself presented as new. The exact sharp transient, full labelled orbit counts, and affine-complement-time classification for these Paley orders are the specific contributions here. Existing calculations of Paley tournament out-neighborhood topology and logical extension properties concern different invariants, not voting trajectories.

## Limitations
The census is proved only for \(p\in\{3,7,11,19\}\), not for all Paley tournaments or general doubly regular tournaments. No universal claim is made about the maximal temporal period as prime order grows. The proof of the universal two-cycle exclusion and fixed-point lemma is elementary; the mathematically motivated non-routine part is the complete small-Paley dynamical and symmetry classification. The original full text of Goles [3] was not accessible during the literature comparison, so earlier broader treatment of related dynamical restrictions remains a priority risk; its available abstract does not state these exact Paley counts. The computations have not undergone independent mathematical audit.

## References
[1] L. K. Jørgensen, *Normally Regular Digraphs*, arXiv:1410.8424v1, publicly posted 2014-10-30; see Section 1, including the Paley construction. https://arxiv.org/abs/1410.8424

[2] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, publicly posted 2014-05-11; see Theorem 1.1 and its undirected-graph hypothesis. https://arxiv.org/abs/1405.2486

[3] E. Goles Ch., *Dynamics of positive automata networks*, Theoretical Computer Science 41 (1985), 19–32, DOI:10.1016/0304-3975(85)90057-X. Abstract inspected; complete text not obtained.
