# Degree-mod-three tangency dichotomy for quasi-Galois three-centre lines of Fermat hypersurfaces

## Finding
Let \(N=n+2\), with integers \(n\ge1\) and \(d\ge4\), and let \(F=V(X_1^d+\cdots+X_N^d)\subset\mathbb P^{N-1}_{\mathbb C}\). Miura and Takahashi identify the order-two quasi-Galois centres as
\[
Q=\{[e_i-\zeta e_j]:1\le i<j\le N,\ \zeta^d=1\}.
\]
A line is **rich** if it contains at least three distinct points of \(Q\). The rich lines consist of precisely \(\binom N2\) coordinate lines, each containing \(d\) centres, and \(d^2\binom N3\) three-centre lines, each containing exactly three:
\[
L_{ijk}^{\zeta,\eta}=\mathbb P\bigl(\mathbb C(e_i-\zeta e_j)+\mathbb C(e_i-\eta e_k)\bigr),\quad i<j<k,\quad\zeta^d=\eta^d=1.
\]
Every coordinate rich line meets \(F\) transversely. Every three-centre line meets \(F\) transversely if and only if \(d\not\equiv1\pmod3\). When \(d\equiv1\pmod3\), it has exactly two distinct ordinary tangencies of intersection multiplicity two. Writing \(\omega^2+\omega+1=0\), their coordinates are
\[
[(1+\omega)e_i-\omega\zeta e_j-\eta e_k],\qquad [(1+\omega^2)e_i-\omega^2\zeta e_j-\eta e_k].
\]
No tangency point is shared by distinct rich lines, so there are exactly \(2d^2\binom N3\) tangency points. The projective monomial group \((\mu_d^N/\mu_d)\rtimes S_N\), of order \(N!d^{N-1}\), acts transitively on these points. Each stabilizer has order \(3(N-3)!d^{N-3}\). If \(d\) is odd, the three quasi-Galois centres on each three-centre line are simple points of \(F\), distinct from the tangencies. The degree-seven case has intersection divisor exactly three simple centres plus the two double tangencies.

## Assumptions and scope
Everything is over \(\mathbb C\), in characteristic zero. Lines are projective lines in the specified ambient projective space; an ordinary tangency means the scheme-theoretic intersection with \(F\) has multiplicity exactly two at the indicated point. We classify lines rich with respect to the *order-two* centres, not lines containing any number of all Galois points. Statements of transversal intersection concern their degree-\(d\) zero-dimensional intersection schemes and not tangent hyperplanes. The paper of Miura--Takahashi supplies the complete list of centres; the incidence and tangency assertions below are separate deductions.

## Proof
**Step 1: all rich lines.** Every centre is supported on exactly two coordinate positions. If two centres have the same support \(\{i,j\}\), they span the coordinate line \(\mathbb P(\mathbb Ce_i+\mathbb Ce_j)\), containing exactly the \(d\) centres with this support; no other centre lies there. If two centres have disjoint supports, their span contains no third centre: every vector with nonzero coefficients from both generators has support four. If their supports overlap in one coordinate, relabel the pair as \([e_i-\zeta e_j]\) and \([e_i-\eta e_k]\). A third centre on their span must have support \(\{j,k\}\), and is uniquely \([\zeta e_j-\eta e_k]\), equivalently \([e_j-(\eta/\zeta)e_k]\). No fourth centre is possible because other supports are absent. Distinct support triples and parameter pairs give distinct lines. This proves the entire list and counts without an assumption of genericity.

**Step 2: exact intersection polynomial.** Write a general point on a three-centre line as
\[
[(s+t)e_i-\zeta s e_j-\eta t e_k],\qquad[s:t]\in\mathbb P^1.
\]
Since \(\zeta^d=\eta^d=1\), its intersection with \(F\) is the homogeneous degree-\(d\) binary form
\[
H_d(s,t)=(s+t)^d+(-1)^d(s^d+t^d).
\]
The restriction to a coordinate line is \(s^d+t^d\), which has \(d\) simple complex roots. Thus coordinate rich lines are transverse.

**Step 3: the complete repeated-root criterion.** Put \(\varepsilon=(-1)^d\) and \(h_d(x)=H_d(x,1)=(x+1)^d+\varepsilon(x^d+1)\). The derivative is \(d((x+1)^{d-1}+\varepsilon x^{d-1})\). If \(h_d(x)=h_d'(x)=0\), eliminating the derivative term from \(h_d\) shows \(x^{d-1}=1\) and \((x+1)^{d-1}=-\varepsilon\); conversely these two equations imply both vanish. As complex numbers they imply \(|x|=|1+x|=1\), and hence \(x=\omega\) or \(x=\omega^2\), where \(\omega\) is a primitive cube root of unity. Since \(\omega+1=-\omega^2\), both candidates satisfy the two equations precisely when \(d\equiv1\pmod3\): for odd \(d\), this is \(d\equiv1\pmod6\); for even \(d\), it is \(d\equiv4\pmod6\). At either root, direct substitution into
\[
h_d''(x)=d(d-1)\bigl((x+1)^{d-2}+\varepsilon x^{d-2}\bigr)=d(d-1)\varepsilon\left(\frac1x-\frac1{x+1}\right)
\]
shows that it is nonzero, so both roots have exact multiplicity two. The point \([1:0]\) is not on the intersection if \(d\) is even (the leading homogeneous coefficient is \(2\)); if \(d\) is odd it is a simple zero because the coefficient of \(s^{d-1}t\) is \(d\). Thus there are no omitted repeated roots at infinity. For odd \(d\), \([s:t]=[1:0],[0:1],[1:-1]\) are precisely the three quasi-Galois centres and are simple roots. The remaining points are simple, since every repeated root has been classified.

**Step 4: distinctness of contacts.** A contact point has three nonzero coordinates. Distinct support triples therefore cannot give the same contact point. For one fixed triple \(\{i,j,k\}\), its coordinate plane meets \(F\) in the smooth plane Fermat curve \(X_i^d+X_j^d+X_k^d=0\). A smooth plane curve has a unique projective tangent line at each point. Two different three-centre lines in this plane consequently cannot both be tangent at the same point. The two contacts on an individual line are distinct because \(\omega\ne\omega^2\). This proves the stated total \(2d^2\binom N3\).

**Step 5: one symmetry orbit.** The monomial group permutes triples of coordinate positions transitively, and coordinatewise multiplication by \(d\)-th roots of unity independently changes \(\zeta\) and \(\eta\). Thus it is transitive on the three-centre lines. Swapping the \(j\)- and \(k\)-coordinates carries a contact corresponding to \(\omega\) on \(L_{ijk}^{\zeta,\eta}\) to a contact corresponding to \(\omega^2\) on \(L_{ijk}^{\eta,\zeta}\), after projective rescaling. This proves transitivity on contacts. The stabilizer order follows from orbit-stabilizer:
\[
\frac{N!d^{N-1}}{2d^2\binom N3}=3(N-3)!d^{N-3}.
\]

## Verification
The accompanying standalone Python 3 script `verify.py` uses exact rational polynomial arithmetic and no nonstandard modules. It computes the monic gcd of \(h_d\) and \(h_d'\) for every integer \(4\le d\le40\), obtaining \(x^2+x+1\) exactly when \(d\equiv1\pmod3\), and \(1\) otherwise. It also checks the projective-leading-coefficient and group/order combinatorics for \(3\le N\le8\) and selected degrees. It prints `CERTIFICATE_OK` on success. These are finite corroborations; the proof in Steps 1--5 establishes every specified \(d,N\).

## Relationship to prior work
Miura and Takahashi, arXiv:2610.09331, Section 4, determine the order-two quasi-Galois centres using complex reflection groups; they do not state the degree-mod-three tangency criterion or the rich-line contact enumeration. Fukasawa, Miura and Takahashi, arXiv:2211.16033, Section 5, treat arrangements and multiple tangents for plane quartics: the fact that some three-centre lines of the Fermat quartic are bitangent is therefore **not** claimed as new. Oka's lecture on Fermat curves and maximal nodal curves gives a general parameterization of plane Fermat bitangents, and hence covers the underlying classical bitangent context but does not explicitly identify all higher-degree quasi-Galois three-centre lines or their congruence-controlled contacts. Toft and Moe, arXiv:2412.16993, investigate tangent and osculating arrangements on Fermat curves and cite the known total bitangent number, not this distinguished rich-line incidence/contact classification. The claim here is the *joint, uniform classification* of three-centre incidence and its tangency for all degrees and all dimensions, not a new classification of all plane Fermat bitangents.

## Limitations
This result is over \(\mathbb C\), is restricted to lines rich in order-two quasi-Galois centres, and does not classify all tangent lines, bitangents, osculating lines, or tangent hyperplanes to a Fermat hypersurface. For plane curves, the special degree-four multiple-tangency behavior and the general bitangent background are classical. Historical priority of the precise combined all-degree statement has not been independently confirmed. The exact script checks only a bounded degree range; it is not a substitute for the uniform proof. Independent mathematical audit has not been performed.

## References
1. K. Miura and T. Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties*, arXiv:2610.09331 (first public 2026-10-07), Section 4, https://arxiv.org/abs/2610.09331.
2. S. Fukasawa, K. Miura and T. Takahashi, *Quasi-Galois points, II: Arrangements*, arXiv:2211.16033 (2022), especially Section 5, https://arxiv.org/abs/2211.16033.
3. M. Oka, *On Fermat curves and maximal nodal curves*, 2014 lecture slides (bitangent formulas, pp. 20--22); associated Michigan Mathematical Journal article (2005). https://pages.mini.pw.edu.pl/~aito/pdf/Oka_Jun14.pdf.
4. K. Toft and T. Moe, *The Fermat curves, arrangements of lines, and intersections of osculating curves*, arXiv:2412.16993, Section 4.2, https://arxiv.org/html/2412.16993v2.
