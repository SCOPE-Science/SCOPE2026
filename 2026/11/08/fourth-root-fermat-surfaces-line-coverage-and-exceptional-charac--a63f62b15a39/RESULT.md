# Fourth-root Fermat surfaces: line coverage and exceptional characteristics

## Finding

Let \(q=p^r\equiv1\pmod4\) be an odd prime power, set \(d=(q-1)/4\), and assume \(d\ge2\). Let
\[
X_d:\quad x_0^d+x_1^d+x_2^d+x_3^d=0\subset\mathbb P^3_{\mathbb F_q}.
\]
For each of the three partitions of the four coordinates into two unordered pairs \(\{i,j\}\sqcup\{k,l\}\), and each \(a,b\in\mathbb F_q\) with \(a^d=b^d=-1\), take the line
\[
L_{ij\mid kl}(a,b):\quad x_i=a x_j,\qquad x_k=b x_l.
\]
Fix one orientation for each pair. Let \(U_d\subset X_d\) be the reduced union of these \(3d^2\) distinct rational lines. Then
\[
\boxed{\#U_d(\mathbb F_q)=9d^3+6d}
\]
and the exact count of rational points off this union is
\[
\boxed{\#(X_d\setminus U_d)(\mathbb F_q)=
\begin{cases}
4d^2,&p=3,\\
4d^3+12d^2,&p=5,\\
0,&p\ge7.
\end{cases}}
\]
In particular, **the distinguished lines contain every rational point if and only if the characteristic is at least seven.** This covers infinitely many smooth surfaces of unbounded degree.

For \(d\ge3\), put \(N_j=\#\{P\in X_d(\mathbb F_q):P\text{ lies on exactly }j\text{ of the displayed lines}\}\). The complete positive-incidence spectrum is
\[
\boxed{N_1=6d^3,\qquad N_2=3d^3,\qquad N_d=6d,\qquad
N_j=0\ (j\notin\{0,1,2,d\}).}
\]
The zero-incidence count is the case distinction above. For the sole admissible quadratic case \(q=9,d=2\), the \(d\)-fold and twofold strata coincide, and \((N_0,N_1,N_2)=(16,48,36)\).

Equivalently, the total rational-point count on the smooth surface is
\[
\#X_d(\mathbb F_q)=
\begin{cases}
9d^3+4d^2+6d,&p=3,\\
13d^3+12d^2+6d,&p=5,\\
9d^3+6d,&p\ge7.
\end{cases}
\]

## Assumptions and scope

All geometric assertions are over the finite base field \(\mathbb F_q\); no algebraic closure is required to define the displayed lines. The assumption \(q\equiv1\pmod4\) ensures \(\mu_4\subset\mathbb F_q\), and \(d=(q-1)/4\) implies \(p\nmid d\), hence \(X_d\) is smooth by the Jacobian criterion. Degree one (\(q=5\)) is excluded because the relevant object would be a projective plane, not a surface of degree at least two. No assertion is needed about possible additional lines in special positive characteristics: coverage and incidence refer to the explicitly defined \(3d^2\)-line union \(U_d\).

## Proof

**Step 1 (short sums of fourth roots).** The map \(\mathbb F_q^\times\to\mu_4\), \(x\mapsto x^d\), is surjective with fibers of size \(d\). Choose \(i\in\mu_4\) with \(i^2=-1\). Its image, with zero adjoined, is \(H=\{0,1,-1,i,-i\}\). For \(y_0,\ldots,y_3\in H\), let \(c_t\) be the number of ordered four-tuples summing to zero and with exactly \(t\) nonzero coordinates. Direct counting gives
\[
\begin{array}{c|ccc}
&c_2&c_3&c_4\\\hline
p\ge7&24&0&36\\
p=3&24&16&36\\
p=5&24&48&52.
\end{array}
\]
Here is a non-experimental verification of the table. For \(p\ge7\), a zero sum is of the form \(A+Bi=0\), with integral signed multiplicities satisfying \(|A|+|B|\le4\). Multiplying by \(A-Bi\) shows that \(p\) divides \(A^2+B^2\). For \((A,B)\ne(0,0)\), its possible values are exactly \(\{1,2,4,5,8,9,10,16\}\), none divisible by \(p\ge7\). Hence \(A=B=0\), and every nonzero term is paired with its negative. This gives \(c_2=\binom42\cdot4=24\), \(c_3=0\), and \(c_4=36\): there are \(12\) quadruples using one opposite pair twice and \(24\) quadruples using both opposite pairs once.

In characteristic three, \(i\notin\mathbb F_3\), so \(1,i\) are linearly independent over \(\mathbb F_3\). Three nonzero roots sum to zero precisely when they are equal; there are \(4\cdot4=16\) such supported triples (including their possible zero coordinate), and the four-term patterns are still the \(36\) opposite-paired tuples. In characteristic five, \(\mu_4=\mathbb F_5^\times\), and the number \(T_n\) of ordered \(n\)-tuples of nonzero elements of \(\mathbb F_5\) summing to zero is
\[
T_n=\frac{4^n+4(-1)^n}{5}.
\]
This follows either from the nontrivial-additive-character sum \(\sum_{u\in\mathbb F_5^\times}\psi(u)=-1\), or by the elementary recurrence \(T_n+T_{n-1}=4^{n-1}\), with \(T_1=0\). Thus \(c_3=4T_3=48\), \(c_4=T_4=52\), and \(c_2=24\). No tuple with exactly one nonzero coordinate can sum to zero.

**Step 2 (rational points).** Each fixed nonzero value in \(\mu_4\) has exactly \(d\) coordinate preimages, while zero has one. Consequently the number of nonzero affine solution vectors is \(c_2d^2+c_3d^3+c_4d^4\). The scalar group \(\mathbb F_q^\times\), of order \(4d\), acts freely on them. Therefore
\[
\#X_d(\mathbb F_q)=\frac{c_2d^2+c_3d^3+c_4d^4}{4d},
\]
which gives the three displayed point-count formulas.

**Step 3 (the line incidence spectrum).** Each line \(L_{ij\mid kl}(a,b)\) is contained in \(X_d\), because its two coordinate pairs contribute opposite \(d\)-th powers. There are three families with \(d^2\) lines per family. In a fixed family, two distinct lines can meet only when one of the parameters agrees; the intersections are the \(6d\) points with exactly two nonzero coordinates whose \(d\)-th powers are opposite. Each such point lies on exactly \(d\) displayed lines, all in that family.

Between any two different families, two lines meet precisely when their four parameters satisfy one multiplicative equality, such as \(ab'=ba'\). Thus there are \(d^3\) pairwise intersections for each of the three unordered pairs of families. These are distinct: every such point has all four coordinates nonzero and cannot lie in a third family. Indeed, its first two opposite-pairing conditions force a pattern of \(d\)-th powers of the form \((h,-h,-h,h)\), where \(h\ne0\); the third pairing would require \(2h=0\), impossible in odd characteristic. It follows that there are exactly \(3d^3\) points on two displayed lines, in addition to the \(6d\) points on \(d\) lines (and these strata coincide only if \(d=2\)).

The total number of rational line-point incidences is \(3d^2(q+1)=3d^2(4d+2)\). Subtracting contributions from the multiple points gives
\[
N_1=3d^2(4d+2)-2\cdot3d^3-d\cdot6d=6d^3.
\]
Therefore the union contains \(6d^3+3d^3+6d=9d^3+6d\) distinct rational points, also for \(d=2\) after merging the twofold strata.

**Step 4 (the exact exceptional loci).** Subtracting this union count from Step 2 yields the claimed complementary counts. To see that the exceptions are genuine without relying on subtraction, in characteristic three the point \([1:1:1:0]\) lies on \(X_d\), but on no displayed line. In characteristic five, choose \(a\in\mathbb F_q^\times\) with \(a^d=2\); then \([1:1:1:a]\) has the same property since \(1+1+1+2=0\) in characteristic five. This completes the proof.

## Verification

The bundled standard-library scripts `verify_root_sums.py` and `verify_point_incidence.py` independently implement the short-sum calculation and direct projective-point incidence counts. Run `python verify_root_sums.py` and `python verify_point_incidence.py` with Python 3. The former checks all \(5^4\) fourth-root tuples for a list of characteristics and confirms the Gaussian norm obstruction and closed-form formulas. The latter enumerates all projective points over \(\mathbb F_9,\mathbb F_{13},\mathbb F_{17},\mathbb F_{25},\mathbb F_{29},\mathbb F_{37},\mathbb F_{49}\), testing each surface equation and explicitly counting how many distinguished lines contain the point. Both completed successfully on the files bundled with this result, respectively producing `VERIFY_ROOT_SUMS_OK` and `VERIFY_POINT_INCIDENCE_OK`.

In particular, the direct rational-point spectra are \((N_0,N_1,N_2)=(16,48,36)\) at \(q=9\), \((N_0,N_1,N_2,N_6)=(1296,1296,648,36)\) at \(q=25\), and \((N_0,N_1,N_2,N_{12})=(0,10368,5184,72)\) at \(q=49\). These are finite cross-checks; the proof above, not computation, establishes all prime powers.

## Relationship to prior work

The three families of Fermat-surface coordinate-pairing lines and their geometric intersection patterns are classical, and their existence and incidence are not presented as new. Schütt, Shioda and van Luijk studied such lines; Andria, Rojas and Mangueira (arXiv:2403.15666, first posted March 23, 2024) provide a detailed intersection treatment and a skew-line classification. Borges, Cook and Coutinho (arXiv:1804.04442, first posted April 12, 2018) study plane sections and rational points for the different index-two regime \(q=2d+1\). Voloch and Zieve (arXiv:1310.1772, first posted October 7, 2013) classify points on Fermat surfaces over quadratic extensions in exponent \(q_0-1\); in particular, their theorem covers the specialization \(q=9,d=2\). Aubry and Voloch (arXiv:2605.09166, first posted May 9, 2026) calculate points and rational-line configurations in several other Fermat-type families, especially exponent \((p-1)/2\).

The contribution here is the **uniform arithmetic point-covering criterion and exact complementary counts in the index-four regime \(q=4d+1\)**, for arbitrary prime powers, including the two exceptional characteristics. It is not a new enumeration of the geometric lines and does not claim novelty for already published isolated small-degree specializations.

## Limitations

The statement assumes odd \(q\equiv1\pmod4\), \(d=(q-1)/4\), and \(d\ge2\). It does not classify rational points or lines for other exponent-to-field-size ratios. In positive characteristic special Fermat surfaces can have additional geometric lines; the result is specifically about the \(3d^2\) defined coordinate-pairing lines. Computational examples are not a substitute for the all-field proof. A historically earlier equivalent fourth-root-sum or arithmetic-incidence formula under different terminology remains possible; no independent priority adjudication has been performed.

## References

1. H. Borges, G. Cook, M. Coutinho, *Plane sections of Fermat surfaces over finite fields*, arXiv:1804.04442 (first posted 2018-04-12), https://arxiv.org/abs/1804.04442 .
2. J. F. Voloch, M. E. Zieve, *Rational points on some Fermat curves and surfaces over finite fields*, arXiv:1310.1772 (first posted 2013-10-07), https://arxiv.org/abs/1310.1772 .
3. S. Andria, J. Rojas, W. Mangueira, *Maximal number of Skew lines on Fermat Surfaces*, arXiv:2403.15666 (first posted 2024-03-23), https://arxiv.org/abs/2403.15666 .
4. Y. Aubry, J. F. Voloch, *Rational points on smooth surfaces in projective three-space over finite fields*, arXiv:2605.09166 (first posted 2026-05-09), https://arxiv.org/abs/2605.09166 .
5. M. Schütt, T. Shioda, R. van Luijk, *Lines on Fermat surfaces*, Journal of Number Theory 130 (2010), 1939–1963.
