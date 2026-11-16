# A modulo-six Walsh stability law for perfect matchings of cycle prisms

## Finding

Let \(G_n=C_n\square K_2\), the simple cycle prism with \(n\ge3\) rungs and \(3n\) edges. Let \(\mathcal M_n\subseteq\mathbb F_2^{E(G_n)}\) consist of the edge-incidence vectors of its perfect matchings. For every binary edge frequency \(\omega\), consider the **unnormalized** Walsh multiplier
\[
W_n(\omega)=\sum_{M\in\mathcal M_n}(-1)^{\langle\omega,M\rangle}.
\]
Then a zero multiplier exists if and only if \(3\mid n\), and the **exact least positive multiplier magnitude** is
\[
\boxed{\min_{\omega:\,W_n(\omega)\ne0}|W_n(\omega)|=
\begin{cases}
4,&n\equiv0\pmod6,\\
2,&n\equiv3\pmod6,\\
1,&3\nmid n.
\end{cases}}
\]
In particular, convolution on \(\ell^2(\mathbb F_2^{E(G_n)})\) by \(\mathbf1_{\mathcal M_n}\), **without normalization of the convolution sum**, is invertible precisely when \(3\nmid n\). Its sharp inverse operator norm in those cases is \(1\), and the Moore–Penrose inverse norm is exactly \(1/4\) when \(6\mid n\) and \(1/2\) when \(n\equiv3\pmod6\).

There is also an explicit exponential family of zero frequencies. For \(n=6k+3\) or \(n=6k+6\), with \(k\ge0\), at least \(2^{2n}4^k\) distinct Walsh coefficients vanish.

## Assumptions and scope

Vertices are \((i,0),(i,1)\), with \(i\in\mathbb Z/n\mathbb Z\); the two horizontal edges at position \(i\) connect consecutive indices on each layer, and the rung connects the two layers at index \(i\). The three edge-sign sequences, each in \(\{+1,-1\}^n\), are \(a_i,b_i,r_i\). Every sign vector corresponds to a unique binary Walsh frequency. Write \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\) and \(L_j=F_{j-1}+F_{j+1}\) for the usual Fibonacci and Lucas numbers.

## Proof

**1. Perfect-matching decomposition.** If a perfect matching uses any rung, the two rail paths remaining between successive rungs must be matched identically. It therefore corresponds uniquely to a matching of the index cycle: each chosen cycle edge represents a pair of horizontal edges, and each uncovered index represents a rung. The same description also covers the two matchings consisting of coincident alternating horizontal pairs when \(n\) is even. In even length, there are exactly two further perfect matchings, obtained by choosing the two opposite alternations on the separate rails. In odd length there are no further matchings.

Consequently the number of perfect matchings is
\[
N_n=F_{n-1}+F_{n+1}+2\mathbf1_{\{2\mid n\}}
=L_n+2\mathbf1_{\{2\mid n\}}.
\]

**2. Exact signed transfer formula.** Define
\[
y_i=a_i b_i r_i r_{i+1},\qquad
T(y)=\begin{pmatrix}1&y\\1&0\end{pmatrix},\qquad
Z_n(y)=\operatorname{tr}\!\left(\prod_{i=0}^{n-1}T(y_i)\right).
\]
The cyclic transfer trace is the sum of \(\prod_{i\in I}y_i\) over all matchings \(I\) of the index cycle. The paired-horizontal contribution is \((\prod_i r_i)Z_n(y)\). For even \(n\), the two opposite-rail contributions are
\[
S_0=\prod_{i\ \mathrm{even}}a_i\prod_{i\ \mathrm{odd}}b_i,
\qquad S_1=\prod_{i\ \mathrm{odd}}a_i\prod_{i\ \mathrm{even}}b_i.
\]
Their product is \(S_0S_1=\prod_i y_i\), since all rung signs occur exactly twice. Thus, for every edge frequency,
\[
W_n=(\prod_i r_i)Z_n(y)+\mathbf1_{\{2\mid n\}}(S_0+S_1).
\tag{1}
\]
Conversely, for **any** prescribed \(y\) and arbitrary \(r_i,a_i\), choosing \(b_i=y_i r_i r_{i+1}a_i\) realizes those parameters. In even length, \(S_0+S_1\) is zero when \(\prod_i y_i=-1\), whereas when that product is \(+1\), its sign can be switched freely by changing one \(a_i\) and the corresponding \(b_i\).

**3. Arithmetic lower bounds.** Lucas numbers are even exactly at indices divisible by three, because the Fibonacci companion matrix modulo two has period three. Therefore \(N_n\) is odd for \(3\nmid n\), and every \(W_n(\omega)\) is odd. If \(3\mid n\), all multipliers are even.

At \(6\mid n\) they are divisible by **four**. Indeed the Fibonacci companion matrix satisfies
\[
\begin{pmatrix}1&1\\1&0\end{pmatrix}^{6}\equiv I\pmod4,
\]
so \(L_n\equiv2\pmod4\) and \(N_n=L_n+2\equiv0\pmod4\). Each rung occurs in precisely \(F_n\) perfect matchings, and each rail edge occurs in precisely \(F_{n-1}+1\) perfect matchings. Both counts are even when \(6\mid n\). For an arbitrary binary frequency \(\omega\), expanding every character modulo four therefore gives
\[
W_n(\omega)\equiv N_n-2\sum_{e\in E(G_n)}\omega_e\#\{M:e\in M\}
\equiv0\pmod4.
\]
The lower bounds for the asserted minimum positive magnitudes are proved.

**4. Exact witnesses and six-site propagation.** Encode \(y_i=+1\) by `+` and \(y_i=-1\) by `-`. Taking all rung signs positive, the following finite witnesses realize the lower bounds. At even lengths the final signed alternating-rail contribution is chosen with the displayed sign by adjusting \(a_i,b_i\), as permitted after (1).

| \(n\) | sign word \(y\) | \(Z_n(y)\) | alternating-rail sum | \(W_n\) |
|---:|:---:|---:|---:|---:|
| 3 | `++-` | 2 | 0 | 2 |
| 4 | `++--` | -1 | 2 | 1 |
| 5 | `+-+--` | 1 | 0 | 1 |
| 6 | `+++-+-` | 6 | -2 | 4 |
| 7 | `+++-+--` | 1 | 0 | 1 |
| 8 | `++++-+--` | 1 | 0 | 1 |

Two further seed words give zero: at length three, `--+` yields the transfer product \(\operatorname{diag}(-1,1)\); at length six, `-+--++` yields \(\operatorname{diag}(1,-1)\) and has sign product \(-1\), so the two alternating-rail terms cancel. In each case (1) vanishes.

Each of the four six-letter words
\[
\texttt{+--+--},\quad\texttt{-+--+-},\quad
\texttt{--+--+},\quad\texttt{------}
\]
has transfer product equal to the identity and sign product \(+1\). Appending any such word leaves \(Z_n(y)\) and \(\prod_i y_i\) unchanged. With fixed parity of \(n\), the alternating-rail sum can be assigned the same desired sign after extending. Starting from the six sharpness witnesses proves the least positive magnitude for **every** \(n\ge3\); starting from the two zero witnesses proves singularity at exactly all multiples of three.

**5. Independent zero-frequency families.** For \(n=6k+3\), start with `--+`, and for \(n=6k+6\), start with `-+--++`. Append any \(k\) of the four identity words independently. The resulting \(4^k\) distinct choices of \(y\) all satisfy \(Z_n(y)=0\). In even length their total sign product is \(-1\), so the alternating-rail sum vanishes as well. For each such \(y\), arbitrary \(r_i\) and \(a_i\) give \(2^{2n}\) distinct edge frequencies via \(b_i=y_i r_i r_{i+1}a_i\). All these frequencies are distinct and have zero multipliers. This proves the asserted lower bound.

**6. Operator conclusion.** The normalized characters of the Boolean edge group form an orthonormal basis of the counting-measure \(\ell^2\) space, and the unnormalized convolution operator is diagonal on them with eigenvalues \(W_n(\omega)\). The just-established exact least nonzero magnitude gives the inverse and pseudoinverse norms.

## Verification

The standalone file `prism_walsh_verifier.py` uses Python standard-library integer arithmetic, independent enumeration of perfect matchings, and a full Walsh–Hadamard transform for \(3\le n\le7\). It independently checks the transfer formula and six-site extension, witnesses and all four identity blocks; it also tests the arbitrary rung/rail sign parameterization exhaustively at \(n=3,6\), and propagated witnesses through \(n=201\). Running `python prism_walsh_verifier.py` prints `PRISM_WALSH_EXACT_TESTS_PASS` on success. The complete transforms contain 192 zeros at \(n=3\) and 124,928 zeros at \(n=6\), and none in the tested other lengths. These finite checks corroborate, but do not replace, the all-length argument.

## Relationship to prior work

Brauch, Kézdy and Snevily (2014) apply discrete Fourier analysis to perfect-matching detection in bipartite graphs, involving a Fourier transform of a circular-lock polynomial and an uncertainty inequality. Their full fifteen-page paper does not supply edge-incidence Boolean Walsh multiplier classifications for cyclic prisms. Lekshmi and West (2020) give the unsigned perfect-matching total for prisms and Möbius ladders, consistent with the count used here. The signed all-frequency classification and mod-four spectral gap are not consequences of that unsigned count alone.

The odd-length case is equivalent, after the paired-horizontal decomposition, to Walsh sums for independent sets of an ordinary cycle; that case is already covered by an earlier cycle-independent-set classification. The genuinely additional content here lies in the even-prism alternating-rail terms, their constrained sign product, the mod-four positive spectral gap at multiples of six, and the resulting full even-length inverse-stability classification.

## Limitations

No formula for the **exact number** of zero frequencies is asserted, only the constructive lower bound. Endpoint \(\ell^1\) and \(\ell^\infty\) inverse norms are not determined. The result concerns the ordinary edge-incidence group of simple prisms, not Möbius ladders or general cylindrical grids. Priority comparison is bounded: the full text of the directly relevant 2020 enumeration paper was unavailable for inspection, and an earlier signed-dimer formulation might exist. Independent mathematical validation has not been performed.

## References

1. T. M. Brauch, A. E. Kézdy and H. S. Snevily, *The Combinatorial Nullstellensatz and DFT on Perfect Matchings in Bipartite Graphs*, Ars Combinatoria **114** (2014), 461–475, first publicly dated 2014-04-30. https://combinatorialpress.com/article/ars/Volume%20114/volume-114-paper-43.pdf
2. R. S. Lekshmi and D. B. West, *The Number of Perfect Matchings in Möbius Ladders and Prisms*, arXiv:2003.09602, first submitted 2020-03-21. https://arxiv.org/abs/2003.09602
