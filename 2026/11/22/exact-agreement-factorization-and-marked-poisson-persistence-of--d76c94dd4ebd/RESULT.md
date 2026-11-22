# Exact agreement factorization and marked Poisson persistence of random best-response equilibria

## Finding

Let \(m,n\ge2\) be the two sizes of a rectangular action grid. In each of two versions \(t=0,1\), let \(I_j^{(t)}\in\{1,\ldots,m\}\) be the row chosen by the first side for column \(j\), and let \(J_i^{(t)}\in\{1,\ldots,n\}\) be the column chosen by the second side for row \(i\). A reciprocal best-response cell \((i,j)\) satisfies \(I_j^{(t)}=i\) and \(J_i^{(t)}=j\).

Suppose the paired choices \((I_j^{(0)},I_j^{(1)})\) are identically distributed, independent across columns, uniform in each margin, and invariant under simultaneous relabeling of their \(m\) choices. Suppose analogously that the paired choices \((J_i^{(0)},J_i^{(1)})\) are independent across rows, uniformly marginal, jointly permutation invariant on \(n\) choices, and independent of all first-side pairs. Write
\[
 a_m=\Pr(I_j^{(0)}=I_j^{(1)}),\qquad b_n=\Pr(J_i^{(0)}=J_i^{(1)}).
\]
If \(N^{(t)}\) is the total equilibrium count and \(C,U,V\) respectively count cells present in both versions, only version zero, or only version one, then **for every finite \(m,n\)**,
\[
 \mathbb E N^{(0)}=\mathbb E N^{(1)}=1,\quad
 \mathbb E C=a_m b_n,\quad
 \operatorname{Cov}(N^{(0)},N^{(1)})=(a_m-1/m)(b_n-1/n).
\]
Also \(\operatorname{Var}(N^{(t)})=(1-1/m)(1-1/n)\), so the exact correlation equals the product of the two chance-corrected best-response agreement coefficients:
\[
 \operatorname{Corr}(N^{(0)},N^{(1)})
 =\frac{a_m-1/m}{1-1/m}\,\frac{b_n-1/n}{1-1/n}.
\]
If both \(m,n\to\infty\) and \(a_m\to a\), \(b_n\to b\), then
\[
 (C,U,V)\ \xrightarrow{\mathrm d}\
 (P_{ab},P_{1-ab},P'_{1-ab}),
\]
with all three Poisson variables independent. Their cell locations, rescaled into the unit square, converge jointly to three independent homogeneous Poisson point processes of the corresponding intensities. No ratio assumption on \(m/n\) is needed.

**Independent payoff refresh specialization.** Let two independent payoff tables (one for each side) have independent entries, each table with its own continuous marginal distribution. A second version is produced by independently retaining each payoff coordinate with probability \(q_{m,n}\), and otherwise replacing that coordinate with a fresh independent sample from its own marginal distribution. The two tables and all retention coins are independent. For \(k\ge2\), define
\[
 p_k(q)=\sum_{j=0}^{k-1}\binom{k-1}{j}q^{k-1-j}(1-q)^j
 \left(\frac{q}{k+j}+\frac{2(1-q)}{k(k+j+1)}\right).
\]
Then \(a_m=m p_m(q_{m,n})\) and \(b_n=n p_n(q_{m,n})\) exactly. If \(q_{m,n}\to q\in[0,1]\), set \(h=q/(2-q)\) and \(s=h^2\). The three marked Poisson intensities become \(s,1-s,1-s\), and the equilibrium counts converge jointly to a bivariate Poisson pair
\[
 (N^{(0)},N^{(1)})\ \xrightarrow{\mathrm d}\ (P_s+P_{1-s},P_s+P'_{1-s}).
\]
Consequently,
\[
 \Pr(N^{(0)}=N^{(1)}=0)\longrightarrow e^{-2+s},\qquad
 \Pr(C\ge1)\longrightarrow1-e^{-s},\qquad
 \operatorname{Cov}(N^{(0)},N^{(1)})\longrightarrow s.
\]
For half retention, \(q=1/2\), the shared equilibrium intensity is \(1/9\), even though both marginal equilibrium intensities remain one.

## Assumptions and scope

All entries within each player's initial payoff table are independent and identically distributed with an atomless distribution; the two players' tables may have different atomless distributions. Fresh replacement entries have the same law as the corresponding original entries. The two large dimensions both diverge; rates may differ arbitrarily. No zero-sum, symmetric-payoff, potential-game, or common-payoff constraint is assumed. A reciprocal best-response cell is a pure strategy equilibrium in the independent-payoff two-player interpretation; the mathematical theorem is a statement about two coupled random bipartite choice maps. A Poisson point process means weak convergence of finite point measures on the compact unit square, with boundary limits interpreted in the usual weak topology.

## Proof

**1. Finite one-cell probabilities.** By label exchangeability, in a choice set of size \(k\),
\[
 \Pr(I^{(0)}=r,I^{(1)}=r)=a_k/k,
 \qquad \Pr(I^{(0)}=r,I^{(1)}=s)=\frac{1-a_k}{k(k-1)}\quad(r\ne s).
\]
The two marginals of every choice are uniform. Therefore any cell is an equilibrium in each fixed version with probability \(1/(mn)\); it is present in both with probability \((a_m/m)(b_n/n)\). Summing over the \(mn\) cells gives the finite means.

**2. Exact covariance by four cell geometries.** Expand \(\mathbb E[N^{(0)}N^{(1)}]\) by the positions of the two contributing cells. The same-cell contribution is \(a_m b_n\). Distinct cells with distinct rows and columns contribute \((m-1)(n-1)/(mn)\). Distinct cells in the same row contribute \((1-b_n)/m\), since different columns use independent first-side choices and the second-side choices in the two versions must differ. Distinct cells in the same column contribute \((1-a_m)/n\). Summing and subtracting \(\mathbb E N^{(0)}\mathbb E N^{(1)}=1\) gives the factorization. For one version, two equilibria cannot share a row or column; nonattacking cells have independent equilibrium events. Thus \(\mathbb E[N^{(t)}(N^{(t)}-1)]=(m-1)(n-1)/(mn)\), proving the variance and correlation identities.

**3. Three marked Poisson laws.** Each cell has exactly one of four statuses: common, zero-only, one-only, or absent. The probabilities of the first three statuses are \(a_m b_n/(mn)\), \((1-a_m b_n)/(mn)\), and the same latter value, respectively. For any fixed number \(r\) of distinct cells with all rows and columns different, their statuses are independent exactly: every relevant first-side column pair and second-side row pair is disjoint. Hence ordered tuples of distinct nonattacking cells contribute the expected products to every joint factorial moment. There are \((m)_r(n)_r\) such tuples.

For tuples with a repeated row or column, a nonzero joint status event requires distinct selected cells in any one row (or column) to be the best reply in different versions. Since each version has only one best reply, there are at most two selected cells in any given row or column. When two distinct indices are prescribed in the same choice pair, their joint probability is at most \(1/[k(k-1)]\); one prescribed index has probability at most \(1/k\). Independence of different choice groups thus bounds any nonzero \(r\)-cell joint event by \((1+O_r(1/m+1/n))/(mn)^r\). Among all \(O_r((mn)^r)\) ordered tuples, only \(O_r((mn)^r(1/m+1/n))\) have a repeated row or column, so their total contribution is \(O_r(1/m+1/n)\). All mixed factorial moments therefore converge to those of independent Poisson counts of means \(ab,1-ab,1-ab\), determining the joint law. Multiplying summands by continuous spatial test functions replaces nonattacking cell counts by Riemann sums and proves convergence of the three marked spatial point processes (equivalently, apply the same factorial-moment argument to disjoint spatial rectangles whose boundaries have zero Lebesgue measure).

**4. Retention probability and its limit.** Apply each continuous payoff distribution's probability integral transform; this preserves every relevant ordering. For one candidate \(X_1\) among \(k\) uniform values, the probability that it is maximal in both original and independently refreshed samples is \(p_k(q)\). Condition on whether its own entry was retained. Given a common candidate value \(u\), each competitor lies below it in both copies with probability \(qu+(1-q)u^2\). Given two independent candidate values \(x,y\), each competitor lies below both with probability \(q\min(x,y)+(1-q)xy\). Thus
\[
 p_k(q)=q\int_0^1[qu+(1-q)u^2]^{k-1}\,du
 +(1-q)\int_0^1\!\int_0^1[q\min(x,y)+(1-q)xy]^{k-1}\,dx\,dy.
\]
Split the square into the two triangles and integrate the smaller coordinate to obtain
\[
 p_k(q)=q\int_0^1u^{k-1}[q+(1-q)u]^{k-1}\,du
 +\frac{2(1-q)}k\int_0^1u^k[q+(1-q)u]^{k-1}\,du,
\]
which expands binomially into the stated finite sum. By exchangeability the common-argmax probability is \(k p_k(q)\). The double integral is at most \(2/[k(k+1)]\), since \(q\min(x,y)+(1-q)xy\le\min(x,y)\). For \(q_k\to q\), Laplace scaling \(u=1-z/k\) in the first integral, with derivative of \(qu+(1-q)u^2\) at one equal to \(2-q\), gives
\[
 k p_k(q_k)\longrightarrow\frac{q}{2-q}.
\]
The domination by \(u^{k-1}\) makes this valid also at \(q=0,1\). Substitute the limit in the general marked theorem. This finishes the proof.

## Verification

The accompanying `verify.py` runs 224 exact finite assertions using only Python's standard library. It checks the endpoint and rational finite-sum formulas; exhaustively enumerates rank orders and retention masks for sample sizes up to three; exhaustively enumerates the coupled best-response maps for rectangular sizes \(2\times2\) and \(2\times3\); and verifies the exact covariance, mean, and shared-equilibrium formulas in those cases. It also compares finite exact values with their limiting expressions. These finite checks are diagnostics and do not replace the analytic factorial-moment proof. Run from the containing directory with `python verify.py`.

## Relationship to prior work

Classical single-game Poisson-one equilibrium laws appear in Powers (1990), Stanford (1996), and in the discussion and Proposition 1 of Heinrich et al. (2023). They concern one game and cannot determine two-game overlap from marginal counts alone. Mimun, Quattropani and Scarsini (2022) consider payoff correlation **between two players inside one game**; their mean number of equilibria depends on that correlation, whereas each game here retains two independent players' payoff tables and exactly unit mean. Varsos, Flouris and Bitsaki (2023) consider additive payoff misinformation, principally in finite two-by-two games, rather than the coupled large-grid resampling model. The present object is a pair of coupled ordinal best-response maps, with an exact finite agreement factorization and three spatial rare-event populations.

## Limitations

No assertion is made for fixed one-sided dimension, discrete payoffs with ties, correlated payoff matrices of the two players, or additive-noise perturbations. The asymptotic statements require both action counts to diverge. No claim is made that all literature on paired random games has been exhaustively inspected; historical priority against unlocated general coupled-map Poisson theorems remains a risk. Independent mathematical audit has not been performed.

## References

- W. Stanford, *The Limit Distribution of Pure Strategy Nash Equilibria in Symmetric Bimatrix Games*, Mathematics of Operations Research 21 (1996), 726–733. https://doi.org/10.1287/moor.21.3.726 (public online 1996-08-01).
- H. A. Mimun, M. Quattropani and M. Scarsini, *Best-Response Dynamics in Two-Person Random Games with Correlated Payoffs*, arXiv:2209.12967, originally submitted 2022-09-26. https://arxiv.org/abs/2209.12967
- T. Heinrich et al., *Best-response dynamics, playing sequences, and convergence to equilibrium in random games*, International Journal of Game Theory 52 (2023), 703–735. https://doi.org/10.1007/s00182-023-00837-4
- C. Varsos, G. Flouris and M. Bitsaki, *Noisy Games: A Study on the Effect of Noise on Game Specifications*, arXiv:2307.01516 (2023). https://arxiv.org/abs/2307.01516
