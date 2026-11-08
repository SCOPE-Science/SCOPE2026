# A sharp three-quarter bispectral uniqueness threshold on finite abelian groups

## Finding

**Theorem (sharp universal spectral-erasure threshold).** Let \(G\) be any finite abelian group, \(N=|G|\), and let \(f,g:G\to\mathbb R\). If the Fourier transform of \(f\) vanishes at fewer than \(N/4\) characters, then equality of its first, second and third ordinary autocorrelations with those of \(g\) forces \(g\) to be a translate of \(f\). The threshold is universally sharp: on \(\mathbb Z_8\), two strictly positive, nontranslation-equivalent real signals share all three autocorrelations while each has exactly two of its eight Fourier coefficients equal to zero. Tensorization supplies such strictly positive counterexamples on \(\mathbb Z_8\times H\) for *every* finite abelian group \(H\), always with exactly one quarter of the Fourier spectrum erased.

Equivalently, the bispectrum together with Fourier magnitudes and the mean distinguishes all real signals with Fourier support strictly exceeding three quarters of the dual group, uniformly in group structure and the arrangement of zeros. Strict inequality cannot be replaced by a weak inequality.

## Assumptions and scope

Write the finite abelian dual group \(A=\widehat G\) additively, with identity \(0\). Normalize the Fourier transform by
\[
\widehat f(a)=\sum_{x\in G}f(x)\overline{a(x)},\qquad
f(x)=\frac1N\sum_{a\in A}\widehat f(a)a(x).
\]
For \(j=1,2,3\), use the *ordinary unnormalized* correlations
\[
\rho_1(f)=\sum_x f(x),\qquad
\rho_2(f)(t)=\sum_x f(x)f(x+t),\qquad
\rho_3(f)(s,t)=\sum_x f(x)f(x+s)f(x+t).
\]
No genericity, coefficient separation, positivity, cyclicity, or Fourier-support geometry is assumed for the uniqueness assertion; only real-valuedness and the strict support-size condition are required. The counterexamples are stronger: they are strictly positive.

## Proof

**Step 1: a sharp dense partial-character extension lemma.** Let \(A\) be a finite abelian group of order \(N\), let \(E\subseteq A\) contain \(0\), and suppose \(r=|A\setminus E|<N/4\). Let \(w:E\to\mathbb T\) satisfy \(w(0)=1\) and
\[
 w(a+b)=w(a)w(b)\quad\text{whenever }a,b,a+b\in E.
\]
Then \(w\) extends **uniquely** to a character on all of \(A\).

For any \(t\in A\), put \(E_t=E\cap(E-t)\). Thus \(|E_t|\ge N-2r>2r\). On \(E_t\) consider the quotient \(Q_t(a)=w(a+t)/w(a)\). If \(a,b\in E_t\) and \(b-a\in E\), applying the partial-character identity to \(a+(b-a)=b\) and \((a+t)+(b-a)=b+t\) gives \(Q_t(a)=Q_t(b)\). Join any two distinct vertices in \(E_t\) whenever their difference is in \(E\). Each vertex has at most \(r\) nonneighbors, since there are only \(r\) differences outside \(E\). Hence every connected component has size at least \(|E_t|-r\). Two different components would require \(|E_t|\ge2(|E_t|-r)\), contrary to \(|E_t|>2r\). The graph is connected, so \(Q_t\) is constant. Define \(W(t)=Q_t(a)\) for any \(a\in E_t\).

For \(t,u\in A\), the three sets \(E\), \(E-t\), \(E-t-u\) intersect because their intersection has size at least \(N-3r>0\). Choose \(a\) in this intersection. Then
\[
W(t+u)=\frac{w(a+t+u)}{w(a)}
=\frac{w(a+t+u)}{w(a+t)}\frac{w(a+t)}{w(a)}=W(u)W(t).
\]
Moreover, for \(t\in E\), use \(a=0\in E_t\) to obtain \(W(t)=w(t)\). Thus \(W\) is a character extending \(w\). An extension is unique because the same quotient at any \(a\in E_t\) is dictated by its values on \(E\).

**Step 2: apply the lemma to Fourier phases.** The Fourier transforms of the correlations are
\[
\widehat{\rho_1(f)}=\widehat f(0),\quad
\widehat{\rho_2(f)}(a)=\widehat f(a)\widehat f(-a)=|\widehat f(a)|^2,
\]
\[
\widehat{\rho_3(f)}(a,b)=\widehat f(a)\widehat f(b)\widehat f(-a-b).
\]
Because the signals are real, \(\widehat f(-a)=\overline{\widehat f(a)}\), and likewise for \(g\). Equality of the first two autocorrelations implies that their common nonvanishing Fourier support \(S\) has the same moduli, that the phase ratio \(w(a)=\widehat g(a)/\widehat f(a)\) lies in \(\mathbb T\), and that \(w(-a)=w(a)^{-1}\) for \(a\in S\). Mean equality gives \(w(0)=1\) if \(0\in S\).

If \(0\notin S\), enlarge to \(E=S\cup\{0\}\) and set \(w(0)=1\); otherwise put \(E=S\). The complement still has fewer than \(N/4\) elements. Equality of third autocorrelations yields \(w(a+b)=w(a)w(b)\) for every \(a,b,a+b\in S\). The same equality remains valid for triples involving the adjoined identity, trivially when an input is zero, and by \(w(-a)=w(a)^{-1}\) when \(a+b=0\). The lemma gives a character \(W\) of \(A\) extending \(w\). Finite Pontryagin duality identifies \(W(a)=a(x_0)\) for some \(x_0\in G\). Thus \(\widehat g(a)=a(x_0)\widehat f(a)\) for every \(a\) including zeros, and Fourier inversion gives \(g(x)=f(x+x_0)\). This proves uniqueness.

**Step 3: exact sharp counterexample.** On \(G=\mathbb Z_8\), let \(S=\{0,1,3,4,5,7\}\), and prescribe Fourier transforms
\[
F(0)=6,\quad F(k)=1\;(k\in S\setminus\{0\}),\quad F(2)=F(6)=0.
\]
Set \(z=e^{i\pi/5}\), and assign phase factors
\[
w(0)=w(4)=1,\quad w(1)=w(5)=z,\quad w(3)=w(7)=z^{-1}.
\]
Put \(B(k)=w(k)F(k)\) on \(S\) and \(B(2)=B(6)=0\). Both Fourier coefficient families obey the conjugate-symmetry identities \(F(-k)=\overline{F(k)}\), \(B(-k)=\overline{B(k)}\), and so invert to real signals \(f,g\). Since each has DC coefficient \(6\), while the total absolute value of its five non-DC coefficients is \(5\), the inverse Fourier series gives \(f(x),g(x)\ge(6-5)/8=1/8\) for every \(x\), establishing strict positivity.

The **only** unordered triples \((a,b,c)\) from \(S\) with \(a+b+c\equiv0\pmod8\) are
\[
(0,0,0),\ (0,1,7),\ (0,3,5),\ (0,4,4),\ (1,3,4),\ (4,5,7).
\]
For each, \(w(a)w(b)w(c)=1\). Therefore the entire bispectra agree; the first correlations agree by equality at zero, and the second agree by equal Fourier moduli. However, if \(g\) were a translate of \(f\), the ratio at Fourier index one would be an eighth root of unity. It is \(e^{i\pi/5}\), which is not such a root. Thus these two signals are not translates, with exactly \(2/8=1/4\) of their Fourier coefficients zero.

**Step 4: families in unbounded dimensions.** For every finite abelian \(H\), let \(h(y)=1+\mathbf1_{\{0\}}(y)\), which is strictly positive and has nowhere-vanishing Fourier transform (equal to \(|H|+1\) at the trivial character and \(1\) at all other characters). Set \(f_H(x,y)=f(x)h(y)\) and \(g_H(x,y)=g(x)h(y)\) on \(\mathbb Z_8\times H\). Their order-\(j\) correlations factor into the product of the correlations of their two factors for each \(j=1,2,3\), so they coincide. Their Fourier zero sets are exactly \(\{2,6\}\times\widehat H\), i.e. one quarter of the dual group. If a translation equated them, summing that identity over the \(H\)-coordinate (where \(\sum_y h(y)>0\)) would force its \(\mathbb Z_8\) component to translate \(f\) to \(g\), impossible. This proves the universal sharpness statement.

## Verification

The accompanying dependency-free `CHECK.py` independently enumerates every allowed zero-sum triple of the six-frequency sharpness example, checks all phase exponents exactly as integers, reconstructs the two real inverse transforms numerically, checks strict positivity and all three correlations, tests nontranslation, and verifies a nontrivial product-group instance. It also exhaustively tests the dense partial-character extension statement for several small cyclic groups using finite-root phase alphabets and checks the graph cardinality inequalities for groups of small orders. These finite tests do not replace the general connectedness/three-intersection proof above. Run `python3 CHECK.py` with Python 3.9 or later; no external dependencies are required.

## Relationship to prior work

Agulnick and Busick-Warner (2026), Theorem 1.3 and Theorem B, provide general upper bounds on *autocorrelation order* based on how a Fourier support multiplicatively generates its ambient subgroup, and exhibit nonuniqueness for sparse spectra. Their analyzed statements do not give the uniform strict three-quarter density criterion for order three, or its positive sharpness examples at exactly one-quarter missing Fourier support. Casper and Orozco (2025/2026), in their Main Theorem and Section 2, reconstruct rational-valued functions using orders depending on group rank; their hypotheses and guarantee differ from an exact order-three cutoff for arbitrary real-valued functions with dense Fourier support. Jaming and Kolountzakis (2003) examine the triple-correlation reconstruction of *indicator functions* and cyclic structural cases, not the present arbitrary real-signal, all-finite-abelian density threshold. Bendory et al. (2017), Proposition II.1, give reconstruction under contiguous Fourier-band support assumptions, a different restriction from arbitrary-location erasures. The phase-ratio reduction is standard; the distinctive statements here are the sharp group-independent density threshold, the dense partial-character extension proof, and the equality counterexamples with strictly positive signals.

## Limitations

The guarantee is noiseless and assumes exact full second- and third-order autocorrelation data and real-valued signals. It does not quantify stability under measurement noise, sparsity-aware reconstruction complexity, or an optimal threshold when the dual-group structure or a specific zero pattern is prescribed. The sharpness counterexamples use unrestricted real coefficient values, not rational-valued or binary-valued signals. Literature overlap has been checked against selected primary research, but no comprehensive priority guarantee or independent mathematical audit is claimed.

## References

1. A. Agulnick and T. Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups* (first publicly posted 2026-04-14), arXiv:2604.13310, https://arxiv.org/abs/2604.13310, especially Theorem 1.3, Theorem B and Sections 2–4.
2. P. Jaming and M. N. Kolountzakis, *Reconstruction of functions from their triple correlations* (2003), arXiv:math/0207051, https://arxiv.org/abs/math/0207051, particularly Section 3.
3. W. R. Casper and B. Orozco, *Reconstructing Rational Functions on Finite Abelian Groups with Higher Autocorrelations* (first posted 2025-03-26; revised 2026), arXiv:2503.21022, https://arxiv.org/abs/2503.21022, especially the Main Theorem and Section 2.
4. T. Bendory, N. Boumal, C. Ma, Z. Zhao, and A. Singer, *Bispectrum Inversion with Application to Multireference Alignment* (2017), arXiv:1705.00641, https://arxiv.org/abs/1705.00641, especially Proposition II.1.
