# Four arithmetic wave clocks for characteristic-three complete tripartite graphs

## Finding

Let \(a,b,c\) be arbitrary **positive** integers, \(N=a+b+c\), and \(K_{a,b,c}\) the simple labelled complete tripartite graph. Over any finite field \(\mathbb F_q\) of characteristic three, \(q=3^f\) with \(f\ge1\), let \(A\) be the adjacency operator and set
\[
T(u,v)=(Au-v,u),\qquad (u,v)\in\mathbb F_q^N\times\mathbb F_q^N.
\]
Every state is periodic from time zero. Sort the three residues of \((a,b,c)\bmod3\) into a string \(\rho\), such as \(012\). The **sharp global periods** are:

| Sorted residue string \(\rho\) | Exact order of \(T\) |
|---|---:|
| \(000,001,002,011,022\) | \(12\) |
| \(012\) | \(24\) |
| \(111,222\) | \(36\) |
| \(112,122\) | \(60\) |

The sole exception is \((a,b,c)=(1,1,1)\), for which the order is **\(9\)**. Thus a third vertex class creates a primitive fifth- or tenth-root temporal sector in the two mixed nonzero residue patterns, and the period-sixty clock is attainable even on \(K_{1,1,2}\).

The following formulas give a **complete exact temporal orbit census** for all positive times. Write \(w=3^{\nu_3(k)}\), \(\epsilon_m=[m\mid k]\), with a bracket equal to one when its divisibility condition holds and zero otherwise. Put \(D_\rho(k)=\dim_{\mathbb F_q}\ker(T^k-I)\), so \(\#\operatorname{Fix}(T^k)=q^{D_\rho(k)}\). Then
\[
\begin{array}{c|l}
\rho&D_\rho(k)\\\hline
000&\epsilon_4\bigl(2(N-6)+6\min(2,w)\bigr)\\
001,002&\epsilon_4\bigl(2(N-5)+2\min(2,w)+2\min(3,w)\bigr)\\
011,022&\epsilon_4\bigl(2(N-4)+2\min(2,w)\bigr)+\min(2,w)(1+\epsilon_2)\\
012&\epsilon_4\bigl(2(N-4)+2\min(2,w)\bigr)+4\epsilon_8\\
111&2(N-3)\epsilon_4+\min(4,w)+\min(2,w)\\
112&2(N-3)\epsilon_4+\min(2,w)+4\epsilon_{10}\\
122&2(N-3)\epsilon_4+\epsilon_2\min(2,w)+4\epsilon_5\\
222&2(N-3)\epsilon_4+\epsilon_2\bigl(\min(4,w)+\min(2,w)\bigr)
\end{array}
\]
In particular, for any positive integer \(d\) dividing the sharp global period, the exact number of labelled states of least period \(d\), and the number of distinct temporal orbits of that length, are
\[
P_d=\sum_{e\mid d}\mu(d/e)q^{D_\rho(e)},\qquad O_d=P_d/d.
\]
The population is zero for every other \(d\). No quotient by graph symmetries or exchange of the two time layers is used. On the smallest period-sixty graph \(K_{1,1,2}\) over \(\mathbb F_3\), there are exactly \(64\) primitive period-sixty orbits, containing \(3840\) of its \(6561\) states.

## Assumptions and scope

The parts are nonempty and their vertices are individually labelled; every cross-part pair is an edge, with no within-part edges or loops. The two time slices are ordered. The field may be any extension of \(\mathbb F_3\); time \(k\) is always a positive integer. All modular residue arithmetic involving part sizes is in characteristic three, while \(N\), fixed-space dimensions, exponents and period counts are ordinary integers. The local rule is **neighbor-sum with previous-state subtraction**, not Boolean majority or chip firing.

## Proof

**1. A fixed three-dimensional factorization.** Define \(S:\mathbb F_q^N\to\mathbb F_q^3\) by the three partwise coordinate sums, and \(U:\mathbb F_q^3\to\mathbb F_q^N\) by replicating each coordinate over its entire part. Let \(M\) be the \(3\times3\) matrix with zero diagonal and all off-diagonal entries one, and let \(D=\operatorname{diag}(a,b,c)\) over \(\mathbb F_q\). Then
\[
SU=D,\quad A=UMS,\quad A^j=UM(DM)^{j-1}S\quad(j\ge1).
\]
The map \(S\) is onto and \(U\) is injective even when a part size is divisible by three. Since \(\det M=2\ne0\) in \(\mathbb F_3\), \(\operatorname{rank}A=3\), and for \(j\ge2\) the rank of \(A^j\) equals the rank of \((DM)^{j-1}\). This retains nilpotent information invisible in an ordinary characteristic polynomial.

**2. Adjacency primary blocks.** The full list of adjacency Jordan data is obtained from the factorization, over an algebraic closure of \(\mathbb F_3\). Write \(J_s(\lambda)\) for a Jordan block of length \(s\) at eigenvalue \(\lambda\). When \(r\) of the three part sizes are nonzero modulo three:

- \(r=0\): \(A^2=0\), \(\operatorname{rank}A=3\); the zero blocks are \(J_2(0)^{\oplus3}\oplus J_1(0)^{\oplus(N-6)}\).
- \(r=1\): the first three ranks are \(3,1,0\); the zero blocks are \(J_3(0)\oplus J_2(0)\oplus J_1(0)^{\oplus(N-5)}\).
- \(r=2\): the ranks are \(3,2,2,\ldots\); the zero blocks are \(J_2(0)\oplus J_1(0)^{\oplus(N-4)}\) and the two other eigenvalues are simple, with \(\lambda^2=ab\) for the two nonzero part-size residues (hence \(\lambda=\pm1\) when the residues agree, and \(\lambda^2=-1\) when they differ).
- \(r=3\): since \(D\) is invertible, the zero blocks are exactly \(J_1(0)^{\oplus(N-3)}\), and the other three dimensions are similar to \(DM\). Their characteristic polynomial is
\[
\chi_{DM}(x)=x^3-(ab+ac+bc)x-2abc.
\]
For \(111\), this is a nonsemisimple \((-1)\)-eigenspace with blocks \(J_2(-1)\oplus J_1(-1)\), because \(DM=M=-I+\boldsymbol1\boldsymbol1^{\mathsf T}\) and the rank-one matrix \(\boldsymbol1\boldsymbol1^{\mathsf T}\) has square zero. The \(222\) case similarly has \(J_2(1)\oplus J_1(1)\). For \(112\), the nonzero factor is \((x+1)(x^2-x-1)\), with distinct roots; for \(122\), it is \((x-1)(x^2+x-1)\), likewise with distinct roots.

The indicated ranks and factorization establish all multiplicities, including singleton part sizes; no generic-position assumption is used.

**3. Transfer to the two-time-level wave.** On a cyclic adjacency block \(J_s(\lambda)\), the wave is the cyclic \(2s\)-dimensional module for
\[
\bigl(z^2-\lambda z+1\bigr)^s.
\]
Indeed, \(T\) is invertible, \(T+T^{-1}=\operatorname{diag}(A,A)\), and a cyclic generator of an adjacency Jordan block together with its time-shift spans both time slices. Its temporal minimal polynomial therefore has degree \(2s\), while the characteristic polynomial is the displayed power. This also handles the double-root resonance when \(\lambda=\pm1\), where the temporal block is a **single** length-\(2s\) Jordan block, not two length-\(s\) blocks.

Put \(h(z)=z^2+1\), \(\Phi_5(z)=z^4+z^3+z^2+z+1\), \(\Phi_{10}(z)=z^4-z^3+z^2-z+1\). The resulting complete temporal elementary-divisor list is:

| Sorted residues | Temporal primary factors, including multiplicities |
|---|---|
| \(000\) | \(h^2\) three times; \(h\) repeated \(N-6\) times |
| \(001,002\) | \(h^3,h^2\), and \(N-5\) copies of \(h\) |
| \(011,022\) | \(h^2\), \(N-4\) copies of \(h\), \((z-1)^2,(z+1)^2\) |
| \(012\) | \(h^2\), \(N-4\) copies of \(h\), \(z^4+1\) |
| \(111\) | \(N-3\) copies of \(h\), \((z-1)^4,(z-1)^2\) |
| \(112\) | \(N-3\) copies of \(h\), \((z-1)^2,\Phi_{10}\) |
| \(122\) | \(N-3\) copies of \(h\), \((z+1)^2,\Phi_5\) |
| \(222\) | \(N-3\) copies of \(h\), \((z+1)^4,(z+1)^2\) |

This table is directly checked by substitution \(x=z+z^{-1}\) in the adjacency factors; \(z^4+1\) is the eighth cyclotomic polynomial. The root orders of \(h,\Phi_5,\Phi_{10},z^4+1,z-1,z+1\) are, respectively, \(4,5,10,8,1,2\). In characteristic three, a length-\(s\) Jordan block at a root of multiplicative order \(m\) has exact order \(m3^{\lceil\log_3 s\rceil}\). Taking least common multiples yields precisely the stated global periods. In the \(111\) case, the zero-sector copies of \(h\) disappear only when \(N=3\), that is, \(K_{1,1,1}\), leaving period nine.

**4. Exact fixed counts.** For any monic irreducible temporal factor \(g\) of degree \(d_g\), the kernel on a \(g^s\) companion block of \(T^k-I\) has dimension \(d_g\min(s,v_g(z^k-1))\). The multiplicity is zero unless the root order divides \(k\); when it does, it equals \(3^{\nu_3(k)}\). Applying this to every factor in Step 3 gives the displayed eight-row dimension formula. The count is \(q^{D_\rho(k)}\), over any characteristic-three extension, since the matrix ranks are unchanged by field extension. Möbius inversion gives all primitive populations and orbit counts. \(\square\)

## Verification

`python tripartite_wave_check.py` constructs the full \(2N\)-dimensional wave matrix over \(\mathbb F_3\) directly from the graph, without using the factorization from the proof, and independently computes its powers and kernel ranks. It verifies the formula at 22 time indices for each of the 56 unordered triples of part sizes in \(\{1,\ldots,6\}\), a total of **1,232 exact rank comparisons**, including all ten residue multisets and the triangle exception. It also checks that the claimed order fixes the entire state space while every proper divisor does not.

`python tripartite_direct_check.py` directly updates every individual two-layer ternary configuration on \(K_{1,1,1}\), \(K_{1,1,2}\), \(K_{1,2,2}\) and \(K_{2,2,2}\), using no matrix powers. It exhausts \(729+6561+59049+531441=597780\) states and checks that all trajectories return immediately, with the primitive populations agreeing with the fixed-space formula. In particular \(K_{1,1,2}\) has \(64\) least-period-sixty orbits; these and the other seven period classes exactly partition all \(6561\) states. These computations are finite corroborations; the all-size theorem follows from Steps 1–4.

## Relationship to prior work

Vlasov (2013) develops the general reversible previous-state subtraction construction, including its ternary instantiation, but does not classify the graph-dependent periods here. Delorme (2012) gives a characteristic polynomial for the adjacency matrix of any complete multipartite graph over the reals; that polynomial can be reduced modulo three, but it does **not** determine the modular Jordan blocks when part sizes vanish modulo three, nor the temporal primary factors and orbit populations.

An existing published result for characteristic-three waves on complete **bipartite** graphs gives periods eight or twelve depending on the two part sizes. It does not imply the tripartite period-36/60 phases: the third part alters the cubic quotient and produces fifth-/tenth-root temporal sectors. A published characteristic-**two** classification on complete multipartite graphs yields a different universal period bound and cannot imply the characteristic-three table. The triangle exception \(K_{1,1,1}\), which is the one-dimensional Hamming graph \(H(1,3)\), is also covered by an existing ternary Hamming-wave classification; that isolated special case is not claimed as new. The present claim is the exact characteristic-three tripartite classification, not a claim to have invented reversible second-order updating, multipartite adjacency spectra, or finite-field Jordan theory.

## Limitations

The formula applies only to the displayed neighbor-sum reversible update on complete **three**-partite graphs and characteristic-three finite fields. It gives every period population but not attraction basins, since the map is invertible and has no transients. Published and searchable records inspected here do not prove worldwide historical uniqueness; an unindexed equivalent modular-wave classification is a residual priority risk. External independent validation has not been performed.

## References

1. Alexander Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297v1, first publicly submitted 2013-11-18, especially Sections 3 and 6.2. https://arxiv.org/abs/1311.4297
2. C. Delorme, *Eigenvalues of complete multipartite graphs*, Discrete Mathematics 312 (2012), 2532–2535, DOI:10.1016/j.disc.2011.07.018. https://doi.org/10.1016/j.disc.2011.07.018
3. *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs*, published mathematical result (2026), record 167b2c8980f2; its all-size bipartite theorem and proof were compared.
4. *Twenty-four-step resonances in reversible waves on complete multipartite graphs*, published mathematical result (2026), record addc32219e63; its characteristic-two classification and proof were compared.
5. *A three-class wave clock and exact orbit census for ternary-modular Hamming graphs*, published mathematical result (2026), record 13302e527b48; its triangle special case is acknowledged.
