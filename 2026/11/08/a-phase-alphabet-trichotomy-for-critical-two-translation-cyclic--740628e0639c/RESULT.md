# A phase-alphabet trichotomy for critical two-translation cyclic Gabor bases

## Finding

Let \(N=2M\ge2\), let \(k\in\{1,\dots,N-1\}\), and let \(q\ge2\) be an integer. For a length-\(N\) window with phases in the \(q\)-th roots of unity, consider the \(N\) vectors obtained from two translations (by \(0\) and \(k\)) and all even frequency modulations. Write \(d=\gcd(N,k)\), and \(t=N/d\), the additive order of \(k\) modulo \(N\).

**Theorem.** The normalized vectors form an orthonormal basis for some such window if and only if precisely one of the following admissible cases holds:

\[
\begin{array}{c|c|c}
  t \pmod 4 & \text{restriction on }q & \text{number of admissible windows}\\\hline
  0 & 2\mid q & 2^d q^M\\
  2 & 4\mid q & 2^d q^M\\
  1,3 & \text{none} & 0.
\end{array}
\]

For \(t\equiv0\pmod4\) and odd \(q\), or \(t\equiv2\pmod4\) and \(4\nmid q\), there are also zero admissible windows. In fact, odd \(t\) excludes **every** constant-modulus complex window, without an alphabet restriction. If phases may vary freely in the unit circle, every even-\(t\) case has exactly \(2^d\) connected components of admissible windows, each a torus of real dimension \(M\).

## Assumptions and scope

All coordinate indices and congruences of indices are modulo \(N\). Let \(\mu_q=\{\exp(2\pi i a/q):0\le a<q\}\), and define \(g=(g(j))_{j\in\mathbb Z_N}\in\mu_q^N\). Set

\[
(T_b g)(j)=g(j-b),\qquad (M_{2a}g)(j)=e^{2\pi i (2a)j/N}g(j).
\]

The candidate orthonormal family is

\[
\mathcal G_{N,k}(g)=\left\{N^{-1/2}M_{2a}T_b g:\;0\le a<M,\ b\in\{0,k\}\right\}\subset\mathbb C^N.
\]

The inner product is the ordinary Hermitian inner product. The window count is **literal**, not a count modulo global phase, cyclic shift, or any other symmetry. All \(N,k,q\) in the displayed ranges are covered; the conclusion does not require that \(\{0,k\}\) be a subgroup.

## Proof

**Step 1: exact orthogonality condition.** Because \(|g(j)|=1\), two distinct even modulations of the same translate are orthogonal: their inner product is a complete nontrivial geometric sum over \(\mathbb Z_N\). For vectors from the two different translates, multiplication by a common modulation reduces their inner product to the Fourier transform at an even frequency of

\[
c(j)=\overline{g(j)}\,g(j-k),\qquad j\in\mathbb Z_N.
\]

As \(e^{2\pi i(2a)(j+M)/N}=e^{2\pi i(2a)j/N}\), this complete set of \(M\) inner products vanishes exactly when

\[
c(j)+c(j+M)=0\qquad(0\le j<M).
\]

Indeed the \(M\)-point Fourier transform is invertible. Define the *half-cycle phase ratio*

\[
H(j)=\frac{g(j+M)}{g(j)}.
\]

Since \(g\) is nowhere zero, the cross condition becomes

\[
\frac{c(j+M)}{c(j)}=\overline{H(j)}\,H(j-k)=-1
\qquad\Longleftrightarrow\qquad H(j-k)=-H(j).
\tag{1}
\]

The displayed equivalence applies to all \(j\in\mathbb Z_N\), by the \(M\)-periodic nature of the paired condition. Conversely, (1) implies all cross inner products vanish; the family has exactly \(N\) unit vectors and therefore is an orthonormal basis. This reduction is an **if and only if** statement, not merely a sufficient construction.

**Step 2: orbit obstruction and phase rigidity.** Addition by \(k\) partitions \(\mathbb Z_N\) into exactly \(d=\gcd(N,k)\) cycles of length \(t=N/d\). Alternating the sign in (1) around a cycle excludes odd \(t\). Suppose \(t\) is even. Write \(k=du\) with \(u\) invertible modulo \(t\); then \(u\) is odd. The index displacement \(M=dt/2\) is realized by \(h\) successive \(k\)-steps on each orbit, with

\[
h\equiv(t/2)u^{-1}\pmod t,
\qquad h\equiv t/2\pmod2.
\]

Consequently (1) implies \(H(j+M)=(-1)^{t/2}H(j)\). But the definition of \(H\), without using (1), also gives \(H(j+M)=H(j)^{-1}\). Thus

\[
H(j)^2=(-1)^{t/2}.\tag{2}
\]

If \(t\equiv0\pmod4\), all ratios must belong to \(\{1,-1\}\); if \(t\equiv2\pmod4\), to \(\{i,-i\}\). In \(\mu_q\), the first case is possible precisely when \(2\mid q\), and the second precisely when \(4\mid q\).

**Step 3: sufficiency, completeness and counting.** For every admissible even-\(t\) case, choose independently one of the two square roots in (2) at one site of each of the \(d\) cycles; propagate \(H\) by the sign change in (1). The congruence for \(h\) shows that this produces exactly the reciprocal relation \(H(j+M)=H(j)^{-1}\) on every cycle. Next independently select the \(M\) phases \(g(0),\ldots,g(M-1)\in\mu_q\) and set

\[
g(j+M)=H(j)g(j),\qquad 0\le j<M.
\]

The resulting window has its prescribed ratios everywhere and satisfies (1). Conversely, each admissible window uniquely determines these \(d\) initial ratio signs and \(M\) first-half phases. This bijection proves the exact count \(2^d q^M\). With \(\mu_q\) replaced by the full unit circle, the ratio signs are still discrete by (2), while each of the \(M\) first-half phases is unconstrained; the resulting parameter space is precisely a disjoint union of \(2^d\) copies of \((S^1)^M\). The proof covers all stated values of \(N,k,q\).

## Verification

The standalone `CHECK.py` independently implements two exact finite tests: a cross-Gram Fourier-pair criterion in root-of-unity exponent arithmetic and the ratio recurrence (1). It exhaustively evaluates \(39{,}640\) phase arrays across \(32\) small parameter configurations, comparing the observed count against \(2^d q^M\) or zero as appropriate. It additionally constructs witnesses and tests the necessary-and-sufficient condition in \(1{,}734\) parameter configurations with even \(N\le34\). Invoke `python3 CHECK.py` with the standard Python library. These are finite consistency checks; the unrestricted theorem follows from the preceding algebraic proof, not from extrapolation.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez study block equivalence and diagonal equivalence for finite Gabor frame operators with subgroup modulation sets, including constructions using special translation subgroups. Their results explain why subgroup modulations are structurally tractable, but their stated theorems do not give the necessary-and-sufficient phase-alphabet criterion, exact window count or topological classification for the **specific critical** system above with arbitrary \(k\). Nicola classifies Gabor bases generated by windows with extremal ambiguity-function localization; this is a different additional hypothesis and does not classify all full-support phase-only windows for the present index-two design. Earlier prime-field Gabor orthonormal-basis work treats different ambient groups and lattice questions.

The generic Gabor biorthogonality mechanism and finite Fourier inversion used in Step 1 are standard; they are not claimed as new. The claimed contribution is their sharp combination into the all-length alphabet trichotomy with complete solution count and connected-component structure. Search nonexhaustiveness leaves open the possibility of an older equivalent treatment in polyphase-filter or finite-Gabor literature.

## Limitations

The classification is limited to even cyclic lengths, the two translations \(\{0,k\}\), all **even** frequency modulations, and constant-modulus windows. It makes no claim about other critical time-frequency patterns, arbitrary nonconstant-amplitude windows, localization quality, noise stability, or a new theorem for infinite-dimensional Gabor bases. The computation checks are not proofs of the all-length claims, and no independent mathematical validation has occurred.

## References

1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139 (first publicly posted May 15, 2026), especially Theorem 1.1, Theorem 1.3 and Sections 3–5. https://arxiv.org/abs/2605.16139
2. F. Nicola, *Maximally localized Gabor orthonormal bases on locally compact Abelian groups*, arXiv:2305.02738 (2023), especially the classification of maximally localized windows. https://arxiv.org/abs/2305.02738
3. A. Iosevich and collaborators, *On Gabor orthonormal bases over finite prime fields*, arXiv:1712.09120 (2017). https://arxiv.org/abs/1712.09120
