# Exact periodic-state census for synchronous majority on wheel networks

## Finding

For every integer \(n\ge 3\), let the **wheel with \(n\) rim vertices** be \(G_n=K_1*C_n\): one hub adjacent to every vertex of a simple \(n\)-cycle. Give each vertex a color in \(\{0,1\}\). All vertices simultaneously adopt the strict majority color among their neighbors and **retain their current color on a tie**. Write \(M\) for this deterministic update.

The **only fixed points of \(M\)** are the two monochromatic colorings. Every other recurrent state lies in a strict two-cycle. There is an exact, all-size enumeration of these states as follows.

For every integer \(L\ge 2\), define the bivariate integer polynomial

\[
Q_L(u,v)=1+u^L v^L+\sum_{m=2}^{L-1}\;\sum_{b=1}^{\min(L-m,\lfloor m/2\rfloor)}
\frac{L}{b}\binom{m-b-1}{b-1}\binom{L-m-1}{b-1}
 u^m v^{m-b}.
\]

Empty sums are zero. Define

\[
P_n(u,v)=\begin{cases}Q_n(u,v),&n\text{ odd},\\Q_{n/2}(u,v)^2,&n\text{ even},\end{cases}
\qquad
S_n=\sum_{\substack{m,e\ge0\\ 2m>n,\;2e<n}}[u^mv^e]P_n(u,v).
\]

Then the exact number of labeled configurations whose period divides two, and the exact number of distinct strict two-cycle **orbits**, are respectively

\[
\boxed{T_n=2+4\mathbf 1_{\{n\text{ even}\}}+2S_n,\qquad
B_n=2\mathbf 1_{\{n\text{ even}\}}+S_n.}
\]

Thus the census is polynomial-time computable in \(n\) using only integer arithmetic and binomial coefficients, without enumerating \(2^{n+1}\) initial configurations. In particular, for \(n=3,4,5,6,7,8,9,10,11,12\) the respective values of \(T_n\) are \(8,6,12,24,44,70,134,156,442,456\), and \(B_n\) are \(3,2,5,11,21,34,66,77,220,227\).

There are exponentially many strict two-cycle orbits on an infinite subsequence: for every integer \(t\ge0\),

\[
\boxed{B_{6t+3}\ge 2^t.}
\]

The two monochromatic fixed configurations therefore coexist with arbitrarily many oscillating periodic orbits, even though no nonmonochromatic fixed configuration exists.

## Assumptions and scope

The graph is finite, undirected, simple, unweighted, with the hub and rim as specified; there are exactly two colors; updates are synchronous and deterministic; rim degrees equal three; the hub degree is \(n\); and ties at the hub (possible for even \(n\)) preserve its current color. The convention \(G_n=K_1*C_n\) avoids variation in the standard wheel-index convention.

A *period-dividing-two configuration* means \(M^2(x)=x\), including fixed points; a *strict two-cycle orbit* is an unordered pair \(\{x,M(x)\}\) with \(M^2(x)=x\ne M(x)\). The result counts periodic states and orbits, **not** initial states that eventually flow into them and **not** attraction-basin probabilities.

## Proof

**1. Local update identities.** Denote the hub by \(c\) and the rim by \(x_i\), with indices in \(\mathbb Z/n\mathbb Z\). By global color complementation it suffices to examine first states with \(c=0\). The next rim coloring is

\[
y_i=x_{i-1}x_{i+1},
\]

where multiplication is Boolean AND. The hub becomes \(1\) exactly when \(m=\sum_i x_i>n/2\); in case of an equality it remains \(0\). Also let

\[
e=\sum_i x_{i-1}x_{i+1}=\sum_i x_ix_{i+2}=\sum_i y_i.
\]

**2. The hub remains fixed in a periodic state.** If the hub remains \(0\) in both steps, then the second-step rim is

\[
z_i=y_{i-1}y_{i+1}=x_{i-2}x_ix_{i+2}.
\]

Equality \(z=x\) requires that whenever \(x_i=1\), both distance-two neighbors are \(1\). In the step-two cyclic graph on the rim indices this forces the set of ones to be a union of entire connected components. If \(n\) is odd this step-two graph has one component, and if \(n\) is even it has two parity components. The all-one rim is incompatible with a hub remaining \(0\), since it makes the hub change to \(1\). The all-zero rim is fixed. For even \(n\), each of the two alternating rim words has exactly half of its positions equal to \(1\), so the hub retains \(0\) and the rim flips between the two alternating words. After global complementation, this yields precisely the two monochromatic fixed points and, only for even \(n\), four additional states forming two strict two-cycle orbits with constant hub.

**3. The hub changes in a periodic state.** Suppose it changes \(0\to1\to0\). In its second update the rim satisfies

\[
z_i=y_{i-1}\lor y_{i+1}=x_i\bigl(x_{i-2}\lor x_{i+2}\bigr).
\]

Thus \(z=x\) if and only if **each \(1\) on the rim has at least one distance-two neighbor that is also \(1\)**. The two hub changes occur if and only if

\[
2m>n\quad\text{and}\quad 2e<n.
\]

These three conditions are jointly necessary and sufficient for a period-two state with hub initially \(0\) and hub switching on both steps. Complementation gives a bijection to the corresponding states with initial hub \(1\). Hence the total number of hub-changing periodic states is twice the number of qualifying rim words.

**4. Exactly counting qualifying rim words.** Arrange rim indices by step-two adjacency. For odd \(n\) they form one cyclic word of length \(n\); for even \(n\) they form two cyclic words of length \(n/2\). The no-isolated-one requirement says every maximal run of ones in each cyclic word has length at least two. In such a word let \(m\) be the number of ones and \(e\) the number of adjacent pairs of ones **counted with cyclic multiplicity**. The all-zero and all-one words contribute respectively \(1\) and \(u^Lv^L\). Every other admissible word has \(b\) nonempty runs of zeros alternating with \(b\) runs of ones of length at least two, and consequently \(e=m-b\).

The number of **labeled** length-\(L\) cyclic words with this \((m,b)\) is

\[
\frac{L}{b}\binom{m-b-1}{b-1}\binom{L-m-1}{b-1}.
\]

Indeed, choose a distinguished first one-run start (\(L\) choices), compose \(m\) into \(b\) positive parts of size at least two, compose \(L-m\) into \(b\) positive parts, and divide by the \(b\) choices of which one-run was distinguished. This also handles the length-two cyclic convention: the edge between its two positions is counted twice. These counts give \(Q_L\), whose product across step-two components is \(P_n\). Extracting coefficients with \(2m>n\) and \(2e<n\) therefore gives exactly \(S_n\). Combining Steps 2 and 3 proves the formulas for \(T_n\) and \(B_n\).

**5. Exhaustiveness.** The general theorem of Goles and Olivos for finite symmetric threshold systems ensures that every trajectory of this majority rule eventually has period one or two. To check its hypotheses despite tie retention, identify the two colors with spins \(s_i\in\{-1,1\}\) and choose any \(0<\varepsilon<1\): the update is the sign of \(\sum_{j\sim i}s_j+\varepsilon s_i\). The neighbor sum is integral; thus a nonzero neighbor majority dominates the self-weight, while a zero neighbor sum retains the old spin. This uses the symmetric coupling matrix \(A+\varepsilon I\), where \(A\) is the undirected adjacency matrix. Steps 2–4 exhaust those periodic configurations and partition them by whether the hub changes. No transient configuration is counted as periodic.

**6. Exponential lower bound.** For odd \(n=6t+3\), arrange rim positions along the single distance-two cycle. Concatenate \(t\) blocks, independently choosing \(110110\) or \(111100\), followed by the block \(110\). These produce \(2^t\) distinct labeled words with \(4t+2\) ones, no isolated ones, and at most \(3t+1\) neighboring-one pairs (the blocks all end in zero). As \(2(4t+2)>6t+3\) and \(2(3t+1)<6t+3\), every such word yields a hub-switching periodic state. Each corresponding strict orbit contains exactly one hub-zero state, proving \(B_{6t+3}\ge2^t\).

## Verification

The accompanying standalone Python 3 script `verify.py` implements a full two-step majority transition independently of the formula, a second four-state transfer-matrix enumerator for no-isolated-one cyclic words, and an exact binomial-coefficient evaluator. Execute from the extracted package directory:

```text
python3 verify.py
```

It checks the complete \(2^{n+1}\)-state space for each \(3\le n\le15\), compares the two independent polynomial calculations for every \(2\le L\le28\), and verifies consistency for every \(3\le n\le60\). The observed stdout begins `PASS: 27 independent polynomial/transfer comparisons; 13 full-state enumerations; 58 all-size exact integer audits; 12 reference counts`. The unbounded theorem is proved above; finite verification is a reproducibility check and is not substituted for proof.

## Relationship to prior work

Goles and Olivos proved the general period-one-or-two theorem for symmetric threshold dynamics; this result invokes rather than re-proves that general theorem. Zehmakan studies synchronous deterministic majority with tie retention on social networks and develops bounds and counts especially on ordinary cycles; the present graph has a universal hub and a different, exact periodic-state enumeration. Turau studies fixed points and two-cycles on **trees**, which do not include wheels. The tree counting work provides an efficient tree-specific method but not the wheel formulas. The graph \(C_n\square K_2\) has a previously studied majority-orbit census but is a different two-layer cubic graph; neither its statement nor its parameters imply the wheel formula. The results are not presented as a new general bound for all graphs.

## Limitations

No claim is made for asynchronous updating, random tie-breaking, weighted edges, missing spokes, other graph families, stabilization-time distributions, or the sizes of attraction basins. Counts distinguish labeled configurations and unordered two-cycle orbits; no quotient by graph automorphisms is taken. The binomial formula is exact for every integer \(n\ge3\), but numerical checks are finite. Publication priority is not independently certified; equivalent formulations in unindexed Boolean-network literature remain a residual risk.

## References

1. A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760, first public February 14, 2023. https://arxiv.org/abs/2302.06760
2. A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems 38 (2024), article 21. https://doi.org/10.1007/s10458-024-09651-y
3. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580, 2022. https://arxiv.org/abs/2202.01580
4. V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769, 2023. https://arxiv.org/abs/2312.13769
5. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1
