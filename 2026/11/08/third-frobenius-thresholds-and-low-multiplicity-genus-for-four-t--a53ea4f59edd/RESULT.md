# Third Frobenius thresholds and low-multiplicity genus for four-term arithmetic progressions

## Finding
For every integer \(a\ge4\) and positive integer \(d\) with \(\gcd(a,d)=1\), let
\[
 R_{a,d}(n)=\#\{(x_0,x_1,x_2,x_3)\in\mathbb Z_{\ge0}^4:\sum_{i=0}^3(a+id)x_i=n\}.
\]
The *third Frobenius threshold* \(F_3(a,d)\) is the greatest nonnegative integer having fewer than three representations, and \(H_3(a,d)\) counts all such nonnegative integers. Put \(q=\lfloor a/3\rfloor\). Then
\[
\boxed{F_3(a,d)=\begin{cases}
a(d+q)+2d,&a\equiv0\pmod3,\\
a(d+q)+d+\max\{a,d\},&a\equiv1\pmod3,\\
a(d+q+1)+2d,&a\equiv2\pmod3.
\end{cases}}
\]
Moreover,
\[
\boxed{H_3(a,d)=3d+2a-1+\mathbf1_{a\equiv2\ (\mathrm{mod}\ 3)}+
\sum_{t=0}^{a-1}\left\lceil\frac t3\right\rceil+
\frac{(a-1)(d-1)}2.}
\]
A stronger residue-by-residue threshold is proved below. It determines not only the extremal exceptional integer, but all integers having at most two representations.

## Assumptions and scope
All four coefficients \(a,a+d,a+2d,a+3d\) are positive; \(a\ge4\), \(d\ge1\), \(\gcd(a,d)=1\), and representations are ordered by coefficient, with all four multiplicities nonnegative. Thus distinct vectors of multiplicities count separately. The threshold concerns *at least three* representations. It is also denoted the \(p=2\) generalized Frobenius number, or the \(3\)-Frobenius number, in two different indexing conventions.

For integer \(T\ge4\) define
\[
 b(T)=\left\lfloor\frac T3\right\rfloor+1+\mathbf1_{T\equiv2\ (\mathrm{mod}\ 3)}.
\]
For \(0\le t<a\), define
\[
 N_t=\begin{cases}
 d+b(a),&t=0,\\
 d+b(a+1),&t=1,\\
 d+\left\lceil\frac{a+2}{3}\right\rceil,&t=2,\\
 3,&t=3,\\
 \left\lceil\frac t3\right\rceil+1,&4\le t<a,
\end{cases}
\qquad M_t=aN_t+dt.
\]
Here the last branch is empty when \(a=4\). The exact residue law is
\[
 \boxed{R_{a,d}(n)\ge3\quad\Longleftrightarrow\quad n\ge M_t
 \ \text{for the unique }t\in\{0,\ldots,a-1\}\text{ with }n\equiv dt\pmod a.}
\]

## Proof
**Representation coordinates.** For a representation of \(n\), set \(L=x_0+x_1+x_2+x_3\) and \(T=x_1+2x_2+3x_3\). Then \(n=aL+dT\). Fix \(t\in\{0,\dots,a-1\}\) and write \(n=aU+dt\). Since \(\gcd(a,d)=1\), every representation corresponds to a unique integer \(j\ge0\) with \(T=t+ja\), \(L=U-jd\). Define
\[
 P(T,L)=\#\{(x_1,x_2,x_3)\in\mathbb Z_{\ge0}^3:
 x_1+2x_2+3x_3=T,\ x_1+x_2+x_3\le L\},
\]
with \(P(T,L)=0\) if \(L<0\). The missing coefficient is uniquely \(x_0=L-x_1-x_2-x_3\). Consequently,
\[
 R_{a,d}(aU+dt)=\sum_{j\ge0}P(t+ja,U-jd).\tag{1}
\]
The sum is finite and nondecreasing in \(U\). Every partition of weight \(T\) into parts \(1,2,3\) has length at least \(\lceil T/3\rceil\).

**Two- and three-representation lengths.** For every \(T\ge4\), the least \(L\) with \(P(T,L)\ge2\) is \(b(T)\): at minimal length \(\lceil T/3\rceil\), weight \(3q+1\) has the two partitions \(3^q1\) and \(3^{q-1}2^2\); weights \(3q\) and \(3q+2\) have only one, and a second partition appears upon allowing one further part. The least \(L\) with \(P(T,L)\ge3\) is
\[
 c(T)=\left\lceil\frac T3\right\rceil+1\qquad(T\ge4).\tag{2}
\]
Indeed, at minimal length there are at most two partitions. One further part supplies three distinct partitions, exhibited by
\[
\begin{array}{ll}
 T=3q\ (q\ge2):&3^q,\;3^{q-1}21,\;3^{q-2}2^3,\\
 T=3q+1\ (q\ge1):&3^q1,\;3^{q-1}2^2,\;3^{q-1}21^2,\\
 T=3q+2\ (q\ge1):&3^q2,\;3^q1^2,\;3^{q-1}2^21.
\end{array}
\]
Here \(3^q\), for example, denotes \(q\) parts of size three, not exponentiation of an integer. For \(T=3\), the three partitions \(3\), \(21\), \(1^3\) first coexist at \(L=3\). For \(T=0,1\) there is always at most one partition, while \(T=2\) has exactly two partitions once \(L\ge2\).

**Exact first triple representations.** If \(t\ge4\), (2) gives three representations from the \(j=0\) term at \(U=c(t)\). Every \(j\ge1\) needs
\[
 U\ge jd+\left\lceil\frac{t+ja}{3}\right\rceil
 \ge d+\left\lceil\frac{t+a}{3}\right\rceil
 \ge c(t)+1,
\]
using \(a\ge4\) and \(d\ge1\). Thus no higher \(j\) can produce an earlier third representation. When \(t=3\), the \(j=0\) term first reaches three at \(U=3\), and every higher term requires \(U\ge d+\lceil(3+a)/3\rceil\ge4\).

For \(t=2\), the \(j=0\) term has exactly two representations for \(U\ge2\). The earliest \(j\ge1\) contribution occurs at \(U=d+\lceil(a+2)/3\rceil\ge3\). This is therefore the first triple threshold.

For \(t=0,1\), the \(j=0\) term always has at most one representation. The \(j=1\) term acquires its second representation at \(U=d+b(a+t)\), yielding three in total. A \(j\ge2\) term cannot intervene sooner: its first possible index is at least
\[
 2d+\left\lceil\frac{t+2a}{3}\right\rceil
 \ge d+b(a+t),
\]
because \(a\ge4\), \(b(v)\le\lceil v/3\rceil+1\), and increasing \(j\) increases the minimum. Thus the proposed \(N_t\) are the exact first triple thresholds. The monotonicity of (1) proves the boxed residue law.

**The maximum.** The largest exception in residue \(dt\pmod a\) is \(M_t-a\), so \(F_3=\max_t M_t-a\). For \(t\ge4\), the expression \(M_t=a(\lceil t/3\rceil+1)+dt\) increases with \(t\). If \(a\ge5\), its last value \(M_{a-1}\) is exactly \(3d\) below \(M_2\), using the three classes of \(a\pmod3\); the \(t=3\) value is also smaller. If \(a=4\), direct substitution gives \(M_3<M_1\). In every case \(M_0\le\max\{M_1,M_2\}\). For \(a=3q\) the latter maximum is \(M_2=a(d+q+1)+2d\); for \(a=3q+2\) it is \(M_2=a(d+q+2)+2d\); and for \(a=3q+1\) it is
\[
 \max(M_1,M_2)=a(d+q+1)+d+\max(a,d).
\]
Subtracting \(a\) gives the stated formula for \(F_3\).

**The count of exceptions.** In residue \(dt\pmod a\) there are exactly \(N_t+\lfloor dt/a\rfloor\) nonnegative integers below \(M_t\). The residues \(dt\pmod a\) form a permutation, hence
\[
 \sum_{t=0}^{a-1}\left\lfloor\frac{dt}{a}\right\rfloor
 =\frac{(a-1)(d-1)}2.
\]
From the displayed \(N_t\), including the special \(N_3=3\), direct splitting into the three classes of \(a\pmod3\) yields
\[
 \sum_{t=0}^{a-1}N_t=3d+2a-1+\mathbf1_{a\equiv2\ (\mathrm{mod}\ 3)}+
 \sum_{t=0}^{a-1}\left\lceil\frac t3\right\rceil.
\]
Adding these contributions proves the formula for \(H_3\). \(\square\)

## Verification
The independently implemented coefficient-counting recurrence
\[
 [z^n]\prod_{j=0}^3(1-z^{a+jd})^{-1}=R_{a,d}(n)
\]
was evaluated by unbounded-knapsack dynamic programming in `verify.py`. For every tested coprime parameter pair the checker compares *all* nonnegative integers through two residue periods beyond the predicted maximum, checks the exact thresholds \(M_t\), and independently counts the exceptions. Tests are finite consistency evidence, not the proof of the infinite theorem.

Examples: \((a,d)=(4,1)\) gives \(M_0,M_1,M_2,M_3=(12,17,14,15)\), hence \(F_3=13\) and \(H_3=13\). When \(a=7\), the maximizing residue changes as \(d\) crosses \(a\), explaining the \(\max\{a,d\}\) term.

## Relationship to prior work
Komatsu and Ying (first posted 27 June 2022, arXiv:2206.13052) derive generalized Frobenius and genus formulas for three-term arithmetic progressions and explicitly identify longer progressions as a desired direction. Mohammed's 2017 dissertation (Cardiff repository 98161, Chapter 6) proves the **second** Frobenius threshold \(F_2(a,a+d,a+2d,a+3d)=a\lfloor a/3\rfloor+d(a+1)\) for \(1\le d<a\). That theorem concerns at least two, rather than at least three, representations; it does not imply the third threshold and its residue profile. Manjunath and Smith (arXiv:1703.10884) furnish general algorithms and structural results for arbitrary generalized Frobenius numbers, not a closed uniform four-term third-threshold classification. Beck and Kifer (arXiv:1005.2692) treat special extreme coefficient families and general elementary principles, not this family-wide piecewise formula.

## Limitations
The theorem is confined to four-term arithmetic progressions with \(a\ge4\), \(d\ge1\), and \(\gcd(a,d)=1\); it does not determine the fourth and higher Frobenius thresholds. The formula is a proof about distinct nonnegative integer representations and does not assert any independent validation or published priority. A previously unindexed equivalent formula or uninspected later revision remains a bibliographic possibility.

## References
1. T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052, first publicly posted 2022-06-27. https://arxiv.org/abs/2206.13052
2. D. H. Mohammed, *Generalised Frobenius numbers: geometry of upper bounds, Frobenius graphs and exact formulas for arithmetic sequences*, Cardiff University doctoral thesis, 2017, Chapter 6. https://orca.cardiff.ac.uk/id/eprint/98161/
3. M. Manjunath and B. Smith, *Commutative Algebra of Generalised Frobenius Numbers*, arXiv:1703.10884, 2017. https://arxiv.org/abs/1703.10884
4. M. Beck and C. Kifer, *An Extreme Family of Generalized Frobenius Numbers*, arXiv:1005.2692, 2010. https://arxiv.org/abs/1005.2692
