# Three-stratum Lie-bracket fibers and adjoint ranks of strictly upper triangular four-by-four matrices

## Finding

Let \(k=\mathbb F_q\) be any finite field, and let \(L=\mathfrak n_4(k)\) be the six-dimensional Lie algebra of strictly upper triangular \(4\times4\) matrices with ordinary matrix commutator. Its derived ideal is \([L,L]=kE_{13}\oplus kE_{24}\oplus kE_{14}\). For \(u,v,w\in k\), define the prescribed Lie-bracket fiber
\[
F_q(u,v,w)=\#\{(X,Y)\in L^2:[X,Y]=uE_{13}+vE_{24}+wE_{14}\}.
\]
Then, for every prime power \(q\), with no characteristic restriction,
\[
F_q(u,v,w)=\begin{cases}
2q^9+q^8-2q^7,&u=v=w=0,\\
2q^7(q^2-1),&u=v=0,\ w\ne0,\\
q^7(q^2-1),&(u,v)\ne(0,0).
\end{cases}
\]
All targets in \([L,L]\) have positive fibers and every target outside \([L,L]\) has no witnesses. In particular, every nonzero central target has exactly twice the number of witnesses of every noncentral target.

Moreover, the ranks of the linear maps \(\operatorname{ad}_X:Y\mapsto[X,Y]\), for \(X\in L\), have the complete distribution
\[
\begin{array}{c|cccc}
\operatorname{rank}(\operatorname{ad}_X)&0&1&2&3\\\hline
\#\{X\}&q&q(q^2-1)&q^3(q^2+q-2)&q^3(q-1)(q^2-1).
\end{array}
\]
The element commuting probability is therefore
\[
\Pr_{X,Y\in L}([X,Y]=0)=2q^{-3}+q^{-4}-2q^{-5}.
\]

## Assumptions and scope

All ordered pairs are counted with multiplicity, including identical matrices and zero matrices. Matrix entries lie in the finite field \(k\), not necessarily a prime field. The characteristic can equal two. \(E_{ij}\) is the elementary matrix with one at position \((i,j)\) and zeros elsewhere. A target with coordinates outside the derived ideal is not a Lie bracket, hence has fiber zero. The proposition concerns the *Lie-algebra bracket* \(XY-YX\), not the multiplicative commutator of the associated unitriangular group.

## Proof

Write
\[
X=aE_{12}+bE_{13}+cE_{14}+dE_{23}+eE_{24}+fE_{34},
\quad
Y=a'E_{12}+b'E_{13}+c'E_{14}+d'E_{23}+e'E_{24}+f'E_{34}.
\]
A direct multiplication of elementary matrices yields
\[
[X,Y]=(ad'-da')E_{13}+(df'-fd')E_{24}+
(ae'-ea'+bf'-fb')E_{14}.
\tag{1}
\]
There is no dependence on the two central entries \(c,c'\); their choices multiply all fiber sizes by \(q^2\).

Fix \((u,v)\). First count \(M(u,v)\), the number of six-tuples \((a,a',d,d',f,f')\) satisfying the first two equations of (1). If \((d,d')\ne(0,0)\), each of the equations \(ad'-da'=u\) and \(df'-fd'=v\) is a nonzero linear functional on two variables and hence has exactly \(q\) solutions. This contributes \(q^2(q^2-1)\) tuples. For \((d,d')=(0,0)\), both left sides vanish; if \(u=v=0\) there are \(q^4\) additional tuples. Consequently,
\[
M(u,v)=q^2(q^2-1)+q^4\mathbf 1_{\{u=v=0\}}.
\tag{2}
\]
For a fixed tuple counted by \(M\), the third equation in (1) is a linear equation in \((b,e,b',e')\). Its coefficient vector is zero precisely when \(a=a'=f=f'=0\). Otherwise it has exactly \(q^3\) solutions, for every prescribed \(w\). The degenerate first-level tuples are precisely the \(q^2\) possibilities for \((d,d')\), available only when \(u=v=0\). For each such tuple there are \(q^4\) solutions if \(w=0\), and none otherwise. Multiplying by the central freedom \(q^2\), we obtain
\[
F_q(u,v,w)=q^5M(u,v)-q^7\mathbf 1_{\{u=v=0\}}
+q^8\mathbf 1_{\{u=v=w=0\}}.
\tag{3}
\]
Substitution of (2) into (3) yields the three stated formulas. Each is positive in its claimed case. The numbers of targets of the three classes are \(1\), \(q-1\), and \(q(q^2-1)\), respectively; their weighted fiber total is
\[
(2q^9+q^8-2q^7)+(q-1)2q^7(q^2-1)
+q(q^2-1)q^7(q^2-1)=q^{12},
\]
which equals \(|L|^2\).

For the adjoint-rank distribution, (1) as a function of the primed variables has output coefficient matrix
\[
\left(\begin{array}{rrrrr}
-d&0&a&0&0\\
0&0&-f&0&d\\
-e&-f&0&a&b
\end{array}\right)
\tag{4}
\]
with columns corresponding to \(a',b',d',e',f'\). When \(d=a=f=0\), its rank is zero if \(b=e=0\) and one otherwise. If \(d=0\) and \((a,f)\ne(0,0)\), the rank is two; if \(d\ne0\) and \(a=f=0\), the rank is also two; and if \(d\ne0\) and \((a,f)\ne(0,0)\), it is three. The unused coordinate \(c\) contributes a factor \(q\). Counting the allowed \((a,b,c,d,e,f)\) gives the four displayed adjoint populations. They sum to \(q^6\), and also reproduce
\[
F_q(0,0,0)=\sum_{X\in L}q^{6-\operatorname{rank}\operatorname{ad}_X}.
\]
Dividing this by \(q^{12}\) yields the commuting probability. This completes the proof in every characteristic.

## Verification

The standalone script `verify.py` uses literal finite-field multiplication of the original \(4\times4\) matrices to enumerate all \(q^{12}\) ordered input pairs for \(q=2,3\). It independently computes the ranks of every adjoint matrix by Gaussian elimination for \(q=2,3,4,5\); for \(q=4\) it implements the extension field \(\mathbb F_2[t]/(t^2+t+1)\). For \(q=4,5\), it also tests 50,000 reproducible randomly chosen ordered pairs and validates the complete mass identity. Output from this execution is included in `verification-output.txt`.

Finite enumeration is corroboration only; equations (1)–(4) give the proof for all prime powers.

## Relationship to prior work

Yan's *Representations of Finite Unipotent Linear Groups by the Method of Clusters* (arXiv:1004.2674, first publicly posted 2010-04-15) studies the corresponding finite unitriangular groups, their adjoint/coadjoint clusters, and character constructions. Those orbit and representation results are not a prescribed Lie-bracket fiber census. Kumar and Prajapati's *Maximal Non-commuting Sets in Certain Unipotent Upper-Triangular Linear Groups* (arXiv:1601.04133, first posted 2016-01-16) studies maximal pairwise noncommuting sets in the unitriangular *group*, rather than counts for each target of the *Lie-algebra* commutator. Ghimire and Huang's *Derivations of the Lie algebra of strictly block upper triangular matrices* (arXiv:1603.08044, first posted 2016-03-25) gives structural descriptions of derivations of a class containing \(L\), without enumerating the prescribed-bracket fibers above.

The novelty assessed here is only the exact three-stratum target-fiber law together with the complete adjoint-rank distribution for \(\mathfrak n_4(k)\), not any general existence, representation, derivation, centralizer, or commuting theory. An unlocated broader theorem could in principle imply this elementary finite-field enumeration; historical priority is not independently certified.

## Limitations

The result does not determine fibers in higher strictly upper triangular Lie algebras, does not describe multiplicative group commutators, and does not classify witness pairs up to conjugacy. The finite-field computations are not a proof for all fields, and neither exhaustive historical priority nor independent mathematical audit has been performed.

## References

1. Ning Yan, *Representations of Finite Unipotent Linear Groups by the Method of Clusters*, arXiv:1004.2674 (initial public posting 2010-04-15), https://arxiv.org/abs/1004.2674 .
2. C. P. Anil Kumar and S. K. Prajapati, *Maximal Non-commuting Sets in Certain Unipotent Upper-Triangular Linear Groups*, arXiv:1601.04133 (initial public posting 2016-01-16), https://arxiv.org/abs/1601.04133 .
3. Prakash Ghimire and Huajun Huang, *Derivations of the Lie algebra of strictly block upper triangular matrices*, arXiv:1603.08044 (initial public posting 2016-03-25), https://arxiv.org/abs/1603.08044 .
