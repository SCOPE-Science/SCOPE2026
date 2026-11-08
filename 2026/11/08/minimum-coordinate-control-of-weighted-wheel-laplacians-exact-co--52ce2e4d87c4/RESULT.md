# Minimum coordinate control of weighted wheel Laplacians: exact coupling resonances and placements

## Finding

Consider the wheel \(W_{m+1}=K_1\vee C_m\), for every integer \(m\ge3\), with rim-edge weight \(1\), uniform spoke-edge weight \(t>0\), independently controlled vertices, and continuous-time Laplacian dynamics \(\dot z=-L_{m,t}z+B_Su\). Put \(q=m\) when \(m\) is odd, and \(q=m/2\) when \(m\) is even. For \(1\le j\le\lfloor m/2\rfloor\), put \(\nu_j=2-2\cos(2\pi j/m)\). A *double-mode resonance* means \(t=\nu_j/m\) for at least one \(j\) with \(1\le j<m/2\).

**Theorem.** The minimum number of independently actuated vertices is precisely \(3\) at a double-mode resonance and precisely \(2\) at every other positive spoke weight. In the latter case, every optimal actuator set is a pair of rim vertices \(\{a,b\}\), \(0\le a<b<m\), with \(d=b-a\), satisfying \(\gcd(q,d)=1\); if \(m\) is even and \(t=4/m\), it must additionally satisfy that \(d\) is odd. No pair containing the hub is controlling.

At a double-mode resonance \(t=\nu_k/m\), necessarily for a unique \(1\le k<m/2\), every optimal set is exactly one of the following:

1. The hub together with two rim vertices \(a,b\) such that \(\gcd(q,b-a)=1\).
2. Three rim vertices \(a<b<c\) such that \(\gcd(q,b-a,c-a)=1\) and the three residues \(ka,kb,kc\pmod m\) are pairwise distinct.

Both descriptions are necessary and sufficient. Two or three consecutive rim vertices exhibit attainability in the respective regimes. The number of optimal pairs away from double-mode resonances is \(m\varphi(m)/2\) when \(m\) is odd, and \(m\varphi(m/2)\) when \(m\) is even and \(t\ne4/m\). At \(t=4/m\) for even \(m\), this number is \(m\varphi(m/2)\) if \(4\mid m\), and \(m\varphi(m/2)/2\) if \(m\equiv2\pmod4\). Here \(\varphi\) denotes Euler's totient.

## Assumptions and scope

Number the rim vertices by the cyclic group \(\mathbb Z/m\mathbb Z\) and the hub by the symbol \(h\). The Laplacian, with the rim block written first, is

\[
L_{m,t}=\begin{pmatrix}
L(C_m)+tI_m&-t\mathbf1_m\\
-t\mathbf1_m^T&mt
\end{pmatrix}.
\]

The input matrix \(B_S\) consists of distinct standard basis columns indexed by \(S\); in particular, different chosen vertices receive *independent* inputs. “Controlling” means the usual finite-dimensional Kalman controllability, equivalently the PBH condition for every real eigenvalue of the symmetric Laplacian. Only \(t>0\), uniform spokes, and unit rims are asserted. Nothing is claimed for a single broadcast signal shared across all selected vertices or for unequal spoke weights.

## Proof

**1. Entire real eigenspace decomposition.** For \(1\le j<m/2\), write \(\theta_j=2\pi j/m\). The rim vectors

\[
c_j(a)=\cos(\theta_j a),\qquad s_j(a)=\sin(\theta_j a)
\]

extended by zero at \(h\), span a real two-dimensional eigenspace of eigenvalue \(t+\nu_j\). If \(m\) is even, the alternating rim vector \((-1)^a\), extended by zero at \(h\), gives a one-dimensional eigenspace of eigenvalue \(t+4\). The constant all-ones vector has eigenvalue \(0\); the vector with rim components all \(1\) and hub component \(-m\) has eigenvalue \((m+1)t\). Orthogonality of discrete Fourier modes shows that these spaces span all \(m+1\) coordinates. Since \(\nu_j\) strictly increases with \(j\) in the indicated range, the only nontrivial coincidences are \((m+1)t=t+\nu_j\), i.e. \(mt=\nu_j\); at most one such \(j\) occurs for any fixed \(t>0\).

**2. PBH on rim samples.** Because \(L_{m,t}\) is real symmetric, a selected set \(S\) is controlling if and only if coordinate restriction from each complete eigenspace to \(\mathbb R^S\) is injective. In particular, a Fourier double eigenspace cannot be detected by a pair containing the hub, since all its eigenvectors vanish there. For a rim pair \(\{a,b\}\), the restriction determinant for mode \(j\) is \(\sin(2\pi j(b-a)/m)\). This vanishes precisely when \(q\mid j(b-a)\), where \(q=m/\gcd(m,2)\). There exists an integer \(j\) with \(1\le j<m/2\) satisfying this congruence if and only if \(\gcd(q,b-a)>1\): when the gcd is \(g>1\), take \(j=q/g\), which lies in the specified range; conversely a nonzero admissible \(j\) cannot be divisible by \(q\). Thus \(\gcd(q,b-a)=1\) is exactly the simultaneous full-rank condition for *all* two-dimensional Fourier modes.

**3. Away from double-mode resonances.** The zero-eigenvalue vector restricts nontrivially to every nonempty input set, as does the radial vector. The alternating eigenvector, when present and not resonant, is nonzero at either rim vertex. Therefore a rim pair is controlling exactly under the gcd condition, unless the radial vector collides with the alternating vector. This last collision is \(m\) even, \(mt=4\); on two rim vertices the radial and alternating restrictions are \((1,1)\) and \(((-1)^a,(-1)^b)\), respectively, and have rank two exactly when \(b-a\) is odd. The Fourier-pair multiplicity already forces at least two inputs. Consecutive rim vertices meet the conditions; this proves the claimed minimum \(2\) and complete pair classification.

**4. At a double-mode resonance.** If \(mt=\nu_k\) with \(1\le k<m/2\), the joint eigenvalue has eigenspace \(\operatorname{span}\{r,c_k,s_k\}\) of dimension \(3\), where \(r\) is the radial vector. PBH therefore forces at least three independent inputs. The hub plus two rim vertices gives a restriction matrix with one nonzero hub entry in its radial column and a two-by-two Fourier determinant on the rim rows. This particular joint eigenspace has rank three exactly when \(q\nmid k(b-a)\). Full controllability also requires rank two at every other Fourier double mode; combining these conditions over *all* indices \(1\le j<m/2\) is equivalent to \(\gcd(q,b-a)=1\). Constant and alternating singleton restrictions are nonzero. For three rim vertices, restriction of the joint eigenspace has, up to nonzero scalar changes, rows \((1,\cos\theta_k a,\sin\theta_k a)\), \((1,\cos\theta_k b,\sin\theta_k b)\), and \((1,\cos\theta_k c,\sin\theta_k c)\). Three points on a unit circle are affinely independent in the plane precisely when they are pairwise distinct, proving the stated modular residue criterion. For each nonresonant Fourier double mode \(j\), the three sampled rows have rank two unless both differences \(b-a,c-a\) satisfy \(q\mid j(b-a)\) and \(q\mid j(c-a)\). An admissible such \(j\) exists precisely when \(\gcd(q,b-a,c-a)>1\), by the same least-positive-multiple argument. If the failing \(j\) were the resonant \(k\), its joint three-dimensional restriction would also fail, so the conditions stated are jointly necessary and sufficient. Constant and alternating singleton eigenspaces cause no further obstruction. The sets \(\{h,0,1\}\) and \(\{0,1,2\}\) satisfy the conditions (the latter has distinct resonant residues since \(1\le k<m/2\)).

**5. Counting optimal pairs.** For odd \(m\), the number of admissible nonzero differences \(d\pmod m\) is \(\varphi(m)\). Every unordered pair is encountered exactly twice among the \(m\) anchored ordered differences; hence \(m\varphi(m)/2\). When \(m=2q\), there are \(2\varphi(q)\) differences \(1\le d<m\) coprime to \(q\), giving \(m\varphi(q)\) pairs. At alternating-mode resonance, parity is automatic for \(q\) even (hence \(4\mid m\)). For \(q\) odd (hence \(m\equiv2\pmod4\)), each admissible residue class modulo \(q\) has two lifts with opposite parity, so exactly half of the corresponding unordered pairs remain.

## Verification

The self-contained Python standard-library checker \(`verify.py`\) constructs integral scalings of the rational-weight Laplacian and computes Kalman ranks modulo the prime \(1000003\). It tests \(75\) rational parameter configurations for rim counts \(3\) through \(14\), \(3548\) two-input placements, and \(1146\) three-input placements at tested non-Nyquist resonances. The executed run reported \(2113\) full-rank and \(1435\) deficient two-input cases, \(526\) successful and \(620\) unsuccessful three-input cases; all predicted statuses agreed. It also checked the arithmetic pair counts for \(68\) rim sizes, and performed separate positive tests on consecutive three-vertex inputs at observed resonances. Execute \(`python verify.py`\) in the extracted directory to reproduce.

These are finite modular computations, *not* exhaustive arithmetic proof for arbitrary \(m\) or irrational spoke weights; the unconditional theorem is established in the five algebraic steps above. Modular full rank certifies rational full rank when observed, whereas deficient modular rank alone does not certify deficient rational rank; the analytic PBH proof establishes the latter.

## Relationship to prior work

Parlangeli and Notarstefano's path/cycle reachability results provide earlier number-theoretic Fourier controllability criteria for cycle and path networks; they do not classify wheel hub eigenvalue collisions as the uniform spoke conductance varies. Florek and Marlewski describe spectral calculations for arrow-bordered circulant matrices and weighted wheels. The Fourier decomposition and wheel spectrum themselves are *not* claimed as new; the contribution here is the simultaneous all-coupling coordinate actuator minimum, its exact pair and triple configurations, and the parity-sensitive placement counts. Published general leader-set PBH and perfect-critical-set frameworks provide necessary and sufficient abstract criteria but do not themselves give the stated closed classification. The closest accessible research-record comparison of sharp two-sensor bounds on finite cycles concerns frequency-limited reconstruction rather than full-system Laplacian controllability with a weighted hub.

## Limitations

The result concerns finite, undirected, real, **uniform-spoke** wheel Laplacians and independently addressable control inputs. It does not address arbitrary edge weights, input costs, strong structural controllability, noisy or restricted-time observability, or robustness near an exact resonance. The exact spectrum is classical; priority for the specific placement classification has been compared with accessible full texts and indexed records, but inaccessible or unindexed specialist literature remains a publication-priority risk. The verification script covers only rational test values and finite rim sizes. No independent audit has been performed.

## References

- G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, first public 2011-09-16, https://arxiv.org/abs/1109.3556 .
- M. Florek and W. Marlewski, *Spectrum of some arrow-bordered circulant matrix*, arXiv:1905.04807, first public 2019-05-12, https://arxiv.org/abs/1905.04807 .
- T. Dai et al., *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications, 2023, https://doi.org/10.1049/cth2.12385 .
