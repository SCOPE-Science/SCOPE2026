# Border-Parikh lexicographic ordering of first-hit letter proportions

## Finding
Let \(\Sigma\) be any alphabet of size \(s\ge2\), let \(w\in\Sigma^m\) be any nonempty word, and sample independent uniform letters \(X_1,X_2,\ldots\) until the first occurrence of \(w\) as a contiguous factor. Write \(\tau\) for the final position, \(N_a\) for the number of occurrences of symbol \(a\) in \(X_1\cdots X_\tau\), and \(Q_a=\mathbb E[N_a/\tau]\).

A **border length** is \(\ell\in\{1,\ldots,m\}\) such that the prefix of \(w\) of length \(\ell\) equals its suffix of length \(\ell\); the full length \(m\) is included. Write \(c_a(\ell)\) for the number of \(a\)'s in that prefix. For any distinct \(a,b\in\Sigma\), set \(d_\ell=c_a(\ell)-c_b(\ell)\) on border lengths. If every \(d_\ell\) vanishes, then \(Q_a=Q_b\). Otherwise, with \(L\) the largest border length for which \(d_L\ne0\),

\[
\operatorname{sgn}(Q_a-Q_b)=\operatorname{sgn}(d_L).
\]

Thus the complete weak ordering, including all ties, of the stopped letter proportions \((Q_a)_{a\in\Sigma}\) is lexicographically determined by the border-prefix Parikh count vectors, read in strictly decreasing border length. In particular, all \(Q_a=1/s\) if and only if **every nonempty border** contains each alphabet letter equally often.

For example, the ternary word \(w=011220\) is globally balanced, but its only nonempty borders have lengths \(1\) and \(6\). Hence \(Q_0>Q_1=Q_2\), despite equal letter counts in \(w\) itself.

## Assumptions and scope
Every letter is sampled with probability \(1/s\), independently of all previous samples, where \(s\) is an integer at least two. The target \(w\) is fixed, finite and nonempty. The stopping time is almost surely finite: independent disjoint blocks of length \(m\) match \(w\) with probability \(s^{-m}\), giving a geometric upper bound for the tail. Expectations of stopped proportions therefore exist and lie in \([0,1]\). No asymptotic assumption on \(m\) or \(s\) is made.

## Proof
For \(0<z<1\) and marker variables \(\mathbf y=(y_a)_{a\in\Sigma}\), attach a letter \(a\) weight \(t_a=zy_a/s\), and write \(p(v)=\prod_{i=1}^{|v|}t_{v_i}\). Put \(S=\sum_a t_a\) and \(\mathcal B=\mathcal B(w)\), the set of nonempty border lengths. The multivariate first-hit generating function is

\[
H(z,\mathbf y)=\mathbb E\!\left[z^\tau\prod_a y_a^{N_a}\right]
=\frac1{1+(1-S)\displaystyle\sum_{\ell\in\mathcal B}\frac1{p(w_{1}\cdots w_\ell)}}.
\tag{1}
\]

To prove (1), the weighted sum of **all** finite words ending with \(w\) equals \(p(w)/(1-S)\). Split each such word uniquely after its first occurrence of \(w\). If the suffix following that occurrence has length at least \(m\), it is an arbitrary word ending with \(w\), of total weight \(p(w)/(1-S)\). If the suffix has length less than \(m\), the two occurrences overlap, so the overlap is precisely a nonempty border of length \(\ell\); the uniquely prescribed intervening suffix has weight \(p(w)/p(w_1\cdots w_\ell)\). Therefore

\[
\frac{p(w)}{1-S}=H(z,\mathbf y)\left(\frac{p(w)}{1-S}+p(w)\sum_{\ell\in\mathcal B}\frac1{p(w_1\cdots w_\ell)}\right),
\]

which gives (1). The decomposition is an identity of absolutely convergent power series near \(\mathbf y=\mathbf1\) for \(0<z<1\).

At \(\mathbf y=\mathbf1\), define

\[
D(z)=1+(1-z)\sum_{\ell\in\mathcal B}(s/z)^\ell>0.
\]

Differentiate (1) with respect to the markers of \(a,b\), then subtract. The derivative of \(S\) cancels and yields

\[
\left.(\partial_{y_a}-\partial_{y_b})H(z,\mathbf y)\right|_{\mathbf y=\mathbf1}
=\frac{(1-z)\displaystyle\sum_{\ell\in\mathcal B}d_\ell(s/z)^\ell}{D(z)^2}.
\tag{2}
\]

For any integer \(T\ge1\), \(1/T=\int_0^1z^{T-1}\,dz\). Moreover \(|N_a-N_b|/\tau\le1\); thus Fubini or bounded truncation of the first-hit generating function justifies

\[
Q_a-Q_b
=\int_0^1\frac{1-z}{zD(z)^2}\left(\sum_{\ell\in\mathcal B}d_\ell(s/z)^\ell\right)dz.
\tag{3}
\]

If all border differences vanish, (3) is zero. Otherwise take \(L\) maximal with \(d_L\ne0\), and interchange \(a,b\) if necessary so that \(d_L\ge1\). Let \(t=z/s\in(0,1/2)\). For every shorter border \(\ell=L-j\), changing from a prefix of length \(\ell\) to one of length \(L\) can change \(c_a-c_b\) by at most \(j\). Hence \(d_{L-j}\ge d_L-j\). Defining coefficients for missing border lengths to be zero, we obtain

\[
\begin{aligned}
(s/z)^{-L}\sum_{\ell\in\mathcal B}d_\ell(s/z)^\ell
&\ge d_L-\sum_{j\ge1}(j-d_L)_+t^j\\
&\ge1-\sum_{j\ge2}(j-1)t^j\\
&=1-\frac{t^2}{(1-t)^2}>0.
\end{aligned}
\]

There are no contributions at border lengths above \(L\), since their differences are zero. Thus the integrand in (3) has the strict sign of \(d_L\) for every \(0<z<1\), proving the pairwise comparison. The lexicographic statement is the same comparison made for every unordered pair of symbols. Finally, all pairwise equality conditions hold exactly when all border-prefix Parikh vectors are constant across letters; since \(\sum_a Q_a=1\), this is equivalent to \(Q_a=1/s\) for every symbol. \(\square\)

## Verification
A standalone `checker.py` recomputes the border polynomial for all targets up to length six on binary and ternary alphabets, and up to length five on a four-letter alphabet. It compares polynomial signs for every letter pair at five independent parameter values, and compares numerical integration of the signed first-hit derivative with an independently implemented prefix-automaton stopping-time dynamic program for six sample targets. The code verifies a ternary balanced-full-word example. These finite checks are corroborative; the strict analytic inequality proves the theorem at every alphabet size and target length. Run with `python checker.py` using Python 3 and SciPy.

## Relationship to prior work
Bóna, Maga and Richey, arXiv:2606.06655 (initially public June 4, 2026), study binary forbidden-pattern letter frequency and identify the first-hit stopped fraction as a separate statistic. An earlier binary border-imbalance classification concerns only two symbols; the present result gives all pairwise comparisons, simultaneous ties and weak rankings for arbitrary finite alphabets. Myers, arXiv:0906.3763, develops weighted generating functions for forbidden substrings; Ostaszewska and Zajkowski, arXiv:1302.4859, investigate waiting times and pattern-winning probabilities. Neither inspected text states this border-Parikh lexicographic law for the **ratio** of stopped letter counts to stopping time. The standard autocorrelation formalism supplies related algebraic machinery, not by itself the strictly signed comparison in (3).

## Limitations
Uniform i.i.d. sampling and stopping on one fixed target are essential to the proof. The theorem compares expected stopped **proportions** but does not give a closed expression for each expectation independently, and does not treat nonuniform sources, multiple competing targets or infinite forbidden sets. Historical novelty is based on inspected available sources and search results; an implicit treatment in classical overlap literature remains a priority risk. This is a self-review, not independent validation.

## References
- M. Bóna, B. Maga and J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655, first public June 4, 2026, https://arxiv.org/abs/2606.06655 .
- A. N. Myers, *Forbidden substrings on weighted alphabets*, arXiv:0906.3763, https://arxiv.org/abs/0906.3763 .
- U. Ostaszewska and K. Zajkowski, *On the waiting time till some patterns occur in i.i.d. sequences*, arXiv:1302.4859, https://arxiv.org/abs/1302.4859 .
- L. J. Guibas and A. M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, Journal of Combinatorial Theory A 30 (1981), 183–208, https://doi.org/10.1016/0097-3165(81)90005-4 .
