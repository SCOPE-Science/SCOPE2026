# Order-reversing square roots of chain idempotents: paired-rail factorization and rank equidistribution

## Finding

Let \([n]=\{1,\ldots,n\}\) be the totally ordered chain and \(\mathcal D_n\) the set of all order-reversing (weakly decreasing) total self-maps of \([n]\). Let \(\mathcal O_n\) denote all order-preserving (weakly increasing) total self-maps. For every idempotent \(e\in\mathcal O_n\), write its distinct fixed points as \(s_1<\cdots<s_k\). The fibers are intervals
\[
I_i=e^{-1}(s_i)=[a_i,b_i],\qquad L_i=s_i-a_i,\quad R_i=b_i-s_i.
\]
Define the polynomial
\[
H_{L,R}(v)=\sum_{j=0}^{\min(L,R)}(j+1)\binom Lj\binom Rj v^j\qquad(L,R\ge0).
\]
Then the complete **square-root fiber polynomial**, counting the image rank of \(f\) above the rank of its square, is
\[
\boxed{\begin{aligned}
\sum_{\substack{f\in\mathcal D_n\\ f^2=e}}v^{|\operatorname{im}f|-k}
={}&\prod_{i=1}^{\lfloor k/2\rfloor}
H_{L_i,R_{k+1-i}}(v)H_{R_i,L_{k+1-i}}(v)\\
&\times\begin{cases}
H_{L_{(k+1)/2},R_{(k+1)/2}}(v),&k\text{ odd},\\
1,&k\text{ even}.
\end{cases}
\end{aligned}}
\]
In particular every order-preserving idempotent has an order-reversing square root; the fiber depends explicitly on **opposite** left/right lengths, rather than only on the multiset of fiber sizes.

For example, when \(n=5\) and \(e\) is the constant map to the middle point, the antitone fiber polynomial is \(H_{2,2}(v)=1+8v+3v^2\), while the order-preserving square-root fiber has polynomial \((1+v)^2=1+2v+v^2\). Thus the global rank equality is not a pointwise equality and cannot be obtained by simply identifying individual square roots of a fixed idempotent.

The local polynomials have the rational double generating function
\[
\boxed{\sum_{L,R\ge0}H_{L,R}(v)x^Ly^R=
\frac{(1-x)(1-y)}{\big((1-x)(1-y)-vxy\big)^2}.}
\]

There is also a global equidistribution result. For every \(n\ge1\) and \(1\le k\le r\le n\),
\[
\boxed{\begin{aligned}
&\#\{f\in\mathcal D_n:f^4=f^2,\ |\operatorname{im}f^2|=k,\ |\operatorname{im}f|=r\}\\
&\qquad=\#\{g\in\mathcal O_n:g^3=g^2,\ |\operatorname{im}g^2|=k,\ |\operatorname{im}g|=r\}\\
&\qquad=\binom{k+r-1}{r-k}\binom{n+k-1}{2r-1}.
\end{aligned}}
\]
Thus, although decreasing transformations can interchange pairs of fixed points of their squares (and increasing transformations cannot), their entire joint image-rank distribution agrees with that of increasing quasi-idempotents. Equivalently, with an empty-map term at \(n=0\), their common ordinary generating function is
\[
\boxed{\sum_{n\ge0}z^n\!\sum_{\substack{f\in\mathcal D_n\\f^4=f^2}}
 u^{|\operatorname{im}f^2|}v^{|\operatorname{im}f|}
=\frac1{1-uvz\left(\frac{1-z}{(1-z)^2-vz^2}\right)^2}.}
\]
The isotone joint distribution and this rational function were previously published for \(\mathcal O_n\); the contributions established here are the **pointwise antitone square-root factorization** and the resulting antitone/isotone equidistribution.

## Assumptions and scope

All maps are total and weakly monotone on a finite, **labeled** chain. Composition uses \(f^2=f\circ f\). The set \(\mathcal D_n\) is not in general closed under composition, so the square condition is interpreted inside the full transformation monoid, not as a square in a subsemigroup \(\mathcal D_n\). A map is order-reversing when \(x\le y\) implies \(f(x)\ge f(y)\); constant maps belong to both \(\mathcal D_n\) and \(\mathcal O_n\), but are counted once in each respective set. The rank of a map is the cardinality of its image. The notation \([a_i,b_i]\) denotes a discrete integer interval, and \(s_i\) is its unique fixed point under \(e\). Binomial coefficients with out-of-range lower indices are zero. The generating functions are formal power series in commuting indeterminates.

For an order-reversing \(f\), the square \(f^2\) is order-preserving. The condition \(f^4=f^2\) is equivalent to idempotence of \(e=f^2\). For any monotone idempotent \(e\), every fiber is an interval containing exactly one point of \(\operatorname{im}e\), which is fixed by \(e\). The theorem is valid for every \(n\ge1\); the empty-map convention extends the generating function to \(n=0\).

## Proof

**1. Root reversal and the splitting into paired rails.** Fix an order-preserving idempotent \(e\) with fixed-point set \(S=\{s_1<\dots<s_k\}\). If an order-reversing \(f\) satisfies \(f^2=e\), it commutes with \(e\). Moreover \(f(S)=S\) and \(f|_S\) is an involution, because \(f^2|_S\) is the identity. As an order-reversing bijection of the ordered set \(S\), it is necessarily the unique reversal:
\[
f(s_i)=s_{k+1-i}.
\]
The commutation identity yields \(e(f(x))=f(e(x))\), hence
\[
f(I_i)\subseteq I_{k+1-i}.
\]
Since these target intervals themselves occur in opposite order, assignments on different source fibers are globally order-reversing exactly when the assignments on individual fibers are order-reversing. The two sides of \(s_i\) map into the opposite sides of \(s_{k+1-i}\). Thus the left rail in \(I_i\) couples to the right rail in \(I_{k+1-i}\), while the right rail in \(I_i\) couples independently to the left rail in \(I_{k+1-i}\). For \(i=(k+1)/2\) when \(k\) is odd, the two rails of the central fiber couple to each other. There are no further cross-fiber constraints.

**2. The paired-rail constraint.** Consider a coupled pair of rails with lengths \(L,R\). Write the values of \(f\), measured away from their respective root points, as two nondecreasing sequences
\[
a_0=0\le a_1\le\cdots\le a_L\le R,\qquad
b_0=0\le b_1\le\cdots\le b_R\le L.
\]
For example, for a left rail rooted at \(s_i\) sent to a right rail rooted at \(s_j\), take \(a_h=f(s_i-h)-s_j\) and \(b_h=s_i-f(s_j+h)\). The corresponding twofold map must return every point on each rail to its root. Therefore
\[
b_{a_h}=0\ (0\le h\le L),\qquad a_{b_h}=0\ (0\le h\le R).
\]
By monotonicity these conditions are equivalent to the **two endpoint tests**
\[
b_A=0,\qquad a_B=0,\qquad A=a_L,\quad B=b_R.
\]
Let \(j\) count the total number of distinct positive values appearing among \(a\) and \(b\). These values represent distinct non-root image points on distinct rails. We next count the allowed pairs by \(L,R,j\).

**3. Enumerating all two-rail solutions.** Put
\[
q=\frac{vxy}{(1-x)(1-y)}.
\]
If \(A=0\), all \(a_h=0\) and \(b\) is arbitrary nondecreasing. For \(j\) distinct positive values of \(b\), first choose those values in \(\binom Lj\) ways, and then choose the \(j\) positive constant runs among \(R\) positions in \(\binom Rj\) ways. Hence the contribution is
\[
\sum_{L,R,j\ge0}\binom Lj\binom Rj v^jx^Ly^R
=\frac1{(1-x)(1-y)(1-q)}.
\]
The case \(B=0\) gives the same expression with the rails exchanged; the case \(A=B=0\), counted twice, consists of a single all-zero pair for every \(L,R\), contributing \(1/((1-x)(1-y))\).

Suppose instead \(A,B>0\). Let \(j_a,j_b\ge1\) be the respective numbers of distinct positive values in the two sequences. The endpoint tests force \(a_1=\dots=a_B=0\) and \(b_1=\dots=b_A=0\). Given \(A,B,j_a,j_b\), choose the other positive values of \(a\) and \(b\) in
\[
\binom{A-1}{j_a-1}\binom{B-1}{j_b-1}
\]
ways. Choosing the successive nonempty positive-value runs after those initial forced zeros contributes
\[
\binom{L-B}{j_a}\binom{R-A}{j_b}.
\]
For a fixed positive \(j_a\), the sum over \(L,B\), and the corresponding sum over \(R,A\), can be performed using
\[
\sum_{m\ge j}\binom mj t^m=\frac{t^j}{(1-t)^{j+1}},\qquad
\sum_{A\ge j}\binom{A-1}{j-1}t^A=\frac{t^j}{(1-t)^j}.
\]
The joint contribution for given \(j_a,j_b\) becomes exactly
\[
\frac{q^{j_a+j_b}}{(1-x)(1-y)}.
\]
Summing over positive \(j_a,j_b\) produces \(q^2/((1-x)(1-y)(1-q)^2)\). Inclusion–exclusion over the cases above therefore gives
\[
\begin{aligned}
\sum_{L,R\ge0}H_{L,R}(v)x^Ly^R
&=\frac1{(1-x)(1-y)}
\left(\frac2{1-q}-1+\frac{q^2}{(1-q)^2}\right)\\
&=\frac1{(1-x)(1-y)(1-q)^2}\\
&=\frac{(1-x)(1-y)}{((1-x)(1-y)-vxy)^2}.
\end{aligned}
\]
Expansion of \((1-q)^{-2}=\sum_{j\ge0}(j+1)q^j\) gives the explicit coefficient
\[
[x^Ly^Rv^j]H(x,y;v)=(j+1)\binom Lj\binom Rj.
\]
In particular, the local factor always has constant term \(1\).

**4. Pointwise fiber formula.** Apply the preceding local count to both independent coupled rail pairs for each mirrored pair \((I_i,I_{k+1-i})\), and to the one coupled pair inside the central fiber when \(k\) is odd. Every root belongs to the image because \(f\) permutes the root set. Each distinct positive rail value gives exactly one further image point, with no repetitions between distinct target rails or target fibers. Consequently image rank equals \(k\) plus the sum of local positive-value counts. Multiplying the corresponding local polynomials proves the stated fiber identity and the existence of a root for every \(e\).

**5. Global rank equidistribution.** To sum over idempotents \(e\) with \(k\) roots, note that the ordered root-centered fibers are determined uniquely by the \(2k\) nonnegative side lengths \((L_i,R_i)\), with total chain length
\[
n=k+\sum_{i=1}^k(L_i+R_i).
\]
In the paired-fiber product, each of the \(k\) coupled rail pairs uses one left-side length and one right-side length exactly once. Summing independently over these lengths, with each length marked by \(z\), contributes the diagonal specialization \(H(z,z;v)\) for every coupled pair. Thus the fixed-\(k\) generating function is
\[
(uvzH(z,z;v))^k
=\left(uvz\left(\frac{1-z}{(1-z)^2-vz^2}\right)^2\right)^k.
\]
Taking the geometric series over \(k\ge0\) proves the displayed rational generating function. Write \(j=r-k\). Using
\[
\left(1-\frac{vz^2}{(1-z)^2}\right)^{-2k}
=\sum_{j\ge0}\binom{2k+j-1}{j}
\frac{v^jz^{2j}}{(1-z)^{2j}},
\]
the coefficient of \(z^nu^kv^r\) is
\[
\binom{2k+(r-k)-1}{r-k}\,[z^{n-k-2(r-k)}](1-z)^{-2r}
=\binom{k+r-1}{r-k}\binom{n+k-1}{2r-1}.
\]
For completeness, the isotone side of the equality has an independent rooted-interval count. If an order-preserving \(g\) satisfies \(g^3=g^2=e\), then \(g\) fixes each root and preserves each fiber of \(e\). On a one-sided rail of length \(a\), with the root indexed by \(0\), write a nondecreasing map \(h\) with \(h(0)=0\) and \(h^2\equiv0\). If it has \(j\) distinct positive image values and \(t=h(a)\), then \(h(0)=\cdots=h(t)=0\), the other \(j-1\) positive values may be selected in \(\binom{t-1}{j-1}\) ways, and the positive runs after position \(t\) in \(\binom{a-t}{j}\) ways. The standard convolution
\[
\sum_{t=j}^{a-j}\binom{t-1}{j-1}\binom{a-t}{j}=\binom a{2j}
\]
(and the all-zero case at \(j=0\)) shows the one-side generating function is
\[
\sum_{a,j\ge0}\binom a{2j}z^av^j=\frac{1-z}{(1-z)^2-vz^2}.
\]
Every isotone root-centered fiber has two independent one-sided rails, giving precisely the same \(k\)-root generating function as above. This also directly rederives the published isotone coefficient identity. The equality of rank distributions therefore follows without assuming a nonexistent per-map reversal of iteration type. All claims follow.

## Verification

Run `python3 verify.py` using only the Python standard library. The checker independently enumerates every order-reversing and every order-preserving total self-map on \([n]\) for \(1\le n\le9\), directly computes squares and checks idempotence, compares the complete image/stable-image rank table with the displayed binomial formula, and checks the **entire root-rank polynomial for every order-preserving idempotent target**. Separately, it exhaustively enumerates all pairs of nondecreasing side sequences satisfying the actual twofold-return constraints for \(0\le L,R\le6\) and checks the local \(H_{L,R}(v)\) coefficients. Its successful final line is `ANTITONE_SQUARE_ROOT_THEOREM_FINITE_CHECKS_PASSED`; actual output is supplied as `verification_output.txt`.

The total number of square-idempotent order-reversing maps for \(n=1,\ldots,9\) is respectively \(1,3,10,33,108,352,1145,3721,12087\). These finite calculations corroborate but do not replace the general combinatorial proof.

## Relationship to prior work

Li and Fernandes (2022) develop the monoid of order-preserving or order-reversing total transformations of a finite chain and its endomorphisms, with precise identification of the order-reversing part. Fernandes, Gomes and Jesus (2005) study structural and congruence properties of these monotone transformation monoids. Neither inspected treatment determines the pointwise antitone square-root fibers or their image-rank polynomials.

Imam and coauthors (2023) study quasi-idempotents in the **order-preserving** transformation monoid. A previously published explicit joint stable-image/image-rank formula for those order-preserving quasi-idempotents is exactly the final binomial expression above. That expression, its rational generating function, and the corresponding univariate sequence are **not** claimed original. Their equality with the antitone counts is a new comparison established by the paired-rail calculation; the stronger pointwise antitone root formula is the central contribution. A known result on square-root fibers in an **injective partial** Catalan monoid concerns different maps, so it does not directly cover full nonincreasing transformations.

## Limitations

This theorem concerns total weakly decreasing maps on a finite chain and exact equations \(f^2=e\) where \(e\) is order-preserving and idempotent. It does not classify all iterative roots of arbitrary transformations, general periodic powers, nonmonotone maps, or partial maps. It also does not give an explicit constructive bijection between increasing and decreasing solutions with the same ranks; equality of counts is established by their generating functions. The numerical equidistribution is strongly related to a prior published isotone formula; novelty is limited to the antitone pointwise decomposition and its comparison with that prior formula. An unlocated general theory of monotone transformation roots could subsume the theorem, and publication priority would require further independent checking. The finite enumerations are evidence, not an independent infinite proof. No independent audit is asserted.

## References

1. D. B. Li and V. H. Fernandes, *Endomorphisms of semigroups of monotone transformations*, first arXiv version posted 2022-04-16, https://arxiv.org/abs/2204.07838 .
2. V. H. Fernandes, G. M. S. Gomes and M. M. Jesus, *Congruences on Monoids of Order-Preserving or Order-Reversing Transformations on a Finite Chain*, Glasgow Mathematical Journal 47 (2005), 413–424; https://doi.org/10.1017/S0017089505002648 .
3. A. T. Imam, S. Ibrahim, G. U. Garba, L. Usman and A. Idris, *Quasi-idempotents in finite semigroup of full order-preserving transformations*, Algebra and Discrete Mathematics 35 (2023), 62–72; https://doi.org/10.12958/adm1846 .
4. *Joint stable-rank and image-rank enumeration of quasi-idempotents on a finite chain*, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-joint-stable-rank-and-image-rank-enumeration-of-quasi-idempotent--12bb479c61e2 .
5. *Motzkin square-root fibers and a Rayleigh fixed-point law in injective partial Catalan monoids*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-motzkin-square-root-fibers-and-a-rayleigh-fixed-point-law-in-inj--d449e4ff8b1b .
