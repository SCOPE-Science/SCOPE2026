# Exact first-two failure frequencies and a sharp stabilization criterion for reciprocal-sum squares

## Finding

Fix any integer \(h\geq1\), put \(k=h^2\), and for each positive integer \(x_0\) define positive rationals by
\[
x_{n+1}=\frac{h^2}{x_0+x_1+\cdots+x_n}\quad(n\geq0),
\qquad x_n=\frac{a_n}{b_n},\quad\gcd(a_n,b_n)=1.
\]
For \(n\geq2\), call \(n\) a *failure* when \(b_n+2a_n/h\) is not the square of an integer. For each prime power \(p^e\parallel h\), put \(q_p=p^{e+1}\), and define
\[
c_p=\begin{cases}
1,&p=2,\\
2,&p\equiv1\pmod4,\\
0,&\text{otherwise},
\end{cases}
\qquad
r_p=\begin{cases}
2,&p=5,\\
4,&p\equiv1,9\pmod{20},\\
0,&\text{otherwise},
\end{cases}
\qquad\alpha_p=\frac{c_p}{q_p},\quad\beta_p=\frac{r_p}{q_p}.
\]
The four **exact natural densities** of the failure indicators at indices \(2\) and \(3\), in the order (neither, only \(2\), only \(3\), both), are
\[
\boxed{\begin{aligned}
P_{00}&=\prod_{p^e\parallel h}(1-\alpha_p-\beta_p),\\
P_{10}&=\prod_{p^e\parallel h}(1-\beta_p)-P_{00},\\
P_{01}&=\prod_{p^e\parallel h}(1-\alpha_p)-P_{00},\\
P_{11}&=1-\prod_{p^e\parallel h}(1-\alpha_p)-\prod_{p^e\parallel h}(1-\beta_p)+P_{00}.
\end{aligned}}
\]
Empty products equal \(1\). These are not just limits: the four proportions are exact on the residue classes modulo \(M(h)=\prod_{p^e\parallel h}p^{e+1}\), with error \(O_h(1)\) in counts of starts \(1\leq x_0\leq X\).

Moreover, the following statements are equivalent:

1. For **every** positive integer start \(x_0\), **every** index \(n\geq3\) is a square (not a failure).
2. No prime dividing \(h\) equals \(5\) or is congruent to \(1\) or \(9\) modulo \(20\).

In this class, the *complete* number of failures is either \(0\) or \(1\). Exactly one failure occurs with natural density
\[
\boxed{\delta(h)=1-\prod_{p^e\parallel h}(1-\alpha_p),}
\]
and, if it occurs, its index is exactly \(2\). Every excluded prime \(p\mid h\) yields some positive start with a failure at index \(3\), so the classification is sharp.

Examples: for \(h=13\), exactly \(2/169\) of starts have one failure, at index \(2\). For \(h=26\), the exact density is \(175/676\). For \(h=5\), the probabilities of a failure at indices \(2\) and \(3\) are each \(2/25\), and they cannot both occur for the same start.

## Assumptions and scope

Integers \(h,x_0\) are positive and fixed/variable respectively, with no upper bound. The arithmetic is over the integers and rational numbers; density is natural density over starts \(x_0\geq1\). A *square* means an integer square, not a rational square. The classification is universal in the initial value; the two-time joint distribution is valid for **every** multiplier \(h\), including those failing the stabilization criterion. It does not assert a full failure-count distribution outside the stabilized class.

## Proof

**1. The published reduction.** Put \(S_n=x_0+\cdots+x_n\) and write \(S_n/h=u_n/v_n\) in lowest terms, where \(u_0=x_0/d\), \(v_0=h/d\), \(d=\gcd(x_0,h)\). Then
\[
u_{n+1}=u_n^2+v_n^2,\qquad v_{n+1}=u_nv_n,
\qquad \gcd(u_n,v_n)=1.
\]
Matijasevick--Rodríguez--Salazar, Proposition 4.1(a), proves that index \(n+1\geq2\) is a failure if and only if \(\gcd(h,u_n)>1\). We take this precise equivalence (including its integer-square, rather than rational-square, direction) from the cited paper. The two iterates' homogeneous numerator polynomials are
\[
u_1=u_0^2+v_0^2,\qquad
u_2=u_0^4+3u_0^2v_0^2+v_0^4.
\]
Thus a prime dividing \(h\) causes a failure at \(2\) exactly when it divides \(u_1\), and at \(3\) exactly when it divides \(u_2\).

**2. Local root counts.** For each \(p^e\parallel h\), put \(H=h/p^e\), so \(p\nmid H\). If \(p^e\nmid x_0\), then \(p\mid v_0\) and \(p\nmid u_0\), making both \(u_1,u_2\) nonzero modulo \(p\). If \(p^e\mid x_0\), the projective initial ratio modulo \(p\) equals \(z=(x_0/p^e)H^{-1}\pmod p\). Consequently the local events are
\[
E_{2,p}:\ z^2+1=0\pmod p,
\qquad
E_{3,p}:\ z^4+3z^2+1=0\pmod p.
\]
Each distinct root \(z\pmod p\) corresponds to exactly one residue class for \(x_0\pmod{p^{e+1}}\). The first polynomial has exactly one root for \(p=2\), two for odd \(p\equiv1\pmod4\), and none otherwise: hence \(c_p\).

For \(p=2\), the quartic has no root; for odd \(p\equiv3\pmod4\), it has none because it is a sum of two squares \((z^2+1)^2+z^2\), and a root would force \(-1\) to be a square. For \(p=5\), it is \((z^2-1)^2\), with exactly two distinct roots. For odd \(p\ne5\), any root requires \((2z^2+3)^2=5\). If \(s^2=5\), its two possible quadratic values satisfy
\[
z^2=\frac{-3\pm s}{2}=-\left(\frac{s\mp1}{2}\right)^2,
\]
where neither right-hand square factor vanishes. Thus it has roots if and only if \(5\) and \(-1\) are both quadratic residues modulo \(p\), namely \(p\equiv1,9\pmod{20}\) by quadratic reciprocity. In that event it has four distinct roots. These are exactly the stated \(r_p\). The local root sets are disjoint: if \(z^2+1=0\), the quartic equals \(z^2=-1\ne0\pmod p\).

**3. Joint density.** For every prime divisor \(p\mid h\), the three local states (no failure at either index, failure at \(2\), failure at \(3\)) have exact probabilities \(1-\alpha_p-\beta_p\), \(\alpha_p\), \(\beta_p\) modulo \(p^{e+1}\). Chinese remaindering makes these states independent among distinct primes. Thus the probability of no failures is \(P_{00}\); the probabilities of no failure at one specified index are \(\prod_p(1-\alpha_p)\) and \(\prod_p(1-\beta_p)\). Subtraction and inclusion-exclusion yield all four displayed densities. Every event is periodic modulo \(M(h)\), so residue proportions give true natural densities and counting errors \(O_h(1)\).

**4. No delayed failures when the quartic has no root.** From the homogeneous recurrence,
\[
u_{j+2}=u_j^4+3u_j^2v_j^2+v_j^4
\qquad(j\geq0).
\]
If \(p\mid u_{j+2}\), coprimality implies \((u_j,v_j)\not\equiv(0,0)\pmod p\). Neither coordinate can vanish modulo \(p\), since setting one to zero would make the displayed expression a nonzero fourth power. Dividing by \(v_j^4\) therefore yields a root of the quartic modulo \(p\). Hence if \(r_p=0\), this prime divides no \(u_n\) with \(n\geq2\). If every \(p\mid h\) has \(r_p=0\), Proposition 4.1(a) shows there are no failures for \(n\geq3\); then only index \(2\) remains, with density \(1-\prod_p(1-\alpha_p)\) by step 3.

**5. Sharp converse.** If \(p\mid h\) has \(r_p>0\), choose an integer \(z\geq1\) with \(z^4+3z^2+1\equiv0\pmod p\). The positive start \(x_0=hz\) has \((u_0,v_0)=(z,1)\), so \(p\mid u_2\) and index \(3\) fails by Proposition 4.1(a). Thus universal stabilization fails whenever \(h\) contains an excluded prime. This also proves the asserted equivalence without any finite-search assumption.

## Verification

Run `python3 verify.py` using only the Python standard library. The independent exact-rational recurrence check covers 720 early terms. Modular checks verify the quartic root classification for all 168 primes through 1000, the complete residue periods for 22 stabilized multipliers (324753 classes), and the complete first-two joint distribution for 12 general multipliers (333461 classes). An excluded prime is independently shown to give an index-3 failure for every such prime through 1000. These are finite checks; the proof's infinite scope follows from steps 1--5, not from the numerical range.

## Relationship to prior work

Matijasevick--Rodríguez--Salazar (arXiv:2610.00765v1, September 30, 2026) prove the reduction to a coprime quadratic recurrence, the square criterion, and a bound of one bad term per relevant prime. Their Section 7(1) asks for the proportions of starts with a given number of failures. None of those prior premises is claimed here. The new result counts both first-level and second-level obstruction fibers, proves their exact joint distribution, and classifies precisely when every later fiber is empty. General preimage-tree Galois theory (Jones--Manes) addresses different invariants and does not by itself state these residue-period statistics. A companion preprint cited in the source on iterates of \(z+k/z\) was not located for complete reading; it is a residual priority risk.

## Limitations

The theorem uses Proposition 4.1(a) of the 2026 source, not a new independent proof of that premise. For multipliers with an excluded prime, failures can occur after index \(3\), and the theorem does not give the full distribution of their total number. The lack of an accessible copy of the named companion preprint and older unavailable records limits the historical-priority assessment. Independent validation is not claimed.

## References

1. M. Matijasevick, S. Rodríguez, G. Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1 (first public posting 2026-09-30), Sections 2, 4, and 7; https://arxiv.org/html/2610.00765v1 .
2. R. Jones, M. Manes, *Galois theory of quadratic rational functions*, Comment. Math. Helv. 89 (2014), 173--213, DOI 10.4171/CMH/316; https://ems.press/journals/cmh/articles/12462 .
3. M. Matijasevick, *Arithmetic dynamics of \(z+k/z\): Galois groups, prime divisors of orbits, and zeros of iterates*, preprint (2026), cited by reference [2] of source [1]; complete original text not located.
