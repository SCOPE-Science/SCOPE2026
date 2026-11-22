# Exact odd-prime valuation spectra of two-index super Catalan numbers

## Finding

For nonnegative integers \(m,n\), let the integral undivided super Catalan factorial quotient be
\[
S(m,n)=\frac{(2m)!(2n)!}{m!n!(m+n)!}.
\]
Fix an odd prime \(p\). For every integer \(r\ge0\), define the entire valuation enumerator over the square of base-\(p\) length \(r\):
\[
H_{p,r}(t)=\sum_{0\le m,n<p^r}t^{\nu_p(S(m,n))}.
\]
Then, with \(L=p(p+1)/2\) and \(B=p(p-1)/2\),
\[
\boxed{\sum_{r\ge0}H_{p,r}(t)z^r=\frac{1-ptz}{1-L(1+t)z+p^3tz^2}.}
\]
Equivalently, \(H_{p,0}=1\), \(H_{p,1}=L+Bt\), and
\[
H_{p,r}=L(1+t)H_{p,r-1}-p^3tH_{p,r-2}\qquad(r\ge2).
\]
Each integer valuation \(j\) with \(0\le j\le r\) is attained. The count of nondivisible quotients is \(L^r\), and the number with valuation exactly \(r\), for \(r\ge1\), is \(BL^{r-1}\). For example, \(H_{3,1}(t)=6+3t\) and \(H_{3,2}(t)=36+27t+18t^2\).

The valuation of a uniformly random pair of indices is exactly the sum of the first \(r\) states of a binary Markov chain started at state zero, with transition matrix
\[
P=\frac{1}{p^2}\begin{pmatrix}L&B\\ B&L\end{pmatrix}.
\]
Thus its expected valuation is
\[
\mathbb E V_r=\frac r2-\frac{1-p^{-r}}{2(p-1)}
\]
and its exact variance is
\[
\operatorname{Var}(V_r)=\frac14\left[r+\frac{2(r(p-1)-p+p^{1-r})-(1-p^{-r})^2}{(p-1)^2}\right].
\]
For fixed odd \(p\), the normalized fluctuations converge to a standard Gaussian:
\[
\frac{V_r-\mathbb EV_r}{\sqrt{r(p+1)/(4(p-1))}}\ \Longrightarrow\ N(0,1).
\]

## Assumptions and scope

The variables \(m,n\) are unrestricted nonnegative integers in the specified finite square, \(p\) is any odd prime, and \(r\) is any nonnegative integer. The factorial quotient \(S(m,n)\) is integer, as established classically. Some references instead use the normalized super Catalan number \(T(m,n)=S(m,n)/2\); because \(p\) is odd, the claimed valuations and histograms are identical for \(S\) and \(T\), even for \(m=n=0\) where \(T(0,0)=1/2\). This theorem does not assert the same formula at \(p=2\).

## Proof

By the factorial Legendre formula or Kummer's theorem,
\[
\nu_p(S(m,n))=\nu_p\binom{2m}{m}+\nu_p\binom{2n}{n}-\nu_p\binom{m+n}{m}.
\]
Read the base-\(p\) digits \(a,b\in\{0,\ldots,p-1\}\) of \(m,n\) from least to most significant. Let \((c_m,c_n,c_s)\in\{0,1\}^3\) be the incoming carries respectively for \(m+m\), \(n+n\), and \(m+n\), initially \((0,0,0)\). The outgoing carry state is
\[
(d_m,d_n,d_s)=\left(\left\lfloor\frac{2a+c_m}{p}\right\rfloor,\left\lfloor\frac{2b+c_n}{p}\right\rfloor,\left\lfloor\frac{a+b+c_s}{p}\right\rfloor\right).
\]
At that digit the valuation gains \(d_m+d_n-d_s\). Because the two arguments are below \(p^r\), each three-way addition has at most one final outgoing carry; all carries are therefore accounted for by the \(r\) selected digits.

Here is a complete integer transition certificate, valid for \(p=2h+1\) and \(h\ge1\). The six reachable carry states, in order, are \(000,010,011,100,101,111\). Define
\[
A=(h+1)^2,\quad B=h(h+1)/2,\quad C=h^2,\quad D=h(h+1),\quad E=(h+1)(h+2)/2,\quad F=h(h-1)/2.
\]
For any row state and column state in the displayed order, the number of digit pairs \((a,b)\) realizing that transition is the corresponding entry of
\[
\begin{pmatrix}
 A&B&B&B&B&C\\
 D&E&B&B&F&D\\
 D&B&E&F&B&D\\
 D&B&F&E&B&D\\
 D&F&B&B&E&D\\
 C&B&B&B&B&A
\end{pmatrix}.
\]
This table follows directly by splitting \(0\le a,b\le2h\) at the two doubling thresholds \(2a+c_m\ge2h+1\), \(2b+c_n\ge2h+1\), and summing the allowed \(a+b+c_s\) inequalities for each cell; for example the first-row \(000\to000\) cell has \((h+1)^2\) pairs and the first-row \(000\to111\) cell has \(h^2\). The first and last cells together with the four middle cells in every row sum to \(p^2\). The transitions \(000\to001\) and \(000\to110\), and all incoming-state analogues, are impossible, so no discarded state is reachable.

Partition the six states by \(\epsilon=c_m+c_n-c_s\), which equals either zero or one: class zero is \(\{000,011,101\}\), class one is \(\{010,100,111\}\). Summing each row of the displayed matrix over its destination class gives exactly
\[
\begin{array}{c|cc}&\epsilon'=0&\epsilon'=1\\\hline
\epsilon=0&L&B\\
\epsilon=1&B&L
\end{array}.
\]
The outgoing increment \(d_m+d_n-d_s\) is exactly the new class \(\epsilon'\). Thus the weighted lumped transfer is
\[
K(t)=\begin{pmatrix}L&Bt\\ B&Lt\end{pmatrix},\qquad
H_{p,r}(t)=(1,0)K(t)^r\binom11.
\]
Since \(\operatorname{tr}K=L(1+t)\) and \(\det K=p^3t\) (because \(L^2-B^2=p^3\)), Cayley–Hamilton yields the recurrence; the initial numerator is fixed by \(H_{p,0}=1\) and \(H_{p,1}=L+Bt\), hence \(L+Bt-L(1+t)=-pt\).

All transition counts between the two classes are positive. Consequently every length-\(r\) binary class word can be realized by digit pairs, so the support is exactly \(\{0,\ldots,r\}\). At \(t=0\), only repeated zero states survive, giving \(L^r\). Repeated class one has count \(BL^{r-1}\) for positive \(r\).

Dividing the transition counts by \(p^2\) gives the stated stationary-symmetric two-state chain; its nontrivial eigenvalue is \(1/p\), so \(\mathbb E[(-1)^{X_i}]=p^{-i}\) and \(\mathbb E[(-1)^{X_i+X_j}]=p^{-|i-j|}\). Summing means and covariances for \(V_r=\sum_{i=1}^{r}X_i\) gives the exact displayed formulas. The irreducible, aperiodic finite-state chain has occupation-time asymptotic variance \((p+1)/[4(p-1)]>0\); the standard finite-state Markov central limit theorem gives the Gaussian statement.

## Verification

The attached standard-library checker independently reconstructs all six-state digit-pair transitions for seven odd primes through nineteen, verifies the rational-generating-function recurrence at depths zero through seven, and directly computes the factorial quotient's valuations over complete squares for primes three through eleven. On execution it reports `CHECK_OK 106310`. These finite checks corroborate, but do not replace, the all-prime digit-inequality and matrix proof.

## Relationship to prior work

Allen–Gheorghiciuc (2014, arXiv:1403.5246) provides the classical quotient, its integrality background and a two-Motzkin weighted interpretation; its Section 1–3 do not state a two-index odd-prime valuation histogram. Their companion super Catalan polynomial paper (arXiv:1403.5296) concerns a \(q\)-analogue and its combinatorial interpretation rather than this odd-prime valuation spectrum. Related one-index Catalan and Fuss–Catalan valuation formulas have different index domains and factorial quotients. Kummer's theorem supplies the valuation-to-carry reduction but not the evaluated six-to-two-state transfer for the specific quotient.

## Limitations

No assertion is made for prime two, whose carry transition structure differs. Historical-priority uncertainty remains for possible prior general results about factorial-ratio carry automata from which this special matrix may be extracted. The central limit theorem is for a fixed odd prime as the digit depth grows; there is no simultaneous-limit claim in \(p\). Finite checker results are not substitutes for the symbolic count identities.

## References

- E. Allen and I. Gheorghiciuc, *A weighted interpretation for the super Catalan numbers*, arXiv:1403.5246, initially posted 2014-03-20, https://arxiv.org/html/1403.5246v2.
- E. Allen and I. Gheorghiciuc, *On super Catalan polynomials*, arXiv:1403.5296, initially posted 2014-03-20, https://arxiv.org/html/1403.5296v2.
- E. E. Kummer, classical base-\(p\) carry theorem for valuations of binomial coefficients (1852).
- J.-C. Liu, *Congruences on sums of super Catalan numbers*, arXiv:1804.09485 (related congruence literature, not a valuation spectrum).
