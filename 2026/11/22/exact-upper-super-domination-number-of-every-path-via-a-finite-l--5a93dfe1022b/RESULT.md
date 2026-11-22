# Exact upper super-domination number of every path via a finite local certificate

## Finding

For every integer \(n\ge2\), the maximum cardinality \(\Gamma_{\mathrm{sp}}(P_n)\) of an inclusion-minimal super dominating set in the path on \(n\) vertices is

\[
\boxed{\Gamma_{\mathrm{sp}}(P_n)=\left\lfloor\frac{5n}{7}\right\rfloor.}
\]

Equivalently, the smallest cardinality of a maximal open-irredundant set is \(\operatorname{oir}(P_n)=\lceil2n/7\rceil\). The one-vertex path is exceptional: \(\Gamma_{\mathrm{sp}}(P_1)=1\). This determines both possible-value ambiguities left by the recently published path bounds. The lower bound is witnessed by an explicit seven-periodic family; the upper bound is proved by a finite, exact, reproducible potential certificate over **every** binary path word.

## Assumptions and scope

A super dominating set \(S\) satisfies: for each \(v\notin S\), some neighbor \(u\in S\) has \(N(u)\cap(V\setminus S)=\{v\}\). It is inclusion-minimal if no proper subset has this property. An open-irredundant set \(T\) satisfies: for each \(u\in T\), some neighbor \(v\notin T\) has \(N(v)\cap T=\{u\}\). The latter property is hereditary under taking subsets; hence maximality can be tested by trying to add each missing vertex individually. Complements exchange super dominating sets and open-irredundant sets, including their respective inclusion-minimal and inclusion-maximal families. All graphs here are simple undirected labelled paths; no probabilistic or asymptotic qualification is used.

## Proof

**1. Local criterion.** Encode \(T\subseteq V(P_n)\) by binary word \(b_1\cdots b_n\), with \(1\) for membership. Pad both ends with four sentinel symbols `#`, which represent nonexistent vertices. A selected vertex \(j\) has an external private-neighbor witness precisely when one adjacent position \(k\) contains \(0\), and the other neighbor \(2k-j\) of \(k\) either lies outside the path or contains \(0\). Define `private_witness(w,j)` for a nine-symbol window accordingly; it is exactly the predicate in the accompanying standalone program. For a window centered at a real vertex \(j\), define `valid_center(w)` as follows: if its central bit is \(1\), the central vertex has a private witness; if its central bit is \(0\), changing only it to \(1\) makes at least one selected vertex among offsets \(-2,-1,0,1,2\) lose every witness. Adding a vertex can only alter private-witness status within two graph edges of it. To evaluate those statuses needs only four graph edges on either side. Thus a word represents a maximal open-irredundant set **if and only if** `valid_center` holds at every real position in its four-sentinel-padded word. This proves the local criterion rather than assuming it from numerical testing.

**2. Universal lower bound on \(|T|\).** Construct a finite weighted directed automaton. A state contains the last at most eight symbols after an initial four sentinels and a counter in \(\{0,1,2\}\) recording the number of real bits so far, capped at two. Start in the state consisting of four initial sentinels and counter zero. Appending a real bit \(a\in\{0,1\}\) changes the counter and updates the eight-symbol suffix, but is permitted only if any newly completed nine-symbol window obeys `valid_center`. Give that edge exact integral weight \(7a-2\). A state with counter two may reach the terminal sink with edge weight zero exactly when appending four final sentinels satisfies all remaining local checks. Every admissible path from the start to the sink therefore corresponds to one maximal open-irredundant binary word with \(n\ge2\), and has weight \(7|T|-2n\). Conversely every such word yields an admissible start-to-sink path. No arbitrary length cutoff is involved.

The complete automaton, enumerated by breadth-first search from its specified initial state, has **232 nonsink states, 403 directed edges including 58 sink edges**, and one sink. Exact integer Bellman–Ford relaxation from the start stabilizes; the resulting distance labels \(d\) satisfy \(d(\mathrm{start})=0\), \(d(v)\le d(u)+w(u,v)\) for all 403 edges, and \(d(\mathrm{sink})=0\). These are explicit finite inequalities checked by `verify.py`; no uninspected solver or external data is used. Summing the inequalities along any start-to-sink path gives \(7|T|-2n\ge d(\mathrm{sink})-d(\mathrm{start})=0\). Thus \(|T|\ge\lceil 2n/7\rceil\), and \(|S|\le\lfloor5n/7\rfloor\) for every inclusion-minimal \(S\).

**3. Sharpness in all seven residue classes.** Let \(n=7q+r\), \(0\le r<7\), \(n\ge2\). The following binary word represents \(T\): repeat block `0010100` exactly \(q\) times, then use the tail indexed by \(r\):

| \(r\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| tail | empty | `1` | `01` | `001` | `0110` | `00110` | `001010` |

Its number of ones is exactly \(2q+\lceil2r/7\rceil=\lceil 2n/7\rceil\). For every residue class, direct nine-symbol local checking verifies all words with \(0\le q\le4\) and \(n\ge2\). This extends to **all** \(q\): when an additional seven-symbol block is inserted after three blocks, every interior length-nine factor is already a factor of the periodic block, while every factor touching either end is determined by at most eight symbols of that seven-periodic block and the fixed four-sentinel boundary or fixed tail. These factors have all appeared by \(q=3\) or \(q=4\), independently of further repetitions. `verify.py` explicitly compares their finite factor sets as well as checking the local criterion. Hence the displayed words are maximal open-irredundant for every admissible \(q,r\). Taking complements yields inclusion-minimal super dominating sets attaining \(\lfloor5n/7\rfloor\). Combined with Step 2, the theorem follows.

**4. The one-vertex boundary.** For \(P_1\), its sole vertex must be selected in any super dominating set, giving \(\Gamma_{\mathrm{sp}}(P_1)=1\).

## Verification

The standalone Python 3 checker `verify.py` uses only the standard library, creates the entire automaton from the nine-symbol definitions, independently checks its potential inequalities and shortest sink cost, and tests all \(2^n\) vertex subsets for each \(2\le n\le13\) using the original graph-theoretic definitions. Its finite sample is a cross-check, not a replacement for the all-order finite-state argument. It also verifies the seven residue-class construction and finite-factor periodicity. Replay with `python3 verify.py`. One actual execution reported:

```text
INDEPENDENT_DIRECT_GRAPH_CHECK_PASS n=2..13 cases= 16380
SEVEN_RESIDUE_CONSTRUCTION_PASS block=0010100 tails=1,01,001,0110,00110,001010
BELLMAN_FORD_CERTIFICATE_PASS states=233 edges=403 termination_edges=58 minimum_cost=0
VERIFY_OK
```

## Relationship to prior work

Avella-Alaminos, Lemańska and Zuazua, *Minimal super dominating sets of maximum cardinality*, first publicly posted November 17, 2026, explicitly formulate the upper super-domination invariant, give exact values through order 21 (their Table 1), and obtain a two-candidate bound for paths in Theorem 2.8. Their Propositions 2.6–2.7 do not specify one answer in every residue class at arbitrary order; the present exact formula selects the answer for all orders, and the finite-state potential supplies a distinct all-order certificate.

Cockayne, Favaron, Finbow and Mynhardt's 2008 study supplies a general characterization of maximal open irredundance, not an identified complete formula for these path values in the inspected material. A separately published full census of inclusion-minimal super dominating sets on **cycles** obtains a seven-periodic upper spectrum there, but cycle results do not give this path formula: the path has different boundary conditions, and the recent motivating paper only proves a one-sided cycle–path inequality. This calculation does not claim to introduce the underlying parameter or the prior cycle periodicity.

## Limitations

Only paths are classified; the number of extremal sets and the complete cardinality polynomial are not determined here. The finite potential computation is a reproducible exhaustive enumeration of a fixed state graph, not a hand listing of all its distance labels; one must run the attached checker to replay every inequality. Independent mathematical audit and exhaustive historical-priority certification have not been performed. Equivalence under alternative older irredundance terminology remains a residual literature risk.

## References

1. D. Avella-Alaminos, M. Lemańska, and R. Zuazua, *Minimal super dominating sets of maximum cardinality*, arXiv:2611.23464v1, first posted November 17, 2026; especially Theorem 2.8, Table 1 and Proposition 2.12. https://arxiv.org/abs/2611.23464v1
2. E. J. Cockayne, O. Favaron, S. Finbow, and C. M. Mynhardt, *Open irredundance and maximum degree in graphs*, *Discrete Mathematics* 308 (2008), 5358–5375, DOI:10.1016/j.disc.2007.10.002. https://doi.org/10.1016/j.disc.2007.10.002
3. *Inclusion-minimal super domination on cycles: a five-gap census and sharp seven-period upper spectrum* (published November 2026), mathematical record at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-inclusion-minimal-super-domination-on-cycles-a-five-gap-census-a--16bec2bc3654
