# A sharp bit-flip threshold for discounted return peaks of finite cat maps

## Finding
For any even \(N\ge2\), an additive two-point Bernoulli perturbation of the finite Arnol'd cat map has a **sharp two-center transition** in its discounted self-return Green diagonal. For flip probability \(\varepsilon<1/2\), the unique maximum is the linear fixed point \(0\); for \(\varepsilon>1/2\), it is the affine fixed point \(z=(N/2,N/2)\); at the exact threshold both and only those points maximize. The threshold and the strict gap estimates hold for **every** discount \(0<\alpha<1\) and all even grid sizes.

## Assumptions and scope
Let \(N\) be an even integer, \(N\ge2\), and set \(G=(\mathbb Z/N\mathbb Z)^2\) with additive notation. Define
\[
A=\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad v=(N/2,0),\quad z=(N/2,N/2).
\]
Both coordinates are residue classes modulo \(N\). Let \(B_t\) be independent Bernoulli variables with \(\Pr(B_t=1)=\varepsilon\), where \(0\le\varepsilon\le1\). Consider the stochastic map
\[
X_{t+1}=AX_t+B_tv\pmod N.
\]
Denote its transition matrix by \(P_\varepsilon\), acting on row probabilities, and fix \(0<\alpha<1\). The *discounted return diagonal* is
\[
L_\varepsilon(x)=\bigl[(I-\alpha P_\varepsilon)^{-1}\bigr]_{x,x}
=\sum_{t=0}^{\infty}\alpha^t\Pr_x(X_t=x).
\]
The series converges absolutely, including at the degenerate endpoints \(\varepsilon=0,1\).

**Theorem.** The maximizers and quantitative gaps are exactly as follows.

1. If \(0\le\varepsilon<1/2\), the sole maximizer is \(0\), with
\[
L_\varepsilon(0)-L_\varepsilon(x)\ge\alpha(1-2\varepsilon)>0\quad(x\ne0).
\]
2. If \(\varepsilon=1/2\), the maximizers are precisely \(0\) and \(z\), their values are equal, and
\[
L_{1/2}(0)-L_{1/2}(x)\ge\alpha/2\quad(x\notin\{0,z\}).
\]
3. If \(1/2<\varepsilon\le1\), the sole maximizer is \(z\), with
\[
L_\varepsilon(z)-L_\varepsilon(x)\ge\alpha(2\varepsilon-1)>0\quad(x\ne z).
\]
For every \(\varepsilon\in[0,1]\), the exact translation duality holds:
\[
L_\varepsilon(x)=L_{1-\varepsilon}(x-z).
\]

## Proof
**Fourier-positive accumulated noise.** The matrix \(A\) is an automorphism of \(G\) since \(\det A=1\). For \(t\ge1\), iterating the chain gives
\[
X_t=A^t x+W_t,\quad
W_t=\sum_{j=0}^{t-1}A^{t-1-j}B_jv.
\]
Let \(\eta_t\) be the probability law of \(W_t\). For a character \(\chi\) of the finite abelian group \(G\), independence yields
\[
\widehat\eta_t(\chi)=\prod_{j=0}^{t-1}
\bigl[(1-\varepsilon)+\varepsilon\chi(A^jv)\bigr].
\]
Because \(2v=0\), every \(A^jv\) is an involution, and hence each character value \(\chi(A^jv)\) is \(1\) or \(-1\). If \(0\le\varepsilon\le1/2\), every factor is nonnegative real (equal to \(1\) or \(1-2\varepsilon\)), so \(\widehat\eta_t(\chi)\ge0\). Fourier inversion and pairing conjugate characters therefore imply, for every \(w\in G\),
\[
\eta_t(0)-\eta_t(w)
=\frac1{|G|}\sum_{\chi\in\widehat G}
\widehat\eta_t(\chi)\bigl(1-\Re\chi(w)\bigr)\ge0.
\]
It follows from the return condition \(W_t=(I-A^t)x\) that
\[
\Pr_x(X_t=x)=\eta_t((I-A^t)x)\le\eta_t(0)=\Pr_0(X_t=0)
\]
for every \(x\) and every integer \(t\ge1\). (At \(t=0\), both return probabilities equal \(1\).) Consequently, \(L_\varepsilon(0)\ge L_\varepsilon(x)\) for all \(x\).

**Strictness from a single step.** Since
\[
I-A=\begin{pmatrix}0&-1\\-1&-1\end{pmatrix},\quad \det(I-A)=-1,
\]
the map \(I-A\) is invertible modulo every \(N\). The one-step return equation \((I-A)x=B_0v\) has exactly two possible solutions: \(x=0\) when \(B_0=0\), and \(x=z\) when \(B_0=1\), as direct multiplication gives \((I-A)z=v\). They are distinct. Hence
\[
\Pr_0(X_1=0)=1-\varepsilon,\quad
\Pr_z(X_1=z)=\varepsilon,\quad
\Pr_x(X_1=x)=0\quad(x\notin\{0,z\}).
\]
For \(\varepsilon<1/2\), comparing the \(t=1\) term gives at least \(\alpha(1-2\varepsilon)\) against \(z\) and at least \(\alpha(1-\varepsilon)\) against any other point. Higher-time differences are nonnegative by the preceding lemma, proving the first assertion. At \(\varepsilon=1/2\), it gives an \(\alpha/2\) gap over every point other than \(0,z\).

**Affine duality and the critical tie.** We have \(Az+v=z\); also \(-v=v\) because \(2v=0\). After translating by \(z\), the process \(Y_t=X_t-z\) satisfies
\[
Y_{t+1}=AY_t+(B_t-1)v=AY_t+(1-B_t)v.
\]
Thus its noise has flip probability \(1-\varepsilon\), and the whole transition matrix is conjugated by the translation \(x\mapsto x-z\). In particular,
\[
L_\varepsilon(x)=L_{1-\varepsilon}(x-z).
\]
At \(\varepsilon=1/2\), the inequality already proved for \(0\) implies that it maximizes, and translation duality makes \(z\) attain the identical value. The strict one-step gap excludes all others. For \(\varepsilon>1/2\), apply the proved \(\varepsilon'<1/2\) case to \(\varepsilon'=1-\varepsilon\) and translate; the claimed unique peak and gap follow. This completes the proof.

The same argument proves a more general lemma for any finite abelian group with an automorphism \(T\) for which \(I-T\) is bijective and any nonzero order-two noise vector \(v\): the two maximizers are the fixed points of \(T\) and \(x\mapsto Tx+v\), with the same threshold and bounds.

## Verification
The included `verify.py` uses only the Python standard library and computes exact rational resolvents by Gauss–Jordan inversion for all \(20\) combinations \(N\in\{2,4\}\), \(\varepsilon\in\{0,1/4,1/2,3/4,1\}\), \(\alpha\in\{1/3,3/4\}\). It checks maximizers, the strict lower gaps, and the translation duality entry by entry. For \(N=2\), it independently tests the exact identity
\[
L_\varepsilon(0)-L_\varepsilon(z)=\frac{\alpha(1+\alpha)(1-2\varepsilon)}{1-\alpha^3(1-2\varepsilon)^2}
\]
for all ten rational parameter pairs. Fourier positivity is separately checked at twelve modulus–noise choices. Run `python verify.py` to reproduce the checks. This finite test corroborates but does not replace the all-modulus analytic proof.

## Relationship to prior work
Chandra's *Arithmetic Landscape Functions of a Discrete Cat Map* (first public version July 26, 2026) studies **deterministic** discrete cat-map resolvents and identifies the unperturbed zero peak via periodic orbits. Its revised October 2026 full text was examined, including its definitions, main results and appendices. The first public abstract also mentioned a first-order Laplacian perturbation; this is not an exact involutive Bernoulli perturbation or its all-parameter peak-switch classification. That deterministic formula cannot directly supply the Bernoulli-noise threshold, its non-deterministic Green diagonal, or the critical two-center tie. The present argument replaces deterministic orbit-length comparisons with Fourier positivity of an accumulated involutive noise law and an affine parameter-complement conjugacy. Yarmola's earlier random-perturbed cat-map work treats a continuous torus with curve-supported random jumps; its complete arXiv HTML text proves line-supported invariant-measure attraction rather than finite-grid discounted-return Green maxima.

The Fourier inversion positivity argument and basic character facts are standard, and the result does not assert those tools as novel. The novel proposed synthesis is the **universal sharp noise threshold, the complete maximizer classification, and the uniform strict gap for every even grid and discount**. Searches of nearby published findings and open scientific literature found no equivalent statement; lack of a search match is not a proof of historical priority.

## Limitations
The theorem is specific to an order-two additive noise increment and even finite tori, with all randomness independent across time and the exact row-transition convention stated above. It does not assert analogous universal thresholds for general noise distributions, odd moduli, continuous tori, non-involutive increments, or finite-time mixing. The exact one-step lower bounds need not be optimal for every grid or discount. Independent scientific review and definitive historical-priority assessment have not been performed.

## References
1. Aryaman Chandra, *Arithmetic Landscape Functions of a Discrete Cat Map*, arXiv:2607.24857v1 (first public 2026-07-26), revised v2 (2026-10-29); https://arxiv.org/abs/2607.24857.
2. Tatiana Yarmola, *A Pathological Random Perturbation of the Cat Map*, arXiv:1301.4413; https://arxiv.org/abs/1301.4413.
