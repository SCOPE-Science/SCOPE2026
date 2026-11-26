# Gaussian universality at Dyck nesting depth three

## Finding
For an integer \(H\ge 1\), let \(\mathcal D_H(n)\) denote the Dyck words of semilength \(n\) with nesting height at most \(H\). Write \(\iota(w)\) for the scattered-subsequence universality index of \(w\): the largest integer \(k\) for which every binary word of length \(k\) occurs as a subsequence. Define
\[
F_H(t,u)=\sum_{n\ge0}\sum_{w\in\mathcal D_H(n)}t^n u^{\iota(w)}.
\]
The exact distributions at the first three height bounds are
\[
\begin{aligned}
F_1(t,u)&=\frac{1}{1-ut},\\
F_2(t,u)&=\frac{1-2ut+ut^2}{(1-ut)(1-2ut)},\\
F_3(t,u)&=\frac{1-4ut+(u+4u^2)t^2+(u-3u^2)t^3}
{(1-ut)((1-2ut)^2-u^2t^3)}.
\end{aligned}
\]
In particular, for every \(n\ge1\), among the \(2^{n-1}\) height-at-most-two Dyck words, exactly one has index \(n\), and the others have index \(n-1\). Thus the random index at height two has variance \(2^{-(n-1)}(1-2^{-(n-1)})\), which tends to zero.

In contrast, let \(X_n\) be the universality index of a uniformly chosen word in \(\mathcal D_3(n)\). Then
\[
\begin{aligned}
\mathbb E X_n&=\frac{2}{\sqrt5}\,n+O(1),\\
\operatorname{Var}(X_n)&=\left(2-\frac{22\sqrt5}{25}\right)n+O(1),\\
\frac{X_n-(2/\sqrt5)n}
{\sqrt{(2-22\sqrt5/25)n}}&\xrightarrow{\mathrm d}\mathcal N(0,1).
\end{aligned}
\]
The positive variance coefficient is approximately \(0.0322601798\). This gives a sharp change in the order of index fluctuations between nesting heights two and three.

## Assumptions and scope
The alphabet is \(\{0,1\}\), with \(0\) an up-step and \(1\) a down-step. A Dyck word has equally many up- and down-steps and all prefix heights nonnegative. Nesting height is the maximum prefix height. Words are indexed distinctly (not modulo rotation); the empty word has index zero. Subsequence means an order-preserving selection of positions, not a contiguous factor. The generating-function identities are exact formal power series over \(\mathbb Q[u]\) for every semilength \(n\). The probabilistic assertions concern uniform sampling only within the height-at-most-three language, as \(n\to\infty\).

## Proof
**Greedy-arch lemma.** Scan a binary word from left to right. Store the first letter seen since the last completed arch. When its opposite is encountered, close an arch, increment a counter, and reset the stored letter. Let \(k\) be the total. Each of the first \(k\) arches contains both letters, so an arbitrary binary word of length \(k\) occurs by choosing its successive letters from successive arches. Conversely each arch ends at the earliest possible occurrence of its closing letter relative to the previous arch. The unfinished suffix contains at most one symbol. Let \(c\) be a symbol absent from that suffix, and let \(b_1,\ldots,b_k\) be the arch-closing symbols. The leftmost greedy embedding of \(b_1\cdots b_k\) uses exactly the successive closing positions; hence the extension \(b_1\cdots b_kc\) cannot be embedded. Thus the scan counter equals \(\iota(w)\) for every finite binary word, including \(k=0\).

**Letter-weighted matrices.** Give the three states the order \(\varnothing,0,1\), where a nonempty state denotes the single letter currently seen in an unfinished arch. With row-to-column transitions, the matrix for reading \(0\) is
\[
M_0=\begin{pmatrix}0&1&0\\0&1&0\\u&0&0\end{pmatrix}
\]
and the matrix for reading \(1\) is
\[
M_1=\begin{pmatrix}0&0&1\\u&0&0\\0&0&1\end{pmatrix}.
\]
A transition closing an arch has weight \(u\); all others have weight one. Consequently, if \(w=w_1\cdots w_r\), the polynomial \(e_{\varnothing}^{\mathsf T}M_{w_1}\cdots M_{w_r}\mathbf1\) equals \(u^{\iota(w)}\).

**Exact Dyck recursion.** Let \(E_H(t,u)\) be the sum of these matrix products over all height-at-most-\(H\) Dyck words, multiplied by \(t^{\text{semilength}}\). Every such word is a unique sequence of primitive excursions \(0v1\), with \(v\) of height at most \(H-1\). Therefore, as a formal matrix power series,
\[
E_0=I_3,\qquad E_H=(I_3-tM_0E_{H-1}M_1)^{-1},
\qquad F_H=e_{\varnothing}^{\mathsf T}E_H\mathbf1.
\]
This is an exact unambiguous combinatorial decomposition; all matrix inverses exist formally because their constant terms are identities. Evaluating the three successive \(3\)-by-\(3\) rational-matrix inversions and reducing fractions gives precisely the three displayed formulas. The accompanying verifier independently recomputes those rational identities symbolically.

The coefficient extraction from \(F_2\) gives, for \(n\ge1\),
\[
[t^n]F_2=u^n+(2^{n-1}-1)u^{n-1}.
\]
Its distribution is a one-step Bernoulli perturbation of \(n-1\). With probability \(p_n=2^{-(n-1)}\) the index is \(n\), otherwise \(n-1\). The displayed exact variance follows.

**Height-three singularity and Gaussian law.** At \(u=1\), cancellation reduces the third generating function to
\[
F_3(t,1)=\frac{1-2t}{1-3t+t^2}.
\]
Its dominant simple pole is \(r=(3-\sqrt5)/2\); the other poles lie strictly farther from zero. For \(u\) in a complex neighborhood of one, the dominant pole is the unique analytic root \(r(u)\) near \(r\) of
\[
Q(t,u)=(1-2ut)^2-u^2t^3=0.
\]
Here \(Q_t(r,1)\ne0\), the numerator is nonzero at the pole, and the remaining poles remain separated in modulus. Partial fractions uniformly give, for analytic nonzero \(K(u)\), some \(\theta\in(0,1)\), and \(u\) sufficiently near one,
\[
[t^n]F_3(t,u)=K(u)r(u)^{-n}(1+O(\theta^n)),
\]
where \(K(1)>0\). The probability generating function is the quotient of this expression by its value at \(u=1\). Hence its logarithm for \(u=e^s\) is
\[
\log\mathbb E[e^{sX_n}]
=n\log\frac{r(1)}{r(e^s)}+O(1),
\]
locally uniformly and analytically near \(s=0\). Implicit differentiation of \(Q(r(u),u)=0\) yields
\[
r'(1)=1-\frac{3\sqrt5}{5},\qquad
r''(1)=-5+\frac{63\sqrt5}{25}.
\]
The first and second derivatives of \(\log(r(1)/r(e^s))\) at zero are, respectively,
\[
-\frac{r'(1)}r=\frac2{\sqrt5},\qquad
-\frac{r''(1)}r-\frac{r'(1)}r+\left(\frac{r'(1)}r\right)^2
=2-\frac{22\sqrt5}{25}>0.
\]
Differentiating the uniform analytic remainder proves the asserted mean and variance estimates. For the central limit theorem, evaluate the moment-generating function at \(s=iy/\sqrt{\sigma^2 n}\), subtract the linear term, use the second-order Taylor expansion (the third-order term is \(O(n^{-1/2})\)), and apply the continuity theorem for characteristic functions. This gives convergence to the standard normal distribution.

## Verification
The included standalone `verify.py` (Python 3, SymPy) reconstructs the three symbolic matrix inversions, verifies equality with all three closed rational functions, independently generates every Dyck word of semilength at most ten at each height, and compares exact index distributions. For semilength at most six it also checks the index directly against all binary subsequences of each candidate length, rather than using the arch algorithm to test itself. Finally it checks all derivative identities at the dominant pole and positivity of the Gaussian variance. Running `python3 verify.py` outputs `VERIFY_OK`. These finite checks support, but do not replace, the all-length matrix argument and analytic proof.

## Relationship to prior work
Mol, Rampersad, and Shallit (2023) analyze Dyck-word nesting and show that a natural repetition-free family has nesting depth at most three, motivating that bounded-height class, but do not enumerate its subsequence-universality index. Schnoebelen and Veron (2023) give the arch-factorization framework and algorithms for computing universality indices of individual words, not the joint height-restricted distribution. Adamson and collaborators (2023) give general methods to count \(k\)-universal words in automata-recognized languages; since bounded-height Dyck words form a regular language for fixed height, this is relevant broader algorithmic coverage. The particular rational functions, explicit irrational Gaussian constants, and the height-two versus height-three fluctuation transition are not asserted in those inspected statements. General automaton machinery could compute their coefficients in principle and must not be mistaken for an independent novelty proof.

A related unrestricted-height Dyck-word universality generating function produces a different Catalan law. It does not determine the bounded-height distribution, because height is not marked in that formula. General binary-word run-restricted universality laws likewise do not imply the Dyck nesting-height result.

## Limitations
The formulas are established only for heights one, two and three; no closed distribution for larger heights is claimed. The central limit law is for height three and uniform semilength-\(n\) sampling, not for unrestricted Dyck words. The result follows from exact transfer algebra combined with singularity analysis; the finite verifier is not an infinite proof. The possibility of an unindexed equivalent special-case enumeration or an independently unpublished calculation remains an originality risk. Independent external mathematical validation has not been performed.

## References
1. Lucas Mol, Narad Rampersad, Jeffrey Shallit, *Dyck words, pattern avoidance, and automatic sequences*, arXiv:2301.06145, first posted January 15, 2023. https://arxiv.org/abs/2301.06145
2. Philippe Schnoebelen, Julien Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932, first posted April 24, 2023. https://arxiv.org/abs/2304.11932
3. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658, first posted November 17, 2023. https://arxiv.org/abs/2311.10658
