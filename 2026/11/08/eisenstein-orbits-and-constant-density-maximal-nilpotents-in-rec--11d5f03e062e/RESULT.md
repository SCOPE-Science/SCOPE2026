# Eisenstein orbits and constant-density maximal nilpotents in rectangular Jordan centralizers

## Finding
Fix a finite field \(\mathbb F_q\), integers \(n\ge2\) and \(r\ge1\), and the nilpotent operator \(B=J_n^{\oplus r}\) on \(\mathbb F_q^{rn}\). Write \(\mathcal C(B)\) for its full matrix centralizer, \(\mathcal N(B)\) for its nilpotent elements, and \(\mathcal R(B)\subseteq\mathcal N(B)\) for those with **one Jordan block of length \(rn\)**. Then
\[
|\mathcal N(B)|=q^{nr^2-r},\qquad
|\mathcal R(B)|=|\mathrm{GL}_r(\mathbb F_q)|q^{r^2(n-1)-r},
\qquad
\frac{|\mathcal R(B)|}{|\mathcal N(B)|}=\prod_{i=1}^{r}(1-q^{-i}).
\]
Thus the conditional maximal-Jordan-block density is exactly independent of the common block length \(n\ge2\), in every characteristic.

There is a simultaneous exact orbit classification. The invertible centralizer of \(B\) acts by conjugation on \(\mathcal R(B)\); two elements are conjugate if and only if their characteristic polynomials over the truncated-polynomial ring agree. These polynomials are precisely the monic Eisenstein polynomials of degree \(r\) for the parameter \(t\). There are exactly
\[
(q-1)q^{r(n-1)-1}
\]
conjugacy classes, each of cardinality
\[
\frac{|\mathrm{GL}_r(\mathbb F_q)|q^{r^2(n-1)}}{(q-1)q^{rn-1}}.
\]

## Assumptions and scope
Let \(R=\mathbb F_q[t]/(t^n)\), with \(n\ge2\). Identifying \(\mathbb F_q^{rn}\) with the free \(R\)-module \(R^r\), the matrix \(B\) acts as multiplication by \(t\), so \(\mathcal C(B)\cong M_r(R)\) and its invertible part is \(\mathrm{GL}_r(R)\). The nilpotency and Jordan forms are taken over the ground field \(\mathbb F_q\), whereas characteristic polynomials and conjugacy representatives are taken over \(R\). A monic degree-\(r\) polynomial
\[
p(X)=X^r+c_{r-1}X^{r-1}+\cdots+c_1X+c_0\in R[X]
\]
is *Eisenstein at \(t\)* if \(c_i\in tR\) for every \(i\) and \(c_0\in tR\setminus t^2R\). In particular, this definition applies when \(n=2\).

## Proof
**1. Reduction detects nilpotence.** Let \(A=A_0+tA_1+\cdots+t^{n-1}A_{n-1}\in M_r(R)\), with \(A_i\in M_r(\mathbb F_q)\). If \(A\) is nilpotent, so is its reduction \(A_0\). Conversely, if \(A_0\) is nilpotent, \(A^r\in tM_r(R)\), whence \(A^{rn}=0\). Thus nilpotence is equivalent to that of \(A_0\), and every nilpotent reduction has exactly \(q^{r^2(n-1)}\) lifts. The classical finite-field nilpotent-matrix count (Fine–Herstein, also given a self-contained proof by Leinster) is \(q^{r^2-r}\). Therefore \(|\mathcal N(B)|=q^{nr^2-r}\).

**2. The maximal-Jordan criterion.** A nilpotent \(\mathbb F_q\)-linear endomorphism on \(\mathbb F_q^{rn}\) has one Jordan block if and only if its kernel has \(\mathbb F_q\)-dimension one. Smith normal form over the principal chain ring \(R\) writes any \(A\), up to independent invertible left and right multipliers, as \(\operatorname{diag}(t^{a_1},\ldots,t^{a_r})\), where \(0\le a_i\le n\), with \(t^n=0\). Because the kernel of multiplication by \(t^{a_i}\) on \(R\) has \(\mathbb F_q\)-dimension \(a_i\), we have
\[
\dim_{\mathbb F_q}\ker A=\sum_{i=1}^{r}a_i.
\]
This is one exactly when \(r-1\) Smith factors are units and the last factor has valuation one. Equivalently, \(A_0\) has rank \(r-1\), and the coefficient of \(t\) in \(\det_R(A)\) is nonzero. Among nilpotent \(r\times r\) reductions, rank \(r-1\) is equivalent to having one Jordan block \(J_r\). This proves the stated structural criterion.

**3. Exact cardinality.** The number of regular nilpotent reductions is the size of the similarity class of \(J_r\), namely
\[
\frac{|\mathrm{GL}_r(\mathbb F_q)|}{(q-1)q^{r-1}},
\]
since the invertible matrices commuting with \(J_r\) are the units of \(\mathbb F_q[J_r]\cong\mathbb F_q[s]/(s^r)\). Fix such a reduction \(A_0\). The coefficient of \(t\) in \(\det(A_0+tA_1+\cdots)\) is \(\operatorname{tr}(\operatorname{adj}(A_0)A_1)\). This is a **nonzero linear functional** of \(A_1\), since \(A_0\) has rank \(r-1\), and therefore \(\operatorname{adj}(A_0)\ne0\) (also true for \(r=1\)). Exactly \((q-1)q^{r^2-1}\) possibilities for \(A_1\) make this coefficient nonzero. All \(r^2(n-2)\) higher coefficients are unrestricted. Multiplication gives
\[
|\mathcal R(B)|=
\frac{|\mathrm{GL}_r(\mathbb F_q)|}{(q-1)q^{r-1}}(q-1)q^{r^2-1}q^{r^2(n-2)}
=|\mathrm{GL}_r(\mathbb F_q)|q^{r^2(n-1)-r}.
\]
Dividing by the count in step 1 and using \(|\mathrm{GL}_r(\mathbb F_q)|=q^{r^2}\prod_{i=1}^{r}(1-q^{-i})\) yields the constant-density formula.

**4. Eisenstein characteristic polynomials.** For \(A\in\mathcal R(B)\), the reduction \(A_0\sim J_r\) implies \(\chi_A(X)\equiv X^r\pmod t\). The constant coefficient \((-1)^r\det A\) has valuation precisely one by step 2, so \(\chi_A\) is Eisenstein. Conversely, if \(\chi_A\) is Eisenstein, its reduction is \(X^r\) and \(\det A\) has valuation one. In particular, its reduction has rank at least \(r-1\); since it is nilpotent, its rank is exactly \(r-1\), and step 2 applies.

A regular nilpotent \(A_0\) has a cyclic vector over \(\mathbb F_q\). Lifting that vector to \(R^r\), its first \(r\) iterates under \(A\) form an \(R\)-basis by reduction modulo \(t\) and Nakayama's lemma. Thus \(A\) is conjugate under \(\mathrm{GL}_r(R)\) to the companion matrix of \(\chi_A\). Conversely, the companion matrix of every Eisenstein degree-\(r\) polynomial has a regular nilpotent reduction and determinant valuation one. Hence the characteristic polynomial indexes the conjugacy classes bijectively.

**5. Uniform orbit sizes.** Since \(A\in\mathcal R(B)\) has Jordan type \((rn)\) as an \(\mathbb F_q\)-linear operator, its full matrix centralizer in \(M_{rn}(\mathbb F_q)\) is \(\mathbb F_q[A]\cong\mathbb F_q[s]/(s^{rn})\). Because \(AB=BA\), also \(B\in\mathbb F_q[A]\), so this entire algebra already commutes with \(B\) and is the centralizer of \(A\) inside \(M_r(R)\). The stabilizer of \(A\) in \(\mathrm{GL}_r(R)\) therefore has cardinality \((q-1)q^{rn-1}\). As \(|\mathrm{GL}_r(R)|=|\mathrm{GL}_r(\mathbb F_q)|q^{r^2(n-1)}\), orbit–stabilizer yields the asserted common orbit size.

Finally, there are \(q^{n-1}\) choices for each of the \(r-1\) nonconstant nonleading coefficients of an Eisenstein polynomial, and \((q-1)q^{n-2}\) choices for its constant coefficient. The number of classes is therefore \((q-1)q^{r(n-1)-1}\). Their sizes sum to \(|\mathcal R(B)|\), giving an independent consistency identity.

## Verification
The standalone `verify_power.py` exhaustively enumerates \(R\)-matrices in five small cases, independently computes each matrix power in \(M_r(R)\), and counts nilpotent elements and those with index exactly \(rn\). It checks \((q,r,n)=(2,2,1),(2,2,2),(2,2,3),(3,2,2),(2,3,2)\). In the final four of these, the observed \((|\mathcal N(B)|,|\mathcal R(B)|)\) are respectively \((64,24),(1024,384),(729,432),(32768,10752)\). The first case checks the separate \(n=1\) boundary.

The independent `verify_orbits.py` enumerates all invertible \(2\times2\) matrices over \(R\) and reconstructs the complete conjugation orbit of every Eisenstein companion. For \((q,n)=(2,2),(2,3),(3,2)\), the numbers of orbits and their common sizes are respectively \((2,12),(8,48),(6,72)\). Their disjoint union exhausts the regular-nilpotent matrices. Both programs terminate with `VERIFY_OK` when run directly.

These checks are finite examples, not substitutes for the proof over all prime-power fields, block multiplicities, or truncation lengths.

## Relationship to prior work
Bogdanić, Đurić, Koljančić, Oblak, and Šivic classify which nilpotent Jordan types can occur in the centralizer of two equal nilpotent blocks, using the description of that centralizer as a matrix ring over truncated polynomials. Their classification concerns *possible partitions*, not the finite-field cardinality of the single-block stratum or its rational conjugacy orbits. The present result also permits arbitrary numbers of equal blocks.

Britnell and Wildon analyze commuting similarity classes over finite fields and characterize which Jordan classes can commute; this establishes existence phenomena rather than the present full fiber counts. Leinster provides a proof of the classical nilpotent-matrix count used in step 1; that count is not claimed new.

A publicly available finite-dual-number calculation, *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers* (2026), counts maximal-index lifts above a **fixed** regular Jordan reduction when \(n=2\). That fixed-reduction special case agrees with step 3 and is expressly **excluded** from any novelty assertion. Here the additional all-thickness \(n\ge3\) count and full Eisenstein-orbit classification are the claimed refinement. Literature and mathematical-record searches did not identify a statement covering this whole conjunction; absence in searches alone cannot prove publication priority.

## Limitations
The block sizes of \(B\) must all be equal, and the count addresses **only** the maximal single-Jordan-block stratum of its nilpotent centralizer. No claim is made for arbitrary nilpotent Jordan partitions of the commuting matrix or arbitrary unequal block sizes of \(B\). The result uses finite fields for cardinalities; the structural Eisenstein and companion arguments apply in a wider local-ring setting, but no general quantitative extension is asserted. This is an exact proof with limited computational cross-checks, not an independently audited result. Specialized existing theories of Eisenstein matrix conjugacy or regular elements of finite chain-ring matrices may contain an equivalent enumeration; publication priority remains provisional.

## References
1. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425v1, first posted 2022-12-16; later Linear Algebra and its Applications, DOI 10.1016/j.laa.2024.03.008.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (2010), Journal of the London Mathematical Society 83 (2011), 470–492.
3. T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562 (2019), supplying an elementary proof of the classical Fine–Herstein enumeration.
4. *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers*, public mathematical research record (2026), published-finding corpus record `2026/10/4/SCOPE-exact-nilpotency-index-distribution-for-jordan-lifts-over-finite--a669645ca0b7`; comparison only, with its special case excluded from the claim of novelty.
