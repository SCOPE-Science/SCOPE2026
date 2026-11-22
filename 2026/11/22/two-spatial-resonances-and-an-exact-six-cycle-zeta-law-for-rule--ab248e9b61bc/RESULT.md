# Two spatial resonances and an exact six-cycle zeta law for Rule 22

## Finding

For every integer \(n\ge3\), let \(F_n\) denote synchronous elementary cellular automaton Rule 22 on the **labelled, oriented** binary cyclic ring of length \(n\). Let \(C_6(n)\) denote the number of **primitive temporal period-six orbits**, without identifying spatial rotations or reflections. Then the exact all-circumference classification is

\[
\boxed{C_6(n)=4\mathbf 1_{8\mid n}+\frac53\bigl(4^{n/10}+2\bigr)\mathbf 1_{10\mid n}.}
\]

The second summand is understood to be zero when \(10\nmid n\), so no fractional powers are needed. The formula yields an integer: when \(n=10k\), \(4^k+2\) is divisible by three. Equivalently, the number of configurations of *least* temporal period six is

\[
\boxed{P_6(n)=24\mathbf1_{8\mid n}+10\bigl(4^{n/10}+2\bigr)\mathbf1_{10\mid n}.}
\]

Thus primitive six-cycles exist **if and only if** the circumference is divisible by eight or by ten. These are two arithmetically distinct populations: the eight-site resonance contributes exactly four labelled temporal orbits for every multiple of eight, while the ten-site resonance contributes exponentially many as its multiplier grows. At simultaneous multiples of forty the contributions add. The spatial fixed-point zeta determinants satisfy the exact factorization

\[
\boxed{\frac{D_6(z)}{D_2(z)}=(1-z^8)^3(1-z^{10})^2(1-4z^{10}),\qquad D_p(z)=\det(I-zA_p),}
\]

where the finite transfer matrices \(A_p\) are defined below. Additionally, \(\operatorname{Fix}(F_n^3)=\operatorname{Fix}(F_n)\) for every \(n\ge3\); no primitive temporal three-cycles occur.

| Circumference \(n\) | 8 | 10 | 16 | 20 | 24 | 30 | 40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Primitive temporal six-orbit count \(C_6(n)\) | 4 | 10 | 4 | 30 | 4 | 110 | 434 |

## Assumptions and scope

Let \(x_i\in\{0,1\}\), where \(i\in\mathbb Z/n\mathbb Z\). The update is simultaneous and obeys
\[
(F_n(x))_i=\mathbf1_{\{x_{i-1}+x_i+x_{i+1}=1\}},
\]
where the sum is ordinary integer addition. This is elementary Rule 22, whose only active neighbourhoods are \(001,010,100\). A primitive temporal period-six orbit has exactly six distinct successive configurations, with return after six updates. Every distinct ring-site labelling is counted separately; no spatial or mirror quotient is taken. Transient attraction basins, other eventual periods and dynamics on infinite aperiodic spatial configurations are outside this claim.

## Proof

**1. Space-time transfer.** Fix any positive temporal height \(p\). Represent each site's cyclic time history as a binary word \(a=(a_0,\ldots,a_{p-1})\in\{0,1\}^p\), with indices modulo \(p\). Build the directed graph \(G_p\) whose vertices are ordered pairs \((a,b)\) of such words and whose edges \((a,b)\longrightarrow(b,c)\) are present exactly when, for every temporal index \(t\),
\[
 b_{t+1}=\mathbf1_{\{a_t+b_t+c_t=1\}}.
\]
Let \(A_p\) be the integer adjacency matrix. A closed directed walk of spatial length \(n\), anchored at site zero, reconstructs exactly one cyclic space-time diagram of temporal height \(p\). Its initial row is therefore fixed by \(F_n^p\). Conversely the entire time history of any fixed-by-\(p\) initial row uniquely supplies this walk. Hence, for **every** \(n\ge3\),
\[
 |\operatorname{Fix}(F_n^p)|=\operatorname{tr}(A_p^n).
\]
The graph contains \(2^{2p}\) vertices. Closed walks never pass outside directed cycle-containing strongly connected components, so their determinant contributions alone determine every trace.

**2. Full exact finite block reduction.** The attached standalone `verify_transfer.py` generates every edge directly from the eight Rule 22 neighbourhoods and performs an exhaustive strongly connected component decomposition. It computes each cyclic component's integer characteristic polynomial using trace counts and Newton's identities; all coefficients and the complete decompositions are asserted exactly. The cycle-containing component sizes are:

| Temporal height \(p\) | Cyclic component sizes |
|---:|---|
| 1 | \(2,1\) |
| 2 | \(4,2,1\) |
| 3 | \(2,1\) |
| 6 | \(60,8,8,8,4,2,1\) |

The cyclic height-six components of sizes four, two and one have characteristic polynomials \(t^4-1\), \(t^2-1\) and \(t-1\). Each size-eight component has characteristic polynomial \(t^8-1\). The size-sixty component has the exactly verified characteristic polynomial
\[
 t^{30}(t-1)^2(t+1)^2(t^5-2)(t^5+2)
 (t^4+t^3+t^2+t+1)^2
 (t^4-t^3+t^2-t+1)^2.
\]
Its thirty zero eigenvalues contribute no factor to \(\det(I-zA_6)\). The remaining factors simplify over the integers to
\[
(1-z^{10})^2(1-4z^{10}).
\]
Comparing with the small height-two blocks yields the exact polynomial identity
\[
D_6(z)=D_2(z)(1-z^8)^3(1-z^{10})^2(1-4z^{10}).
\]
Likewise, the size-two and size-one blocks at heights one and three have identical characteristic polynomials, establishing \(D_1(z)=D_3(z)\).

**3. Extract exact primitive temporal periods.** The identity of formal series
\[
-z\frac{d}{dz}\log\det(I-zA_p)=\sum_{n\ge1}\operatorname{tr}(A_p^n)z^n
\]
is valid over \(\mathbb Q[[z]]\) for every finite adjacency matrix. As the proper divisors of six are one, two and three and \(\operatorname{Fix}(F_n^3)=\operatorname{Fix}(F_n)\), the number of period-exactly-six states is \(|\operatorname{Fix}(F_n^6)|-|\operatorname{Fix}(F_n^2)|\). Therefore
\[
\begin{aligned}
\sum_{n\ge1}P_6(n)z^n
&=-z\frac d{dz}\log\frac{D_6(z)}{D_2(z)}\\
&=\frac{24z^8}{1-z^8}+\frac{20z^{10}}{1-z^{10}}+\frac{40z^{10}}{1-4z^{10}}.
\end{aligned}
\]
For multiples of ten, the coefficient is \(20+40\cdot4^{n/10-1}=10(4^{n/10}+2)\). Dividing by six gives the number of temporal orbits. The coefficient series is nonnegative and has support exactly on multiples of eight or ten, proving the necessity, sufficiency and the two growth mechanisms for **all** ring lengths, not just those tested computationally.

## Verification

`verify_transfer.py` reconstructs all four complete time-height transfer graphs, including the height-six graph with \(4,096\) vertices and \(4,097\) edges. It exactly checks every cyclic block's characteristic polynomial, each nonzero determinant factor and the full sixth-versus-second determinant identity. The finite verification covers **all** possible local temporal-column states, so the transfer argument proves an all-length formula rather than extrapolating from a sample. Execute `python3 verify_transfer.py` using Python 3's standard library.

Independently, `verify_direct.py` computes the actual Rule 22 map on every one of the \(2^n\) indexed binary states for every \(3\le n\le20\); it checks the six-return, two-return, three-return and one-return counts directly against the claimed formula. Execute `python3 verify_direct.py`. This is a cross-check, **not** the infinite-length proof. No external packages or files are needed.

## Relationship to prior work

McIntosh's earlier Rule 22 analysis already describes six-step periodic space-time patterns on spatial rings of length ten and related travelling wave patterns. Martínez and coauthors explicitly display temporal period-six examples on rings of length eight and ten and discuss extended de Bruijn graphs; these examples are **not** claimed as discoveries here. The proposed addition is the exact labelled temporal six-orbit census at **every** circumference, its simultaneous eight/ten divisibility criterion and bounded-versus-exponential mode decomposition.

Existing posted Rule 22 classifications of primitive temporal **four** and **five** orbits use similar transfer methods but their returned-time constraints and renewal denominators do not imply the sixth-return determinant, which has separate factors at lengths eight and ten. A known exact primitive temporal six-census for **Rule 54** involves a different local truth table; it does not entail the Rule 22 law. General foundational studies of the exactly-one cellular automaton primarily treat finite seeds on the infinite line. A finite table of small-ring cycles cannot certify this formula at arbitrarily large lengths.

## Limitations

The proof is a finite exact combinatorial certificate for the specified Rule 22 labelled ring dynamics and has not received independent external audit. It does not compute attraction-basin sizes, the entire temporal period spectrum or any dynamics for other cellular automata. The historical Rule 22 literature already identifies the smallest eight- and ten-site examples; novelty is confined to the **all-length exact census** and structural factorization. A full monograph-level comparison of all historical cycle tables has not been completed, and potential unindexed general formulas remain a priority risk.

## References

1. H. V. McIntosh, *Linear Cellular Automata*, archival manuscript, sections 3.6 and 4.6 and figure 4.7 (historical manuscript dating does not establish its public release date), https://delta.cs.cinvestav.mx/~mcintosh/cellularautomata/Papers_files/lcau.pdf .
2. G. J. Martínez, A. Adamatzky, R. Hoffmann, D. Désérable and I. Zelinka, *On Patterns and Dynamics of Rule 22 Cellular Automaton*, *Complex Systems* **28** (2019), 125–174, https://arxiv.org/abs/2005.01480 .
3. J. Gravner and D. Griffeath, *The One-Dimensional Exactly 1 Cellular Automaton: Replication, Periodicity, and Chaos from Finite Seeds*, *Journal of Statistical Physics*, online 2010-12-10, https://link.springer.com/article/10.1007/s10955-010-0103-9 .
4. *Fourth-period reentrance and a renewal zeta for cyclic Rule 22*, online mathematical research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-fourth-period-reentrance-and-a-renewal-zeta-for-cyclic-rule-22--cba04b56228d/RESULT.md .
5. *A sharp 54-site gap and a renewal zeta for temporal five-cycles of Rule 22*, online mathematical research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-a-sharp-54-site-gap-and-a-renewal-zeta-for-temporal-five-cycles--34a570aa8e2a/RESULT.md .
