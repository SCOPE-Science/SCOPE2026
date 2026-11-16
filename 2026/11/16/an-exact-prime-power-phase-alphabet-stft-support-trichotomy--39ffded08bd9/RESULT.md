# An exact prime-power phase-alphabet STFT support trichotomy

## Finding

Let \(p\) and \(\ell\) be distinct primes, let \(r\ge 1\), let \(q=\ell^r\), and let \(\mu_q\subset\mathbb C\) be the \(q\)-th roots of unity. For any two sequences \(f,g:\mathbb Z_p\to\mu_q\), define the unnormalized cyclic cross short-time Fourier transform by

\[
V_gf(x,k)=\sum_{t=0}^{p-1}f(t)\overline{g(t-x)}\,e^{-2\pi i kt/p},\qquad(x,k)\in\mathbb Z_p^2.
\]

The exact set of possible support cardinalities is

\[
\boxed{\bigl\{p,\ p^2-p+1,\ p^2\bigr\}.}
\]

All three cardinalities occur, with the following **complete support-set and equality classification**.

1. Support cardinality \(p\) occurs exactly when both sequences are constant. The support is then \(\{(x,0):x\in\mathbb Z_p\}\).
2. Support cardinality \(p^2-p+1\) occurs exactly when \(g\) is nonconstant and \(f(t)=\alpha g(t-x_0)\) for some \(\alpha\in\mu_q\) and a unique \(x_0\in\mathbb Z_p\). The only zero entries are precisely \(\{(x_0,k):1\le k\le p-1\}\).
3. In all other cases, every transform entry is nonzero, and the support cardinality is \(p^2\).

After quotienting by **independent global phase multiplications**, equivalently fixing \(f(0)=g(0)=1\), the exact counts of ordered pairs with the three successive support cardinalities are

\[
\boxed{1,\quad p(q^{p-1}-1),\quad q^{2p-2}-1-p(q^{p-1}-1).}
\]

Thus there are exactly \(p+2\) distinct attainable support subsets, not just three attainable cardinalities.

## Assumptions and scope

The cyclic length \(p\) is prime (including \(p=2\)); the coefficient alphabet has prime-power order \(q=\ell^r\), with \(\ell\ne p\) and \(r\ge1\). All sequence entries must belong to \(\mu_q\), so none vanishes and all have modulus one. The input is an **ordered** pair and the short-time transform is unnormalized; any nonzero global Fourier normalization leaves support unchanged. The support counts apply to exact algebraic zeros, not numerical thresholding.

## Proof

**Step 1: no zero-modulation cancellation.** Fix \(x\in\mathbb Z_p\) and write \(c_t=f(t)\overline{g(t-x)}\in\mu_q\). Suppose \(\sum_tc_t=0\). Choose a primitive \(q\)-th root \(\xi\), write each \(c_t=\xi^{j_t}\), and set \(A(X)=\sum_{t=0}^{p-1}X^{j_t}\in\mathbb Z[X]\), with \(0\le j_t<q\). Since \(A(\xi)=0\), the cyclotomic polynomial

\[
\Phi_q(X)=1+X^{\ell^{r-1}}+\cdots+X^{(\ell-1)\ell^{r-1}}
\]

divides \(A(X)\) in \(\mathbb Z[X]\). As \(\deg A<q\), division gives \(A(X)=\Phi_q(X) B(X)\) with \(\deg B<\ell^{r-1}\). At the level of coefficients, this says that the counts at exponents \(j,j+\ell^{r-1},\ldots,j+(\ell-1)\ell^{r-1}\) are equal for each \(0\le j<\ell^{r-1}\). Hence \(A(1)=p\) is divisible by \(\ell\), contrary to \(p\ne\ell\). Therefore \(V_gf(x,0)\ne0\) for every \(x\).

**Step 2: every nonzero-modulation zero forces a constant row.** Set \(C_x(X)=\sum_{t=0}^{p-1}c_tX^t\in\mathbb Q(\xi)[X]\), and let \(\zeta=e^{2\pi i/p}\). The distinct-prime condition implies

\[
[\mathbb Q(\xi,\zeta):\mathbb Q(\xi)]
=\frac{\varphi(pq)}{\varphi(q)}=p-1.
\]

Thus the minimal polynomial of the primitive \(p\)-th root \(\zeta^{-k}\), for every \(k\not\equiv0\pmod p\), over \(\mathbb Q(\xi)\) is \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). If \(V_gf(x,k)=C_x(\zeta^{-k})=0\), then \(C_x\) must be a scalar multiple of \(\Phi_p\) (its degree is at most \(p-1\)). Therefore all \(c_t\) are equal. Conversely, a constant row \(c_t\equiv\alpha\in\mu_q\) has Fourier support exactly \(\{0\}\). Consequently every time slice \(V_gf(x,\cdot)\) has either \(1\) or \(p\) nonzero coefficients, and the former case is equivalent to

\[
f(t)=\alpha g(t-x)\quad\text{for every }t\in\mathbb Z_p.
\]

**Step 3: at most one exceptional shift unless both inputs are constant.** Suppose the constant-row condition holds at two distinct shifts \(x\ne y\). Eliminating \(f\), one gets \(g(u+y-x)=\gamma g(u)\), with \(\gamma\in\mu_q\). Since \(y-x\) generates \(\mathbb Z_p\), iteration through \(p\) steps gives \(\gamma^p=1\). As also \(\gamma^q=1\) and \(\gcd(p,q)=1\), it follows that \(\gamma=1\). The generating translation then makes \(g\) constant and therefore \(f\) constant as well. Conversely, constant pairs have a constant Fourier row at all \(p\) shifts. This proves every support-set and cardinality assertion and uniqueness of \(x_0\).

**Step 4: count phase-normalized ordered pairs.** Every independent global \(\mu_q\)-phase orbit has the unique representative \(f(0)=g(0)=1\), giving \(q^{2p-2}\) total pairs. Exactly one pair has both sequences constant. For each of the \(q^{p-1}-1\) nonconstant normalized windows \(g\), and each shift \(x_0\), exactly one normalized \(f\) satisfies the translated-proportional condition, namely \(f(t)=g(t-x_0)/g(-x_0)\). By Step 3 these \(p\) choices are distinct. Subtraction gives the stated three multiplicities. All three values occur: the normalized constant pair, a nonconstant \(g\) with \(f=g\), and a nonconstant \(f\) with \(g\) constant. This completes the proof.

## Verification

The accompanying `verify.py` independently performs direct complex-DFT enumeration of **all** independently phase-normalized ordered pairs for \((p,q)=(2,3),(3,2),(3,4),(5,2),(5,4)\). The five census sizes are \(9,16,256,256,65536\); the observed support multiplicities are respectively \((1,4,4),(1,9,6),(1,45,210),(1,75,180),(1,1275,64260)\). The minimum numerically nonzero Fourier magnitude in the largest test is greater than \(0.27\); residuals classified as zero were below \(1.1\times10^{-15}\). These computations check the implementation and small instances, while the proof above is what establishes the infinite family.

Run `python verify.py` with Python 3; no third-party packages are needed.

## Relationship to prior work

Nicola (arXiv:2204.14176, 2022, Theorems 1.1 and 1.2) proves the general support bound and characterizes its equality cases for unrestricted complex sequences, but does not give the present complete prime-power-alphabet three-level spectrum or exact counts. Bartusel (arXiv:2206.06729, 2022, Section 4) studies cyclic STFT phase-retrieval injectivity and ambiguity support of other window families; it does not determine this alphabet-specific cross-STFT support law. Lam and Leung (arXiv:math/9511209) characterize lengths of vanishing root-of-unity sums; Step 1 re-proves the specific prime-power fact actually needed here. Existing finite cyclic STFT support-gap statements for arbitrary complex coefficients impose weaker lower bounds and do not imply the precise support-set classification or multiplicities.

## Limitations

The prime-power alphabet and the condition \(p\ne\ell\) are essential for the proof. For example, a five-term sequence over \(\mu_6\) can have zero sum, as witnessed by \(1,-1,1,\omega,\omega^2\) with \(\omega^3=1\) and \(\omega\ne1\), so the zero-frequency noncancellation step does not extend to arbitrary composite alphabet orders. If \(p\mid q\), the cyclotomic disjointness argument also fails. The theorem says nothing about arbitrary unimodular phases, sparse signals, other cyclic lengths, numerical near-zeros, or phase-retrieval uniqueness from magnitudes. Independent mathematical audit and exhaustive historical-priority verification have not been performed.

## References

1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, first public April 29, 2022, https://arxiv.org/abs/2204.14176.
2. D. Bartusel, *Injectivity conditions for STFT phase retrieval on Z, Z_d and R^d*, first public June 14, 2022, https://arxiv.org/abs/2206.06729.
3. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, 1995, https://arxiv.org/abs/math/9511209.
