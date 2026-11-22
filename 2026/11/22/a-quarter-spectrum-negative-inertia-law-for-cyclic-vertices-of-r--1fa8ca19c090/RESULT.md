# A quarter-spectrum negative-inertia law for cyclic vertices of random mappings

## Finding

Let \(n\ge2\), and for every self-map \(f:[n]\to[n]\), let \(C(f)\) be the nonempty set of vertices on directed cycles of its functional graph. Write \(\mu_n(R)=|\{f:C(f)=R\}|\), including multiplicity. Let \(T_n\) be counting convolution by \(\mu_n\) on the Boolean group \(G_n=(\mathbb Z/2\mathbb Z)^n\), with no probability normalization. Then every Walsh multiplier indexed by an odd-cardinality set \(S\subseteq[n]\) with \(2|S|\ge n\) is strictly negative.

Consequently the negative inertia obeys
\[
N_-(T_n)\ge H_n:=\sum_{\substack{\lceil n/2\rceil\le s\le n\\s\equiv1\pmod2}}\binom ns,
\qquad \lim_{n\to\infty}\frac{H_n}{2^n}=\frac14.
\]
In particular, none of these convolution operators is positive semidefinite. The result gives a positive-density, all-order sign obstruction; it does not determine every Fourier multiplier.

## Assumptions and scope

All maps are unrestricted functions from \([n]\) to itself, including loops. A cyclic vertex is one on a directed cycle, not one merely leading into a cycle. The Fourier convention is the unnormalized character \(\chi_S(R)=(-1)^{|S\cap R|}\), so the convolution eigenvalue is \(\Lambda_{n,S}=\sum_R\mu_n(R)\chi_S(R)\). There are \(\binom ns\) characters of Hamming weight \(s\). Strict negativity refers to real eigenvalues, with multiplicity.

## Proof

**1. Exact root-set count.** Fix a nonempty set \(R\) of size \(k\). To have exactly \(R\) cyclic, the restriction of \(f\) to \(R\) must be a permutation (\(k!\) possibilities), and every other vertex must belong to a directed forest rooted in \(R\). The classical complete-graph rooted-forest count is \(k n^{n-k-1}\), interpreted as \(1\) at \(k=n\). Therefore
\[
\mu_n(R)=k!\,k\,n^{n-k-1}.
\]
The formula is integer-valued at the boundary \(k=n\), where it equals \(n!\). There are no maps with empty cyclic set.

**2. Exact Walsh transform.** Let \(s=|S|\) and
\[g_{n,s}(z)=(1-z)^s(1+z)^{n-s}=\sum_{k=0}^n c_kz^k.\]
The coefficient \(c_k\) is precisely \(\sum_{|R|=k}(-1)^{|S\cap R|}\). Because \(\int_0^\infty e^{-t}t^kdt=k!\), the finite sum can be integrated term by term:
\[
\Lambda_{n,s}=\sum_{k=1}^n c_k k!\,k\,n^{n-k-1}
=n^{n-1}\int_0^\infty e^{-t}\frac tn g'_{n,s}(t/n)\,dt.
\]
For \(1\le s\le n\), direct differentiation gives
\[
g'_{n,s}(z)=(1-z)^{s-1}(1+z)^{n-s-1}\bigl((n-2s)-nz\bigr).
\]
At \(s=n\), the factor \((1+z)^{-1}\) cancels against the bracket, giving the polynomial derivative \(-n(1-z)^{n-1}\); thus there is no pole on the integration range. Substitution yields the exact integral
\[
\Lambda_{n,s}=n^{n-2}\int_0^\infty e^{-t}t(n-2s-t)
(1-t/n)^{s-1}(1+t/n)^{n-s-1}\,dt.
\]

**3. Strict sign.** If \(s\) is odd, then \(s-1\) is even and \((1-t/n)^{s-1}\ge0\) for all \(t\ge0\). The second power is strictly positive for \(t\ge0\), and the apparent negative exponent in the endpoint case was already canceled. If also \(2s\ge n\), then \(n-2s-t<0\) for every \(t>0\). The integrand is strictly negative on a nonempty open interval and never positive, so \(\Lambda_{n,s}<0\).

**4. Inertia density.** Each qualifying character gives a negative eigenvalue of the real self-adjoint convolution operator. Counting them yields \(H_n\). Binomial symmetry and the alternating half-binomial identity give \(H_n=2^{n-2}+O(2^n/\sqrt n)\), hence \(H_n/2^n\to1/4\). At least one odd weight above the midpoint exists for every \(n\ge2\), proving the non-positive-semidefinite assertion.

## Verification

The standalone exact checker \(check.py\) independently enumerates every self-map through size six, reconstructs cyclic vertex sets without using the forest formula, and compares the complete Walsh transforms to the finite closed formula. It also tests strict signs for all qualifying odd character weights through size 49, and verifies the derivative-factorization identity coefficientwise through size 25. These computations corroborate boundary handling; the all-order result rests on the preceding analytic proof.

## Relationship to prior work

Hansen and Jaworski's *Random Mappings with a Given Number of Cyclical Points* (2010) develops a rooted-forest-plus-permutation model and conditional component-size laws. Its complete 19-page open article was inspected. The rooted-forest decomposition is classical and is not claimed here. The additional statement is a strict, all-order Walsh sign theorem and the induced positive-density negative-inertia bound. Earlier work on cyclic-point joint laws and negative dependence studies different probabilistic comparisons; such pairwise or low-order statements do not determine signed parity moments for all large odd subsets.

## Limitations

The theorem supplies a guaranteed negative spectral sector, not an exact negative inertia, nullity, positive-frequency classification, invertibility criterion, or operator norm. Novelty is assessed under bounded literature and database inspection; an unindexed equivalent signed cyclic-point identity remains possible. No independent audit has been performed.

## References

- J. C. Hansen and J. Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria 94 (2010), 341–359. Open text: https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf ; publisher record (dated 2010-01-31): https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/ .
- Classical rooted-forest enumeration (Cayley's all-minors forest count) is used only for the known cyclic-root-set multiplicity; the proof above supplies the required specialization.
