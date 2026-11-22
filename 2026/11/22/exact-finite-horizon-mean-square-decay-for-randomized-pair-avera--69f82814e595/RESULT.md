# Exact finite-horizon mean-square decay for randomized pair averaging on stars

## Finding

Let \(m\ge3\) be an integer. On the \((m+1)\)-vertex star \(K_{1,m}\), independently at each discrete interaction select one of the \(m\) hub–leaf edges uniformly and replace the two endpoint values by their arithmetic mean. Write \(y_k=x_k-\bar x\mathbf1\) for the zero-mean disagreement, where \(\bar x\) is the mean of the initial values. Let \(h\) denote the unit hub-versus-leaf-mean vector and \(S\) the \((m-1)\)-dimensional space of leaf vectors summing to zero and vanishing at the hub. For every deterministic initial disagreement \(y_0=a h+v\), \(v\in S\), the **entire finite-horizon mean-square law** is

\[
\mathbb E\|y_k\|_2^2=q_k a^2+r_k\|v\|_2^2,
\qquad \binom{q_k}{r_k}=M_m^k\binom11,
\]

with the explicit rational matrix

\[
M_m=\begin{pmatrix}
\frac{(m-1)^2}{4m^2}&\frac{m^2-1}{4m^2}\\[2pt]
\frac{m+1}{4m^2}&1-\frac{3}{4m}-\frac1{4m^2}
\end{pmatrix}.
\]

For **every** finite integer \(k\ge1\), \(0<q_k<r_k\). Thus the unique worst-case initial subspace is the leaf-contrast space \(S\); no hub-versus-leaves input maximizes expected residual energy. Define

\[
\lambda_\pm(m)=\frac{5(m-1)\pm\sqrt{9m^2-2m-7}}{8m},
\qquad \nu_m=1-\frac1{2m}.
\]

Then the *sharp worst-case* mean-square contraction after \(k\) interactions is

\[
R_m(k)=\sup_{0\ne y_0\perp\mathbf1}
\frac{\mathbb E\|y_k\|_2^2}{\|y_0\|_2^2}
=r_k
=\frac{(\nu_m-\lambda_-)\lambda_+^k+(\lambda_+-\nu_m)\lambda_-^k}{\lambda_+-\lambda_-}.
\]

Here \(0<\lambda_-<\lambda_+<\nu_m<1\), and \(r_k\) is strictly log-concave in \(k\): \(r_k^2>r_{k-1}r_{k+1}\) for all \(k\ge1\). Hence the successive contraction ratios \(r_{k+1}/r_k\) decrease strictly to \(\lambda_+\), and \(r_k<\nu_m^k\) for \(k\ge2\). In particular, the exact exponential mean-square factor is \(\lambda_+\), not the standard one-step eigenvalue upper-bound factor \(\nu_m\), and

\[
\lambda_+=1-\frac{2}{3m}+O(m^{-2}),
\qquad \lim_{m\to\infty}\frac{-\log\lambda_+}{-\log\nu_m}=\frac43.
\]

The same formulas extend to \(m=2\), where \(\lambda_-=0\), \(\lambda_+=5/8\), and \(r_k=(6/5)(5/8)^k\) for all \(k\ge1\); this three-node rate was previously demonstrated in Yilin Mo's 2014 notes and is not claimed as a new base case.

## Assumptions and scope

The edges of the unweighted star are numbered \(\{0,i\}\) for \(1\le i\le m\), with hub \(0\). Choices are independent and uniform over edges at each interaction. Define the orthogonal pair-averaging projection

\[
W_i=I-\tfrac12(e_0-e_i)(e_0-e_i)^{\mathsf T}.
\]

The process is \(y_{k+1}=W_{I_{k+1}}y_k\), with uniform independent \(I_j\), and disagreement \(\mathbf1^{\mathsf T}y_0=0\). Time is **number of pair interactions**, not Poisson-clock wall time. The supremum in \(R_m(k)\) is over nonzero deterministic mean-zero real inputs. No assertions are made about almost-sure pathwise contraction, noisy observations, or joint scheduling of simultaneous pairs.

## Proof

**1. Orthogonal decomposition.** Let

\[
h=\frac{(m,-1,\ldots,-1)^{\mathsf T}}{\sqrt{m(m+1)}},\quad
H=hh^{\mathsf T},\quad J=\frac{\mathbf1\mathbf1^{\mathsf T}}{m+1},\quad P_S=I-J-H.
\]

Then \(\mathbb R^{m+1}=\operatorname{span}(\mathbf1)\oplus\operatorname{span}(h)\oplus S\). The leaf permutation group preserves the law of every update. An invariant real symmetric matrix has constant hub–leaf entries and constant diagonal and off-diagonal entries within the leaves; restricting it to the zero-sum subspace therefore gives one scalar eigenvalue along \(h\) and one on \(S\), without a mixed term. Consequently, the quadratic form \(y_0\mapsto\mathbb E\|y_k\|_2^2\) is invariant under all leaf permutations, so it has one coefficient on \(h\) and one on \(S\), with zero mixed term. This proves the asserted two-coefficient form once the recurrence is established.

**2. Exact covariance dynamics.** Fix any edge \(i\) and set \(\alpha=(m-1)/(2m)\), \(c^2=(m^2-1)/(4m^2)\). The projection identity \(W_i^2=W_i\) and the direct calculation

\[
\langle h,W_i h\rangle=\alpha,\qquad
\|P_SW_i h\|_2^2=\alpha-\alpha^2=c^2
\]

show that the linear covariance operator \(\mathcal T(X)=m^{-1}\sum_iW_i XW_i\) maps the two invariant covariance projectors as follows:

\[
\mathcal T(H)=\alpha^2H+\frac{c^2}{m-1}P_S,
\quad
\mathcal T(P_S)=c^2H+dP_S,
\quad d=1-\frac3{4m}-\frac1{4m^2}.
\]

For the last coefficient, use \(\operatorname{tr}(W_iP_SW_i)=\operatorname{tr}(W_iP_S)=m-1-\alpha\), then subtract its \(h\)-component \(c^2\) and divide by \(m-1\). Thus the coefficient vector of a leaf-permutation-invariant covariance evolves by \(M_m\), with the displayed entries. The expected energy for a unit initial \(h\) or any unit initial \(v\in S\) is obtained by duality from \(\mathcal T^k(I-J)\); the dual coefficient recurrence is precisely \((q_{k+1},r_{k+1})^{\mathsf T}=M_m(q_k,r_k)^{\mathsf T}\) with \(q_0=r_0=1\). This remains valid for nonsymmetric initial rank-one covariances because the observable energy is leaf-permutation invariant.

**3. Strict finite-horizon maximizing subspace.** Set \(\Delta_k=r_k-q_k\). Direct substitution in the recurrence gives

\[
\Delta_{k+1}=\tfrac12q_k+\frac{3(m-1)}{4m}\Delta_k.
\]

Since \(q_0=1\), \(\Delta_0=0\), and \(M_m\) has strictly positive entries, \(q_k>0\) and \(\Delta_k>0\) for every \(k\ge1\). Thus exactly the unit vectors in \(S\) maximize the finite-horizon expected squared error.

**4. Exact rates and strict improvement.** Direct calculation gives

\[
\operatorname{tr}M_m=\frac{5(m-1)}{4m},\qquad
\det M_m=\frac{(m-2)(m-1)}{4m^2},
\]

and the discriminant gives the stated \(\lambda_\pm\). For \(m\ge3\), both eigenvalues are strictly positive and distinct. One-step contraction on \(S\) gives \(r_1=\nu_m\). Moreover,

\[
\nu_m^2-(\operatorname{tr}M_m)\nu_m+\det M_m=\frac{m+1}{8m^2}>0,
\quad
\nu_m-\tfrac12\operatorname{tr}M_m=\frac{3m+1}{8m}>0,
\]

so \(\nu_m>\lambda_+\). Solving the scalar characteristic recurrence with \(r_0=1\), \(r_1=\nu_m\) produces the displayed expression for \(r_k\). Its coefficient of \(\lambda_+^k\) exceeds one, while that of \(\lambda_-^k\) is strictly negative. Hence

\[
r_k^2-r_{k-1}r_{k+1}=
\frac{(\nu_m-\lambda_-)(\nu_m-\lambda_+)}{(\lambda_+-\lambda_-)^2}
(\lambda_+-\lambda_-)^2(\lambda_+\lambda_-)^{k-1}>0.
\]

In particular the ratios \(r_{k+1}/r_k\) strictly decrease from \(r_1/r_0=\nu_m\), giving \(r_k<\nu_m^k\) for all \(k\ge2\), while the positive dominant coefficient yields \(\lim_{k\to\infty}r_k^{1/k}=\lambda_+\). Every nonzero initial disagreement has the same exponential factor because the strictly positive covariance recurrence has a positive Perron eigenvector and \(q_k,r_k\) both have nonzero dominant coefficients.

**5. Large-star boundary.** Expanding the radical in \(\lambda_+\) as \(m\to\infty\) gives \(1-2/(3m)+O(m^{-2})\). Since \(\nu_m=1-1/(2m)\), the logarithmic gap ratio tends to \(4/3\). No interchange of a finite-size numerical calculation with an infinite limit is used.

## Verification

Run the accompanying self-contained Python program `verify_star_gossip.py` with standard-library Python 3. It builds the exact rational averaging matrices on star graphs with \(2\le m\le11\), separately evolves full covariance matrices for up to six interactions, compares both invariant projectors entry by entry against the derived matrix, and checks the finite-horizon inequalities and characteristic coefficients. The program reports 2,060 exact rational assertions passed. These finite checks separately test the implementation; all universal claims follow from the proof above.

## Relationship to prior work

Boyd, Ghosh, Prabhakar and Shah introduced the randomized pairwise gossip model, obtained the expected-averaging spectral-rate bound and set up the general lifted second-moment covariance criterion. The sharp finite-horizon and all-size star formulas here are an evaluation **beyond**, not a replacement for, that general framework. The 2004 conference paper and 2006 journal version are both acknowledged.

Yilin Mo's 2014 notes explicitly calculate the true \(5/8\) mean-square exponential factor for the three-vertex path, which is the \(m=2\) member here. Accordingly the three-node example is prior art; the present family result focuses on \(m\ge3\), the exact finite-horizon extremal subspace, strict log-concavity, and the \(4/3\) asymptotic separation from the standard one-step rate bound. Sirocchi and Bogliolo (2022) study topological predictors of gossip performance via spectral bounds and network experiments rather than this closed-form star covariance law.

## Limitations

The theorem is specific to independently and uniformly chosen star edges, arithmetic (half-half) pair averaging, real initial data, and squared Euclidean disagreement. It is not a guarantee for other probability laws, overlapping simultaneous contacts, pathwise error, physical-clock latency, or gossip with noise. The analysis gives precise expected squared-error decay, not a new generic convergence theorem. Published or unindexed equivalent all-size calculations may exist and should be checked before external priority claims.

## References

1. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, 43rd IEEE CDC (2004), DOI: 10.1109/CDC.2004.1429652. https://web.stanford.edu/~boyd/papers/pdf/gossip_opt.pdf
2. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory **52** (2006), 2508–2530, DOI: 10.1109/TIT.2006.874516. https://web.stanford.edu/~balaji/papers/06randomizedgossip.pdf
3. Y. Mo, *Gossip Algorithm*, lecture notes dated 2014-10-29, https://murray.cds.caltech.edu/images/murray.cds/1/13/Cds27010.pdf
4. C. Sirocchi, A. Bogliolo, *Topological network features determine convergence rate of distributed average algorithms*, Scientific Reports **12** (2022), article 21831, DOI: 10.1038/s41598-022-25974-w. https://www.nature.com/articles/s41598-022-25974-w
