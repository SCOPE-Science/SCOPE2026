# Exact five-adic image and fiber distribution of consecutive fifth-power differences

## Finding
For \(x\in\mathbb Z\), put \(F(x)=(x+1)^5-x^5\), and let \(\mathbb Z_5^2=\{z^2:z\in\mathbb Z_5\}\). The complete image in the five-adic integers is
\[
\boxed{F(\mathbb Z_5)=\left\{\frac{5u-4}{16}:u\in(4+5\mathbb Z_5)\ \sqcup\ (1+50\mathbb Z_5^2)\ \sqcup\ 25\mathbb Z_5^2\right\}.}
\]
The three components are disjoint. Consequently, the image has additive Haar measure exactly \(7/150\).

Let \(R_k\) denote the number of values of \(F\) modulo \(5^k\), and \(Q(j)\) the number of square residues modulo \(5^j\), with \(Q(j)=1\) for \(j\le0\). For every \(k\ge1\),
\[
\boxed{R_1=1,\qquad R_k=5^{k-2}+2Q(k-3)\quad(k\ge2).}
\]
Here, for \(j\ge1\),
\[
Q(j)=1+2\sum_{h=0}^{\lfloor(j-1)/2\rfloor}5^{j-2h-1}.
\]
In particular, \(R_1,\ldots,R_8=1,3,7,31,147,731,3647,18231\).

This classification also gives *every individual fiber*. For \(k\ge3\), write \(j=k-3\), and for a residue \(y\bmod5^k\) with \(y\equiv1\pmod5\), set
\[
u(y)=\frac{16y+4}{5}\bmod5^{k-1}.
\]
The division is well-defined modulo \(5^{k-1}\). Let \(r_j(a)=\#\{z\bmod5^j:z^2\equiv a\pmod{5^j}\}\), with \(r_0(0)=1\). Then
\[
\#F^{-1}(y)=
\begin{cases}
10,&u(y)\equiv4\pmod5,\\
25\,r_j\bigl((u(y)-1)/50\bmod5^j\bigr),&u(y)\equiv1\pmod{25},\\
50\,r_j\bigl(u(y)/25\bmod5^j\bigr),&u(y)\equiv0\pmod{25},\\
0,&\text{otherwise.}
\end{cases}
\]
The first congruence means the entire residue ball \(4+5\mathbb Z_5\); the second and third are in separate balls. The expression \((u(y)-1)/50\) means \(((u(y)-1)/25)\cdot2^{-1}\bmod5^j\), since \(2\) is a unit. For \(k=1\), the sole image residue is \(1\) with five preimages; for \(k=2\), the three components have respectively \(10,5,10\) preimages. A nonzero square \(a\bmod5^j\) of valuation \(2h<j\) has \(r_j(a)=2\cdot5^h\); zero has \(r_j(0)=5^{\lfloor j/2\rfloor}\). All other values have zero roots.

## Assumptions and scope
All images and fibers are taken over the complete residue ring \(\mathbb Z/5^k\mathbb Z\), with inputs counted modulo \(5^k\), and over \(\mathbb Z_5\) for the limiting image. No assertion is made about other primes, other exponents, or independent variables. The affine quotient by \(16\) is defined in \(\mathbb Z_5\), since \(16\) is a unit.

## Proof
**1. Nested-square identity.** The substitution \(t=2x+1\), which is an automorphism of \(\mathbb Z_5\), gives the exact polynomial identity
\[
16F(x)+4=5(t^2+1)^2.
\]
Thus classification of \(F\) is equivalent to the image of \(U(t)=(t^2+1)^2\).

**2. Regular balls.** On \(t\equiv\pm1\pmod5\), one has \(U(t)\equiv4\pmod5\) and \(U'(t)=4t(t^2+1)\) is a five-adic unit. Hensel lifting therefore maps each of these two input balls bijectively onto \(4+5\mathbb Z_5\). This is the full regular component.

**3. The central critical ball.** On \(t\in5\mathbb Z_5\), write \(t=5v\). Then
\[
U(5v)=1+25v^2(2+25v^2).
\]
The factor \(1+(25/2)v^2\) has a unique square root \(S(v)\equiv1\pmod5\), uniformly for \(v\in\mathbb Z_5\). The map \(v\mapsto vS(v)\) is a bijective five-adic isometry: its difference quotient is a unit congruent to \(1\pmod5\), and its reduction is the identity, so digit-by-digit Hensel lifting yields one solution to every target. Consequently the central branch has image exactly \(1+50\mathbb Z_5^2\).

**4. The two outer critical balls.** On \(t\equiv\pm2\pmod5\), one has \(t^2+1\equiv0\pmod5\), and its derivative \(2t\) is a unit. Therefore the map \(t\mapsto(t^2+1)/5\) is a bijection from each of these two residue balls to \(\mathbb Z_5\). Squaring gives their common image \(25\mathbb Z_5^2\). The three output components found in Steps 2–4 have distinct reductions \(4,1,0\pmod5\), so they form a disjoint union and exhaust all inputs.

**5. Counting finite images.** For \(k\ge2\), reduction of the affine map \(u\mapsto(5u-4)/16\) modulo \(5^k\) is a bijection between residues \(u\bmod5^{k-1}\) and residues \(y\equiv1\pmod5\). The regular component contributes \(5^{k-2}\) classes; each singular component contributes exactly \(Q(k-3)\) classes (one class if its square modulus is trivial). The formula for \(Q(j)\) follows by separating nonzero squares according to even valuation \(2h<j\), with \(2\cdot5^{j-2h-1}\) such residues, plus zero. The stated image counts follow.

**6. Exact fibers.** For the regular image, each of the two nonsingular input balls supplies one solution modulo \(5^{k-1}\); because \(F\) depends on \(U\bmod5^{k-1}\), each solution has exactly five lifts modulo \(5^k\). This gives ten preimages. In the central ball, the change of variable from Step 3 identifies the map with \(1+50z^2\), where \(t=5v\); for \(k\ge3\), a root of the reduced square congruence modulo \(5^{k-3}\) has five lifts at the intermediate input precision and five further lifts in \(x\bmod5^k\), giving \(25r_j\). Each of the two outer balls gives five intermediate lifts per square root and five final lifts, for \(50r_j\) in total. The direct low-level cases \(k=1,2\) give the stated exceptional fibers. Standard Hensel lifting for unit squares gives \(2\cdot5^h\) roots at nonzero valuation \(2h\); the zero equation has exactly \(5^{\lfloor j/2\rfloor}\) roots.

**7. Limiting density.** The square set in \(\mathbb Z_5\) has Haar measure
\[
\mu(\mathbb Z_5^2)=\sum_{h\ge0}\frac{4}{2\cdot5}\,5^{-2h}=\frac5{12}.
\]
The three \(U\)-components have respective measures \(1/5\), \(1/60\), and \(1/60\). The outer affine map scales these measures by \(1/5\), giving \(\mu(F(\mathbb Z_5))=(1/5+1/60+1/60)/5=7/150\). Equivalently, this is the limit of \(R_k/5^k\).

## Verification
The standalone Python 3 script `verify_fifth.py` exhaustively evaluates \(F\) on all inputs modulo \(5^k\) for each \(1\le k\le8\), and independently constructs all predicted individual fibers using square-root multiplicities. It verifies equality of the *full fiber maps*, not only their image sizes, in 488,280 integer-input cases. It also checks the count formula at each level and the total fiber mass. These computations support but are not substituted for the all-level proof.

## Relationship to prior work
Arias, Borja, and Anaya (2023, Article 23.8.1, Theorem 25) determine modular image counts for \(x^5+y^5\) with **independent** variables, including the prime five. Their theorem does not impose \(y=x+1\), does not characterize this one-variable difference image, and does not give its fiber law. More generally, the 2019 Arias–Borja–Rubio polynomial-image study treats sums in separate variables and squares, not this fixed adjacent fifth-power difference.

After the affine change \(t=2x+1\), the quartic in Step 1 is an affine transform of a fourth Dickson polynomial: \(D_4(t,-1/2)=t^4+2t^2+1/2\). Thus the 1991 paper of Bremser and Gomez-Calderon, on Dickson value sets over Galois rings, is an important historical comparison. Its accessible abstract describes bounds and selected preimage counts, but the full text was inaccessible during this review; no whole-paper noncoverage assertion is made. Related indexed five-adic, Frobenius-minus-linear, and pentatope value-set findings concern different polynomials and neither their displayed claims nor the inspected full mathematical results imply the present three-branch formula. The established tools of Hensel lifting and five-adic square classification are not claimed as new.

## Limitations
The result is confined to consecutive fifth-power *differences* and modulus powers of five, not to all exponents or primes. The prime-field level is degenerate, so finite computations alone cannot establish its higher-depth singular structure. The 1991 Dickson paper is a priority risk until its complete content is examined; an unindexed equivalent statement is also possible. No independent mathematical audit has been performed.

## References
1. F. Arias, J. Borja, and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences 26 (2023), Article 23.8.1, published 2023-08-28, https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf.
2. F. Arias, J. Borja, and L. Rubio, *Counting Integers Representable as Images of Polynomials Modulo n*, Journal of Integer Sequences 22 (2019), Article 19.6.7, published 2019-09-23, https://cs.uwaterloo.ca/journals/JIS/VOL22/Borja/borja3.html.
3. P. S. Bremser and J. Gomez-Calderon, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory 38 (1991), 240–250, DOI:10.1016/0022-314X(91)90087-R (abstract inspected, full text unavailable).
