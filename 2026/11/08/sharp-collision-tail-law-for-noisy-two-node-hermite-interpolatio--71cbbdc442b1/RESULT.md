# Sharp collision-tail law for noisy two-node Hermite interpolation

## Finding
Fix an integer \(m\geq1\), put \(d=2m-1\), and let \(X,Y\) be independent uniform random variables on \([0,1]\). Let \(f\in C^{2m}([0,1])\) be deterministic. Independently of \((X,Y)\), sample a random vector of real jet errors \((\varepsilon_{X,j},\varepsilon_{Y,j})_{j=0}^{m-1}\), all of whose entries have a common deterministic absolute bound. Different entries of this vector may be dependent. Assume
\[
Z=|\varepsilon_{Y,0}-\varepsilon_{X,0}|,\qquad \Pr\{Z>0\}>0.
\]
For \(X\ne Y\), let \(P_m\) be the unique polynomial of degree at most \(2m-1\) satisfying, for every \(j=0,\dots,m-1\),
\[
P_m^{(j)}(X)=f^{(j)}(X)+\varepsilon_{X,j},\qquad
P_m^{(j)}(Y)=f^{(j)}(Y)+\varepsilon_{Y,j}.
\]
Set \(E_m=\|P_m-f\|_{L^2(0,1)}\),
\[
B_m=\binom{2m-2}{m-1},\qquad
M_d(x)=\left(\frac{x^{2d+1}+(1-x)^{2d+1}}{2d+1}\right)^{1/2}.
\]
Then the following strictly positive, finite, *exact tail constant* exists:
\[
\boxed{\lim_{T\to\infty}T^{1/d}\Pr\{E_m>T\}=C_m
:=2B_m^{1/d}\,\mathbb E[Z^{1/d}]\int_0^1M_d(x)^{1/d}\,dx.}
\]
Consequently, for every real \(p>0\),
\[
\boxed{\mathbb E[E_m^p]<\infty\quad\Longleftrightarrow\quad p<\frac1{2m-1}.}
\]
In particular, the ordinary mean error is infinite for every \(m\ge1\); the cubic, first-derivative Hermite scheme \((m=2)\) has tail exponent \(1/3\). The constant depends on the value-error difference, but not on the derivative errors or on \(f\).

## Assumptions and scope
The knot positions are independently uniform over the *same* interval, not selected from distinct strata and not conditioned to have a minimum separation. The jet errors are bounded, jointly arbitrary but independent of the knot positions. Their first two value components differ with positive probability. The polynomial is the *exact* interpolant of all noisy observations, without regularization, rounding or overdetermined least-squares fitting. The error is evaluated over the fixed full interval \([0,1]\), not only between the knots. The null event \(X=Y\) may be defined arbitrarily.

## Proof
**1. Cardinal functions and the collision coefficient.** Write \(h=Y-X\ne0\) and \(z=(t-X)/h\). Let \(U_{m,j}(z),V_{m,j}(z)\) be the unique degree-at-most-\(d\) cardinal Hermite polynomials having their derivatives of orders \(0,\dots,m-1\) equal to \(\delta_{jk}\) at, respectively, \(z=0\) and \(z=1\), and all corresponding derivatives zero at the other endpoint. The cardinal polynomial associated with the right endpoint's *value* is explicitly
\[
R_m(z)=V_{m,0}(z)=z^m\sum_{k=0}^{m-1}\binom{m+k-1}{k}(1-z)^k.
\]
The factor \(z^m\) forces vanishing of the first \(m\) derivatives at zero; the truncated binomial series for \(z^{-m}=(1-(1-z))^{-m}\) makes \(R_m(z)=1+O((1-z)^m)\) at one. The degree is at most \(d\); its highest coefficient is
\[
[z^d]R_m(z)=(-1)^{m-1}\binom{2m-2}{m-1}=:c_m,
\]
with \([z^d]U_{m,0}=-c_m\), since \(U_{m,0}+V_{m,0}=1\). These identities also cover \(m=1\).

**2. Uniform collision limit.** Let \(H_{f,X,Y}\) be the noiseless degree-\(d\) Hermite interpolant. By uniqueness and the scaling of derivatives under \(t=X+hz\),
\[
P_m(t)-H_{f,X,Y}(t)=\sum_{j=0}^{m-1}h^j\bigl(\varepsilon_{X,j}U_{m,j}((t-X)/h)+\varepsilon_{Y,j}V_{m,j}((t-X)/h)\bigr).
\]
Each cardinal polynomial is fixed and has degree at most \(d\). Expanding in powers of \((t-X)/h\), multiplying by \(h^d\), and using the uniform bound on the errors shows, uniformly over \(t,X\in[0,1]\), over all admissible jet vectors, and all sufficiently small nonzero \(h\) with \(X+h\in[0,1]\),
\[
h^d(P_m(t)-H_{f,X,Y}(t))=c_m(\varepsilon_{Y,0}-\varepsilon_{X,0})(t-X)^d+O(|h|).
\]
All jet orders \(j\ge1\) enter the scaled expression only at order \(O(|h|)\). The standard Hermite interpolation remainder on a real compact interval gives the global bound
\[
\|H_{f,X,Y}-f\|_{L^\infty(0,1)}\le\frac{\|f^{(2m)}\|_\infty}{(2m)!}\max_{t\in[0,1]}|(t-X)^m(t-Y)^m|\le\frac{\|f^{(2m)}\|_\infty}{(2m)!}.
\]
Thus, for \(E_m=\|P_m-f\|_2\),
\[
\lim_{h\to0,\,X+h\in[0,1]}|h|^d E_m=B_m Z\|(\cdot-X)^d\|_2=B_mZM_d(X),
\]
with convergence uniform in the allowed parameters. The same polynomial expansion on \(|h|\le1\) supplies a deterministic constant \(K<\infty\) such that \(|h|^d E_m\le K\) everywhere.

**3. Exact tail coefficient.** Put \(\rho=T^{1/d}\). Using the joint density of \((X,Y)\), then \(h=Y-X\) and \(u=\rho h\), gives
\[
\rho\Pr\{E_m>T\}=\int_0^1dx\int_{\mathbb R}du\;\mathbf1_{\{0\le x+u/\rho\le1\}}\,\mathbb E\left[\mathbf1_{\{E_m(x,x+u/\rho)>T\}}\right].
\]
The deterministic bound in Step 2 forces \(|u|\le K^{1/d}\) whenever the integrand is nonzero. For almost every \(x\in(0,1)\) and \(u\ne0\), the uniform collision limit makes the event converge, except on a Lebesgue-null threshold boundary, to \(\{|u|^d<B_mZM_d(x)\}\). Bounded convergence (first over the bounded \(u\)-range and then over \(x\) and the bounded noise vector) gives
\[
\lim_{T\to\infty}\rho\Pr\{E_m>T\}=\int_0^1\mathbb E\left[2(B_mZM_d(x))^{1/d}\right]dx=C_m.
\]
The constant is finite since the noises are bounded and \(M_d\) is bounded, and positive by \(\Pr(Z>0)>0\).

**4. Sharp moment threshold.** The layer-cake identity \(\mathbb E[E_m^p]=p\int_0^\infty T^{p-1}\Pr(E_m>T)\,dT\) for \(p>0\), together with the positive finite \(T^{-1/d}\) tail equivalent from Step 3, shows convergence exactly when \(p<1/d\); equality diverges logarithmically. This completes the proof.

## Verification
The standalone script `verification/check_hermite_tail.py` uses Python's `fractions.Fraction` for exact construction and solution of the real confluent Hermite systems. It checks the cardinal leading coefficient for \(m=1,\dots,8\), the endpoint derivative constraints, and exact squared-error scaling toward the limit at decreasing rational spacings for \(m=1,\dots,6\), plus evaluations of sample reciprocal-gap normalization formulas. Run `python verification/check_hermite_tail.py` using Python 3 and its standard library; the checked execution reported 281 passed assertions. These finite checks are not a proof of the universal distributional limit, which follows from Steps 1–4.

## Relationship to prior work
Batenkov and Diab [1] prove deterministic singular-value and worst-case reconstruction bounds for Fourier confluent Vandermonde matrices under clustered nodes. Their measured objects and worst-case norms do not imply the explicit unconditional random-knot \(L^2\) error-tail constant here. Niu, Zhang and Zhou [2] study Arnoldi stabilization and polynomial derivative evaluation for confluent Vandermonde/Hermite systems, but do not derive iid-knot heavy-tail probabilities. Zhang and collaborators [3] develop multivariate Hermite least-squares methods; their stabilized overdetermined setting is not this exact, square, unregularized interpolation problem. Respondek [4] surveys confluent-matrix inversion, not the random-knot law, and Gautschi [5] provides classical inverse-norm bounds (only an abstract was accessible for [5]). A separate known deterministic knot-collision instability does not by itself give this distributional coefficient, although it motivates the problem.

## Limitations
The tail law is restricted to iid uniform knots on \([0,1]\), bounded node-independent noise jets with a nonzero value discrepancy, finite fixed Hermite order, and global \(L^2\) error of the exact interpolating polynomial. If the value errors coincide almost surely, derivative-noise exponents may instead dominate and the stated coefficient vanishes; that case is not classified. Node repulsion, enforced minimum spacing, regularization, alternative norms, and high-order random-node ensembles require independent analysis. The proof is mathematical, not a floating-point stability guarantee; older specialized literature may contain equivalent formulations.

## References
[1] D. Batenkov and N. Diab, *Super-resolution of generalized spikes and spectra of confluent Vandermonde matrices*, first public arXiv version 2022-03-22, https://arxiv.org/abs/2203.11923 (full text https://arxiv.org/pdf/2203.11923).

[2] Q. Niu, H. Zhang and Y. Zhou, *Confluent Vandermonde with Arnoldi*, first public arXiv version 2022-07-05, https://arxiv.org/abs/2207.01852 (full text https://arxiv.org/pdf/2207.01852).

[3] *Multivariate confluent Vandermonde with G-Arnoldi and applications*, first public 2024-04-14, https://arxiv.org/abs/2404.09266.

[4] J. S. Respondek, *History of confluent Vandermonde matrices and inverting them algorithms*, arXiv 2024, https://arxiv.org/abs/2407.15696.

[5] W. Gautschi, *On inverses of Vandermonde and confluent Vandermonde matrices III*, Numerische Mathematik 29 (1978), 445–450, https://doi.org/10.1007/BF01432880 (abstract only inspected).
