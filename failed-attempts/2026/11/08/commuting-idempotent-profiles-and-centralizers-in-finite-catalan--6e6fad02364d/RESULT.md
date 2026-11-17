# Commuting-idempotent profiles and centralizers in finite Catalan monoids

## Finding

For each integer \(n\geq 1\), let \(\mathcal C_n\) be the monoid of all weakly increasing, order-decreasing maps \(f:[n]\to[n]\), where \([n]=\{1,\ldots,n\}\) and \(f(i)\leq i\). For each subset \(S\subseteq[n]\) containing \(1\), define
\[
 e_S(i)=\max\{s\in S:s\leq i\}.
\]
These are exactly the idempotents of \(\mathcal C_n\). For two such subsets \(S,T\), the associated idempotents commute precisely when each interval between successive points of \(S\cap T\), with an extra terminal marker \(n+1\), contains exclusive points of at most one of \(S\) and \(T\). In that event, \(e_Se_T=e_Te_S=e_{S\cap T}\).

The full **ordered commuting-idempotent profile** is the trivariate series
\[
 F(z;u,v,w)=\sum_{n\ge1}z^n
 \sum_{\substack{S,T\subseteq[n],\ 1\in S\cap T\\e_Se_T=e_Te_S}}
 u^{|S\setminus T|}v^{|T\setminus S|}w^{|S\cap T|-1}.
\]
Put
\[
 B(z;u,v)=\frac{z}{1-(1+u)z}+\frac{z}{1-(1+v)z}-\frac{z}{1-z}.
\]
Then, as an identity of formal power series in \(z\) over \(\mathbb Z[u,v,w]\),
\[
 \boxed{F(z;u,v,w)=\frac{B(z;u,v)}{1-wB(z;u,v)}.}
\]
This formula refines the number of ordered commuting pairs simultaneously by the two exclusive fixed-point counts and the common fixed-point count.

It also gives **every idempotent centralizer size**. For \(S=\{s_1=1<s_2<\cdots<s_k\}\), let \(b_1=1\) and let each of \(b_2,\ldots,b_k\) be either zero or one. Then
\[
 \boxed{\#\{T\subseteq[n]:1\in T,\ e_Te_S=e_Se_T\}
 =\sum_{b_2,\ldots,b_k\in\{0,1\}}
 2^{\,\sum_{i=1}^{k-1}(s_{i+1}-s_i-1)b_ib_{i+1}+(n-s_k)b_k}.}
\]
The sum counts commuting idempotents, rather than the entire monoid centralizer.

In particular, for \(n\ge1\), the number of ordered commuting idempotent pairs is
\[
 \boxed{c_n=[z^n]\frac{z}{1-4z+2z^2}
 =\frac{(2+\sqrt2)^n-(2-\sqrt2)^n}{2\sqrt2}.}
\]
Its initial values are \(1,4,14,48,164,560,1912,6528,22288\) for \(n=1,\ldots,9\). Because there are \(2^{n-1}\) idempotents, two independent uniform idempotents commute with probability
\[
 \boxed{\frac{c_n}{4^{n-1}}\sim\sqrt2\left(\frac{2+\sqrt2}{4}\right)^n.}
\]
This probability decays exponentially. For a uniformly chosen **commuting** ordered pair, the expected number of common fixed points satisfies
\[
 \mathbb E|S\cap T|=\frac{n}{2\sqrt2}+\frac12+O\!\left(n(3-2\sqrt2)^n\right).
\]

## Assumptions and scope

All maps are **total**, weakly increasing, and order-decreasing on the *labeled* chain \([n]\); composition is ordinary function composition. The opposite, order-*increasing* convention for the Catalan monoid is isomorphic by reversal of the chain and gives the same enumerations. The two idempotents are ordered and independently sampled when a probability is given. A common fixed point is counted once, and the compulsory point \(1\) is omitted from the exponent of \(w\) only to make the generating function uniform. The right terminal marker \(n+1\) is **not** a fixed point and carries no \(w\)-weight. No assertion is made about arbitrary (non-idempotent) commuting transformations.

## Proof

**1. Idempotent normal form.** Let \(f\in\mathcal C_n\) be idempotent and set \(S=\operatorname{im}(f)\). An idempotent fixes every image point; also \(1\in S\). If \(s\) is the largest fixed point not exceeding \(i\), monotonicity gives \(f(i)\ge f(s)=s\). Since \(f(i)\in S\) and \(f(i)\le i\), necessarily \(f(i)=s\). Conversely each \(e_S\) is clearly weakly increasing, decreasing, and idempotent. Thus the parametrization is unique.

**2. The commutation criterion.** Write \(U=S\cap T=\{a_1=1<\cdots<a_k\}\), and set \(a_{k+1}=n+1\). Suppose a gap \((a_j,a_{j+1})\) contains both an \(S\)-exclusive fixed point and a \(T\)-exclusive fixed point. Interchange \(S,T\), if necessary, so that some \(s\in S\setminus T\) precedes some \(t\in T\setminus S\) in the gap. Let \(s'=e_S(t)\). Then \(s'\ge s\), \(s'<t\), and \(s'\in S\setminus T\): it cannot be in \(U\), since there is no common point inside the gap. At \(t\),
\[
 e_S(e_T(t))=e_S(t)=s',\qquad
 e_T(e_S(t))=e_T(s')<s'.
\]
Hence the two transformations cannot commute.

Conversely suppose no gap contains both types of exclusive fixed point. Fix \(i\) in the half-open gap \([a_j,a_{j+1})\). If the gap contains only \(S\)-exclusive points, \(e_T(i)=a_j\), so \(e_S(e_T(i))=a_j\); also \(e_S(i)\) is either \(a_j\) or an \(S\)-exclusive point, and \(e_T(e_S(i))=a_j\). The same holds symmetrically for a gap with only \(T\)-exclusive points, and trivially when it contains neither type. Thus both composites send \(i\) to \(a_j=e_U(i)\), proving sufficiency and the asserted product identity.

**3. Colored gap decomposition.** Each commuting pair corresponds uniquely to the successive gap lengths \(d_j=a_{j+1}-a_j\ge1\), summing to \(n\). For a gap of length \(d\), the \(d-1\) interior sites may be unused or occupied by \(S\setminus T\), **or** unused or occupied by \(T\setminus S\), but the all-unused choice has been counted twice. Its weight polynomial is therefore
\[
 P_d(u,v)=(1+u)^{d-1}+(1+v)^{d-1}-1.
\]
The generating series for one gap is
\[
 \sum_{d\ge1}P_d(u,v)z^d=B(z;u,v).
\]
There are \(k=|U|\) gaps and exactly \(k-1\) additional common fixed points after \(1\), so their total weight is \(w^{k-1}B^k\). Summing over \(k\ge1\) proves \(F=B/(1-wB)\) as a formal identity, without an analytic convergence assumption.

**4. Idempotent centralizers.** Fix \(S=\{s_1,\ldots,s_k\}\), and record by \(b_i\) whether \(s_i\in T\); the first bit is necessarily one. For each bounded gap \((s_i,s_{i+1})\), a point of \(T\) in its interior is allowed **if and only if** both endpoints \(s_i,s_{i+1}\) belong to \(T\). Indeed, if the left endpoint is omitted, the point is in the same common-gap as the previous \(S\)-exclusive point; if the right endpoint is omitted, it is in the same common-gap as that next \(S\)-exclusive point. Either gives the obstruction in step 2. If both endpoints are present, arbitrary interior \(T\)-points are permitted because they lie between two consecutive common fixed points with no \(S\)-exclusive point. On the terminal interval \((s_k,n+1)\), arbitrary \(T\)-points are allowed exactly when \(s_k\in T\). Thus, after the bits are fixed, the number of allowable \(T\)'s is the displayed power of two. Summing the possibilities proves the centralizer formula.

**5. Total and asymptotic enumerations.** Substituting \(u=v=w=1\) gives
\[
 B(z;1,1)=\frac{z}{(1-z)(1-2z)},\qquad
 F(z;1,1,1)=\frac{z}{1-4z+2z^2}.
\]
Partial fractions at the two distinct roots give the closed form for \(c_n\) and the displayed exponential commutation probability. Moreover,
\[
 \left.\frac{\partial F}{\partial w}\right|_{u=v=w=1}
 =\frac{z^2}{(1-4z+2z^2)^2}
 =\sum_{n\ge1}z^n c_n\,
 \mathbb E\bigl[|S\cap T|-1\mid e_Se_T=e_Te_S\bigr].
\]
Partial fractions for this double-pole series, divided by the preceding formula for \(c_n\), give the stated expectation with secondary-root error \(O(n(3-2\sqrt2)^n)\). This completes the proof.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It enumerates *all* weakly increasing decreasing maps through \(n=7\), identifies their actual idempotents by composition, and compares these with the fixed-subset normal form. It then composes all ordered pairs of these idempotents through \(n=9\), records the complete three-variable coefficient distribution, and independently reconstructs that distribution from weighted gap compositions. For every fixed subset through \(n=9\), it compares its brute-force commuting-idempotent centralizer with the bit-sum formula. It also checks the two-step recurrence and exact initial counts. The verification finishes with `VERIFY_OK`. These tests validate specified finite cases, not the infinite theorem, which follows from the proof above.

To reproduce: run `python3 verify.py` in a directory containing the provided file. No extra data or modules are needed.

## Relationship to prior work

The normal form and count of individual Catalan-monoid idempotents are known. Ayık–Ayık–Koç (2011) also count Catalan transformations with specified fixed-point sets; such one-map marginals do not alone determine how two idempotents commute. Pantazi and Spircu (2016/2017) examine their structure and relations between consecutive Catalan monoids; Sapir and Volkov (2022/2023) contrast the classical Catalan monoid with the partial-injective version, whose idempotents commute. A general idempotent commutation test for Hecke–Kiselman monoids is also available in Andrenšek (2026), so a bare commuting criterion is not asserted as an independent priority claim. The present contribution is the **explicit multivariate commutation enumeration**, its all-idempotent centralizer specialization and the resulting probability and fixed-point statistics in the classical Catalan transformation monoid.

Toker (2021) counts zero-divisors and studies the graph relation \(xy=	heta=yx\) (with \(	heta\) the zero transformation); that is strictly narrower than counting arbitrary commuting idempotent pairs, whose common product can be any \(e_{S\cap T}\).

The unrefined sequence \(1,4,14,48,164,\ldots\) already occurs as **OEIS A007070** (with offset shifted here by one) in other combinatorial contexts, including a weighted-compositions interpretation. The numerical recurrence alone is therefore **not** claimed to be previously unknown. The exact trivariate interpretation and centralizer profile are the mathematically substantive statements. Searches and inspected works did not identify this full specialization, but literature priority is not certified.

## Limitations

Only pairs of idempotents in finite classical Catalan monoids are counted. No statement is made about all commuting pairs, higher commuting tuples, or idempotents in other Hecke–Kiselman monoids. The generating function is a formal combinatorial identity; the expectation and asymptotic probability use the indicated distribution, not an arbitrary alternative sampling measure. The agreement of an unrefined coefficient sequence with OEIS is known and does not alone establish originality. A more general prior enumeration might imply the refinements; complete publication-priority verification remains open.

## References

- Olga B. Sapir and Mikhail V. Volkov, *Catalan monoids inherently nonfinitely based relative to finite \(\mathcal R\)-trivial semigroups*, arXiv:2211.12952, first posted November 23, 2022; see the Catalan and i-Catalan comparison. https://arxiv.org/abs/2211.12952
- Stefan V. Pantazi and Tiberiu Spircu, *Relations between consecutive Catalan monoids*, February 10, 2016, updated March 17, 2017; particularly Section 4 (idempotents). https://www.researchgate.net/publication/330567006_Relations_between_consecutive_Catalan_monoids
- Luka Andrenšek, *Homomorphisms of Hecke–Kiselman Monoids Associated to Simple Oriented Graphs*, arXiv:2604.15497, April 16, 2026; especially Section 3 and Corollary 3.9. https://arxiv.org/abs/2604.15497
- Gonca Ayık, Hayrullah Ayık, and Metin Koç, *Combinatorial results for order-preserving and order-decreasing transformations*, Turkish J. Math. **35** (2011), 617–625; publisher abstract available at https://journals.tubitak.gov.tr/math/vol35/iss4/3/ (full text not accessed).
- Kemal Toker, *Zero-divisor graphs of Catalan monoid*, Hacettepe J. Math. Stat. **50** (2021), 387–396, DOI:10.15672/hujms.702478. https://dergipark.org.tr/en/download/article-file/1002929
- OEIS Foundation, *A007070*, recurrence \(a(k)=4a(k-1)-2a(k-2)\); the catalogued number sequence is prior art independently of the interpretation here. https://oeis.org/A007070
