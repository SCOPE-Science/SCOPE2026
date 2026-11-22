# Sharp fixed-index curvature frontier for the \(\tau\)-polynomials of high-girth regular graphs

## Finding

Fix integers \(d\ge3\) and \(j\ge2\). For every sequence of finite connected simple \(d\)-regular graphs \(G_n\) with girth tending to infinity, define \(c_i(G_n)\) by the chromatic rising-factorial expansion in the next section. The coefficient curvature ratio at every fixed index has an exact exponential limit:

\[
\lim_{n\to\infty}\left(\frac{c_j(G_n)^2}{c_{j-1}(G_n)c_{j+1}(G_n)}\right)^{1/|V(G_n)|}
=\Lambda_{d,j}:=\frac{t_d(j+1)^2}{t_d(j)t_d(j+2)}.
\]

The same limit holds with \(c_i\) replaced by \(\bar c_i=i!c_i\). This limit has the following **sharp strict sign classification**:

\[
\Lambda_{d,j}\begin{cases}<1,&2\le j\le d-2,\\>1,&j\ge d-1.\end{cases}
\]

The first range is empty for \(d=3\). Thus, for each fixed index \(j\) and sufficiently large girth, the two coefficient sequences fail log-concavity at \(j\) exactly in the first range, and satisfy the strict log-concavity inequality at \(j\) in the second. In particular, fixed-index curvature in cubic graphs is positive at every \(j\ge2\), while higher regular degrees have a sharp eventual sign reversal at the index \(d-1\). Any finite collection of fixed indices can be treated simultaneously by taking the maximum of the respective girth thresholds.

## Assumptions and scope

All graphs are finite, connected, simple and \(d\)-regular, and the parameter \(d\ge3\) is fixed. Let \(N=|V(G)|\), with chromatic polynomial

\[
P_G(x)=\sum_{i=0}^{N}(-1)^{N-i}c_i(G)x^{\langle i\rangle},\qquad x^{\langle i\rangle}=\prod_{h=0}^{i-1}(x+h),\quad x^{\langle0\rangle}=1.
\]

The \(\tau\)-polynomial is \(\sum_i c_i(G)z^i\), and its augmented variant has coefficients \(\bar c_i(G)=i!c_i(G)\). Let \(b_d=d/2-1\). Define for real \(x\ge1\)

\[
t_d(x)=\begin{cases}
(d-1)\left(\dfrac{(d-1)^2}{(d-1)^2-x}\right)^{b_d},&1\le x\le d-1,\\
x\left(\dfrac{x}{x-1}\right)^{b_d},&x>d-1.
\end{cases}
\]

These formulas agree at the seam. The high-girth limit theorem of Bencs and Csikvári is an external input, explicitly cited below; the new fixed-index recovery and threshold classification follow by the proof given here. The index \(j\) is fixed before taking girth to infinity.

## Proof

**Step 1: coefficient extraction via Tutte evaluations.** Put \(Q_G(k)=(-1)^N P_G(-k)\) for positive integers \(k\). Substitution into the rising-factorial expansion gives the exact falling-factorial identity

\[
Q_G(k)=\sum_{i=0}^{k}c_i(G)\,k_{\underline i},\qquad
c_j(G)=\frac1{j!}\sum_{k=0}^{j}(-1)^{j-k}\binom{j}{k}Q_G(k).
\]

The second equality is finite-difference inversion. For connected graphs, chromatic–Tutte duality gives \(Q_G(k)=kT_G(k+1,0)\), and \(Q_G(0)=0\). The theorem of Bencs and Csikvári [1], applied at each fixed integer \(k\ge1\), yields

\[
\lim_{n\to\infty}Q_{G_n}(k)^{1/|V(G_n)|}=t_d(k+1).
\]

**Step 2: dominance of the final finite difference term.** The function \(t_d(x)\) is strictly increasing for \(x\ge2\): on the first branch this is immediate; on the second branch its logarithmic derivative is \((2x-d)/(2x(x-1))>0\) for \(x\ge d-1\). Hence for any fixed \(1\le k<j\), \(Q_{G_n}(k)/Q_{G_n}(j)\to0\) exponentially fast. The exact finite sum thus implies

\[
c_j(G_n)=\frac{Q_{G_n}(j)}{j!}(1+o(1))
\]

for each fixed \(j\ge1\). In particular these coefficients are eventually positive. Taking the ratios at \(j-1,j,j+1\) and then \(|V(G_n)|\)-th roots proves the announced limit for \(c_i\). For the augmented sequence, the exact ratio is

\[
\frac{\bar c_j^2}{\bar c_{j-1}\bar c_{j+1}}
=\frac{j}{j+1}\frac{c_j^2}{c_{j-1}c_{j+1}},
\]

so its exponential limit is unchanged.

**Step 3: sharp sign of the exponential curvature.** Write \(f(x)=\log t_d(x)\) and \(h=1/[2(d-1)]\). Differentiation in the two regions gives

\[
f'(x)=\begin{cases}
\dfrac{d/2-1}{(d-1)^2-x},&x\le d-1,\\
\dfrac{2x-d}{2x(x-1)},&x\ge d-1.
\end{cases}
\]

The derivative is continuous across the seam. On \([2,d-1]\), \(f'\) is strictly increasing whenever the interval has positive length, reaching \(h\) at \(d-1\). On the second region an exact identity holds:

\[
f'(x)-h=\frac{(x-d+1)(d-x)}{2(d-1)x(x-1)}.
\]

Consequently \(f'(x)>h\) on \((d-1,d)\), whereas \(f'(x)<h\) for \(x>d\). Moreover, on \([d,\infty)\),

\[
f''(x)=\frac{-2x^2+2dx-d}{2x^2(x-1)^2}<0
\]

because \(2x^2-2dx+d=2x(x-d)+d>0\). Now \(\log\Lambda_{d,j}=\int_j^{j+1}f'(x)\,dx-\int_{j+1}^{j+2}f'(x)\,dx\). If \(2\le j\le d-3\), monotonic growth of the derivative on the first region makes this quantity strictly negative. If \(j=d-2\) (possible for \(d\ge4\)), the first integral on \([d-2,d-1]\) is strictly less than \(h\), while the second on \([d-1,d]\) is strictly greater than \(h\), again yielding a negative value. At \(j=d-1\), the first integral is strictly greater than \(h\) and the second on \([d,d+1]\) is strictly less, yielding a positive value. For every \(j\ge d\), strict concavity on \([d,\infty)\) likewise yields a positive value. These exhaust all \(d\ge3\), \(j\ge2\), including \(d=3,j=2\).

**Step 4: eventual strict inequalities.** Since \(\Lambda_{d,j}\ne1\), the proven positive exponential limit forces the ordinary curvature ratio itself to be strictly below or above one for all sufficiently large \(n\) in any high-girth sequence. Equivalently, if no uniform girth threshold existed, there would be a contrary sequence of connected simple \(d\)-regular graphs with girth tending to infinity. The same argument applies to the augmented coefficients using their identical exponential limit. This completes the proof.

## Verification

The standalone standard-library script `verify.py` checks the exact rational square \(\Lambda_{d,j}^2\) for every integer \(3\le d\le100\), \(2\le j\le d+24\), without numerical tolerances; it also independently verifies the sample values \(\Lambda_{3,2}^2=2187/2048\) and \(\Lambda_{4,2}^2=3969/4096\). This is a finite consistency test of the closed formula, not a proof of the unrestricted curvature sign or of the Tutte limit theorem. Those follow from Step 3 and cited [1].

## Relationship to prior work

Bencs and Csikvári [1] proved the asymptotic Tutte-evaluation formula employed as an input in Step 1; their theorem alone is about evaluations, not about sign classifications for rising-factorial coefficient curvature. Zhang and Dong [2] established asymptotic non-log-concavity at \(j=2\) for every \(d\ge4\), including the augmented coefficients. The present result recovers that case but adds an exact all-fixed-index sign frontier, the return to strictly positive curvature at \(j=d-1\), and positive fixed-index curvature throughout cubic degree. These further conclusions require the new coefficient-dominance argument and the piecewise derivative comparison. Graph-join real-rootedness results do not cover high-girth regular graphs by an established implication.

## Limitations

The girth thresholds are existential and depend on the fixed pair \((d,j)\); there is no effective bound here, and there is no assertion uniform in indices growing with graph order. Positive curvature at every *fixed* index does not establish global log-concavity or unimodality for entire coefficient sequences. The external Tutte-growth theorem is used as published rather than reproved. Historical priority remains subject to independent literature review, especially unindexed work on \(\tau\)-polynomials.

## References

[1] F. Bencs and P. Csikvári, *Evaluations of Tutte polynomials of regular graphs*, arXiv:2105.06798, first publicly available 2021-05-14, https://arxiv.org/abs/2105.06798 .

[2] M. Zhang and F. Dong, *Non-log-concave \(\tau\)-polynomials of regular graphs*, arXiv:2611.11056v1, first publicly available 2026-11-08, https://arxiv.org/abs/2611.11056 .

[3] F. Brenti, earlier \(\tau\)-polynomial definitions and questions (1992), as referenced in [2].
