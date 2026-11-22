# Fractional two-pulse amplification below the Cesàro ambient exponent

## Finding
Fix real parameters \(1\le p<\infty\), \(0<q<p\), and \(0<\alpha<1/p\). On the real or complex weighted sequence space \(X=\ell^p(\mathbb N,\omega)\), with \(\omega_j=j^{-\alpha}\) and norm
\[
\|x\|_X^p=\sum_{j=1}^{\infty}|x_j|^p j^{-\alpha p},
\]
let \(B(x_1,x_2,\ldots)=(x_2,x_3,\ldots)\). Write its optimal \(q\)-absolute Cesàro constant as
\[
C_{q,\mathrm{ac}}(B)=\sup_{N\ge1}\sup_{\|x\|_X=1}\frac1N\sum_{k=0}^{N-1}\|B^k x\|_X^q.
\]
The basis-vector test constant, in the notation of Abbar--Arnold--Coine, is
\[
a_q=\sup_{N\ge1}\sup_{j\ge N}\frac1N\sum_{k=0}^{N-1}
\left(\frac{\omega_{j-k}}{\omega_j}\right)^q
=\frac{1}{1-\alpha q}.
\]
Then \(B\) is \(q\)-absolutely Cesàro bounded, yet its optimal constant satisfies the **strict universal gap**
\[
\boxed{\frac1{1-\alpha q}<C_{q,\mathrm{ac}}(B)\le
(1-\alpha p)^{-q/p}<\infty.}
\]
The strict gap is witnessed by normalized vectors supported at only two coordinates. Moreover, this amplification has an explicit fractional boundary law. Set \(r=\alpha p\), \(b=\alpha(p-q)\), \(d=\alpha q=r-b\), and \(\vartheta=q/p\). For \(0<s<1\), put
\[
A_v(t)=\begin{cases}(v/(v-t))^r,&0\le t<v,\\0,&v\le t\le1,\end{cases}
\qquad
F_s(\varepsilon)=\int_0^1[(1-\varepsilon)A_1(t)+\varepsilon A_s(t)]^\vartheta\,dt,
\quad0\le\varepsilon<1.
\]
For \(0<s<1\), the right derivative at zero exists and
\[
\frac{1}{\vartheta}F_s'(0+)
=I(s)-\frac1{1-d},\qquad
I(s)=\int_0^s\left(\frac{s}{s-t}\right)^r(1-t)^b\,dt.
\]
In the near-coincident limit \(s=1-\delta\),
\[
\boxed{\frac1{\vartheta}F_{1-\delta}'(0+)
\sim\frac{b}{1-d}\,\mathrm B(1-r,d)\,\delta^{1-d}
\quad(\delta\downarrow0).}
\]
The beta-function coefficient is strictly positive. Thus, for every permitted parameter triple, \(F_s(\varepsilon)>a_q\) for some \(s<1\) sufficiently close to one and some \(\varepsilon>0\). This is a quantitative failure of the equality \(C_{q,\mathrm{ac}}=a_q\) that is known for \(q\ge p\): its failure below \(p\) occurs for *every* positive power weight in the absolutely bounded regime, not only at isolated parameters.

## Assumptions and scope
The field can be real or complex. The exponent \(q\) may lie below one: only the scalar averages of \(q\)-th powers of norms are used. The restriction \(\alpha p<1\) guarantees integrability of the two-pulse kernels and a finite \(p\)-absolute Cesàro constant. The number \(C_{q,\mathrm{ac}}\) is defined without taking a \(q\)-th root; no exact closed form for this unrestricted optimum is asserted. The beta function is \(\mathrm B(u,v)=\int_0^\infty t^{u-1}(1+t)^{-u-v}\,dt\) for positive \(u,v\).

## Proof
**1. A finite sharp basis constant.** The operator is bounded because \(\sup_{j\ge2}\omega_{j-1}/\omega_j=2^\alpha\). If \(j\ge N\), then \((j/(j-k))^d\) decreases with \(j\) for each \(1\le k<N\). Hence the maximum in \(j\) occurs at \(j=N\). The integral comparison for \(t^{-d}\), \(0<d<1\), yields
\[
\frac{N^d}{N}\sum_{h=1}^N h^{-d}\le\frac{N^d}{N}\int_0^N t^{-d}\,dt=\frac1{1-d}.
\]
The left side converges to \((1-d)^{-1}\) by the integral test, proving the stated identity for \(a_q\).

**2. Finite absolute Cesàro upper bound.** For any \(x\in X\), Tonelli's theorem gives
\[
\frac1N\sum_{k=0}^{N-1}\|B^kx\|_X^p
=\sum_{j\ge1}|x_j|^p\omega_j^p\frac1N
\sum_{0\le k<\min\{N,j\}}\left(\frac{j}{j-k}\right)^r.
\]
For \(j\ge N\), the inner average is at most the corresponding average at \(j=N\), and hence at most \((1-r)^{-1}\). For \(j<N\), its value is at most \(j/[N(1-r)]\le(1-r)^{-1}\). Thus \(C_{p,\mathrm{ac}}(B)\le(1-r)^{-1}\). Single basis vectors with \(j=N\to\infty\) show equality. Jensen's inequality for the concave power \(\vartheta=q/p\) then proves \(C_{q,\mathrm{ac}}(B)\le(1-r)^{-\vartheta}\).

**3. Exact two-pulse scaling.** For large positive integers \(N\), set \(j_N=\lfloor sN\rfloor\) and choose \(x^{(N)}\), supported at \(j_N,N\), with
\[
|x^{(N)}_{j_N}|^p\omega_{j_N}^p=\varepsilon,
\qquad |x^{(N)}_N|^p\omega_N^p=1-\varepsilon.
\]
Then \(\|x^{(N)}\|_X=1\), and a direct shift computation gives
\[
\frac1N\sum_{k=0}^{N-1}\|B^kx^{(N)}\|_X^q
=\frac1N\sum_{k=0}^{N-1}
\left[(1-\varepsilon)\left(\frac{N}{N-k}\right)^r
+\varepsilon\mathbf1_{k<j_N}\left(\frac{j_N}{j_N-k}\right)^r\right]^\vartheta.
\]
As \(N\to\infty\), the expression tends to \(F_s(\varepsilon)\). To justify convergence at both power singularities, split into fixed compact subintervals away from \(s,1\), where convergence is ordinary Riemann convergence. On the remaining intervals use \((u+v)^\vartheta\le u^\vartheta+v^\vartheta\) and the integral test to bound the tails uniformly by constants times \(\eta^{1-d}\), for a neighborhood of radius \(\eta\). Thus no finite truncation is substituted for the limit.

**4. First variation and its fractional boundary layer.** For fixed \(s<1\), differentiation under the integral at \(\varepsilon=0+\) is justified by \(r<1\), \(d<1\), and the lower bound \((1-\varepsilon)A_1\ge A_1/2\) for small \(\varepsilon\). The derivative equals
\[
F_s'(0+)=\vartheta\int_0^1(A_s-A_1)A_1^{\vartheta-1}\,dt
=\vartheta\left[I(s)-\frac1{1-d}\right].
\]
Put \(s=1-\delta\) and \(\eta=\delta/s\). Substitution \(t=s(1-u)\) yields
\[
I(s)=s^{1+b}\left[\frac1{1-d}+J(\eta)\right],
\qquad
J(\eta)=\int_0^1 u^{-r}\big[(u+\eta)^b-u^b\big]du.
\]
By the fundamental theorem of calculus and Tonelli's theorem,
\[
J(\eta)=b\int_0^\eta v^{-d}
\left[\int_0^{1/v} w^{-r}(1+w)^{b-1}\,dw\right]dv.
\]
The inner integral increases to \(\mathrm B(1-r,d)\), finite because \(0<r<1\) and \(0<d<1\). Dominated convergence after rescaling \(v=\eta z\) gives
\[
J(\eta)\sim\frac{b}{1-d}\mathrm B(1-r,d)\eta^{1-d}.
\]
Because \(1-d<1\), the difference \(s^{1+b}-1=O(\delta)=o(\delta^{1-d})\). Therefore
\[
I(1-\delta)-\frac1{1-d}\sim\frac{b}{1-d}\mathrm B(1-r,d)\delta^{1-d}>0.
\]
Fix a sufficiently small positive \(\delta\), so \(F'_{1-\delta}(0+)>0\). Since \(F_{1-\delta}(0)=a_q\), there is a small \(\varepsilon>0\) with \(F_{1-\delta}(\varepsilon)>a_q\). The finite two-pulse vectors in Step 3 then show \(C_{q,\mathrm{ac}}(B)\ge F_{1-\delta}(\varepsilon)>a_q\), proving strictness for every indicated parameter triple. \(\square\)

## Verification
The proof is an infinite-index argument. A standalone numerical script, `verify.py`, independently checks the exact basis constants on finite horizons, the finite two-pulse orbit formula against direct weighted-shift iteration, a concrete strictly amplifying example, and convergence toward the positive beta-function boundary coefficient. The finite examples are diagnostics only and are not used to establish universal strictness.

## Relationship to prior work
Abbar, Arnold and Coine [1, Theorem 3.4] prove \(C_{q,\mathrm{ac}}=a_q\) for \(q\ge p\), and their Example 3.10 gives the *boundedness range* for power weights when \(q<p\). The strict inequality and explicit two-pulse first-variation law in this work concern the previously untreated optimal constant below \(p\); mere boundedness classification does not supply them. Arnold [2] studies universal exponent self-improvement and extremal weighted shifts, rather than this particular sharp comparison of constants. The regularly varying backward-shift weak-endpoint result [3] classifies strong/weak admissible exponents and does not determine subambient optimal Cesàro constants. In all three cases, comparing the conclusions rather than their shared weighted-shift parameters is essential. This comparison does not establish global bibliographic priority.

## Limitations
The exact unrestricted value of \(C_{q,\mathrm{ac}}(B)\), optimal two-pulse mass, and whether two pulses suffice globally remain undetermined. The fractional law describes the first variation of a specific continuum two-pulse family as the two coordinate ratios coalesce, not the full optimizer. The theorem is limited to pure power weights with \(0<\alpha p<1\); it does not assert the same universal strictness for all weights or at the endpoint. Independently audited originality or correctness is not claimed.

## References
1. A. Abbar, L. Arnold and C. Coine, *On Absolutely Cesàro Bounded Operators*, arXiv:2609.24601v1 (first public 2026-09-21), Sections 3.1 and 3.3, https://arxiv.org/html/2609.24601 .
2. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1 (first public 2026-09-24), Sections 1 and 3, https://arxiv.org/html/2610.00271v1 .
3. *Critical weak Cesàro endpoints for regularly varying backward shifts*, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-critical-weak-ces-ro-endpoints-for-regularly-varying-backward-sh--e438690c71d4 .
