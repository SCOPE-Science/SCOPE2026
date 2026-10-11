# Degree distribution of prescribed-commutator graphs of two-by-two matrix rings

## Finding

Let
\[
R=M_2(\mathbf F_q)
\]
for a prime power \(q\), and let \(\Gamma_R^r\) be the simple graph with vertex set \(R\) in which distinct matrices \(x,y\) are adjacent exactly when
\[
[x,y]\ne r
\qquad\text{and}\qquad
[x,y]\ne-r.
\]

The complete degree distribution is as follows.

If
\[
r=0,
\]
then the \(q\) scalar matrices have degree
\[
0,
\]
and every one of the remaining
\[
q^4-q
\]
matrices has degree
\[
q^4-q^2.
\]

If
\[
\operatorname{tr}(r)\ne0,
\]
then
\[
\boxed{\Gamma_R^r\cong K_{q^4}.}
\]
Thus degree
\[
q^4-1
\]
occurs \(q^4\) times.

Finally suppose
\[
r\ne0
\qquad\text{and}\qquad
\operatorname{tr}(r)=0.
\]
Exactly
\[
q^3-q
\]
vertices \(x\) satisfy
\[
r\in[x,R].
\]
For every such vertex,
\[
|C_R(x)|=q^2.
\]

If the characteristic is \(2\), then
\[
\boxed{\deg(x)=q^4-q^2-1}
\]
for those \(q^3-q\) vertices, while the other
\[
q^4-q^3+q
\]
vertices have degree
\[
q^4-1.
\]

If the characteristic is odd, then
\[
\boxed{\deg(x)=q^4-2q^2-1}
\]
for those \(q^3-q\) vertices, while the other
\[
q^4-q^3+q
\]
vertices again have degree
\[
q^4-1.
\]

Thus every nonzero traceless parameter \(r\) gives exactly the same degree multiset, independently of the similarity type of \(r\). In characteristic \(2\), this uniform class includes nonzero scalar matrices, since a scalar matrix can have trace zero and can occur as an additive commutator.

The structural criterion behind the distribution is
\[
\boxed{r\in[x,R]\iff\operatorname{tr}(rx)=0}
\]
for every nonscalar \(x\) whenever
\[
\operatorname{tr}(r)=0.
\]

## Assumptions and scope

The graph convention is the one introduced for finite rings by Nath, Sharma, Dutta, and Shang: the vertex set is all of \(R\), and distinct \(x,y\) are adjacent exactly when their additive commutator is neither \(r\) nor \(-r\).

The result concerns \(2\times2\) full matrix rings over finite fields. It determines the complete degree multiset, not the full graph isomorphism type for different nonzero traceless parameters.

The distinction between characteristic \(2\) and odd characteristic is necessary because
\[
r=-r
\]
for every \(r\) in characteristic \(2\).

## Proof

Use the nondegenerate trace pairing
\[
\langle u,v\rangle=\operatorname{tr}(uv)
\]
on
\[
M_2(\mathbf F_q).
\]
Nondegeneracy follows from the matrix units, since a nonzero entry of one matrix is detected by a transposed matrix unit.

Fix \(x\in R\). The image of the linear map
\[
\operatorname{ad}_x:R\to R,
\qquad
y\mapsto[x,y],
\]
is orthogonal to \(C_R(x)\). Indeed, if \(z\in C_R(x)\), then cyclicity of trace gives
\[
\operatorname{tr}([x,y]z)
=
\operatorname{tr}(y(zx-xz))
=0.
\]

If \(x\) is nonscalar, then its minimal polynomial has degree \(2\), so
\[
C_R(x)=\mathbf F_q[x]=\operatorname{span}_{\mathbf F_q}\{I,x\}.
\]
Hence
\[
\dim C_R(x)=2.
\]
Rank-nullity gives
\[
\dim[x,R]=2,
\]
while
\[
\dim C_R(x)^\perp=2.
\]
Therefore
\[
[x,R]=C_R(x)^\perp.
\]

Now let \(r\) be traceless. For nonscalar \(x\), membership \(r\in[x,R]\) is equivalent to orthogonality against both generators of the centralizer:
\[
\operatorname{tr}(rI)=0,
\qquad
\operatorname{tr}(rx)=0.
\]
The first equation already holds, so
\[
r\in[x,R]
\iff
\operatorname{tr}(rx)=0.
\]

Suppose next that \(r\ne0\). Because the trace pairing is nondegenerate, the functional
\[
x\longmapsto\operatorname{tr}(rx)
\]
is nonzero. Its kernel is therefore a \(3\)-dimensional hyperplane containing exactly
\[
q^3
\]
matrices. If \(r\) is traceless, every scalar matrix lies in this hyperplane. There are \(q\) scalar matrices, and none can satisfy \(r\in[x,R]\) because \([x,R]=0\) for scalar \(x\). Thus exactly
\[
q^3-q
\]
matrices satisfy \(r\in[x,R]\).

For each such nonscalar \(x\), the generalized centralizer
\[
T_{x,r}=\{y:[x,y]=r\}
\]
is a nonempty affine coset of \(C_R(x)\). Therefore
\[
|T_{x,r}|=q^2.
\]

If the characteristic is \(2\), then \(r=-r\), and the general degree formula gives
\[
\deg(x)=q^4-q^2-1
\]
when \(T_{x,r}\ne\varnothing\), and \(q^4-1\) otherwise.

If the characteristic is odd, then \(r\ne-r\) for nonzero \(r\), and the two affine fibers
\[
T_{x,r},\qquad T_{x,-r}
\]
are disjoint. Hence
\[
\deg(x)=q^4-2q^2-1
\]
when \(T_{x,r}\ne\varnothing\), and \(q^4-1\) otherwise.

If \(r=0\), the general degree formula reduces to
\[
\deg(x)=|R|-|C_R(x)|.
\]
Scalar matrices have centralizer \(R\), while every nonscalar matrix has centralizer size \(q^2\), proving the first case.

Finally, every additive commutator has trace zero. Therefore if
\[
\operatorname{tr}(r)\ne0,
\]
neither \(r\) nor \(-r\) can occur as a commutator, so every pair of distinct vertices is adjacent and the graph is complete.

## Verification

The included checker independently enumerates all matrices and all ordered commutator fibers over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_4,\quad\mathbf F_5.
\]
The field \(\mathbf F_4\) is implemented as
\[
\mathbf F_2[t]/(t^2+t+1).
\]

For each field it tests \(r=0\), a nonzero traceless nilpotent matrix, and a matrix of nonzero trace. It additionally tests a nonzero scalar traceless parameter in characteristic \(2\), and a split semisimple traceless parameter in odd characteristic.

For every parameter, the checker constructs the full degree histogram directly from the commutator definition and verifies exact agreement with the formulas above. It separately checks
\[
r\in[x,R]
\iff
\operatorname{tr}(rx)=0
\]
for every nonscalar \(x\) and every tested nonzero traceless \(r\).

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Nath, Sharma, Dutta, and Shang introduced the \(r\)-noncommuting graph of a finite ring and proved the general degree formula in terms of the generalized centralizer
\[
T_{x,r}=\{y:[x,y]=r\}.
\]
Their paper treats structural graph properties, isoclinism, and low-degree restrictions. The inspected full text does not specialize the generalized-centralizer fibers to full matrix rings and does not give the degree distribution for
\[
M_2(\mathbf F_q).
\]

Earlier work of Abdollahi studies ordinary commuting graphs of full matrix rings over finite fields and proves ring-recognition results from those graphs. That work concerns ordinary commutation, corresponding to the \(r=0\) background after deleting central vertices, rather than prescribed nonzero commutator fibers.

The new step is the trace-duality calculation
\[
[x,R]=C_R(x)^\perp
\]
for nonscalar \(2\times2\) matrices, which turns generalized-centralizer existence into the single linear equation
\[
\operatorname{tr}(rx)=0.
\]
This yields the complete degree distribution uniformly for every parameter \(r\).

Targeted searches for \(r\)-noncommuting graphs of matrix rings, generalized centralizers in \(M_2(\mathbf F_q)\), traceless commutator fibers, and exact degree distributions did not locate this result.

## Limitations

The theorem determines only the degree multiset. It does not assert that all nonzero traceless parameters produce isomorphic graphs.

For matrix size greater than \(2\), centralizer dimensions vary among many similarity types, so the same two-degree collapse does not persist without further analysis.

The identity
\[
[x,R]=C_R(x)^\perp
\]
is standard trace-duality for matrix algebras. The originality claim is the use of this identity to solve the generalized-centralizer count and obtain the complete \(r\)-noncommuting degree distribution for \(M_2(\mathbf F_q)\).

A residual bibliographic risk is that an equivalent prescribed-commutator count appears in older linear-algebra literature without graph terminology.

Failed searches do not prove novelty.

## References

1. R. K. Nath, M. Sharma, P. Dutta, and Y. Shang, “On \(r\)-noncommuting graph of finite rings,” arXiv:1907.10350v1, first public version 24 July 2019; *Axioms* 10 (2021), article 233, DOI 10.3390/axioms10030233. Classification includes 16U70.
2. A. Abdollahi, “Commuting graphs of full matrix rings over finite fields,” *Linear Algebra and its Applications* 428 (2008), 2947–2954, DOI 10.1016/j.laa.2008.01.036.
3. J. Dutta, D. K. Basnet, and R. K. Nath, “On generalized non-commuting graph of a finite ring,” *Algebra Colloquium* 25 (2018), 149–160, DOI 10.1142/S100538671800010X.
