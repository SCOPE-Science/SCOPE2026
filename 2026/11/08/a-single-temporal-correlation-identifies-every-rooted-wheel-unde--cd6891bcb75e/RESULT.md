# A single temporal correlation identifies every rooted wheel under synchronous noisy voting

## Finding
Let \(W_{n+1}=K_1\vee C_n\), where \(n\ge3\), and let \(h\) be its universal hub. In the synchronous binary noisy voter model with independent fair refreshing probability \(\varepsilon\in(0,1)\), put \(c=1-\varepsilon\) and \(q=c^2\). Let \(\sigma_t(h)\in\{-1,+1\}\) be the hub spin in stationarity and define \(R_n=\mathbb E[\sigma_t(h)\sigma_{t+1}(h)]\). Then **\(R_n>R_{n+1}\) for every integer \(n\ge3\)**, for every fixed \(\varepsilon\in(0,1)\). Consequently the stationary one-step agreement probability \(\Pr\{\sigma_t(h)=\sigma_{t+1}(h)\}=(1+R_n)/2\) uniquely determines \(n\) among all rooted wheels when \(\varepsilon\) is known.

Here is an explicit expression. Set
\[
\delta=\sqrt{1-4q/9},\quad t=\frac{2q/9}{1-2q/9+\delta},\quad
\ell_n=\frac{n}{\gcd(n,2)},\quad
H_n=\frac{1-t^{\ell_n}}{n\delta(1+t^{\ell_n})},
\]
\[
k=\frac{2q}{3-q},\quad \alpha=\frac{q}{9-4q},\quad
F_q(H)=\frac{k[\alpha+(1-\alpha)H]}{1-4k\alpha(1-H)}.
\]
Then
\[R_n=c F_q(H_n).\]
For fixed \(q\in(0,1)\), define \(D=27-21q-4q^2\). As \(n\to\infty\),
\[
R_n=c\left[\frac{2q^2}{D}+\frac{6q(1-q)(9+q)(9-4q)}{\delta D^2}\frac1n+O_q(n^{-2})\right].
\]
In particular, the limiting lag-one correlation is strictly positive and adjacent wheel sizes have gaps of order \(n^{-2}\), with
\[
\lim_{n\to\infty}n^2(R_n-R_{n+1})=
\frac{6cq(1-q)(9+q)(9-4q)}{\delta D^2}>0.
\]

## Assumptions and scope
The rim is the simple cycle \(C_n\) on vertices \(0,\ldots,n-1\); \(h\) is adjacent to every rim vertex. At every integer time, all vertices simultaneously and independently either redraw a fair \(\{-1,+1\}\) spin with probability \(\varepsilon\), or copy the previous-time spin of a uniformly chosen neighbor with probability \(c\). All random choices are independent over vertices and times. The observation is the spin at \(h\) only; the noise parameter is fixed and known. No self-loops, weighted edges, or asynchronous updates are included.

The finite-state chain is irreducible and aperiodic because a full independent refresh can produce every configuration with positive probability, including the current configuration. Thus its stationary law is unique and empirical lag-one agreements converge almost surely to \((1+R_n)/2\).

## Proof
**1. Stationary covariance equations.** Write \(C_{xy}=\mathbb E[\sigma_t(x)\sigma_t(y)]\) in stationarity. Then \(C_{xx}=1\). For distinct vertices, conditioning on the two independent fresh updates gives
\[
C_{xy}=q\sum_{u\sim x}\sum_{v\sim y}\frac{C_{uv}}{\deg(x)\deg(y)}.
\]
The update rule is spin-flip symmetric, and any term involving an independent fair refresh vanishes. The operator on off-diagonal covariances contracts in supremum norm by at most \(q<1\), so these equations determine the off-diagonal covariances uniquely. Rotational symmetry therefore implies that \(C_{h,i}=a\) for each rim vertex and \(C_{i,i+d}=b_d\) for \(d\in\mathbb Z/n\mathbb Z\), with \(b_0=1\) and \(b_d=b_{-d}\). Put \(S=n^{-1}\sum_{d=0}^{n-1}b_d\).

The hub/rim covariance equation and the rim/rim equations are respectively
\[
a=q\left(\frac a3+\frac{2S}{3}\right),\qquad
b_d=\frac q9\left(1+4a+b_{d-2}+2b_d+b_{d+2}\right)\quad(d\ne0),
\]
with indices modulo \(n\). Therefore \(a=kS\) with \(k=2q/(3-q)\). Setting \(x=\alpha(1+4a)\) with \(\alpha=q/(9-4q)\), the change of variables \(b_d=x+(1-x)u_d\) gives \(u_0=1\) and
\[
u_d=\frac q9(u_{d-2}+2u_d+u_{d+2})\quad(d\ne0).
\]
Since \(0<q<1\), \(x<1\), so the change of variables is valid.

**2. Exact two-step Green function.** Let \(T\) be the cyclic shift on functions on \(\mathbb Z/n\mathbb Z\) and \(L=I-(q/9)(T^2+2I+T^{-2})\). The spectral radius of \((q/9)(T^2+2I+T^{-2})\) is at most \(4q/9<1\), so \(G=L^{-1}\mathbf1_{\{0\}}\) exists and has \(G_0>0\). The function \(u_d=G_d/G_0\) is the unique solution of the boundary equations above. Summing \(LG=\mathbf1_{\{0\}}\) gives \(\sum_dG_d=(1-4q/9)^{-1}=\delta^{-2}\), and hence
\[
\frac1n\sum_d u_d=\frac{1}{n\delta^2G_0}.
\]
For \(\ell_n=n/\gcd(n,2)\), the eigenvalues of \(T^2\) are the \(\ell_n\)-th roots of unity, each with multiplicity \(\gcd(n,2)\). Consequently, writing \(A=1-2q/9\) and \(B=2q/9\),
\[
G_0=\frac1{\ell_n}\sum_{j=0}^{\ell_n-1}\frac1{A-B\cos(2\pi j/\ell_n)}.
\]
The identity \(t=B/(A+\delta)\), \(A^2-B^2=\delta^2\), and the absolutely convergent Poisson-kernel expansion
\[
\frac1{A-B\cos\theta}=
\frac1\delta\left(1+2\sum_{r\ge1}t^r\cos(r\theta)\right)
\]
show, by averaging over roots of unity, that
\[
G_0=\frac1\delta\frac{1+t^{\ell_n}}{1-t^{\ell_n}}.
\]
It follows that \(n^{-1}\sum_du_d=H_n\). Since \(S=x+(1-x)H_n\), solving \(a=kS\) and \(x=\alpha(1+4a)\) gives \(a=F_q(H_n)\). The hub's next spin, when not refreshed, comes from a uniform rim vertex, so \(R_n=ca\).

**3. Strict ordering.** First, \(t\in(0,1/6)\). Indeed \(t+t^{-1}=9/q-2>7\), and the solution below one at the right endpoint \(q=1\) is \((7-3\sqrt5)/2<1/6\). Since \(0<t<1\),
\[
H_n>\frac{1-2t^{\ell_n}}{n\delta}.
\]
For \(n=3\), \(2(n+1)t^{\ell_n}<8/6^3<1\). For \(n\ge4\), \(\ell_n\ge\lfloor n/2\rfloor\) and \(2(n+1)/6^{\lfloor n/2\rfloor}<1\): check \(n=4,5\), then increase \(n\) by two. Thus \(H_n>1/((n+1)\delta)>H_{n+1}\), simultaneously covering even and odd rim sizes.

Finally,
\[
F_q'(H)=\frac{k[1-\alpha(1+4k)]}{[1-4k\alpha(1-H)]^2}>0,
\]
because \(1-\alpha(1+4k)=3(1-q)(9+q)/((3-q)(9-4q))>0\) and \(4k\alpha<1\). It follows that \(R_n=cF_q(H_n)>cF_q(H_{n+1})=R_{n+1}\).

**4. Large-rim expansion.** Since \(\ell_n\ge n/2\) and \(t<1\), \(H_n=1/(n\delta)+O_q(t^{n/2}/n)\). Taylor expansion of the rational function \(F_q\) at zero gives
\[
F_q(0)=\frac{2q^2}{D},\qquad
F_q'(0)=\frac{6q(1-q)(9+q)(9-4q)}{D^2}.
\]
This proves the asserted \(n^{-1}\) expansion. Indeed, \(n^2(H_n-H_{n+1})\to1/\delta\) because the deviations of \(H_j\) from \(1/(j\delta)\) are exponentially small. By the mean value theorem, \(F_q(H_n)-F_q(H_{n+1})=F_q'(\xi_n)(H_n-H_{n+1})\) for some \(\xi_n\in(H_{n+1},H_n)\), and \(\xi_n\to0\). Continuity of \(F_q'\) now yields the asserted \(n^2\)-rescaled gap limit. \(\square\)

## Verification
The accompanying executable `verify.py` independently assembles the full off-diagonal stationary covariance equations for each finite wheel, solves them in exact rational arithmetic, and compares the hub/rim covariance against the spectral formula evaluated to 90 decimal digits. For \(q\in\{1/4,4/9,9/16\}\) and \(3\le n\le10\), all 24 exact pair-systems agree with the formula to better than \(10^{-70}\). Additional exact finite inequalities and high-precision large-index evaluations are checked. Execute `python3 verify.py` using the Python standard library. One check is \(a=2/29\) for \(n=3,q=1/4\), the case \(W_4=K_4\). The checker does not certify all \(n\) or all noise levels; those quantifiers follow from the proof.

## Relationship to prior work
Benjamini, Helman Tov and Zhukovskii (first publicly posted 2022-07-04) introduce local temporal agreement observations for synchronous noisy voting and establish distinguishability for complete graphs, cycles, certain perfect trees, and several other examples. Their Theorems 1.1–1.5 and the complete-bipartite comparison in Section 6 do not state the hub-rooted wheel theorem or its exact one-lag ordering. The present argument derives a wheel-specific Green-function expression and proves monotonicity uniformly in noise and size. Earlier noisy-voter research on heterogeneous networks analyzes other update conventions and aggregate observables; it does not by itself imply this single-root lag-one identification. These comparisons indicate distinct coverage, not proof of historical priority.

## Limitations
The statement concerns simple wheel graphs with \(n\ge3\), known fixed refresh probability, synchronous independent updates, and a hub-only stationary time series. It does not determine an unknown noise parameter jointly with the graph size, provide finite-sample confidence bounds, or assert identification among arbitrary rooted graphs. Numerical testing covers only finite illustrative instances; the infinite and all-parameter assertions rely on the algebraic proof. Independent audit and historical-priority confirmation have not been performed.

## References
1. I. Benjamini, H. Helman Tov, M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, arXiv:2207.01224, first version 2022-07-04, https://arxiv.org/abs/2207.01224 (especially Theorems 1.1–1.5 and Section 6).
2. R. Pymar, N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478, first version 2021-12-02, https://arxiv.org/abs/2112.01478 (different update and global-density setting).
3. A. F. Peralta, A. Carro, M. San Miguel, R. Toral, *Stochastic pair approximation treatment of the noisy voter model*, New Journal of Physics 20 (2018), DOI:10.1088/1367-2630/aae7f5 (different approximation framework).
