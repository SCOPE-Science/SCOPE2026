# Re-entrant positive definiteness and sharp Walsh recovery for two-coloured permutation cycles

## Finding

For each integer \(n\ge1\), take every permutation \(\pi\in S_n\), independently colour each of its cycles one of two named colours, and record only the fixed-position set \(F(\pi)=\{i:\pi(i)=i\}\). Let \(a_n(x)\) be the number of these coloured permutations with incidence vector \(x\in\mathbb F_2^n\), and define unnormalized XOR convolution \(T_nf(x)=\sum_{y\in\mathbb F_2^n}a_n(y)f(x+y)\).

Every Walsh character of weight \(k\) is an eigenvector with eigenvalue
\[
\Lambda_{n,k}=\sum_{j=0}^{k}\binom{k}{j}(-4)^j(n-j+1)!,\qquad 0\le k\le n.
\]
All these eigenvalues are nonzero **except** the weight-one eigenvalues at \(n=3\). Thus \(T_n\) is singular precisely for \(n=3\), when its nullity is \(3\) and its rank is \(5\). The operator is **positive definite precisely for \(n=6\) or \(n\ge8\)**: positivity holds at \(n=6\), fails at \(n=7\), and holds permanently from \(n=8\) onward.

The sharp smallest eigenvalue is \(112\) at \(n=6\), \(12928\) at \(n=8\), and for every \(n\ge9\) equals
\[
M_n=\sum_{j=0}^{n}\binom nj(-4)^j(n-j+1)!>0.
\]
The largest eigenvalue throughout these positive-definite dimensions is \((n+1)!\). Consequently, the exact Euclidean condition numbers are \(45\) at \(n=6\), \(2835/101\) at \(n=8\), and \((n+1)!/M_n\) for \(n\ge9\). Furthermore,
\[
\lim_{n\to\infty}\frac{(n+1)!}{M_n}=e^4.
\]

## Assumptions and scope

There is no probability normalization in \(T_n\); the total number of coloured permutations is \((n+1)!\). Dividing the operator by this number gives the probability convolution and preserves its rank and condition number. Positive definite means positive as a self-adjoint real operator in standard \(\ell^2(\mathbb F_2^n)\). At \(n=3\) the three vanishing characters are precisely those whose support is one coordinate. Each frequency shell of weight \(k\) has multiplicity \(\binom nk\). No claim is made about other cycle-colouring numbers or non-Euclidean inverse norms.

## Proof

**Cycle-weighted enumeration.** For \(m\ge0\), let \(Q_m=\sum_{\pi\in S_m}2^{c(\pi)}\), where \(c(\pi)\) is the cycle count. Inserting a new largest element into an existing cycle gives \(m\) choices, and making it a new one-element cycle gives two colour choices. Hence \(Q_0=1\), \(Q_{m+1}=(m+2)Q_m\), and \(Q_m=(m+1)!\). If \(j\) named positions are required to be fixed, they form \(j\) separate cycles with \(2^j\) colourings, and the unrestricted complement contributes \((n-j+1)!\). Expanding
\[
(-1)^{|A\cap F(\pi)|}=\prod_{i\in A}(1-2\mathbf1_{\{\pi(i)=i\}})
\]
for a character supported on \(A\), \(|A|=k\), gives the stated eigenvalue \(\Lambda_{n,k}\) by counting prescribed fixed points. This also proves the Walsh diagonalization of the convolution without any probabilistic approximation.

**Gamma-moment identity and recurrence.** If \(X\) has density \(xe^{-x}\) on \((0,\infty)\), then \(\mathbb E X^m=(m+1)!\). Thus
\[
\Lambda_{n,k}=\mathbb E\big[X^{n-k}(X-4)^k\big],\quad M_n=\mathbb E[(X-4)^n].
\]
The binomial expression yields the exact adjacent-shell identity
\[
\Lambda_{n,k}-\Lambda_{n,k+1}=4\Lambda_{n-1,k}\qquad(0\le k<n).
\]
Integration by parts against \(xe^{-x}\), with vanishing endpoint terms, gives \(\mathbb E[Xf'(X)]=\mathbb E[(X-2)f(X)]\) for polynomials \(f\). Taking \(f(x)=(x-4)^n\), and writing \(X=(X-4)+4\), proves
\[
M_{n+1}=(n-2)M_n+4nM_{n-1}\qquad(n\ge1).
\]
Direct exact values are \(M_7=-704\), \(M_8=15744\), and \(M_9=71936\). The recurrence has positive coefficients for \(n\ge3\); beginning with \(M_8,M_9>0\) yields \(M_n>0\) for every \(n\ge8\).

**Complete sign and invertibility classification.** The exact vectors of \(\Lambda_{n,k}\), in increasing \(k\), for \(n=1,2,3,4,5,6,7\) are respectively
\[
\begin{aligned}
&(2,-2),\quad (6,-2,6),\quad (24,0,8,-16),\\
&(120,24,24,-8,56),\\
&(720,240,144,48,80,-144),\\
&(5040,2160,1200,624,432,112,688),\\
&(40320,20160,11520,6720,4224,2496,2048,-704).
\end{aligned}
\]
At \(n=8\) the complete vector is
\[
(362880,201600,120960,74880,48000,31104,21120,12928,15744).
\]
These exact evaluations prove all claims for \(n\le8\). At \(n=9\), the adjacent-shell identity and \(\Lambda_{8,k}>0\) show strict decrease as \(k\) increases, while \(\Lambda_{9,9}=M_9>0\); hence all nine-order multipliers are positive. Suppose all multipliers at order \(n-1\) are positive for some \(n\ge10\). The shell identity makes \(\Lambda_{n,0}>\Lambda_{n,1}>\cdots>\Lambda_{n,n}\), and the recurrence makes \(\Lambda_{n,n}=M_n>0\). Induction therefore gives strict positivity and unique smallest weight shell \(k=n\) at every \(n\ge9\). The largest eigenvalue is \(\Lambda_{n,0}=(n+1)!\). Each multiplier appears with multiplicity \(\binom nk\), proving the nullity and precise condition numbers.

**Limit of the condition numbers.** Divide the full-character binomial sum by \((n+1)!\). For every fixed \(j\), its \(j\)-th term tends to \((-4)^j/j!\), and its absolute value is at most \(4^j/j!\), since
\[
\binom nj\frac{(n-j+1)!}{(n+1)!}=\frac{(n)_j}{(n+1)_j j!}\le\frac1{j!}.
\]
Extend the sum by zero beyond \(j=n\). Dominated convergence for series gives \(M_n/(n+1)!\to e^{-4}\). Positive denominators from \(n\ge8\) then give the claimed condition-number limit.

## Verification

The accompanying standalone `verify.py` uses only standard-library exact arithmetic. It independently enumerates every uncoloured permutation through \(n=7\), weights each by its exact number of cycle-colourings, and checks every Boolean character against the derived formula. It additionally checks all character shells and recurrences through \(n=180\), an independent exponential-generating-function calculation through \(n=90\), and the exact small-order condition numbers. It passed \(17890\) exact assertions. These finite computations are corroboration, **not** the infinite induction proof above. Run it with `python verify.py`.

## Relationship to prior work

The fixed-point statistic of permutations is classical; see Diaconis, Fulman and Guralnick. The Ewens cycle-count measure, including its partition function \((1-z)^{-\theta}\), is standard and is explicitly presented for general \(\theta\) in Hughes, Najnudel, Nikeghbali and Zeindler. At \(\theta=2\) this measure is realized without fractional weights by independently colouring every permutation cycle in two ways. This account claims neither the classical cycle enumeration nor the fixed-point marginal distribution as new. Its addition is the **entire weight-by-weight Boolean Fourier sign classification**, including the exceptional \(n=3\) nullspace, nonmonotone positivity at \(n=6,7,8\), and sharp stable recovery constants. The results surveyed in these sources concern permutation-group fixed-point distributions and random permutation-matrix spectral statistics, rather than this separate binary-group convolution's Walsh inertia.

## Limitations

The classification is restricted to two named cycle colours, all permutations on \(n\) labels, and the Boolean encoding of the ordinary fixed-position set. The bound \(e^4\) is an asymptotic condition-number limit, not a uniform upper bound in all dimensions. No assertion is made about the historical absence of equivalent identities in specialized Laguerre, shifted-gamma-moment or Ewens literature; independent priority review remains to be performed. The integer verifier checks a large finite range but does not certify a universal claim by enumeration.

## References

1. P. Diaconis, J. Fulman and R. Guralnick, *On fixed points of permutations*, arXiv:0708.2643v1, publicly submitted 2007-08-20, https://arxiv.org/abs/0708.2643 .
2. C. P. Hughes, J. Najnudel, A. Nikeghbali and D. Zeindler, *Random permutation matrices under the generalized Ewens measure*, arXiv:1109.5010v1, publicly submitted 2011-09-23, https://arxiv.org/abs/1109.5010 ; in particular the cycle-weighted normalization and its generating function in Section 2.
