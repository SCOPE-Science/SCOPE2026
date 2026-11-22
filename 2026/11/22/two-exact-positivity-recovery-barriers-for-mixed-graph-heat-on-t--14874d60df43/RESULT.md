# Two exact positivity-recovery barriers for mixed graph heat on the four-site path

## Finding

For the unweighted four-site path \(P_4\), let \(L\) be its combinatorial Laplacian, \(\eta>0\), and \(S_\eta(t)=\exp[-t(L+\eta L^2)]\). Define \(\lambda_-=2-\sqrt2\), \(\lambda_+=2+\sqrt2\), \(g=1/\sqrt2\), and decay rates
\[
a=\lambda_-(1+\eta\lambda_-),\qquad b=2+4\eta,\qquad c=\lambda_+(1+\eta\lambda_+).
\]
Then \(0<a<b<c\). The functions
\[
F_\eta(t)=1+e^{-bt}-(1+g)e^{-at}-(1-g)e^{-ct},
\]
\[
G_\eta(t)=1-e^{-bt}-g(e^{-at}-e^{-ct})
\]
each have precisely one zero in \((0,\infty)\), respectively \(\tau_3(\eta)\) and \(\tau_2(\eta)\). Both are strictly negative before their positive zero and strictly positive afterward. The exact nonnegative-time set is
\[
\boxed{\{t\ge0:S_\eta(t)\text{ is entrywise nonnegative}\}=\{0\}\cup[\max\{\tau_2(\eta),\tau_3(\eta)\},\infty).}
\]
At strictly later positive times all entries are strictly positive.

The onset and strong-mixing limits are
\[
\lim_{\eta\downarrow0}\frac{\tau_2(\eta)}\eta=2,\qquad
\lim_{\eta\downarrow0}\frac{\tau_3(\eta)}\eta=6,
\]
\[
\lim_{\eta\to\infty}\eta\tau_j(\eta)=\sigma_j\quad(j=2,3),
\]
where \(\sigma_2\) and \(\sigma_3\) are the unique positive zeros of the respective limiting functions obtained by replacing \((a,b,c)t\) with \((\lambda_-^2,4,\lambda_+^2)s\). They obey \(0<\sigma_2<1<\sigma_3\), with \(\sigma_2\approx0.232818924776\) and \(\sigma_3\approx1.552676056635\). Consequently the complete positivity horizon tends to zero at both mixing-strength extremes and has at least one positive maximizer for finite \(\eta\).

## Assumptions and scope

Vertex order is the natural path order \(0,1,2,3\). The matrix is
\[
L=\begin{pmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{pmatrix}.
\]
The heat equation is the unweighted finite-dimensional real system \(u'(t)=-(L+\eta L^2)u(t)\). Entrywise positivity and nonnegativity are entrywise matrix properties, not positivity of the quadratic form. Time \(t=0\) is included as a separate isolated nonnegative time when \(\eta>0\). The theorem concerns \(\eta>0\), not the endpoint \(\eta=0\).

## Proof

**Exact spectral response.** The Laplacian eigenvalues are \(0,\lambda_-,2,\lambda_+\), with real orthogonal spectral projections. Put \(A=e^{-at}\), \(B=e^{-bt}\), \(C=e^{-ct}\). Direct multiplication of the spectral projections gives the complete set of off-diagonal classes:
\[
4(S_\eta)_{03}=1+B-(1+g)A-(1-g)C=F_\eta,
\]
\[
4(S_\eta)_{02}=4(S_\eta)_{13}=1-B-g(A-C)=G_\eta,
\]
\[
4(S_\eta)_{01}=4(S_\eta)_{23}=1-B+g(A-C),
\]
\[
4(S_\eta)_{12}=(1-A)+(B-C)+g(A-C).
\]
Because \(0<C<B<A<1\) for \(t>0\), the latter two classes are strictly positive. Every diagonal is also strictly positive because it is the sum of nonnegative eigenprojection diagonal weights multiplied by positive exponentials, and the constant eigenspace alone contributes \(1/4\) to each diagonal.

**Sign and number of crossings.** The exact generator \(Q=L+\eta L^2\) has \(Q_{02}=\eta\), \(Q_{03}=0\), and \((Q^2)_{03}=-2\eta(1+3\eta)\). Thus
\[
G_\eta(t)=-4\eta t+O_\eta(t^2),\qquad
F_\eta(t)=-4\eta(1+3\eta)t^2+O_\eta(t^3).
\]
Both tend to \(1\) at infinity. We use the standard generalized Descartes zero bound: a nonzero real exponential polynomial with strictly increasing real exponents has at most as many real zeros, counted with multiplicity, as sign changes of its ordered coefficient sequence. Equivalently, this is the variation-diminishing/Chebyshev property of exponential functions and follows by induction with Rolle's theorem after dividing by the last exponential and differentiating. For \(G_\eta\), the coefficient sequence in exponent order \(0,a,b,c\) is \((1,-g,-1,g)\), having two changes. Its zero at zero is simple, leaving at most one positive zero. For \(F_\eta\), the sequence is \((1,-(1+g),1,-(1-g))\), having three changes. Its zero at zero is double, leaving at most one positive zero. Existence follows from negative small-time signs and positive large-time limits. Both positive roots are simple (a higher multiplicity would violate the zero bounds), and all asserted signs follow. Taking the conjunction of the two potentially negative classes proves the exact positivity-time set.

**Two parameter limits.** As \(\eta\downarrow0\), expand the two spectral functions jointly at \(t=\eta u\):
\[
G_\eta(\eta u)=\eta^2(2u^2-4u)+O(\eta^3),\qquad
F_\eta(\eta u)=\eta^3\bigl(\tfrac23u^3-4u^2\bigr)+O(\eta^4),
\]
uniformly for \(u\) in compact sets. Evaluating on either side of the simple positive roots \(u=2\) and \(u=6\), using uniqueness, proves the small-mixing limits. For strong mixing put \(s=\eta t\). The three exponents converge to \(\lambda_-^2s,4s,\lambda_+^2s\), locally uniformly in \(s\). The limiting functions retain the same coefficient sign patterns and negative small-time signs, so each has a unique simple positive zero; zero continuity gives convergence of \(\eta\tau_2\) and \(\eta\tau_3\). Direct elementary evaluation gives \(G_\infty(1)>0\) and \(F_\infty(1)<0\), hence \(\sigma_2<1<\sigma_3\). The full horizon is continuous in \(\eta>0\), positive, tends to zero both as \(\eta\downarrow0\) and \(\eta\to\infty\), and therefore achieves a positive global maximum at some interior parameter by compactness.

## Verification

Run `python check_p4.py` with Python, NumPy and SciPy. The checker independently constructs \(\exp[-t(L+\eta L^2)]\) from a general-purpose matrix exponential and compares it to all four spectral transition formulas at 400 parameter/time pairs. It brackets and solves both positive crossings at eight representative mixing strengths, checks signs on either side, and tests the small-parameter asymptotic predictions. Matrix-exponential tests are numerical corroboration; the all-parameter existence and uniqueness proof is the exponential-polynomial zero bound, not finite sampling.

## Relationship to prior work

Daners, Glück and Kennedy (arXiv:1511.05294, initially public 2015-11-17) develop general spectral and resolvent conditions for eventual positivity, including higher-order generators. Their qualitative theory does not by itself supply the four-site mixed-generator entry formulas, the two sharp sign-crossing equations or their parameter asymptotics. Gregorio and Mugnolo (arXiv:1712.07370, initially public 2017-12-20) treat graph bi-Laplacians and pure \(L^2\) heat; their setting is the strong-mixing limit rather than the continuously variable mixed generator. Separate results on complete-multipartite squared-Laplacian heat and fourth-order Gauss–Legendre time stepping concern different graphs or rational time-stepping maps. The present result is limited to the exact four-site mixed exponential and is not a general eventual-positivity characterization.

## Limitations

The path has precisely four unweighted vertices and uses the unnormalized combinatorial Laplacian. No closed elementary form for the positive crossing roots is claimed. The formula with a maximum does not assert which crossing is later for every finite parameter. Existence, but not uniqueness, of a mixing strength maximizing the complete positivity delay is proved. Weighted paths, graphs with more vertices and time-discretized propagators are outside the result. Historical priority, especially possible older equivalent finite-matrix calculations under different terminology, is not independently certified.

## References

1. D. Daners, J. Glück and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294 (first version 2015-11-17), https://arxiv.org/abs/1511.05294.
2. F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370 (first version 2017-12-20), https://arxiv.org/abs/1712.07370.
3. *Sharp positivity cutoff for squared-Laplacian heat on every complete multipartite graph*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-positivity-cutoff-for-squared-laplacian-heat-on-every-comp--e4f9c89a420f.
4. *Unconditional fourth-order Gauss positivity on weighted paths: a four-vertex cutoff*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unconditional-fourth-order-gauss-positivity-on-weighted-paths-a--73910250a06c.
