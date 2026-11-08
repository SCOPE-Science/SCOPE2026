# A two-hub parity onset and exact period-two majority census on joined cycles

## Finding

Let \(\mathcal D_n=K_2\vee C_n\), \(n\ge3\): two adjacent labelled hub vertices are each joined to all \(n\) vertices of a labelled cycle. Update all binary opinions simultaneously by strict majority among **open neighbors**, retaining the current opinion in a tie. Let \(P_n\) be the number of labelled configurations of **least temporal period exactly two, starting at time zero**.

For integers \(n\ge3\), define the finite sum
\[
 S_n=\sum_{\substack{1\le k<n,\ r\ge1,\ 3r\le k,\ r\le n-k\\
                   2k>n+1,\ 2(k-2r)<n-1}}
 \frac nr\binom{k-2r-1}{r-1}\binom{n-k-1}{r-1}.
\]
For even \(n=2m\), put
\[
 B_n=\sum_{r=1}^{\lfloor m/2\rfloor}
 \frac nr\binom{m-r-1}{r-1}^{\!2};
\]
and put \(B_n=0\) when \(n\) is odd. Each summand is an integer after summing the marked run placements, and the displayed finite sums are exact integers.

**Theorem.** For every \(n\ge3\), there are exactly two fixed configurations, and
\[
 \boxed{P_n=2S_n+2B_n+4\mathbf1_{\{2\mid n\}}.}
\]
Thus the number of distinct initially primitive two-orbits is \(P_n/2\). Such an orbit exists **if and only if** \(n\) is even with \(n\ge4\), or \(n\) is odd with \(n\ge9\). Moreover, for every integer \(m\ge2\),
\[
 \boxed{P_{5m}\ge2^{m+1}.}
\]
Hence two-cycle populations are unbounded and grow at least exponentially along the natural length-five subsequence, despite the fixed-point population remaining equal to two.

The first values of \(P_n\), for \(n=3,4,\ldots,16\), are
\[
 0,20,0,28,0,52,36,184,132,476,364,1208,1160,3380.
\]

## Assumptions and scope

Vertices are labelled: the cycle vertices are \(0,1,\ldots,n-1\) in cyclic order, and the hubs are distinct labelled vertices \(a,b\). Each cycle vertex has precisely four open neighbors, namely its predecessor, successor and both hubs. Each hub has the other hub and every rim vertex as neighbors, hence degree \(n+1\). There are no self-loops or multiple edges. The case \(n=3\) uses the simple triangle for the rim and is included. Only **immediately periodic** states are enumerated, not the basins of eventual periodic states. Temporal orbits count phases related by one simultaneous update as the same orbit; rotations and graph automorphisms are **not** quotiented.

Write the initial rim as \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\), and put \(k=\sum_i x_i\). Use the three cyclic word maps
\[
 E(x)_i=x_{i-1}\wedge x_i\wedge x_{i+1},\qquad
 D(x)_i=x_{i-1}\vee x_i\vee x_{i+1},\qquad
 G(x)_i=\operatorname{maj}(x_{i-1},x_i,x_{i+1}).
\]

## Proof

### Step 1: hub types and local rim maps

If the hubs both hold zero, each rim has two zero hub-neighbors and its update is exactly \(E\); if both hold one, the update is \(D\). If the hubs disagree, the rim has one hub-neighbor of each type and updates by \(G\). These are direct evaluations of the four-neighbor strict-majority rule, including the tie-retention case.

Equal hubs always remain equal after any update, since their own states and external rim votes are identical. Therefore a state with hubs initially different cannot have least period two if the next hub pair is equal. For an initial hub pair \((0,1)\), the conditions that the next pair be \((1,0)\) are
\[
 2(k+1)>n+1,\qquad 2k<n+1,
\]
which hold for an integral \(k\) precisely when \(n=2m\) is even and \(k=m\). Keeping the pair \((0,1)\) unchanged would instead require simultaneously \(2k\le n-1\) and \(2k\ge n+1\), impossible. The same applies after exchanging hub labels. Thus the only immediately periodic unequal-hub case is \((0,1)\leftrightarrow(1,0)\), with exactly half the rim vertices equal to one at both phases.

For a pair \((0,0)\), remaining \((0,0)\) for two updates requires \(E^2(x)=x\). Because \(E^2(x)\le E(x)\le x\) coordinatewise, this forces \(E(x)=x\), so \(x\) is constant on the connected cycle. The all-one rim would flip the hubs to one, so only the all-zero configuration is fixed. The complement argument for initial pair \((1,1)\) gives the all-one fixed configuration. In particular there are exactly two fixed states.

The remaining equal-hub possibility is \((0,0)\leftrightarrow(1,1)\). For its first transition, let \(y=E(x)\). Return after two steps requires \(D(y)=x\), with the hub inequalities
\[
 2k>n+1,\qquad 2\sum_i y_i<n-1. \tag{1}
\]

### Step 2: the equal-hub contribution

For a nonconstant cyclic binary word, \(D(E(x))=x\) holds exactly when **every maximal run of ones has length at least three**. Indeed, erosion shortens each one-run of length at least three by one at each end, and dilation restores precisely those runs; any shorter one-run is erased and cannot be restored. The all-zero and all-one words fail the required hub inequalities (1).

Let the cyclic word have \(k\) ones in \(r\) positive runs, with at least three ones per run. There are exactly \(r\) positive zero-runs; hence \(3r\le k\), \(r\le n-k\). Erosion leaves exactly \(k-2r\) ones. The hub inequalities (1) become \(2k>n+1\) and \(2(k-2r)<n-1\).

For fixed \(k,r\), there are
\[
 \frac nr\binom{k-2r-1}{r-1}\binom{n-k-1}{r-1}
\]
labelled cyclic words. The two binomial factors count ordered positive run compositions after subtracting the mandatory three ones and one zero in each run; one may choose any of \(n\) labelled positions as the start of a designated one-run, while each word is represented \(r\) times. This gives exactly \(S_n\) possible rim words when the hubs initially equal zero. By global bit complement, there are also exactly \(S_n\) configurations initially having both hubs equal one. Their sum is \(2S_n\).

### Step 3: the opposite-hub contribution

The rim evolves by \(G\) while the hubs switch between \((0,1)\) and \((1,0)\). The cyclic radius-one majority map \(G\) has exactly two types of configurations satisfying \(G^2(x)=x\): its fixed configurations, consisting of words with all monochromatic runs of length at least two (including constants), and the two completely alternating words when \(n\) is even. For completeness: an adjacent equal pair is permanent under \(G\), since each endpoint has two agreeing votes among itself and its paired neighbor. Hence the set of equal adjacent bonds can only increase. If such a bond exists and some site is isolated, there is a maximal chain of at least two consecutive unequal bonds bounded by an equal bond. At the boundary of that chain, the first isolated vertex flips while its neighboring vertex belonging to the equal bond stays fixed, turning a previously unequal bond into an equal one. Such a word cannot be periodic, since an equal-bond set cannot increase and then return. If there are no isolated sites, each monochromatic run has length at least two and the word is fixed. If there is no equal bond anywhere, the ring is exactly alternating and must have even length; it flips at every step. These exhaust all possibilities.

For opposite hubs to switch, the rim must contain \(m\) ones at both phases, so \(n=2m\). Both alternating words are balanced. A fixed, balanced, nonconstant rim word has \(r\) one-runs and \(r\) zero-runs, each of length at least two. The number of such labelled words is
\[
 \frac {2m}r\binom{m-r-1}{r-1}^{\!2},
\]
by the same cyclic marked-run argument. Summing gives \(B_n\), and adding the two alternating words gives \(B_n+2\) rim words for either labelled opposite-hub orientation. Since there are two opposite-hub orientations, this contributes \(2B_n+4\mathbf1_{\{2\mid n\}}\). Combining with Step 2 proves the exact formula.

### Step 4: the sharp size threshold and exponential subfamily

For every even \(n=2m\ge4\), the cyclic word with one run of \(m+1\) ones and one run of \(m-1\) zeros satisfies the two hub inequalities and has a one-run of length at least three. Thus \(S_n>0\). For odd \(n=2m+1\), a single one-run can never work: the inequalities would demand both \(k\ge m+2\) and \(k\le m+1\). Two or more one-runs require at least eight sites, so no odd size below nine works. Conversely for every odd \(n=2m+1\ge9\), choose two one-runs of lengths \(3\) and \(m-1\), separated by zero-runs of lengths \(1\) and \(m-2\). Then \(k=m+2\), \(r=2\), and both inequalities hold. This proves the existence criterion.

Finally, for each \(m\ge2\), independently choose any of the two five-bit blocks `11100` and `11110` at each of \(m\) consecutive labelled positions of a length-\(5m\) cycle. All \(2^m\) resulting words have one-runs of lengths three or four, with \(k\in[3m,4m]\) and \(r=m\). Hence \(2k>5m+1\), while \(2(k-2r)<5m-1\). All belong to the equal-zero hub class, and complementing their full configurations gives another \(2^m\) configurations. Therefore \(P_{5m}\ge2^{m+1}\).

## Verification

`verify_formula.py` implements the integer sums and independently enumerates the cyclic-word conditions for each \(3\le n\le16\), checking separately the \(S_n\) and \(B_n\) terms. It also checks the explicit length-five block construction for \(2\le m\le6\). `verify_direct.py` constructs the graph from its edge set and independently simulates both updates of **every one of the \(2^{n+2}\) binary configurations** for each \(3\le n\le16\). All checked fixed and primitive-two counts, and their four possible hub-transition types, agree with the theorem. The two scripts and literal captured output files are included. These finite computations are corroboration; the proof above establishes the formula for every \(n\ge3\).

## Relationship to prior work

Symmetric-threshold dynamics classically has eventual period at most two; that general fact alone neither counts initially periodic states nor determines the parity threshold here. The preprint of Kaaser, Mallmann-Trenn and Natale (2015), examined in its accessible complete online text, develops convergence-time bounds and symmetry reductions, but does not give the cyclic-run census on \(K_2\vee C_n\). Tosic and Agha (2004), whose accessible paper was inspected, and Nakar and Ron (2022) treat one-dimensional threshold automata: their radius-one majority facts help describe the opposite-hub rim, but do not impose the pair of global hub-vote inequalities needed for this result. Earlier exact calculations on the single-hub wheel \(K_1\vee C_n\) have different rim degree, and their run-length constraints do not imply the three-site erosion/opening formula above.

## Limitations

The result enumerates only initially fixed and primitive-two states. It makes no claim about first periodic-entry times, attraction-basin sizes, or a sharp full-sequence exponential growth constant. The exponential bound is only on the subsequence of circumferences divisible by five. The complete original text of Goles and Olivos (1980/1981) was not accessible here, so historical priority remains qualified; an unindexed exact graph-specific derivation is also possible. Independent external auditing has not been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: `10.1016/0012-365X(80)90121-1`.
2. P. T. Tosic and G. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, LNCS 3305, pp. 861–870. Accessible author's PDF: `https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf`.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:`1508.03519`, first posted 2015-08-14, `https://arxiv.org/abs/1508.03519`.
4. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:`2205.08972`, first posted 2022-05-18, `https://arxiv.org/abs/2205.08972`.
