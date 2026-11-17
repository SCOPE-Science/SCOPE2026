# Gaussian and two-jump Poisson laws for three-symbol permutation-burst spheres

## Finding
Let \(q\ge3\) and \(n\ge3\). For \(x\in\{0,\ldots,q-1\}^n\), let \(B(x)\) be the number of **distinct** outputs obtained by permuting exactly one contiguous three-coordinate window, with the identity permutation permitted. Define
\[
E_i=\mathbf1\{x_i=x_{i+1}\},\quad
F_i=\mathbf1\{x_i=x_{i+2}\},\quad
H_i=\mathbf1\{x_i=x_{i+1}=x_{i+2}\},
\]
\(U=\sum_{i=1}^{n-1}E_i\), \(V=\sum_{i=1}^{n-2}F_i\), and \(H=\sum_{i=1}^{n-2}H_i\). Then the **exact sphere-deficit identity** is
\[
D(x):=4n-6-B(x)=5U+3V-2(E_1+E_{n-1})-4H. \tag{1}
\]
The reference \(4n-6\) is the attained maximum for \(q\ge3\). If \(X\) has independent uniform \(q\)-ary coordinates, its moments are exactly
\[
\mathbb E B(X)=4n-6-\frac{8n-15}{q}+\frac{4(n-2)}{q^2}, \tag{2}
\]
\[
\operatorname{Var}(B(X))
=\frac{(q-1)\bigl(34nq^2-88nq+48n-75q^2+208q-128\bigr)}{q^4}. \tag{3}
\]
For every fixed \(q\ge3\), as \(n\to\infty\),
\[
\frac{B(X)-\mathbb EB(X)}{\sqrt{n\sigma_q^2}}\ \Longrightarrow\ N(0,1),\qquad
\sigma_q^2=\frac{2(q-1)(17q^2-44q+24)}{q^4}>0. \tag{4}
\]
There is a different limiting regime if \(q=q_n\to\infty\) and \(n/q_n\to\lambda\in[0,\infty)\):
\[
D(X)\ \Longrightarrow\ 5P_\lambda+3Q_\lambda, \tag{5}
\]
where \(P_\lambda,Q_\lambda\) are **independent** Poisson random variables with mean \(\lambda\). In particular the limiting deficit has probability-generating function \(\exp\{\lambda(z^5-1)+\lambda(z^3-1)\}\), mean \(8\lambda\), and variance \(34\lambda\). Thus a growing alphabet produces a two-jump compound-Poisson law, rather than the fixed-alphabet Gaussian fluctuations.

## Assumptions and scope
The coordinates of the word are linearly ordered; no window wraps around. One operation means an arbitrary permutation of one window of **exactly three** positions, and identical outputs are counted once. The word length satisfies \(n\ge3\); all finite-moment formulas hold for integer \(q\ge3\), without prime-power assumptions. Random letters are independent and uniform. The Gaussian statement fixes \(q\), whereas the Poisson statement permits \(q\) to grow with \(n\) and requires a finite limit of \(n/q\). The maximum \(4n-6\) is attained by any word whose consecutive triples have three different symbols (possible precisely in the stated alphabet range).

## Proof
**Step 1: unique output classification.** Every nonidentity permutation of a three-position window changes either exactly two coordinates, or all three. The two-coordinate cases are (a) one adjacent unequal pair exchanged, counted once for each \(i\in\{1,\ldots,n-1\}\) with \(x_i\ne x_{i+1}\), and (b) unequal endpoints exchanged at distance two, counted once for each \(i\in\{1,\ldots,n-2\}\) with \(x_i\ne x_{i+2}\). Outputs that change all three coordinates are possible precisely when the three symbols are pairwise distinct, in which case there are exactly two such output permutations. These categories cannot collide: the changed-coordinate set determines the operation's effective support, and within that support each output is uniquely specified. Therefore
\[
B(x)=1+\sum_{i=1}^{n-1}(1-E_i)+\sum_{i=1}^{n-2}(1-F_i)
+2\sum_{i=1}^{n-2}\mathbf1\{x_i,x_{i+1},x_{i+2}\text{ pairwise distinct}\}. \tag{6}
\]
For each triple,
\[
\mathbf1\{\text{not pairwise distinct}\}=E_i+E_{i+1}+F_i-2H_i. \tag{7}
\]
Indeed the right side is zero if all symbols differ, one if exactly two coincide, and \(3-2=1\) if all three coincide. Substituting (7) into (6) gives (1). Also every term in (6) is bounded by its all-distinct value, proving the sharp maximum \(4n-6\).

**Step 2: exact moments.** Write \(D=S-4H\), where
\[
S=\sum_{i=1}^{n-1}c_iE_i+3\sum_{i=1}^{n-2}F_i,\qquad
c_i=\begin{cases}3,&i=1\text{ or }i=n-1,\\5,&2\le i\le n-2.\end{cases} \tag{8}
\]
Each pair-equality indicator has mean \(1/q\), and each triple-equality indicator has mean \(1/q^2\); this yields (2). Two *distinct* pair-equality indicators are independent: their edge constraints form a forest with at most two edges, and each has joint probability \(1/q^2\). Thus
\[
\operatorname{Var}(S)=\frac{(34n-75)(q-1)}{q^2}. \tag{9}
\]
A pair-equality indicator has nonzero covariance with \(H_i\) only when both of its endpoints belong to triple \(i\), in which case it is \((q-1)/q^3\). Summing the coefficients gives
\[
\operatorname{Cov}(S,H)=\frac{(13n-30)(q-1)}{q^3}. \tag{10}
\]
Different \(H_i,H_j\) are independent for \(|i-j|\ge2\). For adjacent triples, their covariance is \((q-1)/q^4\), so
\[
\operatorname{Var}(H)=\frac{(n-2)(q^2-1)+2(n-3)(q-1)}{q^4}. \tag{11}
\]
Expanding \(\operatorname{Var}(S-4H)\) using (9)--(11) gives (3) exactly, including \(n=3\).

**Step 3: fixed-alphabet Gaussian law.** Equation (6) writes \(B(X)=1+\sum_{i=1}^{n-2}G_i+\mathbf1\{X_{n-1}\ne X_n\}\), where
\[
G_i=\mathbf1\{X_i\ne X_{i+1}\}+\mathbf1\{X_i\ne X_{i+2}\}
+2\mathbf1\{X_i,X_{i+1},X_{i+2}\text{ pairwise distinct}\}.
\]
The stationary bounded sequence \((G_i)\) is two-dependent. Equation (3) gives asymptotic variance \(\sigma_q^2n\), and \(17q^2-44q+24>0\) for \(q\ge3\). A blocking proof of the two-dependent central limit theorem applies: retain blocks of length \(\lfloor n^{1/3}\rfloor\) separated by two discarded summands. Retained block sums are independent; their centered absolute values are \(O(n^{1/3})=o(\sqrt n)\), while the discarded sum has variance \(O(n^{2/3})\) by finite dependence. Lindeberg's theorem for the independent blocks, followed by the negligible-discard estimate and the bounded terminal term, proves (4).

**Step 4: sparse-collision Poisson law.** Regard \(E_i\) and \(F_i\) as indicators of equality constraints on edges of lengths one and two in a line graph with \(n\) vertices. Each edge has probability \(1/q\). For fixed nonnegative integers \(r,s\), expand \(\mathbb E[(U)_r(V)_s]\) into ordered choices of distinct edges of the two respective types. A fixed chosen edge graph has \(c\) connected components on \(v\) incident vertices, hence all equalities hold with probability \(q^{-(v-c)}\). Configurations of \(r+s\) pairwise vertex-disjoint edges contribute \((n/q)^{r+s}(1+o(1))\). Each connected component containing at least two edges has at least three vertices, only \(O(n)\) possible placements for each fixed shape, and probability at most \(q^{-2}\); its contribution vanishes since \(n/q^2\to0\). There are finitely many shapes for fixed \(r,s\). Therefore the mixed factorial moments converge to \(\lambda^{r+s}\), the mixed factorial moments of independent \(\operatorname{Pois}(\lambda)\) variables, so \((U,V)\) converges jointly to \((P_\lambda,Q_\lambda)\). Finally \(\mathbb E(E_1+E_{n-1})=2/q\to0\) and \(\mathbb EH=(n-2)/q^2\to0\). The correction terms in (1) thus vanish in probability, giving (5). The limiting generating function, mean, and variance follow by independence.

## Verification
The accompanying standalone Python 3 checker computes actual output sets by permuting every length-three window. It compares each set size with (1), and enumerates full input spaces to compare exact rational means and variances with (2)--(3). Its successful replay produced `CERTIFICATE_OK direct_channel_words= 195317 exact_moment_profiles= 16`. This finite replay checks local counting and algebra, not the infinite-limit arguments; the Gaussian and Poisson claims follow from Steps 3 and 4.

To reproduce: run `python3 check.py` in the directory containing this document and the checker.

## Relationship to prior work
Chen and Milenkovic (2026) introduce substring-permutation burst correction and derive a binary sphere-volume decomposition and expected size with a concentration argument. They explicitly leave larger alphabets for future work. Related general-alphabet deterministic sphere-volume and binary three-window formulas are already known; neither those deterministic formulas nor the binary moment special case is claimed here. The distinct contribution of this finding is the **full nonbinary finite dispersion** and the **two-type joint rare-collision limit**, which identifies the exact compound-Poisson jump weights \(3\) and \(5\), alongside the fixed-alphabet Gaussian regime. The result concerns local window permutations, not the Ulam distance on global permutations.

## Limitations
The alphabet is uniform i.i.d., windows have exactly three positions, and there is a single operation. The theorem does not establish compound-Poisson limits for arbitrary window lengths, nonuniform or dependent sources, or coding-rate improvements. The integer-valued limiting law does not imply finite-\(n\) independence of the two collision counts. All statements are mathematical derivations with finite reproducibility tests, not independently certified priority or proof.

## References
1. Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, first public October 11, 2026, https://arxiv.org/html/2610.15701v1 (especially Sections I, II and V).
