# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Index-Level and Quantitative Obstructions to Every-\emph{n} Dependent-Coding
# Rates in the Gowers–Maurey Space, with a Sharp Repair along the Coding Set

## Abstract

We prove that two quantitative claims about the Gowers–Maurey hereditarily
indecomposable space $X_{GM}$ (1992 preprint / 1993 construction, $f(t) =
\log_2(t+1)$, sparse coding set $J$, coding function $\sigma$, norming set $D$)
cannot hold as literally stated: (a) an every-positive-integer-$n$ dependently
coded unconditional-constant growth law, and (b) the level-$\min J$ uniform
$D$-control envelope with a paired special functional. The obstruction is not a
failed estimate but a definitional index fact in the primary source
(math/9205204, verified HTML full text, §3): special functionals/vectors enter
the norming set $D$ and the implicit norm only for lengths $k \in K = \{j_2,
j_4, \dots\}$ (even $J$-indices), while $\min J = j_1$ has $J$-index $1$ (odd),
so $j_1 \in L \setminus K$. We add two quantitative obstructions: a coarsening
window $f(k)/f(n) \le 25/9$ violated across triple-exponential $K$-gaps, and an
explicit designated-special violation of any hoped $y$-level sub-bound by a
factor $\sqrt{F}/n$. We give the sharp repair: the $(1/3)f(k)^{1/2}$
unconditional-constant lower bound along the subsequence $k \in K$ with a base
case at $k_0 = \min K$ in place of $\min J$, proved from Gowers–Maurey's own
lemmas with every inference audited and every number machine-checked (stdlib
only). All obstruction claims are theorems about the construction; the
obstruction itself is original, while the repaired subsequence bound is an
explicit, checked re-derivation of the paper's estimate.

## 1. Setup and conventions

$X_{GM}$ is the Gowers–Maurey space of math/9205204 §3. We use:
$f(x) = \log_2(x+1)$; $J = \{j_1, j_2, \dots\}$ increasing with $m < n$ in $J$
implying $\log\log\log n \ge 2m$ (natural logs) and $f(j_1) \ge 36$; $K = \{j_2,
j_4, \dots\}$ (even $J$-indices); $L = \{j_1, j_3, \dots\} \ni$ values of the
coding injection $\sigma$; norming set $D = \bigcup_N D_N$ with $D_N'' = \bigcup_{k
\in K} B_k(D_N)$ (special vectors only for lengths in $K$); implicit norm with
$\sup\{|g(Ex)| : k \in K, g \in B_k^*(X)\}$ (special functionals only for $k \in
K$). RIS = rapidly increasing sequence of $\ell_{1+}$-averages; $(M,g)$-form =
$g(M)^{-1}\sum_{j=1}^M x_j^*$ with successive $\|x_j^*\|\le 1$; unconditional
constant $K(x_1,\dots,x_n)$ = least $C$ with $\|\sum \varepsilon_i a_i x_i\| \le
C\|\sum a_i x_i\|$ for all scalars and signs.

## 2. Index obstruction (theorems about the construction)

**Theorem 1 (no $\min J$ special).** Let $j^* = \min J = j_1$. Then (i) no special
functional of length $j^*$ and no special vector of length $j^*$ belongs to the
norming system $D$; (ii) no formal special sequence of length $k \in K$ has any
component of weight $j_1$, except that length-$1$ formal sequences start with
weight $j_{2\cdot1-1} = j_1$, and $1 \notin K$ so these never enter the norm.

*Proof.* (i) $D''$ unions $B_k$ over $k \in K$ and the implicit norm takes the sup
over $k \in K$; $j_1$ has $J$-index $1$, odd, hence $j_1 \in L \setminus K$. (ii)
First-component weights are $j_{2k-1}$; $j_{2k-1} = j_1$ iff $k = 1 \notin K$.
Subsequent weights are $\sigma$-values in $L$ determined by injectivity of
$\sigma$, and a weight-$j_1$ value would require repeating the length-$1$ seed,
excluded since $1 \notin K$. ∎

**Theorem 2 (every-$n$ dependent coding is ill-posed).** There is no
length-$n$ special functional for any $n \notin K$, and none enters the norm.
In particular a claim requiring, for every positive integer $n$, a normalized
$n$-block "forming a dependently-coded RIS" together with "the associated
special functionals" from the construction is undefined as stated for every $n
\notin K$ — including every $n \le 65534$ (all $n$ with $(1/4)f(n)^{1/2} \le 1$)
and almost every $n$ thereafter, since $K$ has triple-exponential gaps.

*Proof.* Specials enter $D$/norm only for lengths in $K$; $j_2$ already exceeds
$2^{144}-1 \gg 65534$ (Lemma below), so no $n \le 65534$ is a $K$-length. ∎

**Corollary (fallback as stated cannot hold).** The uniform $D$-control lemma at
$j^* = \min J$ requiring "the associated special functional $h$ of weight $j^*$
with $h(y) \ge L^* = 4$" is unsatisfiable: no such $h$ exists in $D$.

## 3. Quantitative obstructions (natural repairs also fail)

**Lemma (sparsity floor).** $j_1 \ge 2^{36}-1$ and $j_2 \gg 2^{144}-1$; indeed
$\log\log\log j_2 \ge 2j_1 \ge 2(2^{36}-1) \approx 1.37\times 10^{11}$ while
$\log\log\log(2^{144}) \approx 1.53$.

**Theorem 3 (prefix-window obstruction).** Let a length-$k$ ($k \in K$)
dependent sequence give $\|\sum_{i=1}^k x_i\| \ge (k/2-1)/\sqrt{f(k)}$ and let a
prefix $P$ of $n$ of its vectors satisfy $\|P\| \le 1.2\,n/f(n)$ (Lemma-5 scale).
Then the ratio $\|{\rm full}\|/\|P\| \ge (1/4)\sqrt{f(n)}$ requires
$f(k)/f(n) \le 25/9 = 2.777\dots$. Across $K$-gaps ($f(k_{next})/f(n)$ up to
$\sim 10^{11}$-scale towers) this fails; e.g. at $n = 10^6$, admissible $k+1 \le
(n+1)^{2.78} \approx 10^{16.7}$ while the next $K$-element is triply-exponentially
larger.

**Theorem 4 (chunk obstruction).** Let $k = ns$ with $n$ even, $v = \sum_j
(-1)^j y_j$ the chunk-alternating sum. The valid length-$k$ special continuing
the first chunk's functionals gives $\|v\| \ge (s/2-2)/\sqrt{F}$ ($F = f(k)$;
tail box $k^2\cdot k^{-2} = 1$ exact, first-chunk cross $s/k = 1/n$ exact), for
every chunk-sign pattern. Against any hoped $y$-level sub-bound $1.2\,n/f(n)$,
the violation ratio is $\gg 1$ exactly when $\sqrt{F}/n \gg 1$, i.e. $F = \log k
\gg n^2$ — the $k \gg n$ regime forced by $K$-sparsity. Stand-in evaluations:
$(n,F,k) = (1000,200,10^9)$: ratio $293.7$; $(100,50,10^6)$: $39.2$;
$(10,20,10^4)$: $32.1$.

## 4. Sharp repair (subsequence law + canonical base case)

**Theorem 5 (repaired growth law along $K$).** Let $k \in K$ with $k \ge 10$
(every actual $K$-element exceeds $2^{144}$). Every infinite-dimensional block
subspace $Y \subset X_{GM}$ contains a normalized dependent $k$-sequence with
$K(x_1,\dots,x_k) \ge (1/3)f(k)^{1/2} \ge (1/4)f(k)^{1/2}$.

*Proof.* Gowers–Maurey §3 HI construction verbatim: lower bound
$f(k)^{-1/2}(k/2-1)$ via the designated length-$k$ special; upper bound
$1.2\,k/f(k)$ via Lemma 5 with $g'$ excluding $k$ (valid since $\phi \le \phi'$
gives $g \le g' \le f$ and Lemma 7 gives $g'(k) = f(k)$); ratio $=
\sqrt{F}(k-2)/(2.4k) \ge (1/3)\sqrt{F}$ iff $k \ge 10$ (sharp: $k = 9$ fails).
The small-special estimate $|z^*(Ex)| \le 6/\sqrt{f(k)} < 1/2$ needs $f(k) >
144$, satisfied since $j_2 \gg 2^{144}-1$. ∎

**Canonical base case (replacing $\min J$).** At $k_0 = \min K = j_2$: the upper
envelope for non-designated weights and the designated length-$k_0$ special
lower bound are exactly the $k = k_0$ instance of Theorem 5's proof, with
$U$-scale $1.2\,k_0/f(k_0)$ and $L$-scale $(k_0/2-1)/\sqrt{f(k_0)}$, ratio $\ge
(1/3)\sqrt{f(k_0)}$. No length-$j_1$ special is invoked.

## 5. What is proved vs conjectured; originality

Proved here: Theorems 1–5 and the Lemma (index logic + GM-lemma audit + exact
arithmetic). Conjectured/open: whether some other (non-dependent) block
construction yields an every-$n$ rate; we make no claim on this. Originality:
GM proves qualitative HI with no every-$n$ growth law and no level-by-level
$(2,4)$ envelope; Schlumprecht Lemmas 1–5 are $S$-space bounds; Argyros–Haydon
is a different HI object. The index obstruction (parity $j_1 \in L \setminus K$
killing both the every-$n$ dependent-coding qualifier and the $\min J$ special)
and the $25/9$-window / $\sqrt{F}/n$-violation quantification are new. The
Theorem-5 estimate itself is Gowers–Maurey's (constant $1/3$, slack to $1/4$);
our contribution there is the sharp $k \ge 10$ boundary audit and the corrected
index scope. No database tabulates these rates or envelopes.

## 6. Reproduction

Run in the lane directory (stdlib only):
`python3 output/artifacts/check_target_numbers.py` (thresholds, ratio, $j_1$ floor),
`python3 output/artifacts/verify_t_agreement.py` (estimate audit + chunk scaling),
`python3 output/artifacts/verify_hull_chain.py` ($e$-cert, concavity,
submultiplicativity grid, window arithmetic), `python3
output/artifacts/verify_obstruction_scaling.py` (explicit violation ratios),
`python3 output/artifacts/verify_definitions.py` (index/parity logic).
Expected: all print `*_OK`. §3 stand-in integers are illustrative scaling
demonstrations, not $J$/$K$ values; every theorem about $J$/$K$ uses only the
published gap condition and $f(j_1) \ge 36$.

## References

[GM92] W. T. Gowers, B. Maurey, The unconditional basic sequence problem,
arXiv:math/9205204 (verified HTML full text §§0–3). [S91] T. Schlumprecht, An
arbitrarily distortable Banach space, Israel J. Math. 1991 (via GM §2 Lemmas
1–5). [AH09] S. Argyros, R. Haydon, arXiv:0903.3921 (different HI object).
