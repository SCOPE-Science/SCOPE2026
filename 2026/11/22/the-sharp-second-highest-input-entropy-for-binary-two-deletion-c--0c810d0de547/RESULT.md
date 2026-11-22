# The sharp second-highest input entropy for binary two-deletion channels

## Finding

For every integer \(n\ge2\), consider the binary channel that transmits a uniformly chosen word of length \(n+2\) and deletes a uniformly chosen unordered pair of positions. For a received word \(y\in\{0,1\}^{n}\), write \(H_{D,2}(y)\) for the Shannon entropy (in bits) of the transmitted word conditional on observing \(y\). Let \(A_n\) be the alternating binary word beginning with zero and \(\overline A_n\) its complement. Set

\[
f(t)=t\log_2 t\quad(t>0),\qquad f(0)=0,\qquad
c_n=(6\log_2 3-8)n+6-6\log_2 3,
\]
\[
a_n=\left\lfloor\frac{n+4}{2}\right\rfloor,\qquad
b_n=\left\lceil\frac{n+4}{2}\right\rceil,\qquad
Z_n=4\binom{n+2}{2},
\]
\[
\Delta_n=c_n+f(a_n)+f(b_n)-f(n+1).
\]

Then the **strict second-highest** value of \(H_{D,2}\) among all received words (the maximum over nonalternating words) is

\[
H^{(2)}_n=H_{D,2}(A_n)-\frac{\Delta_n}{Z_n}.
\]

Equality holds *exactly* for the words whose run-length sequence consists of a single run of length two, all other runs having length one, with the counts of singleton runs on the two sides differing by at most one. Consequently the second-highest level is attained by exactly two words when \(n\) is even and exactly four words when \(n\) is odd. The gap is positive, and

\[
\lim_{n\to\infty}n\bigl(H_{D,2}(A_n)-H_n^{(2)}\bigr)
=\frac{6\log_2 3-9}{2}>0.
\]

This is a sharp all-length **stability refinement** of the previously established alternating-word maximum, not a new claim that alternating words maximize entropy.

## Assumptions and scope

Every input word of length \(n+2\) has equal prior probability. Independently, every unordered pair of deleted positions is equally likely. An embedding \(e(y,x)\) is the number of strictly increasing selections of \(n\) positions in \(x\) spelling \(y\); selections, not distinct subsequences, are counted. The posterior normalization is \(Z_n\). The alphabet is binary; there are exactly two deletions and no insertions or substitutions. The theorem is for all integers \(n\ge2\); for \(n=1\) both received words maximize entropy and there is no strict second-highest level.

For a binary word, a run is a maximal constant block. The run-length list and starting bit uniquely describe it. In the equality characterization, if the unique double run has \(s_0\) singleton runs before it and \(s_1\) after it, then \(s_0+s_1=n-2\) and \(\lvert s_0-s_1\rvert\le1\).

## Proof

**1. Reduction to an embedding functional.** Define

\[
\Phi(y)=\sum_{x\in\{0,1\}^{n+2}} f(e(y,x)).
\]

Summing embedding counts by first choosing the two deleted positions and then assigning two independently free bits yields \(\sum_x e(y,x)=Z_n\). Bayes' rule therefore gives

\[
H_{D,2}(y)=\log_2 Z_n-\Phi(y)/Z_n.
\]

Hence maximizing entropy is the same as minimizing \(\Phi\). Ma and Zhang [1, Lemmas 2.1 and 3.1] supply an exact run formula, which we state explicitly. Among all runs of \(y\), list those of length at least two, in order, as \(u_1,\ldots,u_q\). Put \(U=\sum_j u_j\), and let \(s_0,\ldots,s_q\) count singleton runs before, between, and after these nonsingleton runs. Define

\[
B_n=f(3)+4n,\qquad h_n(r)=f\!\left(\binom{r+2}{2}\right)+(2n-r)f(r+1).
\]

For \(q\ge1\), put \(w_0=u_1+s_0+1\), \(w_q=u_q+s_q+1\), and \(w_j=u_j+u_{j+1}+s_j+1\) for \(1\le j<q\). Their formula is

\[
\Phi(y)=(n-U)B_n+\sum_{j=1}^{q}h_n(u_j)+\sum_{j=0}^{q}f(w_j).
\tag{1}
\]

For \(q=0\), both alternating words have

\[
\Phi(A_n)=nB_n+f(n+1).
\tag{2}
\]

**2. Cost of a nonsingleton run.** The same paper proves for integers \(2\le r\le n\)

\[
h_n(r)-rB_n\ge c_n,
\tag{3}
\]

with equality at \(r=2\) and strict inequality for \(r>2\). The strict part follows from the displayed adjacent-increment bound in [1, Section 3.2]: for \(r\ge3\),

\[
h_n(r)-h_n(r-1)-B_n
\ge (6\log_2 3-8)n+(4-3\log_2 3)r
\ge (3\log_2 3-4)n>0.
\]

The second comparison uses \(r\le n\) and \(4-3\log_2 3<0\); positivity uses \(3^3>2^4\). Direct substitution gives \(h_n(2)-2B_n=c_n\). The cited increment bound is obtained by convexity of \(f\); [1] proves the full formula and the inequality for the stated integer range.

**3. Exactly one nonsingleton run.** For \(q=1\), write its length as \(r\ge2\). The sum of the two weights in (1) is \(n+r+2\). For any integer \(S\ge2\), strict convexity of \(f\) makes

\[
F(S)=f(\lfloor S/2\rfloor)+f(\lceil S/2\rceil)
\]

its minimum over positive integer pairs with sum \(S\). Moreover \(F(S)\) is strictly increasing in \(S\). From (1) and (3),

\[
\Phi(y)-nB_n\ge c_n+F(n+r+2)\ge c_n+F(n+4),
\tag{4}
\]

and equality requires \(r=2\) and weights as balanced as possible. For \(r=2\), these weights are \(3+s_0\) and \(3+s_1\), and \(s_0+s_1=n-2\). Hence equality in (4) is equivalent to \(\lvert s_0-s_1\rvert\le1\). These words exist for every \(n\ge2\), and their value is exactly \(nB_n+c_n+f(a_n)+f(b_n)\).

**4. At least two nonsingleton runs.** We show that no such word reaches (4). Here \(q\ge2\) implies \(n\ge4\). From (1), (3), and \(\sum_{j=0}^q w_j=n+U+q+1\ge n+3q+1\), Jensen's inequality gives

\[
\Phi(y)-nB_n\ge G_n(q),\qquad
G_n(t)=tc_n+(n+3t+1)\log_2\frac{n+3t+1}{t+1}.
\tag{5}
\]

Indeed \(x\mapsto x\log_2(x/(q+1))\) is increasing for \(x\ge q+1\), so the larger actual sum of weights can be replaced by \(n+3q+1\). For real \(t\ge1\), differentiation gives

\[
G'_n(t)=c_n+3\log_2\left(3+\frac{n-2}{t+1}\right)
-\frac{n-2}{(t+1)\ln2}.
\]

The elementary inequalities \(\log_2 3>19/12\) (because \(3^{12}>2^{19}\)) and \(\ln2>2/3\) imply

\[
c_n>\tfrac32n-\tfrac72,\qquad
G'_n(t)>\tfrac34n-2\ge1\qquad(n\ge4,\ t\ge1).
\tag{6}
\]

The logarithmic term omitted in this lower bound is positive. Thus \(G_n(q)\ge G_n(2)>G_n(1)+1\) for \(q\ge2\). Meanwhile \(G_n(1)=c_n+(n+4)\log_2((n+4)/2)\). If \(n\) is even, strict convexity gives \(F(n+4)=(n+4)\log_2((n+4)/2)\). If \(n\) is odd, Taylor's theorem with \(f''(x)=1/(x\ln2)\), applied at arguments separated by one, yields

\[
0<F(n+4)-(n+4)\log_2((n+4)/2)
\le \frac{1}{4\lfloor(n+4)/2\rfloor\ln2}<1.
\tag{7}
\]

Here \(n\ge4\) ensures the floor in (7) is at least four. Combining (5)--(7),

\[
\Phi(y)-nB_n\ge G_n(q)>c_n+F(n+4).
\]

This excludes every \(q\ge2\) word. When \(n=2,3\) such words cannot occur, so the result follows for all \(n\ge2\).

**5. Entropy, count, and limiting gap.** Subtracting (2) from the unique minimum among nonalternating words yields \(\Delta_n\) as stated; division by \(Z_n\) gives the exact entropy gap. Alternating words are strictly optimal by [1, Theorem 2.2], so \(\Delta_n>0\). The run-list characterization has two choices of starting bit, and either one balanced position (even \(n\)) or two balanced positions (odd \(n\)). Finally, \(f(a_n)+f(b_n)=(n+4)\log_2((n+4)/2)+O(1/n)\), so

\[
\Delta_n=(6\log_2 3-9)n+3\log_2 n+O(1),\qquad Z_n=2(n+1)(n+2),
\]

which proves the limit. This completes the argument.

## Verification

Two standalone Python 3 programs accompany the theorem. `verify_direct.py` counts embeddings with a state-by-state subsequence dynamic program and compares the exact integer products \(Q(y)=\prod_{x:e(y,x)>0}e(y,x)^{e(y,x)}\) for every binary word of received lengths two through eight, including all equality cases. `verify_run.py` separately evaluates the run identity (1) using integer exponentiation and enumerates every binary received word through length fifteen, asserting the exact second value and all attaining words. Both return an explicit PASS marker and use only Python's standard library.

The computations are finite sanity checks, not the proof for arbitrary lengths. The all-length argument is (1)--(7), including the strict derivative and equality checks.

## Relationship to prior work

Ma and Zhang [1] already prove that the alternating words and their complements are the **unique global maximizers** for all received lengths. In particular, that maximality is not a new claim. Their Section 3 gives the run identity and inequalities used above. Their Section 6 and publicly supplied `results.json` [2] report exact finite runner-up examples, but not the all-length second-level formula or the equality classification stated here. The new conclusion requires a comparison between a balanced single double run and *every* configuration with at least two nonsingleton runs, a comparison not contained in the stated global-maximizer theorem.

Singhvi, Sabary, Bar-Lev and Yaakobi [3] characterize a different extreme, the minimum for the two-deletion conditional input entropy, and provide general multiplicity formulas. Their result does not imply the exact second-highest level. The latest inspected material and indexed mathematical search did not show a prior all-length sharp second-level theorem. This is a bounded comparison, not a guarantee of historical priority.

## Limitations

The conclusion applies only to uniform-input binary channels with exactly two deletions and the posterior entropy defined above. It does not assert corresponding results for nonuniform inputs, other alphabets, three deletions, or insertion channels. The proof uses the published run identity and adjacent-increment inequality from [1], whose material statements and proof were inspected. Independent scholarly review has not been performed; an unindexed equivalent stability statement could predate this account. Finite runner-up examples in [2] are existing evidence, not newly discovered observations.

## References

[1] H. Ma and W. Zhang, *Maximal input entropy for binary two-deletion and two-insertion channels*, arXiv:2611.01064v1, first public 2026-10-31, Sections 2--3 and 6. https://arxiv.org/pdf/2611.01064

[2] H. Ma and W. Zhang, source ancillary `results.json` associated with arXiv:2611.01064v1. https://arxiv.org/src/2611.01064v1/anc/results.json

[3] S. Singhvi, O. Sabary, D. Bar-Lev, and E. Yaakobi, *Conditional Entropies of k-Deletion/Insertion Channels*, IEEE Transactions on Information Theory 71 (2025), 6503--6516; preprint arXiv:2407.10026v2. https://arxiv.org/abs/2407.10026
