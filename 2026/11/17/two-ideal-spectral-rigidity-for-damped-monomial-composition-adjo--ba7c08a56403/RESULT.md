# Two-ideal spectral rigidity for damped monomial composition–adjoint products

## Finding
Let \(m,n\ge2\) be distinct integers, write \(d=\gcd(m,n)\), \(M=m/d\), \(N=n/d\), and fix \(0<q<1\). Put \(r=q^{1/(M+N)}\). On the standard complex Hardy space \(H^2(\mathbb D)\), consider
\[
T=C_{rz^m}^{*}C_{rz^n},\qquad D=T^*T-TT^*.
\]
Here \(C_\varphi f=f\circ\varphi\), and \(D\) measures failure of normality of the compact mixed product. The following statements hold simultaneously.

**Exact signed spectrum.** Relative to the orthonormal monomials \(e_k(z)=z^k\), \(D\) is diagonal, with \(D e_0=0\), and for positive integers \(k\), its diagonal value is
\[
\lambda_k=\begin{cases}
q^{2j},& k=Mj,\ N\nmid j,\\
-q^{2j},& k=Nj,\ M\nmid j,\\
q^{2N\ell}-q^{2M\ell},&k=MN\ell,\\
0,&\text{otherwise}.
\end{cases}
\]
These mutually exclusive clauses specify the full spectral multiset with multiplicity. Thus \(D\) is self-adjoint and trace class, has trace zero, and belongs to every Schatten ideal \(\mathcal S_p\) for \(p>0\).

**Exact two-ideal invariants and inverse classification.** Put \(L=\max(M,N)\) and \(S=M+N\). Then
\[
\boxed{\|D\|_{\mathcal S_1}=2\left(\frac{q^2}{1-q^2}-\frac{q^{2L}}{1-q^{2L}}\right),\qquad
\|D\|_{\mathcal S_2}^2=2\left(\frac{q^4}{1-q^4}-\frac{q^{2S}}{1-q^{2S}}\right).}
\]
For a **fixed known** \(q\), the ordered pair of these two numerical invariants uniquely determines the unordered reduced exponent pair \(\{M,N\}\) among all distinct coprime positive integer pairs. The invariants do not determine the common divisor \(d\) or the order of \(m,n\); indeed \(D\) changes sign when they are interchanged.

**Critical all-Schatten boundary law.** For every real \(p>0\), let \(a=\min(M,N)\), \(b=\max(M,N)\). Then
\[
\boxed{\lim_{q\uparrow1}(-\log q)\,\|D\|_{\mathcal S_p}^{p}
=\frac{2-M^{-1}-N^{-1}}{2p}
+\frac{B\!\left(\frac{pa}{b-a},p+1\right)}{2(b-a)}.}
\]
Here \(B(x,y)=\int_0^1u^{x-1}(1-u)^{y-1}\,du\) is Euler's beta function. In particular, the constants at \(p=1\) and \(p=2\) are respectively \(1-1/L\) and \(\frac12-1/S\). The full formula is an actual limit for every fixed distinct pair and exponent, not just two-sided order bounds.

## Assumptions and scope
The field is complex. The Hardy inner product is normalized so that \(\{z^k:k\ge0\}\) is orthonormal. Composition symbols are the strict disk maps \(z\mapsto rz^m\) and \(z\mapsto rz^n\); \(m,n\) are arbitrary distinct integers at least two, and \(q\) is a fixed damping parameter in the exact formulas. The result depends only on reduced degrees \(M,N\) because the product's monomial action does. For \(0<p<1\), \(\|D\|_{\mathcal S_p}\) denotes the usual Schatten quasi-norm; no triangle inequality is needed. The limit holds with \(m,n,p\) fixed and \(q\uparrow1\), not in a simultaneous changing-degree regime.

## Proof
**1. Monomial action and normalization.** For any positive integer \(u\), \(C_{rz^u}e_j=r^j e_{uj}\). Its adjoint annihilates \(e_k\) unless \(u\mid k\), and otherwise sends \(e_{uj}\) to \(r^j e_j\). Since \(m=dM\), \(n=dN\) and \(\gcd(M,N)=1\), the condition \(m\mid nk\) is equivalent to \(M\mid k\). Thus, for \(j\ge1\),
\[
T e_{Mj}=r^{Mj+Nj}e_{Nj}=q^j e_{Nj},\qquad
T e_k=0\quad(M\nmid k,\ k\ge1),\qquad T e_0=e_0.
\]
The arrows from source indices \(Mj\) to target indices \(Nj\) have unique sources and targets; the weights \(q^j\) decay geometrically. The nonconstant part of \(T\) is therefore a compact weighted partial permutation. Its square modulus is diagonal: \(T^*T e_{Mj}=q^{2j}e_{Mj}\), and \(TT^*e_{Nj}=q^{2j}e_{Nj}\). Both act as the identity on constants.

**2. Complete signed diagonal and trace.** Subtraction yields precisely the four mutually exclusive cases in the finding. An index belongs to both positive-degree supports exactly when it equals \(MN\ell\) for an integer \(\ell\ge1\); the input and output weights at that index are respectively \(q^{2N\ell}\) and \(q^{2M\ell}\). Summability is immediate from geometric decay, including for \(0<p<1\). Since the two Gram operators have equal trace \(1+\sum_{j\ge1}q^{2j}\), their trace difference vanishes. No argument from finite sections is needed to establish this trace identity.

**3. Trace norm.** Suppose without loss of generality \(M<N\). Every positive eigenvalue arises on indices \(Mj\) with \(N\nmid j\); at a shared index \(MN\ell\), \(q^{2N\ell}-q^{2M\ell}<0\). Accordingly, the total positive spectral mass is
\[
\sum_{j\ge1,\,N\nmid j}q^{2j}
=\frac{q^2}{1-q^2}-\frac{q^{2N}}{1-q^{2N}}.
\]
Because the trace is zero, the trace norm is twice this positive mass. For \(M>N\), exchange the two exponents and reverse the sign of \(D\). This gives the stated formula with \(L=\max(M,N)\), including cases in which one reduced degree equals one.

**4. Hilbert–Schmidt norm and arithmetic reconstruction.** Before combining any equal-index contributions, each Gram operator's nonconstant diagonal has square mass \(q^4/(1-q^4)\). The overlap of the two Gram diagonals occurs only at \(MN\ell\), whose product is \(q^{2(M+N)\ell}\). Hence
\[
\operatorname{tr}(D^2)
=\operatorname{tr}((T^*T)^2)+\operatorname{tr}((TT^*)^2)
-2\operatorname{tr}(T^*T\,TT^*)
=2\left(\frac{q^4}{1-q^4}-\frac{q^{2(M+N)}}{1-q^{2(M+N)}}\right).
\]
All products are trace class here. For fixed \(q\in(0,1)\), the function \(j\mapsto q^{2j}/(1-q^{2j})\) strictly decreases on the positive integers. Therefore the trace norm uniquely specifies \(L\), and the Hilbert–Schmidt square uniquely specifies \(S\). The smaller degree is \(S-L\). This proves unique unordered recovery, without trying to recover the unobservable common divisor.

**5. Exact \(p\)-series and its limit.** The disjoint diagonal description yields, for every \(p>0\),
\[
\|D\|_{\mathcal S_p}^{p}
=\sum_{\substack{j\ge1\\N\nmid j}}q^{2pj}
+\sum_{\substack{j\ge1\\M\nmid j}}q^{2pj}
+\sum_{\ell\ge1}|q^{2N\ell}-q^{2M\ell}|^p.
\]
Write \(h=-\log q>0\). The first two geometric differences give
\[
h\left(\frac{2e^{-2ph}}{1-e^{-2ph}}
-\frac{e^{-2pNh}}{1-e^{-2pNh}}
-\frac{e^{-2pMh}}{1-e^{-2pMh}}\right)
\longrightarrow\frac{2-M^{-1}-N^{-1}}{2p}.
\]
For the overlap term, define \(f(t)=|e^{-2Nt}-e^{-2Mt}|^p\) on \([0,\infty)\). This function is continuous, vanishes at zero, and has an exponentially decreasing tail. Therefore its right-endpoint Riemann sums converge on every compact interval and the remaining tails are bounded uniformly by a convergent geometric sequence. Consequently
\[
h\sum_{\ell\ge1}f(h\ell)\longrightarrow\int_0^\infty f(t)\,dt.
\]
Writing \(a<b\) for the reduced degrees, the integral is
\[
\int_0^\infty e^{-2pa t}(1-e^{-2(b-a)t})^p\,dt
=\frac{1}{2(b-a)}\int_0^1u^{pa/(b-a)-1}(1-u)^p\,du,
\]
by \(u=e^{-2(b-a)t}\). This is the beta term. The argument works for every real \(p>0\), including quasi-Schatten exponents. At \(p=1\), the integral reduces to \(1/(2a)-1/(2b)\); at \(p=2\) it reduces to \(1/(4a)+1/(4b)-1/(a+b)\). Inserting either expression gives exactly the two endpoint constants stated above, an independent algebraic consistency check.

## Verification
The standalone `checker.py` uses only Python 3 standard-library functions. Running `python checker.py` reports `CHECKS_OK 438`. It constructs the weighted partial-permutation Gram diagonals independently of the asserted eigenvalue formula on finite sections, checks the full diagonal for the safely contained indices, checks the exact trace-zero and two ideal identities for coprime reduced pairs in the range \(1\le M,N\le7\) and several damping parameters, and tests the \(p=1,2\) beta reductions and the all-\(p\) small-\(h\) limit for four degree pairs. Numerical finite-section and limiting samples are supplementary; the infinite operator statement and every real \(p>0\) follow from the foregoing exact coefficient and Riemann-sum proof.

## Relationship to prior work
Leng and Zhao, *Schatten class membership of products of composition operators and their adjoints* (arXiv:2610.15472v1), study membership and general sufficient/necessary conditions for \(C_\psi^*C_\phi\) and its reversed product on Hardy and Bergman spaces. Their Theorems 3.17 and 3.24 address Hilbert–Schmidt criteria and inner-symbol membership equivalences; the paper does not state the present two-ideal numerical formulas, inverse reduced-degree classification, or critical beta-function law for self-commutators of the **product**. Published classifications of unweighted Hardy monomial composition–adjoint products determine their shift/Jordan structures and essential spectra, but fixed damping destroys those unweighted unitary coincidences at the level of the self-commutator's two numerical ideal invariants. Prior radial monomial **mixed commutator** studies compare \(C_\phi^*C_\psi-C_\psi C_\phi^*\), a different operator from \([T^*,T]\). The classical work of Abdollahi and Mehrangiz studies self-commutators of a **single** power-composition operator on Dirichlet space, not a mixed compact product on Hardy space. The coefficient rule and geometric sums are elementary and not claimed as independent innovations: the new conjunction is the exact inverse two-ideal fingerprint and the all-quasi-Schatten critical profile for this naturally arising product family.

## Limitations
The invariant pair is conditioned on knowing \(q\); no recovery of \(q\) is asserted. The original degrees are determined only after dividing by their greatest common divisor and only as an unordered pair. No result is claimed for general analytic symbols, nonradial perturbations, changing degrees in the limit, or \(p=\infty\). Published mathematical work on similar weighted partial permutations might contain equivalent special cases, and priority comparison with inaccessible older books or articles remains incomplete. The computation does not independently certify the infinite-dimensional mathematics; it checks the derived finite formulas and selected asymptotics.

## References
1. Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (first posted 2026-10-11), https://arxiv.org/abs/2610.15472.
2. *Arithmetic unitary types and essential spectra of Hardy monomial composition-adjoint products*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-arithmetic-unitary-types-and-essential-spectra-of-hardy-monomial--71d831748432.
3. *Arithmetic phase residues for radially damped monomial composition commutators*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-arithmetic-phase-residues-for-radially-damped-monomial-compositi--8d286d944eb1.
4. A. Abdollahi and S. Mehrangiz, *Self-Commutators of Composition Operators with Monomial Symbols on the Dirichlet Space*, Abstract and Applied Analysis 2011, Article 618968, https://doi.org/10.1155/2011/618968.
5. J. H. Clifford, D. Levi, and S. K. Narayan, *Commutator of composition operators with adjoints of composition operators*, Complex Variables and Elliptic Equations 57 (2012), 677–686, https://doi.org/10.1080/17476933.2010.534142.
