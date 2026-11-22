# Singular square-root fibers and square-image entropy in cyclic Loewy-three Nakayama radicals

## Finding

Let \(Q_n\) be the oriented cycle on \(n\ge 3\) vertices, and let \(A=\mathbb F_q Q_n/J^3\), where \(q\) is any prime power and \(J\) is the arrow ideal. Write \(a_i\) for the arrow from vertex \(i\) to vertex \(i+1\), and \(p_i=a_i a_{i+1}\) for the length-two path, with indices modulo \(n\). For any prescribed \(Y=\sum_i c_i p_i\in J^2\), we determine the exact number \(R(Y)=\#\{X\in A:X^2=Y\}\), including zero coefficients among the \(c_i\).

Put \(w=q-1\). Define the weighted path independent-set polynomials \(I_m(w)\) by \(I_m(w)=1\) for \(m\le0\), \(I_1(w)=1+w\), and \(I_m(w)=I_{m-1}(w)+w I_{m-2}(w)\) for \(m\ge2\). Then:

1. If all \(c_i\) vanish, \[R(Y)=q^n\bigl(I_{n-1}(w)+wI_{n-3}(w)\bigr).\]
2. If both zero and nonzero coordinates occur, let \(b\ge1\) be the number of maximal cyclic consecutive runs of nonzero \(c_i\), and let \(L_1,\dots,L_b\ge1\) be the lengths of the intervening zero runs. If any \(L_j=1\), then \(R(Y)=0\). Otherwise
   \[\boxed{R(Y)=q^n w^b\prod_{j=1}^b I_{L_j-3}(w).}\]
   In particular, for mixed support the fiber depends on the zero-gap lengths but **not** on the values of the nonzero coefficients.
3. If every \(c_i\ne0\), set
   \[r=\frac{\prod_{i\text{ even}}c_i}{\prod_{i\text{ odd}}c_i}\in\mathbb F_q^\times.\]
   For even \(n\), \(R(Y)=q^n w\) precisely when \(r=1\), and is zero otherwise. For odd \(n\), \(R(Y)=q^n\#\{t\in\mathbb F_q^\times:t^2=r\}\). This familiar full-support toric calculation is included for completeness; the new statement concerns the singular fibers and their aggregate image law.

The set of squares of radical elements is contained in \(J^2\). Let \(S_n(q)=\#\{X^2:X\in J\}\). On the ordered states \((00),(01),(10),(11)\) define

\[
T(w)=\begin{pmatrix}
1&w&0&0\\
0&0&1&w\\
1&0&0&0\\
0&0&1&w
\end{pmatrix}.
\]

Then the **complete square-image cardinality** is

\[
\boxed{S_n(q)=\operatorname{tr}(T(w)^n)-w^n+
\begin{cases}
w^{n-1},&n\text{ even},\\
w^n/\gcd(2,w),&n\text{ odd}.
\end{cases}}
\]

For fixed \(q\), let \(\rho_q\) be the unique real root in \((q-1,q)\) of
\[t^3-qt^2+(q-1)t-(q-1)=0.\]
The image satisfies \(S_n(q)\sim \rho_q^n\) as \(n\to\infty\). Thus the fraction of attainable radical-square targets has the sharp asymptotic
\[\frac{S_n(q)}{q^n}\sim\left(\frac{\rho_q}{q}\right)^n,\]
which decreases exponentially although every target lies in the \(n\)-dimensional vector space \(J^2\).

## Assumptions and scope

All algebras are associative unital finite-dimensional \(\mathbb F_q\)-algebras; \(n\ge3\) avoids double identification of length-two cyclic paths, and \(q\) is a prime power of arbitrary characteristic. The source of the square map is the entire radical \(J\), and the target is \(J^2\); the prescribed-root statement in fact counts roots in the entire algebra \(A\) for these targets. No assertion is made about square roots of targets outside \(J^2\), nor about higher Loewy lengths.

A cyclic nonzero-coordinate run has positive length, and its following zero gap has length \(L_j\). For a zero gap of length two or three, the convention \(I_m=1\) for \(m\le0\) applies. Products over an empty collection are one. For the all-nonzero case, even/odd indices refer to any fixed cyclic labeling; the criterion is invariant under rotating the labels.

## Proof

**Reduction to the edge-product map.** Let \(e_i\) denote the vertex idempotents. Every \(X\in A\) has a unique form
\[X=\sum_i d_i e_i+\sum_i u_i a_i+\sum_i v_i p_i.\]
If \(X^2\in J^2\), passage to \(A/J\simeq \mathbb F_q^n\) gives \(d_i^2=0\) for each \(i\). Hence every \(d_i=0\), without any restriction on characteristic. Since \(J^3=0\), the length-two coefficients of \(X^2\) are precisely \(u_i u_{i+1}\), independently of the \(n\) freely selectable coefficients \(v_i\). Thus
\[R(Y)=q^n\#\{(u_i)\in\mathbb F_q^n:u_i u_{i+1}=c_i\text{ for all }i\}.\]

**Zero target.** When every \(c_i=0\), the positions with \(u_i\ne0\) form an independent set on the cycle, and each chosen position has \(w\) choices. Partitioning independent sets according to whether vertex zero is chosen gives \(I_{n-1}(w)+wI_{n-3}(w)\).

**Mixed support.** Every nonzero edge target \(c_i\) forces the two adjacent unknowns to be nonzero. For a maximal consecutive run of \(r\) nonzero edges, choosing its first unknown in \(w\) ways determines the remaining \(r\) unknowns successively. The zero edge immediately following that run forces the next unknown to vanish, while the zero edge immediately preceding the next run forces the first unknown on that gap to vanish. Therefore a gap of only one zero edge is impossible: its endpoints are both forced nonzero. For a gap of \(L\ge2\) zero edges, precisely \(L-3\) internal vertices are not forced by adjacent nonzero runs (interpreted as zero when \(L\le3\)). Their allowed nonzero supports are independent sets on a path, contributing \(I_{L-3}(w)\) possibilities. Distinct runs/gaps use disjoint free coordinates; multiplying their contributions yields the mixed-fiber formula. All nonzero target values can be propagated along their runs, which explains value-independence.

**Full support.** If all \(c_i\ne0\), all \(u_i\ne0\). Iterating \(u_{i+1}=c_i/u_i\) around the cycle gives a consistency equation. For even \(n\) it is exactly \(\prod_{i\text{ even}}c_i=\prod_{i\text{ odd}}c_i\), and leaves the initial \(u_0\) arbitrary nonzero. For odd \(n\) the equation is \(u_0^2=r\). This completes the prescribed-target classification.

**Counting attained targets.** A mixed-support coefficient pattern is attainable exactly when it has no cyclic zero run of length one. Its nonzero coefficients can independently take any of \(w\) values. The same support rule includes the all-zero pattern and the all-nonzero pattern, although some all-nonzero coefficient assignments are forbidden by the full-support consistency equation. Encode a coefficient as zero or nonzero. A cyclic binary word has no isolated zero precisely when it avoids the consecutive triple \((1,0,1)\). The stated transfer matrix records consecutive pairs and weights each appended \(1\) by \(w\); consequently \(\operatorname{tr}(T(w)^n)\) counts all weighted cyclic patterns with that avoidance property. Subtract the \(w^n\) unrestricted full-support patterns. For even \(n\), their actually attained subset has \(w^{n-1}\) elements (one multiplicative consistency equation). For odd \(n\), the cyclic edge-product map on the \(n\)-torus has kernel of size \(\gcd(2,w)\), so exactly \(w^n/\gcd(2,w)\) full-support targets are attained. This gives \(S_n(q)\).

**Asymptotic.** Direct determinant expansion yields
\[\det(tI-T(w))=t\bigl(t^3-(w+1)t^2+wt-w\bigr).\]
The positive-weight directed graph of \(T(w)\) is strongly connected and contains a loop, hence \(T(w)\) is primitive. Perron–Frobenius theory therefore gives \(\operatorname{tr}(T(w)^n)\sim\rho_q^n\), with the Perron eigenvalue simple. The displayed cubic is negative at \(t=w\) and positive at \(t=w+1=q\), and the unique positive dominant root lies between them; thus \(w<\rho_q<q\). Each full-support correction has size \(O(w^n)\), strictly lower order, proving both asymptotics.

## Verification

The standalone `check_roots.py` exhaustively enumerates all \(q^n\) choices of arrow coefficients and all \(q^n\) prescribed target vectors in each listed parameter pair, including the field \(\mathbb F_4\) modeled by the irreducible polynomial \(T^2+T+1\). It compares the direct root count for **each target** to the four-case formula, and independently checks the total image cardinality from the transfer matrix. For \(q=2\) and \(n=3,4,5,6,8\), \(q=3\) and \(n=3,4,5,6\), \(q=4\) and \(n=3,4,5\), and \(q=5\) and \(n=3,4\), all exhaustive checks pass. The attached `check_roots_output.txt` is the recorded execution transcript. These finite checks are not used as proofs of unbounded statements.

Reproduce with `python3 check_roots.py` using a standard Python 3 interpreter; no nonstandard dependencies are required.

## Relationship to prior work

Shen, *The singularity category of a Nakayama algebra* (arXiv:1404.2451), studies the representation-theoretic setting of Nakayama algebras. Volkov and Zvonareva, *Derived Picard groups of selfinjective Nakayama algebras* (arXiv:1508.01721), investigate another homological invariant of selfinjective cyclic Nakayama algebras. Neither inspected discussion states the prescribed singular-target square-root count or the radical square-image growth constant. Delgado-Eckert, *An algebraic and graph theoretical framework to study monomial dynamical systems over a finite field* (arXiv:0711.1230), develops general monomial dynamics and fixed-point algorithms, but its inspected problem statements do not give these prescribed one-step image fibers. The full-support multiplicative consistency law is classical toric-edge reasoning and is **not** presented as a novel component; graph toric-set methods are represented by Neves, Vaz Pinto and Villarreal, *Vanishing ideals over graphs and even cycles* (arXiv:1111.6278). The separately new claim is the zero-gap-dependent fiber law together with the **full** image count and its entropy rate, which require singular coordinate patterns absent from the algebraic torus.

## Limitations

The classification concerns squares of elements of \(J\) in truncation length three and prescribed targets in \(J^2\). The much larger square-map image on the full algebra \(A\) is not counted. No structural classification of higher powers or truncations is asserted. Potentially equivalent finite-field monomial-map results for graph maps with coordinate zeros remain a historical-priority risk; the inspected source material and searches do not constitute a proof of priority. The asymptotic fixes \(q\) before letting \(n\to\infty\). The result has had no independent mathematical audit.

## References

- E. Delgado-Eckert, *An algebraic and graph theoretical framework to study monomial dynamical systems over a finite field*, arXiv:0711.1230, first publicly submitted 2007-11-08, https://arxiv.org/abs/0711.1230.
- D. Shen, *The singularity category of a Nakayama algebra*, arXiv:1404.2451, first publicly submitted 2014-04-09, https://arxiv.org/abs/1404.2451.
- Y. Volkov and A. Zvonareva, *Derived Picard groups of selfinjective Nakayama algebras*, arXiv:1508.01721, first publicly submitted 2015-08-07, https://arxiv.org/abs/1508.01721.
- A. Neves, M. Vaz Pinto and R. H. Villarreal, *Vanishing ideals over graphs and even cycles*, arXiv:1111.6278, 2011, https://arxiv.org/abs/1111.6278.
