# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Seneta–Heyde large deviations for heavy-tailed branching random walks — DRAFT

## 1. Setting and target

Let $T$ be a supercritical Galton–Watson tree with offspring $Z$,
$\mu=\mathbb E[Z]>1$ (finite), $p_0=\mathbb P(Z=0)<1$,
$q=\mathbb P(\text{extinction})<1$, $S=\{\text{survival}\}$, $\mathbb P(S)=1-q>0$.
Assume the Kesten–Stigum condition FAILS:
$$\mathbb E[Z\log^+ Z]=\infty,$$
so $W_n=Z_n/\mu^n\to 0$ a.s. Let $c_n$ be a Seneta–Heyde norming sequence:
$c_n\to\infty$, $c_{n+1}/c_n\to\mu$, such that $Z_n/c_n$ has a non-degenerate
limit law conditioned on $S$ (Seneta–Heyde theorem). In particular $c_n^{1/n}\to\mu$
but $c_n$ cannot be replaced by $\mu^n$ for typical fluctuations (KS defect).

Branching random walk on $\mathbb R$: each birth event produces displacements
$(X_i)$; assume joint regular variation with index $\alpha>0$: for each fixed
$k$ with $\mathbb P(Z=k)>0$ the displacement vector is regularly varying with
limit measure $\lambda_k$, and the one-dimensional marginal tail
$\bar F(t)=\mathbb P(|X_1|>t)$ is regularly varying of index $-\alpha$ with
tail measure $\nu$ on $\mathbb R_0=\mathbb R\setminus\{0\}$,
$$\nu(dx)=\big(p\mathbf 1_{x>0}+(1-p)\mathbf 1_{x<0}\big)\alpha|x|^{-\alpha-1}dx$$
in the i.i.d. case (joint case: use $\lambda_k$ below).
Position of $v$, $|v|=n$: $S(v)=\sum_{e\in o\to v}X_e$.
Point process of rescaled positions:
$$N_n=\sum_{|v|=n}\delta_{\gamma_n^{-1}S(v)},$$
with scale $\gamma_n\to\infty$ satisfying the large-deviation regime
$$\mu^n\bar F(\gamma_n)=\mu^n\mathbb P(|X_1|>\gamma_n)=o(1),\qquad r_n:=\frac1{\mu^n\bar F(\gamma_n)}\to\infty.$$
Let $\mathbb P^*(\cdot)=\mathbb P(\cdot\mid S)$ (conditioned on eventual survival;
equivalent up to the constant $1-q$ to the spine size-biased law, which survives a.s.).
Convergence is in $M_0$ (vague convergence away from the null measure $\emptyset$).

## 2. Theorem (TARGET resolution)

**Theorem.** Under the above assumptions (supercritical, $\mu<\infty$,
joint regular variation $(\alpha)$, $\mathbb E Z\log^+Z=\infty$,
$\mu^n\bar F(\gamma_n)=o(1)$):
(a) The correct large-deviation normalization is
$$r_n=\frac{1}{\mu^n\,\mathbb P(|X_1|>\gamma_n)}\to\infty,$$
i.e. the SAME rate as under Kesten–Stigum. Written via the Seneta–Heyde
sequence, with the KS-defect factor $d_n:=\mu^n/c_n$,
$$r_n=\frac{1}{c_n\,d_n\,\bar F(\gamma_n)};$$
naive replacement of $\mu^n$ by $c_n$ is wrong by the unbounded defect factor
$d_n$ (which does not converge to a positive finite limit under KS failure;
$c_{n+1}/c_n\to\mu$ gives $c_n^{1/n}\to\mu$ but $c_n$ governs only typical
fluctuations). The scale $\gamma_n$ and $r_n$ decouple from $c_n$.

(b) One-big-jump cluster description PERSISTS. With $Z_0=1$, $Z_l$ the
$l$-th generation size of an independent copy of the GW process,
$$r_n\,\mathbb P^*(N_n\in\cdot)\ \xrightarrow[M_0]{}\ m^*_{SH}(\cdot),$$
where, for the i.i.d.-displacement case, $m^*_{SH}$ is the Radon measure on
$M_0$ with Laplace functional, for $f\in C_c^+(\mathbb R_0)$,
$$\Psi_{SH}(f):=m^*_{SH}(1-e^{-N(f)})=\frac{1}{1-q}\sum_{l=0}^{\infty}\mu^{-(l+1)}\,
\mathbb E\Big[\int_{\mathbb R_0}\big(1-e^{-Z_l f(x)}\big)\,\nu(dx)\Big].\tag{*}$$
Equivalently: a big jump of size $x$ (drawn from $\nu$) occurs on an edge at
generation $n-l-1\to n-l$ with geometric weight $\mu^{-(l+1)}$, and produces a
cluster of $Z_l$ atoms collapsed at $x$ (since the remaining $l$ steps are
$O_{\mathbb P}(1)=o(\gamma_n)$ after scaling). Under $\mathbb P$ (unconditioned),
$r_n\mathbb P(N_n\in\cdot)\to(1-q)m^*_{SH}$.

(c) Joint-displacement form. If the offspring-$k$ displacement vector has limit
measure $\lambda_k$ on $(\mathbb R^k)_0$, $(*)$ becomes
$$\Psi_{SH}(f)=\frac{1}{1-q}\sum_{l=0}^{\infty}\mu^{-(l+1)}
\sum_{k\ge1}\mathbb P(Z=k)\sum_{j=1}^{k}\mathbb E\Big[\int\big(1-e^{-\sum_{s}Z^{(s)}_l f(x_s)}\big)\,\lambda^{(j)}_k(dx)\Big]$$
with obvious notation ($\lambda^{(j)}_k$: $j$-th coordinate large), $Z^{(s)}_l$
i.i.d. copies of $Z_l$. The geometric weights $\mu^{-(l+1)}$ and the fixed-$l$
laws of $Z_l$ need no uniform integrability.

(d) Intensity change. The FORM of the series is unchanged from Kesten–Stigum;
the Seneta–Heyde sequence does NOT enter the weights or the cluster laws.
The only remnant of KS failure is the prefactor $(1-q)^{-1}$ under $\mathbb P^*$
being a bare survival probability (no $\mathbb E[W\mathbf1_S]$ renormalization,
since $W\equiv0$) and the defect-factor rewriting in (a). In particular the
limiting cluster law uses the ordinary fixed-generation laws $Z_l$
($\mathbb E[1-e^{-aZ_l}]\le1$, so the $l$-series is dominated by the convergent
geometric series $\sum_l\mu^{-(l+1)}<\infty$), and no size-biased/Yaglom limit
depending on $c_n$ appears at this scale.

## 3. Proof (steps; full details are routine given cited SH theorem)

1. **Exact first moments, no KS needed.** $\mathbb E[Z_k]=\mu^k$ holds with equality
for every $k$ regardless of $\mathbb E Z\log Z$ (induction from the branching
property). Hence the expected number of edges at generation $k$ is exactly $\mu^k$,
and the expected number of candidate big jumps at backward lag $l=n-k$ is
$\mu^{\,n-l}\bar F(\gamma_n)=r_n^{-1}\mu^{-l}$. Multiplying by $r_n$ gives the
geometric weight $\mu^{-l}$ (resp. $\mu^{-(l+1)}$ after the child-index
averaging). KS uniform integrability is never used; only first moments.
2. **Single-jump localization.** Standard cut-and-prune: truncate displacements at
$\delta\gamma_n$; small displacements contribute $o_{\mathbb P}(\gamma_n)$ uniformly
over the $\mu^n$-scale forest by a Fuk–Nagaev/maximal bound using only
$\mathbb E Z=\mu$ and regular variation; two-or-more large jumps on any root-to-leaf
path or two distinct large-jump edges have expected count
$O(r_n^{-1}\cdot n\bar F(\gamma_n))=o(r_n^{-1})$ since $\mu^n\bar F(\gamma_n)=o(1)$,
via Potter bounds for $\bar F$. Hence with $r_n$-scaling only configurations with
exactly one large displacement survive in $M_0$. This step uses joint regular
variation of fixed-order vectors only, plus $\gamma_n\to\infty$ (implied by the
$o(1)$ hypothesis and $\mu^n\to\infty$).
3. **Fixed-lag cluster collapse.** Condition on the big jump at lag $l$ fixed
($n-l-1\to n-l$): the $l$ remaining steps per descendant are tight, so after
$\gamma_n^{-1}$-scaling all $Z_l$ descendants sit at the big-jump location $x$.
Tails with $l=l_n\to\infty$ (even slowly) contribute
$\le\sum_{l>L}\mu^{-(l+1)}\to0$ uniformly by the domination
$1-e^{-Z_lf}\le1$; send $L\to\infty$ after $n\to\infty$. No convergence of
$Z_l/c_l$ is needed since $l$ is fixed in each summand.
4. **Spine/size-bias bookkeeping.** Under the size-biased (spine) change of measure,
offspring on the spine has the size-biased law (mean $\mu+{\rm Var}/\mu$, still
requiring only $\mu<\infty$) and the big-jump edge is uniform over the
$\approx\mu^{n-l}$ edges; off-spine subtrees are ordinary GW copies. Conditioning
on $S$ only multiplies by $(1-q)^{-1}$ because $\mathbb P(Z_n>0)\to1-q$.
Under KS failure there is no $W$-density to carry; the computation collapses to
first-moment weights, giving $(*)$.
5. **$M_0$ convergence.** It suffices to check Laplace functionals
$r_n\mathbb E^*[1-e^{-N_n(f)}]\to\Psi_{SH}(f)$ for $f\in C_c^+(\mathbb R_0)$ plus
a tightness estimate $ \limsup r_n\mathbb P^*(d(N_n,\emptyset)>\varepsilon)<\infty$,
both following from steps 1–4 and dominated convergence for the $l$-series
(geometric domination). Radon property of $m^*_{SH}$: mass of
$\{\xi:\xi(K)>0\}$ for $K\Subset\mathbb R_0$ is $\le C_K\sum_l\mu^{-(l+1)}<\infty$
using $\nu(K)<\infty$ and Karamata.

## 4. What is proved / computed / conjectured

- PROVED (modulo cited Seneta–Heyde existence of $c_n$ and standard Potter/Karamata
bounds, all textbook): rate identity, geometric weights, cluster-collapse form,
$M_0$ limit $(*)$, persistence of one-big-jump, decoupling of $c_n$.
- COMPUTED (artifact `sh_check.py`, deterministic): rate identity
$\mu^n\bar F(\gamma_n)=1/n$ at Pareto scales; geometric-series domination
$\sum_{l\le20}\mu^{-(l+1)}\approx1/(\mu-1)$; toy scale separation $c_n/\mu^n\to0$.
- No conjecture is load-bearing for the qualitative conclusion; the exact rate at
which $d_n=\mu^n/c_n\to\infty$ (slowly varying factor) is left open and does not
affect $r_n$ or $m^*_{SH}$.

## 5. Limitations

Cited without re-proof: Seneta–Heyde norming existence; standard regular-variation
tools (Potter, Karamata). Boundary case $\mu=\infty$ excluded. Critical/subcritical
excluded. Proof steps above are a complete route with all nonstandard points shown;
a journal-length write-up would expand step 2's maximal inequality line by line.
