# Parity dichotomy in the reversal Hamming spectrum of Sturmian integral lifts

## Finding

For every irrational \(0<\alpha<1\), integer \(m\ge2\), and \(n\ge1\), let \(Y_\alpha\) be the bilateral Sturmian subshift of slope \(\alpha\), and let
\[
X_{\alpha,m}=\bigl\{x\in(\mathbb Z/m\mathbb Z)^\mathbb Z:
 (x_{i+1}-x_i\bmod m)_{i\in\mathbb Z}\in Y_\alpha\bigr\}.
\]
Write \(\mathcal L_n\) for its length-\(n\) language, \(\operatorname{rev}(v)\) for reversal, and
\[
\mathcal H_m(n)=\{n^{-1}d_H(u,\operatorname{rev}(v)):u,v\in\mathcal L_n\}.
\]
**The complete asymptotic Hamming spectrum** has the following parity dichotomy in Hausdorff distance on \([0,1]\):
\[
\boxed{\lim_{n\to\infty}\mathcal H_m(n)=
\begin{cases}
\{1-1/m\},&m\text{ odd},\\
[1-2/m,\,1],&m\text{ even}.
\end{cases}}
\]
In particular, the minimum number of symbol changes needed to turn a length-\(n\) factor into the reversal of another factor satisfies
\[
\boxed{\lim_{n\to\infty}\frac1n\min_{u,v\in\mathcal L_n}d_H(u,\operatorname{rev}(v))=
\begin{cases}1-1/m,&m\text{ odd},\\1-2/m,&m\text{ even}.\end{cases}}
\]
For every irrational slope this is a uniform \(o(n)\) approximation. If \(\alpha\) has bounded continued-fraction coefficients (in particular, if it is quadratic irrational), the error in the *un-normalized* Hamming spectrum and in its minimum is \(O_{\alpha,m}(\log(n+1))\). For odd \(m\), **every** ordered pair \(u,v\in\mathcal L_n\) has Hamming distance \((1-1/m)n+O_{\alpha,m}(\log(n+1))\) in the bounded-type case.

## Assumptions and scope

Use the usual mechanical Sturmian language: its binary words arise, for generic phases \(\rho\), from \(y_i=\lfloor\rho+(i+1)\alpha\rfloor-\lfloor\rho+i\alpha\rfloor\). No restriction beyond irrationality is needed for the limiting theorem. The \(m\)-symbol lift uses *oriented*, not undirected, symbol equality under the ordinary Hamming metric. Reversal does not include a relabeling or a cyclic alphabet shift. The Hausdorff limit means each point of each finite spectrum approaches the displayed compact set and each point of that set is approximated by a point of the finite spectrum at **every sufficiently large** length. The letters are the labeled residues \(0,1,\dots,m-1\).

The same full language admits the circle model
\[
x_i(\theta)=\lfloor\theta+i\alpha\rfloor\bmod m,
\qquad \theta\in\mathbb R/m\mathbb Z,
\]
with generic phases avoiding integer partition boundaries. Indeed, taking differences recovers the mechanical word; conversely every mechanical factor and every initial residue lift to one of these phases. Boundary codings are limits of generic phases and add no finite words.

## Proof

**1. Exact matching geometry.** Put \(\mathbb T_m=\mathbb R/m\mathbb Z\), with un-normalized arc length \(|\mathbb T_m|=m\), and define \(\chi(t)=\lfloor t\rfloor\bmod m\), away from integer boundaries. For two generic phases \(\theta,\psi\), set
\[
C=\theta+\psi+(n-1)\alpha\pmod m,
\qquad z_i=\theta+i\alpha\pmod m.
\]
Then \(x_i(\theta)=x_{n-1-i}(\psi)\) exactly when \(z_i\) belongs to
\[
E_C=\{z\in\mathbb T_m:\chi(z)=\chi(C-z)\}.
\]
The length of the portion of \(E_C\) in the cell \([j,j+1)\) is the overlap of two unit arcs. Hence, using \((s)_+=\max\{s,0\}\),
\[
\ell_m(C):=|E_C|=
\sum_{j=0}^{m-1}\sum_{k\in\mathbb Z}
\bigl(1-|C-(2j+1)-km|\bigr)_+.
\tag{1}
\]
At most finitely many summands are nonzero at any \(C\). Also, \(E_C\) is a union of at most \(2m\) arcs (including the possibility of wrapping at the circle origin).

**2. The parity law.** The ordinary triangular tents \((1-|C-r|)_+\), indexed by all integer centers \(r\), sum to one for every real \(C\). If \(m\) is odd, the residues \(2j+1\bmod m\) run over all residues once, so equation (1) becomes
\[\boxed{\ell_m(C)=1\quad(m\text{ odd},\text{ every }C).}\]
If \(m\) is even, the odd residues occur twice and the even residues never occur. Summing the tents at odd integer centers gives \(\operatorname{dist}(C,2\mathbb Z)\), where the distance is in \([0,1]\). Therefore
\[\boxed{\ell_m(C)=2\operatorname{dist}(C,2\mathbb Z)
\quad(m\text{ even}).}\]
This has image exactly \([0,2]\). In both parity cases, the largest agreement-set measure is \(1\) (odd) or \(2\) (even).

**3. Uniform orbit counting.** Define the un-normalized arc discrepancy of the irrational rotation by \(\alpha\) on \(\mathbb T_m\) by
\[
D_{\alpha,m}(n)=\sup_{\theta,I}\left|
\#\{0\le i<n:\theta+i\alpha\in I\}
-\frac{n|I|}{m}\right|,
\]
where \(I\) ranges over arcs of \(\mathbb T_m\). By uniform distribution of irrational rotations, \(D_{\alpha,m}(n)=o(n)\). Equivalently, rescaling the circle to length one gives the rotation number \(\alpha/m\). For bounded-type \(\alpha\), also \(\alpha/m\) is badly approximable, and the continued-fraction/Ostrowski discrepancy estimate gives \(D_{\alpha,m}(n)=O_{\alpha,m}(\log(n+1))\).

The decomposition into at most \(2m\) arcs now yields for all generic phases, **uniformly** in \(\theta,\psi,n\),
\[
\left|d_H(x_{[0,n)}(\theta),\operatorname{rev}(x_{[0,n)}(\psi)))
-n\left(1-\frac{\ell_m(C)}m\right)\right|
\le 2mD_{\alpha,m}(n).
\tag{2}
\]
No boundary ambiguity is used: every finite factor of the language is realizable by a non-boundary phase, and for fixed \(C\), generic \(\theta\) gives such a phase pair via \(\psi=C-\theta-(n-1)\alpha\). The latter observation is important: **every** \(C\in\mathbb T_m\) is realized at every length, not merely along a subsequence.

**4. Exact limiting spectrum.** Equation (2) bounds the Hausdorff distance from \(\mathcal H_m(n)\) to the image of \(C\mapsto1-\ell_m(C)/m\) by \(2mD_{\alpha,m}(n)/n\). Step 2 identifies this image as the asserted singleton for odd \(m\), and as the full closed interval for even \(m\). Applying the same bound to the minimum of the two sets proves the sharp minimum limit and its quantitative logarithmic remainder. This completes the proof.

## Verification

Run `python3 CHECK.py` in a standard Python 3 environment. It uses exact fractions and integer phase partitions only, and performs 1,413 exact overlap/parity identity tests, 252 independent comparisons between rotation-generated and Fibonacci-substitution-generated finite languages, and 28 brute-force minimum-distance checks. These are finite consistency checks; statements for all lengths and irrational slopes follow from the proof above. In the checker \(\alpha\) is approximated for finite tests by the high-order Fibonacci ratio \(832040/2178309\); a separate substitution construction confirms the exact finite languages on the tested ranges. No computer evaluation is needed for the infinite result.

## Relationship to prior work

Kang and Jäger established strict ergodicity for the noble-means substitution lifts under modular-difference block codes, including the Fibonacci case. Their results and constructions concern minimality, unique ergodicity and finite permutation extensions, not Hamming separation from reversed languages. Berstel and Vuillon studied coding circle rotations by finite interval partitions and the resulting recodings through Sturmian words. Dvořáková and Pelantová analyzed reflection complexity, which counts words up to exact reversal and does not quantify *near* reversals. An earlier calculation for modular-difference lifts likewise determines the number of exact reversal classes; it implies short-length reversal obstructions but not a linear-distance lower bound or a complete asymptotic Hamming spectrum. The new claim is the parity-dependent **metric** statement, not these underlying coding, strict-ergodicity or exact-reflection results.

## Limitations

Historical priority is supported by targeted comparisons, not exhaustive indexing of all prior literature. A classical circle-interval overlap formula and the known discrepancy theorem are essential proof inputs; novelty lies in their sharp interpretation for the two-language reversal-distance spectrum. The result does **not** cover edit distance permitting insertions/deletions, alphabet relabeling, arbitrary permutative block codes, or non-Sturmian base shifts. No uniform logarithmic rate is claimed for irrational slopes of unbounded continued-fraction type. The finite checker is not an infinite proof. Independent mathematical validation has not been performed.

## References

1. Z. Kang and T. Jäger, *Permutative lifts of strictly ergodic subshifts*, arXiv:2609.01140, version 1 publicly available 1 September 2026; version 2, 2 November 2026. https://arxiv.org/abs/2609.01140
2. L. Dvořáková and E. Pelantová, *Reflection on the Reflection Complexity*, Theory of Computing Systems 70, article 35 (2026), 18 May 2026. https://doi.org/10.1007/s00224-026-10278-7
3. J. Berstel and L. Vuillon, *Coding rotations on intervals*, Theoretical Computer Science 281 (2002), 99–107. https://www-igm.univ-mlv.fr/~berstel/Articles/2002CodingRotations.pdf
4. L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences*, Wiley (1974), for classical circle discrepancy and bounded-type rotation estimates.
