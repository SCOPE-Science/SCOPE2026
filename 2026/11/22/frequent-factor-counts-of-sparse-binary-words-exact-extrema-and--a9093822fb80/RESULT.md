# Frequent-factor counts of sparse binary words: exact extrema and an atomic-continuous limit law

## Finding

For a finite word \(w\), let \(\operatorname{occ}_w(u)\) count overlapping starting-position occurrences of the **distinct, nonempty contiguous factor** \(u\), and put
\[
\Phi(w)=\#\{u:\ u\text{ is a nonempty factor of }w,\ \operatorname{occ}_w(u)>|u|\}.
\]
For every binary word containing exactly two ones, write uniquely
\[
w=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\quad N=a+b+c=|w|-2.
\]
Then the following exact formula holds, including \(N=0\):
\[
\boxed{\Phi(w)=1+\sum_{j=1}^{N}\mathbf 1_{\{\sum_{g\in\{a,b,c\}}(g-j+1)_+>j\}}},\qquad (x)_+=\max(x,0).
\]
For every \(N\ge0\), the sharp range endpoints over the \(\binom{N+2}{2}\) such words are
\[
\boxed{1+\left\lfloor\frac{N+2}{4}\right\rfloor\ \le\ \Phi(w)\ \le\ 1+\left\lfloor\frac N2\right\rfloor.}
\]
The lower endpoint is attained when \((a,b,c)\) is as balanced as possible; the upper endpoint is attained when all zeros occupy one gap.

Let \(W_n\) be chosen uniformly from binary words of length \(n\) containing exactly two ones. As \(n\to\infty\),
\[
\frac{\Phi(W_n)}n\ \Longrightarrow\ Y.
\]
The limiting law has one atom and an absolutely continuous part:
\[
\boxed{\mathbb P(Y=1/4)=1/16},\qquad
\boxed{f_Y(t)=\begin{cases}66t-12,&1/4<t<1/3,\\12-24t,&1/3<t<1/2,\\0,&\text{otherwise},\end{cases}}
\]
with no other atoms. Equivalently, its right-continuous distribution function is
\[
\boxed{F_Y(t)=\begin{cases}
0,&t<1/4,\\
33t^2-12t+1,&1/4\le t\le1/3,\\
-12t^2+12t-2,&1/3\le t\le1/2,\\
1,&t\ge1/2.
\end{cases}}
\]
The limiting first two moments, and hence the normalized limiting variance, are
\[
\boxed{\mathbb EY=\frac{187}{576}},\quad
\boxed{\mathbb EY^2=\frac{1499}{13824}},\quad
\boxed{\operatorname{Var}(Y)=\frac{1007}{331776}}.
\]
The same limits hold for the corresponding moments of \(\Phi(W_n)/n\).

## Assumptions and scope

All factors are linear (not cyclic), distinct by spelling (not by positional occurrence), and occurrence counts include overlaps. The strict comparison \(\operatorname{occ}_w(u)>|u|\) is essential. For the finite formula and sharp extrema, \(n=N+2\ge2\) is arbitrary. For the distributional assertion \(n\to\infty\) through integers, the two one-positions are uniformly chosen without replacement. A repeated factor must be interpreted according to the original linear word, without a terminal sentinel. The source is sparse: its Hamming weight is exactly two, not merely asymptotically two.

## Proof

**1. Complete finite factor classification.** A factor containing both ones occurs at most once, since the two marker positions are unique. A factor containing exactly one one occurs at most twice, so if its length is at least two it cannot occur more often than its own length. The one-letter factor \(1\) occurs twice and therefore always qualifies. Every remaining candidate has the form \(0^j\), and its occurrences are precisely the runs inside the three zero gaps. The count is
\[
\operatorname{occ}_w(0^j)=(a-j+1)_++(b-j+1)_++(c-j+1)_+.
\]
This expression decreases with \(j\), while the comparison threshold \(j\) increases. Hence qualifying powers of zero, if any, are exactly \(0^1,\ldots,0^L\), for a single cutoff \(L\), giving the first formula.

**2. Sharp finite extrema.** For every positive integer \(j\),
\[
\sum_{g\in\{a,b,c\}}(g-j+1)_+\ge N-3(j-1).
\]
Thus every \(j\) satisfying \(4j<N+3\) qualifies, and every word has at least \(1+\lfloor(N+2)/4\rfloor\) frequent factors. This bound is sharp: balance the three gaps, so each is either \(q\) or \(q+1\), with \(N=3q+r\), \(0\le r\le2\). The resulting zero-power occurrence count is \(N-3(j-1)\) for \(j\le q\), is \(r\) for \(j=q+1\), and is zero above. Its final qualifying index is exactly \(\lfloor(N+2)/4\rfloor\), also for the small cases \(q=0\).

For the other endpoint, whenever \(j\ge1\), the sum of positive run contributions is at most \((N-j+1)_+\): if there are any active gaps, the total contribution equals the sum of their lengths minus \((j-1)\) times their count. Consequently qualifying indices obey \(2j<N+1\), so \(L\le\lfloor N/2\rfloor\). Taking gaps \((N,0,0)\) attains every such index. Both bounds are sharp for every \(N\ge0\).

**3. Continuous root representation.** For \(N>0\), set \(x=(a/N,b/N,c/N)\) on the simplex \(\Delta=\{x_i\ge0,\sum x_i=1\}\) and define
\[
H_x(t)=\sum_{i=1}^3(x_i-t)_+-t,\qquad t\ge0.
\]
The function is continuous and strictly decreasing (its slope on every linear segment is at most \(-1\)); moreover \(H_x(0)=1\) and \(H_x(1)<0\). It has a unique root \(T(x)\in[1/4,1/2]\). This root is continuous as a function of \(x\), since perturbing \(x\) changes \(H_x\) by at most the \(\ell_1\) perturbation, and the inverse-root shift is no larger than the same perturbation.

The discrete sign test for \(0^j\) is \(H^{(N)}_x(j/N)>0\), where
\[
H^{(N)}_x(t)=\sum_{i=1}^3(x_i-t+N^{-1})_+-t.
\]
Pointwise, \(H_x(t)\le H_x^{(N)}(t)\le H_x(t)+3/N\). The monotonicity estimate implies their unique roots differ by at most \(3/N\), and replacing the root by the largest strictly positive integer-grid test loses at most one grid cell. Including the always-frequent factor \(1\) yields the uniform bound \(|\Phi(w)/N-T(x)|\le5/N\). Thus \(\Phi(w)/n\) and \(T(x)\) differ uniformly by \(O(N^{-1})\).

The \(\binom{N+2}{2}\) zero-gap triples form the complete uniform integer grid on \(\Delta\). Normalized Riemann sums therefore converge to normalized two-dimensional area on \(\Delta\), namely the Dirichlet\((1,1,1)\) distribution. By continuity of \(T\), the limit variable is \(Y=T(X)\) with \(X\) uniform on that simplex.

**4. Derivation of the mixed law.** The simplex has constant coordinate density two when described by \((x_1,x_2)\). First, if all three coordinates are at least \(1/4\), the root is exactly \(1/4\). Translating the simplex by \((1/4,1/4,1/4)\) leaves total mass \(1/4\), hence area ratio \((1/4)^2=1/16\). The boundary has zero area, so this is the only atomic contribution.

Away from the boundary, let \(k\in\{1,2\}\) be the number of coordinates strictly larger than the root \(t\). If \(k=2\), sort \(x_1\ge x_2\ge x_3\). Then \(x_3=1-3t\), \(t<x_2<3t/2\), and \(1/4<t<1/3\). There are six coordinate permutations. Multiplying simplex density two, the Jacobian \(|dx_3/dt|=3\), and the \(x_2\)-interval length \(t/2\) yields density \(18t\).

If \(k=1\), choose the unique largest coordinate (three choices). It equals \(2t\), while the two other coordinates sum to \(1-2t\) and each is at most \(t\). Their allowed interval length is \(4t-1\) when \(1/4<t<1/3\), and \(1-2t\) when \(1/3<t<1/2\). Multiplying by simplex density two, three coordinate choices, and Jacobian two yields respective densities \(12(4t-1)\) and \(12(1-2t)\). Adding the \(k=1\) and \(k=2\) contributions gives the displayed piecewise density. Direct integration, including the atom, gives the distribution function and rational moments. The atom plus density integrate to one.

**5. Moment convergence.** The finite bound in Step 2 gives \(0\le\Phi(W_n)/n\le(1+\lfloor N/2\rfloor)/(N+2)\le1\). Consequently weak convergence implies convergence of the first two moments, proving the asserted expectation and variance limits.

## Verification

The independent literal checker `verify.py` builds all substring multiplicities without using the zero-gap formula. It compared the claimed finite formula and both extrema for all \(1140\) length-composition instances with \(0\le N\le17\). It also compared normalized finite cutoffs to the continuous-root model for \(N\in\{19,30,61,100,150,225\}\), and integrated the density with exact rational arithmetic for normalization, mean, second moment, and variance. All checks passed; see `output.txt`. These finite checks do not prove the unbounded claims: Steps 1–5 provide the proof.

Reproduce with `python3 verify.py` using the Python standard library, with no external data or dependencies. The full source and captured output accompany this text.

## Relationship to prior work

Bals, Charalampopoulos, Lachish, Pissis, and Verbeek, *Text Indexing: From Reporting to Counting* (arXiv:2607.24043, first public 2026-07-27; ESA 2026), establish the general \(\Phi(w)\le|w|\) theorem and a construction with a growing alphabet. Their Theorem 1 and Proposition 6 address the unrestricted upper bound and witnesses, not the fixed-Hamming-weight-two statistic or its limiting distribution.

The public result *Fixed-binary asymptotic sharpness of the frequent-factor bound* (2026) extends the unrestricted extremal asymptotic to the binary alphabet via periodic de Bruijn words, but those sources have many ones and the assertion \(\max\Phi(w)/n\to1\) does not imply the law at fixed weight two. Related fixed-two-marker factor results concern other invariants, including minimal absent factors, not factors whose overlapping occurrence count exceeds their own length.

## Limitations

The distribution is for uniformly sampled words of weight exactly two; neither the fixed-weight-three law nor the regimes of marker weight increasing with length are settled here. The density describes only the limiting normalized count, not a complete finite-length probability mass function. No independent mathematical audit has been performed. Published sources were inspected as described in the accompanying review, but historical priority cannot be proved by database search and an unindexed equivalent remains possible.

## References

1. B. Bals, P. Charalampopoulos, O. Lachish, S. P. Pissis, H. Verbeek, *Text Indexing: From Reporting to Counting*, arXiv:2607.24043 (first version 2026-07-27), ESA 2026, Article 68, DOI: 10.4230/LIPIcs.ESA.2026.68. Full open text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol388-esa2026/html/LIPIcs.ESA.2026.68/LIPIcs.ESA.2026.68.html
2. *Fixed-binary asymptotic sharpness of the frequent-factor bound* (2026), public record and proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-fixed-binary-asymptotic-sharpness-of-the-frequent-factor-bound--18eac5e211b6/RESULT.md
3. *Minimal absent factors of two-marker binary words: exact counts and a limit law* (2026), related distinct invariant, public record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-minimal-absent-factors-of-two-marker-binary-words-exact-counts-a--e744971e8c41
