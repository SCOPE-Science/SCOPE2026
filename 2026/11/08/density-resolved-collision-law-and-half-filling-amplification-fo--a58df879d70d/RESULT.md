# Density-resolved collision law and half-filling amplification for cyclic Rule 184

## Finding

For the synchronous binary traffic cellular automaton Rule 184 on a labelled cyclic ring of length \(n\ge3\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be its global update and \(|x|\) the number of occupied sites. Define the ordered-pair collision counts
\[
C_{n,k}=\#\{(x,y):F_n(x)=F_n(y),\ |x|=|y|=k\},\qquad C_n(z)=\sum_{k=0}^n C_{n,k}z^k.
\]
Put
\[
D(u,z)=(1+zu^2)\bigl(1-(1+z)u-zu^2+z(z+1)u^3-2z^2u^4\bigr).
\]
For every integer \(n\ge3\), the **exact two-variable collision law** is
\[
\boxed{\sum_{n\ge1}C_n(z)u^n=-u\,\frac{\partial}{\partial u}\log D(u,z)}.
\]
Thus each coefficient gives the complete collision count at a prescribed conserved particle number, rather than merely the unconditional collision count. In particular, \(C_{n,k}=C_{n,n-k}\).

Let
\[
\lambda=\frac12+\sqrt{\frac54+\sqrt3}=2.226861548465561\ldots,
\qquad \sigma^2=\frac{\lambda^2-1}{4(2\lambda-1)(\lambda^2-\lambda-1)}=0.165450374154605\ldots.
\]
If \(X,Y\) are independent uniformly distributed binary words on the ring, then
\[
\boxed{\Pr(F_nX=F_nY)\sim(\lambda/4)^n}.
\]
If \(n\) is even and, instead, \(X,Y\) are independent and uniform among the \(\binom n{n/2}\) words containing exactly \(n/2\) particles, then
\[
\boxed{\Pr(F_nX=F_nY)\sim\sqrt{\frac{\pi n}{8\sigma^2}}\,(\lambda/4)^n}.
\]
The asymptotic constant in the unconditional formula is one; the half-filling condition creates a sharp, nonconstant \(\sqrt n\) amplification. The first formula also determines the order-two Rényi entropy rate of the single-update output distribution.

## Assumptions and scope

All words have labelled positions \(i\in\mathbb Z/n\mathbb Z\), no identification by rotation. Both updates and all collisions are synchronous, and ordered pairs \((x,y)\) are counted with multiplicity. For bits \(a,b,c\), the local Rule-184 map is
\[
f(a,b,c)=(1-b)a+bc,
\qquad (F_nx)_i=f(x_{i-1},x_i,x_{i+1}).
\]
The addition here is ordinary integer addition of mutually exclusive terms. The rule moves each occupied site one position right if that destination is empty, hence conserves \(|x|\). The variable \(u\) counts ring length and \(z\) counts particles in either input (equal automatically when their outputs coincide). The displayed asymptotics concern lengths tending to infinity; the central-density statement is only for even lengths.

## Proof

**Paired-symbol transfer.** Let \(A=\{00,01,10,11\}\), with \(v=(v_1,v_2)\) denoting a pair of input bits. Index a \(16\times16\) matrix \(T(z)\) by ordered pairs \((a,b)\in A^2\). Define its entries by
\[
T(z)_{(a,b),(b',c)}=\begin{cases}
z^{b_1},&b'=b\ \text{and}\ f(a_1,b_1,c_1)=f(a_2,b_2,c_2),\\
0,&\text{otherwise}.
\end{cases}
\]
A length-\(n\) closed walk chooses precisely one pair of cyclic input words, and the transition conditions require their output bits to agree at every site. Its weight is \(z^{|x|}\). Therefore \(C_n(z)=\operatorname{tr}(T(z)^n)\), including all sectors and all ring lengths.

**Exact determinant.** Direct integer-polynomial elimination of this explicitly specified sparse matrix gives
\[
\det(tI-T(z))=t^{10}(t^2+z)
\bigl(t^4-(1+z)t^3-zt^2+z(z+1)t-2z^2\bigr).
\]
Equivalently, \(\det(I-uT(z))=D(u,z)\). For every finite matrix, \(-u\partial_u\log\det(I-uT)=\sum_{n\ge1}\operatorname{tr}(T^n)u^n\) as a formal power series. This proves the exact bivariate identity. All determinant arithmetic and low-length coefficients can be independently reproduced from the standalone programs below, without relying on a numerical eigenvalue estimate.

The complement-reflection involution \((Rx)_i=1-x_{-i}\) satisfies \(F_nR=RF_n\). It maps a colliding pair at particle number \(k\) bijectively to one at \(n-k\); hence \(C_{n,k}=C_{n,n-k}\).

**Unconditional exponential law.** At \(z=1\) the quartic becomes \((t^2-t-1)^2-3\). Its four roots are \(\frac12\pm\sqrt{\frac54+\sqrt3}\) and \(\frac12\pm i\sqrt{\sqrt3-\frac54}\). The remaining nonzero roots of the full characteristic polynomial are \(i\) and \(-i\). The displayed \(\lambda\) is simple and has strictly larger modulus than every other root. Since a trace of an integer matrix power is the sum of its eigenvalue powers with algebraic multiplicities, \(C_n(1)\sim\lambda^n\), with leading coefficient exactly one. Division by \(4^n\), the number of ordered input pairs, proves the first probability law.

**Density-constrained local limit.** For \(z>0\), the matrix \(T(z)\) has a unique dominant strongly connected component, on state indices \(\{0,1,2,3,5,6,7,9,10,11,12,15\}\) when pairs of bit-pairs are indexed by \(4a+b\), with \(a,b\in\{0,1,2,3\}\). Its unweighted adjacency matrix has a strictly positive sixth power; all other components contribute only lower-modulus eigenvalues. This component contains a loop of weight \(1\) (index \(0\)) and a loop of weight \(z\) (index \(15\)). The Perron eigenvalue \(\lambda(z)\) is therefore positive, simple, analytic near \(z=1\), and for every real \(\theta\not\equiv0\pmod{2\pi}\) the weighted matrix \(T(e^{i\theta})\) has spectral radius strictly less than \(\lambda(1)\): equality in the Perron triangle inequality would force both loop phases to equal the same phase, forcing \(e^{i\theta}=1\).

Writing \(z=e^s\), complement-reflection implies \(\lambda(e^s)=e^s\lambda(e^{-s})\), so \(\partial_s\log\lambda(e^s)|_{s=0}=1/2\). Twice implicitly differentiating the quartic eigenvalue equation gives
\[
\left.\partial_s^2\log\lambda(e^s)\right|_{s=0}
=\frac{\lambda^2-1}{4(2\lambda-1)(\lambda^2-\lambda-1)}=\sigma^2>0.
\]
Fourier coefficient extraction in \(z\), the spectral gap away from angle zero, and the resulting Gaussian saddle at angle zero yield
\[
C_{n,n/2}\sim\frac{\lambda^n}{\sqrt{2\pi n\sigma^2}}\quad(n\to\infty\ \text{through even integers}).
\]
There is no additional periodicity multiplier because the two loops carry distinct weights. Dividing by \(\binom n{n/2}^2\sim4^n\,2/(\pi n)\) proves the central-density formula.

## Verification

The included `verify_transfer.py` constructs the exact 16-state matrix from the Wolfram-code truth table, checks its characteristic polynomial over \(\mathbb Z[z,t]\), and directly computes initial traces. `verify_direct.py` independently implements parallel particle moves and exhaustively groups every output fiber at each particle count for all ring lengths \(3\le n\le16\), checking every coefficient of the formula. `verify_density.py` uses the independent Newton recurrence and compares the central coefficient with the saddle-point expression for even lengths \(20,40,80,120,160,200\). The captured outputs `verify_transfer.out`, `verify_direct.out`, and `verify_density.out` record completed runs. The finite checks support, but do not replace, the exact transfer proof and spectral local-limit argument.

Run the standalone checks with Python 3 (`sympy` is required for `verify_transfer.py`): `python3 verify_transfer.py`, `python3 verify_direct.py`, `python3 verify_density.py`.

## Relationship to prior work

Rule 184 is the classical synchronous deterministic traffic rule. Fukś (1997) proves density-classification results using Rule 184 and counts preimages of finite all-zero blocks; Fukś (1999) develops arbitrary-time traffic flow and zero-block preimage enumeration. Those results and the general de Bruijn transfer technique are existing tools, not claimed as new here. The new mathematical statement is the all-length, *particle-number-resolved second moment of the complete cyclic output-fiber distribution*, its factorized bivariate rational generating function, and the sharp conditional/unconditional collision asymptotics. Neither arbitrary-time current nor a fixed-block preimage count is identical to that global second moment.

Rodríguez Zamora and Chapa (2004) explicitly study Rule 184 using de Bruijn diagrams. Its available description was compared; the complete chapter was not accessible, so whether it contains a specialized equivalent of the present collision law is an unresolved priority risk. Wolfram's Rule-184 finite-size atlas illustrates finite state-transition and cycle data, not an all-length density-resolved collision theorem in the accessible material. An earlier mass-resolved entrance-time census for cyclic Rule 184 classifies when configurations reach free flow, not the sizes or pairwise second moments of one-step output fibers. Earlier separate exact collision calculations for Rule 4 concern a different local update and do not imply this polynomial, its density sectors or its half-filling amplification.

## Limitations

This theorem concerns one synchronous update on a finite labelled cyclic ring, not long-time traffic-flow relaxation, other traffic rules, intervals with absorbing boundaries, or higher Rényi orders. The computational scripts use exhaustive checks only at stated finite lengths. Historical originality is qualified by unavailable full text of a directly relevant 2004 conference chapter and possible unindexed equivalents; no independence or external certification is claimed.

## References

1. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, arXiv:comp-gas/9703001v1 (first public 7 March 1997), https://arxiv.org/pdf/comp-gas/9703001 .
2. H. Fukś, *Exact results for deterministic cellular automata traffic models*, arXiv:comp-gas/9902001v1 (first public 4 February 1999); Phys. Rev. E 60, 197–202 (1999), https://arxiv.org/pdf/comp-gas/9902001 .
3. R. Rodríguez Zamora and S. Chapa, *Using de Bruijn Diagrams to Analyze 1d Cellular Automata Traffic Models*, ACRI 2004, pp. 306–315, https://doi.org/10.1007/978-3-540-30479-1_32 .
4. Wolfram Atlas, *Rule 184 — Finite size properties*, https://atlas.wolfram.com/01/01/184/01_01_32_184.html .
