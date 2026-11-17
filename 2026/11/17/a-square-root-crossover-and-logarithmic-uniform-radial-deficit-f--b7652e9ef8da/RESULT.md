# A square-root crossover and logarithmic-uniform radial deficit for harmonic polytopes

## Finding
Let \(H_{n,n}\subset\mathbb R^n\times\mathbb R^n\) be the standard Ardila–Escobar harmonic polytope, where \(n\ge2\), and let \(V_n\) be a vertex chosen uniformly from its **distinct vertices**. Let
\[
c_n=\left(\left(\frac{n+1}{2}+\frac1n\right)\mathbf1,\left(\frac{n+1}{2}+\frac1n\right)\mathbf1\right),
\qquad R_n^2=\frac{(n^2-1)(n^2+12)}{6n}.
\]
The center and radius here are the known unique minimum enclosing Euclidean sphere of this polytope. Define the squared-radius deficit
\[
D_n=\frac{R_n^2-\|V_n-c_n\|_2^2}{2}\in\{0,\ldots,n-1\},\qquad Z_n=\frac{\log\max\{1,D_n\}}{\log n}.
\]
Then **the logarithmic radial deficit converges to the uniform distribution on \([1/2,1]\)**:
\[
\boxed{Z_n\ \xrightarrow[n\to\infty]{\mathrm d}\ \operatorname{Uniform}([1/2,1]).}
\]
In particular, for each \(1/2<t<1\),
\[
\boxed{\lim_{n\to\infty}\Pr\{D_n\le n^t\}=2t-1,}
\]
and the corresponding limits are \(0\) for \(t\le1/2\) and \(1\) for \(t\ge1\). Moreover,
\[
\lim_{n\to\infty}\mathbb E Z_n=\frac34,\qquad
\lim_{n\to\infty}\operatorname{Var}(Z_n)=\frac1{48}.
\]

There is an explicit, nontrivial transition profile at squared-radius deficit of order \(\sqrt n\). Set
\[
H_n=\sum_{j=1}^n\frac1j,\qquad w_n(d)=H_n\Pr\{D_n=d\}.
\]
For any fixed \(x>0\) and integers \(d_n\) satisfying \(d_n/\sqrt n\to x\),
\[
\boxed{\sqrt n\, w_n(d_n)\longrightarrow
x\int_0^1\exp\{-x^2u(1-u)\}\,du.}
\]
The two matching scales are
\[
w_n(d)\sim\frac{d+1}{n}\quad(d=o(\sqrt n)),
\qquad
w_n(d)\sim\frac2d\quad(\sqrt n\ll d\ll n).
\]
All these statements use the uniform **vertex** law, not Euclidean-volume, facet-area, or Gaussian-normal-cone sampling.

## Assumptions and scope
The polytope has its source's unscaled Euclidean coordinate realization
\[
H_{n,n}=(\Pi_n\times\Pi_n)+\operatorname{conv}\{e_i+f_i:1\le i\le n\},
\]
where \(\Pi_n\) is the permutation polytope of \((1,\ldots,n)\), and \(e_i,f_i\) belong to distinct coordinate blocks. The inherited metric is the standard one in \(\mathbb R^{2n}\). Every fine harmonic triple \((k;\pi_1,\pi_2)\) labels exactly one vertex, as shown in the primary source. All limits refer to integer \(n\to\infty\); a variable \(d=d_n\) is integral with \(0\le d\le n-1\). The notation \(a_n\sim b_n\) means ratio tending to one for the indicated parameter sequences. The previously published shell spectrum and multiplicities are inputs, not new claims.

## Proof
**1. An exact shell-probability identity.** Ardila–Escobar, Proposition 3.6 and the proof of Proposition 3.5, show that a vertex is specified by a distinguished label \(k\) and two permutations. Each other label belongs to one of three groups of sizes \(a,b,c\): before \(k\) only in the first permutation, before \(k\) in both, or before \(k\) only in the second. The fourth possibility, after \(k\) in both, is excluded. Thus \(a+b+c=n-1\). The established Euclidean shell theorem gives
\[
\|v-c_n\|^2=R_n^2-2(n-1-b),
\]
and counts vertices with given \(b\) by
\[
M_{n,b}=\frac{n!}{b!}\sum_{a=0}^{n-1-b}(a+b)!(n-1-a)!.
\]
The total vertex number, from Ardila–Escobar, is \((n!)^2H_n\). Hence for \(d=n-1-b\),
\[
\begin{aligned}
w_n(d)&=\frac{M_{n,n-1-d}}{(n!)^2}\\
&=\frac1n\sum_{a=0}^{d}R_{n,d}(a),\\
R_{n,d}(a)&=\frac{(n-1-d+a)!(n-1-a)!}{(n-1-d)!(n-1)!}
=\frac{\binom{n-1-d+a}{a}}{\binom{n-1}{a}}.
\end{aligned}
\tag{1}
\]
Every term is in \((0,1]\), and \(R_{n,d}(a)=R_{n,d}(d-a)\). Formula (1) proves \(\sum_{d=0}^{n-1}w_n(d)=H_n\), with no asymptotic approximation.

**2. Global controls.** For \(d\ge1\) and \(0\le a\le\lfloor d/2\rfloor\),
\[
R_{n,d}(a)=\prod_{j=1}^{a}\left(1-\frac{d+1-2j}{n-j}\right).
\]
Since \(\log(1-z)\le-z\) for \(0\le z<1\),
\[
R_{n,d}(a)\le\exp\left\{-\frac{a(d-a)}n\right\}
\le\exp\left\{-\frac{ad}{2n}\right\}.
\tag{2}
\]
The symmetry in (1), together with \(1/(1-e^{-u})\le1+1/u\) for \(u>0\), gives
\[
0<w_n(d)\le\min\left\{\frac{d+1}{n},\frac2n+\frac4d\right\}.
\tag{3}
\]
Also \(w_n(0)=1/n\). It follows that \(\sum_{d\le\sqrt n}w_n(d)=O(1)\), and, for each fixed \(\varepsilon>0\),
\[
\sum_{\sqrt n<d\le n^{1/2+\varepsilon}}w_n(d)
\le4\varepsilon\log n+O(1)+o(\log n).
\tag{4}
\]

**3. The square-root crossover.** For \(d=O(\sqrt n)\), uniformly over \(0\le a\le d\), expansion of the logarithms of the factorial ratios in (1) yields
\[
\log R_{n,d}(a)=-\frac{a(d-a)}n+O\left(\frac{d^3+d^2}{n^2}\right).
\tag{5}
\]
To see this directly, the factors are \(1-(d+1-2j)/(n-j)\); summing their linear terms gives \(-a(d-a)/n\), and the error from replacing denominators by \(n\), and from the quadratic Taylor remainders, is at most a constant times \((d^3+d^2)/n^2\) when \(d\le C\sqrt n\). Thus if \(d/\sqrt n\to x>0\), (1) and a Riemann sum give
\[
\sqrt n\,w_n(d)=\frac{\sqrt n}{n}\sum_{a=0}^d
\exp\left\{-\frac{a(d-a)}n+o(1)\right\}
\longrightarrow x\int_0^1e^{-x^2u(1-u)}\,du.
\]
When \(d=o(\sqrt n)\), the same expansion gives \(R_{n,d}(a)=1+o(1)\) uniformly, hence \(w_n(d)\sim(d+1)/n\), including bounded \(d\).

**4. The inverse-deficit regime.** Suppose \(\sqrt n\ll d\ll n\). On the scale \(0\le a\le L n/d\), for any fixed \(L>0\),
\[
\log R_{n,d}(a)=-\frac{ad}{n}+o(1)
\tag{6}
\]
uniformly. Indeed, the error is bounded by a constant multiple of \(a^2/n+ad^2/n^2+a/n\), which tends to zero because \(n/d^2\to0\) and \(d/n\to0\). The sum over this interval is asymptotic to \((n/d)(1-e^{-L})\). For \(Ln/d<a\le d/4\), (2) improves to \(R_{n,d}(a)\le e^{-3ad/(4n)}\), and its tail sum is \(O((n/d)e^{-3L/4})\). For \(d/4<a\le d/2\), (2) gives \(R_{n,d}(a)\le e^{-3d^2/(16n)}\); the summed tail is \(o(n/d)\). Letting \(L\to\infty\), the half-sum is asymptotic to \(n/d\); symmetry doubles it. Consequently,
\[
\boxed{w_n(d)\sim2/d\quad(\sqrt n\ll d\ll n).}
\tag{7}
\]
All estimates here are uniform when \(n^{1/2+\varepsilon}\le d\le n^t\) for fixed \(\varepsilon>0\) and \(t<1\).

**5. The weak limit.** For \(1/2<t<1\), fix \(0<\varepsilon<t-1/2\). The uniform estimate (7) gives
\[
\sum_{n^{1/2+\varepsilon}\le d\le n^t}w_n(d)
=2\left(t-\frac12-\varepsilon\right)\log n+o(\log n).
\]
By (3)–(4) the smaller-deficit contribution is nonnegative and at most \(4\varepsilon\log n+o(\log n)\). Since \(H_n=\log n+O(1)\), division by \(H_n\) and then \(\varepsilon\downarrow0\) prove
\[
\Pr\{D_n\le n^t\}\longrightarrow2t-1.
\]
At \(t\le1/2\) the probability tends to zero by (3), and at \(t\ge1\) it is one for sufficiently large \(n\). This proves the convergence in distribution. Because \(0\le Z_n\le1\), bounded convergence of the first two moments under weak convergence gives \(\mathbb EZ_n\to3/4\) and \(\operatorname{Var}(Z_n)\to1/48\).

## Verification
The included dependency-free `verify.py` enumerates all fine harmonic triples for \(2\le n\le5\) from the primary maximality criterion. It reconstructs the Euclidean coordinates and verifies exact squared distances, each shell multiplicity, the closed ratio (1), and the total vertex count. A numerically stable symmetry-based recurrence also checks the probability normalization and the global inequalities (3) at \(n=100,400,1200\). These are **finite corroborations**, not an infinite proof; steps 3–5 supply the analytical asymptotics. To replay, run `python3 verify.py` with the package's Python file and no dependencies beyond the standard library.

## Relationship to prior work
Ardila and Escobar [1] establish fine harmonic triples, vertex coordinates and total count. A published exact-shell theorem [3] already gives **every finite shell multiplicity** and the circumcenter, which are explicitly credited above; this result does **not** claim a new finite shell enumeration, circumradius or incenter. The contribution here is the square-root critical profile and the continuous logarithmic-uniform distribution for a uniformly sampled vertex. These require an asymptotic analysis of the factorial ratio in (1); they are not stated in the source's finite enumeration. Ardila's bipermutahedron results [2] concern a related but different polytope and the Minkowski quotient. Related work [4] computes covariance of uniformly sampled harmonic vertices, a different aggregate statistic that does not identify the deficit's nonconcentrated logarithmic law.

## Limitations
The critical profile and limit law apply only to the canonical coordinate realization and uniform **distinct-vertex** sampling. The earlier exact-shell theorem determines the entire finite distribution and thus is the essential stronger finite source; this result should be interpreted strictly as a new asymptotic analysis, not an independent exact enumeration. It does not establish a finite-\(n\) convergence rate or characterize nonvertex boundary-point sampling. Earlier equivalent asymptotic interpretations of the known shell counts would affect historical priority. No independent mathematical audit is asserted.

## References
1. Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078v1, first public 2020-06-04; Selecta Mathematica 27 (2021), article 91, DOI 10.1007/s00029-021-00687-6. Full primary text: https://arxiv.org/pdf/2006.03078.
2. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295v1, first public 2020-08-05; Combinatorial Theory 2(3) (2022). Full primary text: https://arxiv.org/pdf/2008.02295.
3. *Harmonic-polytope vertices form exactly n Euclidean shells*, published mathematical research record, 2026-10-11: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-harmonic-polytope-vertices-form-exactly-n-euclidean-shells--f2f2da42b2f8.
4. *A nine-label covariance-axis reversal in harmonic polytopes*, published mathematical research record, 2026-11-08: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-nine-label-covariance-axis-reversal-in-harmonic-polytopes--140bb9bcc506.
