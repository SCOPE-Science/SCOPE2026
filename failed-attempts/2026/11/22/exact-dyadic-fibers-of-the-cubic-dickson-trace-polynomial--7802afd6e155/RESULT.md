# Exact dyadic fibers of the cubic Dickson trace polynomial

## Finding

Let \(F(X)=D_3(X,1)=X^3-3X\), the degree-three Dickson polynomial of the first kind with parameter one. For every integer \(k\ge4\) and every residue \(y\) modulo \(2^k\), put
\[
N_k(y)=\#\{x\pmod{2^k}:F(x)\equiv y\pmod{2^k}\}.
\]
The following explicit formula determines **every** fiber \(N_k(y)\), including all singular fibers.

For \(\epsilon\in\{+,-\}\), set \(z_+(y)=y+2\) and \(z_-(y)=y-2\), and for integer \(r\ge2\) set
\[
c_{+,r}=\begin{cases}7,&r=2,\\3,&r\ge3,\end{cases}
\qquad
c_{-,r}=\begin{cases}1,&r=2,\\5,&r\ge3.\end{cases}
\]
Define \(H_{\epsilon,k}(z)\) by the following exhaustive cases, with every congruence interpreted modulo \(2^k\):
\[
H_{\epsilon,k}(z)=\begin{cases}
2^{\lfloor k/2\rfloor},&z\equiv0\pmod{2^k},\\
2^{\min\{k-r-1,r+2\}},
 &\begin{gathered} \nu_2(z)=2r<k,\ r\ge2,\ m=k-2r,\\
 (z/2^{2r})\equiv c_{\epsilon,r}\pmod{2^{\min\{3,m\}}},\end{gathered}\\
0,&\text{otherwise}.
\end{cases}
\]
Here the valuation and unit of a nonzero residue modulo \(2^k\) are well defined because \(\nu_2(z)<k\) in the second case. Then
\[
\boxed{N_k(y)=\begin{cases}
0,&y\text{ odd},\\
1+H_{+,k}(y+2)+H_{-,k}(y-2),&y\text{ even}.
\end{cases}}
\]
The two correction terms come from disjoint odd input classes \(1+4\mathbb Z\) and \(-1+4\mathbb Z\). In particular, the image modulo every \(2^k\) consists of exactly the even residues, and its cardinality is \(2^{k-1}\). The least positive index period of \(F(n)\) modulo \(2^k\) is \(2^k\) for \(k\ge2\), and one for \(k=1\).

The formula has a stronger inverse-limit counterpart. In \(\mathbb Z_2\), introduce the disjoint sets
\[
\begin{aligned}
\mathcal C_+={}&\{-2\}\sqcup\bigl(-2+16(7+8\mathbb Z_2)\bigr)
\sqcup\bigsqcup_{r\ge3}\bigl(-2+2^{2r}(3+8\mathbb Z_2)\bigr),\\
\mathcal C_-={}&\{2\}\sqcup\bigl(2+16(1+8\mathbb Z_2)\bigr)
\sqcup\bigsqcup_{r\ge3}\bigl(2+2^{2r}(5+8\mathbb Z_2)\bigr).
\end{aligned}
\]
Every even \(y\in\mathbb Z_2\) has precisely one **even** preimage. An additional two **odd** preimages occur exactly when \(y\in(\mathcal C_+\cup\mathcal C_-)\setminus\{-2,2\}\); an additional one odd preimage occurs at each of \(y=-2\) and \(y=2\). No odd target has a preimage. Thus \(F(\mathbb Z_2)=2\mathbb Z_2\) and the target set with exactly three preimages has normalized Haar measure
\[
\boxed{\mu\{y:\#F^{-1}(y)=3\}=\frac1{48}}.
\]
There are exactly two exceptional targets with two preimages, namely \(\pm2\). The targets with exactly one preimage have measure \(23/48\), while the targets with no preimage have measure \(1/2\).

## Assumptions and scope

Inputs are all residues of \(\mathbb Z/2^k\mathbb Z\), without a unit restriction, and the target is any residue of the same ring. The polynomial parameter is exactly one, and its normalization is \(D_3(X,1)=X^3-3X=2T_3(X/2)\). The last identity is an identity over \(\mathbb Q[X]\): substituting \(X/2\) is **not** an invertible change of variables over \(\mathbb Z_2\). The displayed finite formula covers all \(k\ge4\); the image and period statements include the stated smaller precisions. Infinite fibers mean actual points of \(\mathbb Z_2\), not limits of the finite counts. Haar measure is normalized by \(\mu(\mathbb Z_2)=1\). The critical targets \(\pm2\) are distinguished because the discriminant of \(X^3-3X-y\) is \(27(4-y^2)\).

## Proof

**1. Even inputs are a complete isometric branch.** For all \(a,b\),
\[
F(a)-F(b)=(a-b)(a^2+ab+b^2-3).
\]
When \(a,b\) are even, the last factor is odd. Hence
\[
\nu_2(F(a)-F(b))=\nu_2(a-b)
\quad(a,b\in2\mathbb Z_2).
\]
For each \(k\), the map on even residues is injective and therefore bijective onto the even residues, since \(F(2u)\) is even. The inverse systems are compatible, so every even \(2\)-adic target has a unique even preimage. Moreover, \(F(x)=x(x^2-3)\) is even for every odd input as well, since \(x^2-3\) is even. All odd targets have zero preimages.

**2. Exact odd-input factorization and valuation shells.** Every odd \(x\) is in exactly one of \(1+4\mathbb Z_2\) or \(-1+4\mathbb Z_2\). The elementary identities
\[
F(x)+2=(x-1)^2(x+2),\qquad
F(x)-2=(x+1)^2(x-2)
\]
show that if \(x=1+2^r u\) with \(r\ge2\) and \(u\) odd, then
\[
F(x)+2=2^{2r}U_{+,r}(u),
\quad U_{+,r}(u)=u^2(3+2^r u),
\]
while if \(x=-1+2^r u\), then
\[
F(x)-2=2^{2r}U_{-,r}(u),
\quad U_{-,r}(u)=u^2(-3+2^r u).
\]
Both \(U_{\epsilon,r}(u)\) are odd. For \(r=2\), reduction modulo eight gives the fixed residues seven and one; for \(r\ge3\) it gives three and five. These are exactly the constants \(c_{\epsilon,r}\). Each noncenter odd input has output offset of valuation exactly \(2r\). The center inputs \(x=1\) and \(x=-1\) map to \(-2\) and \(2\), respectively.

**3. The two local branches cover the full prescribed unit ball exactly.** For odd \(u,v\) and \(a\in\{3,-3\}\),
\[
\begin{aligned}
&u^2(a+2^r u)-v^2(a+2^r v)\\
&\quad=(u-v)\bigl(a(u+v)+2^r(u^2+uv+v^2)\bigr).
\end{aligned}
\]
If \(u\equiv v\pmod4\) and \(r\ge2\), then \(\nu_2(u+v)=1\), and the parenthesized factor has valuation exactly one: its first summand has valuation one and its second has valuation at least two. Therefore on either fixed class \(u\equiv1\) or \(3\pmod4\),
\[
\nu_2(U_{\epsilon,r}(u)-U_{\epsilon,r}(v))
=\nu_2(u-v)+1.
\]
Each class maps into \(c_{\epsilon,r}+8\mathbb Z_2\). At precision \(2^m\) for \(m\ge3\), each class contains exactly \(2^{m-3}\) distinct images, because its \(2^{m-3}\) representatives modulo \(2^{m-1}\) have distinct images modulo \(2^m\). The target ball also contains exactly \(2^{m-3}\) residues; hence the restricted map is onto at every precision and, by compactness, bijective from each class onto the full ball in the inverse limit. The two input classes have identical images. Thus every point of that unit ball has exactly two odd-unit preimages \(u\), one from each class.

**4. All finite fibers.** Fix \(k\ge4\) and an odd-input branch, and write \(z\) for the corresponding offset \(y+2\) or \(y-2\). If \(z\equiv0\pmod{2^k}\), step 2 shows precisely the inputs with \(\nu_2(x\mp1)\ge\lceil k/2\rceil\) contribute. There are \(2^{\lfloor k/2\rfloor}\) such residues. Otherwise a contributing odd input requires \(\nu_2(z)=2r<k\), with \(r\ge2\); no other valuation can occur. For a fixed such \(r\), the odd parameter \(u\) has exactly \(2^{k-r-1}\) residue choices modulo \(2^{k-r}\), and its unit target has precision \(m=k-2r\). When \(m\le2\), all choices give the same permissible unit residue, resulting in \(2^{k-r-1}\) preimages. When \(m\ge3\), each of the two classes \(u\pmod4\) maps onto every unit target congruent to \(c_{\epsilon,r}\pmod8\), each with multiplicity \(2^{r+1}\), giving \(2^{r+2}\) combined preimages. These two cases are exactly \(2^{\min\{k-r-1,r+2\}}\). The appropriate unit-congruence test and the zero case therefore give \(H_{\epsilon,k}\). Summing the disjoint even and two odd input branches proves the boxed formula for \(N_k(y)\).

**5. Exact inverse-limit fibers and measure.** Step 3 makes the output of an exact valuation shell \(\nu_2(x\mp1)=r\) precisely the corresponding translated ball in \(\mathcal C_+\) or \(\mathcal C_-\), with two odd roots for every target there. The centers contribute exactly one odd root each, by the factorization in step 2. Distinct shells have distinct offset valuations, and the plus and minus branch images differ modulo sixteen (fourteen versus two), so all displayed components are disjoint. With the unique even root, this establishes the complete inverse-limit fiber classification.

Each noncenter ball at level \(r\) has measure \(2^{-(2r+3)}\). For either sign, the total measure of the two-root odd-target region is
\[
2^{-7}+\sum_{r\ge3}2^{-2r-3}
=\frac1{128}+\frac1{384}=\frac1{96}.
\]
The two signs therefore give \(1/48\). The centers have zero Haar measure. Since the full image has measure \(1/2\), the one-preimage target region has measure \(1/2-1/48=23/48\), completing the measure assertions.

**6. Least index periods.** Polynomial evaluation is periodic modulo \(2^k\) with period \(2^k\). If a positive integer \(T\) is a period, then \(F(T)\equiv F(0)=0\pmod{2^k}\). When \(T\) is odd, \(F(T)\equiv2\pmod4\); when \(T\) is even, \(\nu_2(F(T))=\nu_2(T)\). Thus for \(k\ge2\) every period is divisible by \(2^k\), proving sharpness. Modulo two all values vanish and the least period is one.

## Verification

Run the complete standalone artifact `python3 check_trace_cubic.py` with an ordinary Python 3 interpreter. It enumerates the polynomial images independently for all input residues modulo \(2^k\) for every \(4\le k\le17\), builds the exact target-by-target histogram and compares **every target** to the mathematical formula. It also checks every input's parity and mod-sixteen branch restrictions, the total input counts and the image sizes. All these direct enumerations passed. The cases \(k=4,5,6,7,8\) respectively have target-fiber histograms \(\{0:8,1:6,5:2\}\), \(\{0:16,1:12,5:4\}\), \(\{0:32,1:28,9:4\}\), \(\{0:64,1:58,9:4,17:2\}\), and \(\{0:128,1:120,17:8\}\). The script uses only the Python standard library and has no external dependencies. These finite calculations are diagnostics; the proof above establishes every precision and every infinite root count.

## Relationship to prior work

Bremser and Gomez-Calderon (1991) directly study **first-kind Dickson value sets over Galois rings** and report estimates and preimage counts in some cases. This is the closest potentially dominating source. Its publisher abstract and bibliographic record were examined, but its full text was unavailable; the abstract is **not** sufficient to rule out a special case equivalent to the present all-depth dyadic fiber formula. Consequently this work retains a concrete historical-priority risk.

Qu and Ding (2014, full author-posted paper inspected, including Theorem 3.2 and its conclusion) classify **permutation** behavior for Dickson polynomials of the **second kind**. Their statements do not give the present fibers of the nonpermuting first-kind cubic. Fan and Liao (2015, full arXiv HTML manuscript inspected, main Theorem 2) classify **dynamics of normalized Chebyshev maps** on \(\mathbb Z_2\); the scaling \(X\mapsto X/2\) does not transport their entire-space dynamical theorem to dyadic fibers of \(2T_3(X/2)\). Shang (2023, full arXiv manuscript inspected) gives **upper bounds** for value-set cardinalities of arbitrary nonpermutation polynomials, not target-by-target counts for this cubic.

Related published studies of the **same cubic modulo powers of three** concern iteration and first-hit depths, not one-step fibers at powers of two. Published classifications of iterated **even-degree** first-kind Dickson images and of second-kind quartics use other degrees and do not imply the cubic formula. Published general root-count distributions for **random monic cubics** concern averages across all coefficient vectors, not this named polynomial's target-by-target fibers. The new claim is restricted to the exact arithmetic classification stated here, not the classical factorization, Dickson identity, or general lifting principles.

## Limitations

The theorem is for the one-parameter first-kind cubic with parameter one and the prime two; it does not classify every Dickson degree, other parameters, other primes, or arbitrary cubic polynomials. The finite formula begins at precision four, although the image and least periods include smaller precisions. The inaccessible complete Bremser–Gomez-Calderon paper is a material unresolved historical-priority limitation, not evidence of noncoverage. Exhaustive checks through precision seventeen cannot replace the infinite proof and do not establish historical novelty. No independent mathematical validation is claimed.

## References

1. P. S. Bremser and J. Gomez-Calderon, “Value sets of Dickson polynomials over Galois rings,” *Journal of Number Theory* **38** (1991), 240–250. https://doi.org/10.1016/0022-314X(91)90087-R (publisher abstract inspected; full text not available).
2. L. Qu and C. Ding, “Dickson polynomials of the second kind that permute \(\mathbb Z_m\),” *SIAM Journal on Discrete Mathematics* **28** (2014), 722–735; first published electronically 2014-05-01. https://doi.org/10.1137/130942589 ; full author-posted paper: https://www.cse.ust.hk/faculty/cding/JOURNALS/siamdm141.pdf .
3. J. Fan and L. Liao, “Dynamics of Chebyshev polynomials on \(\mathbb Z_2\),” arXiv:1511.03529, first submitted 2015-11-11. https://arxiv.org/abs/1511.03529 .
4. S. Shang, “Value sets of non-permutation polynomials over the residue class rings of integers,” arXiv:2310.20226v1 (2023). https://arxiv.org/abs/2310.20226 .
5. W. S. Chou, J. Gomez-Calderon and G. L. Mullen, “Value sets of Dickson polynomials over finite fields,” *Journal of Number Theory* **30** (1988), 334–344. https://doi.org/10.1016/0022-314X(88)90006-6 .
