# Exact finite-spacing threshold for two marine reserves under correlated catastrophes

## Finding

In a two-reserve discrete-time occupancy model with catastrophe probability \(0<r<1\), inter-reserve distance \(d\geq0\), exponential colonization probability \(c(d)=e^{-\alpha d}\), and probability \(q(d)=e^{-d/\mu}\) that a catastrophe affects both reserves, let \(\rho(d)\) be the Perron eigenvalue of the transient occupancy transition matrix. Here \(\alpha,\mu>0\); the all-empty state is absorbing. Its infinitely-separated benchmark is \(L=1-r/2\).

Write \(k=\alpha\mu\), \(A=2-r\), \(B=4-3r\), and for \(k>1\) set
\[
H_r(k)=\frac{A}{k}\left(\frac{(k-1)A}{kB}\right)^{k-1}.
\]
There is exactly one \(k_c(r)>1\) satisfying \(H_r(k_c(r))=r\). The complete strict comparison with infinitely separated reserves is:

1. If \(0<k\le1\), there is exactly one finite \(d_0>0\) for which \(\rho(d_0)=L\); \(\rho(d)>L\) holds exactly when \(d>d_0\). A finite distance attains a global maximum strictly greater than \(L\).
2. If \(1<k<k_c(r)\), there are exactly two finite positive distances \(d_-<d_+\) at which \(\rho(d_\pm)=L\), with \(\rho(d)>L\) exactly for \(d_-<d<d_+\). Again, a finite global maximum strictly exceeds \(L\).
3. If \(k=k_c(r)\), exactly one finite distance \(d_*>0\) satisfies \(\rho(d_*)=L\); all other finite distances give \(\rho(d)<L\). Thus \(d_*\) is the unique finite maximizer, with no strict gain over the limiting benchmark.
4. If \(k>k_c(r)\), \(\rho(d)<L\) for every finite \(d\ge0\), and the supremum \(L\) is approached only as \(d\to\infty\).

The threshold is exact rather than a numerical near-plateau criterion. At \(k=2\), the strict finite-spacing advantage occurs precisely when
\[
0<r<\frac{10-4\sqrt3}{13}.
\]
For example \(k=2\), \(r=1/10\), and \(\mu=1\) produce an advantage window approximately \(0.789702149<d<2.821215764\), with a numerical maximum \(\rho\approx0.957274401\) at \(d\approx1.360456106\), versus \(L=0.95\).

## Assumptions and scope

States \(0,1,2\) denote the number of occupied identical marine reserves. State \(0\) is absorbing. Within a discrete step, first a catastrophe may occur, with probability \(r\). If both reserves were occupied, it kills both with conditional probability \(q(d)\), or one (symmetrically) with probability \(1-q(d)\). If exactly one reserve was occupied, a catastrophe kills the occupied reserve with probability \((1+q(d))/2\). After catastrophes, if one reserve remains occupied, it colonizes its empty partner with probability \(c(d)\). There is no external immigration or independent local extinction. This is the baseline transition mechanism of Wagner, Ross and Possingham, *Catastrophe Management and Inter-Reserve Distance for Marine Reserve Networks* (first publicly available arXiv version 2003-09-16), not that paper's subsequent enriched models.

The extinction process is governed by the largest eigenvalue of the substochastic transient block, which determines the asymptotic conditional-survival factor at every finite positive distance. The comparison \(L\) means a limit of this factor as inter-reserve distance diverges; it does not mean that two infinitely separated reserves have a physically realizable joint marine reserve network.

## Proof

**Transient matrix.** In occupancy-count order \((1,2)\), the catastrophe and colonization blocks are
\[
E_+=\begin{pmatrix}1-\tfrac r2(1+q)&0\\r(1-q)&1-r\end{pmatrix},\qquad
C_+=\begin{pmatrix}1-c&c\\0&1\end{pmatrix},
\]
where \(c=c(d)\), \(q=q(d)\). Their product is
\[
M(d)=\begin{pmatrix}
(1-\tfrac r2(1+q))(1-c)&(1-\tfrac r2(1+q))c\\
r(1-q)(1-c)&1-r+r(1-q)c
\end{pmatrix}.
\]
For \(d>0\) the two off-diagonal entries are strictly positive, hence its eigenvalues are distinct and real. As \(d\to\infty\), \(c,q\to0\), and the matrix becomes lower triangular with diagonal entries \(1-r/2\) and \(1-r\), proving \(\rho(d)\to L=1-r/2\). At \(d=0\), the matrix has spectral radius \(1-r<L\).

**An exact eigenvalue sign test.** Write the eigenvalues as \(\rho>\sigma\). Since
\[
M_{11}=(1-c)(1-\tfrac r2(1+q))<L
\]
and \(\sigma<M_{11}\) by strictly positive off-diagonal entries, \(\sigma<L\). Thus the sign of \(\rho-L\) is the opposite of the sign of \(\det(LI-M)\). Direct expansion gives the exact identity
\[
\det(LI-M)=\frac r4\{rq-c[2-r-(4-3r)q]\}.
\]
Consequently, for every \(d>0\),
\[
\boxed{\rho(d)>L\quad\Longleftrightarrow\quad q^{k-1}(A-Bq)>r},
\qquad q=e^{-d/\mu}\in(0,1).
\]
Equality and strict reverse inequality follow from the same determinant identity. The inequality forces \(0<q<A/B\), and \(A/B<1\) for every \(0<r<1\).

**The sharp alternatives.** On \(0<q<A/B\), if \(0<k\le1\), both positive factors \(q^{k-1}\) and \(A-Bq\) are nonincreasing as \(q\) grows, with the product strictly decreasing. At \(q\downarrow0\) its value tends to \(+\infty\) for \(k<1\) and to \(A>r\) for \(k=1\); at \(q\uparrow A/B\) it tends to zero. There is precisely one equality root, so decreasing \(q\) (increasing \(d\)) gives the claimed half-line.

When \(k>1\), the function \(F(q)=q^{k-1}(A-Bq)\) vanishes at the endpoints \(0,A/B\) and has exactly one maximum, because
\[
F'(q)=q^{k-2}\{(k-1)A-kBq\}.
\]
Its unique maximizer is \(q_*=(k-1)A/(kB)\), with maximum \(H_r(k)\). A horizontal level \(r>0\) therefore intersects this graph twice, once (tangentially), or not at all according as \(H_r(k)>r\), \(=r\), or \(<r\). Those are exactly the two-boundary, tangency, and no-advantage alternatives in distance.

For \(k>1\), \(H_r(k)\) is continuous and strictly decreasing in \(k\): each \(q^{k-1}(A-Bq)\) decreases strictly in \(k\) on the compact region \(0<q\le A/B<1\), including at its maximizing point. Also \(H_r(k)\to A>r\) as \(k\downarrow1\), and \(H_r(k)\to0\) as \(k\to\infty\), since \(H_r(k)\le A(A/B)^{k-1}\). Hence a unique \(k_c(r)>1\) exists. Continuity of \(\rho\) and its limit at infinity give the stated finite-optimizer existence and nonexistence assertions.

Finally, at \(k=2\), \(H_r(2)=A^2/(4B)\), so the strict-advantage condition is \((2-r)^2>4r(4-3r)\), equivalent to \(13r^2-20r+4>0\). In \(0<r<1\) this is exactly \(r<(10-4\sqrt3)/13\). All boundary and equality cases are included.

## Verification

Run `python3 verify.py`. The standard-library-only checker reconstructs the determinant identity in exact rational arithmetic at 486 parameter triples, verifies the strict diagonal bound, tests the direct Perron eigenvalue versus the comparison expression over 12,000 deterministic random parameter triples, checks critical-parameter monotonic regimes, and verifies the explicit quadratic example. On the packaged source it reports `12532 checks passed`. Numerical tests are supplementary: the proof above treats the continuous parameter domain exactly.

## Relationship to prior work

Wagner, Ross and Possingham (arXiv:math/0309255, first public version 2003-09-16; journal 2007) introduced this baseline two-reserve catastrophe–colonization transition matrix and numerically investigated distance-dependent quasi-stationary persistence. This result does **not** claim their model or eigenvalue objective as new. The mathematical addition is a complete exact phase classification versus infinitely separated reserves: a unique critical ratio, finite bounded advantage windows, a tangency regime, and proof that some parameter regions have no finite maximizer. The accessible complete preprint discusses numerical near-plateaus and finite optima but does not give this sign-equivalent determinant identity or threshold classification.

The published two-reserve continuous-time common-catastrophe result *Mean-persistence reserve spacing is never shorter than tail-persistence spacing* treats different catastrophe clocks and two different persistence objectives; its proof and hypotheses do not imply this discrete-time baseline matrix's finite-versus-infinite spectral comparison. Blowes and Connolly (2012) study long-run growth and quasi-extinction under stochastic demographic covariance, a distinct model. Its full text was not accessible in the present comparison, and abstract-level overlap in reserve-spacing phase transitions remains a historical-priority risk, not proof of coverage. Shanks, Grantham and Carr (2003) provide empirical and conceptual motivation for dispersal-distance-dependent reserve spacing, without this Markov eigenvalue classification in the material accessed.

## Limitations

The theorem is exact for the specified two identical-reserve, one-catastrophe-per-step baseline, exponentially decaying colonization and common-hit probability, and the long-run transient Perron factor. It does not classify absolute optimal locations when an interior maximizer exists, except by existence and the benchmark comparison, nor does it address finite-horizon survival, mean extinction time from a chosen starting state, continuous-time processes, external recruitment, heterogeneous reserves, correlated multiple events or empirical parameter uncertainty. Real reserve distances are finite; mathematical separation to infinity is only a benchmark. The theorem is a theoretical diagnostic, not a fitted conservation recommendation. No independent audit or priority certification has been performed.

## References

- Wagner, L. D., Ross, J. V., and Possingham, H. P., *Catastrophe Management and Inter-Reserve Distance for Marine Reserve Networks*, arXiv:math/0309255 (first public version 2003-09-16), later *Ecological Modelling* **201** (2007), 82–88. https://arxiv.org/abs/math/0309255 ; https://doi.org/10.1016/j.ecolmodel.2006.07.030.
- Blowes, S. A., and Connolly, S. R., *Risk spreading, connectivity, and optimal reserve spacing*, *Ecological Applications* **22** (2012), 311–321. https://doi.org/10.1890/11-0952.1.
- Shanks, A. L., Grantham, B. A., and Carr, M. H., *Propagule dispersal distance and the size and spacing of marine reserves*, *Ecological Applications* **13** (2003), 159–169. https://doi.org/10.1890/1051-0761(2003)013%5B0159:PDDATS%5D2.0.CO;2.
- *Mean-persistence reserve spacing is never shorter than tail-persistence spacing*, public mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mean-persistence-reserve-spacing-is-never-shorter-than-tail-pers--fe260ea93f6a.
