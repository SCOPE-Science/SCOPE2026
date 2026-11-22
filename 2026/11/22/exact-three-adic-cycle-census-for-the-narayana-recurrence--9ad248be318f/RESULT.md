# Exact three-adic cycle census for the Narayana recurrence

## Finding
For every integer \(k\ge1\), set \(q=3^k\) and define the recurrence-state permutation
\[
T_k:(\mathbb Z/q\mathbb Z)^3\longrightarrow(\mathbb Z/q\mathbb Z)^3,
\qquad T_k(a,b,c)=(a+c,a,b).
\]
It is the state map for the Narayana recurrence \(u_{n+3}=u_{n+2}+u_n\), with each state written in reverse chronological order. Write \(C_k(d)\) for the number of distinct cycles of **least** positive length \(d\). Then
\[
\boxed{C_k(1)=1,\qquad C_k(2\cdot3^r)=1,\qquad
C_k(8\cdot3^r)=\frac{13\cdot9^r-1}{4}\quad(0\le r<k),}
\]
with \(C_k(d)=0\) for all remaining positive integers \(d\). Thus the unique fixed point is zero, every other state is periodic without a transient segment, and
\[
\boxed{\sum_{d\ge1} C_k(d)=1+\frac{3k}{4}+\frac{13(9^k-1)}{32}.}
\]
The least common multiple of all cycle lengths, and the longest cycle length itself, is \(8\cdot3^{k-1}\).

## Assumptions and scope
The theorem concerns **all** \(q^3\) seed triples, not just the conventional Narayana cow initial values. All state components and calculations are modulo \(q\). The formulas apply for every positive \(k\) with no restriction on seeds. The characteristic polynomial and the primary research context belong to integer linear recurrences (MSC 11B37).

## Proof
**1. Integral matrix and local decomposition.** The state matrix is
\[
M=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad \det M=1,
\qquad f(X)=\det(XI-M)=X^3-X^2-1.
\]
The vectors \(e_3,Me_3,M^2e_3\) are an integral basis (their determinant is a unit). Consequently multiplication by \(X\) on the rank-three algebra \(R=\mathbb Z_3[X]/(f)\) realizes the operator \(M\). Modulo three,
\[
f(X)\equiv(X+1)(X^2+X-1)\pmod3.
\]
The two factors are coprime and the quadratic is irreducible over \(\mathbb F_3\): its discriminant is \(2\). By the Hensel factorization and the Chinese remainder theorem,
\[
R\simeq \mathbb Z_3\oplus\mathcal O,
\]
where \(\mathcal O\) is a free unramified rank-two \(\mathbb Z_3\)-algebra. The operator \(M\) acts on these summands as multiplication by units \(\lambda\) and \(\alpha\), with \(\lambda\equiv-1\pmod3\) and \(\alpha^2+\alpha-1\equiv0\pmod3\). In \(\mathbb F_9\), the latter relation yields \(\alpha^4=-1\), so \(\alpha\) has exact multiplicative order eight modulo three.

**2. Exact lifting exponents.** Since \(f(-1)=-3\) and \(f'(-1)=5\) is a three-adic unit, the simple root \(\lambda\) satisfies \(v_3(\lambda+1)=1\). As \(\lambda-1\) is a unit, \(v_3(\lambda^2-1)=1\). Direct integral multiplication gives
\[
M^8-I=3B,\qquad
B=\begin{pmatrix}4&2&3\\3&1&2\\2&1&1\end{pmatrix},
\qquad\det B=1.
\]
Thus both summands of \(M^8-I\) have exactly one factor of three: in particular \(\alpha^8-1\in3\mathcal O\setminus9\mathcal O\). The elementary odd-prime lifting identity, valid for each unit \(z\) in either unramified summand whenever \(z\equiv1\pmod3\) but \(z\not\equiv1\pmod9\), is
\[
v_3(z^{3^r}-1)=r+1\qquad(r\ge0).
\]
It follows by expanding \((1+3^s w)^3\) and induction, as its first nonconstant term has exact valuation \(s+1\) and the others strictly greater. Therefore, for each \(r\ge0\),
\[
v_3(\lambda^{2\cdot3^r}-1)=r+1,
\qquad v_3(\alpha^{8\cdot3^r}-1)=r+1.
\]
On the quadratic summand \(\alpha^{2\cdot3^r}-1\) and \(\alpha^{4\cdot3^r}-1\) are units, since \(\alpha\) has order eight modulo three. On the scalar summand the exponents \(2\cdot3^r\) and \(4\cdot3^r\) have the same valuation \(r+1\). For odd exponents, neither summand has a fixed nonzero reduction modulo three.

**3. Fixed points and primitive cycles.** Denote the number of points fixed by \(T_k^d\) by \(F_k(d)\). A scalar endomorphism of valuation \(s\) on a free rank-\(j\) module modulo \(3^k\) has exactly \(3^{j\min(k,s)}\) kernel points. The direct-sum description gives, for every \(r\ge0\),
\[
F_k(1)=1,\quad
F_k(2\cdot3^r)=F_k(4\cdot3^r)=3^{\min(k,r+1)},\quad
F_k(8\cdot3^r)=3^{3\min(k,r+1)}.
\]
In addition \(F_k(3^r)=1\). Because \(M^8-I=3B\) with \(B\) invertible, the binomial lifting identity yields \(M^{8\cdot3^{k-1}}\equiv I\pmod{3^k}\), so **every** cycle length divides \(8\cdot3^{k-1}\). Its positive divisors have form \(3^r\), \(2\cdot3^r\), \(4\cdot3^r\) or \(8\cdot3^r\). The equal fixed-point counts for the \(2\)- and \(4\)-families eliminate all genuine \(4\)-family cycles. The odd family contributes only the fixed zero state. For \(0\le r<k\), subtracting lower fixed-point populations produces
\[
\begin{aligned}
&\#\{x:\operatorname{per}(x)=2\cdot3^r\}=2\cdot3^r,\\
&\#\{x:\operatorname{per}(x)=8\cdot3^r\}=26\cdot3^{3r}-2\cdot3^r.
\end{aligned}
\]
For \(r=0\), these read \(3-1=2\) and \(27-3=24\). Dividing each population by its least period yields exactly one \(2\cdot3^r\)-cycle and \((13\cdot9^r-1)/4\) many \(8\cdot3^r\)-cycles. Summing the geometric series proves the total-cycle formula. All assertions follow.

## Verification
The independent pure-Python program `check.py` enumerates every one of the \(3^{3k}\) states for \(k=1,2,3,4\), follows each full cycle once, and compares all least-period multiplicities to the formula. It also checks the integer matrix identity and its determinant. The enumerated cycle totals are \(5,35,299,2669\), with all \(27+729+19683+531441=551880\) state instances covered across these four moduli. Finite enumeration checks examples; the preceding algebraic proof establishes every positive \(k\).

## Relationship to prior work
Xin Lin (2021) studies negative-index identities and convolutions of the Narayana sequence, which fix the recurrence and number-theoretic setting but do not classify arbitrary modular seed states. Guadalupe's 2021 work gives exact three-adic valuations for the **standard initial sequence**, not the cycle spectrum of the complete three-dimensional state space. The earlier study of Narayana sequences in cryptography discusses modular periods of special sequences; its full text was not available for a decisive all-state comparison. The present result classifies primitive cycles for every seed and every power of three, not merely a single orbit's least period or output residues.

## Limitations
The formula applies to the specified recurrence and prime three, not to other companion matrices or other primes without further analysis. Algebraic order and kernel counting are used here but do not automatically confer novelty over an equivalent previously published all-seed orbit decomposition. The accessible earlier cryptography paper was inspected only at abstract level; priority uncertainty remains. All finite checks are supporting tests, not substitutes for the general proof.

## References
- Xin Lin, *On the Recurrence Properties of Narayana’s Cows Sequence*, Symmetry **13** (2021), 149, https://doi.org/10.3390/sym13010149 (public 17 January 2021; MSC 11B37, 11B83).
- Russelle Guadalupe, *On the 3-adic valuation of the Narayana numbers*, arXiv:2112.06187 (first version 12 December 2021), https://arxiv.org/abs/2112.06187.
- *Narayana Sequences for Cryptographic Applications*, arXiv:1509.05745 (2015), https://arxiv.org/abs/1509.05745 (abstract compared; full text not inspected).
