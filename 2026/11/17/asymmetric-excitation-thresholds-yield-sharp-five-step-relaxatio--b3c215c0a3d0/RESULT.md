# Asymmetric excitation thresholds yield sharp five-step relaxation and two recurrent-wave onsets on bicliques

## Finding
Let \(m,n\ge1\). For synchronous three-state Greenberg–Hastings excitation on a labelled complete bipartite graph \(K_{m,n}\), give vertices in the first shore threshold one and those in the second shore threshold two. Every configuration reaches its eventual periodic orbit within five updates, and the bound is attained exactly when \(m\ge3\) and \(n\ge2\). The all-rest configuration is the only fixed configuration; other recurrent states have primitive period three or four.

Write
\[
 A_m=\sum_{\substack{i+j+k=m\\i,j,k\ge2}}\frac{m!}{i!j!k!},\qquad
 B_m=\sum_{j=2}^{m-2}\binom mj,
\]
where empty sums vanish. Then the exact numbers of *labelled configurations already on primitive orbits* are
\[
 P_3(m,n)=A_m\bigl(3^n-3\cdot2^n+3\bigr),\qquad
 P_4(m,n)=2B_m\bigl(2^n-2\bigr).
\]
Thus period-three orbits occur exactly when \(m\ge6,n\ge3\), and period-four orbits occur exactly when \(m\ge4,n\ge2\); their orbit numbers are respectively \(P_3/3\) and \(P_4/4\). For example, on \(K_{6,3}\) there are 540 configurations on three-cycles and 600 on four-cycles, i.e. 180 and 150 primitive orbits.

There is also an exact universal coefficient formula for every **first periodic-entry time** \(t\) and **eventual least period** \(p\). Define \(f_0(z)=1\), \(f_1(z)=z\), \(f_2(z)=e^z-1-z\). For each \(\sigma\in\{0,1,2\}^6\), let \((t_\sigma,p_\sigma)\) be the pair returned by the six-group finite recurrence in the proof. Then
\[
 N_{t,p}(m,n)=m!n!\,[x^m y^n]
 \sum_{\substack{\sigma\in\{0,1,2\}^6\\(t_\sigma,p_\sigma)=(t,p)}}
 \prod_{j=0}^2f_{\sigma_j}(x)\prod_{j=3}^5f_{\sigma_j}(y).
\]
This coefficient is a finite nonnegative integer and \(\sum_{t,p}N_{t,p}(m,n)=3^{m+n}\). All entries not listed in the finite enumeration of the proof are zero.

## Assumptions and scope
States are \(0\) (resting), \(1\) (excited) and \(2\) (refractory). In one *simultaneous* update, every excited site becomes refractory, every refractory site becomes resting, and a resting site becomes excited precisely when it sees at least its own threshold number of excited neighbors. The left shore has threshold \(1\) and size \(m\), the right shore threshold \(2\) and size \(n\). No self-neighbors or stochasticity occur. The first periodic-entry time \(t\ge0\) is the minimum index for which the state at \(t\) belongs to a periodic orbit, and \(p\ge1\) is its primitive period. All vertex labels are distinct, and neither shore is empty.

## Proof
**Finite exact reduction.** Partition the initial vertices in each shore by their *initial* state, giving six fixed, labelled classes \(L_0,L_1,L_2,R_0,R_1,R_2\). Vertices in each initial class always evolve together: their current state and their neighbor sets agree. For each initial class \(j\), record its multiplicity truncated at two, \(\sigma_j=\min(2,|C_j|)\). Since both activation thresholds are at most two, every later excitation test depends only on these six truncated multiplicities, not on the original cardinalities. Empty classes have a sentinel state \(-1\); nonempty classes start with state \(j\bmod3\). If \(c_j(s)\) denotes the current state of class \(j\) after \(s\) updates, calculate capped excitation totals
\[
 E_L(s)=\min\left(2,\sum_{j=0}^{2}\sigma_j\mathbf1_{\{c_j(s)=1\}}\right),\quad
 E_R(s)=\min\left(2,\sum_{j=3}^{5}\sigma_j\mathbf1_{\{c_j(s)=1\}}\right).
\]
For nonempty left classes set \(c_j(s+1)=2\) if \(c_j(s)=1\), \(0\) if \(c_j(s)=2\), and \(\mathbf1_{\{E_R(s)\ge1\}}\) if \(c_j(s)=0\); for right classes replace the last test by \(\mathbf1_{\{E_L(s)\ge2\}}\). Keep empty classes at \(-1\). This is a fully specified deterministic transition on at most \(3^6=729\) initial signatures. A repeat of the six-class state vector is equivalent to a repeat of the microscopic labelled configuration, since every nonempty class remains monochromatic.

**Exhaustive finite lemma.** Applying that recurrence to all 729 signatures, comparing class vectors through the ninth step, gives exactly the following numbers of signatures indexed by \((t,p)\):

| First entry \(t\) | Period \(p=1\) | Period \(p=3\) | Period \(p=4\) |
|---:|---:|---:|---:|
| 0 | 9 | 8 | 8 |
| 1 | 72 | 0 | 32 |
| 2 | 234 | 0 | 56 |
| 3 | 178 | 0 | 24 |
| 4 | 68 | 0 | 8 |
| 5 | 32 | 0 | 0 |

The table accounts for all 729 signatures, including signatures with empty shores (which are used only as a certificate). The attached `verify_profiles.py` states and verifies every transition, compares this complete table with the enumerated results, and checks the sharpness and recurrent-profile characterizations. This finite lemma is an exhaustive combinatorial calculation, not extrapolation from bounded graph sizes.

**Period populations and sharpness.** In the full finite table, the only immediately primitive-three profiles have all three left classes of size at least two and all three right classes nonempty. They therefore contribute \(A_m(3^n-3\cdot2^n+3)\) labelled colorings. The only immediately primitive-four profiles have the left initially supported on \(\{0,2\}\) or \(\{0,1\}\), with both present classes of size at least two; the right initially uses the matching two phases \(\{0,1\}\) or \(\{0,2\}\), each nonempty. Each choice contributes \(B_m(2^n-2)\), giving the claimed factor two. The only immediately fixed coloring with positive shore sizes is all-rest. The finite table bounds first entry by five. Every signature with first entry five needs at least three left and two right sites, and the signature \((2,0,1;0,1,1)\), with extra vertices assigned to its nonzero classes, proves the bound is attained for every \(m\ge3,n\ge2\).

**All-time enumeration.** For a class of required capped size zero, one or at least two, the exponential generating functions for its actual labelled cardinality are respectively \(1\), \(z\), and \(e^z-1-z\). Multiplication over the six initial classes, followed by the two coefficient extractions, counts exactly all initial colorings of each signature. Grouping by the rigorously determined \((t_\sigma,p_\sigma)\) proves the stated universal formula.

## Verification
`verify_profiles.py` enumerates all 729 initial signatures, verifies the complete table, the recurrent-profile shapes, and the sharp-entry witness conditions. `verify_micro.py` independently evolves 89,514 labelled microscopic configurations over ten shore-size pairs, computes first entry and least period, and compares their entire \((t,p)\) histograms against the coefficient formula, also confirming the two closed population counts. See `profile_output.txt` and `micro_output.txt`. Both scripts require only Python's standard library and can be run from the same directory with `python verify_profiles.py` and `python verify_micro.py`.

## Relationship to prior work
Fisch, Gravner and Griffeath introduced threshold-dependent excitable cellular automata and investigated their large-scale lattice dynamics. Durrett and Griffeath studied threshold-range scaling and asymptotic activity. Gravner, Lyu and Sivakoff analyzed three-color excitable dynamics on arbitrary graphs with a common threshold-one rule, not the present shore-dependent threshold pair. Published complete-bipartite homogeneous-threshold-one and homogeneous-threshold-two censuses likewise do not immediately imply the mixed-threshold phase counts: changing a threshold changes the contact condition and is not a conjugacy or monotone transformation of orbit periods. The present result addresses the response to *heterogeneous activation thresholds* on two distinguished shores and gives all-size counts of its immediate recurrent and transient configurations.

## Limitations
The all-parameter proof uses a small, complete computer-replayable finite lemma rather than a fully hand-tabulated case analysis; the scripts are part of the proof evidence. It does not address arbitrary graphs, nonuniform thresholds within each shore, asynchronous updates, or four or more states. No assertion of absolute historical priority or independently certified proof is made. Older journal literature may have earlier year-level dates than the first exactly day-dated cited preprint, and some closely related repository records were available only as abstracts.

## References
1. R. Fisch, J. Gravner, D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39. https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf
2. R. Durrett, D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv preprint 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
3. J. Gravner, H. Lyu, D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, Annals of Applied Probability **28** (2018), 3324–3357. https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf
4. *Threshold-two excitation on bicliques: sharp orbit onsets and a five-step clock*, published research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-threshold-two-excitation-on-bicliques-sharp-orbit-onsets-and-a-f--5bef754e247f
5. *A four-step relaxation law and complete orbit-depth census for bipartite excitable dynamics*, published research record. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-four-step-relaxation-law-and-complete-orbit-depth-census-for-b--3a7e2d671cfb
