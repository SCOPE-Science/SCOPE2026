# Three minimal 3-adic components for \(x\mapsto x^2+1\)

## Finding
Let \(f:\mathbb Z_3\to\mathbb Z_3\) be \(f(x)=x^2+1\), where \(\mathbb Z_3\) is the ring of 3-adic integers. Every forward orbit enters \(B=2+3\mathbb Z_3\) in at most two iterates. The invariant clopen set \(B\) is the disjoint union of exactly three invariant minimal components
\[
\begin{aligned}
C_0&=(2+27\mathbb Z_3)\cup(5+27\mathbb Z_3)\cup(26+27\mathbb Z_3),\\
C_1&=(8+27\mathbb Z_3)\cup(11+27\mathbb Z_3)\cup(14+27\mathbb Z_3),\\
C_2&=(17+27\mathbb Z_3)\cup(20+27\mathbb Z_3)\cup(23+27\mathbb Z_3).
\end{aligned}
\]
On each \(C_j\), the map is conjugate to the 3-adic adding machine. The induced cycle length on the component at modulus \(3^n\) is \(3\) for \(n=2,3\), and \(3^{n-2}\) for every \(n\ge4\). In particular, \(f\) has no periodic point in \(\mathbb Z_3\); all points belong to the basin of one of these three components.

## Assumptions and scope
The domain is exactly \(\mathbb Z_3\), and the map is the integral polynomial \(f(x)=x^2+1\). Congruences are interpreted in \(\mathbb Z/3^n\mathbb Z\). A minimal component means a nonempty compact invariant set on which every forward orbit is dense. No statement is made for other primes, other constant terms, or the full algebraic closure of \(\mathbb Q_3\).

## Proof
First, modulo 3 the map has the residue transitions \(0\mapsto1\mapsto2\mapsto2\). Hence every orbit reaches \(B=2+3\mathbb Z_3\) in at most two steps, and \(B\) is invariant. For \(x,y\in B\),
\[
f(x)-f(y)=(x-y)(x+y),\qquad x+y\equiv1\pmod3,
\]
so \(f\) is an isometry on \(B\).

Put \(g=f^3\). Direct polynomial multiplication gives
\[
g(x)-x=(x^2-x+1)P(x),
\]
where
\[
P(x)=x^6+x^5+4x^4+3x^3+7x^2+4x+5.
\]
Writing \(x=2+3a\), one obtains
\[
x^2-x+1=3(1+3a+3a^2)
\]
and
\[
P(2+3a)=9(81a^6+351a^5+666a^4+705a^3+441a^2+156a+25).
\]
The factor in parentheses in the first expression is a 3-adic unit, and the last parenthesis is congruent to 1 modulo 3. Therefore
\[
\nu_3(g(x)-x)=3\quad\text{for every }x\in B.
\]
Also \(g'(x)=(2x)(2f(x))(2f^2(x))\equiv1\pmod3\) on \(B\).

We use the following lifting lemma. If \(G\in\mathbb Z_3[x]\), \(s\ge2\), and on a ball \(a+3^s\mathbb Z_3\) one has \(\nu_3(G(x)-x)=s\) for every \(x\) and \(G'(x)\equiv1\pmod3\), then \(G\) has one cycle of length \(3^{n-s}\) on that ball modulo \(3^n\), for every \(n\ge s\). At the first lift, the unit displacement gives a 3-cycle among the three residue classes modulo \(3^{s+1}\). For the induction, if a return iterate \(H\) has displacement \(\delta=H(x)-x\) with \(\nu_3(\delta)=n\) and \(H'(x)\equiv1\pmod3\), Taylor expansion and \(n\ge2\) give
\[
H^3(x)-x\equiv3\bigl(H(x)-x\bigr)\pmod{3^{n+2}}.
\]
Thus each lift increases the cycle length by a factor of 3. The derivative condition persists under iteration, so induction proves the lemma.

Apply the lemma to \(g=f^3\) on each ball \(r+27\mathbb Z_3\) with \(r\in B\pmod{27}\). Modulo 27, the three cycles of \(f\) in \(B\) are exactly
\[
(2,5,26),\qquad(8,11,14),\qquad(17,20,23).
\]
Each cycle defines one invariant component \(C_j\) above. On each of its three constituent balls, \(g\) has a single cycle of length \(3^{n-3}\) modulo \(3^n\), for \(n\ge3\). Since \(f\) cyclically permutes the three balls, \(f\) has one cycle of length \(3^{n-2}\) on \(C_j\) modulo \(3^n\). The projection of each component modulo 9 is the same 3-cycle, so its period there is also 3. These single-cycle quotients at every level imply that every orbit is dense in \(C_j\), proving minimality and the adding-machine description.

The three components are disjoint and cover \(B\). Since every orbit enters \(B\) within two steps, every point eventually enters exactly one \(C_j\). A periodic point would have to lie in one of the minimal infinite components, which is impossible. This proves the full stated decomposition.

## Verification
The algebraic factorization and valuation calculation above are symbolic and hold for every \(x\in B\); the lifting lemma supplies the all-level argument. The included script checks the polynomial identity on sample integers and enumerates the induced map modulo \(3^n\) for \(2\le n\le8\), reproducing the predicted cycle counts. Those finite checks are sanity checks only, not the proof for all levels.

## Relationship to prior work
Fan and Liao prove an abstract minimal-decomposition theorem for polynomial maps on \(\mathbb Z_p\) and list the possible periodic periods when \(p=3\), but their detailed quadratic classification is for \(p=2\). Their general theorem does not identify the three components, the absence of periodic points, or the exact cycle-growth law for \(x^2+1\) on \(\mathbb Z_3\). Work on the square map \(x\mapsto x^2\) is related context but concerns a different polynomial. The claim here is the explicit decomposition and lifting rate for this particular 3-adic map.

## Limitations
This is a complete classification only for \(x^2+1\) on \(\mathbb Z_3\). It does not classify all quadratic maps on \(\mathbb Z_3\), prove a parameter-family theorem, or assert novelty for broader p-adic polynomial dynamics. The comparison is limited to the inspected literature and targeted searches; an unlocated paper specifically treating this exact map remains a residual possibility.

## References
1. A.-H. Fan and L. Liao, “On minimal decomposition of p-adic polynomial dynamical systems,” arXiv:1010.5583, first public version 27 October 2010; later published in *Advances in Mathematics* 228 (2011), 2116–2144. DOI: 10.1016/j.aim.2011.06.032. https://arxiv.org/abs/1010.5583
2. S. Fan and L. Liao, “Dynamics of the square mapping on the ring of p-adic integers,” arXiv:1408.4574, first public version 20 August 2014; *Proceedings of the American Mathematical Society* 144 (2016), 1183–1196. DOI: 10.1090/proc12777. https://arxiv.org/abs/1408.4574
