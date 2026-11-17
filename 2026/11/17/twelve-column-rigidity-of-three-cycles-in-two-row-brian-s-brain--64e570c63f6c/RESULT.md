# Twelve-column rigidity of three-cycles in two-row Brian’s Brain

## Finding
For every integer \(n\ge3\), define synchronous Brian’s Brain on the indexed torus \(\mathbb Z_2\times\mathbb Z_n\). A ready site becomes firing exactly when two of its eight Moore-neighbor **offsets** are firing; firing becomes refractory, and refractory becomes ready. Coincident offsets are counted separately. Let \(F_n\) be one synchronous update. Then

\[
\#\operatorname{Fix}(F_n^3)=1+24\mathbf1_{12\mid n},
\qquad C_3(n)=8\mathbf1_{12\mid n}.
\]

Here \(C_3(n)\) counts primitive temporal three-orbits without quotienting spatial rotations. All nontrivial three-periodic configurations have least spatial period exactly 12. For \(12\mid n\), they are the 12 rotations of each of two oriented phase patterns described below. For any other circumference there are no temporal three-cycles.

## Assumptions and scope
At each site, state 0 is ready, state 1 is firing, and state 2 is refractory. The update is \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) precisely when the number of firing Moore offsets is two, otherwise \(0\mapsto0\). The eight offsets are \((\Delta r,\Delta x)\in\{-1,0,1\}^2\setminus\{(0,0)\}\), reduced modulo \((2,n)\). With two rows, different offsets can arrive at the same site; all eight incidences remain counted. No assertion is made about other temporal periods, their attraction basins, or the different distinct-neighbor convention.

The phase type of a site is `*` if it stays ready at all three times; otherwise phase 0, 1, or 2 means it fires at that time modulo three. For a phase-0 site the three-time state history is `(1,2,0)`; phase 1 has `(0,1,2)`; phase 2 has `(2,0,1)`. Every three-periodic site has exactly one of these four histories.

Up to rotation, the two spatial length-12 column-type words (each ordered pair is top and bottom phase type) are:

```
A: (*,0) (0,2) (1,*) (0,1) (*,2) (2,1) (0,*) (2,0) (*,1) (1,0) (2,*) (1,2)
B: (*,0) (1,2) (2,*) (1,0) (*,1) (2,0) (0,*) (2,1) (*,2) (0,1) (1,*) (0,2)
```

These two words and their rotations give 24 distinct labelled configurations whenever \(12\mid n\). Repeating them along the circumference gives the larger-torus solutions.

## Proof
**Four histories.** If a site fires at some time in a temporal-three orbit, the subsequent two states are forced to be refractory and ready; returning at time three forces it to fire again. Otherwise it remains ready throughout. This proves the four-type description without assuming all sites are active.

**Exact local constraint.** Write consecutive phase columns as \(a,b,c\in\{*,0,1,2\}^2\). For row \(r\in\{0,1\}\) and time \(t\in\{0,1,2\}\), set \(\chi_t(s)=1\) if the type \(s\) fires at time \(t\), and zero otherwise (including \(s=*\)). The number of firing Moore offsets adjacent to the middle-column site is exactly

\[
N_{r,t}(a,b,c)=\chi_t(a_r)+2\chi_t(a_{1-r})
+2\chi_t(b_{1-r})+\chi_t(c_r)+2\chi_t(c_{1-r}).
\]

The coefficients \(2\) on the opposite row arise from coincident vertical/diagonal offsets. If \(b_r=*\), admissibility requires \(N_{r,t}\ne2\) for every time \(t\). If \(b_r=j\in\{0,1,2\}\), admissibility requires \(N_{r,j-1\bmod3}=2\); its other two state transitions are forced. These are necessary and sufficient conditions on the entire three-time orbit.

**Finite transfer proof, valid for all circumferences.** There are 16 column types and 256 ordered pairs. Put an edge from pair \((a,b)\) to \((b,c)\) exactly when both middle-column row conditions hold. A direct finite enumeration of the 4096 candidate triples (supplied in two independently implemented verification programs) gives 199 vertices incident to an edge and 346 edges. The graph has precisely three strongly connected components containing directed cycles: one loop at the all-silent column pair and two directed simple cycles of 12 vertices each. In each 12-cycle, every vertex has exactly one internal predecessor and one internal successor; the two phase words above list their columns explicitly. All other components contain no directed cycle.

A length-\(n\) closed walk in this graph is in bijection with a labelled \(2\times n\) configuration fixed by \(F_n^3\): the consecutive column-pair overlaps guarantee a unique cyclic column string, and the local conditions guarantee every update. Every closed walk belongs to a cyclic strongly connected component. A single loop contributes one, and each directed 12-cycle contributes 12 closed walks exactly when \(12\mid n\). Therefore

\[
\#\operatorname{Fix}(F_n^3)=1+24\mathbf1_{12\mid n}.
\]

A temporal fixed point can contain neither firing nor refractory sites, so it is uniquely all-ready. As three is prime, every other point of \(\operatorname{Fix}(F_n^3)\) has least temporal period three. Dividing its population by three proves the orbit formula. The two 12-cycles imply all these states have least spatial period 12, establishing rigidity.

## Verification
Run `python3 verify_transfer.py` and `python3 verify_history.py` from the directory containing them. The first enumerates phase constraints; the second evaluates all three original-time updates independently and computes strongly connected components using a separate algorithm. Both confirm the 199-vertex, 346-edge graph, components of sizes 12, 12, and 1, and single-cycle internal degrees. The first additionally verifies all closed-walk counts for circumferences 3 through 24; the infinite-length conclusion uses the full graph decomposition, not those finite tests.

Compile `verify_direct.cpp` using `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct` and run `./verify_direct`. It exhaustively evolves all \(3^{2n}\) initial states for each \(3\le n\le6\), confirming only the all-ready state returns after three updates. It also evolves an explicitly listed width-12 nontrivial witness, verifying the three-step return. The recorded outputs are included alongside the source files.

## Relationship to prior work
The Brian’s Brain rule is attributed to Brian Silverman in a 1996 reference and is documented with its three states and exact-two birth rule in accessible descriptions [1–3]. The earlier graph method of Banks and Djirar [4] establishes a general way to study fixed and shift cycles of cellular automata; its inspected theorem and examples do not give this specific three-state, two-row, eight-offset resonance. A separate existing three-row Brian’s Brain census concerns \(\mathbb Z_3\times\mathbb Z_n\), whose vertical incidence structure differs and whose conclusions do not imply this width-two theorem.

## Limitations
The assertion is only about primitive temporal three-cycles, not all periodic orbits or eventual behavior. Two coincident Moore offsets remain separate; replacing them by distinct neighbors changes the local rule. The 1996 original active-essay page was unavailable for full-text comparison; published rule descriptions and a related archived graph-theoretic research report were inspected instead. Completeness of the full historical literature cannot be guaranteed. Independent external mathematical audit has not been performed.

## References
1. M. Resnick and B. Silverman, *Exploring Emergence: The Brain Rules* (1996-02-04), MIT Media Laboratory. Original historical URL: https://www.playfulinvention.com/emergence/mutants.html ; 1996 work also listed at https://courses.media.mit.edu/1997spring/mas712/slweb/information/papers.html . Original page currently inaccessible.
2. *Brian’s Brain*, HandWiki, rule and oscillator description and references: https://handwiki.org/wiki/Brian%27s_Brain .
3. Playful Invention Company, *Cellular Automata*, origin attribution: https://www.playfulinvention.com/PICOsite/projects/ .
4. S. P. Banks and S. Djirar, *Fixed Points and Shift Cycles in Cellular Automata*, Sheffield research report 459, September 1992: https://eprints.whiterose.ac.uk/id/eprint/79286/1/acse%20research%20report%20459.pdf .
