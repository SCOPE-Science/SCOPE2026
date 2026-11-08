# Dyadic transient strata on Mersenne-height parity cylinders

## Finding

For any integer \(r\ge2\), set \(q=2^r\) and \(m=q-1\). On the simple cylindrical grid \(G=P_m\square C_n\), \(n\ge3\), work over any finite field \(\mathbb F_Q\) with characteristic two. Let \(B\) be the open-neighbor sum operator: \((Bx)_v=\sum_{w\sim v}x_w\). Define \(h=2^{\nu_2(n)}\). Its complete zero-eigenvalue primary summand has the following Jordan blocks, with zero multiplicities suppressed:

\[
\mathcal J_0(B)=\begin{cases}
J_{q-1}(0),&h=1,\\
J_q(0)^{\oplus 2(k-1)}\oplus J_{q-k}(0)^{\oplus2},&h=2k,\ k<q,\\
J_k(0)^{\oplus2(q-1)},&h=2k,\ k\ge q.
\end{cases}
\]

The complementary invariant summand, of dimension \((q-1)(n-h)\), is invertible. For each nonnegative integer \(t\), define

\[
K(t)=\begin{cases}
\min(t,q-1),&h=1,\\
2(k-1)\min(t,q)+2\min(t,q-k),&h=2k,\ k<q,\\
2(q-1)\min(t,k),&h=2k,\ k\ge q.
\end{cases}
\]

If \(T(x)\) is the least nonnegative number of updates after which the trajectory of \(x\) lies on a periodic orbit, then

\[
\#\{x:T(x)\le t\}=Q^{(q-1)(n-h)+K(t)},\qquad
\#\{x:T(x)=t\}=\#\{T\le t\}-\#\{T\le t-1\}\quad(t\ge1).
\]

In particular, \(\#\{T=0\}=Q^{(q-1)(n-h)}\). The sharp upper entry time is \(q-1\) for \(h\in\{1,2\}\), is \(q\) for \(4\le h<2q\), and is \(h/2\) for \(h\ge2q\). The entire operator is nilpotent exactly when \(n\) is a power of two. Thus an infinite sequence of cylinders exhibits an arithmetic transition between a constant transient plateau and circumference-proportional settling.

## Assumptions and scope

The path \(P_m\) has vertices \(0,\ldots,m-1\) with edges between consecutive vertices; the cycle \(C_n\) has vertices modulo \(n\) with edges \(j\sim j\pm1\). All grids are simple, with no self-loops and with the two cycle neighbors distinct because \(n\ge3\). Their Cartesian product has \(mn\) labelled sites. Boundary vertices have the neighbors supplied by the graph, not fictitious exterior or self neighbors. The symbol \(Q\) denotes field cardinality, while \(q=2^r\) is an integer determining the number of rows. The nilpotent decomposition is a statement over \(\mathbb F_Q\) itself, not merely after extending scalars.

## Proof

**Path factor.** Write \(D_j(X)=\det(XI-A_{P_j})\) in characteristic two. The path recurrence reads \(D_0=1\), \(D_1=X\), and \(D_j=XD_{j-1}+D_{j-2}\). With a formal invertible symbol \(z\) and \(X=z+z^{-1}\), the recurrence gives \(D_j(X)=(z^{j+1}+z^{-(j+1)})/(z+z^{-1})\). At \(j=q-1\), Frobenius yields \(z^q+z^{-q}=(z+z^{-1})^q\), so \(D_{q-1}(X)=X^{q-1}\). The path adjacency has one-dimensional kernel (the even-index coordinates vanish and all odd-index coordinates agree), hence, being entirely nilpotent and having one Jordan block, it is similar to \(J_{q-1}(0)\). This height is canonical rather than an arbitrary slice: for any open path, the same Laurent-polynomial identity implies that its adjacency is nilpotent only if every interior binomial coefficient of the relevant power vanishes modulo two. By the binary binomial criterion, this occurs precisely when the number of vertices plus one is a power of two. Thus the Mersenne-height paths are exactly the nontrivial nilpotent open paths in characteristic two.

**Cycle factor.** The cycle adjacency is multiplication by \(z+z^{-1}\) on \(\mathbb F_Q[z,z^{-1}]/(z^n-1)\). Write \(n=hu\) with \(u\) odd. Over an algebraic closure, \(z^n-1=(z^u-1)^h\), whose distinct odd-order roots give local components of dimension \(h\). The multiplier \(z+z^{-1}\) vanishes only at \(z=1\). At every other root it is a unit, and adding the commuting nilpotent path operator leaves it invertible. Therefore the zero-primary subspace has dimension \((q-1)h\), and the complementary invertible dimension is \((q-1)(n-h)\). These dimensions and the zero-primary blocks descend to \(\mathbb F_Q\), since the root \(1\) and its primary ring are already defined over that field.

**Local reduction.** Set \(s=z+1\) at the zero root and write \(a\) for the path nilpotent coordinate. The zero-primary space is the algebra \(R=\mathbb F_Q[a,s]/(a^{q-1},s^h)\), and the update is multiplication by \(a+s^2/(1+s)\). Multiplying this element by the unit \(1+s\) does not alter the kernels of any of its powers. The coordinate change \(a\mapsto(1+s)a\) is an automorphism of \(R\). Consequently the desired nilpotent Jordan blocks equal those of multiplication by \(a+s^2\). If \(h=1\) this is one \(J_{q-1}(0)\). If \(h=2k\), splitting the even and odd powers of \(s\) gives two invariant copies of \(\mathbb F_Q[a,w]/(a^{q-1},w^k)\), on each of which the operator is multiplication by \(v=a+w\). Here \(k\) is a power of two.

**Two-power truncated-algebra lemma.** On \(S=\mathbb F_Q[a,w]/(a^{q-1},w^k)\), the dimension of \(S/vS\) equals \(\min(q-1,k)\). If \(k\ge q\), the Frobenius identity \(v^k=a^k+w^k=0\) shows that all nilpotent Jordan blocks have length at most \(k\). There are \(q-1\) blocks whose total size is \((q-1)k\), forcing all to have size \(k\).

If \(k<q\), similarly \(v^q=0\) and there are \(k\) blocks. Since every binomial coefficient in \((a+w)^{q-1}\) is odd, reduction modulo \(a^{q-1}\) and \(w^k\) gives

\[
v^{q-1}=\sum_{j=q-k}^{q-2}a^j w^{q-1-j}.
\]

Every vector in the image of multiplication by \(v^{q-1}\) is a linear combination of \(v^{q-1}w^i\), because multiplying by \(a=v+w\) is equivalent to multiplying by \(w\) after multiplication by \(v^{q-1}\). Exactly the \(k-1\) vectors with \(0\le i\le k-2\) are nonzero and independent: their coefficients of \(a^{q-2}w^{i+1}\) distinguish them. Thus \(\operatorname{rank}v^{q-1}=k-1\), so exactly \(k-1\) blocks have length \(q\). The remaining one has length \((q-1)k-(k-1)q=q-k\). This includes \(k=1\), for which the displayed sum is empty and the remaining block has length \(q-1\). Taking two copies proves the three Jordan cases.

**Entry populations.** Over a finite field, the Fitting decomposition is the direct sum of the zero-primary nilpotent subspace and the invertible recurrent subspace. A state first reaches periodic behavior by time \(t\) exactly when its nilpotent component belongs to \(\ker B^t\). The latter has dimension \(K(t)\) from the blocks just derived. Hence the cumulative count is \(Q^{(q-1)(n-h)+K(t)}\). Differences give exact first-entry populations, and the maximum Jordan length gives the sharp entry time. A nonzero invertible summand remains exactly when the odd factor \(u\) of \(n\) exceeds one, proving the extinction criterion.

## Verification

Three standalone Python 3 standard-library checks accompany the result: `check_grid_ranks.py` constructs the labelled grid adjacency matrix directly and compares the nullity of every update power against the theorem for 128 parameter choices (1,606 comparisons); `check_local_algebra.py` independently computes powers in the truncated two-variable quotient for 23 parameter pairs (462 comparisons); `check_census.py` exhaustively enumerates 299,520 labelled binary states on the small three-row cylinders of circumferences 3 through 6 and matches every entrance-time cumulative population. Run each with `python3 <file>` from a directory containing the named file; captured stdout files are provided. These finite checks corroborate the algebraic proof but are not used to infer the infinite assertion.

## Relationship to prior work

Wolfram (1983) and Martin, Odlyzko and Wolfram (1984) developed additive cellular-automaton methods, including finite state-transition graphs and higher-dimensional periodic lattices; their framework is used here and is not claimed as new. Norman (1995, 2008) developed general modular Jordan-sum and tensor-product theory; the truncated-algebra lemma here is a special case of that broader subject, and no generic Jordan-sum method is claimed as new. The present scoped statement concerns the zero-primary structure and exact entry-time populations on the mixed-boundary cylindrical family \(P_{2^r-1}\square C_n\), with both \(r\) and \(n\) unrestricted in their stated domains. Searches did not locate an exact existing cylinder-family formula; the complete Norman (2008) article was not accessible and could contain a relevant specialization.

## Limitations

Only characteristic-two fields and row counts exactly one below a power of two are covered. The theorem classifies first entry into periodic dynamics, not the primitive periods or the numbers of individual periodic orbits. Published general algebraic Jordan results can provide alternative routes to intermediate block calculations. Historical originality remains contingent on comparison with inaccessible or unindexed exact cylinder applications. No external independent validation has been performed.

## References

1. S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics 55 (1983), 601–644. Published July 1, 1983. DOI: 10.1103/RevModPhys.55.601.
2. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic properties of cellular automata*, Communications in Mathematical Physics 93 (1984), 219–258. DOI: 10.1007/BF01223745. Section 4D discusses multidimensional additive rules.
3. C. W. Norman, *On the Jordan form of the tensor product over fields of prime characteristic*, Linear and Multilinear Algebra 38 (1995), 351–371. DOI: 10.1080/03081089508818371.
4. C. W. Norman, *On Jordan bases for the tensor product and Kronecker sum and their elementary divisors over fields of prime characteristic*, Linear and Multilinear Algebra 56 (2008), 415–451. DOI: 10.1080/03081080701395640.
