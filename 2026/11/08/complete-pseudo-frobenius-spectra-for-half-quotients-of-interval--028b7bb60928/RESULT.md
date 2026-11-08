# Complete pseudo-Frobenius spectra for half-quotients of interval numerical semigroups

## Finding
For every odd integer \(a\ge5\) and integer \(3\le k\le a-2\), let \(S_{a,k}=\langle a,a+1,\ldots,a+k\rangle\) and \(Q_{a,k}=\{x\in\mathbb N_0:2x\in S_{a,k}\}\). Put
\[
r=(a-1)/2,\qquad T=\lfloor(a-3)/k\rfloor,\qquad
L_j=\lfloor j(a+k)/2\rfloor+1,\qquad
U_j=\lfloor((j+1)a-1)/2\rfloor.
\]
Here a *gap* is a positive integer outside the semigroup. A *pseudo-Frobenius number* is a gap \(x\) such that \(x+s\in Q_{a,k}\) for every positive \(s\in Q_{a,k}\).

**Theorem.** The complete gapset is the disjoint union
\[
G(Q_{a,k})=\bigsqcup_{j=0}^{T}[L_j,U_j]\cap\mathbb Z.
\]
In particular, the Frobenius number and genus are
\[
F(Q_{a,k})=U_T,
\qquad
 g(Q_{a,k})=\sum_{j=0}^{T}\left(r-\left\lceil\frac{kj}{2}\right\rceil\right).
\]
The *entire pseudo-Frobenius spectrum* is
\[
\operatorname{PF}(Q_{a,k})=[L_T,U_T]\cap\mathbb Z\ \cup\ E_{a,k},
\]
where the union is disjoint and
\[
E_{a,k}=\begin{cases}
\{U_{T-1}\},& T\ge1\text{ odd},\\
\{L_{T-1}\},& T\ge2\text{ even and }k\text{ even},\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
Consequently, the type, the number of pseudo-Frobenius numbers, is
\[
t(Q_{a,k})=r-\left\lceil\frac{kT}{2}\right\rceil+
\boldsymbol{1}_{\{T\text{ odd}\}}+
\boldsymbol{1}_{\{T\ge2\text{ even and }k\text{ even}\}}.
\]

## Assumptions and scope
All variables are integers. The base \(a\) is odd, \(a\ge5\); the interval length satisfies \(3\le k\le a-2\). The quotient divisor is exactly two, which does not divide \(a\). The genus and Frobenius number refer to \(Q_{a,k}\), not \(S_{a,k}\). Intervals \([v,w]\cap\mathbb Z\) include both endpoints. The definition of pseudo-Frobenius number uses all positive semigroup elements; checking a generating set is equivalent.

## Proof
**1. Gap intervals and extremal statistics.** For each integer \(j\ge0\), the sums of exactly \(j\) generators from the interval \(\{a,\ldots,a+k\}\) comprise the integer interval \([ja,j(a+k)]\). Thus \(S_{a,k}=\bigcup_{j\ge0}([ja,j(a+k)]\cap\mathbb Z)\). Consecutive blocks leave a (possibly empty) gap \([j(a+k)+1,(j+1)a-1]\). Selecting its even numbers and dividing by two gives exactly \([L_j,U_j]\cap\mathbb Z\). Its cardinality is \(r-\lceil kj/2\rceil\), positive if and only if \(kj\le a-3\). The last nonempty block has index \(T\); all later source intervals overlap or abut, proving the asserted complete gapset, Frobenius number and genus.

**2. Explicit quotient generators.** Write \(a=2r+1\), \(m=r+1\) and \(h=\lfloor(k-1)/2\rfloor\). Then
\[
Q_{a,k}=\langle m,m+1,\ldots,m+h,\ a\rangle
\quad\text{if }k\text{ is odd},
\]
while when \(k\) is even one must also include \(a+k\). Indeed, to represent an even element of \(S_{a,k}\), occurrences of odd source generators (even offsets from \(a\)) may be paired. Each such pair has half-sum \(a+i\) for some \(0\le i\le2\lfloor k/2\rfloor\). All these half-sums belong to the proposed generated semigroup: \(a\) is listed; sums of two among \(m,\ldots,m+h\) include the entire interval \([a+1,a+2h+1]\); when \(k\) is even the one remaining value is \(a+k\). Individual even source generators halve to \(m,m+1,\ldots,m+h\). Conversely, each proposed generator evidently doubles to an element of \(S_{a,k}\). This proves equality.

**3. Only the final two gap intervals can contribute.** For \(0\le j\le T\), the block length is at most \(r=m-1\). Hence \(x+m>U_j\) for any \(x\in[L_j,U_j]\). It follows immediately that every gap in the final block \([L_T,U_T]\) is pseudo-Frobenius, since it becomes greater than \(F(Q_{a,k})\) after adding the smallest positive generator \(m\).

For a gap \(x\in[L_j,U_j]\) with \(j<T\), the consecutive translates \(x+m,x+m+1,\ldots,x+m+h\) are strictly above \(U_j\) and strictly below \(L_{j+2}\). For instance, \(U_j+m+h<L_{j+2}\) follows from \(h<k\) and the endpoint definitions. Thus these translates can meet only the next gap block \([L_{j+1},U_{j+1}]\). Since they form an interval of integers, avoiding that block requires either
\[
x+m>U_{j+1}\qquad\text{or}\qquad x+m+h<L_{j+1}.
\]
To analyze these inequalities use
\[
U_{j+1}-U_j-m=\begin{cases}-1,&j\text{ even},\\0,&j\text{ odd},\end{cases}
\]
and
\[
L_{j+1}-L_j-m-h=\begin{cases}1,&j\text{ odd and }k\text{ even},\\0,&\text{otherwise}.
\end{cases}
\]
The only possible survivors are therefore \(x=U_j\) for even \(j\), and \(x=L_j\) for odd \(j\) and even \(k\). (The two possibilities cannot coincide at a fixed index.)

For \(j\le T-2\), the right-endpoint survivor fails because \(U_j+a=U_{j+2}\) is another gap; the left-endpoint survivor fails because \(L_j+(a+k)=L_{j+2}\) is another gap, with \(a+k\) a quotient generator in the even-\(k\) case. Therefore no gap from any block before \(T-1\) is pseudo-Frobenius.

**4. The penultimate block.** If \(j=T-1\) is even (equivalently \(T\) is odd), its sole possible survivor \(U_{T-1}\) passes: adding \(m\) already exceeds \(U_T=F(Q_{a,k})\), so adding any positive element also exceeds the Frobenius number. If \(j=T-1\) is odd and \(k\) even (equivalently \(T\ge2\) even and \(k\) even), its survivor \(L_{T-1}\) has all translates by \(m,\ldots,m+h\) between the penultimate gap block and the final one; its translates by the remaining generators \(a\) and \(a+k\) exceed \(U_T\). It is therefore pseudo-Frobenius. All other candidates fail by step 3. Counting the final block and the possible singleton proves the type formula, including \(T=0\).

## Verification
A standalone exact-integer Python checker is included as `artifacts/check.py`. It independently reconstructs all gaps from the Apéry residue graph of the displayed quotient generators and checks pseudo-Frobenius membership against every generator for all 5,476 pairs with odd \(5\le a\le151\) and \(3\le k\le a-2\). It also computes reachability from the *original* interval generating set by an independent integer dynamic program on eight representative examples. Run `python3 artifacts/check.py`; its deterministic output is included as `artifacts/check_output.txt`. All checks passed. This finite evidence supplements the infinite symbolic argument above and does not substitute for it.

For instance, \((a,k)=(21,4)\) gives \(F=52\), \(g=30\), and \(\operatorname{PF}=\{38,51,52\}\). The parity-dependent isolated extra pseudo-Frobenius gap is present at \(38\).

## Relationship to prior work
Adeniran, Butler, Defant, Gao, Harris, Hettle, Liang, Nam, and Volk (2018) studied genera and Frobenius numbers of numerical-semigroup quotients and posed arithmetic-progression quotient problems. Liu (2023a) obtained quotient Apéry/Frobenius results for almost arithmetic progressions under a divisibility condition on the first generator; it does not apply to the odd-base quotient by two here. Liu (2023b) developed general generating-function and generator methods for quotients; existence of such general methods does not give the explicit pseudo-Frobenius spectrum or type computed here. Bogart, O'Neill and Woods (2023) studied geometric and quotient-rank properties rather than these exact invariants. General pseudo-Frobenius methods are classical; no priority claim is made for their definitions or for gap interval decompositions themselves.

## Limitations
This theorem covers odd starting generators and half-quotients only, with \(k\ge3\). It neither classifies quotients by arbitrary divisors nor claims a general formula for all interval-generated semigroups. Literature searching does not prove absence of unpublished or unindexed equivalent results; independent validation has not been performed.

## References
- A. Adeniran et al., *On the Genus of a Quotient of a Numerical Semigroup* (first posted 2018-09-25), arXiv:1809.09360, https://arxiv.org/abs/1809.09360.
- F. Liu, *On quotients of numerical semigroups for almost arithmetic progressions* (first posted 2023-12-11), arXiv:2312.06096, https://arxiv.org/abs/2312.06096.
- F. Liu, *Generating functions for the quotients of numerical semigroups* (first posted 2023-12-18), arXiv:2312.10889, https://arxiv.org/abs/2312.10889.
- T. Bogart, C. O'Neill and K. Woods, *Numerical semigroups via projections and via quotients* (first posted 2023-06-20), arXiv:2306.11564, https://arxiv.org/abs/2306.11564.
