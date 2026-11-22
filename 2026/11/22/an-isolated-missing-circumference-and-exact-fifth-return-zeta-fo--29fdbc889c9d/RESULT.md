# An isolated missing circumference and exact fifth-return zeta for Rule 73

## Finding

Consider the synchronous elementary binary cellular automaton Rule 73 on an indexed cyclic ring of length \(n\ge3\). Write \(F_n\) for one global update, and let \(c_n\) be the number of distinct **primitive temporal five-cycle orbits** of \(F_n\), identifying the five time phases of a cycle but **not** identifying spatial translations. Then

\[
\boxed{c_n>0\quad\Longleftrightarrow\quad n\in\{11,12\}\cup\{14,15,16,\ldots\}.}
\]

In particular, primitive five-cycles first appear at circumferences \(11\) and \(12\), disappear at \(13\), and reappear permanently at \(14\). Their exact census at **every** circumference is the following rational-logarithmic derivative:

\[
\boxed{\sum_{n\ge1}c_nz^n=\frac z5\frac{d}{dz}\log\frac{D_1(z)}{D_5(z)}},
\]

where

\[
\begin{aligned}
D_1(z)&=1-z^3-z^4,\\
A(z)&=1+z^8+z^9-z^{16}-2z^{17}-z^{18},\\
B(z)&=1-z^3-z^4-2z^8-2z^9-3z^{11}-z^{12}+2z^{13},\\
D_5(z)&=A(z)^2B(z).
\end{aligned}
\]

The series formula also holds formally at circumferences \(1,2\) under the periodic-neighborhood convention. If \(\lambda_5\) is the Perron eigenvalue of the explicitly specified \(49\)-state fifth-return transfer matrix below, then

\[
\boxed{c_n\sim\frac{\lambda_5^n}{5},\qquad
\lambda_5=1.378913380008526\ldots.}
\]

In contrast to the shorter temporal-three sector, the number of primitive five-cycles grows with the strictly smaller exponential base: the temporal-three transfer matrix has spectral radius greater than \(3/2\), whereas \(\lambda_5<7/5\). This comparison concerns uniform orbit populations, not attraction basins or evolution from uniformly random initial words.

## Assumptions and scope

The local function \(f:\{0,1\}^3\to\{0,1\}\) has output \(1\) exactly on input triples `000`, `011`, and `110`. Thus \((F_n(x))_i=f(x_{i-1},x_i,x_{i+1})\), with indices modulo \(n\). Ring positions are indexed, so distinct cyclic translations count separately unless they are identical states. A primitive temporal five-cycle is a set of five distinct words \(\{x,F_n(x),F_n^2(x),F_n^3(x),F_n^4(x)\}\) with \(F_n^5(x)=x\). Since five is prime, every word fixed by the fifth update is either fixed by one update or has least temporal period five. No assertion concerns transients, basins, or longer temporal periods.

## Proof

**1. The finite space-time transfer.** For an integer \(p\ge1\), write a temporal history as \(a=(a_0,\ldots,a_{p-1})\in\{0,1\}^p\). Form the directed graph \(G_p\) with vertices ordered pairs of such histories. There is an edge

\[
(a,b)\longrightarrow (b,c)
\quad\Longleftrightarrow\quad
b_{t+1\bmod p}=f(a_t,b_t,c_t)
\ \text{for every }t\in\{0,\ldots,p-1\}.
\]

This is a finite graph defined entirely by the eight-entry local truth table. An indexed binary ring word fixed by \(F_n^p\) gives \(n\) consecutive temporal columns and hence a length-\(n\) closed walk in \(G_p\). Conversely, a length-\(n\) closed walk determines a unique periodic space-time cylinder, with its time-zero row an indexed word fixed by \(F_n^p\). The constructions are inverse, including when a word has smaller spatial period. Therefore, with \(M_p\) the adjacency matrix of \(G_p\),

\[
|\operatorname{Fix}(F_n^p)|=\operatorname{tr}(M_p^n).
\]

**2. Exact determinant calculation.** Applying the definition to \(p=1\) leaves a single nontrivial recurrent strongly connected component on four vertices. For \(p=5\), the sole directed-cycle-bearing strongly connected component has \(49\) vertices and \(70\) edges. All other vertices lie on no closed walk and contribute neither to traces nor to determinants. Let \(A_1,A_5\) be adjacency matrices on these recurrent components. Direct integer computation from the vertex and edge predicates gives

\[
\det(I-zA_1)=D_1(z),\qquad\det(I-zA_5)=D_5(z).
\]

For reproducibility, `verification/transfer.py` reconstructs every graph from the local truth table, finds the recurrent components by two-pass reachability, and computes all coefficients of these exact determinants by Newton's identities

\[
d_0=1,\qquad
k d_k=-\sum_{j=1}^{k}d_{k-j}\operatorname{tr}(A^j)
\quad (1\le k\le\dim A).
\]

The trace sums are calculated by exact integer walk counts; thus this checks all \(49\) determinant coefficients, not a fit to sample ring sizes. By the matrix identity

\[
-\log\det(I-zA)=\sum_{n\ge1}\frac{\operatorname{tr}(A^n)}n z^n,
\]

and because five is prime,

\[
c_n=\frac{\operatorname{tr}(A_5^n)-\operatorname{tr}(A_1^n)}5.
\]

The displayed generating function follows for every \(n\), with the divisor five accounting for the five temporal phases of each orbit.

**3. Sharp existence spectrum.** Integer traces from the two exact matrices yield \(c_n=0\) at \(n=3,\ldots,10\) and \(n=13\). These finite exclusions are also checked independently by exhaustive simulation of every one of the \(2^n\) possible binary initial words for each of those circumferences, applying the local rule exactly five times. Two actual primitive five-cycle seeds (time-zero words written in site order) are

```
n=11: 11000000000
n=12: 110000000000
```

Their five temporal phases are directly verified in `verification/direct.py`. Both contain, at consecutive spatial positions, the **constant time histories** \(1^5\) and \(0^5\), so their space-time closed walks visit the pair vertex \((1^5,0^5)\) in \(G_5\). At this vertex the time-constant portion of \(G_5\) contains two return paths, of lengths three and four, obtained from the stationary history columns

```
length 3: 1 0 1 1 0
length 4: 1 0 0 1 1 0
```

The first and last two entries in each line agree, and each intervening triple satisfies \(f(a,b,c)=b\). Inserting either closed path at the displayed vertex augments any existing period-five space-time cylinder by three or four sites while leaving at least one genuinely time-varying column unchanged. The resulting ring still has **least** temporal period five. Hence the two seeds produce primitive five-cycles at every circumference

\[
n\in\{11+3a+4b,\ 12+3a+4b:a,b\in\mathbb Z_{\ge0}\}
=\{11,12\}\cup\{n\in\mathbb Z:n\ge14\}.
\]

Together with the finite exclusions, this proves the if-and-only-if spectrum for all ring lengths, with no extrapolation from finite enumeration.

**4. Exponential growth and period contrast.** The unique \(49\)-vertex recurrent component is strongly connected. It contains the embedded time-constant closed walks of lengths three and four described above, so its period is one. Perron–Frobenius theory gives a simple positive eigenvalue \(\lambda_5\) strictly larger in modulus than all its other eigenvalues and

\[
\operatorname{tr}(A_5^n)=\lambda_5^n+o(\lambda_5^n).
\]

The four-vertex fixed-point matrix has characteristic polynomial \(x^4-x-1\), whose positive Perron root is below \(13/10\). Integer Collatz–Wielandt bounds computed on the actual \(49\)-vertex graph place \(\lambda_5\) strictly between \(1.37890\) and \(1.37893\), so fixed configurations are exponentially negligible in the five-return trace. This proves the displayed asymptotic. The numerical value is the Perron eigenvalue of the exact matrix, equivalently the real root near \(1.37891338\) of the degree-\(13\) reciprocal polynomial of \(B\).

The separately generated temporal-three transfer has a recurrent \(19\)-state strongly connected component. Exact integer Collatz–Wielandt inequalities using its \(50\)-th iterate of the all-ones vector show that its spectral radius exceeds \(3/2\); analogous \(100\)-step inequalities on the fifth-return component show \(\lambda_5<7/5\). Thus the temporal-three orbit population has strictly larger exponential growth than the temporal-five population. This comparison is independent of any earlier numerical orbit census.

## Verification

Run `python verification/transfer.py` and `python verification/direct.py` from this directory with a standard Python interpreter. The first program reconstructs the full temporal-history graphs for periods one, three and five, identifies their recurrent components, reproduces the factored determinant coefficient by coefficient using integer Newton identities, and calculates all primitive five-cycle populations through circumference \(55\). It also proves the stated strict spectral separation by integer positive-vector inequalities, without a floating-point sign decision. The second program independently updates every possible binary ring state at lengths three through seventeen and checks the exact orbit counts, the two period-five witnesses and the admissible three- and four-edge stationary return paths. Their supplied `.out` files are recorded outputs; correctness for unbounded length follows from the graph bijection, exact determinant calculation, and closed-path insertion argument, **not** from the test range alone.

Selected exact primitive five-cycle orbit counts are

| \(n\) | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 20 | 30 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(c_n\) | 11 | 12 | 0 | 14 | 30 | 32 | 51 | 72 | 120 | 3150 |

## Relationship to prior work

Jiang and Qin (2011) had already exhibited a period-five **finite vertical-map string** for elementary Rule 73. This establishes that period-five behavior was known, and no novelty is claimed for its mere existence. Their object is a finite string between fixed walls, not the complete set of indexed periodic-ring lengths, exact all-length cycle counts, or a spatial zeta. Schüle and Stoop (2011) classified Rule 73's topological-dynamics type, without these ring enumerations. Sutner's *Linear Cellular Automata and Automaticity*, section 3.1, reports the temporal-**three** ring existence spectrum and finite counts, not the temporal-five formulas. Stricker (2023) studies the **maximum** cycle length on finite rings and presents numerical classes, not the count at each fixed temporal period. Kang (2014) investigates a **long-distance** Rule-73 neighborhood that is different from the nearest-neighbor update used here.

Existing publicly accessible exact Rule-73 studies of temporal **two** periods, temporal-three space-time occupation, and one-step images give different invariants and do not imply the fifth-return generating function or the missing-circumference classification. The symmetry-equivalent elementary Rule 109 has the same cycle census under bit complement and was included in the equivalence comparison; the result is not claimed as a different finding for Rule 109. Existing transfer-automaton techniques are standard prior methodology; the exact fifth-return factorization, sharp isolated absence at length thirteen, and all-length constructive spectrum are the claims here.

## Limitations

This theorem concerns the labeled finite-ring primitive temporal-five sector only. It neither classifies all possible temporal periods nor determines eventual attractor basins or average transient times. The asymptotic is an exact-orbit-population result, not a statistical law under random initialization. While the explicitly compared primary sources and prior records do not give an equivalent theorem, inaccessible, unpublished, or unindexed earlier statements may exist. Independent external mathematical review has not been performed.

## References

1. J. Zhisong and Q. Dakang, *The Fixed String of Elementary Cellular Automata*, *Complex Systems* **19** (2011), 243–267, especially p. 257 (previously known period-five Rule-73 finite string). https://doi.org/10.25088/ComplexSystems.19.3.243 ; https://content.wolfram.com/sites/13/2019/03/19-3-4.pdf.
2. M. Schüle and R. Stoop, *A Full Computation-relevant Topological Dynamics Classification of Elementary Cellular Automata*, arXiv:1107.2080, first submitted 2011-07-11. https://arxiv.org/abs/1107.2080 ; https://ar5iv.labs.arxiv.org/html/1107.2080.
3. K. Sutner, *Linear Cellular Automata and Automaticity*, section 3.1 (Rule-73 temporal-three spectrum). https://www.cs.cmu.edu/~sutner/papers/sutner-ca-automaticity.pdf.
4. H.-P. Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, *Complex Systems* **32** (2023), 229–251. https://doi.org/10.25088/ComplexSystems.32.3.229 ; https://content.wolfram.com/sites/13/2024/01/32-3-1.pdf.
5. L. Kang, *Complex Behavior in Long-Distance Cellular Automata*, *Complex Systems* **23** (2014), 93–119. https://doi.org/10.25088/ComplexSystems.23.2.93 ; https://wpmedia.wolfram.com/uploads/sites/13/2018/12/23-2-1.pdf.
6. *Rule 73: exact temporal-two zeta and an exponential oscillation–equilibrium gap* (publicly available mathematical result, 2026-11-17). https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-rule-73-exact-temporal-two-zeta-and-an-exponential-oscillation-e--91ecce9dc622.
7. *Exact space-time occupation law and Gaussian concentration in Rule 73 three-cycles* (publicly available mathematical result, 2026-11-17). https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-space-time-occupation-law-and-gaussian-concentration-in-ru--786af882d163.
8. *Exact cyclic one-step image series of elementary cellular automaton Rule 73* (publicly available mathematical result, 2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-one-step-image-series-of-elementary-cellular-automa--4412da3b7a44.
