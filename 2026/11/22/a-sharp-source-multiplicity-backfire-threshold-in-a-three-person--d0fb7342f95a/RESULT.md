# A sharp source-multiplicity backfire threshold in a three-person bounded-confidence network

## Finding

In a three-person attractive-only weighted bounded-confidence network, adding a third perfectly aligned, slowly moving source can *reduce* the ordinary population's final average opinion by exactly \(31/50\). The source-count cutoff is sharp on the stated fixed ordinary graph:

\[
\lim_{t\to\infty}\frac{x_A(t)+x_{A'}(t)+x_B(t)}3=
\begin{cases}
1,&K=1,2,\\
19/50,&K\ge3.
\end{cases}
\]

Thus more sources favoring the same endpoint do not necessarily increase their final influence when confidence links can break. This is an exact small-network classification, not a general monotonicity theorem or an assertion that the qualitative possibility of manipulation backfire was previously unknown.

## Assumptions and scope

The opinions lie in \([0,1]\). There are three ordinary agents \(A,A',B\) initially at \(0,0,21/100\), and an arbitrary positive integer \(K\) of externally prescribed sources \(S_1,\ldots,S_K\). The fixed loop-free undirected weighted graph has the ordinary triangle with weights \(w_{AA'}=1\) and \(w_{AB}=w_{A'B}=1/2\); every source connects only to \(B\) with weight \(1\). The graph has no other edges. Each source has the same exogenously prescribed nondecreasing opinion

\[
s_t=\min\{1,1/2+t/1000\},\qquad t\in\{0,1,\ldots\}.
\]

Each ordinary agent at each integer time \(t\) simultaneously takes the weighted average of its adjacent agents whose current opinions differ from its own by at most \(\varepsilon=3/10\). It has no self-loop. Sources do not update through averaging. The observable is the mean of **only the three ordinary agents**, not an average including the varying number of sources. Every ordinary agent has at least one compatible neighbor for all \(t\), as proved below.

## Proof

By symmetry, the two ordinary agents \(A,A'\) always agree; call their common opinion \(a_t\), and write \(b_t=x_B(t)\). At \(t=0\), all edges are confidence-compatible: the two relevant initial gaps are \(21/100\) and \(29/100\), both strictly less than \(3/10\). Therefore

\[
a_1=\frac{2a_0+b_0}{3}=\frac7{100},\qquad
b_1=\frac{a_0+Ks_0}{K+1}=\frac{K}{2(K+1)}.
\]

**One or two sources.** Suppose all edges remain compatible. The update is

\[
a_{t+1}=\frac{2a_t+b_t}{3},\qquad
b_{t+1}=\frac{a_t+Ks_t}{K+1}.
\]

Set \(d_t=b_t-a_t\) and \(e_t=s_t-b_t\), and let \(\delta_t=s_{t+1}-s_t\), so \(0\le\delta_t\le1/1000\). Direct substitution yields

\[
\begin{pmatrix}d_{t+1}\\e_{t+1}\end{pmatrix}
=
\begin{pmatrix}
(2K-1)/(3(K+1))&K/(K+1)\\
1/(K+1)&1/(K+1)
\end{pmatrix}
\begin{pmatrix}d_t\\e_t\end{pmatrix}
+
\begin{pmatrix}0\\\delta_t\end{pmatrix}.
\]

For \(K=1\), the first step has \((d_1,e_1)=(9/50,251/1000)\), and the rectangle \(0\le d\le1/5\), \(0\le e\le3/10\) is forward invariant: the new first coordinate is at most \(1/30+3/20=11/60<1/5\), and the new second at most \(1/4+1/1000=251/1000<3/10\). For \(K=2\), the initial pair \((21/100,29/100)\) lies in \([0,3/10]^2\), which is invariant because \(d'=(d+2e)/3\le3/10\) and \(e'=(d+e)/3+\delta\le201/1000<3/10\). Consequently, by induction all relevant gaps stay within the confidence bound for both source counts, validating the assumed update at every step.

Once \(t\ge500\), the sources are constant at \(1\), so \(\delta_t=0\). For \(K=1\), the nonnegative gap matrix is \(\left(\begin{smallmatrix}1/6&1/2\\1/2&1/2\end{smallmatrix}\right)\); for \(K=2\), it is \(\left(\begin{smallmatrix}1/3&2/3\\1/3&1/3\end{smallmatrix}\right)\). In each case the row sums are at most one, with at least one strictly smaller than one and every matrix entry positive. Their second powers have both row sums strictly less than one, hence the gap vectors tend to zero geometrically. As \(s_t=1\) eventually, both ordinary opinion coordinates converge to \(1\).

**Three or more sources.** For every integer \(K\ge3\), the gap at time one is

\[
b_1-a_1=\frac{K}{2(K+1)}-\frac7{100}\ge\frac38-\frac7{100}=\frac{61}{200}>\frac3{10}.
\]

Both ordinary links incident on \(B\) therefore become incompatible at time \(1\). At that moment the source gap is \(s_1-b_1\le501/1000-3/8=126/1000<3/10\). Thus at the next update \(A\) and \(A'\) only average each other, so both remain exactly \(7/100\), whereas \(B\) averages the identical sources and equals \(s_1\). By induction \(a_t=7/100\) for all \(t\ge1\) and \(b_t=s_{t-1}\) for every \(t\ge2\): the source-to-\(B\) gap is at most \(1/1000\), the ordinary-to-\(B\) gap is at least \(1/2-7/100=43/100>3/10\), and the ordinary pair stays compatible. Hence the ordinary mean tends to

\[
\frac{2(7/100)+1}{3}=\frac{19}{50}.
\]

All active-neighbor sets are nonempty for every \(K\), so the dynamics is well defined. The difference between \(1\) and \(19/50\) is exactly \(31/50\), completing the proof.

## Verification

The companion standalone `checker.py` uses exact rational numbers to simulate each weighted, confidence-gated graph, without assuming the active edge set. It checks \(K=1,2,3,4,6,30\) across \(1100\) synchronous steps, including the full source ramp and a post-ramp interval, confirms the first rupture time, and independently tests the two invariant-rectangle recurrences. The code is a reproducibility and arithmetic check; the theorem for all integer \(K\) and infinite time is established by the proof, not by this finite simulation.

## Relationship to prior work

Tarantino, Mazza, Piccardi and Pierri (2026) introduce weighted bounded-confidence dynamics with static or gradually increasing exogenous opinion sources and evaluate influence numerically on community networks. The present result uses their explicit neighbor-only weighted averaging convention but supplies a complete finite graph and source-count phase separation. Their discussion already addresses loss of reach through premature opinion separation, so that mechanism alone is not claimed as new. Bautista (2025), especially Section 3 and Corollary 3.3, provides an increasing-source influence threshold in homogeneous grouped HK populations, and Section 5 studies other weighted attractive/repulsive variants. Those statements do not give the above sharp threshold for a fixed three-person attractive-only weighted graph with a moving common source schedule. Earlier work on moving stubborn agents provides sufficient pacing conditions, but not this count classification. An analogous claim in unsearched or unindexed older literature remains possible.

## Limitations

This is an exact, deterministic, specially weighted three-ordinary-agent example, not a population-wide prediction or an optimal intervention design. Its threshold is for a **fixed graph family** as \(K\) varies, not a universal minimum group size. Adding sources changes the total number of vertices and the incoming weight at \(B\), although it leaves the original three-agent graph and each per-source weight unchanged. The source opinion is an externally prescribed piecewise-linear ramp. No independent scientific validation has been undertaken.

## References

1. P. Tarantino, F. Mazza, C. Piccardi, F. Pierri, *Static and Dynamic Strategies for Influencing Opinions in Social Networks* (2026), arXiv:2605.14918v1, https://arxiv.org/abs/2605.14918 (first posted 2026-05-14).
2. A. Bautista, *Opinion dynamics in bounded confidence models with manipulative agents: Moving the Overton window* (2025), arXiv:2501.12198v1, https://arxiv.org/abs/2501.12198.
3. *Effect of Stubborn Agents on Bounded Confidence Opinion Dynamic Systems: Unanimity in Presence of Stubborn Agents* (2019), DOI:10.1109/IRANIANCEE.2019.8786531, https://doi.org/10.1109/IRANIANCEE.2019.8786531.
