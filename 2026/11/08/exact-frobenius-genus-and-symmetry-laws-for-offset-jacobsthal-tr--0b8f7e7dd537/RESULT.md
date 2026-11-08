# Exact Frobenius, genus, and symmetry laws for offset Jacobsthal triples

## Finding
Let \(J_0=0\), \(J_1=1\), and \(J_{m+2}=J_{m+1}+2J_m\). For each integer \(n\ge3\) set
\[
a=J_n,\qquad b=J_{n+3},\qquad c=J_{n+4},\qquad S_n=\langle a,b,c\rangle\subseteq\mathbb N_0.
\]
The generators have greatest common divisor one. Let \(F_n\) be the largest nonnegative integer omitted by \(S_n\), let \(g_n\) be its number of omitted positive integers, and let \(\Delta_n=2g_n-F_n-1\) be its symmetry defect. Then the **exact formulas for every \(n\ge3\)** are
\[
F_n=\begin{cases}
\dfrac{ab}{3}-a-b+2c,&3\mid n,\\[3pt]
\dfrac{a+2}{3}b+c-a,&3\nmid n,\ a\equiv1\pmod3,\\[3pt]
\dfrac{a+7}{3}b-a,&3\nmid n,\ a\equiv2\pmod3;
\end{cases}
\]
\[
g_n=\begin{cases}
(F_n+1)/2,&3\mid n,\\[3pt]
\dfrac{(a-1)(b-1)}2+\dfrac{(a-5)(8-b)}3,&3\nmid n;
\end{cases}
\]
and
\[
\Delta_n=\begin{cases}
0,&3\mid n,\\
\dfrac{8(a-10)}3,&3\nmid n,\ a\equiv1\pmod3,\\[3pt]
\dfrac{16(a-5)}3,&3\nmid n,\ a\equiv2\pmod3.
\end{cases}
\]
Consequently \(S_n\) is symmetric **if and only if** \(3\mid n\) or \(n=4\). More strongly, when \(3\nmid n\), the entire Apéry set with respect to \(a\) admits the three-strip description established below.

## Assumptions and scope
All indices are integers \(n\ge3\). The Jacobsthal recurrence has the closed form \(J_n=(2^n-(-1)^n)/3\). A numerical semigroup is the additive submonoid of nonnegative integers with finite complement. Its Apéry set with respect to \(a\in S\setminus\{0\}\) consists of the least element of \(S\) in each residue class modulo \(a\). A semigroup is symmetric if for its Frobenius number \(F\), exactly one of \(z\) and \(F-z\) belongs to it for every \(0\le z\le F\); equivalently \(2g=F+1\).

## Proof
**1. Universal identities.** Writing \(s=(-1)^n\), the Jacobsthal closed form gives
\[
b=8a+3s,\qquad c=16a+5s,\qquad 3c=8a+5b,\qquad c=2b-s.
\]
In particular \(\gcd(b,c)=\gcd(b,s)=1\). Also \(\gcd(a,b)=\gcd(a,3)\). Since \(2\) has order six modulo nine, \(3\mid a\) exactly when \(3\mid n\). For \(n\ge3\), we have \(b\ge21\), hence \(0<2c<5b\). The gcd condition on all three generators follows immediately.

**2. Indices divisible by three.** If \(3\mid n\), set \(u=a/3\) and \(v=b/3\). Then \(\gcd(u,v)=1\), \(\gcd(3,c)=1\), and \(c=8u+5v\in T=\langle u,v\rangle\). Thus
\[
S_n=3T\ \dot\cup\ (c+3T)\ \dot\cup\ (2c+3T).
\]
The union is disjoint by residue modulo three; any coefficient of \(c\) can be reduced modulo three because \(c\in T\). The two-generator Sylvester formula gives \(F(T)=uv-u-v\), and the two-generator gap count gives \(g(T)=(F(T)+1)/2\), including the case \(T=\mathbb N_0\) where \(F(T)=-1\). In each residue class having nonnegative gaps, its largest gap is formally one of \(3F(T)\), \(c+3F(T)\), and \(2c+3F(T)\), respectively; a negative value indicates that the class has no nonnegative gaps. Hence \(F_n=3F(T)+2c=ab/3-a-b+2c\). The gap count is
\[
g_n=3g(T)+\left\lfloor\frac c3\right\rfloor+\left\lfloor\frac{2c}3\right\rfloor
=3g(T)+c-1=(F_n+1)/2,
\]
where the floor identity uses \(\gcd(c,3)=1\). Thus \(\Delta_n=0\).

**3. A three-candidate Apéry reduction when \(3\nmid n\).** Now \(\gcd(a,b)=1\). Let \(t\in\{0,\ldots,a-1\}\) satisfy \(3t\equiv5\pmod a\); then \(c\equiv tb\pmod a\). An Apéry element uses no copies of \(a\), since subtracting \(a\) would give a smaller semigroup element in the same residue class. Every Apéry element with respect to \(a\) uses fewer than three copies of \(c\): if it used at least three, replacing \(3c\) by \(5b\) subtracts \(8a>0\) while preserving its residue. It also uses fewer than \(a\) copies of \(b\), since subtracting \(ab\) would preserve the residue. Therefore the Apéry element in the class \(kb\pmod a\), for \(0\le k<a\), is exactly
\[
w(k)=\min_{y\in\{0,1,2\}}
\left(\bigl((k-yt)\bmod a\bigr)b+yc\right).
\]
Here the remainder lies in \(\{0,\dots,a-1\}\). This is an exhaustive minimization, not an experimental search.

**4. The residue case \(a\equiv1\pmod3\).** For \(n\ge3\) in this case \(a\ge43\) and \(t=(a+5)/3\), so \(0<t<2t<a\). Comparing the three candidates in the preceding display, using \(c<5b/2\) and \(t\ge16\), proves that the minimizing \(y\) is
\[
y=\begin{cases}0,&0\le k<t,\\1,&t\le k<2t,\\2,&2t\le k<a.\end{cases}
\]
For example, below the first breakpoint both wrapped candidates exceed \(kb\); in the middle strip the once-unwrapped candidate beats both alternatives; and above the second breakpoint the twice-unwrapped candidate wins. The maximum in each strip occurs at its last \(k\), and the middle-strip endpoint \((t-1)b+c\) exceeds the first by \(c\) and the third by \(5b-c>0\). Therefore
\[
F_n=(t-1)b+c-a=\frac{a+2}{3}b+c-a.
\]
Summing the Apéry values gives
\[
\sum_{k=0}^{a-1}w(k)
=\frac{a(a-1)}2b+(c-tb)(a-5).
\]
Since \(3(c-tb)=a(8-b)\), the Apéry genus identity
\(g_n=a^{-1}\sum w(k)-(a-1)/2\) yields the stated genus formula.

**5. The residue case \(a\equiv2\pmod3\).** The exceptional smallest such case is \(a=5\), i.e. \(n=4\). Here \(c=85\) is a multiple of \(a\), and the Apéry set is simply \(\{0,b,2b,3b,4b\}\), so \(F=4b-a=167\) and \(g=84\), in agreement with the formulas.

For \(a\ge11\), set \(t=(2a+5)/3\) and \(u=2t-a=(a+10)/3\). Then \(0<u<t<a\). Direct comparison of the three candidates using \(2c<5b\) and \(u\ge7\) shows that the minimizing \(y\) is
\[
y=\begin{cases}0,&0\le k<u,\\2,&u\le k<t,\\1,&t\le k<a.\end{cases}
\]
The endpoint values are \((u-1)b\), \((t-1-u)b+2c\), and \((a-1-t)b+c\); the second is smaller than the first by \(5b-2c>0\), and the third is smaller than the second by \(c\). Consequently
\[
F_n=(u-1)b-a=\frac{a+7}{3}b-a.
\]
The genus follows from
\[
\sum_{k=0}^{a-1}w(k)
=\frac{a(a-1)}2b+(2c-ub)(t-u)+(c-tb)(a-t),
\]
together with \(t-u=a-t=(a-5)/3\), \(3(2c-ub)=a(16-b)\), and \(3(c-tb)=a(8-2b)\). This simplifies to exactly the same genus formula as in Step 4.

**6. Symmetry.** Subtracting the Frobenius formulas from twice the genus minus one yields
\[
2g_n-F_n-1=\frac{8(a-10)}3\quad(a\equiv1\pmod3),\qquad
2g_n-F_n-1=\frac{16(a-5)}3\quad(a\equiv2\pmod3).
\]
In the first case \(a\ge43\), so this is strictly positive. In the second case it vanishes precisely when \(a=5\), which occurs only at \(n=4\); all other such indices have \(a\ge11\). The divisible-by-three case is symmetric by Step 2. This completes the exact classification.

## Verification
An independent exact-integer shortest-path computation of each Apéry set for all \(3\le n\le16\) confirms both closed formulas and the symmetry classification; it also independently checks each prescribed minimizing branch of the explicit three-candidate Apéry expression. Run the included standalone `checker.py` with Python 3. No external packages or data files are needed; its output is in `verification_output.txt`. These finite computations are corroborative only: the argument in Steps 1–6 proves the unrestricted theorem.

## Relationship to prior work
Komatsu, Laishram and Punyani study generalized-Fibonacci/Jacobsthal triples whose generator indices include an offset of two, and give formulas for their \(p\)-Frobenius numbers and genera. Komatsu and Pita-Ruiz also study Jacobsthal triples with the offset-two generator. Mu and Komatsu's later recurrence-triple results retain an offset-two generator. None of those inspected theorem statements directly contains the family with offsets three and four considered here. The two-generator Sylvester and Apéry identities are classical; the three-strip Apéry geometry, piecewise exact formulas and the resulting symmetry-defect classification are the present claims. A separately recorded Pell-offset family uses a different recurrence and different gluing relation, and does not mathematically imply the Jacobsthal formulas. Searches cannot establish absolute priority, and unindexed equivalent results remain possible.

## Limitations
The claim applies only to the usual Jacobsthal sequence, to the offset triple \((n,n+3,n+4)\), and to \(n\ge3\). It does not compute \(p\)-Frobenius numbers for \(p>0\), nor make assertions about all generalized Jacobsthal parameters or other offset patterns. An independent external mathematical audit has not been performed. The later general-recurrence article's abstract and stated offset-two scope were accessible, but its complete full text was not inspected; this is a residual originality risk.

## References
- T. Komatsu, S. Laishram and P. Punyani, “\(p\)-Numerical Semigroups of Generalized Fibonacci Triples,” *Symmetry* 15 (2023), 852; arXiv:2304.00443, first public 2023-04-02. https://arxiv.org/abs/2304.00443 ; https://doi.org/10.3390/sym15040852.
- T. Komatsu and C. Pita-Ruiz, “The Frobenius Number for Jacobsthal Triples Associated with Number of Solutions,” *Axioms* 12 (2023), 98. https://doi.org/10.3390/axioms12020098.
- J. Mu and T. Komatsu, “\(p\)-Numerical Semigroups of Triples from the Three-Term Recurrence Relations,” *Axioms* 13 (2024), 608. https://doi.org/10.3390/axioms13090608.
- J. Herzog, “Generators and relations of abelian semigroups and semigroup rings,” *Manuscripta Mathematica* 3 (1970), 175–193. https://doi.org/10.1007/BF01273309.
