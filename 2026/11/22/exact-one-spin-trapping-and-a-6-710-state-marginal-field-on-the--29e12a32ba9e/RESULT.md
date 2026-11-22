# Exact one-spin trapping and a 6,710-state marginal field on the Ising dodecahedron

## Finding

On the twenty-vertex dodecahedral graph \(D=GP(10,2)\), put classical spins \(\sigma_v\in\{-1,+1\}\) and the homogeneous antiferromagnetic Hamiltonian
\[
\mathcal H_h(\sigma)=J\sum_{uv\in E(D)}\sigma_u\sigma_v-h\sum_{v\in V(D)}\sigma_v,
\qquad J>0,\quad h\geq0.
\]
A configuration is **strictly one-spin stable** when reversing any single spin *strictly increases* its energy; it is **weakly one-spin stable** if no reversal strictly decreases energy. Under ordinary zero-temperature single-spin Glauber dynamics, precisely the strict configurations are absorbing because a zero-energy flip is allowed.

Writing \(x=h/J\), the complete labelled-configuration census is:

| Field | Strictly stable configurations | Weakly stable configurations | Ground configurations | Strict excited traps |
| --- | ---: | ---: | ---: | ---: |
| \(x=0\) | 250 | 250 | 250 | 0 |
| \(0<x<1\) | 250 | 250 | 5 | 245 |
| \(x=1\) | 5 | 6710 | 5 | 0 |
| \(1<x<3\) | 295 | 295 | 5 | 290 |
| \(x=3\) | 0 | 5828 | 5828 | 0 |
| \(x>3\) | 1 | 1 | 1 | 0 |

There is **no equilibrium ground-state change at \(x=1\)**: the five positive-field ground configurations are the same throughout \(0<x<3\). Nevertheless the strictly absorbing landscape changes there, and exactly 6710 configurations are marginally stable at \(x=1\).

The strict states for \(0\leq x<1\) are **exactly the 250 zero-field ground states**, with magnetizations \(-4,0,4\) and multiplicities \(5,240,5\). In the upper interval \(1<x<3\), the down-spin set is exactly a maximal independent set of \(D\). Its possible sizes \(6,7,8\) have respective multiplicities \(10,280,5\). At \(x=3\), the 5828 weakly stable states are precisely all independent down-spin sets. This latter independence-set total, like the zero-field ground count and five-state plateau, is established equilibrium combinatorics rather than asserted as new. The new conclusion is the complete strict/weak single-spin landscape, its structural correspondence, and the interior-field marginal spike.

## Assumptions and scope

Label the vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with the thirty edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), using indices modulo ten. Each spin is exactly \(+1\) or \(-1\). The graph is finite, undirected, and has twelve pentagonal faces and degree three at every vertex. The ratio \(x=h/J\) ranges over **all real** nonnegative values; the two integer field thresholds are handled separately. Configurations are counted with vertex labels, not modulo graph automorphisms. Strict stability means an energy increase under **all** one-spin flips, not stability against two-spin or multi-spin moves.

## Proof

**Local-flip criterion.** Set \(N_i=\sum_{j\sim i}\sigma_j\in\{-3,-1,1,3\}\). The exact energy cost to flip site \(i\) is
\[
\Delta_i\mathcal H=2\sigma_i(h-JN_i).
\]
Thus it is enough to check the field chambers separated by \(x=1\) and \(x=3\) and the two equality points. All inequalities below follow directly from this formula.

**Every low-field strict state is a zero-field ground state.** If \(0\leq x<1\), strict stability means each site has at most one neighbor of the same spin. Hence the set of aligned (frustrated) edges is a matching. On every pentagonal face the number of aligned edges must be odd because the product of the five edge spin products equals one. Since a matching uses at most two edges of a pentagon, there is exactly one aligned edge on each face. Every edge belongs to two faces, so precisely six of the thirty edges are aligned. The exchange energy is therefore \(-18J\). Conversely, every configuration attaining the face-frustration lower bound \(-18J\) has exactly one aligned edge on each face, and two aligned edges sharing a vertex would lie on a common face. Thus its aligned edges form a matching and it is strict for \(0\leq x<1\).

The twelve faces form the vertices of the dual icosahedral graph. Choosing exactly one aligned primal edge on every face is equivalent to choosing a perfect matching of the dual. Every such matching determines globally consistent primal spin agreements: each pentagonal boundary has four disagreements, an even number, and facial cycles generate the planar cycle space. The assignment is unique up to global spin reversal. A finite perfect-matching recursion on the explicit twelve-face dual yields exactly 125 matchings; hence there are \(250\) low-field strict configurations. The accompanying face-dual verifier independently reconstructs all matchings and the magnetization multiplicities \(5,240,5\).

**Ground states throughout the positive plateau.** Let \(A\) be the down-spin set, let \(k=|A|\), and let \(e(A)\) count edges with both endpoints in \(A\). Since \(D\) is cubic, the exact energy is
\[
\mathcal H_h=30J-20h-6Jk+4Je(A)+2hk.
\]
The maximum independent-set cardinality is exactly eight, with five size-eight sets, as proved by complete recursion over the explicit graph in `verify_structural.py`. Relative to any such eight-set, for \(k\leq8\) the energy difference is
\[
2J(3-x)(8-k)+4Je(A)\geq0 \qquad (0<x<3),
\]
with equality only for an independent eight-set. For \(k>8\), compare the exchange energy with the universal pentagonal-face bound \(-18J\). The magnetization is smaller than four, so for every \(h>0\) this state has strictly greater total energy than the eight-set. Thus exactly five configurations minimize the energy for all \(0<x<3\). At \(x=0\) the preceding face argument gives 250 ground states. At \(x=3\), the energy above the fully positive configuration is \(4Je(A)\), and so **all** independent sets are ground states. For \(x>3\) the difference is \(2J(x-3)k+4Je(A)\), which is positive whenever \(k>0\); the fully positive state is unique.

**The upper-field absorbing states and the marginal field.** For \(1<x<3\), a down spin is strict if and only if all three neighbors are up, while an up spin is strict if and only if at least one neighbor is down. Therefore \(A\) must be independent and dominating, equivalently a maximal independent set. An exact include/exclude recursion on the twenty-vertex graph enumerates these sets: \(10\) of size six, \(280\) of size seven, and \(5\) of size eight, totaling \(295\). Since only five are ground, exactly \(290\) are excited strict traps.

At \(x=1\), strict stability requires \(A\) independent and every up vertex to have at least two neighbors in \(A\). Counting crossing edges gives \(3k\geq2(20-k)\), hence \(k\geq8\). Since the independence number is eight, only the five independent eight-sets can qualify; the exact graph recursion verifies that each does. Weak stability instead says that the induced subgraph on \(A\) has maximum degree at most one **and** every up vertex has a down neighbor. A separate constrained-subset recursion counts exactly \(6710\) such sets. At \(x=3\), weak stability is equivalent to independence, giving \(5828\) subsets; no configuration is strict, because every down spin has a zero-or-negative flip cost and the all-up state has a zero-cost flip. For \(x>3\), every down spin can lower the energy by flipping, so only the all-up configuration is strict. Since every neighbor sum is odd, zero-energy flips occur only at \(x=1\) or \(x=3\); thus the strict and weak counts agree on every open field chamber.

## Verification

The two included, dependency-free Python 3 programs check different finite claims with exact integers. Run:

```bash
python3 verify_bruteforce.py
python3 verify_structural.py
```

`verify_bruteforce.py` examines **every integer spin mask from 0 through \(2^{20}-1\)**, calculating every site's flip cost and all sampled chamber/threshold ground energies exactly. `verify_structural.py` does **not** use the energy scan: it constructs the twelve pentagonal faces and their dual, generates each perfect matching and its compatible spins, enumerates independent and maximal independent vertex sets by recursive branching, and counts field-one weak states by constrained dissociation/dominating-set branching. Both passed and yield the same table. The locality of the flip criterion proves that representative rational field values suffice for all open real intervals, while the critical equalities are checked separately. The analytic face argument and field inequalities extend the finite enumerations to the stated continuous field domain; no simulation or extrapolation is used.

## Relationship to prior work

Strečka, Karľová and Madaras (2015) exactly establish the *equilibrium* regular-Ising-polyhedron magnetization curve. Their dodecahedral Table 5 gives the five ground configurations throughout \(0<h/J<3\), the zero-field 250-state ground manifold, and enumerates independent sets by size. Those counts and the saturation field are not presented here as new. Their equilibrium energy/magnetization tables do not determine whether a configuration can lower its energy by flipping an individual site, nor the critical-field number of nonabsorbing weakly stable configurations. Konstantinidis's dodecahedron analysis (first posted 2023) traces magnetization jumps at the Ising limit, but the inspected ground-state analysis does not classify local one-spin traps. Spirin, Krapivsky and Redner (2001) analyze zero-temperature *ferromagnetic* lattice freezing and give the appropriate kinetic context; their model and geometry are different.

Also compared were published results on the dodecahedral independence complex and on dodecahedral competing-interaction and spin-one equilibrium classifications. The independence-complex result includes the previously known total of 5828 independent sets; it does not provide the all-field strict/weak kinetic classification, the low-field no-excited-trap-at-zero-field mechanism, or the 6710-state marginal count. No claim of absolute historical priority follows solely from these searches.

## Limitations

The classification concerns **one-spin** stability of the exactly specified finite classical antiferromagnet. It does not give Glauber absorption probabilities from random initial states, escape barriers, finite-temperature lifetimes, multispin stability, or the behavior of larger fullerene families. At the critical fields weakly stable configurations can still move by zero-energy flips, so their number must not be interpreted as an absorbing-state count. The published 2015 equilibrium counts are reproduced only as necessary benchmarks. Unindexed or differently expressed historical kinetic classifications remain a priority risk; no independent audit has been carried out.

## References

1. V. Spirin, P. L. Krapivsky and S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037, first posted 2001-05-02. https://arxiv.org/abs/cond-mat/0105037
2. J. Strečka, K. Karľová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449, first posted 2015-02-16. https://arxiv.org/html/1502.04449v1
3. N. P. Konstantinidis, *Origin of the classical magnetization discontinuities of the dodecahedron*, arXiv:2311.17205, first posted 2023-11-28. https://ar5iv.labs.arxiv.org/html/2311.17205
