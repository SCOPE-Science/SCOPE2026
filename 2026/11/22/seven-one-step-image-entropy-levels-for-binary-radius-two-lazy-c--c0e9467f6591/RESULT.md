# Seven one-step image-entropy levels for binary radius-two lazy cellular automata

## Finding
Let \(A=\{0,1\}\). A *lazy radius-two rule* changes the central symbol in exactly one of the 32 five-bit neighborhoods and otherwise leaves it unchanged. Write \(F:A^{\mathbb Z}\to A^{\mathbb Z}\) for its synchronous map, \(Y=F(A^{\mathbb Z})\) for its one-step spatial image, and \(Z=\operatorname{Fix}(F)\) for its fixed-point subshift. Entropies below are topological entropies of the spatial shift, not of temporal iteration.

**The 32 rules realize exactly seven image entropies.** With the writing symbol fixed to one, encode an active neighborhood with center zero by
\[
(a,b,0,d,e)\quad\longmapsto\quad p=a+2b+4d+8e\in\{0,\ldots,15\}.
\]
The table gives *all* 16 such rule codes. Each occurs twice among the 32 rules, since exchanging zero and one conjugates the two writing-symbol cases. The exact Perron polynomial for every class is in `spectral_classes.csv` and reproduced in the table below; the Perron root \(\lambda\) is its unique root in the indicated rational interval, with endpoints divided by \(10^9\).

| Class | Codes \(p\) (write one) | Number among 32 | Perron polynomial in \(t\) | Root interval numerators | Approximate \(\lambda\) |
|---|---|---:|---|---|---:|
| C | 2,4,9,11,13 | 10 | \(t^5-2t^4+t-1\) | 1933184981, 1933184982 | 1.9331849819 |
| E | 5,10 | 4 | \(t^5-2t^4+t^2-2t+1\) | 1937629450, 1937629451 | 1.9376294502 |
| G | 15 | 2 | \(t^5-2t^4+t^2-t-1\) | 1941713034, 1941713035 | 1.9417130343 |
| F | 6 | 2 | \(t^5-2t^4+t^3-2t^2+t-1\) | 1947891872, 1947891873 | 1.9478918727 |
| B | 1,7,8,14 | 8 | \(t^7-2t^6+t^2-1\) | 1948935746, 1948935747 | 1.9489357463 |
| A | 0 | 2 | \(t^5-t^4-t^3-t^2-t-1\) | 1965948236, 1965948237 | 1.9659482366 |
| D | 3,12 | 4 | \(t^6-2t^5+t-1\) | 1967168212, 1967168213 | 1.9671682128 |

In every case \(h_{\mathrm{top}}(Y)=\log\lambda\). Exactly 12 of the 32 maps are non-idempotent: those in classes B and D. All twelve have the **same fixed-point entropy** \(h_{\mathrm{top}}(Z)=\log\delta\), where \(\delta\) is the unique root in \((1927561975/10^9,1927561976/10^9)\) of
\[
\delta^4-\delta^3-\delta^2-\delta-1=0.
\]
Their one-step image entropy is **strictly larger**. There are precisely two entropy gaps:
\[
 h_{\mathrm{top}}(Y)-h_{\mathrm{top}}(Z)=
 \begin{cases}
 \log(\lambda_B/\delta)\approx0.0110274732,&\text{8 maps in B},\\
 \log(\lambda_D/\delta)\approx0.0203390740,&\text{4 maps in D}.
 \end{cases}
\]
The other 20 lazy rules are idempotent, so their image and fixed-point subshifts coincide.

## Assumptions and scope
A five-neighbor pattern reads coordinates \(i-2,i-1,i,i+1,i+2\) on the **two-sided full binary shift**. For code \(p\), the local rule with writing symbol one is
\[
 f_p(a,b,c,d,e)=c\lor\bigl((c=0)\land(a+2b+4d+8e=p)\bigr).
\]
Here logical notation denotes an output bit. Every assignment of the four neighboring bits, together with the central zero, gives exactly one distinct rule. The 16 rules writing zero are obtained by complementing all input and output bits (their active neighbor codes become \(15-p\)). All statements about counts are for labeled rules, not symmetry classes. Entropy uses natural logarithms; no stochastic choice, finite ring restriction, or temporal entropy interpretation is involved.

## Proof
**1. A complete labeled input graph.** Represent the four consecutive input bits \((a,b,c,d)\) by the state \(s=8a+4b+2c+d\), for \(0\le s<16\). Appending \(e\in\{0,1\}\) moves to \(s'=(2s+e)\bmod16\), with edge label \(f_p(a,b,c,d,e)\). Every output word of length \(n\) is realized if and only if it labels a path of length \(n\) in this graph: the forward direction is local, and any finite input path extends to a bi-infinite binary input.

**2. Determinize without losing word counts.** For any subset \(S\) of the sixteen input states and output symbol \(u\), let \(\Delta_p(S,u)\) comprise all heads of \(u\)-labeled edges starting in \(S\). Start with the full set of sixteen states. Visit every reachable nonempty subset by applying both output symbols; represent each as a sixteen-bit integer. The exact computation produces between 11 and 14 reachable nonempty subsets for each \(p\), as recorded in `spectral_classes.csv`. Empty subsets reject a word and are excluded. All nonempty subsets accept. Let \(M_p\) be the resulting nonnegative integer adjacency matrix: the entry \((S,T)\) counts the output symbols with \(\Delta_p(S,u)=T\). With \(v\) the initial-state row and \(\mathbf1\) the all-ones column, the exact number of different output words is
\[
 a_p(n)=vM_p^n\mathbf1\qquad(n\ge0).
\]
All nonempty states are reachable, and they all allow arbitrarily long forward extensions. Perron–Frobenius theory and finite-matrix path growth therefore give \(\lim_{n\to\infty}a_p(n)^{1/n}=\rho(M_p)\). The row sums are at most two, so \(\rho(M_p)\le2\).

**3. Exact exhaustive spectrum.** For every one of the 16 codes, construct \(M_p\) from the stated finite formula and compute its characteristic polynomial over the integers. The accompanying `verify.py` checks that the asserted class polynomial divides this characteristic polynomial. Exact Sturm root counting proves that the full characteristic polynomial has exactly one real root in the claimed rational interval, and no real root from its upper endpoint to 2; also 2 itself is not a root. A nonnegative matrix has a nonnegative real Perron eigenvalue, so the isolated root is \(\rho(M_p)\). The seven intervals are disjoint. This proves exactly seven levels, their strict ordering, and the full population counts, without extrapolating finite experiments to infinite words.

**4. Fixed points and non-idempotence.** Since the local map modifies precisely one five-bit pattern \(p\), a configuration is fixed exactly when it avoids that pattern at every spatial translate. This is a single-forbidden-word finite-type shift. A separate exact nine-input-bit comparison of \(F_p^2\) and \(F_p\), sufficient because the radius is two, finds non-idempotence exactly at \(p\in\{1,3,7,8,12,14\}\). The fixed-point adjacency matrix in these six cases has characteristic polynomial
\[
 t^{11}(t-1)(t^4-t^3-t^2-t-1).
\]
The fixed-point Perron root is \(\delta\), certified by exact root isolation. The intervals for \(\lambda_B\) and \(\lambda_D\) lie strictly above the interval for \(\delta\). For all other codes, \(F_p^2=F_p\) on every configuration, so \(Y=Z\). Bit complement transfers every result to the other 16 maps.

## Verification
The package includes `verify.py` (Python 3 with SymPy), `verify_direct.c` (standard C99), `spectral_classes.csv`, and `word_counts.csv`. In a directory containing these files run:

```
python3 verify.py
cc -std=c99 -O2 verify_direct.c -o verify_direct
./verify_direct word_counts.csv
```

The Python program constructs **all** reachable subset graphs, their exact characteristic polynomials and Sturm intervals, verifies both CSV catalogs, checks all 16 idempotence decisions from all possible nine-bit input neighborhoods, derives the common fixed-point polynomial for the six non-idempotent rules, and directly enumerates words through length nine. The C program independently enumerates all finite input blocks and checks 176 counts (16 codes, lengths zero through ten) without a subset automaton. Both programs passed on the packaged files. The exact finite-state path identity, not these bounded word-count cross-checks alone, proves the infinite-length entropy statement.

## Relationship to prior work
Alcalá-Arroyo, Castillo-Ramirez, Magaña-Chávez and de los Santos Baños (2026) give general **idempotence** criteria for lazy cellular automata, not the image-entropy levels. Castillo-Ramirez, Magaña-Chavez and de los Santos Baños (2024 preprint) establish the single-forbidden-word fixed-point description and dynamical dichotomy for interval neighborhoods; consequently the fixed-point part of the present calculation and the image entropies of the 20 idempotent rules are applications of known structural results, **not claimed as independent innovations**. Alcalá-Arroyo and Castillo-Ramirez (2025 preprint) study orders of lazy maps, not entropy of their first images. The published 256-rule elementary image-entropy census treats radius one, so it does not contain any of the sixteen distinct radius-two neighborhood rules here. The distinct contributions claimed are the **evaluated exact complete radius-two image spectrum** and, in particular, the two strict non-idempotent image-versus-fixed entropy gaps with their sharp populations.

## Limitations
This result addresses one synchronous update on the entire bilateral binary full shift. It does not determine subsequent image filtrations, limit sets, periodic-ring image counts, or temporal dynamical entropy. The detailed polynomial census is a finite exact computation reproducible using SymPy; the supporting C program tests shorter words independently but does not itself prove the spectral root isolation. Examination of identified literature and indexed records does not establish exhaustive historical priority; equivalent unindexed radius-two tables remain a residual risk. Independent mathematical audit has not been performed.

## References
1. E. Alcalá-Arroyo, A. Castillo-Ramirez, M. G. Magaña-Chávez, and L. de los Santos Baños, *Idempotence criteria for lazy cellular automata*, arXiv:2610.11811 (first posted 2026-10-08), https://arxiv.org/abs/2610.11811.
2. A. Castillo-Ramirez, M. G. Magaña-Chavez, and L. de los Santos Baños, *One-dimensional cellular automata with a unique active transition*, arXiv:2411.03601 (first posted 2024-11-06), https://arxiv.org/abs/2411.03601.
3. E. Alcalá-Arroyo and A. Castillo-Ramirez, *On the order of lazy cellular automata*, arXiv:2510.14841 (first posted 2025-10-16), https://arxiv.org/abs/2510.14841.
4. *Exact nineteen-value spatial image entropy spectrum of elementary cellular automata*, published-finding corpus public record (2026-10-27), https://github.com/published-finding corpus/2026/blob/main/2026/10/27/SCOPE-exact-nineteen-value-spatial-image-entropy-spectrum-of-elementar--d4f1725c3486/RESULT.md.
