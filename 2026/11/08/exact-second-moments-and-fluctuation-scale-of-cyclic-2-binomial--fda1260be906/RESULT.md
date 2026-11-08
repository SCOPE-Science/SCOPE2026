# Exact second moments and fluctuation scale of cyclic 2-binomial signature diversity

## Finding

For a binary word \(w\), two linear words are *2-binomially equivalent* when the numbers of scattered subsequences of lengths at most two agree. Let \(T(w)\) denote the number of different such equivalence signatures occurring among the cyclic rotations of \(w\). We give an **exact finite first and second moment** of this circular diversity statistic in the first nontrivial arithmetic stratum, with a strictly positive limiting variance.

Fix integers \(m\ge2\) and \(1\le h<m\) satisfying \(\gcd(m,h)=1\). Let \(W\) be uniform over length-\(2m\) binary words containing exactly \(2h\) ones; the words are labeled by their linear positions, so there are \(\binom{2m}{2h}\) equally likely samples. Put \(C(W)=2m-T(W)\). Define
\[
B=\binom mh^2,\qquad A_d=\sum_{a\in\mathbb Z}\binom da^2\binom{m-d}{h-a}^2\quad(1\le d<m),
\]
where \(\binom uv=0\) when \(v\notin\{0,\ldots,u\}\). Then
\[
\boxed{\mathbb EC=\frac{mB}{\binom{2m}{2h}},\qquad
\mathbb EC^2=\frac{mB+2\sum_{d=1}^{m-1}(m-d)A_d}{\binom{2m}{2h}}.}
\]
In particular \(\mathbb ET=2m-\mathbb EC\) and \(\operatorname{Var}(T)=\mathbb EC^2-(\mathbb EC)^2\). For any sequence of coprime integer pairs \((m,h)\) with \(m\to\infty\) and \(h/m\to p\in(0,1)\),
\[
\boxed{\frac{\mathbb E(2m-T)}{\sqrt m}\longrightarrow\frac1{\sqrt{\pi p(1-p)}},\qquad
\frac{\operatorname{Var}(T)}m\longrightarrow\frac{\pi-2}{2\pi p(1-p)}>0.}
\]
Thus the **mean** number of distinct signatures is \(2m-\Theta(\sqrt m)\), while their standard deviation is also of order \(\sqrt m\). In particular, the leading deficit is not deterministic at that scale.

## Assumptions and scope

A scattered occurrence of \(01\) is an ordered pair of positions holding zero then one, not necessarily adjacent. For a word of fixed length and fixed number of ones, the entire 2-binomial signature is determined by the scattered-\(01\) count: all one-letter counts, equal-letter two-subsequence counts, and the sum of the \(01\) and \(10\) counts are fixed. Circular windows in this result have exactly \(m\) consecutive positions, with indices taken modulo \(2m\). We treat exactly the arithmetic stratum \(\gcd(2m,2h)=2\), equivalent to \(\gcd(m,h)=1\).

## Proof

**Signature collisions reduce to opposite cyclic cuts.** Number positions from zero. Let \(S_s\) be the number of scattered \(01\) occurrences in the left rotation by \(s\), and let \(K_s\) be the number of ones in the first \(s\) positions. Moving one zero from the beginning to the end removes \(2h\) scattered \(01\) pairs; moving one one instead adds \(2m-2h\) pairs. Summing yields
\[
S_s-S_0=2mK_s-2hs,\qquad 0\le s\le2m.
\]
Modulo \(2m\), equality of \(S_s\) and \(S_t\) forces \(2h(s-t)\equiv0\pmod{2m}\). Coprimality implies \(s\equiv t\pmod m\). For distinct cuts \(0\le s,t<2m\), therefore the only possible matching pair is \(s,s+m\) with \(0\le s<m\). The corresponding signatures agree precisely when the length-\(m\) circular factor beginning at \(s\) has \(h\) ones. Let \(I_s\) be the indicator of that event. No signature can have multiplicity three in this stratum, so
\[
C=2m-T=\sum_{s=0}^{m-1}I_s.
\]
This is the needed cyclic-to-hypergeometric reduction.

**Exact first moment.** Each of the \(m\) length-\(m\) windows has a hypergeometric count of ones. Its probability of containing \(h\) ones equals
\[
\Pr(I_s=1)=\frac{\binom mh\binom mh}{\binom{2m}{2h}}=\frac{B}{\binom{2m}{2h}}.
\]
Linearity of expectation proves the first formula.

**Exact second moment.** For \(s<t<m\), put \(d=t-s\). The two circular windows split the circle into consecutive arcs of lengths \(d,m-d,d,m-d\). Having \(h\) ones in each window forces the first and third arcs to have the same number \(a\) of ones, and the second and fourth to have \(h-a\) ones. Thus precisely \(A_d\) of the \(\binom{2m}{2h}\) words have both indicators equal to one. There are \(m-d\) ordered pairs \((s,t)\) with \(t-s=d\). Expanding \(C^2=\sum_s I_s+2\sum_{s<t}I_sI_t\) gives the second formula, including all endpoint ranges through the convention for binomial coefficients.

**First-order fluctuation constants.** Write \(p_m=h/m\) and \(q=p(1-p)\). Stirling's formula implies
\[
P_m:=\Pr(I_0=1)=\frac{\binom mh^2}{\binom{2m}{2h}}\sim\frac1{\sqrt{\pi m q}}.
\]
Conditioning on \(I_0=1\) makes the two length-\(m\) halves independent uniform words with \(h\) ones each. For \(d\in\{1,\ldots,m-1\}\), let \(X_d,Y_d\) be independent hypergeometric random variables with population size \(m\), marked population \(h\), and sample size \(d\). Comparing the entering and leaving arcs shows
\[
\Pr(I_d=1\mid I_0=1)=\Pr(X_d=Y_d)=\sum_a\Pr(X_d=a)^2.
\]
For \(d/m\to x\in(0,1)\), a local central limit estimate for the hypergeometric mass with variance \(\sigma_d^2=d p_m(1-p_m)(m-d)/(m-1)\) gives
\[
\sum_a\Pr(X_d=a)^2\sim\frac1{2\sqrt{\pi m q x(1-x)}}.
\]
For completeness, this estimate follows by applying Stirling's formula uniformly on the central window \(a=dp_m+O(\sqrt{m\log m})\), where the mass is \(\sigma_d^{-1}\varphi((a-dp_m)/\sigma_d)(1+o(1))\), bounding the tails by hypergeometric exponential concentration, and replacing the central lattice sum of the squared normal density by its integral \(\int\varphi^2=1/(2\sqrt\pi)\). The corresponding global estimate
\[
\sum_a\Pr(X_d=a)^2\le\max_a\Pr(X_d=a)\le
\frac{K}{\sqrt{1+d(m-d)/m}}
\]
holds uniformly for all \(d\) for sufficiently large \(m\), where \(K\) depends only on a compact subinterval of \((0,1)\) containing \(p_m\): use the same Stirling bound for a hypergeometric mode, and symmetry under replacing the drawn subset by its complement. This integrable bound justifies passing to the Riemann-sum limit, including the endpoints. Consequently,
\[
\frac{\mathbb EC^2}{m}\longrightarrow
\frac1{\pi q}\int_0^1\frac{1-x}{\sqrt{x(1-x)}}\,dx
=\frac1{2q},
\]
because the integral is \(\pi/2\), while \(\mathbb EC/m\to0\). Also \((\mathbb EC)^2/m\to1/(\pi q)\). Subtraction yields
\[
\lim_{m\to\infty}\frac{\operatorname{Var}(T)}m
=\frac{1}{2q}-\frac1{\pi q}=\frac{\pi-2}{2\pi q}.
\]
The constant is strictly positive for every \(p\in(0,1)\).

## Verification

The accompanying standalone `VERIFY.py` independently constructs the complete 2-binomial signature of every cyclic rotation, compares its number of distinct values with the balanced-window formula, and sums the deficit and its square. For every admissible \((m,h)\) with \(2\le m\le8\), all 25,180 eligible labeled words were tested. It also verifies the exact first and second moment formulas as rational numbers. The output is `DIRECT_TYPES_AND_BOTH_MOMENTS_OK 25180`. Numerical checks for \(h=(m-1)/2\) and odd \(m\le161\) show convergence toward the stated asymptotic constants; the infinite limits rest on the proof, not on the finite experiments. To reproduce: `python3 VERIFY.py`.

## Relationship to prior work

Rao, Rigo and Salimov defined 2-binomial equivalence and studied avoidance of 2-binomial squares and cubes [1], not the random number of distinct equivalence types across cyclic cuts. The established deterministic theorem on cyclic 2-binomial fingerprints gives sharp upper/lower bounds and equality cases for this same observable; **those prior bounds and equality cases are not claimed here**. They do not determine its first moment, its joint collision counts, its second moment or its positive-order fluctuation scale. Golafshan's fixed-length class-size distribution [2] instead counts linear words in each equivalence class; it does not specify their cyclic orbit diversity. Arnoux [3] studies adjacent *factors* of circular words rather than scattered-subsequence signatures. The circular adjacent-\(01\) statistics in OEIS A119462 [4] concern a different invariant.

## Limitations

The exact formulas require \(\gcd(m,h)=1\), and the asymptotic formulas additionally require \(h/m\to p\in(0,1)\). They do not cover other gcd strata, endpoint density regimes, the entire distribution of \(T\), or a weak limit for its centered fluctuation. The proof establishes moment limits, not a full limiting law. Originality is assessed against accessible primary literature and prior published records; a missed equivalent treatment of balanced semicircle counts is possible. No independent audit is asserted.

## References

[1] M. Rao, M. Rigo, P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743, first posted 2013-10-17. https://arxiv.org/abs/1310.4743

[2] M. Golafshan, *Binary binomial equivalence via hyperplane arrangements*, arXiv:2606.23426, 2026. https://arxiv.org/abs/2606.23426

[3] P. Arnoux, *Note on occurrences of factors in circular words*, RAIRO Theor. Inf. Appl. 50 (2016), 167–170. https://doi.org/10.1051/ita/2016019

[4] OEIS A119462, number of circular binary words by adjacent \(01\)-occurrence count. https://oeis.org/A119462
