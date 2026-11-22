# A sharp all-dimension mean-square Euler stability law for a nonnormal Jordan chain

## Finding

For each integer \(m\ge2\), define \(n=m-1\), the \(m\times m\) shift \(N_m\) by \((N_m)_{i,i+1}=1\) with every other entry zero, and \(e_i\) as the \(i\)th Euclidean coordinate vector. Set
\[
A=-I_m+\kappa N_m,\quad B=\sigma e_m e_1^{\mathsf T},\quad
P_n(z)=\sum_{j=0}^n\binom{n}{j}^2 z^j,\quad
G=\sigma^2\kappa^{2n},
\]
where \(\kappa,\sigma>0\). The Euler–Maruyama recursion for \(dX=AX\,dt+BX\,dW\), with independent increments of mean zero and variance \(h\), is asymptotically mean-square stable for every deterministic initial condition **if and only if**
\[
\boxed{0<h<2\quad\text{and}\quad G P_n((1-h)^2)<(2-h)^{2n+1}.}
\]
Equivalently, with \(R_n(h)=(2-h)^{2n+1}/P_n((1-h)^2)\), stability holds exactly when \(G<R_n(h)\). For each fixed \(n\ge1\), this ratio is **strictly decreasing** on \((0,2)\), with
\[
\lim_{h\downarrow0}R_n(h)=G_{c,n}=\frac{2^{2n+1}}{\binom{2n}{n}},\qquad
\lim_{h\uparrow2}R_n(h)=0.
\]
If \(G<G_{c,n}\), there is exactly one \(h_*\in(0,2)\) satisfying \(G=R_n(h_*)\), and the *complete* positive stability interval is \(0<h<h_*\). If \(G\ge G_{c,n}\), no positive step is asymptotically mean-square stable. This includes equality: the critical step is not asymptotically decaying. The continuous Itô SDE itself has mean-square asymptotic stability **if and only if** \(G<G_{c,n}\).

## Assumptions and scope

The Wiener increments are independent, centered, and have variance \(h\); no other distributional moment is needed for covariance stability. The initial state is deterministic and the assertion quantifies over **every** initial state. The chain length \(m\) is any finite integer at least two, while \(\kappa\) and \(\sigma\) are strictly positive. Mean-square stability means \(\lim_{k\to\infty}\mathbb E\|X_k\|_2^2=0\) for every deterministic \(X_0\). The only numerical method considered is unmodified, fixed-step explicit Euler–Maruyama.

## Proof

**1. A positive rank-one covariance feedback.** Set \(T=(1-h)I_m+\kappa h N_m\), \(E=e_me_m^{\mathsf T}\), and \(\beta=h\sigma^2\). Independence and centering give the exact covariance update
\[
\Phi_h(C)=TCT^{\mathsf T}+\beta C_{11}E.
\]
For \(0<h<2\), \(a=1-h\) satisfies \(|a|<1\), hence the unforced covariance map \(\Phi_0(C)=TCT^{\mathsf T}\) has spectral radius \(a^2<1\). For each real \(r>a^2\), define
\[
V_r=\sum_{k=0}^\infty r^{-k-1}T^k E(T^{\mathsf T})^k,\quad
f(r)=\beta(V_r)_{11}.
\]
The matrix \(V_r\) is nonzero and positive semidefinite and \((rI-\Phi_0)V_r=E\). The function \(f\) is strictly decreasing from infinity at \(r\downarrow a^2\) to zero at infinity. Indeed its terms are nonnegative and its impulse coefficient below is nonzero for infinitely many \(k\) if \(a\ne0\), while for \(a=0\) its finite nonzero impulse creates a pole at zero. Thus there is a unique \(r_*>a^2\) with \(f(r_*)=1\). At that value \(\Phi_h(V_{r_*})=r_*V_{r_*}\). Conversely, a spectral-radius eigenmatrix of the positive covariance map may be taken positive semidefinite (finite-dimensional Perron theory for a proper cone); if its eigenvalue \(s>a^2\), its resolvent identity forces \(f(s)=1\). So \(r_*\) is precisely the covariance spectral radius. It follows that \(\rho(\Phi_h)<1\) exactly when \(f(1)<1\), and that equality and reverse inequality are not asymptotically stable for all deterministic inputs (positive semidefinite eigenmatrices are sums of rank-one input covariances).

**2. Evaluate the return loop.** With \(n=m-1\), the binomial theorem for the nilpotent shift gives, for \(k\ge n\),
\[
 e_1^{\mathsf T}T^k e_m=\binom{k}{n}(1-h)^{k-n}(\kappa h)^n,
\]
where the entry vanishes for \(k<n\). Thus, putting \(z=(1-h)^2\),
\[
 f(1)=h\sigma^2(\kappa h)^{2n}\sum_{j\ge0}\binom{n+j}{n}^2z^j.
\]
The elementary binomial-square generating-function identity (obtainable by the Euler transformation of the terminating binomial hypergeometric series, or by comparing coefficients) reads
\[
 \sum_{j\ge0}\binom{n+j}{n}^2z^j
 =\frac{P_n(z)}{(1-z)^{2n+1}},\quad |z|<1.
\]
Since \(1-z=h(2-h)\), cancellation of all powers of \(h\) gives \(f(1)=G P_n((1-h)^2)/(2-h)^{2n+1}\). For \(h\ge2\), the deterministic mean \(\mathbb EX_k=T^kX_0\) is not asymptotically stable for all \(X_0\), hence mean-square stability is impossible by Jensen's inequality.

**3. Strictly one stability interval.** Write \(r=1-h\), so that \(R_n(h)=(1+r)^{2n+1}/P_n(r^2)\). For \(-1<r\le0\), its numerator strictly increases in \(r\) and its denominator weakly decreases, proving strict increase. For \(0<r<1\), put \(p=r/(1+r)\) and
\[
 C_n(p)=\frac{P_n(r^2)}{(1+r)^{2n}}=\mathbb P(U=V),\quad U,V\overset{\mathrm{iid}}{\sim}\operatorname{Bin}(n,p).
\]
Fourier inversion yields
\[
 C_n(p)=\frac1{2\pi}\int_{-\pi}^\pi
 \big(1-4p(1-p)\sin^2(\theta/2)\big)^n\,d\theta.
\]
For \(n\ge1\), \(C_n(p)\) strictly decreases as \(p\) increases from zero to one half. Consequently \(R_n=(1+r)/C_n(p)\) strictly increases with \(r\), or strictly decreases with \(h\), also in \(0<h<1\). The central Vandermonde identity \(P_n(1)=\binom{2n}{n}\) gives the stated endpoint limits. Continuity and strictness establish existence and uniqueness of \(h_*\) and preclude any reentry.

**4. Exact continuous-time boundary.** The rank-one covariance feedback applies as well to the continuous generator. Its return-loop integral is
\[
\sigma^2\int_0^\infty\big|e_1^{\mathsf T}e^{tA}e_m\big|^2dt
=\sigma^2\kappa^{2n}\frac{1}{(n!)^2}\int_0^\infty e^{-2t}t^{2n}dt
=G\frac{\binom{2n}{n}}{2^{2n+1}}.
\]
The same strictly positive resolvent feedback criterion gives continuous-time mean-square stability precisely when this gain is less than one. This proves the theorem.

## Verification

The attached standalone `verification_jordan.py` independently checks the finite coefficient identities through order 19 for eight chain indices, compares 30 rational return-loop calculations to matrix powers, compares 45 Kronecker covariance spectral-radius decisions, and checks nine central binomial limits. Run `python verification_jordan.py` with Python, SymPy and NumPy. Its captured output is in `verification_jordan_output.txt`. These finite checks are not used as substitutes for the preceding all-dimension proof.

An explicit example is \(m=3\), \(\kappa=1\), \(\sigma^2=2\), where \(G=2<16/3\), so the continuous SDE is mean-square stable. Yet the Euler step \(h=1\) violates \(2P_2(0)<1\) and is mean-square unstable, while \(h=1/2\) satisfies \(2P_2(1/4)<(3/2)^5\) and is stable. The Euler **mean** decays at both steps.

## Relationship to prior work

The open full text of Senosiain and Tocino (2023) analyzes mean-square stability for nonnormal diffusion test systems in two and three dimensions, including lateral noise and a three-coordinate model with three separate noises; its stated theorems are for continuous-time systems, not the all-dimension Euler–Maruyama Jordan chain with one closing feedback noise considered here. Earlier Buckwar–Kelly work addresses \(\theta\)-Maruyama linear stability for nonnormal drift, and may cover the two-dimensional member; no claim of originality for the isolated two-dimensional case is made. The independent claim is the uniform **every-chain-length** closed polynomial step condition and strict all-length no-reentry law, with the exact continuous/discrete boundary match. Finite-dimensional rank-one feedback theory and binomial identities are known tools; neither alone states this all-length family result. Historical priority requires independent scrutiny, particularly against the 2012 Buckwar–Kelly article, whose full text was unavailable during this comparison.

## Limitations

The theorem is restricted to one very specific nilpotent-chain drift and one rank-one multiplicative noise direction. It does not assert stability for other feedback positions, general nonnormal matrices, adaptive steps, or nonlinear SDEs. Equality at either critical boundary is not asymptotic mean-square decay. The analytic result establishes a new candidate statement relative to inspected material, not an independently certified literature-priority finding.

## References

1. M. J. Senosiain and A. Tocino, “A survey of mean-square destabilization of multidimensional linear stochastic differential systems with non-normal drift,” *Numerical Algorithms* 93 (2023), 1543–1559, DOI: 10.1007/s11075-022-01478-6 (first public date 2023-01-09; open full text).
2. E. Buckwar and C. Kelly, “Non-normal drift structures and linear stability analysis of numerical methods for systems of stochastic differential equations,” *Computers & Mathematics with Applications* 64 (2012), 2282–2293, DOI: 10.1016/j.camwa.2012.02.059 (bibliographic record and abstract inspected, full text not obtained).
3. E. Buckwar and C. Kelly, “Towards a systematic linear stability analysis of numerical methods for systems of stochastic differential equations,” *SIAM Journal on Numerical Analysis* 48 (2010), 298–321, DOI: 10.1137/090771843 (abstract inspected).
4. E. Buckwar and R. D'Ambrosio, “Exponential mean-square stability properties of stochastic linear multistep methods,” *Advances in Computational Mathematics* 47 (2021), article 55, DOI: 10.1007/s10444-021-09879-2 (online abstract inspected).
