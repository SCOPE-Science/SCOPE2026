# A sharp Fourier-boundary law for stationary digits on the \(p\)-adic integers

## Finding

Fix any prime \(p\). Every probability measure \(\mu\) on the additive compact group \(\mathbb Z_p\) invariant under deletion of its least-significant base-\(p\) digit has a canonical circle-probability Fourier boundary \(\nu\). For every integer \(k\) and integer \(n\ge1\),
\[
\left|\widehat\mu(kp^{-n})-\widehat\nu(k)\right|\le 2\pi|k|p^{-n}.
\]
The constant \(2\pi\) is optimal for the universal estimate at \(k=1\), in the limiting sense as \(n\to\infty\).

In particular, the only stationary-digit probability on \(\mathbb Z_p\) with Fourier transform vanishing at infinity is normalized Haar measure. Equivalently, with the standard dimension-one cap on Fourier dimension, every non-Haar digit-shift-invariant probability has Fourier dimension exactly zero, while Haar probability has Fourier dimension one. Neither ergodicity nor any independence or mixing hypothesis is needed.

## Assumptions and scope

The base \(p\) is prime and \(\mu\) is an arbitrary Borel probability on \(\mathbb Z_p\). Each \(x\in\mathbb Z_p\) has a unique expansion \(x=\sum_{j\ge0}a_jp^j\) with \(a_j\in\{0,\dots,p-1\}\). Put
\[
S(x)=\sum_{j\ge0}a_{j+1}p^j,
\qquad S_*\mu=\mu.
\]
Let \((a_j)_{j\in\mathbb Z}\) be the canonical two-sided stationary extension of the digit law under \(\mu\). Define the real random variable and its truncations
\[
U=\sum_{j=1}^{\infty}a_{-j}p^{-j}\in[0,1],
\qquad U_n=\sum_{j=1}^na_{-j}p^{-j};
\]
and let \(\nu\) be the law of \(U\pmod1\) on \(\mathbb R/\mathbb Z\). The standard additive character convention is
\[
\widehat\mu(\xi)=\int_{\mathbb Z_p}\exp(-2\pi i\{\xi x\}_p)\,d\mu(x),
\qquad\widehat\nu(k)=\int_{\mathbb R/\mathbb Z}e^{-2\pi ikt}\,d\nu(t),
\]
where \(\{y\}_p\in[0,1)\) is the fractional part of the finite negative-power \(p\)-adic expansion, and \(\xi\in\mathbb Q_p\). A probability is Rajchman when its transform tends to zero as \(|\xi|_p\to\infty\). Fourier dimension is the supremum of \(s\in[0,1]\) for which \(|\widehat\mu(\xi)|\le C_s(1+|\xi|_p)^{-s/2}\) for all \(\xi\).

## Proof

**Stationary extension.** Digit invariance under \(S\) says precisely that the one-sided digit process is stationary. Its compatible finite-dimensional laws have a unique two-sided stationary extension (by the consistency theorem); no reversibility is assumed.

**Exact finite-prefix identity.** For \(k\in\mathbb Z\) and \(n\ge1\), multiplication by \(kp^{-n}\) only reads the first \(n\) \(p\)-adic digits modulo integers. Hence
\[
\widehat\mu(kp^{-n})=
\mathbb E\exp\!\left(-2\pi ik\sum_{j=0}^{n-1}a_jp^{j-n}\right).
\]
By stationary block reversal in the two-sided extension, the ordered block \((a_0,\ldots,a_{n-1})\) has the same joint distribution as \((a_{-n},\ldots,a_{-1})\). Reindexing the weighted sum then gives the *exact* identity
\[
\widehat\mu(kp^{-n})=\mathbb E e^{-2\pi ikU_n}.
\tag{1}
\]
The deterministic expansion tail satisfies \(0\le U-U_n\le p^{-n}\), since \(\sum_{j>n}(p-1)p^{-j}=p^{-n}\). The elementary Lipschitz estimate \(|e^{is}-e^{it}|\le|s-t|\) therefore yields
\[
\big|\mathbb E e^{-2\pi ikU_n}-\mathbb E e^{-2\pi ikU}\big|\le2\pi|k|p^{-n},
\]
which proves the Fourier-boundary assertion for every integer \(k\), simultaneously.

**Rigidity.** If \(\mu\) is normalized Haar probability, its digits are independent uniform symbols and all its nontrivial Fourier coefficients vanish. Conversely, if \(\nu\) were normalized Lebesgue measure on the circle, every length-\(m\) base-\(p\) interval would have probability \(p^{-m}\). The interval endpoints have Lebesgue measure zero, so every past-digit word of length \(m\) then has probability \(p^{-m}\). Stationarity transfers those uniform word probabilities to all nonnegative-index words. Thus the digits under \(\mu\) are independent uniform symbols and \(\mu\) is Haar. It follows that non-Haar \(\mu\) has non-Lebesgue \(\nu\). Fourier uniqueness for finite circle measures provides some nonzero integer \(k\) with \(\widehat\nu(k)\ne0\). Equation (1) and the quantitative limit imply
\[
\lim_{n\to\infty}\widehat\mu(kp^{-n})=\widehat\nu(k)\ne0.
\]
Because \(|kp^{-n}|_p=p^n|k|_p\to\infty\), \(\mu\) is not Rajchman and cannot satisfy any positive-power Fourier-decay estimate. Thus its Fourier dimension is zero. Haar has Fourier dimension one by its exact cancellation at all nontrivial characters.

**Sharp error.** Take the fixed-point measure \(\mu=\delta_{-1}\); all digits equal \(p-1\), so \(U=1\), \(\widehat\nu(1)=1\), and
\[
\widehat\mu(p^{-n})=e^{2\pi i/p^n},\qquad
\lim_{n\to\infty}p^n\big|\widehat\mu(p^{-n})-1\big|=2\pi.
\]
No smaller universal coefficient than \(2\pi\) can hold in the displayed bound with \(k=1\).

## Verification

The accompanying dependency-free `CHECK.py` implements finite-prefix Fourier transforms both by exact digit-word enumeration and by reversed Markov-chain recursion. It checks the identities across nonuniform independent digits, nontrivially correlated reversible and nonreversible stationary chains, and uniform digits; it also tests the sharp fixed-point asymptotic. Run `python3 CHECK.py`. These finite computations are supplementary and cannot replace the argument for arbitrary stationary measures or unbounded \(n\).

## Relationship to prior work

Liu and Liao (2026) give non-Archimedean Fourier-dimension definitions and compute the dimensions of a family of \(p\)-adic Riesz products. The new statement concerns **all** shift-stationary digit laws, including arbitrarily correlated or nonergodic distributions, with an explicit circle Fourier boundary and optimal uniform convergence rate; their studied Riesz-product theorem does not imply it directly. Kingsbery, Levin, Preygel, and Silva (2009) describe the digit shift and its dynamics without proving the Fourier-boundary or Rajchman classification. Huang (2016) studies Fourier coefficients and rigidity of \(\times p\)-invariant measures on the *real circle* under different additional invariance/mixing hypotheses; the present claim concerns additive \(p\)-adic Fourier frequencies and uses a reversed stationary digit process. The sharp estimate and exhaustive stationarity class are the claimed additions, not the underlying digit coding, existence of a stationary extension, or uniqueness of Fourier coefficients. A previously recorded equivalent Fourier-duality observation could still exist.

## Limitations

The theorem requires digit-shift invariance and uses the standard additive Fourier characters on \(\mathbb Z_p\). It says nothing about Fourier decay of arbitrary nonstationary probabilities, or about Fourier dimension of their supports (as opposed to the measures themselves). The circle boundary does not necessarily distinguish distinct atomic stationary laws because two real base-\(p\) expansions can represent the same point. The coefficient \(2\pi\) is an optimal universal limit, not an assertion that each measure saturates the estimate. No independent external verification has been performed.

## References

1. Cheng Liu and Lingmin Liao, *\(P\)-adic \(s\)-energy and Fourier dimension*, arXiv:2609.22881, first submitted September 19, 2026. https://arxiv.org/abs/2609.22881
2. James Kingsbery, Alex Levin, Anatoly Preygel, and Cesar E. Silva, *Dynamics of the \(p\)-adic Shift and Applications*, arXiv:0903.4226, 2009. https://arxiv.org/html/0903.4226v1
3. Huichi Huang, *Fourier coefficients of \(\times p\)-invariant measures*, arXiv:1606.06078, 2016. https://arxiv.org/abs/1606.06078
