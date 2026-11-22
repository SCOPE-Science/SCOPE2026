# Two sharp entropy spikes for a row-staggered three-state Potts antiferromagnet

## Finding
For the two-row diagonally triangulated cyclic ladder defined below, with three Potts colors and an equal-strength row-staggered field preferring color \(0\) on the top row and color \(1\) on the bottom row, the minimum energy per column in units of the antiferromagnetic coupling is
\[
g(h)=\min\left\{-\frac{2h}{3},\ \frac23-\frac{4h}{3},\ 2-2h\right\}\qquad(h\geq0).
\]
The two and only two positive critical fields are \(h=1\) and \(h=2\). For **every** column count \(n\geq3\) divisible by \(3\), the exact finite-system minimum is \(E_n(h)=nJg(h)\). In the three strict intervals, the number of labeled ground configurations is respectively \(6\), \(3\), and \(1\). At \(h=1\), the exact ground-state count is \(3L_{2n/3}\), with \(L_k\) the Lucas number defined by \(L_0=2,L_1=1,L_{k+2}=L_{k+1}+L_k\). At \(h=2\), the count is \(\sum_{j=1}^3\lambda_j^n\), where \(\lambda_j\) are the three complex roots, counted with multiplicity, of \(\lambda^3-\lambda^2-2\lambda-1=0\). Both coexistence values have exponentially many ground states while the three neighboring open-field phases have only finitely many. Their exact residual entropies per spin along the lengths divisible by \(3\) are, respectively,
\[
s(1)=\frac13\log\!\left(\frac{1+\sqrt5}{2}\right),\qquad
s(2)=\frac12\log\rho,
\]
where \(\rho\approx2.1478990357\) is the unique positive root of \(\rho^3-\rho^2-2\rho-1=0\). At every noncritical positive field the residual entropy is zero. For arbitrary lengths \(n\to\infty\), including lengths not divisible by \(3\), the normalized minimum-energy limit is still \(g(h)\).

## Assumptions and scope
For each integer \(n\geq3\), take vertices \(T_i,B_i\), with column indices \(i\in\mathbb Z/n\mathbb Z\). Edges are \(T_iB_i\), \(T_iT_{i+1}\), \(B_iB_{i+1}\), and \(T_iB_{i+1}\), once for every \(i\). All spins \(\sigma_v\) take values in \(\{0,1,2\}\). For \(J>0\) and \(H\geq0\), define the dimensionless field \(h=H/J\) and the Hamiltonian
\[
\mathcal H(\sigma)=J\sum_{uv\in E}\mathbf1_{\sigma_u=\sigma_v}
-H\sum_{i=0}^{n-1}\left(\mathbf1_{\sigma_{T_i}=0}+\mathbf1_{\sigma_{B_i}=1}\right).
\]
Ground states are **labeled** spin assignments, without quotienting by rotations or color permutations. A residual entropy means \(\lim_{k\to\infty}\log D_{3k}(h)/(6k)\), with \(D_n(h)\) the exact ground-state multiplicity. No positive-temperature singularity is asserted.

## Proof
Write each column as \(u=(a,b)\in\{0,1,2\}^2\), and the next as \(v=(c,d)\). The four bonds charged to the transition are exactly
\[
C(u,v)=\mathbf1_{c=d}+\mathbf1_{a=c}+\mathbf1_{b=d}+\mathbf1_{a=d},\qquad M(v)=\mathbf1_{c=0}+\mathbf1_{d=1}.
\]
Thus \(\mathcal H/J=\sum_i(C(u_i,u_{i+1})-hM(u_{i+1}))\). There are exactly nine column states, in lexicographic order \((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)\).

For \(h\in\{0,1,2\}\), the following table gives the claimed energy lower bound \(g(h)\) and a dual potential \(p_h\), with entries in that state order:

| \(h\) | \(g(h)\) | \(p_h\) |
|---|---|---|
| \(0\) | \(0\) | \((0,0,0,0,0,0,0,0,0)\) |
| \(1\) | \(-2/3\) | \((-1/3,-4/3,-2/3,-1/3,0,-2/3,0,-1,0)\) |
| \(2\) | \(-2\) | \((0,-2,-1,0,0,0,0,-1,0)\) |

All \(243\) exact rational inequalities
\[
C(u,v)-hM(v)-g(h)+p_h(u)-p_h(v)\geq0
\]
hold for the three rows and all ordered pairs of column states. They can be checked directly by the included dependency-free program. Summing over a closed walk telescopes the potential terms, so \(E_n(h)/J\ge ng(h)\) at the three checkpoint fields. Linear interpolation in \(h\) and in the potentials proves the same bound on \([0,1]\) and \([1,2]\); for \(h\ge2\), keeping the last potential gives an additional nonnegative term \((h-2)(2-M(v))\).

The three periodic column words
\[
((0,1),(1,2),(2,0)),\quad ((0,1),(0,2),(2,1)),\quad ((0,1))
\]
have mean bond penalties \(0,2/3,2\) and mean field counts \(2/3,4/3,2\), respectively. Therefore their energies per column are exactly the three branches. Their lengths divide every \(n\) divisible by \(3\). Each is a strict ground-energy branch on exactly one nonempty open interval, proving both sharp transitions. For all other lengths, padding a repeated minimizing word by at most two columns changes its energy by a bounded amount depending on \(h\), proving the same limiting energy density.

For a fixed field, take a dual potential obtained above by interpolation and let \(A_h\) be the nine-by-nine zero-one matrix with an entry \(1\) exactly when the displayed dual inequality is an equality. At all lengths divisible by \(3\), the minimizing constructions attain the lower bound exactly; hence every ground-state closed walk uses only equality edges and conversely. Thus \(D_n(h)=\operatorname{tr}(A_h^n)\). Exact characteristic-polynomial calculations give

| Field | \(\det(\lambda I-A_h)\) |
|---|---|
| \(0\le h<1\) | \(\lambda^3(\lambda-1)^2(\lambda^2+\lambda+1)^2\) |
| \(h=1\) | \(\lambda^3(\lambda^6-3\lambda^3+1)\) |
| \(1<h<2\) | \(\lambda^6(\lambda^3-1)\) |
| \(h=2\) | \(\lambda^6(\lambda^3-\lambda^2-2\lambda-1)\) |
| \(h>2\) | \(\lambda^8(\lambda-1)\) |

Inside the open intervals the equality graph is constant because the interpolated nonnegative slack of an edge vanishes at an interior field only when it vanishes at both surrounding endpoints. The table follows from exact integer determinant coefficients (Newton identities) and is reproduced by the included program. Powers of the nonzero eigenvalues give the stated exact multiplicities. At \(h=1\), setting \(x=\lambda^3\) gives \(x^2-3x+1=0\), whose roots are the squares of the golden ratio and its inverse, yielding the Lucas formula. At \(h=2\), the nonnegative irreducible critical component has Perron root \(\rho\), the positive root of the displayed cubic. The formulas for the entropy follow by taking logarithmic growth rates. All noncritical cases have uniformly bounded multiplicities.

## Verification
Running `python3 verify_staggered_potts.py` checks the three dual potentials against all \(243\) rational inequalities, verifies the three exact periodic witness energies, reconstructs the full nine-state zero-slack matrices, and obtains their characteristic-polynomial coefficients using integer arithmetic and Newton identities. It also enumerates independently all \(9^6=531441\) six-column spin configurations, with ground-state counts \((6,21,3,98,1)\) at fields \((1/2,1,3/2,2,3)\). All checks passed. The finite enumeration is a verification of small instances, not the proof for arbitrary system sizes; the exact dual inequalities and transfer argument supply the general proof.

## Relationship to prior work
Shrock and Tsai (1999) and Chang and Shrock (2000) analyze zero-field Potts models on triangular-lattice strips, including width-two cyclic strips. Chang and Shrock (2009) give full-field transfer-matrix machinery on such strips with a **single common favored Potts color at every site**. Shrock and Xu (2010) likewise address uniform color-set fields and several graph families. Those formulas provide relevant comparison and methodology but do not yield the present row-dependent color preference by a global spin relabeling: relabeling only the bottom row would twist the cross-row equality interactions. The present exact two-threshold row-staggered diagram, its full commensurate-size ground-state counts, and the two entropy spikes were not found in the compared texts. The possibility of earlier unindexed work or an equivalent treatment using more general site-dependent transfer matrices remains.

## Limitations
The finite-size multiplicity formulas require \(3\mid n\); for other circumferences only the limiting ground-energy density is proved here. The field is nonnegative, the three Potts colors and four specified bond families have uniform antiferromagnetic coupling, and the two row preferences have the same strength. The two entropy spikes concern the zero-temperature ground-state limit, not finite-temperature phase transitions. The cited literature and database searches do not independently certify publication priority or mathematical novelty.

## References
1. R. Shrock and S.-H. Tsai, *Exact Partition Functions for Potts Antiferromagnets on Cyclic Lattice Strips*, first posted July 26, 1999, https://arxiv.org/abs/cond-mat/9907403 .
2. S.-C. Chang and R. Shrock, *Exact Potts Model Partition Function on Strips of the Triangular Lattice*, first posted April 11, 2000, https://arxiv.org/abs/cond-mat/0004181 .
3. S.-C. Chang and R. Shrock, *Structure of the Partition Function and Transfer Matrices for the Potts Model in a Magnetic Field on Lattice Strips*, first posted July 6, 2009, https://arxiv.org/abs/0907.0925 .
4. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, first posted September 7, 2010, https://arxiv.org/abs/1009.1182 .
