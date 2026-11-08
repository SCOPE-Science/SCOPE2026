# Exact three-step zero-digit correlations and a Gaussian law at a golden-map plateau endpoint

## Finding

Put \(\beta=(1+\sqrt5)/2\) and \(\alpha_\star=1+\beta^{-2}\). Let \(T\) be the skewed symmetric golden map at \(\alpha_\star\), let \(\mu\) be its absolutely continuous invariant probability, and set \(Y_j(x)=\mathbf1_{[-\beta^{-1},\beta^{-1}]}(T^j x)\). Under \(x\sim\mu\), define \(C(n)=\operatorname{Cov}(Y_0,Y_n)\) for integers \(n\ge0\). Then

\[
\begin{aligned}
\mathbb E_\mu Y_0&=\tfrac34,\\
C(0)&=\tfrac3{16},\\
C(3k+1)&=-\tfrac1{16}\beta^{-6k},\\
C(3k+2)&=\tfrac{4\sqrt5-9}{16}\beta^{-6k},\\
C(3k+3)&=\tfrac{27-12\sqrt5}{16}\beta^{-6k}
\quad(k\ge0).
\end{aligned}
\]

In particular \(C(n+3)=\beta^{-6}C(n)\) for all \(n\ge1\), and the absolutely convergent bilateral Green–Kubo covariance sum is
\[
\sigma^2=C(0)+2\sum_{n=1}^\infty C(n)=\frac{\sqrt5}{32}>0.
\]
Writing \(Z_N=\sum_{j=0}^{N-1}Y_j\), both for initial \(x\sim\mu\) and for normalized Lebesgue measure on \([-1,1]\),
\[
\frac{Z_N-3N/4}{\sqrt N}\ \Longrightarrow\ \mathcal N\left(0,\frac{\sqrt5}{32}\right).
\]
Under the stationary measure, \(\lim_{N\to\infty}N^{-1}\operatorname{Var}(Z_N)=\sqrt5/32\).

## Assumptions and scope

The map, defined on \([-1,1]\), has three increasing affine branches
\[
T(x)=\begin{cases}
\beta^2x+\beta\alpha_\star,&-1\le x<-\beta^{-1},\\
\beta x,&-\beta^{-1}\le x\le\beta^{-1},\\
\beta^2x-\beta\alpha_\star,&\beta^{-1}<x\le1.
\end{cases}
\]
The zero digit occurs exactly on the middle branch. Dajani and Sanderson establish existence and uniqueness of the absolutely continuous invariant probability and show that \(\alpha_\star\) is the right endpoint of the full maximal \(3/4\)-frequency plateau. We use only the single endpoint parameter, not its neighboring parameters. Endpoint conventions have no effect under the continuous distributions considered here.

## Proof

**Seven-cell Markov partition.** Let \(e_0,\ldots,e_7\) be, in order,
\[
-1,\;-\beta^{-1},\;-\beta^{-2},\;-\beta^{-3},\;\beta^{-3},\;\beta^{-2},\;\beta^{-1},\;1.
\]
For \(0\le i\le6\), let \(I_i=(e_i,e_{i+1})\). Direct substitution, using \(\beta^2=\beta+1\), shows that the open images of these cells are the unions of the cells with indices
\[
\begin{array}{c|c}
i &\{j:T(I_i)\supset I_j\}\\\hline
0&\{2,3,4,5\}\\
1&\{0\}\\
2&\{1\}\\
3&\{2,3,4\}\\
4&\{5\}\\
5&\{6\}\\
6&\{1,2,3,4\}
\end{array}
\]
(the image equalities are meant up to endpoints). The respective branch slopes are \(\beta^2,\beta,\beta,\beta,\beta,\beta,\beta^2\). Thus the probability of moving from \(I_i\) to a covered \(I_j\), conditional on being uniform inside \(I_i\), is \(|I_j|/|T(I_i)|\). Because every nonempty itinerary cylinder maps affinely **onto its entire terminal cell**, conditional uniformity is preserved given the full symbolic past. In particular, the seven-cell itinerary for normalized Lebesgue starts as an exact, finite-state Markov chain. Its unique stationary distribution gives a step-function invariant density, equal to \(\mu\) by the source's uniqueness theorem.

**Symmetry and four-state reduction.** Reflection \(x\mapsto-x\) interchanges cells \(I_i\) and \(I_{6-i}\). The seven-cell transition matrix is strongly lumpable into states \(A=I_0\cup I_6\), \(B=I_1\cup I_5\), \(C=I_2\cup I_4\), and \(D=I_3\). Its exact row-stochastic matrix and invariant row vector are
\[
Q=\begin{pmatrix}
0&\sqrt5-2&7-3\sqrt5&2\sqrt5-4\\
1&0&0&0\\
0&1&0&0\\
0&0&(3-\sqrt5)/2&(\sqrt5-1)/2
\end{pmatrix},\qquad
\pi=\tfrac14\bigl(1,1,3-\sqrt5,\sqrt5-1\bigr).
\]
All entries are nonnegative, \(\pi Q=\pi\), and the directed graph is irreducible and aperiodic (state \(D\) has a positive self-loop). The zero-digit indicator on these states is \(r=(0,1,1,1)^{\mathsf T}\). Hence \(\pi r=3/4\).

**Spectral covariance.** Set \(f=r-\frac34\mathbf1\). Direct multiplication gives
\[
\begin{aligned}
C(n)&=\pi\,\operatorname{diag}(f)Q^nf,\\
C(0)&=\tfrac3{16},\quad C(1)=-\tfrac1{16},\\
C(2)&=\tfrac{4\sqrt5-9}{16},\quad
C(3)=\tfrac{27-12\sqrt5}{16}.
\end{aligned}
\]
The characteristic polynomial is
\[
\det(tI-Q)=t(t-1)(t^2+\beta^{-2}t+\beta^{-4}).
\]
Its four roots are distinct. On the mean-zero subspace, the eigenvalues are zero and \(\beta^{-2}e^{\pm2\pi i/3}\). Because \(Q^n\) kills the zero eigenspace for \(n\ge1\), its nonstationary component obeys \(Q^{n+3}=\beta^{-6}Q^n\) after projection onto mean-zero observables for every \(n\ge1\). The displayed covariances therefore satisfy the full three-step recurrence. Summation of the three geometric residue classes gives
\[
\frac3{16}+\frac{2[-1+(4\sqrt5-9)+(27-12\sqrt5)]}{16(1-\beta^{-6})}
=\frac{\sqrt5}{32}.
\]

**Gaussian limit and initialization.** For a finite irreducible aperiodic Markov chain, the centered additive functional \(\sum_{j=0}^{N-1}f(X_j)\) admits the usual bounded Poisson-equation martingale decomposition. Explicitly, writing \(g=(I-Q+\mathbf1\pi)^{-1}f\), the differences \(g(X_{j+1})-(Qg)(X_j)\) are bounded martingale differences, and the telescoping remainder is bounded. The ergodic theorem for conditional variances gives the martingale central limit theorem; the limiting variance is the above Green–Kubo sum. This argument applies with stationary initial law \(\pi\) and with any initial distribution on the finite states, in particular the cell-length distribution of normalized Lebesgue on \([-1,1]\). Since the initial-law bias in mean counts is bounded, centering by \(3N/4\) remains valid. The covariance summability also gives the stationary variance-per-observation limit.

## Verification

The included `check_golden_covariance.py` uses exact algebraic arithmetic to reconstruct every branch image and all seven transition rows, checks strong lumpability and stationary probabilities, independently computes the characteristic polynomial, first four lag covariances, the three-step recurrence at twelve additional lags, and the Green–Kubo variance by both geometric summation and matrix resolvent. Execute with `python check_golden_covariance.py` using SymPy. These finite computations are checks on the exact identities; the matrix derivation and general spectral argument establish the statements for all time lags.

## Relationship to prior work

Dajani and Sanderson, *Ergodic properties of a parameterised family of symmetric golden maps: the matching phenomenon revisited* (first public preprint January 20, 2023), Theorems 1.1–1.2 and §3, introduce the family, prove existence of the unique absolutely continuous invariant probability, and determine the maximal zero-digit frequency plateau. The paper also notes the relevant boundary parameter possesses a finite Markov partition for the related map and supplies general step-density machinery. Those facts are prior work, not claimed as new. The present result computes the **complete zero-digit autocovariance sequence**, its nontrivial three-step oscillatory decay, the exact asymptotic variance, and a concrete Gaussian fluctuation law for the specified boundary map. The finite-state Markov-chain central limit theorem is classical; it is not claimed as new by itself.

## Limitations

Only the single endpoint \(\alpha_\star\) and zero-digit observable are treated. Nothing here establishes the variance profile along the whole plateau or for other parameters. The result makes no assertion about atypical starting points, exact endpoint itineraries, or an independent mathematical audit. The explicit laws may overlap with unindexed work not found in the searches; the later journal version of the initiating paper was not independently inspected in full.

## References

1. K. Dajani and S. Sanderson, *Ergodic properties of a parameterised family of symmetric golden maps: the matching phenomenon revisited*, arXiv:2301.08623v1 (public January 20, 2023), https://arxiv.org/abs/2301.08623 .
2. Classical central limit theorem for finite, irreducible, aperiodic Markov chains, using the Poisson-equation martingale decomposition (the standard probability result used in the proof; no specific new source claim).
