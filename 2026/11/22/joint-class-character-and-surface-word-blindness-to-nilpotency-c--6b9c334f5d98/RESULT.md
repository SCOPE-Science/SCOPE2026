# Joint class, character and surface-word blindness to nilpotency class in exponent-\(p\) groups

## Finding

For every prime \(p\ge5\), there exist two nonisomorphic finite groups of order \(p^{2p+1}\) and exponent \(p\), with the same derived-group and center orders, the same **complete multiplicities** of all conjugacy-class sizes and complex irreducible character degrees, and identical probability distributions for every orientable surface word \(w_t=\prod_{i=1}^{t}[x_i,y_i]\) (\(t\ge1\)), under a linear identification of their elementary abelian derived groups. Their nilpotency classes are nevertheless \(p-1\) and \(2\), respectively. Thus the class gap \(p-3\) is unbounded as primes vary.

More generally, let \(N\ne0\) be an \(n\times n\) nilpotent matrix over \(\mathbb F_p\) with \(N^{p-1}=0\). Put \(b=\dim\ker N\), \(T=I+N\), and \(G_N=(\mathbb F_p)^n\rtimes_T C_p\). The complete conjugacy-class-size generating polynomial (the coefficient of \(X^s\) counts classes of size \(s\)) is
\[
K_N(X)=p^b X+\frac{p^n-p^b}{p}X^p+(p-1)p^b X^{p^{n-b}}.
\]
If \(n-b=1\), the two positive-size terms coincide and their coefficients are automatically added. The complete irreducible complex character-degree multiplicities are \(p^{b+1}\) at degree \(1\) and \((p^n-p^b)/p\) at degree \(p\), with no other degrees. The group has order \(p^{n+1}\), exponent \(p\), center order \(p^b\), derived group \(W=N\mathbb F_p^n\) of order \(p^{n-b}\), and nilpotency class equal to the maximum Jordan-block length of \(N\).

For independent uniform inputs, each surface-word value lies in \(W\), and for \(z\in W\) its exact probability is
\[
\Pr(w_t=z)=p^{-2t}\mathbf1_{\{z=0\}}+(1-p^{-2t})p^{-(n-b)}.
\]
The exact ordered fiber size is \(p^{2t(n+1)}\Pr(w_t=z)\). In particular, all these distributions and multiplicities depend on \(n,b,p\) but not on the other Jordan-block lengths.

Take \(n=2p\) and the partitions \(\lambda=(p-1,3,1^{p-2})\) and \(\mu=(2^p)\). Each has \(p\) parts, the same \(n,b\), and maximum block length at most \(p-1\). For each group the conjugacy-class counts at sizes \(1,p,p^p\) are respectively \(p^p\), \(p^{2p-1}-p^{p-1}\), and \((p-1)p^p\); character counts at degrees \(1,p\) are \(p^{p+1}\) and \(p^{2p-1}-p^{p-1}\). Their nilpotency classes differ.

## Assumptions and scope

The base field is the prime field \(\mathbb F_p\); \(p\) is an odd prime and \(N\ne0\), \(N^{p-1}=0\). The cyclic factor \(C_p\) acts via \(T=I+N\); this is well-defined since \(T^p=I\) and \(T\ne I\). The commutator convention is \([g,h]=ghg^{-1}h^{-1}\). The surface-word statement concerns products of **independent** commutators, not arbitrary words. The pairing of the groups uses any \(\mathbb F_p\)-linear isomorphism of their derived groups, not a group isomorphism of the ambient groups.

## Proof

Write elements as \((v,j)\) with \(v\in V=(\mathbb F_p)^n\), \(j\in\mathbb Z/p\mathbb Z\) and multiplication \((v,j)(w,k)=(v+T^jw,j+k)\). Since \(N^{p-1}=0\), \((I+N)^p=I\), and for each \(j\ne0\), the identity \(T^j-I=N u_j(N)\) holds with \(u_j(0)=j\ne0\). Therefore \(u_j(N)\) is invertible, so \(\ker(T^j-I)=\ker N\) and \(\operatorname{im}(T^j-I)=W=NV\) for every nonzero \(j\).

The commutators with the cyclic generator generate \(W\), hence \(G_N'=W\), and iterated commutators give \(\gamma_{k+1}(G_N)=N^kV\) for \(k\ge1\). Thus the class equals the nilpotency index of \(N\). For \(j\ne0\), the \(p\)-th power of \((v,j)\) is \((\sum_{h=0}^{p-1}T^{jh}v,0)\). In characteristic \(p\), \(\sum_{h=0}^{p-1}X^h=(X-I)^{p-1}\) for an endomorphism \(X\) with \(X^p=I\); hence this power vanishes because \((T^j-I)^{p-1}=0\). Vectors \((v,0)\) also have \(p\)-th power one. Thus the exponent is \(p\).

A vector \((v,0)\) is central exactly when \(Nv=0\). The \(p^b\) such elements give singleton classes, while every other vector has a conjugacy orbit of cardinality \(p\), giving \((p^n-p^b)/p\) classes. For \(j\ne0\), conjugation by vectors shifts the first coordinate by \(\operatorname{im}(I-T^j)=W\). Conjugation by the cyclic generator changes it only within that coset. Thus each of the \((p-1)p^b\) cosets with \(j\ne0\) and \(v\bmod W\) is exactly one class of size \(p^{n-b}\). When \(n-b=1\), merge the two equal sizes in the class-size polynomial.

Let \(\widehat V\) be the group of complex linear characters of \(V\), with \(|\widehat V|=p^n\). The \(T\)-invariant characters are those annihilating \(W\), so there are \(p^b\). Each extends to \(p\) distinct linear characters of \(G_N\) (because the quotient is cyclic of order \(p\)), giving \(p^{b+1}\) characters of degree one. All remaining characters of \(V\) have cyclic orbits of length \(p\), and one irreducible induced character of degree \(p\) corresponds to each orbit. This gives \((p^n-p^b)/p\) characters of degree \(p\). The degree-square sum equals \(p^{n+1}\), independently checking completeness.

Direct multiplication yields \([(v,j),(w,k)]=((I-T^k)v+(T^j-I)w,0)\). Conditioned on \((j,k)=(0,0)\) the bracket is zero; for any other pair, one of the two indicated linear maps is surjective onto \(W\), so the bracket is exactly uniform on \(W\). Consequently one commutator has law \(p^{-2}\delta_0+(1-p^{-2})U_W\). The identity \(U_W*U_W=U_W\) and independence give the stated \(t\)-commutator convolution law. Substituting the two Jordan partitions proves the claimed joint indistinguishability, while their largest parts \(p-1\) and \(2\) prove unequal classes.

## Verification

The standalone checker `checker.py` constructs each Jordan operator over \(\mathbb F_p\), verifies \(T^p=I\), \(N^{p-1}=0\), the image/kernel rank for every nonzero action exponent, and the rank of every conditional commutator map. For two four-dimensional modules at each of \(p=5\) and \(p=7\), it additionally enumerates **all** group conjugacy orbits by generators and compares their exact size multiplicities with the formula. The higher-dimensional examples are checked by finite-field rank identities, not infeasible full group enumeration. Outputs are in `checker_output.txt`, with final line `ALL CHECKS PASS`. The infinite-prime assertion follows from the algebraic proof, not these finite tests.

## Relationship to prior work

Fernández-Alcober and Moretó investigate which **numbers of distinct** character degrees and class sizes finite \(p\)-groups can have, using class-two constructions; they do not assert coincidence of the **full multiplicity vectors** for two groups of different classes together with all surface-word fibers. Mann explicitly notes that three distinct class sizes are compatible with unbounded nilpotency class; that qualitative observation is not new here. Ito and Mann count classes and characters of certain relatively free prime-exponent groups, and O'Brien and Voll give broad Lie-theoretic tools for calculating class and character vectors for groups of nilpotency class below \(p\); their techniques cover general enumeration, but their examined statements do not give this paired simultaneous invariant collision or surface-word law. This result makes no claim that standard Clifford theory, the conjugacy arguments, or Fourier/convolution observations are themselves new.

## Limitations

The class gap grows as \(p\) grows: no unbounded-class claim is made for a fixed prime. The law treats only orientable surface words and the listed coarse character and conjugacy multiplicities, not character tables, all individual conjugacy classes, all group words, or isoclinism. The matched invariants do **not** make the groups isomorphic. A stronger prior theorem on unipotent cyclic-by-elementary-abelian groups might subsume some or all of this joint collision; the original full text of the 2006 Ito–Mann paper was not obtained. 

## References

- G. A. Fernández-Alcober and A. Moretó, *On the number of conjugacy class sizes and character degrees in finite p-groups*, Proc. Amer. Math. Soc., DOI: https://doi.org/10.1090/S0002-9939-01-05946-9. Open author manuscript: https://www.uv.es/777Bx84IiIlPQ==/3.pdf.
- N. Ito and A. Mann, *Counting classes and characters of groups of prime exponent*, Israel J. Math. 156 (2006), 205–220, DOI: https://doi.org/10.1007/BF02773832.
- A. Mann, *Conjugacy class sizes in finite groups*, J. Aust. Math. Soc. 85 (2008), 251–255, DOI: https://doi.org/10.1017/S1446788708000906.
- E. A. O'Brien and C. Voll, *Enumerating classes and characters of p-groups*, arXiv:1203.3050, original public version March 14, 2012. https://arxiv.org/abs/1203.3050.
