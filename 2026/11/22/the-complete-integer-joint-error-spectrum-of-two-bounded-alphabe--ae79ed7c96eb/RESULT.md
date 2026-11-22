# The complete integer joint-error spectrum of two bounded-alphabet functional dependencies

## Finding

Let \(n,b,c\geq1\). Consider any nonempty finite team \(T\) of \(n\) distinct assignments, with variables \(x,y,z\), in which \(y\) has at most \(b\) possible values and \(z\) has at most \(c\) possible values. For a functional dependency \(u\to v\), let \(\delta_T(u\to v)\) be the minimum number of assignments one must delete to make it true. Write
\[
p=\delta_T(x\to y),\qquad q=\delta_T(x\to z),\qquad r=\delta_T(x\to(y,z)).
\]
Then necessarily
\[
0\leq p\leq n-\left\lceil\frac n b\right\rceil,\qquad
0\leq q\leq n-\left\lceil\frac n c\right\rceil,
\]
and the *complete* range for the joint error at those fixed marginal errors is every integer in
\[
\boxed{\max\{p,q\}\leq r\leq n-m_0,\quad
m_0=\max\left\{n-p-q,\left\lceil\frac{n-p}{c}\right\rceil,
\left\lceil\frac{n-q}{b}\right\rceil,\left\lceil\frac{n}{bc}\right\rceil\right\}.}
\]
Precisely: (i) every team with the stated alphabet bounds obeys these inequalities; (ii) for every admissible integer quadruple \((n,b,c,p,q)\) and every integer \(r\) in the displayed interval there is a team attaining exactly \((p,q,r)\). The latter team can use a constant \(x\) and one auxiliary unconstrained identifier attribute to keep its \(n\) assignments distinct. This is an exact integer-spectrum theorem, not merely an asymptotic estimate.

Thus on an \(n\)-row team, assumptions of approximate dependence \(\mathord{=}_{p/n}(x,y)\) and \(\mathord{=}_{q/n}(x,z)\) imply the sharp alphabet-sensitive conclusion \(\mathord{=}_{(n-m_0)/n}(x,yz)\), with the displayed integer parameters understood as upper bounds (and clipped to their maximal feasible errors). For \(n=20\), \(b=2\), \(c=3\), \(p=8\), and \(q=12\), the attainable joint errors are *exactly* \(12,13,14,15,16\): the ordinary union-of-deletions bound gives only \(r\leq20\).

## Assumptions and scope

A team is a finite **set** of assignments (not a multiset). The determinant \(x\) may be a tuple of variables, while the two outputs \(y,z\) are individual variables with bounded alphabets. The value of \(x\) may vary across the team. The auxiliary identifier attribute in the existence statement is not part of any dependency, and permits repeated \((x,y,z)\)-patterns as distinct assignments, without violating set semantics. All variables take values in a sufficiently large common universe; the named finite output alphabets may be disjoint or overlapping. Empty fibres are ignored. No restriction on the identifier alphabet is assumed. The conclusion concerns exact minimum **numbers** of deleted assignments, not the number of disagreeing pairs.

## Proof

**Step 1 (fibre formula).** Partition \(T\) into nonempty fibres of constant \(x\). For one fibre of size \(s\), let \(a_{ij}\) be the count of assignments with \(y=i,z=j\), after including zero rows/columns to obtain a \(b\)-by-\(c\) matrix. If its largest row sum is \(A\), largest column sum is \(B\), and largest cell is \(M\), the three deletion counts in that fibre are respectively \(s-A,s-B,s-M\). The global deletion counts are sums over fibres because values of \(x\) partition the constraints. In particular, the individual errors do not exceed \(n-\lceil n/b\rceil\) and \(n-\lceil n/c\rceil\).

**Step 2 (four necessary cell bounds).** In each fibre, the intersection of a largest row and a largest column has at least \(A+B-s\) assignments. Also a row of size \(A\) uses at most \(c\) cells, a column of size \(B\) uses at most \(b\), and the entire matrix uses at most \(bc\). Consequently
\[
M\geq A+B-s,\qquad cM\geq A,\qquad bM\geq B,\qquad bcM\geq s.
\]
Summing these inequalities across fibres shows that the total number of kept assignments for the joint dependency, \(n-r\), is at least \(n-p-q\), \((n-p)/c\), \((n-q)/b\), and \(n/(bc)\). Since \(n-r\) is integral, it is at least \(m_0\). Projection of the joint output yields \(r\geq\max\{p,q\}\).

**Step 3 (all integer values occur).** Put \(A=n-p\), \(B=n-q\), and let \(m\) be any integer satisfying
\[
m_0\leq m\leq\min\{A,B\}.
\]
We construct a nonnegative integer \(b\)-by-\(c\) matrix of total sum \(n\), with largest row sum exactly \(A\), largest column sum exactly \(B\), and largest entry exactly \(m\).

If \(b=1\) or \(c=1\), the errors along the singleton-alphabet coordinate are zero, and an arbitrary distribution of \(n\) units into the other alphabet, with a prescribed largest cell, settles the statement (the formula forces \(m=\min\{A,B\}\)). Now assume \(b,c\geq2\). Mark one row, one column and their intersection. The real matrix with four constant blocks is
\[
a_{11}=m,\quad
 a_{1j}=\frac{A-m}{c-1}\ (j>1),\quad
 a_{i1}=\frac{B-m}{b-1}\ (i>1),\quad
 a_{ij}=\frac{n-A-B+m}{(b-1)(c-1)}\ (i,j>1).
\]
Every entry is nonnegative, by \(m\leq A,B\) and \(m\geq A+B-n\). Every entry is at most \(m\): for the off-diagonal blocks use \(A\leq cm\) and \(B\leq bm\). For the lower-right block, note that \(A\geq n/b\), \(B\geq n/c\), and \(bc-b-c\geq0\), hence
\[
n-A-B\leq\frac{(bc-b-c)n}{bc}\leq(bc-b-c)m.
\]
The marked row sums to \(A\) and the marked column sums to \(B\). Every unmarked row sums to \((n-A)/(b-1)\leq A\), and every unmarked column sums to \((n-B)/(c-1)\leq B\), by the assumed admissibility of \(p,q\).

This real matrix is a feasible fractional circulation in a directed bipartite flow network: arcs source-to-row have integral capacity \(A\), with the marked row constrained to carry exactly \(A\); row-to-column arcs have integral capacity \(m\), with the marked cell constrained to carry exactly \(m\); column-to-sink arcs have integral capacity \(B\), with the marked column constrained to carry exactly \(B\); and the return arc sink-to-source carries exactly \(n\). All bounds are integers. The integral-circulation theorem (or total unimodularity of a directed incidence matrix with lower and upper integral arc bounds) supplies an *integral* feasible circulation. Its row-column arc flows form the required integer matrix. The marked row, column and cell attain their respective upper bounds, so their maxima are exactly \(A,B,m\). Assign unique identifier values to the \(n\) entries counted by this matrix and let \(x\) be constant. The resulting team has joint error \(n-m\). As \(m\) runs through every integer from \(m_0\) to \(\min\{A,B\}\), the joint error runs through every claimed integer, proving both sharpness and absence of gaps.

**Step 4 (example).** For the parameters \((n,b,c,p,q)=(20,2,3,8,12)\), the matrices
\[
\begin{pmatrix}8&2&2\\0&4&4\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}4&4&4\\4&2&2\end{pmatrix}
\]
have largest row sum \(12\), largest column sum \(8\), and largest cell \(8\) and \(4\) respectively. The integral-circulation argument supplies the three intervening cell maxima as well.

## Verification

The accompanying standalone \(\texttt{verify.py}\) enumerates all nonnegative tables of chosen small sizes (339,613 total), checks the entire attained spectrum at each marginal-error pair, builds 3,373 integral circulation witnesses at independently sampled parameters up to seven-by-seven alphabets and forty rows, and checks 9,984 randomly constructed multi-fibre teams. Its observed output is:

```
VERIFY_OK exhaustive_tables=339613 constructed_instances=3373 multi_fiber_tests=9984
```

These finite computations stress-test the normalization, integer cutoffs, and integrality construction; they do not replace the unbounded proof above.

## Relationship to prior work

Fröhlich, Häggblom, Hirvonen and Hirvonen (2026) study approximate dependence as deletion distance in team semantics, and emphasize that the errors of joint outputs can interact in ways not captured by elementary inference rules. They give an example of a missing general rule and analyze unary entailment and model checking. The present result instead determines the **entire feasible integer spectrum** for two single bounded-alphabet outputs and arbitrary determinant fibres. The unrestricted rule obtained by a union of deletion sets gives \(r\leq p+q\), while the bounded-alphabet region can be strictly smaller.

Classical Fréchet-type bounds constrain the intersection of a selected modal row and column; the additional pigeonhole and integral transportation argument determine every possible modal **cell** count. Work on integer contingency tables with prescribed full margins gives general enumeration tools, but does not itself state this joint-error spectrum in terms of only the two marginal deletion errors. These comparisons establish mathematical distinction in the materials inspected; they do not establish exhaustive historical novelty.

## Limitations

The existence direction permits an auxiliary identifier attribute; without it, at most \(bc\) distinct assignments can occupy one constant-\(x\) fibre, so the realization assertion may fail. The theorem covers two output attributes and *deletion* error, not weighted repairs, three or more outputs, independent deletion sets required to serve all dependencies simultaneously, or arbitrary approximate-formula combinations. It does not claim a new axiomatisation of approximate dependence. A previous equivalent contingency-table result under different terminology remains possible.

## References

1. N. Fröhlich, M. Häggblom, Å. Hirvonen, M. Hirvonen, *Approximate Functional Dependencies—Implication Problem Revisited*, arXiv:2608.16570, first submitted 2026-08-17. https://arxiv.org/html/2608.16570
2. J. W. Miller and M. T. Harrison, *Exact Enumeration and Sampling of Matrices with Specified Margins*, arXiv:1104.0323, 2011. https://arxiv.org/abs/1104.0323
3. M. Al-atar and A. Sali, *Approximate Keys and Functional Dependencies in Incomplete Databases With Limited Domains—Algorithmic Perspective*, arXiv:2402.05161, 2024. https://arxiv.org/abs/2402.05161
4. Integral feasible circulation theorem / total unimodularity of directed network incidence matrices (classical integral network-flow theorem).
