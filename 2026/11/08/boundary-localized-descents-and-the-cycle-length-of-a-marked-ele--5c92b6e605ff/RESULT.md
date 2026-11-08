# Boundary-localized descents and the cycle length of a marked element

## Finding
Let \(\Pi\) be uniform on the permutations of \([n]\), \(n\ge3\). Write \(K\) for the length of the cycle containing \(1\), \(D_i=\mathbf1\{\Pi(i)>\Pi(i+1)\}\) for \(1\le i<n\), and \(D=\sum_{i=1}^{n-1}D_i\). Then \(K\) is uniform on \(\{1,\ldots,n\}\), and **the entire conditional first-moment effect of \(K\) on descents is localized at the first comparison**:
\[
\Pr(D_i=1\mid K=k)=\tfrac12\quad (2\le i<n,\ 1\le k\le n),
\]
whereas
\[
\Pr(D_1=1\mid K=k)=
\begin{cases}
0,& k=1,\\
\dfrac{n+1}{2(n-1)},&k=2,\\
\dfrac{n}{2(n-1)},&3\le k\le n-1,\\
\dfrac12,&k=n.
\end{cases}
\]
The middle range is empty for \(n=3\). Consequently
\[
\operatorname{Cov}(K,D)=\operatorname{Cov}(K,D_1)=
\frac{n^2-3n+4}{4n(n-1)}>0,
\qquad
\lim_{n\to\infty}\operatorname{Cov}(K,D)=\frac14.
\]
Moreover, using the classical uniform-permutation Eulerian variance and the uniform distribution of \(K\),
\[\operatorname{Corr}(K,D)\sim 3n^{-3/2}.\]

## Assumptions and scope
All permutations of \([n]\) have probability \(1/n!\). The symbol \(\Pi(i)\) denotes the value at position \(i\), and the cycle containing \(1\) is defined by iteration of \(\Pi\) as a map. \(D_i\) is an **ordinary linear descent** indicator, not a cycle descent or cyclic wrap-around descent. All conditional events \(K=k\) have positive probability. The conditional statement concerns individual descent probabilities (and their sum), not the joint law of the full descent-indicator vector. The theorem holds for every integer \(n\ge3\), including its boundary cases.

## Proof
**1. Tagged-cycle sampling.** For a prescribed \(k\), choose the other \(k-1\) members \(S\) of the marked cycle uniformly from \(\{2,\ldots,n\}\), arrange the resulting \(k\)-cycle uniformly, and put an independent uniform permutation on the other \(n-k\) labels. Each \(k\) accounts for exactly \(\binom{n-1}{k-1}(k-1)!(n-k)!=(n-1)!\) permutations. Hence \(\Pr(K=k)=1/n\).

**2. Every position after the first.** Fix \(2\le i<n\), and let \(\tau\) exchange the consecutive labels \(i,i+1\). The map \(\Pi\mapsto\tau\Pi\tau\) preserves \(K\) and its conditional uniform distribution. Except when the unordered image-pair \(\{\Pi(i),\Pi(i+1)\}\) equals \(\{i,i+1\}\), this conjugation reverses the descent comparison: swapping adjacent *values* cannot change any other pair's order. The two exceptional events are \(E_{\rm fix}=\{\Pi(i)=i,\Pi(i+1)=i+1\}\) and \(E_{\rm swap}=\{\Pi(i)=i+1,\Pi(i+1)=i\}\), each left unchanged by the conjugation. They have equal conditional probabilities: both must occur in the independent complementary permutation, and for \(n-k\ge2\) their common probability is
\[
\frac{(n-k)(n-k-1)}{(n-1)(n-2)}\cdot\frac1{(n-k)(n-k-1)}
=\frac1{(n-1)(n-2)}.
\]
For \(n-k<2\) both events are impossible. Pairing under conjugation therefore gives
\(\Pr(D_i=1\mid K=k)=\tfrac12+\tfrac12(\Pr(E_{\rm swap}\mid K=k)-\Pr(E_{\rm fix}\mid K=k))=\tfrac12\).

**3. First position.** Put \(Y=\Pi(1)\) and \(Z=\Pi(2)\). If \(k=1\), then \(Y=1<Z\), so the probability is zero. For \(k\ge2\), \(Y\) is uniform on \(\{2,\ldots,n\}\). When \(k=2\), if \(Y=2\) then \(Z=1\); if \(Y=y\ge3\), label \(2\) is outside the marked cycle and \(Z\) is uniform on \(\{2,\ldots,n\}\setminus\{y\}\). Thus
\[
\Pr(Y>Z\mid K=2)=\frac1{n-1}\left(1+\sum_{y=3}^n\frac{y-2}{n-2}\right)
=\frac{n+1}{2(n-1)}.
\]
When \(3\le k\le n-1\), the case \(Y=2\) has \(Y<Z\). Conditional on \(Y=y\ge3\), the two values \(Z=1\) and \(Z=2\) each have probability \(1/(n-2)\): the first comes from label \(2\) occupying the last position in the marked cycle, and the second from label \(2\) remaining outside that cycle and being fixed by the complementary permutation. The \(n-3\) other possible values \(z\in\{3,\ldots,n\}\setminus\{y\}\) have equal probabilities \((n-4)/((n-2)(n-3))\) by relabeling symmetry. Therefore
\[
\Pr(Y>Z\mid K=k)=\frac1{n-1}\sum_{y=3}^n\left(\frac2{n-2}+\frac{(y-3)(n-4)}{(n-2)(n-3)}\right)=\frac{n}{2(n-1)}.
\]
For \(k=n\), if \(Y=2\), then \(Z\ge3\); for \(Y=y\ge3\), \(Z\) is uniform on \([n]\setminus\{2,y\}\), giving \(\Pr(Z<y\mid Y=y,K=n)=(y-2)/(n-2)\). Summation over \(y\) gives \(1/2\).

**4. Covariance and asymptotic correlation.** From the first two steps,
\(\mathbb E[D\mid K=k]=(n-2)/2+\Pr(D_1=1\mid K=k)\).
Summing the four-case formula against the uniform distribution of \(K\), with \(\mathbb E[K]=(n+1)/2\) and \(\mathbb E[D_1]=1/2\), yields
\[
\operatorname{Cov}(K,D)=\frac1n\sum_{k=1}^n\left(k-\frac{n+1}{2}\right)\Pr(D_1=1\mid K=k)
=\frac{n^2-3n+4}{4n(n-1)}.
\]
Its numerator is positive for \(n\ge3\). The identities \(\operatorname{Var}(K)=(n^2-1)/12\) and \(\operatorname{Var}(D)=(n+1)/12\) then imply the stated \(3n^{-3/2}\) correlation asymptotic.

## Verification
The included standalone `verify.py` exhaustively enumerates all permutations for \(3\le n\le9\), checks every conditional local descent probability as an exact rational number and verifies the covariance for each size. It also verifies consistency of the probability and covariance formulas for all \(3\le n\le300\). Its recorded result is `OK: 1195 exact rational assertions; 409110 complete permutation objects; n=3..9, plus symbolic formulas checked for n=3..300`. The infinite theorem rests on the proof, **not** on the finite checks. Reproduce by running `python3 verify.py` with Python's standard library.

## Relationship to prior work
Conger (2005) derives the joint distribution of the **first image value** and the total number of descents, not the cycle length containing that first label. Reutenauer (1989, predecessor to Gessel–Reutenauer 1993) counts permutations by **unmarked cycle type** and descent set, whereas here the cycle containing the specified label is marked. Those unmarked summaries do not themselves identify the marked length: for \(n=4\), permutations \((1,4,2,3)\) and \((2,3,1,4)\) have the same cycle type \((3,1)\) and descent set \(\{2\}\), but their cycles through \(1\) have lengths \(1\) and \(3\), respectively. Diaconis–McGrath–Pitman (1991/1995) studies cycle type and descents in riffle shuffles. Earlier localization of fixed-point/descent dependence covers part of the \(K=1\) boundary, but it does not imply the \(K=2\), interior plateau, and \(K=n\) distinctions or their covariance. The assessed result is the combined complete marked-cycle local profile and its exact aggregate consequence, not those classical marginals.

## Limitations
No conditional independence of the whole suffix descent process is asserted. The result is for uniform permutations and a distinguished smallest label, not arbitrary Ewens/Mallows parameters or all marked labels. The accessible literature comparison cannot rule out an implicit formula in less easily searchable distinguished-cycle enumerations. The mathematical proof and finite checker have not received independent specialist validation.

## References
- Mark Conger, *A Refinement of the Eulerian Numbers, and the Joint Distribution of \(\pi(1)\) and \(\mathrm{Des}(\pi)\) in \(S_n\)*, first public arXiv version August 5, 2005, https://arxiv.org/abs/math/0508112.
- Christophe Reutenauer, *Number of Permutations with Given Descent Set and Cycle Structure*, Séminaire Lotharingien de Combinatoire B21h (1989), https://www.mat.univie.ac.at/~slc/s/s21reut.html; later jointly published with Ira Gessel, *Counting Permutations with Given Cycle Structure and Descent Set*, JCTA 64 (1993), DOI 10.1016/0097-3165(93)90095-P.
- Persi Diaconis, Michael McGrath, Jim Pitman, *Cycles and Descents of Random Permutations*, Stanford report (October 1991), https://statistics.stanford.edu/technical-reports/cycles-and-descents-random-permutations; expanded as *Riffle Shuffles, Cycles, and Descents*, Combinatorica 15 (1995), DOI 10.1007/BF01294457.
