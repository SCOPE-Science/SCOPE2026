# Hermite-law thresholds for odd capped Boolean Hamming metrics

## Finding
For every fixed odd integer \(r=2m+1\ge5\), the sharp negative-type exponent of the capped Hamming metric on the Boolean \(n\)-cube satisfies
\[
\lim_{n\to\infty}n^m\beta_{n,r}=\frac{(2m)!}{M_m\log(r/(r-1))},\qquad M_m=-\min_{t\in\mathbb R}H_{2m}(t)>0.
\]
Here \(H_j\) is the probabilists' Hermite polynomial, determined by \(\exp(tu-u^2/2)=\sum_{j\ge0}H_j(t)u^j/j!\). For the first new odd cap,
\[
\lim_{n\to\infty}n^2\beta_{n,5}=\frac4{\log(5/4)}=17.9256805\ldots,
\]
and every endpoint-critical Walsh frequency has \((n-2k)/\sqrt n\) approaching the set \(\{-\sqrt3,\sqrt3\}\). For cap seven, direct evaluation of \(\min H_6=-40-20\sqrt{10}\) yields
\[
\lim_{n\to\infty}n^3\beta_{n,7}=\frac{36}{(2+\sqrt{10})\log(7/6)}.
\]
The result characterizes how an odd cap's Fourier obstruction migrates into central-limit-scale Hamming frequencies.

## Assumptions and scope
Fix \(m\in\mathbb Z\) with \(m\ge2\) and put \(r=2m+1\). For each \(n\ge r\), let \(G_n=\mathbb F_2^n\) and define \(d_{n,r}(x,y)=\min\{\operatorname{wt}(x-y),r\}\). This is a genuine translation-invariant metric: the positive, increasing, subadditive map \(u\mapsto\min\{u,r\}\) preserves the triangle inequality. A powered distance is conditionally negative definite (CND) if for every real function \(c\) on \(G_n\) with \(\sum_x c(x)=0\),
\[
\sum_{x,y\in G_n}c(x)c(y)d_{n,r}(x,y)^p\le0.
\]
Define \(\beta_{n,r}=\sup\{p>0:d_{n,r}^p\text{ is CND}\}\). For each sufficiently large \(n\), the proof shows \(0<\beta_{n,r}<\infty\). The exponent is an exponent of the metric's entries, not a change of the vertex set or of the graph shortest-path distance.

## Proof
**1. Exact Fourier spectrum.** Fix a nonzero Walsh frequency \(a\in G_n\) of Hamming weight \(k\in\{1,\dots,n\}\). Put \(s=n-2k\) and define the binary Krawtchouk values
\[
K_j(n,k)=[z^j](1-z)^k(1+z)^{n-k},\qquad
(j+1)K_{j+1}=sK_j-(n-j+1)K_{j-1},
\]
with \(K_0=1\), \(K_1=s\). Since \(\sum_x(-1)^{a\cdot x}=0\), the eigenvalue of the powered distance matrix in this Walsh direction equals
\[
\lambda_{n,k}(p)=-r^p+\sum_{j=1}^{r-1}(j^p-r^p)K_j(n,k).\tag{1}
\]
The trivial Walsh frequency does not enter conditional negative definiteness, so \(d_{n,r}^p\) is CND exactly when \(\lambda_{n,k}(p)\le0\) for all \(1\le k\le n\). At \(p=0\) every nonconstant eigenvalue is \(-1\).

**2. Critical-scale polynomial maximization.** Set \(d=r-1=2m\) and \(p_n=\alpha n^{-m}\) for fixed \(\alpha>0\). Let
\[
A_j(p)=\frac{j^p-r^p}{p}\quad(1\le j\le d),\qquad
L_{n,p}(k)=\sum_{j=1}^d A_j(p)K_j(n,k).
\]
Then \(\lambda_{n,k}(p)=-r^p+pL_{n,p}(k)\) and \(A_j(p_n)\to\log(j/r)<0\), uniformly over the finite set of indices. The generating function above, with \(s=t\sqrt n\), gives, uniformly on each fixed bounded set of \(t\),
\[
 n^{-j/2}K_j(n,k)\longrightarrow\frac{H_j(t)}{j!}.
\]
Indeed, substitute \(z=u/\sqrt n\) in \((1-z^2)^{n/2}\exp(s\operatorname{artanh}z)\); the exponent converges uniformly for \(u,t\) in bounded complex sets to \(tu-u^2/2\), so fixed coefficients converge. Consequently, uniformly for bounded \(t\),
\[
 n^{-m}L_{n,p_n}(k)\longrightarrow
-\frac{\log(r/(r-1))}{(2m)!}H_{2m}(t).\tag{2}
\]
This local limit controls the *global* maximum as well. To verify that no remote Walsh frequencies are missed, iterate the displayed recurrence at each fixed degree \(j\): for \(|s|\ge R\sqrt n\), with \(R\) sufficiently large depending only on \(m\),
\[
K_{2m}(n,k)=\frac{s^{2m}}{(2m)!}\bigl(1+O_m(n/s^2)\bigr)>0,
\qquad |K_j(n,k)|\le C_m|s|^j\quad(j<2m).
\]
These estimates follow by induction, since each lower-degree correction introduces a factor \(O_m(n/s^2)\). As \(A_{2m}(p_n)\) is bounded above by a fixed negative number, its \(|s|^{2m}\) contribution dominates the bounded-coefficient terms of lower degree uniformly on \(|s|\ge R\sqrt n\) for all sufficiently large \(n\). Thus \(L_{n,p_n}(k)<0\) outside that central region. Within it, mesh points \((n-2k)/\sqrt n\) become dense, so (2) proves
\[
\max_{1\le k\le n}\frac{L_{n,p_n}(k)}{n^m}
\longrightarrow C_m:=\frac{M_m\log(r/(r-1))}{(2m)!}>0.\tag{3}
\]
The positivity of \(M_m\) follows from the Gaussian orthogonality relation \(\int_{\mathbb R}H_{2m}(t)e^{-t^2/2}dt=0\), as \(H_{2m}\) is nonconstant and positive for sufficiently large \(|t|\).

**3. Sharp exponent and endpoint frequencies.** By (1) and (3), for every fixed \(\alpha>0\),
\[
\max_{1\le k\le n}\lambda_{n,k}(\alpha n^{-m})
\longrightarrow-1+\alpha C_m.\tag{4}
\]
Take any \(\alpha_-<C_m^{-1}<\alpha_+\). For sufficiently large \(n\), all nonconstant eigenvalues are strictly negative at \(p=\alpha_-n^{-m}\), while some are strictly positive at \(p=\alpha_+n^{-m}\). CND exponents form an initial interval: if \(d^p\) is CND, so is \(d^q\) for \(0<q<p\), since \(t\mapsto t^{q/p}\) preserves CND through the Bernstein-function integral representation. Hence
\[
\alpha_-n^{-m}\le\beta_{n,r}\le\alpha_+n^{-m},
\]
which proves the limit. By continuity of all finitely many eigenvalues, some nonconstant Walsh eigenvalue is zero at the finite positive endpoint for sufficiently large \(n\). If its frequency weight is \(k_n\), then (1), (3) and the limiting exponent force \(n^{-m}L_{n,\beta_{n,r}}(k_n)\to C_m\). The tail exclusion and (2) imply every accumulation point of \((n-2k_n)/\sqrt n\) minimizes \(H_{2m}\). For \(m=2\), \(H_4(t)=t^4-6t^2+3\) has global minimum \(-6\) only at \(t=\pm\sqrt3\), giving the cap-five coefficient and critical-frequency localization. For \(m=3\), \(H_6(t)=t^6-15t^4+45t^2-15\) has global minimum \(-40-20\sqrt{10}\), giving the cap-seven coefficient.

## Verification
The standalone `odd_cap_walsh_check.py` verifies the exact Krawtchouk recurrence against complete Walsh-character enumeration in dimensions \(3\) through \(8\), then numerically brackets the first nonconstant spectral zero for caps \(3\), \(5\), and \(7\) in dimensions up to \(1000\). For cap five, \(n^2\beta_{n,5}\) is approximately \(19.6455\) at \(n=100\), \(18.2649\) at \(n=500\), and \(18.0953\) at \(n=1000\), approaching \(4/\log(5/4)=17.9257\ldots\). These finite checks corroborate, but do not prove, the all-dimension limit; the proof rests on (1)–(4).

## Relationship to prior work
The finite-metric negative-type framework and determinant approach are established in Sánchez, *On the supremal p-negative type of a finite metric space* (2011, arXiv:1108.0451). Murugan, *Generalized roundness of vertex transitive graphs* (2011, arXiv:1112.5657), gives a spectral criterion for vertex-transitive metrics and a result for subsets of the **uncapped** Hamming cube. Dominici, *Asymptotic analysis of the Krawtchouk polynomials by the WKB method* (2005, arXiv:math/0501042), develops Krawtchouk-to-Hermite limits. These ingredients are credited. The present asymptotic analysis additionally requires a global-in-frequency maximization of the *specific capped metric's* Walsh eigenvalues, giving an odd-cap family threshold rather than a general computation recipe or a standalone polynomial limit. The previously determined cap-three case provides a consistency check, whereas earlier even-cap behavior uses a different Fourier scale.

## Limitations
The cap is fixed and odd, at least five, as dimension tends to infinity. No exact finite-dimensional threshold formula is claimed for cap five or higher, and the proof gives localization to Hermite minimizers rather than a unique critical frequency at each finite dimension. The finite checker is not an infinite proof. A historical formula in a specialized source could imply the result; the primary-literature comparison is bounded and independent priority review has not been performed.

## References
1. D. Dominici, *Asymptotic analysis of the Krawtchouk polynomials by the WKB method* (first public arXiv version 2005-01-04), arXiv:math/0501042, https://arxiv.org/abs/math/0501042.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space* (first public arXiv version 2011-08-02), arXiv:1108.0451, https://arxiv.org/abs/1108.0451.
3. M. K. Murugan, *Generalized roundness of vertex transitive graphs* (first public arXiv version 2011-12-23), arXiv:1112.5657, https://arxiv.org/abs/1112.5657.
