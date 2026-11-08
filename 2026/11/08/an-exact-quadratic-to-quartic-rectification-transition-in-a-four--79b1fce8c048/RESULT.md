# An exact quadratic-to-quartic rectification transition in a four-site exclusion ring

## Finding

For a four-site periodic exclusion process with exactly two particles, let the four site-departure rates be \((a,b,1,1)\), where \(a,b>0\), and let the clockwise and counterclockwise hopping rates from site \(i\) be, respectively, \(w_i(1+\varepsilon)/2\) and \(w_i(1-\varepsilon)/2\). Hops onto occupied sites are suppressed. Write \(J_{a,b}(\varepsilon)\) for the unique stationary clockwise current across bond \((0,1)\), for \(|\varepsilon|<1\).

Set
\[
A=ab+2a+2b+1,\qquad B=ab+3a+3b+1.
\]
The response is real analytic at zero, with \(J_{a,b}(0)=0\) and coefficients defined by \(J_{a,b}(\varepsilon)=\sum_{k\ge1}c_k(a,b)\varepsilon^k\) locally. Its first two coefficients are exactly
\[
c_1(a,b)=\frac{4ab(a+b+2)}{AB},\qquad
c_2(a,b)=\frac{4ab(a-1)(a-b)(b-1)(ab-3)}{A^2B^2}.
\]
Consequently this *entire two-contrast family* has the following exhaustive classification of its first nonzero even response coefficient:

1. If \(a=1\), \(b=1\), or \(a=b\), a reflection preserves all site rates. The full current is odd: \(J_{a,b}(\varepsilon)=-J_{a,b}(-\varepsilon)\) for every \(|\varepsilon|<1\).
2. If \(a,b\ne1\), \(a\ne b\), and \(ab\ne3\), then \(c_2(a,b)\ne0\); the leading even response is quadratic. Its sign is the sign of \((a-1)(a-b)(b-1)(ab-3)\).
3. If \(a,b\ne1\), \(a\ne b\), and \(ab=3\), the quadratic response vanishes *without* a spatial reflection or a uniform bond-bias ratio. Writing \(b=3/a\), the next even coefficient is
\[
c_4(a,3/a)=
\frac{12a^2(a-3)(a-1)(a^2-3)}{(a^2+2a+3)^2(3a^2+4a+9)^2}\ne0.
\]
Thus the leading parity-breaking response on the entire non-reflective cancellation curve is quartic:
\[
\frac{J_{a,3/a}(\varepsilon)+J_{a,3/a}(-\varepsilon)}2
=c_4(a,3/a)\varepsilon^4+O(\varepsilon^6),
\quad a>0,\ a\notin\{1,\sqrt3,3\}.
\]

The complete three-way classification is not merely a single counterexample to a generic quadratic-response conjecture: it specifies both the sign and the exact codimension-one crossover where the first rectification term changes order. The isolated existence of non-reflective zero-quadratic-response rings is already known and is not claimed as new.

## Assumptions and scope

The system is a continuous-time, hard-core exclusion process on \(\mathbb Z/4\mathbb Z\). Exactly two indistinguishable particles occupy distinct sites. A rightward hop from occupied site \(i\) to vacant site \(i+1\) occurs at rate \((1+\varepsilon)w_i/2\); a leftward hop to vacant site \(i-1\) occurs at rate \((1-\varepsilon)w_i/2\). All indices are modulo four. The rate vector is exactly \(w=(a,b,1,1)\) with \(a,b>0\), and \(-1<\varepsilon<1\). There are no entry or exit reservoirs. Uniform choice of time units fixes the two baseline rates to one. The model includes both adjacent nonbaseline trap rates and their symmetric or identical-rate limits.

The stationary chain is irreducible for every parameter in this domain. The clockwise current across the oriented bond \(0\to1\) is the mean number of accepted \(0\to1\) hops per time minus the accepted \(1\to0\) hops per time. Stationarity makes the same signed current flow across all four oriented bonds.

The leading *even response* means the first nonzero Taylor coefficient of the symmetric part \([J(\varepsilon)+J(-\varepsilon)]/2\); it does not mean the first nonlinear term of the full current, which may have a cubic contribution.

## Proof

**1. Finite-state analytic reduction.** Order the six occupied-site configurations as \((01,02,03,12,13,23)\). Let \(Q(\varepsilon)=Q_0+\varepsilon Q_1\) be the six-state column generator, with off-diagonal entries given by the allowed hops, and diagonal entries chosen to make each column sum zero. Let the column vector \(\pi(\varepsilon)\) denote the stationary law. Irreducibility implies existence and uniqueness for \(|\varepsilon|<1\), and replacing one row of \(Q(\varepsilon)\) with ones produces a matrix invertible at zero. Thus \(\pi\), and hence \(J\), are real analytic near zero.

The exact matrices, in the stated state order, are \(Q_j=K_j/2\), with
\[
K_0=\begin{pmatrix}
-a-b&1&0&0&1&0\\
b&-2a-2&1&b&0&1\\
0&1&-a-1&0&b&0\\
0&a&0&-b-1&1&0\\
a&0&a&1&-2b-2&1\\
0&a&0&0&b&-2
\end{pmatrix},
\quad
K_1=\begin{pmatrix}
a-b&-1&0&0&1&0\\
b&0&-1&-b&0&1\\
0&1&1-a&0&-b&0\\
0&a&0&b-1&-1&0\\
-a&0&a&1&0&-1\\
0&-a&0&0&b&0
\end{pmatrix}.
\]
The signed current functional is \(J(\varepsilon)=(F_0+\varepsilon F_1)\pi(\varepsilon)\), with
\[
F_0=\tfrac12(0,a,a,-b,-b,0),\qquad
F_1=\tfrac12(0,a,a,b,b,0).
\]
All entries follow directly by enumerating each possible vacant neighboring destination; these formulas also fix every normalization and orientation convention.

**2. Exact response coefficient.** Expand \(\pi(\varepsilon)=\sum_{k\ge0}\pi_k\varepsilon^k\). Detailed balance at zero gives
\[
\pi_0=A^{-1}(1,b,b,a,a,ab)^{\mathsf T}.
\]
For \(k\ge1\), the unique normalized correction solves
\[
Q_0\pi_k=-Q_1\pi_{k-1},\qquad
\mathbf1^{\mathsf T}\pi_k=0.
\]
In particular, \(c_k=F_0\pi_k+F_1\pi_{k-1}\) for \(k\ge1\). For reproducible elimination, replace the last row of \(Q_0\) by ones, replace the last component of \(-Q_1\pi_{k-1}\) by zero, and solve the resulting \(6\times6\) linear system. Two exact rational eliminations yield the displayed \(c_1\) and \(c_2\). Both identities, including the fully factored numerator of \(c_2\), are checked symbolically by the independent-in-file verification program.

Since \(A,B>0\), the complete zero set of \(c_2\) is precisely the union \(\{a=1\}\cup\{b=1\}\cup\{a=b\}\cup\{ab=3\}\), with signs determined by the numerator product. The first three pieces are reflection-symmetric rate arrays, so reflection together with reversal of the drive conjugates their Markov generators and negates the oriented current. This proves exact oddness on these pieces, not merely quadratic cancellation.

**3. Quartic lifting on the nongeometric curve.** For \(ab=3\), substitute \(b=3/a\) directly into the same six-state generator and solve the normalized stationary linear system over rational functions of \((a,\varepsilon)\). Extract the fourth Taylor coefficient of \((F_0+\varepsilon F_1)\pi\) at \(\varepsilon=0\); exact cancellation gives
\[
\frac{1}{24}\left.\frac{\partial^4J_{a,3/a}}{\partial\varepsilon^4}\right|_{\varepsilon=0}
=\frac{12a^2(a-3)(a-1)(a^2-3)}{(a^2+2a+3)^2(3a^2+4a+9)^2}.
\]
This is a rational-polynomial identity, rather than a numerical interpolation. Its positive denominator and complete numerator factorization show that its only positive zeros are \(a=1,\sqrt3,3\), exactly the reflection-symmetric points on the curve. For every other positive \(a\), the coefficient is nonzero. Analyticity then gives the asserted quartic leading even term, with next even remainder \(O(\varepsilon^6)\).

**4. Nongeometric character.** When \(a,b\ne1\) and \(a\ne b\), all three values \(a,b,1\) are distinct. Uniformity of the bond ratio \(p_i/q_{i+1}\) would require \(w_i/w_{i+1}\) constant, and cyclic positivity then makes all four rates equal, which is impossible here. Even the weaker published inversion-correspondence condition, allowing a per-site choice between the two reflected indices, fails: its possible reflection centers are \(k=0,1,2,3\); choosing offsets \(i=1,1,3,1\), respectively, gives unequal rate values for both allowed reflected targets in each case. Thus the extra surface \(ab=3\) cannot be attributed to either named sufficient symmetry condition.

As an exact witness, take \(a=2\), \(b=3/2\). Direct elimination gives
\[
J_{2,3/2}(\varepsilon)=
\frac{12\varepsilon(\varepsilon-11)(\varepsilon+11)(1+\varepsilon^2)}{4\varepsilon^5-13\varepsilon^4-4\varepsilon^3-3486\varepsilon^2-3509},
\]
whose quadratic coefficient is zero while its fourth coefficient is \(-48/101761\). The full current is therefore not odd despite its zero quadratic response.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The executable independently builds all six-state allowed-hop transition matrices, checks their column sums, solves the normalized stationary perturbation equations, verifies the symbolic formulas for both leading coefficients, substitutes the entire \(ab=3\) curve into the *full* finite generator to verify the fourth coefficient, and checks the rational witness. It also compares 18 exact stationary currents with an independent Markov-chain tree-minor determinant construction using positive rational rates and biases. The verification involves no random sampling or approximate floating-point equality.

All symbolic identities were checked with exact rational polynomial cancellation. The finite-state derivation is exhaustive because the system has exactly \(\binom42=6\) possible configurations. Generalizations to larger rings or higher particle number are not established here.

## Relationship to prior work

Sakai and Akimoto introduced the site-dependent exclusion model and conjectured that a nonzero quadratic bias coefficient occurs whenever neither of their two structural sufficient conditions holds. Their paper gives nonlinear-response and inversion-correspondence arguments but does not supply this complete two-contrast coefficient factorization or quartic-onset classification.

A subsequent public mathematical record, *A disordered exclusion ring whose \(\varepsilon^2\) current response vanishes although neither symmetry condition holds*, already constructs a different exact four-site, two-particle counterexample with rate vector \((2,4,3,41)\). Consequently **the general refutation and the mere existence of nonsymmetric quadratic cancellation are prior results**. The present claim is strictly the new two-parameter sign/zero classification and the universal quartic lift on its nongeometric cancellation curve. The earlier witness does not imply the exact factor \((a-1)(a-b)(b-1)(ab-3)\), the complete classification, or the nonzero fourth-order coefficient for every nonsymmetric point on \(ab=3\).

Sakai and Akimoto's later boundary-driven exclusion paper discusses possible cancellations of nonlinear terms in open systems; it neither studies this periodic four-site ensemble nor determines its exact response-stratification surface. Standard finite Markov-chain stationary-solvers supply a method, but not these evaluated and factored parameter relations.

## Limitations

The result applies only to four sites, two particles and the displayed two-adjacent-contrast trap family. It does not classify arbitrary four-site rate quadruples, arbitrary densities, higher-dimensional lattices or disorder averages. The classification is for a Taylor expansion around zero bias; finite-bias sign crossings are not classified. The quartic coefficient is nonzero at every non-reflective point of \(ab=3\), but its numerical magnitude may be small. The stationary state is exact for the stated classical Markov process, not an approximation to a physical microscopic reservoir model.

The strongest originality risk is the extensive existing literature on finite-state exclusion and an independent previously published counterexample to the same conjecture. No claim is made to be first to refute that conjecture. Independent priority checking of the specific full classification has not been performed.

## References

1. I. Sakai and T. Akimoto, *Symmetry breaking of current response in disordered exclusion processes*, arXiv:2512.03316, first public 2025-12-03, later Phys. Rev. E **113**, 044123 (2026). https://arxiv.org/pdf/2512.03316
2. *A disordered exclusion ring whose \(\varepsilon^2\) current response vanishes although neither symmetry condition holds*, publicly accessible problem dossier and accompanying result. https://www.trureturing.org/research/sakai-akimoto-2026-disordered-exclusion-quadratic-response/
3. I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560, first public 2026-09-03. https://arxiv.org/abs/2609.03560
4. I. Sakai and T. Akimoto, *Unexpected effects of disorder on current fluctuations in the symmetric simple exclusion process*, arXiv:2408.11364, first public 2024-08. https://arxiv.org/abs/2408.11364
