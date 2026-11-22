# Sharp Schatten decay and a critical weak-ideal obstruction for Aluthge smoothing of power-law shifts

## Finding
Fix \(0<t<1\) and \(\alpha>0\). On \(\ell^2(\mathbb N)\), let \(W_\alpha e_j=j^{-\alpha}e_{j+1}\) and write \(\Delta_t(T)=|T|^tU|T|^{1-t}\) for the generalized Aluthge transform of the polar decomposition \(T=U|T|\). Let \(m=nt\). For every \(p>1/\alpha\), setting \(s=\alpha p\), the following sharp two-term asymptotics hold as integers \(n\to\infty\):

\[
\|\Delta_t^n(W_\alpha)\|_{\mathcal S_p}^{p}
=\frac{m^{1-s}}{s-1}-\frac{1+st}{2(1+s)}m^{-s}+O_{\alpha,p,t}(m^{-s-1}),
\]
\[
\|\Delta_t^n(W_\alpha)\|
=m^{-\alpha}\bigl(1-\alpha(1+t)/(2m)+O_{\alpha,t}(m^{-2})\bigr).
\]
Writing \(p_0=1/\alpha\), every iterate has the exact critical weak-Schatten quasi-norm
\[
\|\Delta_t^n(W_\alpha)\|_{\mathcal S_{p_0,\infty}}
:=\sup_{k\ge1}k^{1/p_0}s_k(\Delta_t^n(W_\alpha))=1.
\]
Thus all strong \(\mathcal S_p\) norms above the critical index decay at sharp polynomial rates, but the critical weak norm never decays, although the operator norm tends to zero. No iterate belongs to \(\mathcal S_p\) for \(p\le p_0\).

The leading constants are universal beyond exact powers: if \(w_j=j^{-\alpha}L(j)>0\) is nonincreasing and \(L\) is slowly varying at infinity, and \(We_j=w_je_{j+1}\), then for \(p>1/\alpha\),
\[
\|\Delta_t^nW\|\sim w_{\lfloor nt\rfloor},\qquad
\|\Delta_t^nW\|_{\mathcal S_p}
\sim\frac{(nt)^{1/p}w_{\lfloor nt\rfloor}}{(\alpha p-1)^{1/p}}.
\]
The two-term coefficients above concern exact power weights only; no second-order universality is asserted.

## Assumptions and scope
All spaces are complex Hilbert spaces. All weights are positive and nonincreasing; \(j\) is indexed from \(1\). The transform parameter is strictly between zero and one. The asymptotics for \(\mathcal S_p\) use \(p>1/\alpha\) (including quasi-Schatten exponents below one, with the standard \(p\)-power singular-value sum). We use the conventional decreasing singular-value enumeration \(s_k\). The weak ideal is the Lorentz–Schatten class \(\mathcal S_{p_0,\infty}\) with quasi-norm as displayed.

A function \(L\) is slowly varying if \(L(cx)/L(x)\to1\) for every fixed \(c>0\), applied here on the positive integers or via any positive interpolation. No differentiability, second-order regular variation, or bounded-ratio assumption is required.

## Proof
**1. Exact iteration.** For a positive weighted unilateral shift \(We_j=w_je_{j+1}\), the polar partial isometry is the forward unweighted shift. Thus \(\Delta_t(W)e_j=w_j^{1-t}w_{j+1}^{t}e_{j+1}\). Iterating yields
\[
a_{n,j}:=s_j(\Delta_t^nW)
=\prod_{k=0}^{n}w_{j+k}^{\binom nk t^k(1-t)^{n-k}}
=\exp\{\mathbb E\log w_{j+X}\},\quad X\sim\operatorname{Bin}(n,t).
\]
Monotonicity of \(w_j\) makes \(a_{n,j}\) nonincreasing in \(j\); hence these are the ordered singular values, and the operator norm is \(a_{n,1}\). With power weights, \(a_{n,j}=\exp[-\alpha\mathbb E\log(j+X)]\).

**2. Uniform Taylor estimate.** Put \(m=nt\), \(Y=X-m\), and \(q=j+m\ge m+1\). Then \(\mathbb EY=0\), \(\mathbb EY^2=m(1-t)\), \(\mathbb EY^3=O_t(m)\), and \(\mathbb EY^4=O_t(m^2)\). A binomial Chernoff estimate makes \(\mathbb P(|Y|>m/2)\le C_te^{-c_tm}\). On the complementary event, fourth-order Taylor expansion of \(\log(q+Y)\) gives a remainder bounded by \(C_t(\mathbb E|Y|^4)/q^4\). On the exceptional event, \(j+X\ge1\) and \(q\ge m+1\), so its contribution is exponentially small uniformly in \(j\). Consequently, with a uniform constant for all \(j\ge1\),
\[
\mathbb E\log(j+X)=\log(j+m)-\frac{m(1-t)}{2(j+m)^2}+O_t(m^{-2}).
\]
The estimate is uniform in \(j\), since the Taylor derivatives decrease as \(q\) increases. Exponentiating yields
\[
a_{n,j}^{p}=(j+m)^{-s}\left(1+\frac{sm(1-t)}{2(j+m)^2}+O_{s,t}(m^{-2})\right).
\]

**3. Sum and coefficients.** Euler summation (or the integral test with its first trapezoidal correction) gives, for fixed \(s>1\),
\[
\sum_{j=1}^{\infty}(j+m)^{-s}
=\frac{m^{1-s}}{s-1}-\frac12m^{-s}+O_s(m^{-s-1}),
\]
\[
\sum_{j=1}^{\infty}(j+m)^{-s-2}
=\frac{m^{-s-1}}{s+1}+O_s(m^{-s-2}).
\]
The summed uniform \(O(m^{-2})\) remainder is \(O(m^{-s-1})\). The second term therefore has coefficient \(-1/2+s(1-t)/(2(s+1))=-(1+st)/(2(s+1))\), establishing the sharp Schatten law. Setting \(j=1\) in Step 2 and expanding \(\log(m+1)\) gives \(\mathbb E\log(1+X)=\log m+(1+t)/(2m)+O_t(m^{-2})\), hence the operator-norm law.

**4. Critical ideal.** Since \(j+X\ge j\), \(a_{n,j}\le j^{-\alpha}\). For every fixed \(n\), the binomial variable \(X\) is bounded by \(n\), so \(\mathbb E\log(j+X)=\log j+o(1)\) as \(j\to\infty\). Thus \(j^\alpha a_{n,j}\to1\), and \(\sup_j j^\alpha a_{n,j}=1\) for every \(n\). The same tail equivalence implies divergence of \(\sum_j a_{n,j}^p\) when \(\alpha p\le1\).

**5. Slowly varying universality.** Let \(w_j=j^{-\alpha}L(j)\) be positive and nonincreasing, and put \(m=nt\). A binomial law of large numbers together with the uniform convergence theorem for regularly varying sequences shows for every fixed \(x\ge0\) (uniformly on bounded \(x\)-intervals) that
\[
\frac{a_{n,\max\{1,\lfloor mx\rfloor\}}}{w_{\lfloor m\rfloor}}
\longrightarrow(1+x)^{-\alpha}.
\]
Here exponentially unlikely events \(X<m/2\) are harmless: for \(j\le Cm\), the logarithm of the largest ratio \(w_1/w_{\lfloor m\rfloor}\) is \(O(\log m+|\log L(m)|)=O(\log m)\) by slow variation; for larger \(j\) monotonicity only improves the lower-tail comparison. For fixed \(\epsilon>0\), Potter's regular-variation bounds and binomial concentration imply a uniform envelope
\[
\frac{a_{n,j}}{w_{\lfloor m\rfloor}}
\le C_\epsilon(1+j/m)^{-\alpha+\epsilon}
\]
for sufficiently large \(m\) and all \(j\ge1\). Indeed, for \(j\ge m\) the geometric mean obeys \(a_{n,j}\le w_j\), and Potter's bound compares \(w_j\) with \(w_{\lfloor m\rfloor}\). For \(1\le j<m\), monotonicity yields \(a_{n,j}\le a_{n,1}\), while the local limit at \(x=0\) makes \(a_{n,1}/w_{\lfloor m\rfloor}\) bounded; the envelope's right-hand power is bounded below by a positive constant on \(0\le j/m\le1\). Choose \(\epsilon\) with \(p(\alpha-\epsilon)>1\). Dominated Riemann-sum convergence now gives
\[
\frac{\sum_{j\ge1}a_{n,j}^{p}}{m w_{\lfloor m\rfloor}^{p}}
\to\int_0^\infty(1+x)^{-\alpha p}\,dx
=\frac1{\alpha p-1}.
\]
Because the weights are nonincreasing, the operator norm is \(a_{n,1}\), and the same local limit at \(x=0\) proves \(a_{n,1}/w_{\lfloor m\rfloor}\to1\).

## Verification
A standalone numerical checker in `verify.py` implements the exact binomial-log weight formula, independently compares finite numerical sums against the two-term formula using a controlled zeta tail, checks small-parameter exact iteration and singular-value ordering, and tests the critical weak-norm bounds and tail approach. The checker is reproducible with Python 3 and NumPy/SciPy; finite checks are not proofs of the limits. The analytical proof above supplies the infinite-dimensional quantifiers.

## Relationship to prior work
Stanković (2026), Proposition 5.8 and the surrounding discussion, gives the binomial weight formula and qualitative convergence for compact weighted shifts in the Schatten classes containing them, without sharp convergence coefficients or critical weak-ideal persistence. The proof here uses that exact formula as a starting point but derives a quantified, class-universal asymptotic law, a nonzero correction for exact power weights, and a persistent weak-ideal boundary. Earlier studies of stretched-exponential bilateral and unilateral weighted shifts have markedly different decay and spectral mass scales; their findings do not give these power-weight constants. The available literature comparisons do not establish bibliographic uniqueness against every unindexed result.

## Limitations
The two-term coefficients require exact powers, and the universality statement assumes positive nonincreasing regularly varying weights. No estimate is asserted uniformly as \(t\to0\) or \(t\to1\). No operator-theoretic claim beyond unilateral shifts, and no independent validation, is claimed. The first asymptotic correction does not quantify convergence for general slowly varying factors.

## References
1. H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1 (5 November 2026), especially Proposition 5.8. https://arxiv.org/abs/2611.07728
2. S. H. Lee, W. Y. Lee, J. Yoon, *Subnormality of Aluthge transforms of weighted shifts*, Integral Equations and Operator Theory **72** (2012), 241–251, for iterated binomial weights. https://www.math.snu.ac.kr/~wylee/12_1_IEOT.pdf
3. *A sharp singular-value boundary layer for stretched-exponential Aluthge iterates* (2026), a related published result for non-power decay. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-singular-value-boundary-layer-for-stretched-exponential--8ed808d0b606
4. *Two-scale Aluthge asymptotics of compact bilateral stretched-exponential shifts* (2026), a related bilateral non-power model. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-scale-aluthge-asymptotics-of-compact-bilateral-stretched-exp--304047bdec1c
