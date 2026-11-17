# Complete two-sum fibers and sumset growth of modular hyperbolas over odd prime powers

## Finding
Fix an odd prime \(p\) and an integer \(k\geq2\), put \(Q=p^k\), and let \(R=\mathbb Z/Q\mathbb Z\), \(U=R^\times\). The multiplicative hyperbola is
\[
H=\{(x,x^{-1}):x\in U\}\subset R^2.
\]
For \((s,t)\in R^2\), let \(r(s,t)\) count **ordered** representations of \((s,t)\) as the sum of two points of \(H\). Write \(\nu_p(0)=k\), and truncate every other valuation at \(k\). Put \(\varphi_j=(p-1)p^{j-1}\) for \(j\geq1\). The complete representation law is as follows.

* If \(s=t=0\), then \(r(s,t)=\varphi_k\).
* If \(\nu_p(s)\ne\nu_p(t)\), then \(r(s,t)=0\).
* If \(\nu_p(s)=\nu_p(t)=v<k\), put \(m=k-v\), choose the canonical integer representatives of \(s,t\), and define the units \(\sigma=s/p^v\), \(\tau=t/p^v\) in \(\mathbb Z/p^m\mathbb Z\). Set
\[
\Delta=s^2-4\sigma\tau^{-1}\pmod{p^m}.
\]
Then
\[
\boxed{r(s,t)=p^v\mathcal R_m(\Delta)},
\]
where the *exact* square-root count is
\[
\mathcal R_m(\Delta)=\begin{cases}
p^{\lfloor m/2\rfloor},&\Delta\equiv0\pmod{p^m},\\
2p^j,&\nu_p(\Delta)=2j<m\text{ and }\Delta/p^{2j}\text{ is a square modulo }p,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus the theorem specifies every zero and every positive fiber, not merely a maximal fiber size.

Define the number of nonunit squares (including zero) in \(\mathbb Z/p^k\mathbb Z\) by
\[
B_{p,k}=1+\frac12\sum_{j=1}^{\lfloor(k-1)/2\rfloor}\varphi_{k-2j}.
\]
Then the twofold sumset and ordered additive energy have the exact forms
\[
\boxed{|H+H|=1+\varphi_k\left(\frac{(p-3)p^{k-1}}2+B_{p,k}\right)
       +\frac12\sum_{m=1}^{k-1}\varphi_m^2},
\]
\[
\boxed{E(H):=\sum_{s,t\in R}r(s,t)^2
       =3(p-1)p^{2k-2}\bigl(k(p-1)-1\bigr).}
\]
For the complete modular Kloosterman sum
\[
K_Q(a,b)=\sum_{x\in U}\exp\left(\frac{2\pi i}{Q}(ax+bx^{-1})\right),
\]
character orthogonality gives the exact two-parameter fourth moment
\[
\boxed{\frac1{Q^2}\sum_{a,b\in R}|K_Q(a,b)|^4=E(H).}
\]
All displayed formulas extend to any **odd composite modulus** by the Chinese remainder theorem: the representation function, sumset size, and energy factor over its prime-power factors. The prime case \(k=1\), included by the same equations, recovers the already known field energy \(3(p-1)(p-2)\); novelty is asserted only for prime-power depth at least two and the complete ring-level fiber and sumset classification.

## Assumptions and scope
The modulus is odd throughout, so two is invertible and ordinary Hensel lifting applies to unit square roots. No statement about even moduli, optimal weighted Fourier extension norms, or the distribution of individual Kloosterman values is made. Values of \(r\) are ordered-pair counts. Valuations and discriminants always use the stated prime-power modulus; the integer representatives only specify how to divide by \(p^v\), and the result is independent of that choice modulo \(p^m\). Fourth moments use the **unnormalized** complete Kloosterman sum, then an outer average over all \(Q^2\) frequency pairs.

## Proof
**1. Exact fibers.** For units \(x,y\) with \(x+y=s\), the inverse-sum identity is \(x^{-1}+y^{-1}=s/(xy)\). Since \(xy\) is a unit, \(\nu_p(s)=\nu_p(t)\). For \(s=0\), necessarily \(t=0\); each unit \(x\) has unique partner \(-x\), giving \(\varphi_k\) ordered representations.

When both valuations equal \(v<k\), divide \(txy\equiv s\pmod{p^k}\) by \(p^v\). This yields \(xy\equiv\sigma\tau^{-1}\pmod{p^m}\), and on substituting \(y=s-x\),
\[
x^2-sx+\sigma\tau^{-1}\equiv0\pmod{p^m}.
\]
Because two is invertible, the substitution \(z=2x-s\) reduces this congruence bijectively to \(z^2\equiv\Delta\pmod{p^m}\). Each root modulo \(p^m\) has exactly \(p^v\) lifts modulo \(p^k\). Every lift has \(x\) and \(s-x\) units: if \(v=0\), their product is a unit; if \(v>0\), \(s\equiv0\pmod p\) and their product is a unit. The resulting count is exactly \(p^v\mathcal R_m(\Delta)\).

For completeness, if \(\Delta\equiv0\pmod{p^m}\), roots are exactly the multiples of \(p^{\lceil m/2\rceil}\), numbering \(p^{\lfloor m/2\rfloor}\). Otherwise an odd valuation rules out a square. If \(\nu_p(\Delta)=2j<m\), writing \(z=p^j w\) reduces to the unit congruence \(w^2\equiv\Delta/p^{2j}\pmod{p^{m-2j}}\). A nonzero quadratic residue has exactly two roots by Hensel lifting, each yielding \(p^j\) values of \(z\); a nonresidue has none. This proves the complete root-count formula, including all degenerate cases.

**2. Exact sumset size.** For \(1\le v\le k-1\), fix \(s\) of valuation \(v\). The discriminant above is a unit whose residue equals \(-4\sigma\tau^{-1}\pmod p\). As \(t\) ranges over its \(\varphi_m\) possible values of valuation \(v\), exactly half make that residue a quadratic square. Hence there are exactly \(\varphi_m/2\) nonempty targets above each such \(s\), and there are \(\varphi_m\) choices of \(s\).

If \(s\) is a unit, \(t\) must also be a unit, and the map \(t\mapsto\Delta=s^2-4s/t\) is a bijection from units to discriminants satisfying \(\Delta\not\equiv s^2\pmod p\). Among unit squares modulo \(p^k\), exactly \(\varphi_k/2\) occur; exactly \(p^{k-1}\) have residue \(s^2\pmod p\) and must be excluded. Thus \((p-3)p^{k-1}/2\) admissible unit squares remain. Nonunit squares consist of zero and squares of valuations \(2,4,\ldots<k\); the number at valuation \(2j\) is \(\varphi_{k-2j}/2\). This gives the stated \(B_{p,k}\) additional admissible discriminants. There are \(\varphi_k\) unit values of \(s\), and one target at \(s=0\). Adding the three cases gives the sumset formula.

**3. Exact energy.** The zero-sum fiber contributes \(\varphi_k^2\). For each \(v\ge1\), the \(\varphi_{k-v}/2\) populated targets over each of \(\varphi_{k-v}\) first-coordinate sums have multiplicity exactly \(2p^v\). Their squared sum therefore equals \(2p^{2v}\varphi_{k-v}^2=2\varphi_k^2\). There are \(k-1\) such valuation classes.

It remains to compute \(T(s):=\sum_t r(s,t)^2\) for a unit \(s\). Write \(x=sz\), \(y=s(1-z)\). Then \(z,1-z\) must be units, and two such ordered pairs produce the same inverse-sum coordinate exactly when
\[
z(1-z)\equiv w(1-w)\pmod{p^k},\quad\text{equivalently}\quad(z-w)(1-z-w)\equiv0\pmod{p^k}.
\]
For each \(z\not\equiv0,1,1/2\pmod p\), the two distinct simple roots \(w\equiv z,1-z\pmod p\) lift uniquely to solutions modulo \(p^k\). These contribute \(2(p-3)p^{k-1}\) ordered collision pairs. If \(z\equiv1/2\pmod p\), the partner must have the same residue. Put \(z=1/2+pa\), \(w=1/2+pb\) modulo \(p^k\); the condition is \(a^2\equiv b^2\pmod{p^{k-2}}\). Each residue pair modulo \(p^{k-2}\) has \(p^2\) lifts to the possible \(a,b\) modulo \(p^{k-1}\).

The number of pairs \((a,b)\pmod{p^j}\) with \(a^2=b^2\) is
\[
D_j=p^j+j(p-1)p^{j-1}\quad(j\ge1),\qquad D_0=1.
\]
Indeed, the invertible linear change \((a,b)\mapsto(a-b,a+b)\) reduces this to counting products zero modulo \(p^j\): the first factor zero contributes \(p^j\) possibilities; each of its \(j\) nonzero valuation classes contributes exactly \((p-1)p^{j-1}\) possibilities. Hence the critical residue class contributes \(p^2D_{k-2}=p^k+(k-2)(p-1)p^{k-1}\), and
\[
T(s)=2(p-3)p^{k-1}+p^k+(k-2)(p-1)p^{k-1}
=p^{k-1}\bigl((k+1)p-k-4\bigr).
\]
There are \(\varphi_k\) unit first-coordinate sums. Consequently
\[
E(H)=(2k-1)\varphi_k^2+\varphi_k p^{k-1}\bigl((k+1)p-k-4\bigr)
=3(p-1)p^{2k-2}\bigl(k(p-1)-1\bigr).
\]

**4. Fourier and composite moduli.** Expanding \(\sum_{a,b}|K_Q(a,b)|^4\) and summing both additive characters yields \(Q^2\) precisely for quadruples whose two graph-point sums agree and zero otherwise. This proves the fourth-moment identity. For an odd composite \(N=\prod_i p_i^{k_i}\), the ring is the direct product of its prime-power factors. Units, graph points, sum representations, Fourier characters, and ordered additive-energy equations all factor componentwise. Therefore \(r_N(s,t)=\prod_i r_{p_i^{k_i}}(s_i,t_i)\), \(|H_N+H_N|=\prod_i|H_{p_i^{k_i}}+H_{p_i^{k_i}}|\), and \(E(H_N)=\prod_i E(H_{p_i^{k_i}})\).

## Verification
A self-contained exact-integer checker, `CHECK.py`, recomputes every ordered pair sum, every predicted individual fiber, the sumset size, and the energy for 13 prime-power test moduli, including \(3^4\), \(5^3\), \(7^3\), and \(11^2\). It also checks the Chinese-remainder predictions on nine odd composite moduli. The saved-package replay reports `CHECK_OK moduli=22 target_slots=231934 all_multiplicities_exact=True`. Examples are \((p,k)=(3,3)\) giving \(|H+H|=57\), \(E(H)=2430\), and \((p,k)=(5,3)\) giving \(|H+H|=3009\), \(E(H)=82500\). These finite checks are corroborative; the proof above covers every odd prime and every exponent at least two.

## Relationship to prior work
Iosevich, Li, and Yu (2026) relate Fourier concentration on finite residue rings to fourth moments and additive energy, with exact divisor-sum synthesis constants for paraboloids. Their September 2026 paper provides the present motivation but does not classify the inverse-graph twofold convolution or the cardinality of its sumset. Iosevich, Murphy, and Pakianathan (2014) study the same modular hyperbolas via Kloosterman Fourier decay and the square-root law; their examined theorems and sections do not determine these pair-sum fibers. Gong, Veys, and Wan (2013/2016) give deep formulas for **one-parameter** Kloosterman power moments; these may imply parts of the energy corollary after additional frequency decompositions, but do not specify the positionwise ordered two-sum fibers or their nonzero target set.

The published result *Sharp fourth-moment extension on the finite-field multiplicative hyperbola* (2026) already determines \(E(H)=3(p-1)(p-2)\) **over fields**; that exponent-one specialization is expressly not asserted as new. The published result *Sharp orthogonal exponential capacity and digit-tree rigidity of prime-power modular hyperbolas* (2026) treats the same ring hyperbola but addresses orthogonality of restricted characters, not its additive two-sum fibers. The more recent finite-field *zero-completed inverse graph* extension work treats a different graph over fields. The structural new claim here concerns all residue-ring depths at least two, including the degenerate discriminant strata and exact sumset growth.

## Limitations
The formula for the fourth moment is **constant-input** and averaged over **both** frequency variables; it is not an optimal weighted Fourier-extension bound or an identity for one-frequency moments. No even-modulus formula is claimed. General Hensel lifting and quadratic square counts are classical and are not claimed as original. Some energy consequences may be recoverable indirectly from earlier Kloosterman moment formulas; independent priority review of the full fiber and sumset classification is outstanding.

## References
1. A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404v1, first public 2026-09-21; Sections 4, 6, and 8.
2. A. Iosevich, B. Murphy, J. Pakianathan, *The square root law and structure of finite rings*, arXiv:1405.7657v1, first public 2014-05-29; Sections 1–2 and 5.
3. K. Gong, W. Veys, D. Wan, *Power moments of Kloosterman sums*, arXiv:1306.4104v1, first public 2013-06-18; especially the definition of one-parameter moments and Theorem 4 of the revised manuscript.
4. *Sharp fourth-moment extension on the finite-field multiplicative hyperbola* (public mathematical result, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-fourth-moment-extension-on-the-finite-field-multiplicative--0835fe791166 .
5. *Sharp orthogonal exponential capacity and digit-tree rigidity of prime-power modular hyperbolas* (public mathematical result, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-orthogonal-exponential-capacity-and-digit-tree-rigidity-of--debdea61056e .
6. *Sharp Fourier extension on the zero-completed finite-field inverse graph* (public mathematical result, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourier-extension-on-the-zero-completed-finite-field-inver--b05317385d5a .
