# Strict Fourier positivity and sharp stability of Motzkin sharp-peak profiles

## Finding
For each integer \(n\geq2\), let \(\mathcal M_n\) denote the ordinary (uncolored) Motzkin excursions of \(n\) unit steps \(U=(1,1)\), \(H=(1,0)\), and \(D=(1,-1)\). For \(P\in\mathcal M_n\), put \(e_i(P)=1\) if positions \(i,i+1\) form the adjacent sharp peak \(UD\), and zero otherwise, for \(1\leq i<n\). Set \(G_n=(\mathbb F_2)^{n-1}\) and define convolution on this group by \((T_nf)(x)=\sum_{P\in\mathcal M_n}f(x+e(P))\), counting multiplicities. For every frequency \(S\subseteq\{1,\ldots,n-1\}\), its unnormalized Walsh multiplier is
\[
W_n(S)=\sum_{P\in\mathcal M_n}(-1)^{\sum_{i\in S}e_i(P)}.
\]
Write \(M_n=|\mathcal M_n|\), and \(p_n=W_n(\{1,\ldots,n-1\})\). Then the entire spectrum satisfies the **sharp inequalities**
\[
\boxed{0\leq p_n\leq W_n(S)\leq M_n.}
\]
Here \(p_2=p_3=0\); for **every \(n\geq4\)** one has \(p_n>0\), and consequently \(T_n\) is strictly positive definite and invertible. For \(n\geq6\), the lower bound is attained only for the complete set \(S=\{1,\ldots,n-1\}\); the upper bound is always attained at the empty set. Furthermore,
\[
\|T_n^{-1}\|_{\ell^2\to\ell^2}=p_n^{-1},\qquad
\kappa_2(T_n)=\frac{M_n}{p_n}
\sim \frac{3\sqrt3}{2}\left(\frac32\right)^n.
\]
The finite exceptions are exact: \(T_2\) has Fourier rank one out of two, \(T_3\) has rank three out of four; no other orders are singular.

## Assumptions and scope
A Motzkin excursion begins at height zero, stays at nonnegative integer heights, and ends at height zero. A *sharp peak* is an immediately consecutive \(UD\) pair, regardless of its height; humps \(U H^kD\) with \(k>0\) do not count. A position \(i\) indexes the first step in \(UD\). Distinct paths with the same binary peak profile are counted separately. The Fourier transform is the unnormalized Walsh transform \(\widehat f(S)=\sum_{x\in G_n} f(x)(-1)^{\langle S,x\rangle}\). Operator norms and condition numbers use counting measure on the finite group, so no normalization factor is hidden.

## Proof
**1. Forcing separated peaks.** For any subset \(A\) of nonconsecutive starting positions, the paths with a sharp peak beginning at each position of \(A\) are in bijection with arbitrary Motzkin excursions of length \(n-2|A|\): delete each forced \(UD\) block. Its net height displacement is zero, so deletion and reinsertion preserve the nonnegative-excursion condition. Consecutive starting positions cannot both be peaks. Expanding each sign as \((-1)^{e_i}=1-2e_i\) therefore yields the exact all-frequency identity
\[
W_n(S)=\sum_{\substack{A\subseteq S\\A\text{ contains no consecutive integers}}}(-2)^{|A|}M_{n-2|A|}.\tag{1}
\]
No independence of peak events is presumed.

**2. The all-marked coefficient.** Put \(P(z)=\sum_{n\geq0}p_nz^n\), with \(p_0=p_1=1\). Splitting a nonempty excursion into an initial horizontal step followed by an excursion, or an initial \(UQD\) followed by an excursion, gives
\[
P=1+zP+z^2P(P-2).\tag{2}
\]
Indeed, the interior \(Q=\varnothing\) creates a sharp peak with sign \(-1\), whereas every nonempty interior carries its own signed peak weight; thus the signed interior contribution is \(P-2\). Coefficient comparison shows \(p_2=p_3=0\), \(p_4=p_5=p_6=1\), and, for \(n\geq3\),
\[
p_n=p_{n-1}+\sum_{j=1}^{n-3}p_jp_{n-2-j}.\tag{3}
\]
All terms on the right are nonnegative inductively. In particular \(p_n\geq p_{n-1}>0\) for every \(n\geq5\), so positivity begins at \(n=4\).

**3. Removing a marked coordinate.** Fix \(i\in S\). The difference \(W_n(S\setminus\{i\})-W_n(S)\) counts paths having a sharp peak at \(i\), weighted by all other marked sharp peaks, multiplied by two. Deleting that \(UD\) block identifies this weighted sum with \(W_{n-2}(S')\) for a subset \(S'\) of the \(n-3\) remaining peak-start coordinates: selected positions adjacent to \(i\) cannot be peaks and disappear; other selected positions shift naturally after deletion. Therefore
\[
W_n(S\setminus\{i\})-W_n(S)=2W_{n-2}(S').\tag{4}
\]
The lower-order multiplier on the right is nonnegative by simultaneous induction on \(n\). Thus removing marked coordinates never decreases \(W_n\). Starting with the fully marked set and successively deleting marks proves \(p_n\leq W_n(S)\). Starting from the empty set proves \(W_n(S)\leq W_n(\varnothing)=M_n\). When \(n\geq6\), the lower-order size is at least four, and every term \(W_{n-2}(S')>0\), making every deletion strict. The small sizes \(n=2,3\) have multipliers \((2,0)\) and \((4,2,2,0)\), respectively. (The statements are immediate for empty paths in induction bases \(n=0,1\).)

**4. Spectral consequences.** Walsh characters form an orthogonal eigenbasis of the real symmetric convolution operator. Its multipliers are all positive at \(n\geq4\), with exact smallest and largest values \(p_n\) and \(M_n\). The stated inverse norm, rank and condition number follow. Solving (2) for the branch analytic at zero gives
\[
P(z)=\frac{1-z+2z^2-\sqrt{(1-z)(1-2z)(1+z+2z^2)}}{2z^2}.
\]
At its unique dominant singularity \(z=1/2\), the singular term is \(-2\sqrt{1-2z}\), whence \(p_n\sim2^n/(\sqrt\pi\,n^{3/2})\). The ordinary Motzkin generating function is \(M(z)=(1-z-\sqrt{(1-3z)(1+z)})/(2z^2)\), with \(M_n\sim (3\sqrt3/(2\sqrt\pi))3^n n^{-3/2}\). Their ratio proves the asymptotic condition number.

## Verification
The independent standard-library checker `verify_peak_spectrum.py` reproduces **every** Walsh multiplier for each \(2\leq n\leq12\) by three different exact methods: direct full-path peak-profile enumeration followed by an integer Walsh–Hadamard transform, a height/last-up-step signed dynamic program, and formula (1) using independent sets of a path. It verifies 4,094 characters total, all inequalities and the exceptional ranks. This finite check tests the proof but is not substituted for the induction or asymptotic argument. Run `python3 verify_peak_spectrum.py` in the directory containing the checker; no external packages are required.

## Relationship to prior work
Sapounakis and Tsikouras [1, Proposition 3.6, page 8] explicitly count Motzkin paths by **total number of peaks**, so the all-marked univariate signed coefficient \(p_n\) can be obtained from their enumerators; its generating function is not claimed as a novel standalone result. Their statistic is position-free and does not give the simultaneous inequalities over all \(2^{n-1}\) positionwise signs or their strict Fourier rank and condition number. Ding and Du [2] give bijections and total hump enumerations, not the positionwise negative character. Tirrell's thesis [3, Section 1.4.4–1.4.6] uses negatively marked peaks to cancel paths **containing forbidden marked peaks**: its inclusion-exclusion gives coefficient \(-1\) for selecting a forbidden peak and weight zero for that peak, whereas Walsh signs require the coefficient \(-2\) and weight \(-1\). This distinction does not by itself settle the present positivity comparison. The published-finding corpus record [5] studies **up/down-step indicator positions** of Motzkin paths, not adjacency-based sharp-peak-start positions, and therefore concerns a distinct binary embedding and different spectra. General Motzkin polynomial methods [4] remain background.

## Limitations
Only ordinary one-color Motzkin excursions and adjacent sharp \(UD\) peaks are treated. No corresponding claim is established for colored, Schröder, altitude-filtered, hump, or unconstrained paths, or for non-Hilbert inverse norms. The aggregate peak distribution and its generating function occur in earlier literature; the mathematical content asserted here is the **simultaneous positionwise strict Walsh positivity, monotonicity under marking, unique minimizer at large order, and sharp spectral stability**. Earlier papers may contain equivalent multivariate specializations not located in the bounded comparison, especially material beyond the inspected portions of general weighted enumeration literature.

## References
[1] A. Sapounakis and P. Tsikouras, *Counting peaks and valleys in k-colored Motzkin paths*, Electronic Journal of Combinatorics **12** (2005), R16, published 2005-03-18, https://doi.org/10.37236/1913 (full primary PDF, especially pp. 2–8).

[2] Y. Ding and R. R. X. Du, *Counting Humps in Motzkin paths*, 2011, https://arxiv.org/abs/1109.2661 (full open text).

[3] J. O. Tirrell, *Orthogonal polynomials, lattice paths, and skew Young tableaux*, doctoral thesis, Brandeis University, 2016, https://people.brandeis.edu/~gessel/homepage/students/JordanTirrellThesis.pdf (Sections 1.4.4–1.4.6).

[4] R. Oste and J. Van der Jeugt, *Motzkin Paths, Motzkin Polynomials and Recurrence Relations*, Electronic Journal of Combinatorics (2015), https://doi.org/10.37236/4781 (background abstract).

[5] *The first post-cubic Walsh resonance and exact Fourier range projection for length-ten Motzkin paths*, published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-the-first-post-cubic-walsh-resonance-and-exact-fourier-range-pro--5e973760c6a6 (record summary compared for subject separation).
