# A sharp boundary–bulk covariance reversal for uniformly random compositions

## Finding

For a uniformly selected positive integer composition \(A=(a_1,\ldots,a_K)\) of \(n\), let \(L_n=\sum_{j=1}^{K-1}|a_j-a_{j+1}|\) be the linear adjacent absolute variation and let \(B_n=|a_K-a_1|\) be the seam variation obtained when the linear composition is closed into a cycle. Then \(\operatorname{Cov}(L_n,B_n)=0\) for \(n=1,2\), is strictly positive exactly for \(3\le n\le14\), and is strictly negative for all \(n\ge15\). Further,

\[
\lim_{n\to\infty}\operatorname{Cov}(L_n,B_n)=-\frac4{189}.
\]

In particular the finite transition is sharp: \(\operatorname{Cov}(L_{14},B_{14})=1745/2097152>0\) while \(\operatorname{Cov}(L_{15},B_{15})=-551287/67108864<0\).

## Assumptions and scope

The composition has ordered strictly positive integer parts summing to \(n\). Every one of the \(2^{n-1}\) compositions is equiprobable. The one-part linear and seam variations are zero, and the two-part seam is counted only once in \(B_n\) (even though the cyclic arrangement has two oriented adjacencies). No independence between the two variations is assumed. The theorem is exact for every integer \(n\ge1\), not a statement about a random number of iid unconstrained parts.

## Proof

Introduce the ordinary generating-function variable \(z\) for total composition size and set \(t=z/2\). Every composition of size \(n\) receives weight \(2t^n=2^{1-n}z^n\), hence coefficients in \(z\) are expectations. Define

\[
W=\frac{t}{1-t},\quad P=\sum_{a,b\ge1}|a-b|t^{a+b}=\frac{2t^3}{(1-t)^3(1+t)},\quad Q=\sum_{a,b\ge1}(a-b)^2t^{a+b}=\frac{2t^3}{(1-t)^4}.
\]

For three consecutive parts with shared endpoint define

\[
J=\sum_{a,b,c\ge1}|a-b||a-c|t^{a+b+c}.
\]

Write \(h_a=\sum_{b\ge1}|a-b|t^b=t((a-1)-at+2t^a)/(1-t)^2\). Squaring and summing \(\sum_{a\ge1}t^a h_a^2\) yields the closed form

\[
J=\frac{t^2}{(1-t)^4}\left(\frac{t^2}{1-t}+4t^2\left[\frac{1-t}{(1-t^2)^2}-\frac1{1-t^2}\right]+\frac{4t^3}{1-t^3}\right).
\]

Distinguish a linear adjacent pair and the closing seam. For two-part compositions they coincide, giving \(Q\); for three or more parts the two edges incident to the seam share an endpoint, giving two copies of \(J/(1-W)\); all remaining pairs of edges are separated, giving \(P^2/(1-W)^2\). Therefore the generating functions of the mixed moment and the marginal means are

\[
H(z)=\sum_{n\ge1}\mathbb E[L_nB_n]z^n=2\left(Q+\frac{2J}{1-W}+\frac{P^2}{(1-W)^2}\right),
\]
\[
F(z)=\sum_{n\ge1}\mathbb E[L_n]z^n=\frac{2P}{(1-W)^2},\qquad G(z)=\sum_{n\ge1}\mathbb E[B_n]z^n=\frac{2P}{1-W},
\]

where the right-hand expressions are evaluated at \(t=z/2\). Direct rational reduction gives

\[
H(z)=\frac{128z^3-96z^5+48z^6-48z^7+20z^8+4z^9}{256-640z+384z^2+160z^3-160z^4-24z^5+8z^6+22z^7-3z^8-4z^9+z^{10}},
\]

\[
F(z)=\frac{-2z^3}{-4+8z-3z^2-2z^3+z^4},\qquad G(z)=\frac{-4z^3}{-8+12z-2z^2-3z^3+z^4}.
\]

These rational forms are also complete finite algorithms for the moments, by recurrence with constant denominator coefficient nonzero. Let \(h_n,f_n,g_n\) be their respective \(z^n\) coefficients; the desired covariance is exactly \(c_n=h_n-f_ng_n\).

Expand the three rational functions about their common dominant pole at \(z=1\). Exact partial-fraction subtraction yields

\[
H(z)=\frac{8/9}{(1-z)^2}-\frac{620/189}{1-z}+H_0(z),\quad F(z)=\frac{2/3}{(1-z)^2}-\frac{22/9}{1-z}+F_0(z),\quad G(z)=\frac{4/3}{1-z}+G_0(z),
\]

where \(H_0,F_0,G_0\) are rational, analytic on the open disc \(|z|<2\), with explicitly reproducible numerator and denominator listed in the verifier's algebraic notes below. Thus

\[
c_n=-\frac4{189}+h_{0,n}-\frac43 f_{0,n}-\left(\frac{2n}3-\frac{16}9\right)g_{0,n}-f_{0,n}g_{0,n}.
\]

On \(|z|=3/2\), coefficient-absolute-sum bounds on numerators and root-distance lower bounds on denominators give

\[
|H_0(z)|\le\frac{134105456}{189},\quad|F_0(z)|\le\frac{496}{9},\quad|G_0(z)|\le\frac{592}{3}.
\]

Every residual denominator has all roots on \(|z|=2\), so the Cauchy estimate gives, with \(r=2/3\),

\[
|c_n+4/189|\le\left[\frac{134105456}{189}+\frac43\frac{496}{9}+\left(\frac{2n}3+\frac{16}9\right)\frac{592}3\right]r^n+\frac{496}{9}\frac{592}{3}r^{2n}.
\]

For \(n\ge100\) this bound is decreasing and at \(n=100\) is smaller than \(4/189\), so \(c_n<0\) for every \(n\ge100\). Exact rational recurrence computation for \(n=1,\ldots,100\) proves \(c_1=c_2=0\), \(c_n>0\) at \(3\le n\le14\), and \(c_n<0\) at \(15\le n\le100\). This finite proof step is complete rather than extrapolation: all required 100 coefficients are evaluated by the displayed rational recurrences, checked by the embedded executable, which supplies the exact decisive inequalities and independent small-size enumeration. The asymptotic limit follows from the same pole separation.

## Verification

Run \(\texttt{python3 verify.py}\) using standard-library Python. It computes every coefficient of all three rational generating functions exactly using fractions, checks each sign for \(1\le n\le100\), independently enumerates all compositions for \(2\le n\le9\), and checks the strict rational Cauchy bound at \(n=100\) (monotone thereafter). The first sign-change values are reported exactly. The proof of the generating-function decomposition and complex-analytic bound is mathematical and not replaced by those finite tests.

## Relationship to prior work

Mansour's work on the sum of adjacent-letter differences addresses unconstrained words, not the joint seam/interior covariance for uniformly weighted positive compositions. Archibald, Knopfmacher and Mansour develop generating functions for the linear variation of compositions and its size/part-count statistics. Their described marginal variation generating functions do not specify its joint law with the closing absolute difference, which involves the three-part shared-endpoint sum \(J\). The present result is the joint moment, sharp sign boundary and limit, not a claim that variation itself or its marginal generating function is new.

## Limitations

The claim is for uniform ordered positive compositions and absolute first differences. Other weights, weak compositions and signed first differences are not classified. The proof supplies a same-document finite coefficient certificate and analytic all-size bound, but no independent audit and no absolute guarantee against historical implicit coverage by more general generating-function results.

## References

1. T. Mansour, “Enumeration of words by the sum of differences between adjacent letters,” *Discrete Mathematics and Theoretical Computer Science* (2009), https://dmtcs.episciences.org/467/pdf.
2. M. Archibald, A. Knopfmacher and T. Mansour, “Variation Statistics on Compositions,” *Fundamenta Informaticae* 117 (2012), 1–17, https://doi.org/10.3233/FI-2012-685.
