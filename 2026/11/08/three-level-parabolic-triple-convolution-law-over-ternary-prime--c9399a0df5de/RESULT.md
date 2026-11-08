# Three-level parabolic triple-convolution law over ternary prime-power rings

## Finding
For any integer \(k\ge1\), put \(N=3^k\) and \(R=\mathbb Z/N\mathbb Z\). Let the parabola be \(P_N=\{(u,u^2):u\in R\}\), and let \(r_N(s,t)\) count ordered triples \((u,v,w)\in R^3\) satisfying
\[
u+v+w=s,\qquad u^2+v^2+w^2=t.\]
**The complete convolution distribution** consists of exactly three levels:
\[
\begin{array}{c|ccc}
 r_N(s,t)&0&N&2N\\\hline
\#\{(s,t)\}&N(N-1)/6&N(2N+1)/3&N(N-1)/6
\end{array}.
\]
All three levels occur for every \(k\ge1\). More precisely, when \(s\) is a unit modulo \(3\), \(r_N(s,t)=N\) at every \(t\). When \(3\mid s\), take any \(h\in R\) with \(3h=s\), and put \(c=2t-6h^2\). The count equals \(N\) at \(c=0\), equals \(2N\) if \(c\ne0\) and \(c/3^{v_3(c)}\equiv1\pmod3\), and vanishes otherwise. Here \(v_3(c)\) is the unique integer in \(\{0,\ldots,k-1\}\) for which \(3^{v_3(c)}\mid c\) but \(3^{v_3(c)+1}\nmid c\), for nonzero \(c\). The criterion is independent of the chosen \(h\).

Consequently the triple sumset has exact size
\[|P_N+P_N+P_N|=\frac{N(5N+1)}6.\]
For the unweighted quadratic Fourier sum
\[G_N(a,b)=\sum_{u\in R}\exp\!\left(\frac{2\pi i(au+bu^2)}N\right),\]
the exact normalized two-parameter sixth moment is
\[\frac1{N^2}\sum_{a,b\in R}|G_N(a,b)|^6=\frac{N^3(4N-1)}3.\]

## Assumptions and scope
The ring is \(\mathbb Z/3^k\mathbb Z\), not the finite field \(\mathbb F_{3^k}\). All triples are ordered, the polynomial graph uses **all** ring elements, and all Fourier coefficients have weight one. No divisibility or invertibility assumptions on \(s\), \(t\), \(a\), or \(b\) are imposed. The exponential uses integer residue representatives and is independent of representatives.

## Proof
**Reduction to a ramified binary norm.** Fix \(s\). Write \(w=s-u-v\), \(x=u-v\), and \(y=u+v\). Because \(2\) is invertible in \(R\), the map \((u,v)\mapsto(x,y)\) is bijective, and
\[
 2(u^2+v^2+w^2)=x^2+3y^2-4sy+2s^2.
\]
If \(s\) is a unit, then for each \(x\), the map \(y\mapsto3y^2-4sy\) is bijective modulo \(3^k\): it reduces to the nonzero linear map \(y\mapsto-sy\) modulo three, and its derivative \(6y-4s\) is a unit at every residue. Successive unique Hensel lifting therefore produces exactly one \(y\) for every right-hand side, so \(r_N(s,t)=N\).

If \(3\mid s\), choose \(h\) with \(s=3h\). Completing the square yields
\[x^2+3(y-2h)^2=2t-6h^2=:c,\]
so \(r_N(s,t)=A_k(c)\), where
\[A_k(c)=\#\{(x,z)\in(\mathbb Z/3^k\mathbb Z)^2:x^2+3z^2=c\}.\]
Changing \(h\) by a multiple of \(3^{k-1}\) does not change \(6h^2\) modulo \(3^k\), so this is well defined.

**Exact norm-representation count.** We prove
\[
A_k(c)=\begin{cases}
3^k,&c=0,\\
2\cdot3^k,&c\ne0\text{ and }c/3^{v_3(c)}\equiv1\pmod3,\\
0,&\text{otherwise}.
\end{cases}
\]
For unit \(c\), reduction modulo three forces \(x^2\equiv c\pmod3\). If \(c\equiv2\pmod3\), there are no solutions. If \(c\equiv1\pmod3\), each of the \(3^k\) choices of \(z\) leaves a unit with two simple square roots for \(x\), giving \(2\cdot3^k\) solutions.

For \(k\ge2\) and \(v_3(c)=1\), necessarily \(3\mid x\). Put \(x=3x'\) and divide the equation by three modulo \(3^{k-1}\):
\[z^2+3(x')^2=c/3\pmod{3^{k-1}}.\]
For every \(x'\in\mathbb Z/3^{k-1}\mathbb Z\), the resulting unit on the right has two simple square roots for \(z\) exactly when \(c/3\equiv1\pmod3\), and none otherwise. Each root modulo \(3^{k-1}\) has three lifts for \(z\) modulo \(3^k\), so the result is again \(2\cdot3^k\) or zero.

If \(9\mid c\) and \(k\ge3\), reduction modulo three forces \(3\mid x\); reducing modulo nine then forces \(3\mid z\). Dividing both variables by three gives the exact recurrence
\[A_k(c)=9A_{k-2}(c/9).\]
The base cases at the zero residue are \(A_1(0)=3\) and \(A_2(0)=9\). The recurrence proves \(A_k(0)=3^k\) and, inductively, the asserted nonzero counts. It also establishes all boundary cases.

**Global multiplicities.** For each of the \(2N/3\) unit values of \(s\), every one of the \(N\) values of \(t\) produces \(r_N=N\). For each of the \(N/3\) nonunit values of \(s\), the map \(t\mapsto c=2t-6h^2\) is bijective. There is one zero \(c\); the number of nonzero \(c\) with initial nonzero ternary digit \(1\) is
\[\sum_{j=0}^{k-1}3^{k-j-1}=\frac{N-1}{2},\]
with an equal number beginning with digit \(2\). Thus the three global multiplicities above follow. The number of attained sums is the sum of the \(N\)- and \(2N\)-level multiplicities, \(N(5N+1)/6\).

**Sixth moment.** Expanding \(|G_N(a,b)|^6\) and averaging over \((a,b)\) uses the exact orthogonality identity \(N^{-1}\sum_{a\in R}\exp(2\pi iaj/N)={\bf1}_{j=0}\). The resulting count equals \(\sum_{s,t}r_N(s,t)^2\), hence
\[
\frac1{N^2}\sum_{a,b}|G_N(a,b)|^6
=N^2\!\left(\frac{N(2N+1)}3+4\frac{N(N-1)}6\right)
=\frac{N^3(4N-1)}3.
\]
This completes the proof.

## Verification
Run `python3 verify.py` using Python's standard library. It independently enumerates ordered triples for \(\(\(N=3,9\),27,81\)\), checks every target coefficient against the explicit norm formula, compares all multiplicities, computes the sumset size and integer sixth-moment energy, and evaluates the Fourier sixth-moment identity directly at \(\(N=3,9\)\) within a numerical tolerance. These are finite regression checks, not an infinite proof. The all-\(k\) result follows from the preceding lifting recurrence and character orthogonality.

## Relationship to prior work
Mockenhaupt and Tao (2002) introduced the finite-field restriction framework. Hickman and Wright (2018) developed restriction theory over composite-modulus rings, including the distinction between finite fields and residue rings. González-Riquelme and Oliveira e Silva (2024, Proposition 3.3) explicitly calculate a three-fold parabolic convolution over finite fields of characteristic greater than three; that theorem assumes the characteristic is greater than three and does not evaluate the present ramified three-power ring convolution. Lv and Zhang (2021) compute a sixth moment of Dirichlet-character-weighted Gauss sums with a different averaging operation over prime moduli; their result is not the present unweighted two-frequency moment.

The present classification is a specialized exact ternary-ring convolution statement. Standard quadratic norm and local-density calculations may contain stronger material from which its norm-count step follows; historical-priority claims therefore remain bounded pending more exhaustive comparison.

## Limitations
This work does not determine the sharp \(\ell^2\)-to-\(L^6\) extension constant for arbitrary complex coefficient functions. It does not treat primes other than three, other quadratic graphs, or mixed moduli. The finite computational checks are not proofs beyond their tested range. Independent validation and exhaustive priority verification have not been performed.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (first public 18 April 2002), https://arxiv.org/abs/math/0204234 .
2. J. Hickman and J. Wright, *The Fourier Restriction and Kakeya Problems over Rings of Integers Modulo N*, Discrete Analysis 2018:11, arXiv:1801.03176, https://arxiv.org/abs/1801.03176 .
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, especially Proposition 3.3, https://arxiv.org/abs/2405.16647 .
4. X. Lv and W. Zhang, *The generalized quadratic Gauss sums and its sixth power mean*, AIMS Mathematics 6 (2021), 11275–11285, https://doi.org/10.3934/math.2021654 .
