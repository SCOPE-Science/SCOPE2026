# Unique maximum predecessor multiplicity for finite cyclic Rule 22

## Finding
For every integer \(n\ge 1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the one-step elementary cellular automaton Rule 22 with **cyclic indices**: the output at site \(i\) is one if and only if exactly one of the three entries \(x_{i-1},x_i,x_{i+1}\) is one. Entries in the neighborhood are counted with their positions, including when \(n=1\) or \(n=2\).

**Theorem.** Among all labeled outputs, the all-zero word is the **unique** word with the greatest number of one-step predecessors, for every \(n\ge1\). The maximum equals
\[
\max_{y\in\{0,1\}^n}|F_n^{-1}(y)|=1+T_n,
\]
where \(T_0=3\), \(T_1=T_2=1\), and \(T_{n+3}=T_{n+2}+T_n\). In particular, the maximum grows as \(\lambda^n+1+O(\lambda^{-n/2})\), where \(\lambda\in(1.46557,1.46558)\) is the positive root of \(t^3-t^2-1\). The uniqueness assertion, rather than the already-known homogeneous-preimage counting method, is the central result.

## Assumptions and scope
The ring is indexed (not quotiented by spatial rotations), neighborhoods have radius one, and predecessors are one-step predecessors. No claim concerns the infinite lattice, fixed boundary conditions, multi-step predecessor fibers, or other elementary rules.

## Proof
**1. Transfer representation and homogeneous count.** Use de Bruijn states \((00,01,10,11)\). The two output-symbol adjacency matrices are
\[
M_0=\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&1&0&0\\0&0&1&1\end{pmatrix},\quad
M_1=\begin{pmatrix}0&1&0&0\\0&0&1&0\\1&0&0&0\\0&0&0&0\end{pmatrix}.
\]
A cyclic predecessor is precisely a closed de Bruijn walk, so for every word \(y\),
\[
N(y):=|F_n^{-1}(y)|=\operatorname{tr}(M_{y_0}M_{y_1}\cdots M_{y_{n-1}}).
\]
The \(0\)-matrix is the direct sum of the scalar \(1\) and
\[
B=\begin{pmatrix}0&0&1\\1&0&0\\0&1&1\end{pmatrix},\qquad \det(tI-B)=t^3-t^2-1.
\]
Consequently \(N(0^n)=1+T_n\) with the stated integer recurrence, including \(n=1,2\). The other two eigenvalues of \(B\) are complex conjugates of modulus \(\lambda^{-1/2}\); hence
\[
N(0^n)\ge1+\lambda^n-2\lambda^{-n/2}>\lambda^n\quad(n\ge4),
\]
because \(\lambda^2>2\).

**2. Simultaneous singular-value bound.** Let \(D=\operatorname{diag}(1,\sqrt\lambda,\lambda^{-1/2},1)\) and \(A_j=D^{-1}M_jD\). Direct calculation of the Gram matrices gives the descending singular-value lists
\[
\sigma(A_0)=(\lambda,\lambda,1,\lambda^{-2}),\qquad
\sigma(A_1)=(\lambda^{1/2},\lambda^{1/2},\lambda^{-1},0).
\]
The standard matrix product trace inequality
\[
|\operatorname{tr}(X_1\cdots X_s)|\le\sum_{j=1}^4\prod_{i=1}^s\sigma_j(X_i)
\]
therefore shows that if \(y\) has exactly \(k\ge1\) ones,
\[
0\le N(y)\le 2\lambda^{n-k/2}+\lambda^{-k}.
\]
For \(k\ge4\), this is at most \(2\lambda^{n-2}+\lambda^{-4}<\lambda^n\), since \(\lambda^4-2\lambda^2-\lambda^{-4}>0\). This excludes all such nonzero outputs for every length.

**3. Sparse nonzero outputs on long rings.** Let \(v=(0,\sqrt\lambda,\sqrt\lambda,\lambda^2)^T\) and \(P=vv^T/(v^Tv)\). Then \(P\) is the orthogonal rank-one spectral projector for the Perron eigenvalue of \(A_0\), and \(S=A_0-\lambda P\) satisfies \(PS=SP=0\). For the nontrivial three-by-three block, straightforward exact multiplication and reduction modulo \(\lambda^3-\lambda^2-1=0\) give
\[
\begin{array}{c|c}
 m&\|S_B^m\|_F^2\\\hline
 3&3-\lambda^2\\
 4&3\lambda^2-8\lambda+6\\
 5&6\lambda^2-12\lambda+5
\end{array}
\]
and all three values lie strictly between zero and one. The remaining scalar block of \(S\) is \(1\). Every integer \(m\ge3\) is a sum of members of \(\{3,4,5\}\), so submultiplicativity implies \(\|S^m\|_2\le1\) for all \(m\ge3\).

If \(1\le k\le3\) and \(n\ge25\), some cyclic run of zeros has length \(m\ge8\) (there are \(n-k\) zeros in at most \(k\) runs). Cyclically rotate the trace to \(N(y)=\operatorname{tr}(A_0^m Q)\). The norm bound above yields
\[
\|Q\|_2\le \lambda^{n-m-k/2},\quad
N(y)=\operatorname{tr}((\lambda^mP+S^m)Q)
\le (\lambda^m+4)\|Q\|_2
\le\lambda^n\lambda^{-1/2}(1+4\lambda^{-8})<\lambda^n.
\]
The rank-one trace bound is \(|\operatorname{tr}(PQ)|\le\|Q\|_2\); the remainder follows from \(|\operatorname{tr}(S^mQ)|\le4\|S^m\|_2\|Q\|_2\). Every displayed strict scalar inequality follows from the rational enclosure \(146557/100000<\lambda<146558/100000\), verified without floating-point arithmetic by `proof_bounds.py`.

**4. Finite sparse boundary.** The only remaining cases have \(n\le24\) and \(1\le k\le3\). The `verify.py` integer transfer-matrix verifier examines **every** choice of the \(k\) one-positions: exactly 15,250 cases. In each case it computes the exact trace, compares it strictly with \(\operatorname{tr}(M_0^n)\), and passes. These four steps cover all lengths and all nonzero outputs, proving uniqueness.

## Verification
Run `python3 algebra_certificate.py`, `python3 proof_bounds.py`, `python3 verify.py`, and `python3 brute.py` from the extracted file directory. The first verifies exactly, in the cubic quotient field, the three residual Frobenius identities. The second checks all scalar inequalities using rational numbers. The third checks the complete finite sparse boundary \(n\le24\) (not random sampling). The fourth independently computes the global predecessor distribution from direct cyclic rule evaluation for \(1\le n\le14\). The latter finite experiment is a cross-check, not a substitute for the all-length argument. Their recorded outputs are reproduced in `VERIFICATION.md`.

## Relationship to prior work
McIntosh's June 24, 1993 Rule-22 discussion already gives the two de Bruijn matrices, their spectral interpretation, and a qualitative expectation that zero-rich configurations have many more ancestors. Powley and Stepney study homogeneous predecessor counts by trace formulas, thereby covering the **homogeneous count** but not the global comparison with all heterogeneous outputs. Jen develops predecessor recurrences and asymptotic extrema for sequences on infinite lattices rather than the exact cyclic all-target uniqueness problem. Gravner and Griffeath study Rule-22 evolution from finite seeds; Martínez and collaborators study its dynamics, diagrams, and basins. The new assertion is the uniform strict inequality against *every* nonzero cyclic target, including arbitrarily sparse and dense targets. It does not present transfer matrices or the homogeneous recurrence as new.

## Limitations
The result concerns one update on finite indexed binary rings only. The scalar estimates are sufficient, not sharp, for heterogeneous words. The proof is constructive and finite-sparse verification is exhaustive, but no independently performed scientific or historical-priority audit is asserted. Earlier unindexed results or implicit corollaries of a general norm theorem remain a historical-priority risk.

## References
1. H. V. McIntosh, “ancestors (3),” posting dated June 24, 1993, https://groups.google.com/g/comp.theory.cell-automata/c/fV-VsEEvq80 and expanded commentary https://delta.cs.cinvestav.mx/~mcintosh/oldweb/wandl/node6.html.
2. E. J. Powley and S. Stepney, “Counting preimages of homogeneous configurations in 1-dimensional cellular automata,” https://www-users.york.ac.uk/~ss44/bib/ss/nonstd/jca11.pdf.
3. E. Jen, “Scaling of Preimages in Cellular Automata,” *Complex Systems* 1 (1987), 1045–1062, https://content.wolfram.com/sites/13/2018/02/01-6-2.pdf.
4. J. Gravner and D. Griffeath, “The one-dimensional Exactly 1 cellular automaton: replication, periodicity, and chaos from finite seeds,” https://www.math.ucdavis.edu/~gravner/papers/ex1.pdf.
5. G. J. Martínez et al., “On Patterns and Dynamics of Rule 22 Cellular Automaton,” *Complex Systems* 28 (2019), 125–173, https://content.wolfram.com/uploads/sites/13/2019/06/28-2-1.pdf.
