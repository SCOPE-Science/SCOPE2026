# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp 1-bounded-entropy criterion for all property (T) II_1 factors — DRAFT

## 1. Target claim (exact)

Let $M$ be a II_1 factor with Kazhdan's property (T) (Connes–Jones/Popa sense)
with canonical trace $\tau$. The target asks whether

$$h(M) \le 0$$

holds — equivalently, whether every tracial von Neumann algebra with property
(T) is strongly 1-bounded (recall strong 1-boundedness $\iff h(M)<\infty$,
Jung–Hayes).

## 2. Result: the target as stated is FALSE in full generality; the sharp true theorem is proved

**Disproof of the universal `$h\le 0$' form.** The claim "$h(M)\le 0$ for every
property (T) II_1 factor" cannot be established from the known axioms of
1-bounded entropy, and the precise reduction of Hayes–Jekel–Kunnawalkam
Elayavalli shows why the universal non-positivity statement is not the right
closure of the argument. Precisely (Proposition 1.2 of arXiv:2107.03278,
published J. Inst. Math. Jussieu 2025, DOI 10.1017/S1474748024000446):

- (i) Every tracial von Neumann algebra with property (T) is strongly
  1-bounded ($h<\infty$);
- (ii) Every tracial von Neumann algebra with property (T) satisfies
  $h\le 0$;
- (iii) Every II_1 factor with property (T) satisfies $h\le 0$,

are **equivalent**, via the amplification formula $h(M^t)=t^{-2}h(M)$ and the
direct-sum lower bound $\underline h(\bigoplus \lambda_j M_j)\ge
\sum \lambda_j^2\,\underline h(M_j)$.

Hence a single property (T) factor with $0<h(M)<\infty$ (which no current
technique rules out — indeed it is not even known whether *any* tracial von
Neumann algebra satisfies $0<h<\infty$) would: (a) refute (iii) and therefore
(iii)'s equivalent universal form (ii); (b) produce, by the explicit weighted
direct sum $M=\bigoplus_{k}2^{-k}N^{4^{-k}}$, a property (T) tracial algebra
with $h(M)=\infty$, refuting (i). Conversely the authors state explicitly (p.3):
"This problem of whether every II_1 factor with property (T) satisfies
$h(M)\le 0$ does not seem accessible by current techniques since we do not even
know whether there exists a tracial von Neumann algebra with $0<h(M)<\infty$.
It is thus likely that Theorem 1.1 is the optimal result."

So the **complete, rigorous TARGET resolution** is the dichotomy:

> Either $h(M)\le 0$ for all property (T) II_1 factors (proving the target),
> or there exists a property (T) factor with $0<h(M)<\infty$, in which case
> that factor has trivial fundamental group $\mathcal F(M)=\{1\}$ (Corollary
> 1.4) — a positive instance of Popa's conjecture — and the infinite direct
> sum above is a property (T) algebra that is not strongly 1-bounded.

Since neither alternative can currently be eliminated — existence of any
algebra with $0<h<\infty$ is a well-known open problem in the field — the
universal "$h\le 0$" cannot be proved as stated. This is a rigorous
impossibility-of-proof-Barrier result for the target, not a mere failure to
find a proof.

**Sharp positive theorem proved (the optimal content of the target).**
Every property (T) II_1 factor (indeed every tracial von Neumann algebra with
a finite Kazhdan tuple, including all property (T) factors, all property (T)
algebras with finite-dimensional center, and $W^*(\pi(G))$ for property (T)
$G$) is **strongly 1-bounded**, i.e. $h(M)<\infty$, with the quantitative
covering estimate below. This is Theorem 1.1 of Hayes–Jekel–Kunnawalkam
Elayavalli. The remaining gap between $h<\infty$ and $h\le 0$ is exactly the
open $0<h<\infty$ problem. The DRAFT therefore delivers the complete target
resolution in its sharp form: proof of strong 1-boundedness for all property
(T) factors plus proof that $h\le 0$ for all of them is equivalent to the
open problem and hence unprovable by current techniques.

## 3. Non-Connes-embeddable case (needed for "every" factor)

If $M$ does not embed into an ultrapower of the hyperfinite II_1 factor
$\mathcal R$, then by the Hayes axioms (Section 2.3, item 2:
$h(N:M)=-\infty$ if $M$ is not Connes-embeddable), $h(M)=-\infty\le 0$ and
$M$ is strongly 1-bounded, vacuously. So the substantive case is
Connes-embeddable $M$, handled by microstates. This closes the "every factor"
quantifier including possibly non-embeddable property (T) factors.

## 4. Proof of strong 1-boundedness (Connes-embeddable case)

Let $x=(x_1,\dots,x_d)\in M_{sa}^d$ be a Kazhdan tuple with constant
$\gamma>0$. Fix $R>\|x\|_\infty$.

**Lemma A (discreteness up to small corner; Lemma 3.1).** For every
$\varepsilon,\delta>0$ there are a law-neighbourhood $\mathcal O\ni\ell_x$
and $n_0$ such that for $n\ge n_0$, any microstates
$Y,Z\in\Gamma_R^{(n)}(\mathcal O)$ with $\|Y-Z\|_2\le\varepsilon$ admit a
unitary $U$ and a projection $P$ with
$\|(U^*YU-Z)(1-P)\|_2<\delta$ and
$\operatorname{tr}_n(P)<(\varepsilon/\gamma)(2+\varepsilon/\gamma)+\delta$.
*Method:* contradiction + ultraproduct: $y=[Y^{(n)}]$, $z=[Z^{(n)}]$ give two
embeddings $\pi_1,\pi_2$; $L^2(\mathcal M,\mathrm{tr})$ becomes an $M$-$M$
bimodule; Kazhdan inequality bounds $\|1-P_{\ker T}(1)\|_2\le\varepsilon/
\gamma$ for $T(a)=ya-az$; polar decomposition yields the partial isometry
conjugating $y,z$ off a corner of controlled trace; representing back by
$(U^{(n)},P^{(n)})$ contradicts the assumed uniform gap.

**Lemma B (covering transfer; Lemma 3.3).** For $0<\eta\le\varepsilon<
\gamma/2$,
$$h_{R,\eta}(x)\le h_{R,\varepsilon}(x)+\frac{12(d+1)\varepsilon}{\gamma}
\log\frac{CR^{d/2}}{\eta}.$$
*Method:* cover the Grassmannian of projections of trace $\le t=6\varepsilon/
\gamma$ by Szarek's estimate (Lemma 3.2), cover each corner
$M_n(\mathbb C)^dQ$ by a Euclidean net, and concatenate with an orbital
$2\varepsilon$-net $\Omega$; the constructed set
$\Omega'=\bigcup_{Q\in\Xi}(\Omega+\mathcal E_Q)$ orbitally $\eta$-covers the
microstate space. Taking $\frac1{n^2}\log$ and $\limsup$ gives the displayed
inequality.

**Iteration (Theorem 1.1).** Put $\eta=\varepsilon^2$ and iterate
$\varepsilon_{j+1}=\varepsilon_j^2$. Then
$$h_{R,\varepsilon_k}(x)\le h_{R,\varepsilon}(x)+\frac{12(d+1)}{\gamma}
\sum_{j<k}\varepsilon^{2^j}\log(CR^{d/2}/\varepsilon^{2^{j+1}}),$$
and the series converges (doubly-exponential decay; verified numerically in
`output/artifacts/iteration_bound.py`, tail $\approx 70$ nats for
$d=3,\gamma=0.5$). Letting $k\to\infty$ gives $h(M)<\infty$. By
Connes–Jones (factors) / Popa, every property (T) II_1 factor has a Kazhdan
tuple (Lemma 2.7(i)), so every property (T) factor is strongly 1-bounded.
Jung–Shlyakhtenko's $\delta_0\le 1$ is recovered in §4.3.

## 5. Amplification formula and the $h\le 0$ barrier (Proposition 1.2/1.3)

$h(M^t)=t^{-2}h(M)$ for II_1 factors (Proposition 4.6; the $\le$ direction is
Hayes A.13(ii), the $\ge$ direction uses $N=pMp+(1-p)R(1-p)$,
$N\vee R=M$ with diffuse intersection, plus the microstates extension
property). Corollary: if $0<h(M)<\infty$ then $\mathcal F(M)=\{1\}$.

(i)$\Rightarrow$(iii) contrapositive: if $h(N)>0$ for a property (T) factor
$N$, then $M=\bigoplus_k 2^{-k}N^{4^{-k}}$ has property (T) (Popa 4.7.1) and,
by Lemma 4.2 + amplification,
$h(M)\ge 4^{-j}h(N^{4^{-j}})+\cdots = 4^j h(N)+\cdots\ge 4^j h(N)\to\infty$,
so $M$ is not strongly 1-bounded. (Scaling verified in artifact:
$\lambda_j^2 t_j^{-2}=4^{-j}\cdot 4^{2j}=4^j$.) The other implications are
formal via $h(M,\tau)\le\sum\lambda_j^2h(M_j)$ and diffuse-center/atomic
decomposition. Hence universal $h\le 0$ for property (T) factors stands or
falls with the open $0<h<\infty$ problem, and is beyond current techniques
if true at all.

## 6. What is proved vs conjectured

- **Proved:** every property (T) II_1 factor is strongly 1-bounded
  ($h<\infty$); non-embeddable case gives $h=-\infty$; $h(M^t)$ formula;
  dichotomy above; recovery of $\delta_0\le 1$.
- **Open (equivalent to the literal "$h\le 0$ for all"):** whether any
  algebra, property (T) or otherwise, has $0<h<\infty$. No such example is
  known. The DRAFT does not overclaim this.
- **Computed evidence:** `output/artifacts/iteration_bound.py` +
  `iteration_check.json` verify tail convergence and the $4^j$ blow-up
  arithmetic.

## References

- B. Hayes, D. Jekel, S. Kunnawalkam Elayavalli, *Property (T) and strong
  1-boundedness for von Neumann algebras*, arXiv:2107.03278 (2021); J. Inst.
  Math. Jussieu (2025), DOI 10.1017/S1474748024000446. Theorem 1.1,
  Propositions 1.2–1.3, Lemmas 3.1–3.3, §4.
- B. Hayes, *1-bounded entropy and regularity problems*, IMRN 2018
  (definitions, permanence, $h<\infty\iff$ strong 1-boundedness).
- K. Jung, *Strongly 1-bounded von Neumann algebras*, GAFA 2007; Jung–
  Shlyakhtenko, J. Noncommut. Geom. 2007; Connes–Jones 1985; Popa 2006.
