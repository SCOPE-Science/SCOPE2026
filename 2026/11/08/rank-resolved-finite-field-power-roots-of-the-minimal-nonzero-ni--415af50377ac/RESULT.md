# Rank-resolved finite-field power roots of the minimal nonzero nilpotent orbit

## Finding
Let \(q\) be any prime power, \(n\ge 2\), \(m\ge 2\), and \(C\in M_n(\mathbb F_q)\) a nonzero rank-one matrix satisfying \(C^2=0\). For each integer \(r\), set
\[
R_{n,m,q}(r;C)=\#\{X\in M_n(\mathbb F_q):X^m=C,\ \operatorname{rank}X=r\}.
\]
If \(n\le m\), all these fibers are empty. If \(n\ge m+1\), set \(k=n-m-1\), \(\mu=(2,1^{n-2})\), and, for a partition \(\lambda\), define
\[
A_\lambda(q)=q^{\sum_{j\ge1}(\lambda'_j)^2}
\prod_{d\ge1}\prod_{i=1}^{b_d(\lambda)}(1-q^{-i}),
\]
where \(\lambda'\) is the conjugate partition and \(b_d(\lambda)\) is the multiplicity of the part \(d\). The empty products equal one. Then the **complete rank-resolved prescribed-target power-fiber law** is
\[
\boxed{R_{n,m,q}(r;C)=
\sum_{\substack{\nu\vdash k,\ \nu_1\le m\\ \ell(\nu)=n-1-r}}
\frac{A_\mu(q)}{A_{(m+1)\cup\nu}(q)}.}
\]
For \(k=0\), the empty partition occurs once. Every summand is a positive integer. In particular, the possible root ranks are **exactly**
\[
\boxed{m\le r\le n-1-\left\lceil\frac{n-m-1}{m}\right\rceil,}
\]
with no gaps, and every listed rank occurs over every finite field. The answer depends on the target only through its nonzero rank-one square-zero similarity type.

For fixed \(n,m\) with \(n\ge m+1\), a uniformly chosen solution of \(X^m=C\) has the maximum permitted rank with probability tending to one as \(q\to\infty\) through prime powers. More precisely, writing \(k=am+b\), \(0\le b<m\), the unique root Jordan type of greatest conjugacy-orbit dimension is \((m+1,m^a,b)\), with a zero part omitted.

## Assumptions and scope
The target must be **nonzero**, satisfy \(C^2=0\), and have rank one. Fields of any characteristic, including those dividing \(m\), are included. Here \(X^m\) is the ordinary product of \(m\) copies of \(X\), and all matrices are counted as labeled matrices in a fixed basis, not up to conjugacy. The formula does not count roots of the zero target, roots of arbitrary nilpotent targets, or roots with additional symmetry constraints.

## Proof
**Step 1: exhaustive Jordan types.** Since \(X^m=C\) and \(C^2=0\), one has \(X^{2m}=0\), so \(X\) is nilpotent. Its Jordan type \(\lambda=(\lambda_1,\ldots)\) is defined over \(\mathbb F_q\) (nilpotent Jordan blocks require no field extension). The elementary identity
\[
\operatorname{rank}(J_d(0)^m)=\max(d-m,0)
\]
holds in every characteristic. Thus \(\operatorname{rank}X^m=1\) is equivalent to **exactly one** Jordan block of size \(m+1\), with every other block of size at most \(m\). Conversely, each such type has \(X^m\) of rank one and square zero and hence similar to \(C\). This gives precisely the types \(\lambda=(m+1)\cup\nu\), where \(\nu\vdash k=n-m-1\) has parts at most \(m\). No solution exists when \(n\le m\).

**Step 2: centralizer size lemma.** Regard a nilpotent Jordan matrix \(J_\lambda\) as the \(\mathbb F_q[t]\)-module \(\bigoplus_d(\mathbb F_q[t]/(t^d))^{b_d(\lambda)}\). The dimension of its endomorphism algebra is
\[
\sum_{d,e}b_d(\lambda)b_e(\lambda)\min(d,e)=\sum_{j\ge1}(\lambda'_j)^2.
\]
Its semisimple quotient is \(\prod_d M_{b_d(\lambda)}(\mathbb F_q)\): equal-length blocks give the full matrix factors upon reduction modulo the respective maximal ideals, while maps between unequal lengths and maps divisible by \(t\) lie in the Jacobson radical. The radical is nilpotent, so an endomorphism is invertible precisely when its images in all these matrix factors are invertible. The unit count therefore equals the number of points of the invertible centralizer,
\[
|Z_{\mathrm{GL}_n(\mathbb F_q)}(J_\lambda)|
=q^{\sum_j(\lambda'_j)^2}
\prod_d\prod_{i=1}^{b_d(\lambda)}(1-q^{-i})=A_\lambda(q).
\]
In particular \(A_\mu(q)=q^{(n-1)^2+1}(1-q^{-1})\prod_{i=1}^{n-2}(1-q^{-i})\), including \(n=2\).

**Step 3: count a prescribed fiber.** Let \(\mathcal O_\lambda\) be the \(\mathrm{GL}_n(\mathbb F_q)\)-orbit of \(J_\lambda\). The power map \(X\mapsto X^m\) is equivariant under conjugation. On each type from Step 1, its image is the entire orbit \(\mathcal O_\mu\), and every target in that orbit has the same number of preimages. Orbit-stabilizer gives
\[
\frac{|\mathcal O_\lambda|}{|\mathcal O_\mu|}
=\frac{|Z_{\mathrm{GL}_n}(J_\mu)|}{|Z_{\mathrm{GL}_n}(J_\lambda)|}
=\frac{A_\mu(q)}{A_\lambda(q)}.
\]
These disjoint type strata partition all roots. A nilpotent matrix of type \(\lambda\) has rank \(n-\ell(\lambda)=n-1-\ell(\nu)\). Summing by this rank proves the displayed formula and the integrality of its summands.

**Step 4: exact rank interval.** A partition of \(k\) into \(L\) positive parts each at most \(m\) exists exactly when \(\lceil k/m\rceil\le L\le k\). Construct one by starting with \(L\) ones and distributing the remaining \(k-L\) boxes, at most \(m-1\) per part. Substitution into \(r=n-1-L\) gives the claimed complete rank interval. The case \(k=0\) gives only \(r=m\).

**Step 5: concentration on maximum rank.** Among partitions of \(k\) with parts at most \(m\), the greedy partition \(\nu^*=(m^a,b)\), omitting \(b=0\), strictly dominates every different such partition. Strict dominance reverses the value of \(E(\lambda)=\sum_j(\lambda'_j)^2\): one can reach \(\nu^*\) from a different partition by moving boxes from shorter to longer rows, and each move strictly lowers \(E\). Thus \((m+1)\cup\nu^*\) uniquely minimizes \(E\) among the admissible root types. For fixed \(\lambda\), the factor multiplying \(q^{(n-1)^2+1-E(\lambda)}\) in Step 3 tends to one as \(q\to\infty\). All other types are smaller by at least one integral power of \(q\), proving concentration on the maximum-rank stratum.

## Verification
The standalone standard-library program `verify_roots.py` constructs every matrix commuting with the standard target \(C=E_{1,2}\) (using one-based row and column indices), then tests its actual \(m\)-th power and ranks. Every root must commute with \(C\), so the search is exhaustive, not sampled. The full log is `verification_output.txt`.

The tests cover \(q=2,3,4,5\), dimensions \(3,4,5\) as recorded, and every \(m\) with \(2\le m<n\) in those cases, including a genuine \(\mathbb F_4\) arithmetic implementation. Representative checked fiber counts are \(2\) for \((n,m,q)=(3,2,2)\), \(12\) for \((4,2,2)\), and, when \((n,m,q)=(5,2,2)\), counts \(56\) at rank two and \(168\) at rank three. These are independent finite corroborations, not proofs for all dimensions or fields. To reproduce, run `python verify_roots.py` with Python 3.

## Relationship to prior work
Higham and Lin's 2009 preprint and Schwaiger's work analyze existence and canonical-form descriptions of matrix roots; Britnell and Wildon develop finite-field centralizer and nilpotent-similarity tools. Öztürk's 2021 paper gives a detailed general criterion for possible nilpotent-root Jordan types. Those results supply the natural foundations for the present count but, in the inspected material, do not state the **exact finite-field multiplicity of each rank of a root of a fixed nonzero minimal nilpotent target**, or the maximum-rank concentration property. The present proof derives the result from Jordan power behavior together with the finite-field centralizer unit formula; the classical ingredients are not separately claimed as new.

## Limitations
The assertion is conditional on a nonzero rank-one square-zero target; zero and larger-rank targets require different type lists. It counts actual matrices, not components of a nonreduced solution scheme or orbits under the target's centralizer. The novelty comparison does not rule out an unidentified general orbit-fiber theorem that packages this rank-stratified count as a corollary. Only the finite cases listed in the verification log were exhaustively enumerated; independent external validation has not been performed.

## References
1. N. J. Higham and L. Lin, *On pth Roots of Stochastic Matrices*, MIMS EPrint 2009.21, version dated 2009-03-10, https://eprints.maths.manchester.ac.uk/1241/ .
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first posted 2010-01-06, https://arxiv.org/abs/1001.0811 .
3. J. Schwaiger, *More on Rootless Matrices*, Anzeiger Abt. II 141 (2005), 3–8; printed 2006, https://austriaca.at/0xc1aa5572%200x00145b6e.pdf .
4. S. Öztürk, *On m-th roots of nilpotent matrices*, Electronic Journal of Linear Algebra 37 (2021), 718–733, https://doi.org/10.13001/ela.2021.6331 .
5. J. A. Green, *The characters of the finite general linear groups*, Transactions of the American Mathematical Society 80 (1955), 402–447.
