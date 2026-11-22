# Five-component onset of positive spectator covariance in fluctuating complex assembly

## Finding

For each integer \(m\in\{2,3,4,5\}\), consider \(m\) independently loaded species with counts \(N_i\sim\operatorname{Pois}(\lambda)\), \(\lambda>0\), and instantaneous maximal assembly of one complex using one particle of every species. Let \(M=\min_{1\le i\le m}N_i\) be the number of complexes and \(U_i=N_i-M\) the unreacted count of species \(i\). Then the covariance between any two distinct unreacted species has the exact expression below, is negative at sufficiently small loading, and has the high-loading limit

\[
\lim_{\lambda\to\infty}\frac{\operatorname{Cov}(U_1,U_2)}{\lambda}
=c_m:=\operatorname{Var}\left(\min_{1\le i\le m}Z_i\right)-\frac{2}{m},
\]

where the \(Z_i\) are independent standard normals. The signs are \(c_2<0\), \(c_3<0\), \(c_4<0\), and \(c_5>0\), and certified numerical enclosures are respectively \((-0.318310,-0.318309)\), \((-0.107200,-0.107198)\), \((-0.008286,-0.008283)\), and \((0.047533,0.047536)\). Thus five is the smallest component number *among the complete classification \(2\le m\le5\)* with positive large-loading spectator pair covariance. In particular five-component assembly has a genuine negative-to-positive covariance change as its mean species loading increases.

## Assumptions and scope

The initial counts are mutually independent and identically Poisson at the *same* mean, without fixed-total conditioning. Each complex consumes exactly one of every species, with no kinetic or spatial constraints, and assembly proceeds to the realization-wise maximum. No diffusion, chemical rate law, compartment exchange, or post-assembly stochastic dynamics is assumed. The observable is the covariance between two different surviving *unbound* species, not the variance of the product count, nor the covariance of the initial counts. The asymptotics fix \(m\) before taking either \(\lambda\downarrow0\) or \(\lambda\to\infty\).

## Proof

**Exact identity.** Write \(p_k=e^{-\lambda}\lambda^k/k!\) and \(Q_k=\Pr(N_1\ge k)\), with \(Q_0=1\). The tail-sum formula for the minimum gives

\[
 a_m:=\mathbb E M=\sum_{k\ge1}Q_k^m,\qquad
 b_m:=\mathbb E M^2=\sum_{k\ge1}(2k-1)Q_k^m.
\]

Since independent Poisson counts satisfy \(\mathbb E[N_1f(N_1,\ldots)]=\lambda\mathbb E[f(N_1+1,\ldots)]\), applying this to \(f=M\) gives

\[
\operatorname{Cov}(N_1,M)=\lambda\Pr\{N_1<\min_{j\ne1}N_j\}
=\lambda\sum_{k\ge0}p_k Q_{k+1}^{m-1}.
\]

Here the strict inequality is essential: increasing \(N_1\) by one changes the minimum precisely when its former value is smaller than *each* other count, with no ties. Expanding \(\operatorname{Cov}(N_1-M,N_2-M)\), using \(\operatorname{Cov}(N_1,N_2)=0\) and exchangeability, yields the exact absolutely convergent formula

\[
\boxed{C_m(\lambda)=b_m-a_m^2-2\lambda\sum_{k\ge0}p_kQ_{k+1}^{m-1}.}
\]

All sums converge because the Poisson distribution has finite moments; the tail-sum series are bounded by the first two Poisson moments.

**Low loading.** As \(\lambda\downarrow0\), \(\Pr(M\ge1)=(1-e^{-\lambda})^m=\lambda^m+O_m(\lambda^{m+1})\). The probability \(\Pr(M\ge2)\) is \(O_m(\lambda^{2m})\), so \(\operatorname{Var}(M)=\lambda^m+O_m(\lambda^{m+1})\). The unique-minimum event is led by \(N_1=0\) and \(N_j\ge1\) for all other species, giving \(\Pr(N_1<\min_{j\ne1}N_j)=\lambda^{m-1}+O_m(\lambda^m)\). Therefore

\[
\boxed{C_m(\lambda)=-\lambda^m+O_m(\lambda^{m+1}).}
\]

**High loading.** With \(Y_i^{(\lambda)}=(N_i-\lambda)/\sqrt\lambda\), the multivariate central limit theorem and continuity of the coordinate minimum yield \((M-\lambda)/\sqrt\lambda\Rightarrow Z_{(1)}=\min_iZ_i\). For \(\lambda\ge1\), the fourth moments of \(Y_i^{(\lambda)}\) equal \(3+1/\lambda\), and \(|(M-\lambda)/\sqrt\lambda|^4\le\sum_i|Y_i^{(\lambda)}|^4\); hence the minimum's first two moments converge. Consequently \(\operatorname{Var}(M)/\lambda\to\operatorname{Var}(Z_{(1)})\). The probability that \(N_1\) is the unique minimum tends to \(1/m\): Gaussian minima are a.s. unique and the asymptotic Gaussian vector is exchangeable. The exact identity now gives the claimed \(c_m\).

**Gaussian sign calculation.** Let \(\varphi\) and \(Q=1-\Phi\) denote the standard Gaussian density and upper tail. Integration by parts gives, for \(m\ge2\),

\[
\begin{aligned}
 \mu_m:=\mathbb EZ_{(1)}&=-m(m-1)\int_{\mathbb R}\varphi(x)^2Q(x)^{m-2}\,dx,\\
 \nu_m:=\mathbb EZ_{(1)}^2&=1+\tfrac12m(m-1)(m-2)\int_{\mathbb R}\varphi(x)^3Q(x)^{m-3}\,dx
\end{aligned}
\]

(the second integral term is zero at \(m=2\)). Normalize \(\varphi^2\) and \(\varphi^3\) to Gaussian densities of variances \(1/2\) and \(1/3\). The remaining upper-tail powers are orthant probabilities for equicorrelated centered Gaussians, with correlations \(1/3\) and \(1/4\), respectively. Their dimensions are at most three and two, so the exact probabilities are

\[
 P_0(\rho)=1,\quad P_1(\rho)=\tfrac12,\quad
 P_2(\rho)=\tfrac14+\frac{\arcsin\rho}{2\pi},\quad
 P_3(\rho)=\tfrac18+\frac{3\arcsin\rho}{4\pi}.
\]

Thus, with \(A_m=P_{m-2}(1/3)\), \(B_m=P_{m-3}(1/4)\),

\[
 \mu_m=-\frac{m(m-1)}{2\sqrt\pi}A_m,\qquad
 \nu_m=1+\frac{m(m-1)(m-2)}{4\pi\sqrt3}B_m
\]

for \(m\ge3\), with \(\nu_2=1\). Therefore \(c_m=\nu_m-\mu_m^2-2/m\). The standalone `verify.py` bounds the required \(\pi\), square roots and arcsines using exact rational intervals and checks strictly \(c_2,c_3,c_4<0<c_5\). Since \(\lambda\mapsto C_5(\lambda)\) is continuous on \((0,\infty)\) (uniform convergence of Poisson-moment sums on compact loading intervals), its opposite signs at sufficiently small and large loading imply at least one positive zero.

## Verification

Run `python3 verify.py` with Python 3's standard library. It uses Machin's identity and alternating arctangent bounds for \(\pi\), positive-coefficient arcsine series with explicit geometric remainder bounds, and squared rational bounds for \(\sqrt\pi\) and \(\sqrt3\). All four signs are established using exact rational interval arithmetic, not floating-point threshold guesses. The exact Poisson identity and asymptotic arguments above are analytic; the script checks the delicate sign constants rather than substituting finite enumeration for infinite proof.

## Relationship to prior work

Rubinovich and Polak (2026) introduce matching frustration, independent-Poisson loading, spectator leftovers, and the multicomponent capacity \(M=\min_iN_i\). In their manuscript and integrated supplemental section K, the multicomponent discussion treats mean deficit and fusion monotonicity, not the covariance of two residual species or the high-loading four-to-five sign reversal. Gaussian order-statistic moments are classical; the evaluated orthant integrals here are tools for the new assembly covariance statement, not claimed as original methods. Prior two-Poisson-extreme results cover only two input counts and do not establish the multicomponent residual covariance sign classification.

## Limitations

The result does **not** establish negativity for every loading in the two-, three-, or four-component cases; only the low-loading and high-loading signs are proved. It also does not establish uniqueness or location of the five-component crossing, nor behavior at arbitrary larger numbers of species. The model is an instantaneous capacity calculation without reaction kinetics, interactions, spatial heterogeneity or conditioning on a fixed total population. Literature coverage is qualified by incomplete full-text access to some general Gaussian order-statistics papers and unavailable full text for two related indexed Poisson-extrema records. Independent scientific validation has not been performed.

## References

1. L. Rubinovich and M. Polak, *Intrinsic Matching Frustration in Fluctuating Finite Systems*, arXiv:2607.03549, first posted July 3, 2026; especially supplemental section K, equations (S82)–(S88). https://arxiv.org/abs/2607.03549
2. *Accurate approximation of the expected value, standard deviation, and probability density function of extreme order statistics from Gaussian samples*, Communications in Statistics - Simulation and Computation (2022), DOI:10.1080/03610918.2022.2034865. https://doi.org/10.1080/03610918.2022.2034865
