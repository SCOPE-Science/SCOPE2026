# The three \((9_3)\) incidence geometries have distinct majority phase spectra

## Finding
Let \(\mathcal C\) be any simple symmetric incidence configuration of nine points and nine lines, with three incidences per point and per line, and with any two points on at most one common line. On its eighteen-vertex point-line Levi graph, let every vertex synchronously replace its binary opinion by the strict majority of its three neighbors. There are exactly three incidence-isomorphism types. Classify them by the cycle lengths of the graph on points joining pairs **not** lying on any common configuration line. This graph is 2-regular; the three possible types are \((9)\), \((3,6)\), and \((3,3,3)\). The last is the Pappus configuration.

For each type, the update map \(F\) has only fixed points and primitive temporal two-cycles. Its complete exact attraction-basin census is determined by the following table. A fiber histogram \(\{t:m_t\}\) means that \(m_t\) recurrent point-side symbols have exactly \(t\) preimages under the fourth-step point-side retraction.

| Noncollinearity cycles | Recurrent symbols \(S\) | Fixed states | Primitive two-cycle orbits | Sharp maximum transient | Fiber histogram \(\{t:m_t\}\) |
|---|---:|---:|---:|---:|---|
| \((9)\) | 98 | 98 | 4753 | 4 | \(\{1:18,2:18,3:36,4:24,127:2\}\) |
| \((3,6)\) | 96 | 96 | 4560 | 4 | \(\{1:16,2:30,3:12,4:36,128:2\}\) |
| \((3,3,3)\), Pappus | 92 | 92 | 4186 | 3 | \(\{2:54,4:36,130:2\}\) |

The histogram gives **every individual attractor basin**, not just their sums: for each symbol with fiber size \(t\), its corresponding fixed-point basin has size \(t^2\); for each unordered pair of distinct symbols of weights \(s,t\), the corresponding two-cycle basin has size \(2st\). Symbols are counted with multiplicity. Thus the entire multiset is specified, including when several pairs yield the same number. In particular the Pappus graph has no fixed point with a singleton basin, unlike both non-Pappus types, and only Pappus has universal periodization within three updates.

The numbers of labelled states first entering a periodic orbit at times \(0,1,2,3,4\) are, respectively,

| Noncollinearity cycles | Time 0 | Time 1 | Time 2 | Time 3 | Time 4 |
|---|---:|---:|---:|---:|---:|
| \((9)\) | 9604 | 57996 | 81396 | 95040 | 18108 |
| \((3,6)\) | 9216 | 64768 | 70416 | 105600 | 12144 |
| \((3,3,3)\) | 8464 | 79152 | 47808 | 126720 | 0 |

Every row sums to \(2^{18}=262144\).

## Assumptions and scope
Vertices are independently labelled and have states \(0,1\). A configuration is periodic at time \(r\) if and only if \(F^{r+2}(z)=F^r(z)\); its **first periodic-entry time** is the least such \(r\). All degrees are three, so no tie convention is needed. An attractor basin contains all starting configurations eventually entering that **temporal orbit**; a two-cycle orbit consists of two configurations, not one.

The three representative configurations have point set \(\{0,\ldots,8\}\) and the following nine line triples (the order shown labels line vertices \(0,\ldots,8\)):

- Noncollinearity \((9)\): \((012),(034),(056),(137),(168),(246),(278),(358),(457)\).
- Noncollinearity \((3,6)\): \((012),(034),(056),(148),(167),(237),(268),(358),(457)\).
- Noncollinearity \((3,3,3)\): \((012),(034),(056),(138),(157),(247),(268),(367),(458)\).

Here, for example, \((012)\) denotes the line incident with points \(0,1,2\). No statement concerns other sizes of configurations, other thresholds, asynchronous updates or spatial-symmetry quotients.

## Proof
**Exhaustive incidence-type reduction.** Fix a point, label it zero and normalize its three lines to \((012),(034),(056)\) by relabelling the six points collinear with zero. The remaining two points are 7 and 8. Every valid completion consists of six distinct triples among \(\binom{\{1,\ldots,8\}}3\), each pair of points used at most once, and each point meeting its remaining prescribed degree (two for points 1 through 6 and three for 7 and 8). Search the candidate triples in lexicographically increasing order, removing their pair pairs from future use. This finite recursion has **176** completions. Their missing-collinearity 2-regular graphs have cycle patterns \((9)\) in 96 completions, \((3,6)\) in 72, and \((3,3,3)\) in eight. For every completion, direct enumeration of rotations/reflections and permutations of equal-length cycles of its missing-collinearity graph gives a point permutation transporting all nine incidence triples to the displayed representative of that cycle pattern. The patterns are nonisomorphic, since their missing-collinearity cycle lengths differ. This proves exactly the three listed incidence classes without assuming the literature enumeration.

**One-shore factorization.** Let \(A:\{0,1\}^9\to\{0,1\}^9\) apply majority from point bits to line bits and \(B\) apply majority from line bits to point bits. Then
\[
 F(x,y)=(B(y),A(x)),\qquad
 F^2(x,y)=(H(x),K(y)),\quad H=B\circ A,\ K=A\circ B.
\]
Using the nine explicit line triples for each representative, the attached standalone finite certificate evaluates all \(512\) input values of \(H,K\) and verifies
\[
 H^3=H^2,\qquad K^3=K^2.
\]
It follows for all \(2^{18}\) starting states that \(F^6=F^4\). Put \(X=\operatorname{im} H^2\), \(Y=\operatorname{im}K^2\). Both \(H\) and \(K\) are the identity on their respective images. In particular, \(A:X\to Y\) and \(B:Y\to X\) are inverse bijections: \(B(A(x))=x\), and the analogous identity holds on \(Y\). Therefore the restriction of \(F\) to \(X\times Y\) is conjugate to the swap \((x,z)\mapsto(z,x)\) on \(X^2\). In all three cases the finite computation finds \(|X|=|Y|=S\), with the three sizes shown. There are exactly \(S\) fixed points and \(S(S-1)/2\) primitive two-cycle orbits.

**Every basin.** Since \(F^4(x,y)=(H^2(x),K^2(y))\), define \(\alpha_x=|(H^2)^{-1}(x)|\) for \(x\in X\), and \(\beta_y=|(K^2)^{-1}(y)|\) for \(y\in Y\). The same finite calculation verifies \(\beta_{A(x)}=\alpha_x\) for every \(x\in X\). A fixed-point basin indexed by \(x\) consequently has size \(\alpha_x^2\); the two-cycle indexed by distinct \(x,z\) has basin size \(2\alpha_x\alpha_z\). Counting the values of \(\alpha_x\) yields precisely the three displayed histograms. As a checksum, each satisfies \(\sum_x\alpha_x=512\), so summing the resulting basin sizes yields \(512^2=262144\).

**Sharp times.** The finite table verifies \(F^5\neq F^3\) for the two non-Pappus types, for example from point-side input mask 46 and line-side input mask 0: at steps 3 and 5 the two states are respectively \((0,8)\), \((0,0)\) in the \((9)\) type and \((0,32)\), \((0,0)\) in the \((3,6)\) type. Hence the bound four cannot decrease. For Pappus the table verifies the stronger identity \(F^5=F^3\) for all inputs, while the input \((13,0)\) gives distinct states \((1,0)\) and \((0,0)\) at steps two and four. Thus its sharp bound is three.

This proof uses finite enumeration solely to establish exact finite identities. Those identities, together with the algebraic factorization, entail the statements for **all** initial configurations of each of the three finite graphs.

## Verification
Run `python3 verify_93.py` (Python 3 standard library only). It enumerates all 176 normalized incidence completions, independently checks their isomorphisms to three representatives via explicit permutations of disjoint cycles, evaluates each of the 512 point-side and 512 line-side inputs, proves the key composition identities by complete equality of arrays, and checks every fiber, basin formula, sharpness witness and total. It prints `PASS` on success.

For an independent computation of the original dynamics rather than the one-shore factorization, compile and run `g++ -O2 -std=c++17 check_full_states.cpp -o check_full_states && ./check_full_states`. This computes all 262144 states **separately for each of the three graphs**, identifies cycles using indegree peeling, and counts their full individual attraction basins and entry times. It verifies all three tables against the stated results and ends with `PASS all 786432 states`.

The Python certificate and C++ exhaustive checker were executed successfully on their actual files. Their different procedures agree on all attractor counts, maximum entry times and basin spectra.

## Relationship to prior work
Adam, Dahleh and Ozdaglar (2012) study general finite binary threshold networks, prove eventual periods at most two, give convergence bounds, and establish counting complexity results. Those general theorems supply background, not the exact three incidence-type phase retractions, fiber spectra, or settling-time separation proved here. Bokowski and Pilaud (2012; journal 2014) treat enumeration of point-line configurations, including the Pappus configuration as a geometric example, but not majority updating on Levi graphs. Earlier exact counts on other individual incidence or cubic graphs do not imply these three nine-point incidence-type calculations. The result claims a complete new **dynamical** classification, not discovery of the three underlying incidence types or of the general period-two theorem.

## Limitations
The verified finite identities yield a proof for precisely these three eighteen-vertex graphs; they are not evidence for a universal finite-time bound on all \((n_3)\) configurations. The enumeration is computational but fully specified, bounded and independently cross-checked. Historical priority is qualified: obscure or unindexed equivalent exact dynamical tables may exist. No independent external mathematical audit or formal proof-assistant certification has been performed.

## References
1. J. Bokowski and V. Pilaud, *Enumerating topological \((n_k)\)-configurations*, original arXiv preprint dated 2012-10-01, https://arxiv.org/abs/1210.0306 .
2. E. M. Adam, M. A. Dahleh and A. E. Ozdaglar, *On Threshold Models over Finite Networks*, original arXiv preprint dated 2012-11-04, https://arxiv.org/abs/1211.0654 .
3. E. W. Weisstein, *\((9_3)\) Configuration*, MathWorld, https://mathworld.wolfram.com/9-3Configuration.html .
4. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html .
