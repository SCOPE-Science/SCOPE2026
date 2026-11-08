# A unique forbidden pair in the elementary-direction Rayleigh graph of a four-dimensional zonotope

## Finding
Consider the standard vectors \(e_1,e_2,e_3,e_4\) of \(\mathbb R^4\), and set \(d_{ij}=e_i-e_j\) for \(1\le i<j\le4\). Write \(Z(g_1,\ldots,g_m)=\sum_k[0,g_k]\). For every \(t\ge0\) define
\[
A_t=Z(e_1,e_2,e_3,d_{24},d_{34},t(e_1-e_2-e_3)).
\]
Let \(\mathcal D=\{e_1,e_2,e_3,e_4\}\cup\{d_{ij}:1\le i<j\le4\}\), the ten elementary columns of the ordinary portion of the Oxley--Walsh four-dimensional \(2\)-modular template. For two **distinct** members \(u,v\in\mathcal D\) and any \(s,r>0\), define the log-submodularity defect
\[
\Delta_{u,v}(t;s,r)
=|A_t|\,|A_t+[0,su]+[0,rv]|
-|A_t+[0,su]|\,|A_t+[0,rv]|.
\]
All volumes are four-dimensional Lebesgue volumes.

**Complete sign classification:** For \(t>0\), among the \(\binom{10}{2}=45\) unordered distinct pairs, the **only** pair for which this defect can be positive is \(\{d_{14},d_{23}\}\). Its exact defect is
\[
\Delta_{d_{14},d_{23}}(t;s,r)=4sr\,t(2-t).
\]
Every other pair has strictly negative defect for every \(t>0\). Thus for \(0<t<2\), exactly one elementary-direction pair violates log-submodularity; at \(t=2\), that pair is an equality case and the other \(44\) pairs satisfy the inequality strictly; and for \(t>2\), all \(45\) pairs satisfy it strictly. At \(t=0\), exactly eight pairs are equality cases and the other \(37\) satisfy the inequality strictly. These statements hold for **all** positive segment lengths \(s,r\), not just unit segments. The full \(45\)-pair coefficient table appears below.

## Assumptions and scope
Directions are regarded as unoriented for volume: replacing a generator by its negative translates the zonotope and has no effect on the defect. Both added directions are taken from the fixed ten-element set \(\mathcal D\), and are distinct. Some may already occur as base generators, in which case adding a parallel segment is nevertheless well-defined. The parameter is real and nonnegative, and the two lengths are strictly positive. If either length vanishes, the defect is trivially zero for every direction pair. The result does not claim a sign classification for arbitrary directions outside \(\mathcal D\), or for arbitrary four-dimensional zonoids. At \(t=1\), all generators lie in the original integral \(2\)-modular template; for general real \(t\) no modularity assertion is made.

## Proof
**1. Exact zonotope formula.** If a list \(L=(g_1,\dots,g_m)\) spans \(\mathbb R^4\), then the standard determinant formula is
\[
|Z(L)|=\sum_{I\subseteq\{1,\ldots,m\},\ |I|=4}
\left|\det(g_i:i\in I)\right|.
\]
Put \(G=(e_1,e_2,e_3,d_{24},d_{34})\) and \(h=e_1-e_2-e_3\). For each pair \(u,v\), write \(a(t)=|Z(G,th)|\), and define \(b(t),c(t),q(t)\) uniquely by
\[
|A_t+[0,u]|=a(t)+b(t),\quad
|A_t+[0,v]|=a(t)+c(t),
\]
\[
|A_t+[0,u]+[0,v]|=a(t)+b(t)+c(t)+q(t).
\]
Every maximal minor in these four volume formulas contains \(th\) at most once. Its absolute value is therefore either constant or exactly \(t\) times an integer for \(t\ge0\). Hence \(a,b,c,q\) are affine functions of \(t\) with integer coefficients. The base volume is exactly \(a(t)=4+10t\).

**2. Dependence on both segment lengths.** Multilinearity of maximal minors in separate newly added columns gives, for all \(s,r\ge0\),
\[
|A_t+[0,su]+[0,rv]|=a(t)+s b(t)+r c(t)+sr q(t).
\]
Consequently
\[
\Delta_{u,v}(t;s,r)
=sr\big(a(t)q(t)-b(t)c(t)\big)
=-sr F_{u,v}(t),\qquad
F_{u,v}(t):=b(t)c(t)-a(t)q(t).
\]
Each \(F_{u,v}\) is an explicit polynomial of degree at most two. Its three coefficients can be reconstructed entirely from determinant sums at \(t=0\) and \(t=1\). If \((a_j,b_j,c_j,q_j)\) denotes those four exact values at \(t=j\), put \(\dot a=a_1-a_0\) and similarly for the other three. Then the constant, linear and quadratic coefficients are respectively
\[
\alpha=b_0c_0-a_0q_0,\quad
\beta=b_0\dot c+c_0\dot b-a_0\dot q-q_0\dot a,\quad
\gamma=\dot b\dot c-\dot a\dot q.
\]
This formula requires no sampling assumption: affineness was proved above.

**3. Complete finite sign certificate.** The following table lists \((\alpha,\beta,\gamma)\) for every one of the exactly \(45\) unordered pairs, with \(F_{u,v}(t)=\alpha+\beta t+\gamma t^2\). Each entry follows by the explicit maximal-minor formula in Step 1 and the coefficient formulas in Step 2; the included `PAIR_CERTIFICATE.tsv` gives the same integer data in machine-readable form, and `verify.py` regenerates every entry from scratch using only integer arithmetic.

| First direction | Second direction | Constant | Linear | Quadratic |
|---|---|---:|---:|---:|
| \(e_1\) | \(e_2\) | 0 | 0 | 10 |
| \(e_1\) | \(e_3\) | 0 | 0 | 10 |
| \(e_1\) | \(e_4\) | 0 | 0 | 8 |
| \(e_1\) | \(d_{12}\) | 16 | 24 | 10 |
| \(e_1\) | \(d_{13}\) | 16 | 24 | 10 |
| \(e_1\) | \(d_{14}\) | 16 | 24 | 8 |
| \(e_1\) | \(d_{23}\) | 0 | 0 | 8 |
| \(e_1\) | \(d_{24}\) | 0 | 0 | 2 |
| \(e_1\) | \(d_{34}\) | 0 | 0 | 2 |
| \(e_2\) | \(e_3\) | 1 | 2 | 5 |
| \(e_2\) | \(e_4\) | 4 | 12 | 10 |
| \(e_2\) | \(d_{12}\) | 9 | 12 | 5 |
| \(e_2\) | \(d_{13}\) | 1 | 0 | 25 |
| \(e_2\) | \(d_{14}\) | 4 | 2 | 10 |
| \(e_2\) | \(d_{23}\) | 4 | 16 | 20 |
| \(e_2\) | \(d_{24}\) | 1 | 4 | 5 |
| \(e_2\) | \(d_{34}\) | 1 | 4 | 5 |
| \(e_3\) | \(e_4\) | 4 | 12 | 10 |
| \(e_3\) | \(d_{12}\) | 1 | 0 | 25 |
| \(e_3\) | \(d_{13}\) | 9 | 12 | 5 |
| \(e_3\) | \(d_{14}\) | 4 | 2 | 10 |
| \(e_3\) | \(d_{23}\) | 4 | 16 | 20 |
| \(e_3\) | \(d_{24}\) | 1 | 4 | 5 |
| \(e_3\) | \(d_{34}\) | 1 | 4 | 5 |
| \(e_4\) | \(d_{12}\) | 4 | 4 | 10 |
| \(e_4\) | \(d_{13}\) | 4 | 4 | 10 |
| \(e_4\) | \(d_{14}\) | 16 | 40 | 24 |
| \(e_4\) | \(d_{23}\) | 0 | 0 | 4 |
| \(e_4\) | \(d_{24}\) | 4 | 20 | 26 |
| \(e_4\) | \(d_{34}\) | 4 | 20 | 26 |
| \(d_{12}\) | \(d_{13}\) | 25 | 2 | 5 |
| \(d_{12}\) | \(d_{14}\) | 36 | 34 | 10 |
| \(d_{12}\) | \(d_{23}\) | 4 | 8 | 20 |
| \(d_{12}\) | \(d_{24}\) | 1 | 2 | 5 |
| \(d_{12}\) | \(d_{34}\) | 1 | 2 | 5 |
| \(d_{13}\) | \(d_{14}\) | 36 | 34 | 10 |
| \(d_{13}\) | \(d_{23}\) | 4 | 8 | 20 |
| \(d_{13}\) | \(d_{24}\) | 1 | 2 | 5 |
| \(d_{13}\) | \(d_{34}\) | 1 | 2 | 5 |
| \(d_{14}\) | \(d_{23}\) | 0 | -8 | 4 |
| \(d_{14}\) | \(d_{24}\) | 4 | 18 | 26 |
| \(d_{14}\) | \(d_{34}\) | 4 | 18 | 26 |
| \(d_{23}\) | \(d_{24}\) | 4 | 16 | 16 |
| \(d_{23}\) | \(d_{34}\) | 4 | 16 | 16 |
| \(d_{24}\) | \(d_{34}\) | 1 | 6 | 9 |

Inspection of this **complete** table, rather than a sample of parameter values, gives the sign classification. The exceptional row is \((0,-8,4)\), so \(F_{d_{14},d_{23}}(t)=4t(t-2)\). Every other row has \(\alpha\ge0\), \(\beta\ge0\), and \(\gamma>0\); hence its polynomial is strictly positive at every \(t>0\). Precisely eight rows have \(\alpha=0\), proving the equality count at \(t=0\). The exceptional row alone vanishes at \(t=2\) among the pairs when \(t>0\). Multiplication by positive \(sr\) does not change signs. This proves every assertion.

## Verification
The accompanying standalone `verify.py` uses the explicit list of ten four-dimensional integer vectors. It enumerates all \(\binom{10}{2}=45\) pairs, computes every determinant of every four-column sublist appearing in the four volume formulas at \(t=0\) and \(t=1\), builds their three polynomial coefficients using integer arithmetic, and checks each row against `PAIR_CERTIFICATE.tsv`. It also verifies \((a,b,c,q)=(4,8,4,8)\) at \(t=0\) and \((14,16,12,14)\) at \(t=1\) for the exceptional pair, the unique potentially negative coefficient pattern, and eight equality pairs at \(t=0\). No floating-point or random sampling is involved. Execute `python3 verify.py` with the TSV in the same directory. The exhaustive finite certificate is legitimate here because exactly \(45\) specified pairs occur; the claim for every real \(t,s,r\) follows algebraically from the affineness and polynomial sign argument, not an extrapolation from tests.

## Relationship to prior work
Skorupinski's 2026 work supplies the canonical six-vector zonotope and demonstrates the single violating pair \(\{d_{14},d_{23}\}\) at unit scale. A separately available research note gives its scalar scale phase diagram, including the factor \(4t(2-t)\), and another studies two independent components of the exceptional generator while **keeping the pair fixed**. The present classification does **not** claim those single-pair formulas as new: it proves that *no other pair among the full canonical set of ten elementary column directions violates the inequality*, for any positive segment lengths, together with the exact other-pair equality and strictness classification. The earlier single-pair calculations do not logically imply these other \(44\) signs.

Fradelizi and collaborators relate zonoid log-submodularity to Rayleigh properties of multiaffine zonotope volume polynomials. Their general positive theorem when dimension or codegree is at most three does not cover the eight-generator, four-dimensional cases here, whose codegree can be four. Averkov, von Dichter and Soprunov prove a different log-submodularity-type inequality for zonoids; that universal result is not the four-volume inequality whose exact directional defect is classified here. In this respect the complete sign graph is a local, explicit refinement rather than a new general zonoid inequality.

## Limitations
The classification is restricted to the ten specified elementary directions in four dimensions and to one fixed special generator scaled by a nonnegative parameter. The exact phase of the exceptional pair was already recorded; the additional conclusion is the complete pair classification. The integer table has been checked with a standalone deterministic verifier but has not undergone an independent mathematical audit. Relevant additional literature available only through abstracts may contain related enumerations; no claim of absolute historical priority is possible from search alone. Nothing here shows a general log-submodularity inequality for arbitrary segment directions or arbitrary zonoids.

## References
1. R. Skorupinski, *Zonoid volumes are not log-submodular*, arXiv:2608.07702v1, first publicly posted August 7, 2026, especially Sections 1--3.
2. *Exact scale phase diagram for a four-dimensional zonotope log-submodularity defect*, published mathematical research note, record `75844497da3f` (October 2026).
3. *Exact two-parameter directional phase diagram for a zonotope log-submodularity counterexample*, published mathematical research note, record `f4edcfe36776` (October 2026).
4. M. Fradelizi, A. Hubard, A. Manui, C. S. Ndiaye, S. Wang, A. Zvavitch, *Volume and Projection Inequalities I: Zonoids and Courtade's Conjecture*, arXiv:2608.12681v1, August 13, 2026.
5. G. Averkov, K. von Dichter, I. Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v2, October 2026.
