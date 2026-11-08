# All-order rational run statistics and the exact five-state run-transition law for the base-\(3/2\) Thue–Morse word

## Finding
Let \(t_0t_1t_2\cdots\) be the binary parity sequence of the unique rational-base representations
\[
n=\sum_{j\geq 0}\frac{d_j}{2}\left(\frac32\right)^j,\qquad d_j\in\{0,1,2\},\qquad t_n=\sum_jd_j\pmod2.
\]
Let \(L_0,L_1,\ldots\) denote lengths of its successive maximal constant-symbol runs. Every run has length in \(\{1,2,3,4,5\}\). For every finite tuple \((a_1,\ldots,a_s)\) of positive integers, the natural frequency
\[
\lim_{N\to\infty}\frac1N\#\{0\leq j<N:(L_j,\ldots,L_{j+s-1})=(a_1,\ldots,a_s)\}
\]
exists, is rational, and is given by a terminating nine-residue recursion below. It is zero whenever any \(a_i>5\).

In particular, the exact joint distribution of two consecutive run lengths is the following matrix, with rows and columns indexed by \(1,\ldots,5\):
\[
\Pr(L_j=a,L_{j+1}=b)\ \longrightarrow\ \frac1{108}
\begin{pmatrix}
0&9&12&0&6\\
9&0&12&6&0\\
12&12&8&2&2\\
0&6&2&0&1\\
6&0&2&1&0
\end{pmatrix}_{a,b}.
\]
The row and column marginals are \((1/4,1/4,1/3,1/12,1/12)\); the mean run length is \(5/2\). Precisely the eight zero-matrix ordered pairs cannot occur.

## Assumptions and scope
The rational-base representation and Thue–Morse parity follow the half-scaled digit convention above. The distinct convention \(n=\sum d_j(3/2)^j\) yields a related but different sequence. Positions and finite words are zero-indexed where applicable. All limits refer to natural frequencies in the one-sided infinite sequence, not to a stationary random source. At the start of the word an initial incomplete backward run has no effect on the limits.

Write \(y_n=t_n\oplus t_{n+1}\) for its difference word. The established Toeplitz description of this sequence is the regular \((9,4)\) filling template \(01?0?10??\): the four question marks, filled from left to right by successive symbols of \(y\), occur at residues \(2,4,7,8\) modulo \(9\). Equivalently, for every \(k\geq0\),
\[
(y_{9k},\ldots,y_{9k+8})=(0,1,y_{4k},0,y_{4k+1},1,0,y_{4k+2},y_{4k+3}).
\]
This established structural description is used as a premise; the all-order frequency conclusion and explicit joint matrix are the results here.

## Proof
**Step 1: existence of factor frequencies, including arithmetic-progressions.** After \(m\) rounds of filling the \((9,4)\) Toeplitz template, the specified coordinates form a periodic partial word of period \(9^m\), with exactly a \((4/9)^m\) proportion of still unspecified coordinates. For any fixed binary word \(v\), its occurrence indicator at starting index \(k\) is determined by this periodic approximation except when at least one of its \(|v|\) positions is unspecified. The upper density of exceptional starts is at most \(|v|(4/9)^m\), which tends to zero. It follows by periodic approximation that the natural factor frequency \(F(v)\) exists.

The same convergence holds when starting indices are restricted to any progression \(4k+c\), for fixed integer \(c\): multiplication by \(4\) permutes residues modulo \(9^m\), and hence the proportion of unspecified positions sampled along this progression is also \((4/9)^m\). The same union bound works for every fixed window. Consequently the occurrence frequency of \(v\) along \(4k+c\) equals \(F(v)\). This progression invariance is essential to the nine-residue calculation; no independence of Toeplitz coordinates is assumed.

**Step 2: a terminating exact recursion.** Set \(F(\varnothing)=1\), and let \(P=01?0?10??\). For any word \(v=v_0\cdots v_{\ell-1}\), and \(r\in\{0,\ldots,8\}\), inspect the template positions \((r+j)\bmod9\) for \(0\leq j<\ell\). If any known template symbol contradicts \(v_j\), declare that residue incompatible. Otherwise form \(h_r(v)\) by concatenating, in order, those \(v_j\) whose template positions are question marks. The corresponding positions in the source \(y\) are consecutive indices beginning at a residue-dependent constant in the progression \(4k+c\). By Step 1,
\[
F(v)=\frac19\sum_{r=0}^8 {\bf1}_{\{r\ \mathrm{compatible}\}}F(h_r(v)). \tag{1}
\]
For \(\ell\geq3\) every three consecutive template positions include a fixed symbol, so \(|h_r(v)|<|v|\). Formula (1) therefore reduces all factor frequencies to lengths at most two.

The one-symbol equations are \(9F(1)=2+4F(1)\) and \(F(0)=1-F(1)\), giving \(F(1)=2/5\), \(F(0)=3/5\). For the pair \(11\), the nine residues give \(9F(11)=2F(1)+F(11)\), hence \(F(11)=1/10\). Stationarity of limiting adjacent-pair counts gives \(F(01)=F(10)\); their sum with \(F(11)\) and \(F(00)\) yields
\[
F(00)=F(01)=F(10)=3/10,\qquad F(11)=1/10.
\]
Thus (1) is an exact terminating rational algorithm for every binary factor \(v\).

**Step 3: translate factor occurrences to successive runs.** A digit \(y_n=1\) marks exactly a boundary between runs of \(t\). The fixed ones at residues \(1\) and \(5\) ensure that the distance between consecutive ones is at most five. Every complete run after the first corresponds to exactly one such distance. For any positive run-length tuple \(\boldsymbol a=(a_1,\ldots,a_s)\), define its boundary word
\[
B(\boldsymbol a)=1\,0^{a_1-1}1\,0^{a_2-1}1\cdots0^{a_s-1}1.
\]
An occurrence of \(B(\boldsymbol a)\) in \(y\) is exactly a group of \(s\) successive complete runs with those lengths, anchored at the first boundary. Because \(F(1)=2/5\), boundary indices have density \(2/5\); dividing the occurrence frequency among positions by this density gives the frequency among run indices:
\[
\Pr_{\mathrm{run}}(\boldsymbol a)=\frac{F(B(\boldsymbol a))}{F(1)}=\frac52F(B(\boldsymbol a)).\tag{2}
\]
All limits therefore exist and are rational; all patterns containing a length greater than five are absent. The formula applies also to tuples of length one.

**Step 4: exact pair matrix and completeness.** Apply (1) to \(B(a,b)=1\,0^{a-1}1\,0^{b-1}1\) for \(a,b\in\{1,2,3,4,5\}\); formula (2) gives the displayed matrix. An exact-fraction implementation supplied with this result evaluates all twenty-five entries and asserts equality with the stated matrix. Independently, representative exact frequencies are
\[
F(101)=1/10,\quad F(100)=1/5,\quad F(1001)=2/15,\quad
F(1000)=F(0001)=1/15,\quad F(0000)=1/30.
\]
The matrix sums to one, its row sums give the asserted marginal probabilities and \(\sum_{a=1}^5a\Pr_{\mathrm{run}}(a)=5/2\). Any factor that occurs in a regular Toeplitz word is contained in a fully specified segment at some finite stage, whose periodic repeats give it strictly positive natural frequency. Thus a zero entry implies the corresponding adjacent-run pattern never occurs, rather than merely having zero density.

## Verification
The standalone `exact_profile.py` evaluates the finite recursion using Python's exact `Fraction` arithmetic, checks every matrix entry, its symmetry, normalization, marginals, and additional short-factor frequencies. It returns `EXACT_RUN_PROFILE_OK`. Separately, `independent_prefix.py` constructs the first 200,001 parity digits directly from the rational-base digit extraction, recomputes 200,000 differences, and checks exact agreement with the Toeplitz expansion. It checks the observed 79,997 consecutive run-length pairs against the matrix; this numerical agreement is a finite consistency check and is not used as a proof of limiting frequencies. Run `python3 exact_profile.py` and `python3 independent_prefix.py` from the directory containing the supplied two scripts.

## Relationship to prior work
Cassaigne, Espinoza, Rigo and Stipulanti (2026, arXiv:2602.21895) identify the first-difference sequence as the \((9,4)\) Toeplitz word and determine its single-symbol frequencies. The present contribution uses that structural identity to prove an explicit *all-order* rational frequency algorithm for consecutive run lengths and evaluate the complete five-by-five adjacent-run matrix; those statements and that matrix were not located in the inspected source. Dekking (2023, arXiv:2301.13563) studies a related rational-base Thue–Morse word with a distinct digit convention and does not supply this run-transition law.

## Limitations
The proof depends on the cited Toeplitz identity for the difference sequence and applies to the specified half-scaled base-\(3/2\) parity word. It computes frequencies of *run-length patterns*, not arbitrary factor frequencies of the original parity word \(t\). It does not assert stochastic independence, a finite-state Markov property of the run process, a central limit theorem, or a classification for other rational bases. The cited Toeplitz result makes the algorithmic deduction accessible; no independent scholarly priority determination has been performed.

## References
1. J. Cassaigne, C. Espinoza, M. Rigo and M. Stipulanti, *Symbols frequencies in the Thue–Morse word in base 3/2 and related conjectures*, arXiv:2602.21895, first posted 2026-02-25, https://arxiv.org/abs/2602.21895.
2. F. M. Dekking, *The Thue–Morse sequence in base 3/2*, arXiv:2301.13563, https://arxiv.org/abs/2301.13563.
