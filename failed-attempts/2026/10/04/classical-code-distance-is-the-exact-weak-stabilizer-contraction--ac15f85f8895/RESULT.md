# Classical-code distance is the exact weak-stabilizer contraction exponent
## Finding
For a qubit stabilizer code with \(r\) independent generators, consider one measurement round made of \(L\) equal-strength, nonselective weak measurements of stabilizer observables. Fix a generator basis and identify a stabilizer with a vector \(v\in\mathbb F_2^r\). If the measured stabilizers are \(B(v_1),\ldots,B(v_L)\), form
\[
G=[v_1\ \cdots\ v_L]\in\mathbb F_2^{r\times L}.
\]
With \(\zeta=\operatorname{sech}(\epsilon)\), the round has the exact spectrum
\[
\mathcal T_G\big|_{W_{B(u)}^{\mathbb C}}
=\zeta^{\operatorname{wt}(u^{\mathsf T}G)}I,
\qquad u\in\mathbb F_2^r.
\]
Thus, when \(\operatorname{rank}G=r\),
\[
\left\|\mathcal T_G\big|_{\bigoplus_{u\ne0}W_{B(u)}^{\mathbb C}}\right\|_{2\to2}
=\zeta^{d(C_G)},
\qquad
C_G=\{u^{\mathsf T}G:u\in\mathbb F_2^r\},
\]
where \(d(C_G)\) is the minimum Hamming distance of the binary linear \([L,r]\) code \(C_G\). If \(G\) is rank deficient, some nonzero \(u\) has \(u^{\mathsf T}G=0\), so a nontrivial isotypical sector is unchanged and the restricted norm is \(1\).

It follows that the optimal worst-sector residual factor among all \(L\)-measurement schedules with repetition allowed is
\[
\zeta^{d_2(L,r)},
\]
where \(d_2(L,r)\) is the largest possible minimum distance of a binary linear \([L,r]\) code. If measured stabilizers are required to be distinct, the identical conclusion holds after restricting to full-rank generator matrices with distinct nonzero columns.

This places the two protocols analyzed in the source at coding-theoretic endpoints. Measuring only an independent generating set gives a \([r,r,1]\) code and worst factor \(\zeta\). Measuring every nonidentity stabilizer gives the binary simplex code
\[
[2^r-1,r,2^{r-1}],
\]
and worst factor \(\zeta^{2^{r-1}}\). A first intermediate example occurs already at \(r=3\): measuring the three generators and their triple product corresponds to
\[
G=\begin{bmatrix}
1&0&0&1\\
0&1&0&1\\
0&0&1&1
\end{bmatrix},
\]
whose nonzero codewords have minimum weight \(2\). One additional weak stabilizer measurement therefore improves the worst one-round factor from \(\zeta\) to \(\zeta^2\), while the seven-observable full-group endpoint gives \(\zeta^4\).

## Assumptions and scope
The code is a qubit stabilizer code with \(r=n-k\) independent stabilizer generators. Each elementary measurement is the same nonselective weak stabilizer measurement used by Dominy, Paz-Silva, Rezakhani, and Lidar, with one common strength \(\epsilon>0\). Its attenuation parameter is \(\zeta=\operatorname{sech}(\epsilon)\in(0,1)\). The finding concerns the measurement superoperator itself, with the Hilbert--Schmidt norm induced by the mutually orthogonal isotypical decomposition of operator space.

Repeated stabilizer observables are allowed in the unrestricted scheduling statement and simply consume additional elementary measurements. The distinct-observable variant forbids repeated or identity columns. The identity stabilizer is omitted because its nonselective measurement is the identity channel.

No claim is made that the complete system--bath trace-distance error after interleaving these rounds with arbitrary Hamiltonian evolution is exactly \(\zeta^{d(C_G)}\). Extending the source's dynamical bounds from its two endpoint protocols to arbitrary coded schedules requires a separate recurrence analysis.

## Proof
Fix independent generators \(\bar S_1,\ldots,\bar S_r\) and the group isomorphism
\[
B:\mathbb F_2^r\longrightarrow\mathbf S,
\qquad
B(v)=\prod_{i=1}^r\bar S_i^{v_i}.
\]
The source defines the character exponent
\[
\sigma_{B(u)}(B(v))=u^{\mathsf T}v\pmod2
\]
and the mutually orthogonal operator sectors \(W_{B(u)}^{\mathbb C}\). Its Lemma 5 proves that for \(A_u\in W_{B(u)}^{\mathbb C}\),
\[
\mathcal P_{B(v),\epsilon}(A_u)
=\zeta^{u^{\mathsf T}v}A_u.
\]
Because every elementary measurement is diagonal in this common orthogonal decomposition, the measurement superoperators commute. Composing the \(L\) measurements therefore gives
\[
\mathcal T_G(A_u)
=\prod_{j=1}^L\zeta^{u^{\mathsf T}v_j}A_u
=\zeta^{\sum_{j=1}^L u^{\mathsf T}v_j}A_u
=\zeta^{\operatorname{wt}(u^{\mathsf T}G)}A_u.
\]
Here each scalar product is interpreted in \(\{0,1\}\), so its ordinary integer sum is precisely the Hamming weight of the length-\(L\) word \(u^{\mathsf T}G\).

If \(G\) has rank \(r\), the map \(u\mapsto u^{\mathsf T}G\) is injective and its image \(C_G\) is a binary linear \([L,r]\) code. Since the isotypical sectors are Hilbert--Schmidt orthogonal and \(0<\zeta<1\), the induced norm on their nontrivial direct sum is the largest eigenvalue there:
\[
\max_{u\ne0}\zeta^{\operatorname{wt}(u^{\mathsf T}G)}
=\zeta^{\min_{u\ne0}\operatorname{wt}(u^{\mathsf T}G)}
=\zeta^{d(C_G)}.
\]
If \(G\) is rank deficient, some nonzero \(u\) belongs to its left kernel, producing eigenvalue \(1\).

Conversely, every full-rank binary \(r\times L\) generator matrix specifies a stabilizer schedule by measuring the stabilizer represented by each column. Therefore minimizing the worst residual factor is exactly equivalent, because \(\zeta\in(0,1)\), to maximizing the minimum distance of a binary linear \([L,r]\) code. This proves the unrestricted optimization statement. Requiring distinct nonidentity stabilizers is exactly the additional condition that the columns are distinct and nonzero.

For the generator-only schedule, \(G=I_r\), so \(d(C_G)=1\). For the full nonidentity stabilizer schedule, the columns are all nonzero vectors of \(\mathbb F_2^r\). For every nonzero \(u\), exactly half of all \(2^r\) vectors satisfy \(u^{\mathsf T}v=1\), and the zero vector never does; hence every nonzero codeword has weight \(2^{r-1}\). This is the binary simplex endpoint. For the stated \(r=3\) intermediate matrix, direct evaluation gives six nonzero words of weight \(2\) and one of weight \(4\), hence distance \(2\).

## Verification
The proof is analytic. The accompanying checker independently enumerates all nonzero character labels for the generator endpoint, the full nonidentity endpoint, and the \(r=3\) four-observable schedule. It also exhausts all distinct nonidentity-column schedules for \(r=3\), obtaining optimal distances \(1,2,2,3,4\) for lengths \(3,4,5,6,7\), respectively. These finite checks are supplementary; the general theorem follows from the character formula and linear-code identification above.

The critical nonstandard input was checked directly in the open full text of Dominy et al.: their Lemma 5 gives the single-measurement eigenvalue \(\zeta^{\sigma_S(g)}\), their Lemma 6 gives the full-group exponent \(2^{r-1}\), and their Lemma 7 gives the generator-only weight-dependent spectrum. The present proof uses Lemma 5 and derives the arbitrary-schedule result without assuming either endpoint lemma.

## Relationship to prior work
Paz-Silva, Rezakhani, Dominy, and Lidar introduced weak stabilizer measurements for Zeno protection. Dominy, Paz-Silva, Rezakhani, and Lidar then supplied the detailed isotypical decomposition and analyzed two schedules: the full stabilizer group and a minimal generating set. Their paper does not formulate the arbitrary multiset of measured stabilizers as a binary code or optimize its worst isotypical contraction by code distance.

A separate literature on robust syndrome extraction uses classical coding for a different objective. Ashikhmin, Lai, and Brun's syndrome-measurement codes add redundant stabilizer measurements so that noisy classical syndrome outcomes form codewords of a binary linear code. Ouyang later gave a general code-inspired construction of robust projective measurements, with classical minimum distance controlling correction of corrupted measurement outcomes. Those works establish that classical codes naturally organize redundant observables, but they study selective/projective readout and classical outcome errors, not the spectrum of a nonselective weak-measurement channel. The new point here is that the same code's Hamming weight is exactly the exponent of quantum coherence attenuation, so its minimum distance is exactly the worst-sector weak-measurement contraction exponent.

Classical code tables already contain parameters such as the binary \([4,3,2]\) code used in the example. No classical code parameter is claimed as new; the contribution is the exact weak-stabilizer channel correspondence and its resource/suppression optimization.

## Limitations
The result assumes a common weak-measurement strength. Unequal strengths lead instead to a weighted Hamming objective. The exact norm statement is Hilbert--Schmidt and applies to the measurement layer; it is not an exact trace-distance statement for a complete open-system evolution. Physical implementation cost may depend strongly on stabilizer Pauli weight, so counting elementary observables alone does not model every hardware architecture.

The classical-code redundancy idea is established prior work. The literature comparison did not locate a source explicitly stating the weak nonselective attenuation/code-distance equivalence, but an unindexed or differently phrased source could exist. In particular, the 2014 robust-syndrome-extraction paper and later data-syndrome literature remain the closest conceptual predecessors even though their stated objective is classical syndrome reliability.

## References
1. G. A. Paz-Silva, A. T. Rezakhani, J. M. Dominy, and D. A. Lidar, “Zeno effect for quantum computation and control,” arXiv:1104.5507, first public 2011-04-28; Phys. Rev. Lett. 108, 080501 (2012), DOI: 10.1103/PhysRevLett.108.080501.
2. J. M. Dominy, G. A. Paz-Silva, A. T. Rezakhani, and D. A. Lidar, “Analysis of the quantum Zeno effect for quantum control and computation,” arXiv:1207.5880, J. Phys. A 46, 075306 (2013), DOI: 10.1088/1751-8113/46/7/075306.
3. A. Ashikhmin, C.-Y. Lai, and T. A. Brun, “Robust quantum error syndrome extraction by classical coding,” IEEE ISIT (2014), DOI: 10.1109/ISIT.2014.6874892.
4. A. Ashikhmin, C.-Y. Lai, and T. A. Brun, “Quantum Data-Syndrome Codes,” arXiv:1907.01393.
5. Y. Ouyang, “Robust projective measurements through measuring code-inspired observables,” npj Quantum Information 10, 104 (2024), DOI: 10.1038/s41534-024-00904-y.
6. M. Grassl, “Bounds on the minimum distance of linear codes,” codetables.de; the database includes the binary \([4,3,2]\) code as the dual of the length-four repetition code.
