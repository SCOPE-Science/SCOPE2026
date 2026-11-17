# Period-doubling without period six: exact twelve-cycles of Rule 30

## Finding

For every integer \(n\ge 3\), let \(F_n\) be elementary cellular automaton Rule 30 on the *indexed* cyclic binary ring of circumference \(n\). Let \(C_t(n)\) count distinct **primitive temporal** orbits of least period \(t\), without quotienting by spatial translations. Then

\[
\boxed{C_6(n)=14\mathbf{1}_{84\mid n},\qquad
C_{12}(n)=15\mathbf{1}_{60\mid n}+25\mathbf{1}_{100\mid n}+46\mathbf{1}_{138\mid n}.}
\]

In particular, a primitive twelve-cycle exists at circumference \(60\) but no primitive six-cycle exists there; the least circumference of a primitive six-cycle is \(84\). Conversely, circumference \(84\) admits a six-cycle but no twelve-cycle. The first circumference that admits both periods is \(420\).

The only primitive spatial lengths of period-twelve configurations are \(60\), \(100\), and \(138\), with respectively \(3\), \(3\), and \(4\) cycles of the space-time column transfer map. These contribute respectively \(15\), \(25\), and \(46\) temporal orbits when their lengths divide the ring circumference. The only primitive spatial length for period-six configurations is \(84\), represented by one transfer cycle.

## Assumptions and scope

The local update is exactly

\[
(F_nx)_j=x_{j-1}\mathbin{\mathrm{xor}}(x_j\mathbin{\mathrm{or}}x_{j+1}),
\qquad j\in\mathbb Z/n\mathbb Z,
\]

with binary coordinates and synchronous updates. A primitive period means \(F_n^t(x)=x\) and \(F_n^s(x)\ne x\) for every positive \(s<t\). Spatial rotations of a configuration are regarded as distinct unless the configurations are equal as indexed words. The result concerns initially periodic configurations, not trajectories that enter these orbits after a transient, and does not address bi-infinite nonspatially-periodic configurations.

## Proof

**1. A finite, complete representation.** Fix a temporal height \(p\in\{6,12\}\). Encode the full \(p\)-periodic temporal history of a spatial site by \(b\in\{0,1\}^p\), where its bit \(t\) is the state at time \(t\bmod p\). Let the cyclic time rotation be \(R(b)_t=b_{t+1\bmod p}\). For consecutive histories \(a,b,c\), the local Rule 30 equations at every time are exactly

\[
R(b)=a\mathbin{\mathrm{xor}}(b\mathbin{\mathrm{or}}c),
\quad\text{hence}\quad
 a=R(b)\mathbin{\mathrm{xor}}(b\mathbin{\mathrm{or}}c).
\]

Thus the transfer map

\[
T_p(b,c)=\bigl(R(b)\mathbin{\mathrm{xor}}(b\mathbin{\mathrm{or}}c),\ b\bigr)
\]

is a fully specified function on exactly \(2^{2p}\) ordered pairs. Starting with the histories at positions \(j,j+1\), successive applications of \(T_p\) traverse the ring in the direction of decreasing spatial index. Hence \(p\)-step periodic indexed configurations of circumference \(n\) correspond bijectively to pairs on the cycles of \(T_p\) whose cycle lengths divide \(n\). A transfer cycle of primitive spatial length \(d\mid n\) yields exactly \(d\) distinct indexed configurations.

**2. Exhaustive cycle decomposition.** The accompanying C++17 certificate enumerates all \(2^{2p}\) pair states, computes every indegree, removes all states of indegree zero recursively, and walks every remaining directed cycle. Since each state has one outgoing edge, repeated zero-indegree removal eliminates exactly the noncyclic vertices: a noncyclic vertex cannot survive, while each cyclic vertex keeps an incoming edge from its predecessor on that cycle. No ring circumference is truncated in this argument. The complete checked cycle spectra, written as (spatial length, least temporal period, number of transfer cycles), are:

| Height | Spatial length | Least temporal period | Transfer cycles |
|---|---:|---:|---:|
| \(6\) | 1 | 1 | 1 |
| \(6\) | 2 | 1 | 1 |
| \(6\) | 12 | 3 | 1 |
| \(6\) | 84 | 6 | 1 |
| \(12\) | 1 | 1 | 1 |
| \(12\) | 2 | 1 | 1 |
| \(12\) | 7 | 4 | 4 |
| \(12\) | 12 | 3 | 1 |
| \(12\) | 60 | 12 | 3 |
| \(12\) | 84 | 6 | 1 |
| \(12\) | 100 | 12 | 3 |
| \(12\) | 138 | 12 | 4 |

At height \(6\), the \(4{,}096\) pair states consist of \(3{,}997\) noncyclic and \(99\) cyclic states. At height \(12\), the \(16{,}777{,}216\) pair states consist of \(16{,}776{,}057\) noncyclic and \(1{,}159\) cyclic states. These sums and every cycle classification are asserted and checked by the executable source. The temporal least period is determined by the first positive time rotation fixing *all* histories on each transfer cycle, and is additionally checked by direct physical evolution in an independent program.

**3. Orbit division and arithmetic.** A transfer cycle of length \(d\) and least temporal period \(p\) contributes \(d\) indexed periodic configurations whenever \(d\mid n\). Since each primitive temporal orbit has exactly \(p\) configurations, its contribution is \(d/p\) orbits. The height-six length-\(84\) cycle gives \(84/6=14\). The height-twelve cycles give \(3\cdot60/12=15\), \(3\cdot100/12=25\), and \(4\cdot138/12=46\). This proves the formulas for all \(n\ge3\).

The minimum six-period circumference is \(84\); the minimum twelve-period circumference is \(60\). A circumference admitting both must be a multiple of \(84\) and at least one of \(60,100,138\); their minimum least common multiple is \(\operatorname{lcm}(84,60)=420\).

## Verification

Run the two standalone programs in a C++17 environment:

```
g++ -O2 -std=c++17 transfer_certificate.cpp -o cert
./cert
g++ -O2 -std=c++17 direct_crosscheck.cpp -o crosscheck
./crosscheck
```

Compare the text outputs with `transfer_output.txt` and `direct_output.txt`. The first program uses indegree elimination and direct time-word tests; the second uses independent on-the-fly graph traversal, reconstructs each spatial ring, and directly evolves the Rule 30 update to determine its temporal least period and verify the space-time columns. Both exhaust the entire respective finite pair-state spaces and agree on every cycle-length/temporal-period multiplicity. The files `witnesses.txt` and `make_witnesses.py` give independently re-evolvable examples at spatial lengths \(84,60,100,138\). Witnesses alone would not prove the nonexistence assertions; exhaustive transfer decomposition supplies those.

## Relationship to prior work

Wolfram's *A New Kind of Science* (2002), pages 267–268 and note page 954, introduces repeated-block short-period Rule 30 configurations, shows period six at block length \(84\), and explains the finite constraint approach. The illustrated complete examples concern least temporal periods up to ten, with a separate statement about period eleven. The book notes that periods up to fifteen occur, but does not state the present complete period-twelve circumference/orbit formula or the exact six-versus-twelve onset inversion. The period-six minimum is therefore credited as an established example, independently checked here as part of the comparison.

The general results on Rule 30 as a surjective, one-sided permutive automaton and on short temporal-period points do not specify these three primitive length-twelve components. The Rule 30 temporal-eleven all-circumference classification in another public mathematical record has distinct temporal height and does not imply the height-twelve spectrum. No historical priority beyond the inspected sources and searches is claimed.

## Limitations

This is an exact, finite-state, reproducible theorem restricted to primitive temporal periods six and twelve on indexed cyclic rings. It does not give attraction-basin sizes, general period spectra, random-initial-state behavior, or a lower bound for periods other than six and twelve. The finite computer check is an exhaustive proof of a finite transfer graph used to infer infinitely many ring circumferences; it is not a computational search limited to particular ring sizes. The programs and proof have not undergone independent external validation. Unindexed or inaccessible catalogues may contain an earlier equivalent result.

## References

1. Stephen Wolfram, *A New Kind of Science*, Wolfram Media, 2002, pages 267–268 and note page 954. https://www.wolframscience.com/nks/p267--special-initial-conditions/ ; https://www.wolframscience.com/nks/p268--special-initial-conditions/ ; https://www.wolframscience.com/nks/notes-6-6--repeating-blocks-in-cellular-automata/
2. Wolfram Media, *A New Kind of Science* publication record, May 14, 2002. https://www.wolfram-media.com/products/nks/
3. Johan Kopra, *Cellular Automata with Complicated Dynamics*, University of Turku, 2019, section 3.1, page 24 (Rule 30 background, not a twelve-cycle census). https://www.utupub.fi/bitstreams/f229bc81-1590-4a47-9047-cc8113366378/download
4. Dominic van der Zypen, question and discussion *Rule 30 in the infinite setting*, MathOverflow, 2022 (published counts through temporal period ten, not a period-twelve spatial spectrum). https://mathoverflow.net/questions/429509/rule-30-in-the-infinite-setting
