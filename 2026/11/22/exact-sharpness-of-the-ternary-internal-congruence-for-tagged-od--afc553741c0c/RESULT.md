# Exact sharpness of the ternary internal congruence for tagged odd-part partitions

## Finding

Let \(T(n)=\mathrm{PDO}_{\mathrm t}(n)\) be the total number of tagged parts over all odd-part partitions with designated summands, and let \(T(0)=0\). For each integer \(m\ge 0\), form
\[
D_m=T(12\cdot3^{m+1})T(24\cdot3^m)-T(12\cdot3^m)T(24\cdot3^{m+1}).
\]
Then
\[
\boxed{\nu_3(D_m)=2m+7,\qquad D_m/3^{2m+7}\equiv(-1)^{m+1}\pmod3.}
\]
In particular, for every \(m\ge0\), the **greatest** integer \(e\) for which there exists an integer \(c\), independent of \(n\), such that
\[
T(12\cdot3^{m+1}n)\equiv cT(12\cdot3^m n)\pmod{3^e}\quad\text{for every }n\ge0,
\]
is exactly \(\boxed{e=m+5}\). This optimal exponent is achieved by \(c=3\mu_m\) with \(\mu_m=5\) for even \(m\) and \(\mu_m=8\) for odd \(m\), as established by Li and Tang. The new assertion is the all-depth sharpness and leading-unit law.

## Assumptions and scope

All quantities are ordinary integers; \(m,n\) range over **all** nonnegative integers, and \(\nu_3(0)=+\infty\). In a designated-summand partition, exactly one occurrence of each distinct part size is tagged. Only odd part sizes are permitted; \(T(n)\) sums the number of tagged parts across all such partitions of \(n\). The generating function, due to Lin, is
\[
\sum_{n\ge0}T(n)q^n=q\frac{E(q^2)E(q^3)^2E(q^{12})^2}{E(q)^2E(q^6)},\qquad E(q)=\prod_{j\ge1}(1-q^j).
\]
The proof uses the exactly specified coefficient extraction and the all-index coefficient-vector valuation inequality proved in Li–Tang (2026), Theorem 3.2 and Lemmas 4.4 and 5.2(ii). These cited results are inputs, not new discoveries.

## Proof

**1. Coefficient vectors and a determinant.** Set
\[
\vartheta(q)=\frac{E(q^2)^8E(q^3)^5}{E(q)^7E(q^6)^4},\qquad
\xi(q)=q\frac{E(q^2)E(q^6)^5}{E(q)^5E(q^3)}.
\]
Both are integral formal power series, with \(\vartheta(0)=1\) and \(\xi(q)=q+O(q^2)\). Li–Tang's Theorem 3.2 gives
\[
\sum_{n\ge0}T(12\cdot3^mn)q^n=\vartheta(q)\sum_{j\ge1}y_{m,j}\xi(q)^j,
\qquad \mathbf y_{m+1}=\mathbf y_m B,
\]
where \(\mathbf y_0=(144,1728,0,\ldots)\) and \(B=(\Psi_{i,j})\) is an integer matrix with finite row support at each level. Reading the first two coefficients, for a fixed integer \(h=[q^2](\vartheta\xi)\), yields
\[
T(12\cdot3^m)=y_{m,1},\qquad T(24\cdot3^m)=h y_{m,1}+y_{m,2}.
\]
Define the alternating coefficient minors
\[
\Lambda^m_{k,\ell}=y_{m+1,k}y_{m,\ell}-y_{m,k}y_{m+1,\ell}.
\]
It follows identically that \(D_m=-\Lambda^m_{2,1}\). Thus there is no unstated analytic limit involved in transferring the coefficient result.

**2. Source valuation bound and the new strict leading-term check.** Define
\[
u_3(0)=+\infty,\qquad u_1=0,\qquad u_j=\left\lfloor\frac{3j-4}{2}\right\rfloor\quad(j\ge2).
\]
Li–Tang's Lemma 5.2(ii), with its proof based on their coefficient-matrix valuation bound and antisymmetric recurrence, establishes for **every** \(m\ge0\) and \(k>\ell\ge1\)
\[
\nu_3(\Lambda^m_{k,\ell})\ge 2m+6+u_k+u_\ell.
\]
Their Theorem 3.2 and Appendix give the following two columns of \(B\), in row order, with all later rows zero:
\[
(\Psi_{i,1})_{i=1}^6=(81,17,1,0,0,0),\qquad
(\Psi_{i,2})_{i=1}^6=(5256,5985,2274,393,32,1).
\]
For \(1\le\ell<k\le6\), set \(\Delta_{k,\ell}=\Psi_{\ell,1}\Psi_{k,2}-\Psi_{\ell,2}\Psi_{k,1}\). A finite calculation **independent of any conjectural stability assumption** gives
\[
\Delta_{2,1}=395433=9\cdot43937,\qquad 43937\equiv-1\pmod3,
\]
and the sharp strict gap
\[
\nu_3(\Delta_{k,\ell})+u_k+u_\ell\ge4
\quad\text{for }1\le\ell<k\le6,\ (k,\ell)\ne(2,1).
\]
The complete finite check is implemented and asserted in `verify_sharpness.py`; no table outside the package is needed. The number \(4\) is strictly larger than the leading pair's weighted valuation \(\nu_3(\Delta_{2,1})+u_2+u_1=3\).

**3. Exact all-depth minor valuation.** The matrix recurrence implies, after antisymmetrizing,
\[
\Lambda^{m+1}_{2,1}=\sum_{k>\ell\ge1}\Lambda^m_{k,\ell}\Delta_{k,\ell}.
\]
Only the fifteen pairs \(1\le\ell<k\le6\) contribute, because both relevant columns vanish thereafter. Li–Tang compute the initial first coordinates \(y_{1,1}=1520\cdot3^3\) and \(y_{1,2}=137024\cdot3^4\); direct substitution into \(\mathbf y_0\) verifies
\[
\Lambda^0_{2,1}=698368\cdot3^7,\qquad 698368\equiv1\pmod3.
\]
Assume inductively that \(\nu_3(\Lambda^m_{2,1})=2m+7\). The unique term \((k,\ell)=(2,1)\) has valuation \(2m+9\); every other term has valuation at least \(2m+10\) by the cited *all-index* minor bound and the new strict finite gap. Therefore cancellation of the minimal term is impossible and
\[
\Lambda^{m+1}_{2,1}\equiv395433\,\Lambda^m_{2,1}\pmod{3^{2m+10}}.
\]
Consequently \(\nu_3(\Lambda^{m+1}_{2,1})=2m+9\) and
\[
\frac{\Lambda^{m+1}_{2,1}}{3^{2m+9}}\equiv
43937\frac{\Lambda^m_{2,1}}{3^{2m+7}}\equiv
-\frac{\Lambda^m_{2,1}}{3^{2m+7}}\pmod3.
\]
The base case proves \(\Lambda^m_{2,1}/3^{2m+7}\equiv(-1)^m\pmod3\) for all \(m\ge0\). Since \(D_m=-\Lambda^m_{2,1}\), this establishes both boxed determinant identities.

**4. Optimality for every integer multiplier.** Li–Tang's Theorem 1.2(ii) proves the existence of an integer multiplier \(c=3\mu_m\) giving the congruence modulo \(3^{m+5}\) for all \(n\). Suppose instead that an integer \(c\), not necessarily divisible by three, worked modulo \(3^{m+6}\). Apply this hypothesis at \(n=1,2\), write the two errors as multiples of \(3^{m+6}\), and eliminate \(c\) using the determinant \(D_m\). Their Theorem 1.1 gives \(3^{m+2}\mid T(12\cdot3^m)\) and \(3^{m+2}\mid T(24\cdot3^m)\), so this elimination forces \(3^{2m+8}\mid D_m\), contradicting \(\nu_3(D_m)=2m+7\). This rules out all stronger exponents, uniformly over all possible integer multipliers. \(\square\)

## Verification

Run `python3 verify_sharpness.py` using the complete companion file in this package. It verifies all finite first-two-column minors (the unique low-weight term and eleven nonzero strict alternatives), the exact initial minor, and independently expands Lin's integer-coefficient eta-quotient modulo \(3^{30}\) through index \(648\). The latter checks the determinant law and the cited internal congruence at \(m=0,1,2\) with both \(n=1\) and \(n=2\). The infinite assertion depends on the fully quantified, published Li–Tang minor bound and the induction in Section 3 above; finite coefficient tests are not its proof.

## Relationship to prior work

Li and Tang (arXiv:2611.15164v1, Theorems 1.2(ii), 3.2 and Lemma 5.2(ii)) prove the internal congruence modulo \(3^{m+5}\) and lower-bound all coefficient minors by \(3^{2m+6+u_k+u_\ell}\); their article does **not** assert equality at all levels, or optimality against arbitrary multipliers. Their initial minor and two matrix columns are used and credited here. The new strict finite exterior-square gap shows equality persists for the specific minor at **every** level and provides the coefficient leading-unit law. Singh and Barman (2023) investigate the same partition statistic but establish small-depth congruences and different progressions rather than this all-depth optimal internal modulus. Lin (2018) defines the tagged-part statistic and its generating function. The analogous \(8\cdot3^m\) progression uses a *different* coefficient matrix, so it does not logically imply the present \(12\cdot3^m\) result.

## Limitations

This is a result specifically for the \(12\cdot3^m\) progression and universal integer multipliers; it does not classify the optimal exponents for the separate \(8\cdot3^m\) progression or other shifted progressions. The proof relies on the published Li–Tang coefficient-vector bound and explicitly supplied first two matrix columns. The priority search is not an exhaustive proof of novelty, and independent mathematical validation has not been performed.

## References

1. Xingyi Li and Dazhao Tang, *Congruence properties modulo powers of 3 for designated summands in partitions into odd parts*, arXiv:2611.15164v1 (first submitted 2026-11-11), https://arxiv.org/html/2611.15164v1 . Theorems 1.1, 1.2(ii), 3.2; Lemmas 4.4 and 5.2; Appendix A.
2. Gurinder Singh and Rupam Barman, *Congruences for the partition function PDO_t(n) modulo powers of 2 and 3*, arXiv:2307.04687v1 (2023), https://arxiv.org/abs/2307.04687 .
3. Bernard L. S. Lin, *The number of tagged parts over the partitions with designated summands*, Journal of Number Theory **184** (2018), 216–234; DOI:10.1016/j.jnt.2017.08.020 .
