# Exact skip-transposition sphere spectrum of proper ternary words

## Finding
For every integer \(n\ge2\), a *proper ternary word* is a word \(w=w_1\cdots w_n\) over \(\{0,1,2\}\) with \(w_i\ne w_{i+1}\) for all \(1\le i<n\). A legal *skip transposition* exchanges the symbols at positions \(i\) and \(i+2\), for some \(1\le i\le n-2\), and must produce a **different** proper word. Write \(D(w)\) for the number of distinct legal outputs. Let \(N_{m,k}\) count the proper words of length \(m+1\) having \(D(w)=k\).

The complete degree enumerator is the rational formal power series
\[
\sum_{m\ge1}\sum_{k\ge0}N_{m,k}z^m u^k
=\frac{6A(z,u)}{1-A(z,u)},\qquad
A(z,u)=z+uz^2+\frac{z^3}{1-z}.
\]
For every \(m\ge1\), the attainable degrees are exactly \(0,1,\ldots,\lfloor m/2\rfloor\), and the number attaining the maximum is
\[
N_{m,\lfloor m/2\rfloor}=\begin{cases}
6,&m\text{ even},\\
3(m+1),&m\text{ odd}.
\end{cases}
\]
In particular the frozen-center (degree zero) enumerator is
\[
\sum_{m\ge1}N_{m,0}z^m=\frac{6(z-z^2+z^3)}{1-2z+z^2-z^3}.
\]
For \(W_m\) uniform among the \(3\cdot2^m\) proper words of length \(m+1\),
\[
\mathbb E D(W_m)=\frac{m+1}{8}\quad(m\ge3),\qquad
\operatorname{Var}D(W_m)=\frac{7m+1}{64}\quad(m\ge5),
\]
and
\[
\frac{D(W_m)-m/8}{\sqrt{7m/64}}\Longrightarrow\mathcal N(0,1).
\]
Thus the skip-transposition graph has exactly \(3n2^{n-5}\) undirected edges for \(n\ge4\). Its proportion of frozen vertices is exponentially small, with rate \((\lambda/2)^m\), where \(\lambda\) is the largest real root of \(\lambda^3-2\lambda^2+\lambda-1=0\).

## Assumptions and scope
The alphabet is the **labeled, three-symbol** cyclic group \(\mathbb Z/3\mathbb Z\); positions are **linear**, not circular, and indexed. Only one exchange of positions exactly two apart is allowed; there is no intervening rearrangement, no substitution and no swap of adjacent positions. The output is required to remain proper. Spheres are sets of distinct **nonidentical** outputs (the original center is not counted). No prescribed composition is imposed. The formulas are for every integer \(n\ge2\); the stated moment formulas have their indicated lower-length bounds. The asymptotic statement is for \(m\to\infty\).

## Proof
**Step 1: sign bijection.** Every proper ternary word is uniquely specified by its first letter and its \(m=n-1\) signs \(s_i=w_{i+1}-w_i\pmod3\), each in \(\{+1,-1\}\). Conversely, every choice of first letter and signs gives one proper word, so there are exactly \(3\cdot2^m\) words and the signs are independent fair bits under uniform sampling.

**Step 2: characterization of one legal exchange.** At positions \(i,i+1,i+2\), swapping endpoints changes the word precisely when \(s_i=s_{i+1}\); if the two signs differ, the endpoints already have equal letters. When they agree, the swapped triple has both adjacent pairs unequal. Its new left endpoint clashes with \(w_{i-1}\), when present, precisely if \(s_{i-1}=s_i\), and its new right endpoint clashes with \(w_{i+3}\), when present, precisely if \(s_{i+2}=s_i\). Therefore the exchange is legal exactly when \(s_i,s_{i+1}\) form an entire maximal constant-sign run of length exactly two. Exchanges at different positions modify different pairs of coordinates, so they give distinct outputs. Consequently,
\[
D(w)=\#\{\text{maximal constant-sign runs of length exactly }2\text{ in }(s_1,\ldots,s_m)\}.
\]
This identity includes both endpoints; a run of length two at either end remains maximal without requiring a non-existent outside sign.

**Step 3: enumerator and extremizers.** A nonempty binary sign sequence has a unique ordered composition of its length into maximal run lengths, and its first run sign has two choices. Each maximal run has weight \(z^j\), with an additional factor \(u\) exactly when its length \(j\) is two. The single-run generating function is \(A(z,u)=z+uz^2+z^3/(1-z)\); summing one or more runs and three starting letters gives \(6A/(1-A)\). At most \(\lfloor m/2\rfloor\) disjoint length-two runs fit, and all intermediate degrees occur by taking the required number of parts of length two and using length-one parts for the rest. When \(m\) is even, the unique maximal-degree composition consists solely of twos. When \(m\) is odd, it consists of twos and exactly one one, in \((m+1)/2\) possible positions. Multiplying by six choices of initial letter and sign gives the maximal-degree census. Substituting \(u=0\) and clearing denominators gives the frozen enumerator.

**Step 4: exact moments.** Differentiate the rational generating function with respect to \(u\), then set \(u=1\). With \(F(z,u)=6A(z,u)/(1-A(z,u))\),
\[
F_u(z,1)=\frac{6z^2(1-z)^2}{(1-2z)^2},\qquad
F_{uu}(z,1)=\frac{12z^4(1-z)^3}{(1-2z)^3}.
\]
Dividing coefficients of \(z^m\) by \(3\cdot2^m\) yields \(\mathbb E D=(m+1)/8\) for \(m\ge3\) and \(\mathbb E[D(D-1)]=(m-2)(m+3)/64\) for \(m\ge5\). The latter, plus \(\mathbb E D\), gives variance \((7m+1)/64\). The sum of all degrees equals \(3\cdot2^m(m+1)/8\), and half of this gives the edge formula for \(n=m+1\ge4\).

**Step 5: Gaussian limit.** Except for at most two boundary runs, \(D\) is a sum of the indicators that four consecutive signs realize \(-++-\) or \(+--+\). These stationary bounded indicators are \(3\)-dependent, each has mean \(1/8\), and their covariances at lags one, two, three are respectively \(-1/64,+1/64,0\). The limiting variance per sign is therefore \(7/64\). The classical central limit theorem for bounded finite-dependent stationary sequences applies; the boundary indicators contribute only a bounded error. The exact mean differs from \(m/8\) by a constant, irrelevant to the normal limit.

**Step 6: frozen exponential rate.** If \(\lambda=1/\rho\), the denominator \(1-2z+z^2-z^3\) vanishes precisely when \(\lambda^3-2\lambda^2+\lambda-1=0\). The cubic has one real root \(1<\lambda<2\): its derivative is \((3\lambda-1)(\lambda-1)\), and the local extremum values of the cubic are both negative. Its two nonreal roots have modulus \(\lambda^{-1/2}<1\), since the product of the three roots is one. Thus the positive pole \(\rho=\lambda^{-1}\) is simple and strictly smaller in modulus than the other poles; its numerator \(6\rho(1-\rho+\rho^2)\) is nonzero. Rational-function coefficient extraction gives \(N_{m,0}=\Theta(\lambda^m)\). Since there are \(3\cdot2^m\) proper words, the frozen fraction decays exponentially.

## Verification
The included standard-library Python program `checker.py` implements two distinct tests: direct manipulation of every proper ternary word and the run-sign formula, then an independent integer composition recurrence for the exact degree distribution. It checks all \(24{,}570\) proper words of lengths \(2\) through \(13\), all candidate swaps, every coefficient at those lengths, extremal counts, and the moment formulas where applicable. The direct-enumeration checks are finite corroboration; the proof above, not enumeration, establishes the all-length statements. Execute `python checker.py`.

Some frozen counts, by length \(n=2,3,\ldots,13\), are \(6,6,12,24,42,72,126,222,390,684,1200,2106\).

## Relationship to prior work
Adamson, Flaherty, Potapov and Spirakis analyze arbitrary two-position transpositions within full fixed-composition word-permutation graphs; their graph retains words that would violate an adjacency restriction and permits arbitrary position separations. Sawada, Williams and Wong study binary flip-swap languages, involving a different restricted operation. Fuchs and coauthors study exchanges at **adjacent** vertices while maintaining a proper coloring, especially path-coloring reachability. None of those specified operations yields the present *distance-two-only, proper-output* neighborhood, whose degree is controlled by maximal two-runs of ternary signs. In particular, an adjacent-swap degree enumerator does not imply this skip-swap degree enumerator: the proper word `02010` has no legal adjacent swap but one legal skip swap, whereas `0120` has legal adjacent swaps but no legal skip swap. Published results on nonbinary three-symbol permutation bursts allow broader output languages and therefore do not directly enumerate proper-output skip swaps.

## Limitations
The alphabet-three cyclic sign bijection is essential; no generalization to arbitrary alphabet size is proved. The result does not classify graph components or optimal error-correcting codes, does not address repeated swaps, and does not imply any communication guarantee for noisy channels. Related or equivalent work under another terminology may exist; literature searching alone cannot establish absolute priority. The finite checker is not an independent mathematical audit.

## References
- D. Adamson, N. Flaherty, I. Potapov, P. G. Spirakis, *Structural and Combinatorial Properties of 2-swap Word Permutation Graphs*, arXiv:2307.01648v1 (2023), https://arxiv.org/abs/2307.01648.
- J. Sawada, A. Williams, D. Wong, *Inside the Binary Reflected Gray Code: Flip-Swap Languages in 2-Gray Code Order*, arXiv:2105.03556v1 (2021), https://arxiv.org/abs/2105.03556.
- J. Fuchs, R. Saito, T. Suga, T. Suzuki, Y. Tamura, *Coloring Reconfiguration under Color Swapping*, arXiv:2511.06473v1 (2025), https://arxiv.org/abs/2511.06473.
- K. Yamanaka et al., *Swapping Colored Tokens on Graphs*, Theoretical Computer Science 729 (2018), https://doi.org/10.1016/j.tcs.2018.03.016.
